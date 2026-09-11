# Bicep Learning Path — Infrastructure as Code on Azure

**Goal:** Deploy and manage Azure infrastructure with Bicep.  
**Note:** Learn Terraform first — Bicep is Azure-only and easier once you understand IaC concepts.  
**Estimated time:** 2–3 weeks (1–2 hours/day)

---

## Overview

| # | Topic | Status |
|---|---|---|
| 1 | Fundamentals | ⬜ |
| 2 | Bicep on Azure | ⬜ |
| 3 | Modules | ⬜ |
| 4 | Real Projects | ⬜ |

---

## Step 1 — Fundamentals
**Estimated time:** Week 1

### Setup (Day 1)

```bash
az bicep install
az bicep version    # verify
```

Install the VS Code extension: search **Bicep** in the Extensions panel.

---

### What Bicep is

Bicep is Microsoft's own language for deploying Azure resources. It compiles to ARM templates (Azure's native format) but is much easier to read and write.

```
You write Bicep  →  compiles to ARM JSON  →  Azure creates the resources
```

---

### Your first Bicep file

Create a file called `main.bicep`:

```bicep
// Parameters — like variables in Terraform
param location string = resourceGroup().location
param projectName string

// Resource — storage account
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sa${projectName}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true    // Data Lake Gen2
  }
}

// Output
output storageAccountName string = storageAccount.name
```

**Deploy it:**
```bash
# Create resource group first
az group create --name rg-learning --location westeurope

# Deploy the Bicep file
az deployment group create \
  --resource-group rg-learning \
  --template-file main.bicep \
  --parameters projectName=rezadata
```

---

### Parameters — like variables

```bicep
// Required — must be passed at deploy time
param projectName string

// With default value — optional
param location string = resourceGroup().location
param environment string = 'dev'

// With allowed values
@allowed(['dev', 'test', 'prod'])
param environment string = 'dev'

// Secure — hides value in logs
@secure()
param sqlAdminPassword string
```

Pass parameters at deploy time:
```bash
az deployment group create \
  --resource-group rg-learning \
  --template-file main.bicep \
  --parameters projectName=rezadata environment=dev
```

Or use a parameters file (`main.parameters.json`):
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "projectName": { "value": "rezadata" },
    "environment": { "value": "dev" }
  }
}
```

---

### Conditions and loops

```bicep
// Condition — only create firewall in prod
param createFirewall bool = false

resource firewall 'Microsoft.Network/azureFirewalls@2023-04-01' = if (createFirewall) {
  name: 'fw-main'
  location: location
  // ...
}

// Loop — create multiple storage containers
var containers = ['raw', 'processed', 'curated']

resource blobContainers 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = [for container in containers: {
  name: '${storageAccount.name}/default/${container}'
}]
```

---

### Bicep vs Terraform — syntax comparison

Same result, different syntax:

**Terraform:**
```hcl
resource "azurerm_storage_account" "datalake" {
  name                     = "sadatalake"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}
```

**Bicep:**
```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sadatalake'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
  }
}
```

| | Terraform | Bicep |
|---|---|---|
| Works with | Any cloud | Azure only |
| Syntax | HCL | Bicep (close to JSON) |
| State management | Built-in | Azure handles it |
| Job market | Very high demand | Azure-focused roles |

---

## Step 2 — Bicep on Azure
**Estimated time:** Week 2

### Common Data Engineering resources

```bicep
param location string = resourceGroup().location
param projectName string

@secure()
param sqlAdminPassword string

// Storage Account — Data Lake Gen2
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sa${projectName}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
  }
}

// Azure Data Factory
resource dataFactory 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: 'adf-${projectName}'
  location: location
  identity: {
    type: 'SystemAssigned'
  }
}

// Azure SQL Server
resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: 'sql-${projectName}'
  location: location
  properties: {
    administratorLogin: 'sqladmin'
    administratorLoginPassword: sqlAdminPassword
  }
}

// Azure SQL Database
resource sqlDatabase 'Microsoft.Sql/servers/databases@2022-05-01-preview' = {
  parent: sqlServer    // parent links child to parent — Bicep handles dependency
  name: 'sqldb-${projectName}'
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
}
```

---

### Referencing other resources

```bicep
// Use the resource's symbolic name to reference its properties
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sadatalake'
  location: location
  // ...
}

// Reference it in another resource
output storageId string = storageAccount.id
output storageEndpoint string = storageAccount.properties.primaryEndpoints.blob
```

---

### Tags

```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sadatalake'
  location: location
  tags: {
    environment: 'dev'
    project: projectName
    owner: 'reza'
    managedBy: 'bicep'
  }
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
```

---

## Step 3 — Modules
**Estimated time:** Week 3

A module in Bicep is a separate `.bicep` file you call from `main.bicep` — same concept as Terraform modules.

```
modules/
└── storage.bicep

main.bicep
```

```bicep
// modules/storage.bicep
param projectName string
param location string

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'sa${projectName}'
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
  properties: { isHnsEnabled: true }
}

output storageAccountName string = storageAccount.name
output storageAccountId string = storageAccount.id
```

```bicep
// main.bicep — call the module
module storage './modules/storage.bicep' = {
  name: 'storageDeployment'
  params: {
    projectName: projectName
    location: location
  }
}

// Use the module's output
output storageId string = storage.outputs.storageAccountId
```

---

## Step 4 — Real Projects
**Do these in order — each builds on the last.**

| Project | What you practice |
|---|---|
| 1. Resource group + storage account | Basics: deploy, parameters, outputs |
| 2. Full data lake: ADLS + 3 containers using a loop | Parameters, loops |
| 3. ADLS + ADF + SQL Database in one file | Multiple resources, parent/child |
| 4. Split into modules | Modules, reusability |
| 5. Add conditions — create firewall only in prod | Conditional resources |

---

## Key commands

```bash
az login                                           # sign in to Azure
az account show                                    # verify account
az group create --name rg-name --location westeurope
az deployment group create \
  --resource-group rg-name \
  --template-file main.bicep \
  --parameters projectName=myproject
az bicep build --file main.bicep                   # compile to ARM JSON
az deployment group show \
  --resource-group rg-name \
  --name main                                      # show deployment status
```

---

## Resources

| Resource | Type | Cost |
|---|---|---|
| [Microsoft Bicep docs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) | Docs | Free |
| [Bicep Playground](https://aka.ms/bicepdemo) | Interactive | Free |
| [Microsoft Learn — Bicep path](https://learn.microsoft.com/en-us/training/paths/fundamentals-bicep/) | Course | Free |

---

✅ **You are ready when you can:**
- Write a Bicep file that deploys ADLS + ADF + SQL Database
- Use parameters, conditions, and loops
- Split a large deployment into modules
- Explain the difference between Bicep and Terraform to a colleague
