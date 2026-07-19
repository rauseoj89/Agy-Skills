---
name: managing-cicd
description: Designs, configures, and maintains CI/CD pipelines for automated build, test, and deployment workflows. Supports GitHub Actions, GitLab CI, and Docker-based pipelines. Use when asked to set up automated builds, configure deployment pipelines, create workflow files, or automate release processes.
version: 1.0.0
tags: [universal, devops, cicd, deployment]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: CI/CD Pipeline Specialist

## 🎯 Objetivo

Design secure, efficient, and robust pipelines, ensuring that all code is validated, compiled, and deployed using least-privilege runners, keyless OIDC authentication, and encrypted secret mappings while preventing Poisoned Pipeline Execution (PPE).

## 🕒 Cuándo usar

- Al estructurar scripts de compilación, test y despliegue automatizados.
- Al crear o modificar archivos de workflow (ej: `.github/workflows/main.yml`, `.gitlab-ci.yml`).
- Al configurar despliegues en múltiples entornos (dev, staging, producción).
- Al integrar escaneos de dependencias o de vulnerabilidad SAST/SCA.

## 🛡️ Principios Universales

1. **Poisoned Pipeline Execution (PPE) Prevention (CICD-SEC-4):** Force branch protection rules. Avoid running forks with write access or access to secrets.
2. **Least Privilege Identity & Access (CICD-SEC-2):** Restrict runner token permissions by default. Pin third-party steps to static SHA hashes.
3. **No Hardcoded Secrets**: Inject credentials at runtime via environment variables or vault keys.
4. **Vulnerability Scanning**: Automatically run dependency auditing and static analysis inside the pipeline.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ejecutar comandos de verificación de YAML locales
# Subir cambios al repositorio git
```

### ▶️ Si estás en Hermes Agent:

```python
# Modificar los archivos del pipeline usando las herramientas de edición
workflow_data = read_file(path=".github/workflows/main.yml")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP filesystem para actualizar el archivo de workflow de CI/CD
await filesystem.writeFile(".github/workflows/deploy.yml", yamlContent);
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Pide al usuario que configure los secretos en los ajustes del repositorio:
# "Agrega el secreto API_KEY en la configuración de GitHub/GitLab."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera la configuración de CI/CD YAML completa.
2. Pide al usuario: "Crea el archivo `.github/workflows/deploy.yml` y pega este contenido".
3. Proporciona instrucciones sobre cómo configurar los secretos de forma manual en la interfaz del proveedor.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Crear archivo de workflow | write_to_file() | Mostrar YAML en el chat para guardar |
| Configurar secretos | Usar herramientas de configuración de repo | Pedir al usuario configurar secretos en UI (GitHub/GitLab) |
| Ejecutar pipeline local | terminal() con `act` o similar | Pedir al usuario que haga commit y push para validar en remoto |

---

## ✅ Verificación

- El workflow de CI/CD tiene habilitada la cancelación de compilaciones obsoletas (concurrency).
- Los runners están configurados con permisos de sólo lectura por defecto.
- No hay secretos en texto plano.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
