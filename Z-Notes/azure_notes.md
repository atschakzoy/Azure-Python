# Azure Entra ID Notes

Azure Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based identity and access management service. The main things it does:

## Identity Management
- Stores and manages user accounts, groups, and service principals
- Acts as the "source of truth" for who is allowed into your systems

## Authentication
- Handles sign-in for users (passwords, MFA, passwordless options like FIDO2)
- Supports Single Sign-On (SSO) — log in once, access many apps without re-authenticating

## Authorization / Access Control
- Role-Based Access Control (RBAC) — assign roles to users/groups to control what they can do
- Conditional Access — enforce policies like "require MFA if signing in from outside the office"

## App Registration & API Access
- Apps register with Entra ID to get tokens (OAuth 2.0 / OpenID Connect)
- Controls which apps can call which APIs on behalf of which users

## B2B / B2C
- B2B: invite external partners/contractors as guest users
- B2C: let end customers sign up with social logins (Google, Facebook, etc.)

## Device Management (via Intune integration)
- Register and join devices (Windows, iOS, Android) so only compliant devices can access resources

## Monitoring & Security
- Sign-in logs, risky user detection, Identity Protection alerts
- Integrates with Microsoft Sentinel for SIEM

---

**Summary:** It answers "who are you, are you who you claim to be, and what are you allowed to do?" for everything in the Microsoft/Azure ecosystem.

---

# Azure Hierarchy

Azure has a 4-level management hierarchy, from broadest to most specific:

## 1. Management Groups
- The top level — used to organize multiple subscriptions
- You can apply policies and RBAC here that cascade down to everything below
- A root management group sits above all others (one per Entra ID tenant)
- Good for large orgs with many teams/business units

## 2. Subscriptions
- A billing and trust boundary
- All resources belong to a subscription
- You might have separate subscriptions for prod, dev, and staging
- Each subscription trusts exactly one Entra ID tenant for identity

## 3. Resource Groups
- A logical container for related resources
- Resources must belong to exactly one resource group
- Typically grouped by app, environment, or lifecycle (things you deploy and delete together)
- RBAC and policies can be applied at this level too

## 4. Resources
- The actual things: VMs, storage accounts, databases, app services, etc.
- Always live inside a resource group

## How Policies & Permissions Flow

```
Management Group
    └── Subscription
            └── Resource Group
                    └── Resource
```

Anything assigned at a higher level (policy, RBAC role) **inherits down** automatically. So a policy on a Management Group applies to every subscription, resource group, and resource underneath it — you don't have to set it repeatedly.

**Quick mental model:** Management Groups = org chart, Subscriptions = billing accounts, Resource Groups = project folders, Resources = the actual stuff.

## Management Group Limits
- Up to **10,000 management groups** per tenant
- Maximum **6 levels of depth** (not counting root or subscription level)
- Each management group can have unlimited children
- Each management group has exactly one parent
- There is one root management group per tenant — it can't be moved or deleted

## The Root Management Group
Every Azure account belongs to a **tenant** — your organization's instance of Entra ID (e.g., `yourcompany.onmicrosoft.com`). When Azure sets up your tenant, it automatically creates one Root Management Group. Everything else sits under it:

```
Root Management Group  ← auto-created, one per tenant, can't delete
    ├── Management Group A
    │       └── Subscription 1
    ├── Management Group B
    │       ├── Subscription 2
    │       └── Subscription 3
    └── Subscription 4  ← can sit directly under root too
```

- You can't move or delete it — it's always there
- Every subscription ultimately rolls up to it, no matter how deep your hierarchy is
- Global admins in Entra ID can elevate themselves to manage it
- Any policy or RBAC role assigned at the root applies to **everything** in your tenant — so be careful assigning things there
- It exists so you have one single place to apply org-wide governance without touching every subscription individually
