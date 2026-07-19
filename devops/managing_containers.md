---
name: managing-containers
description: Audits, deploys, and maintains Docker containers, Compose architectures, and image environments. Use when asked to configure Dockerfiles, compose services, parse container logs, verify port configurations, or manage local development virtualization.
version: 1.0.0
tags: [universal, devops, docker, kubernetes, containers]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Docker & Kubernetes Container Specialist

## 🎯 Objetivo

Design, deploy, and maintain robust, high-performance containerized and orchestrated infrastructures, strictly adhering to CIS Docker and Kubernetes Security Benchmarks.

## 🕒 Cuándo usar

- Al configurar u optimizar archivos `Dockerfile` o `docker-compose.yml`.
- Al configurar manifiestos de Kubernetes (Deployments, Services, NetworkPolicies).
- Al inspeccionar procesos, redes o volúmenes activos de Docker/K8s.
- Al analizar logs de contenedores para diagnosticar caídas o errores de arranque.

## 🛡️ Principios Universales

1. **Non-Root Runtime:** Force execution context using non-root users (`USER 10001` or `runAsNonRoot: true`).
2. **Capability Drop:** Drop all Linux privileges by default: `capabilities.drop: ["ALL"]`.
3. **Read-Only Root Filesystem:** Mount root directory as read-only.
4. **Base Image Pinning**: Always pin base Docker images to cryptographic SHA256 hashes instead of mutable tags.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Ejecutar comandos locales usando la CLI de Docker
# Auditar salud del sistema con docker_ps o herramientas nativas
```

### ▶️ Si estás en Hermes Agent:

```python
# Usar el terminal integrado para inspeccionar contenedores
result = terminal(command="docker ps", timeout=60)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar el MCP de shell/terminal o docker si está disponible para interactuar
const result = await shell.exec("docker ps");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Pide al usuario que corra comandos de diagnóstico locales si no tienes terminal:
# "Por favor ejecuta 'docker logs <nombre-contenedor>' y pega el error."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Genera los archivos `Dockerfile` o `docker-compose.yml` correctos.
2. Pide al usuario: "Guarda este Dockerfile y ejecuta 'docker build -t app .'".
3. Solicita que ejecute comandos de verificación y te reporte los logs.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Ver estado de contenedores | docker_ps() / terminal("docker ps") | Pedir al usuario que ejecute `docker ps` |
| Ver logs del contenedor | docker_logs() / terminal("docker logs") | Pedir al usuario que ejecute y pegue `docker logs` |
| Eliminar recursos | docker_control() / terminal("docker rm") | Generar el comando `docker rm` para el usuario |

---

## ✅ Verificación

- El contenedor corre bajo un usuario no-root.
- El sistema de archivos raíz es de sólo lectura.
- Los logs del contenedor no muestran excepciones críticas.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
