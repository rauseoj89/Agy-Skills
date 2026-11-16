# 🛡️ Agy-Skills: Hardened Blueprints for Local AI Agent Workflows

![Agy-Skills Cover Image](agy_skills_cover.png)

Welcome to **Agy-Skills**! This repository contains a curated collection of standardized, security-first **AI Skill Blueprints** (written in Markdown) designed to guide advanced coding agents (such as Roo Code, Cline, Claude Code, GitHub Copilot, Cursor, Hermes, and Antigravity) and local LLMs (such as Ollama, Gemma 2, Llama 3) in executing operational and infrastructure workflows safely.

---

## 🏗️ The "Hardened Vanilla" Standard
All skills in this repository are engineered to enforce high-security postures during execution:
1.  **Least Privilege Runtime:** All system scripts, service containers, and processes are strictly configured to run under limited-privilege, non-root system accounts.
2.  **Zero plain-text Secrets:** No credentials, API tokens, database connection strings, or private keys are ever hardcoded or printed to the screen/logs. Output is dynamically masked using `********` patterns.
3.  **Atomic Write Operations:** File operations (like generating spreadsheets, Word documents, or writing configurations) utilize temp-then-rename atomic write workflows to prevent file corruption.
4.  **Path Traversal Protection:** All file reading/writing tools must sanitize paths, verify offsets, and reject traversal attempts trying to step outside authorized workspaces.

---

## 🚀 Multi-Agent & Universal Compatibility
Every skill in this library has been upgraded to be **Universal**:
- Compatible with Hermes, Antigravity, Cline, Roo-Code, Copilot, and Cursor.
- Includes specific execution directives per agent.
- Features standard manual fallbacks in case advanced tools (read_file, terminal access) are not available.

To use:
1. Copy the contents of the chosen skill file (e.g., `executing_sop_and_runbooks.md`).
2. Paste it into your agent's system prompt or configuration rules (e.g., `.clinerules`, `.roo-code-instructions`, or custom system fields).
3. If the agent lacks direct tool access, follow the **Fallback** instructions provided inside the skill.

---

## 📂 Active Skill Library

The repository is structured logically by domain categories:

```bash
agy-skills/
├── README.md
├── MIGRATION.md                          # Migration history and universal guidelines
├── TEMPLATE-universal-skill.md           # Template for new universal skills
├── agy_skills_cover.png                  # Project cover banner
├── data/
│   ├── analyzing_data.md                 # Cleanup metrics logs & compile Excel summaries
│   └── designing_apis.md                 # REST/GraphQL endpoints design & OpenAPI 3.1 specs
├── devops/
│   ├── browser_testing.md                # E2E browser automation & Lighthouse audits
│   ├── docker_build_strategies.md        # BuildKit cache mounts, secret injection & multi-stage builds
│   ├── docker_compose_patterns.md        # Compose v2, readiness dependencies & sidecar healthchecks
│   ├── docker_destructive_guardrails.md  # 3-tier risk classification & confirmation gates for Docker
│   ├── docker_project_foundations.md     # Scaffolding the foundational triad (.dockerignore, Dockerfile, compose)
│   ├── managing_cicd.md                  # GitHub Actions, secrets mapping & pinned runners
│   ├── managing_containers.md            # Multi-stage, non-root Docker builds & diagnostics
│   ├── managing_dependencies.md          # Dependency CVE audits, exact pinning & SRI hashes
│   ├── managing_git_workflows.md         # Interactive semantic commits, logical splitting & PR workflows
│   ├── profiling_performance.md          # Query EXPLAIN tuning, browser traces & Core Web Vitals
│   └── qa.md                             # Unit/E2E testing, negative exploit matrix & Trivy scans
├── marketing/
│   └── seo_audit.md                      # Technical SEO audits, meta validation & bilingual reports
├── network/
│   └── general_network_audit.md          # Hardening management protocols & vetting unused ports
├── operations/
│   ├── architech.md                      # Modular software/UI blueprints, OpenAPI 3.1 & data flows
│   ├── client_onboarding.md              # Structured client onboarding lifecycle
│   ├── coder.md                          # Hardened Python/PHP/JS implementation & modern web standards
│   ├── creating_agy_mcps.md              # Automate blueprinting & git deployment of custom MCP servers
│   ├── creating_agy_skills.md            # Automate blueprinting & git deployment of custom Agy-skills
│   ├── documenting_sessions.md           # Private daily reviews & .gitignore automation
│   ├── executing_sop_and_runbooks.md     # Step-by-step interactive runbook execution
│   ├── idea_assessment.md                # Feasibility, spikes & bounded solution shaping (Go/Clarify/Stop)
│   ├── legal_compliance_drafting.md      # Attorney-grade contracts, DPAs, BAAs & CC0 legal templates
│   ├── managing_m365.md                  # Administer M365 users, licenses, and security
│   ├── managing_system_operations.md     # Sorting folder assets & executing tar backups
│   ├── managing_tasks.md                 # Eisenhower prioritization, risk scoring & sprint Gantt plans
│   ├── monitoring_and_alerting.md        # System health checks, DB pool metrics & alert thresholds
│   ├── patch_management.md               # Govern patch windows and rollback policies
│   ├── powershell_automation.md          # Write, test, and deploy PowerShell automation
│   ├── researching_topics.md             # Tier-1 technical research & comparative evaluation matrices
│   ├── skill_creator.md                  # Standardize & generate local agent SKILL.md directories
│   ├── spec_driven_development.md        # Spec-Kit workflow (spec.md -> plan.md -> tasks.md)
│   ├── systematic_debugging.md           # Root-cause-first debugging (Assess -> Fix -> Test)
│   └── writing_documentation.md          # Versioned manuals, release notes, FAQs & sanitized guides
└── security/
    ├── database_management.md            # PostgreSQL schemas, indices, permissions & migrations
    ├── git_secret_audit.md               # Audit Git history, sanitize tracked credentials & .gitignore rules
    ├── host_security_audit.md            # Linux VPS audit, SSH hardening, Fail2ban sync & firewall
    ├── incident_response.md              # Triage, contain, investigate, and recover from incidents
    ├── managing_secrets_and_vaults.md    # In-memory secrets injection & vault bridge operations
    ├── sec_engineer.md                   # Hardened Vanilla enforcement, STRIDE & adversarial disproof
    ├── security_audit.md                 # Autonomous 6-phase coverage-led vulnerability hunting harness
    └── resources/                        # Progressive disclosure language/platform directives
```

### 🧠 Summarized Skill Index

*   **[Security Engineer](security/sec_engineer.md):** Senior Security Solutions Architect and Lead DevSecOps Engineer. Enforces security mandates, STRIDE modeling, and holds Veto Power.
*   **[Autonomous Security Audit Harness](security/security_audit.md):** 6-phase coverage-led vulnerability discovery harness (Cloudflare methodology): reconnaissance, coverage ledger mapping, isolated hunting, adversarial disproof, schema validation, and reporting.
*   **[Linux Host Security Specialist](security/host_security_audit.md):** Audits Linux VPS, servers, and host OS security configurations (SSH hardening, firewall vs. listening sockets alignment, Fail2ban/CrowdSec jail sync).
*   **[Specification-Driven Development](operations/spec_driven_development.md):** Eliminates agent drift and hallucinated assumptions by enforcing the Spec-Kit progression (`spec.md` $\rightarrow$ `plan.md` $\rightarrow$ `tasks.md`).
*   **[Systematic Debugging](operations/systematic_debugging.md):** Root-cause-first debugging harness enforcing reproduction before modification, surgical minimal patching, and regression testing (**Assess $\rightarrow$ Fix $\rightarrow$ Test**).
*   **[Idea & Feasibility Assessment](operations/idea_assessment.md):** Pre-implementation evaluation and technical spike framework delivering evidence-backed scorecards (**Go**, **Clarify**, **Stop**).
*   **[Legal & Compliance Drafting](operations/legal_compliance_drafting.md):** Generates attorney-drafted contracts, terms of use, privacy policies, DPAs, and HIPAA BAAs based on General Legal CC0 standards.
*   **[Docker Build Strategies](devops/docker_build_strategies.md):** Architects and optimizes production Dockerfiles using BuildKit cache mounts, secret mounts, and distroless minimal runtimes.
*   **[Docker Compose Patterns](devops/docker_compose_patterns.md):** Manages multi-container stacks using canonical `compose.yaml`, readiness dependencies (`condition: service_healthy`), and healthcheck sidecars.
*   **[Docker Destructive Guardrails](devops/docker_destructive_guardrails.md):** Enforces 3-tier risk classification and explicit user confirmation gates before destructive Docker commands.
*   **[Docker Project Foundations](devops/docker_project_foundations.md):** Scaffolds the foundational container triad (`.dockerignore`, `Dockerfile`, `compose.yaml`) with zero host toolchain pollution.
*   **[SEO Audit](marketing/seo_audit.md):** Conducts technical and on-page SEO evaluations, generates professional bilingual PDF and Markdown reports.
*   **[SOP & Runbooks Orchestrator](operations/executing_sop_and_runbooks.md):** Guides the agent through a safe, sequential **Validate $\rightarrow$ Execute $\rightarrow$ Verify** lifecycle when executing complex technical SOPs, database migrations, or server maintenance scripts.
*   **[Session Review Documenter](operations/documenting_sessions.md):** Tracks local work sessions, hides the private `CHG-Review` logs directory, and automatically manages `.gitignore` rules to keep diaries private.
*   **[Docker Container Specialist](devops/managing_containers.md):** Formulates highly optimized, secure multi-stage Dockerfiles and Compose files, verifying process states, maps, and volumes.
*   **[Secrets & Credentials Guard](security/managing_secrets_and_vaults.md):** Audits `.gitignore` files, runs dynamic log scrubbers, and safely retrieves or rotates credentials using secret vaults.
*   **[Git Secret Auditor](security/git_secret_audit.md):** Audits local Git repositories, detects tracked credentials, and safely purges sensitive data from commit history.
*   **[Data Analyst & Processing Suite](data/analyzing_data.md):** Ingests and cleans multi-format datasets (CSV, Excel, PDF, Word, Logs), calculates statistical metrics via `data-analyst-mcp`, and compiles structured summaries and spreadsheets.
*   **[Personal System Administrator](operations/managing_system_operations.md):** Automates repetitive folder cleanups, manages local compressed backup files (retaining max 5 history logs), and verifies disk allocations.
*   **[Agy-Skills Automator](operations/creating_agy_skills.md):** Generates and deploys new security-first operational skill files inside the local Agy-Skills repository.
*   **[Agy-MCP Automator](operations/creating_agy_mcps.md):** Designs, blueprints, and structures custom Model Context Protocol (MCP) server configurations.
*   **[Browser Testing Specialist](devops/browser_testing.md):** Automates browser E2E workflows, visual regressions, and Lighthouse audits.
*   **[Database Security Administrator](security/database_management.md):** Governs database schemas, indexes, role separation, and DDL migrations.
*   **[CI/CD Pipeline Specialist](devops/managing_cicd.md):** Configures automated pipelines, dependency audits, and secrets mapping.
*   **[Git Workflow Specialist](devops/managing_git_workflows.md):** Enforces interactive semantic commits, logical commit group splitting, scoped staging, branching strategies, and PR reviews.
*   **[API Architect & Designer](data/designing_apis.md):** Designs RESTful and GraphQL API contracts, schemas, and OpenAPI 3.1 YAML specifications.
*   **[General Network Auditor](network/general_network_audit.md):** Audits and hardens network configurations, management protocols, and ports.
*   **[Client Onboarding Specialist](operations/client_onboarding.md):** Coordinates tenant, network discovery, credential vaulting, and monitoring baseline setups during client onboarding.
*   **[Microsoft 365 Administrator](operations/managing_m365.md):** Governs user provisioning, deprovisioning workflows, licensing, MFA checks, and Conditional Access policies.
*   **[Patch Management Specialist](operations/patch_management.md):** Controls patch inventory, risk gating, pre-patch backups, staged deployment, and rollback configurations.
*   **[PowerShell Automation Specialist](operations/powershell_automation.md):** Scripting authority enforcing strict parameter validation, SecureString management, and Pester tests.
*   **[Incident Response Specialist](security/incident_response.md):** Governs triage, containment, log preservation, and recovery workflows during security incidents.
*   **[Senior Architect](operations/architech.md):** Designs modular software interfaces, native HTML/CSS blueprints, OpenAPI 3.1 contracts, and security-first data flows.
*   **[Lead Engineer](operations/coder.md):** Executes hardened Python, PHP, HTML, and JavaScript implementation with parameterized queries, redacted errors, and non-root containers.
*   **[Dependency & Supply Chain Manager](devops/managing_dependencies.md):** Audits npm, pip, and Composer dependencies for CVEs, enforces exact version pinning, and generates SRI hashes.
*   **[Project Manager & Task Coordinator](operations/managing_tasks.md):** Prioritizes backlogs via the Eisenhower Matrix, scores risks, and builds sprint plans with Mermaid Gantt timelines.
*   **[Systems Observer & Alert Configurator](operations/monitoring_and_alerting.md):** Configures read-only health checks, DB connection pool monitors, and CPU/memory/disk alert thresholds.
*   **[Performance & Profiling Specialist](devops/profiling_performance.md):** Profiles SQL queries with `EXPLAIN (ANALYZE, BUFFERS)`, captures browser traces, and optimizes Core Web Vitals.
*   **[Quality Assurance Engineer](devops/qa.md):** Runs Pytest/PHPUnit suites, Chrome DevTools E2E/Lighthouse audits, Trivy container scans, and negative exploit testing.
*   **[Research & Competitive Analyst](operations/researching_topics.md):** Gathers Tier-1 technical documentation, vets sources, and compiles objective comparison matrices.
*   **[Skill Creator](operations/skill_creator.md):** Standardizes and generates modular `SKILL.md` directories with compliant YAML frontmatter and security guardrails.
*   **[Technical Documenter & Writer](operations/writing_documentation.md):** Authors version-controlled manuals, release notes, and FAQs with zero leaked secrets, IPs, or local paths.

---
_Feel free to open Pull Requests to contribute new blueprints, refine checklists, or add vendor-specific system configurations!_

---
**Created by:** Jimmy Rauseo  
**Powered by:** Antigravity / Gemini

