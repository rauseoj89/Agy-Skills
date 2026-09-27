---
name: managing-containers
description: Audits, deploys, and maintains Docker containers, Compose architectures, and image environments. Use when asked to configure Dockerfiles, compose services, parse container logs, verify port configurations, or manage local development virtualization.
version: 1.1.0
tags: [universal, devops, docker, kubernetes, containers, buildkit, compose-v2]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker & Kubernetes Container Specialist

## 🎯 Objetivo

Design, deploy, and maintain robust, high-performance containerized and orchestrated infrastructures, strictly adhering to modern Docker standards (BuildKit, Compose v2) and CIS Docker and Kubernetes Security Benchmarks.

## 🕒 Cuándo usar

- Al configurar u optimizar archivos `Dockerfile` o `compose.yaml`.
- Al configurar manifiestos de Kubernetes (Deployments, Services, NetworkPolicies).
- Al inspeccionar procesos, redes o volúmenes activos de Docker/K8s.
- Al analizar logs de contenedores para diagnosticar caídas o errores de arranque.
- Al verificar límites de recursos, políticas no-root o gates de operaciones destructivas.

## 🛡️ Principios Universales

1. **Canonical Compose v2:** Always use `compose.yaml` (never legacy `docker-compose.yml`).
2. **BuildKit Standards:** Always declare `# syntax=docker/dockerfile:1`. Use package cache mounts (`--mount=type=cache`), secret mounts (`--mount=type=secret`), and `COPY --link`.
3. **Non-Root Runtime:** Force execution context using non-root users (`USER 10001` or `USER nonroot:nonroot` / `runAsNonRoot: true`).
4. **Readiness Dependencies:** Always pair `depends_on` with `condition: service_healthy` for databases and backend services.
5. **Distroless Sidecar Healthchecks:** For images without curl/shell, attach a sidecar container using `network_mode: "service:<target>"`.
6. **3-Tier Destructive Gate:** Never delete volumes or run `system prune` without explicit user confirmation and presenting scoped alternatives.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Inspeccionar procesos y logs con nas-tools o shell nativo
# docker compose -f compose.yaml up -d
```

### ▶️ Si estás en Hermes Agent:
```python
# Usar el terminal integrado para inspeccionar contenedores
result = terminal(command="docker compose ps", timeout=60)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Usar el MCP de shell/terminal o docker
const result = await shell.exec("docker compose ps");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Pide al usuario que corra comandos de diagnóstico locales si no tienes terminal:
# "Por favor ejecuta 'docker compose ps' y 'docker logs <nombre-contenedor>'."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Genera los archivos `Dockerfile` y `compose.yaml` correctos.
2. Pide al usuario: "Guarda estos archivos y ejecuta 'docker compose up -d'".
3. Solicita que ejecute comandos de verificación y te reporte los logs.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Ver estado de contenedores | docker_ps() / terminal("docker compose ps") | Pedir al usuario que ejecute `docker compose ps` |
| Ver logs del contenedor | docker_logs() / terminal("docker logs") | Pedir al usuario que ejecute y pegue `docker logs` |
| Control de contenedor | docker_control() / terminal("docker start/stop") | Generar el comando correspondiente para el usuario |
| Eliminar recursos (Tier 3) | Solicitar confirmación + terminal("docker rm") | Advertir sobre pérdida de datos y generar comando exacto |

---

## ✅ Verificación

- El archivo de orquestación se llama `compose.yaml`.
- El contenedor corre bajo un usuario no-root (`USER nonroot`).
- El sistema de archivos raíz es de sólo lectura.
- Los logs del contenedor no muestran excepciones críticas y el estado es `healthy`.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.1.0
