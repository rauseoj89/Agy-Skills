---
name: docker-build-strategies
description: Strategies for efficient, secure, and optimized Docker image builds. Use when writing, reviewing, or optimizing Dockerfiles, handling multi-stage builds, BuildKit cache mounts, secret mounts, .dockerignore hygiene, and distroless runtimes.
version: 1.0.0
tags: [universal, devops, docker, buildkit, multi-stage, caching, security]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Build Strategies

## 🎯 Objetivo

Architect, optimize, and secure container image builds using modern BuildKit capabilities: multi-stage architectures, package manager cache mounts, build-time secret injection, `COPY --link` optimizations, and minimal non-root runtime environments.

## 🕒 Cuándo usar

- Al crear o refactorizar archivos `Dockerfile` para cualquier tecnología (Node, Python, Go, Java, Rust).
- Al optimizar la velocidad de compilación, el tamaño de imagen o resolver problemas de invalidación de caché.
- Al necesitar inyectar credenciales privadas (tokens npm, claves SSH) de forma segura sin persistirlas en capas.
- Al depurar capas infladas o generar archivos `.dockerignore` estrictos.

## 🛡️ Principios Universales

1. **BuildKit First:** Siempre declarar `# syntax=docker/dockerfile:1` en la primera línea.
2. **Secrets Hygiene:** Nunca usar `ARG` o `ENV` para contraseñas, tokens o SSH keys (se filtran en el historial y metadata). Usar `--mount=type=secret,id=...` o `--mount=type=ssh`.
3. **Multi-Stage & Minimal Runtime:** Separar la etapa de build (`FROM ... AS build`) de la etapa de ejecución (`FROM ... AS runtime`). Usar distroless (`gcr.io/distroless/static-debian12:nonroot`) o imágenes Alpine/Slim.
4. **Cache Optimization:** Ordenar instrucciones de menor a mayor frecuencia de cambio. Usar cache mounts (`--mount=type=cache,target=...`) para gestores de paquetes (Go, npm, pip, maven).
5. **Decoupled Layers:** Usar `COPY --link` para desacoplar capas de archivos independientes y maximizar el reúso de caché.
6. **Non-Root Execution:** Forzar siempre `USER nonroot` o un UID no privilegiado antes del `ENTRYPOINT`/`CMD`.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Ejecutar compilación con BuildKit activado
DOCKER_BUILDKIT=1 docker build --secret id=npmrc,src=.npmrc -t myapp:latest .
```

### ▶️ Si estás en Hermes Agent:
```python
# Ejecutar build a través del terminal
result = terminal(command="DOCKER_BUILDKIT=1 docker buildx build --tag myapp:latest .", timeout=300)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Usar el terminal o comando integrado
const result = await shell.exec("docker buildx build -t app:latest .");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Pide al usuario que corra la compilación con BuildKit:
# "Ejecuta 'DOCKER_BUILDKIT=1 docker build -t mi-app .' para validar la sintaxis y caché."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Diseña el `Dockerfile` optimizado siguiendo el patrón multi-stage y cache mounts.
2. Diseña el `.dockerignore` exhaustivo bloqueando `.git`, `.env*`, `node_modules`, `tests/`.
3. Provee las instrucciones exactas de build al usuario con las banderas de BuildKit.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Compilación de imagen | `docker buildx build` vía terminal/MCP | Generar comando con flags y pedir ejecución |
| Inspección de capas | `docker history` / `docker_inspect()` | Pedir salida de `docker history <image>` |
| Diagnóstico de tamaño | `docker images --format` | Solicitar reporte de peso al usuario |

---

## ✅ Verificación

- La primera línea es `# syntax=docker/dockerfile:1`.
- El archivo `.dockerignore` existe y previene filtraciones de secretos y archivos de desarrollo.
- El usuario final en la imagen de producción es explícitamente no-root.
- No existen secretos ni tokens en variables `ARG` o `ENV`.
- La compilación aprovecha el caché en ejecuciones subsiguientes.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
