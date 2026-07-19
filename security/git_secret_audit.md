---
name: git-secret-audit
description: Runs security audits on local Git repositories to detect tracked credentials, analyze .gitignore files, and safely purge secrets from Git history.
version: 1.0.0
tags: [universal, security, git, secrets]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Git Secret Audit & Sanitization

## 🎯 Objetivo

Run security audits on local Git repositories to detect tracked credentials, analyze `.gitignore` files, and safely purge sensitive files (like `.env` or configurations) from Git history without affecting local instances.

## 🕒 Cuándo usar

- Al revisar si se subieron secretos al repositorio remoto por accidente.
- Al verificar y auditar las reglas de `.gitignore`.
- Al limpiar el historial de commits de Git (e.g. usando `git rm --cached` o `git filter-repo`).

## 🛡️ Principios Universales

1. **Secrets Sanitization**: Immediately detect and untrack `.env`, keys, certificates, or databases.
2. **Never Force Destructive Git Purges Without Backup**: Git history rewrite commands (like `git filter-repo`) are dangerous and must be confirmed.
3. **No Plaintext credentials**: Environment configurations must be vaulted, not stored in source code.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ejecutar comandos de Git locales
git ls-files | grep -E "\.env|\.key|\.pem"
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar la terminal para correr checks de git
result = terminal(command="git ls-files", timeout=30)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP git para verificar status o shell para listar archivos
const files = await git.git_status();
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al desarrollador en su terminal local:
# Pide: "Corre 'git ls-files | grep .env' para revisar si el archivo está siendo trackeado."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Pide al usuario que corra los comandos de Git para listar archivos o ver el status.
2. Analiza los archivos reportados.
3. Genera la línea exacta de comando (`git rm --cached <nombre>`) para que el usuario la ejecute.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Listar archivos de Git | `git_status()` / terminal | Pedir al usuario correr `git ls-files` |
| Quitar archivo de cache | terminal("git rm --cached") | Dar comando exacto al usuario |
| Limpiar historial | terminal("git filter-repo") | Instruir al usuario sobre uso de filter-repo o BFG |

---

## ✅ Verificación

- El archivo `.env` o similar fue removido de la cache de Git.
- `.gitignore` contiene las exclusiones correctas.
- No quedan referencias a secretos en el historial de commits reciente.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
