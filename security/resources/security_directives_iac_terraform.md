# Hardened Terraform & Infrastructure as Code (IaC) Security Directives

When writing, generating, or auditing Infrastructure as Code (IaC) configurations, the following security standards must be strictly enforced:

### 1. Secure State Operations
Terraform State files store cloud resource details in plaintext, including database credentials and API keys.
- **Rule:** Never save state files locally in git repositories. Use a remote backend (e.g., S3, Azure Blob, Terraform Cloud) with encryption at rest and strict access controls.

### 2. Encryption and Public Access
Cloud storage and database instances must be isolated from public networks.
- **Rule:** Set `publicly_accessible = false` on RDS resources.
- **S3 Buckets:** Enforce default server-side encryption and block public access:
  ```hcl
  resource "aws_s3_bucket_public_access_block" "block" {
    bucket                  = aws_s3_bucket.main.id
    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
  }
  ```
