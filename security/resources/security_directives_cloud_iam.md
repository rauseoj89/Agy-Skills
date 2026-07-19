# Hardened Cloud IAM Security Directives

When writing, generating, or auditing IAM configurations for AWS, GCP, or Azure, the following security standards must be strictly enforced:

### 1. Least Privilege Policies
Broad admin wildcards allow unauthorized lateral movement.
- **Rule:** Never define permissions with wildcard actions on wildcard resources (e.g., `Effect: Allow, Action: *, Resource: *`).
- **Resource Constraints:** Always scope actions to exact resource ARNs or tags wherever supported.

### 2. IAM Roles for Compute
Saving API keys or user access keys inside servers or containers is prohibited.
- **Rule:** Use instance profiles or IAM Roles for Service Accounts (IRSA) to grant permissions to workloads dynamically (e.g., AWS ECS Task Role, GCP Service Account binding).
