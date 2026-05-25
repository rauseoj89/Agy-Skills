# 🚀 Launching Agy-Skills: Hardened Blueprints for Local AI Agent Workflows

![Agy-Skills Cover Banner](agy_skills_cover.png)

## 📌 Elevator Pitch
If you use local AI agents (Roo Code, Cline, Claude Code) or local LLMs (Ollama/Gemma) to build code and automate systems, you know the biggest risk: **accidental security exposure**. A single unparameterized script or path traversal error can compromise your local machine or server.

**Agy-Skills** is an open-source library of standardized, security-first **AI Skill Blueprints** engineered on the **"Hardened Vanilla"** standard. These blueprints ensure that your AI assistants execute container setups, database queries, and system runbooks with zero plain-text leaks, strict non-root isolation, and robust atomic write checks.

---

## 🛠️ The "Hardened Vanilla" Framework
Why use **Agy-Skills**? Every blueprint enforces three core constraints:
1.  **Least-Privilege Containment:** AI-generated system Dockerfiles are strictly barred from root execution context.
2.  **Scrubbed Log Diagnostics:** The agent automatically redacts database credentials, SSH keys, or API tokens using `********` mask filters.
3.  **Atomic File Workflows:** File writes utilize a strict temp-then-rename pipeline to prevent configuration corruption.

---

## 📂 Included Blueprints

*   **`operations/executing_sop_and_runbooks.md`**  
    *The Task Master:* Guides agents through a secure **Validate $\rightarrow$ Execute $\rightarrow$ Verify** sequence to run complex SOPs, deployments, and backups step-by-step.
*   **`devops/managing_containers.md`**  
    *The Sandbox Specialist:* Formulates multi-stage Docker builds and audits active containers while isolating ports.
*   **`security/managing_secrets_and_vaults.md`**  
    *The Lockbox:* Audits `.gitignore` scopes, sanitizes diagnostic logs, and secures integrations with secret vaults.
*   **`data/analyzing_data.md`**  
    *The Data Clean Room:* Cleans messy spreadsheet telemetry, handles missing values, and outputs structured analytical tables.
*   **`operations/managing_system_operations.md`**  
    *The SysAdmin:* Organizes raw directory layouts, clears duplicates via file hashing, and runs secure compressed backup schedules.

---

## 🚀 Getting Started in 60 Seconds
Integrating these skills into your local agent environment is simple:

1.  **Clone the Blueprints:**
    ```bash
    git clone https://github.com/rauseoj89/Agy-Skills.git
    ```
2.  **Load the Instructions:** Copy the markdown skill file (e.g., `managing_containers.md`) and paste it directly into your AI client's custom instruction folder (like `.roo-code-instructions` or `.clinerules` in your target repo).
3.  **Deploy Offline:** Run it completely locally using your server-side Ollama/Gemma model with zero third-party dependencies!

---
🔗 **Explore the code on GitHub:** [rauseoj89/Agy-Skills](https://github.com/rauseoj89/Agy-Skills)  
*Contributions are welcome! Open an issue or submit a Pull Request to help expand the community standard for secure AI automation.*
