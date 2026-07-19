---
name: designing-apis
description: Designs RESTful and GraphQL API architectures, generates OpenAPI 3.1 specifications, defines endpoint contracts, and establishes versioning strategies. Use when asked to design APIs, write API specs, define endpoint schemas, or plan API versioning.
version: 1.0.0
tags: [universal, api, design, rest, graphql]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: API Architect & Designer

## 🎯 Objetivo

Design secure, highly performant, and self-documenting API interfaces, establishing contracts, schemas, and version gates before functional code implementation, while strictly complying with OWASP API Security Top 10 (2023) mandates.

## 🕒 Cuándo usar

- Al diseñar interfaces de API o endpoints HTTP.
- Al crear especificaciones de OpenAPI 3.1 o Swagger.
- Al planificar estrategias de control de versiones de API (URI, cabeceras).
- Al definir patrones de autenticación, límites de tasa de peticiones y estructuras de error.

## 🛡️ Principios Universales

1. **Security-First Architecture (OWASP API Security Top 10 2023)**:
   - **BOLA & BOPLA Mitigation (API1 / API3):** Server-side authorization checks on both object and property levels.
   - **Authentication (API2):** Bearer Tokens (JWT) or API Keys, never in query parameters.
   - **Resource Consumption Limits (API4):** Strict payload limit (e.g. max 10MB), limit array lengths.
   - **SSRF Protection (API7):** Validate external URL redirects; block loopback/private ranges (RFC 1918).
   - **Shadow API Mitigation (API9):** Version routes (e.g., `/api/v1/`) and deprecate explicitly.
   - **Third-Party Consumption (API10):** Validate third-party API payloads against JSON Schema.
2. **No Hardcoded Server Paths, Passwords, or IPs**: Spec templates must use dynamic parameters (e.g. `${API_BASE_URL}`).
3. **No Unbounded Collections**: Force pagination on all list-returning endpoints.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Escribir especificaciones OpenAPI 3.1 y guardarlas en el workspace
# Usar el flujo de confirmaciones de la plataforma
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar read_file / write_file para crear los schemas
spec_content = read_file(path="openapi.yaml")
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el filesystem MCP para leer y escribir las especificaciones OpenAPI
const currentSpec = await filesystem.readFile("openapi.yaml");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Si no hay terminal ni herramientas de edición directa:
# Pide al usuario que cree el archivo schema.graphql o openapi.yaml
# y proporciona el contenido completo formateado en bloques de código.
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera el contenido YAML/JSON completo del API Contract.
2. Explica la arquitectura detalladamente.
3. Pide al usuario: "Guarda este contenido en un archivo `openapi.yaml`".

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Crear archivo de spec | write_to_file() | Proporcionar el bloque de código para que el usuario lo guarde |
| Validar YAML/JSON | Ej. correr validador en terminal | Pedir al usuario que corra el validador y pegue el output |

---

## ✅ Verificación

- La spec pasa las reglas de OpenAPI 3.1 sin advertencias.
- Se implementan paginación y límites en todos los endpoints de listas.
- Se previenen leaks de stacktrace en el esquema de error estándar.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
