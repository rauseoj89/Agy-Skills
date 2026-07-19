---
name: managing-secrets-and-vaults
description: Secures system credentials, manages API keys, rotates environment variables, and orchestrates integration with secure vaults. Use when requested to configure environment keys, edit secrets, retrieve items from Vault, or secure sensitive configurations.
version: 1.0.0
tags: [universal, security, vault, secrets]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Secrets & Credentials Manager

## 🎯 Objetivo

Enforce bulletproof security for application credentials, ensuring zero secrets are leaked to disk, logs, or repositories, while utilizing advanced vaulting and rotation workflows.

## 🕒 Cuándo usar

- Al actualizar contraseñas, claves de API, cadenas de conexión o certificados.
- Al configurar o modificar archivos de variables de entorno (`.env`, `.env.local`).
- Al inventariar o rotar secretos usando bovedas externas.
- Para auditar y prevenir fugas de secretos en el historial de Git.

## 🛡️ Principios Universales

1. **The Redaction Protocol**: Strip or replace plaintext passwords/keys with `[REDACTED]` or `********` in all logs, screenshots, and terminal outputs.
2. **Git-Leak Defense**: Force the target config files (like `.env`) to be explicitly in `.gitignore` before writing secrets to them.
3. **Atomic Secret File Writes**: Never edit environment files directly. Write updates to `.env.tmp` first, then replace.
4. **Least Privilege**: Query specific paths rather than reading all credentials in bulk.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Interactuar con vault-bridge-mcp para leer o rotar secretos
# Utilizar variables del sistema local de forma segura
```

### ▶️ Si estás en Hermes Agent:

```python
# Cargar secretos de forma dinámica usando hermes_secrets o variables de entorno
import os
db_pass = os.getenv("DB_PASSWORD") or hermes_secrets.get("db_password")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Llamar al MCP de bóveda o vault-bridge-mcp para consultar secretos
const secret = await vault.getSecret({ path: "production/db", key: "password" });
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario para que guarde las claves en sus variables de entorno locales:
# Pide: "Configura la variable de entorno 'DB_PASSWORD' en tu equipo local."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Solicita al usuario que defina las variables de entorno de forma manual en su sistema operativo.
2. Genera plantillas `.env.example` vacías con placeholders claros (ej: `DB_PASSWORD=YOUR_PASSWORD_HERE`).
3. Advierte al usuario sobre no subir nunca estos archivos a Git y verificar que estén en `.gitignore`.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Obtener secreto | `get_secret()` / vault.getSecret() | Pedir al usuario configurar variable localmente |
| Escribir archivo .env | Escribir via `.env.tmp` y renombrar | Dar la plantilla de variables de entorno al usuario |
| Rotar credencial | `rotate_secret()` | Proporcionar guía de rotación en consola al usuario |

---

## 5. ✅ Verificación

- El archivo `.env` está en `.gitignore`.
- No hay secretos en texto plano en la consola o los logs del agente.
- Los archivos temporales `.tmp` de secretos fueron eliminados tras la escritura.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
