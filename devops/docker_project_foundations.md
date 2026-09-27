---
name: docker-project-foundations
description: Guidance for initializing, structuring, and containerizing a project from scratch. Use when creating initial .dockerignore, Dockerfile, and compose.yaml assets for local development without polluting the host toolchain.
version: 1.0.0
tags: [universal, devops, docker, scaffolding, foundations, compose-v2]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Project Foundations

## 🎯 Objetivo

Scaffold complete, production-aligned containerization for any project from zero, delivering the foundational triad (`.dockerignore`, `Dockerfile`, `compose.yaml`) with zero host toolchain pollution and strict credential isolation.

## 🕒 Cuándo usar

- Al "Dockerizar" o inicializar la infraestructura de contenedores para un proyecto nuevo o existente.
- Cuando un repositorio carece de activos de Docker o usa configuraciones obsoletas de `docker-compose.yml` v1.
- Al agregar dependencias locales (Postgres, Redis, RabbitMQ) para desarrollo sin instalar binarios en el host del usuario.

## 🛡️ Principios Universales

1. **The Foundational Triad:** Todo proceso de containerización debe proveer los 3 artefactos esenciales:
   - `.dockerignore`: previene contaminar el build context con dependencias locales, binarios o secretos.
   - `Dockerfile`: compilación multi-stage, uso de BuildKit, usuario no-root.
   - `compose.yaml`: orquestación de servicios con healthchecks y redes dedicadas.
2. **Zero Host Toolchain Pollution:** Diseñar los flujos para que compilación, migraciones y ejecución ocurran dentro de los contenedores, sin forzar instalaciones globales (`npm -g`, `pip install`, `brew`) en la máquina host.
3. **Strict Credential Isolation:** Asegurar que `.env` y certificados nunca sean indexados por el build context o versionados en git. Proveer `.env.example` sanitizado.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Validar el contexto de build y ejecutar la orquestación inicial
docker compose up -d --build
```

### ▶️ Si estás en Hermes Agent:
```python
# Inicializar los archivos de configuración y verificar arranque
result = terminal(command="docker compose up -d", timeout=120)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Escribir los 3 archivos de la tríada y verificar sintaxis con shell
await shell.exec("docker compose config");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Generar los archivos y solicitar al desarrollador ejecutar:
# "Ejecuta 'docker compose up -d --build' para inicializar tu entorno de desarrollo."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Detecta la tecnología principal (Node.js, Go, Python, PHP, Rust) examinando los archivos de manifiesto.
2. Redacta la tríada completa (`.dockerignore`, `Dockerfile`, `compose.yaml`) y el archivo `.env.example`.
3. Brinda al usuario la guía de inicialización y verificación paso a paso.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Crear tríada | Herramientas de escritura de archivos | Generar contenido en markdown para copiar/pegar |
| Validar stack | `docker compose up -d` / `docker compose ps` | Pedir al usuario confirmación de logs de arranque |
| Verificar ignore | `docker build` (monitorear bytes enviados) | Revisión manual de exclusiones en `.dockerignore` |

---

## ✅ Verificación

- Se generaron los 3 archivos: `.dockerignore`, `Dockerfile`, `compose.yaml`.
- `.dockerignore` excluye explícitamente `.git`, `.env*`, carpetas de dependencias y artefactos de compilación.
- `compose.yaml` define dependencias ordenadas por comprobación de salud (`condition: service_healthy`).
- El stack inicia sin requerir software instalado directamente en el host del desarrollador.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
