# Terraform Learning Path — Infrastructure as Code on Azure

**Goal:** Deploy and manage Azure infrastructure with Terraform in a professional Data Engineering environment.  
**Estimated time:** 4 weeks (1–2 hours/day)

---

## Overview

| # | Topic | Status |
|---|---|---|
| 1 | Fundamentals | ⬜ |
| 2 | Terraform on Azure | ⬜ |
| 3 | State & Modules | ⬜ |
| 4 | Real Projects | ⬜ |

---

## Step 1 — Fundamentals
**Estimated time:** Weeks 1–2

### Setup (Day 1)

```bash
# Install Terraform on Mac
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
terraform -version    # verify

# Install Azure CLI
brew install azure-cli
az login              # opens browser to sign in
az account show       # verify you're connected
```

Install the VS Code extension: search **HashiCorp Terraform** in the Extensions panel.

---

### Core concepts

| Concept | What it is |
|---|---|
| **Provider** | Plugin that connects Terraform to a cloud (Azure, AWS, GCP) |
| **Resource** | A single piece of infrastructure (storage account, VM, database) |
| **State** | A file Terraform keeps to track what it has already created |

---

### Your first Terraform file

Create a folder and a file called `main.tf`:

```hcl
# Tell Terraform to use the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# Configure the Azure provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "main" {
  name     = "rg-learning"
  location = "West Europe"
}
```

**Run it:**
```bash
terraform init      # download the Azure provider plugin
terraform plan      # preview what will be created (no changes yet)
terraform apply     # actually create the resources
terraform destroy   # delete everything Terraform created
```

> Always run `terraform plan` before `terraform apply` — it shows you exactly what will change. Never apply without reading the plan.

---

### Variables — don't hardcode values

```hcl
# variables.tf
variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "West Europe"
}

variable "project_name" {
  description = "Used as a prefix for all resource names"
  type        = string
}
```

```hcl
# main.tf — use variables with var.variable_name
resource "azurerm_resource_group" "main" {
  name     = "rg-${var.project_name}"
  location = var.location
}
```

```bash
# Pass variables at runtime
terraform apply -var="project_name=reza-data"

# Or use a .tfvars file (like .env but for Terraform)
# terraform.tfvars
project_name = "reza-data"
```

---

### Outputs — read values after creation

```hcl
# outputs.tf
output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "resource_group_id" {
  value = azurerm_resource_group.main.id
}
```

```bash
terraform output                          # show all outputs
terraform output resource_group_name      # show one output
```

---

### Standard file structure

```
my-infra/
├── main.tf           # resources
├── variables.tf      # variable declarations
├── outputs.tf        # outputs
├── terraform.tfvars  # variable values (never commit if contains secrets)
└── .gitignore
```

`.gitignore` for Terraform:
```
.terraform/
terraform.tfstate
terraform.tfstate.backup
*.tfvars
```

---

## Step 2 — Terraform on Azure
**Estimated time:** Weeks 2–3

### The 5 Azure resources you'll use most as a Data Engineer

```hcl
# 1. Resource Group — container for everything else
resource "azurerm_resource_group" "main" {
  name     = "rg-${var.project_name}"
  location = var.location
}

# 2. Storage Account — Azure Data Lake Storage (ADLS)
resource "azurerm_storage_account" "datalake" {
  name                     = "sa${var.project_name}datalake"  # globally unique, no dashes
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true    # enables Data Lake Gen2
}

# 3. Storage Container (like a folder in ADLS)
resource "azurerm_storage_container" "raw" {
  name                  = "raw"
  storage_account_name  = azurerm_storage_account.datalake.name
  container_access_type = "private"
}

# 4. Azure Data Factory
resource "azurerm_data_factory" "main" {
  name                = "adf-${var.project_name}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

# 5. Azure SQL Database
resource "azurerm_mssql_server" "main" {
  name                         = "sql-${var.project_name}"
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_user
  administrator_login_password = var.sql_admin_password
}

resource "azurerm_mssql_database" "main" {
  name      = "sqldb-${var.project_name}"
  server_id = azurerm_mssql_server.main.id
  sku_name  = "Basic"
}
```

---

### Referencing other resources

Resources can reference each other — Terraform handles creation order automatically:

```hcl
resource "azurerm_storage_account" "datalake" {
  name                = "sadatalake"
  resource_group_name = azurerm_resource_group.main.name     # references the RG
  location            = azurerm_resource_group.main.location
  # ...
}
```

Format: `resource_type.resource_name.attribute`

---

### Tagging — always tag your resources

```hcl
resource "azurerm_resource_group" "main" {
  name     = "rg-${var.project_name}"
  location = var.location

  tags = {
    environment = "dev"
    project     = var.project_name
    owner       = "reza"
    managed_by  = "terraform"
  }
}
```

> Tags let you filter costs in Azure Cost Management. Always tag resources in a team project.

---

## Step 3 — State & Modules
**Estimated time:** Week 4

### Remote State — for team projects

Terraform writes a `terraform.tfstate` file after every `apply`. In a team, everyone needs the same state file — store it in Azure Blob Storage.

```hcl
# backend.tf
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-terraform-state"
    storage_account_name = "saterraformstate"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}
```

```bash
# Create the storage manually once
az group create --name rg-terraform-state --location westeurope
az storage account create --name saterraformstate --resource-group rg-terraform-state --sku Standard_LRS
az storage container create --name tfstate --account-name saterraformstate

# Then init
terraform init
```

---

### Modules — reusable infrastructure blocks

A module is a folder of `.tf` files you call like a function — write once, reuse everywhere.

```
modules/
└── storage/
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

```hcl
# modules/storage/main.tf
resource "azurerm_storage_account" "this" {
  name                     = var.name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}
```

```hcl
# main.tf — call the module
module "datalake" {
  source              = "./modules/storage"
  name                = "sadatalake"
  resource_group_name = azurerm_resource_group.main.name
  location            = var.location
}
```

---

## Step 4 — Real Projects
**Do these in order — each builds on the last.**

| Project | What you practice |
|---|---|
| 1. Resource group + storage account | Basics: `init`, `plan`, `apply`, `destroy` |
| 2. Add variables and outputs | Variables, tfvars, outputs |
| 3. Full data lake: ADLS + 3 containers (raw/processed/curated) | Multiple resources, references |
| 4. Store state in Azure Blob Storage | Remote state, team workflow |
| 5. Extract storage into a module and reuse it | Modules |
| 6. Full pipeline environment: ADLS + ADF + SQL Database | End-to-end project |

---

## Key commands

```bash
terraform init       # download providers
terraform plan       # preview changes
terraform apply      # create/update resources
terraform destroy    # delete all resources
terraform output     # show outputs
terraform fmt        # auto-format your .tf files
terraform validate   # check syntax
```

---

## Resources

| Resource | Type | Cost |
|---|---|---|
| [Terraform Azure Provider docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) | Docs | Free |
| [HashiCorp Learn — Terraform on Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started) | Tutorial | Free |
| [freeCodeCamp Terraform course](https://www.youtube.com/watch?v=SLB_c_ayRMo) | Video | Free |

---

✅ **You are ready when you can:**
- Write a Terraform config that creates a full Azure data environment (ADLS + ADF + SQL)
- Use variables, outputs, and remote state
- Extract reusable infrastructure into a module
- Explain what state is and why it matters in a team
