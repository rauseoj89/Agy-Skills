---
name: "Managing CI/CD"
description: "Configures automated build, lint, scan, test, and deploy pipelines using GitHub Actions or GitLab CI."
category: "generic/devops"
tools_required: ["vault-bridge-mcp"]
last_updated: 2026-06-15
---

# 🧠 Skill: CI/CD Pipeline Specialist

## 🎯 Goal
Design and maintain secure build and release workflows, enforcing least-privilege runners, dynamic secrets injection, and static dependency vulnerability scans.

## 📊 Inputs Required
- Target repository layout and language specifications.
- Required secrets (mapped dynamically to pipeline configurations).
- Pinned dependency versions.

## 🛠️ Step-by-Step Instructions
1. **Pipeline Architecture & Linting**:
   - Establish workflow blocks (Lint -> Build -> Test -> Security Scan -> Deploy).
   - Ensure lint and formatting checks run automatically on all pull request triggers.
2. **Secrets Mapping & Hardening**:
   - Never write credentials, SNMP keys, or API tokens in plaintext inside pipeline config files.
   - Load credentials dynamically using platform secrets integrations or Vault Bridge paths.
3. **Runner Version Pinning**:
   - Pin third-party workflow actions to static Git commit SHA hashes instead of mutable tags (e.g. use `actions/checkout@8ade135...` instead of `@v4`).
4. **Vulnerability & CVE Scans**:
   - Integrate automated image scanners (like Trivy) or dependency CVE scanners (like `pip-audit`) directly in the build pipeline.
   - Block pipelines if any CRITICAL severity CVEs are detected.

## 🛡️ Verification & Security Checklist
1. **Secrets Isolation**: Confirm that zero plaintext secrets appear in repository workflow configurations.
2. **Lockfile Enforcement**: Verify that builds are reproducible by committing lockfiles and enforcing lockfile dependency resolution.
3. **Verification Scans**: Ensure that image scanning reports exit with non-zero codes on CVE violations to prevent dirty builds from deploying.

---
*Created by Efficiency Core*
