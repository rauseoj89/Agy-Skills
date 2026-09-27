---
name: docker-compose-patterns
description: Patterns for robust, maintainable Docker Compose configurations. Use when wiring multi-container stacks, configuring health checks, dependencies with service readiness, network topologies, volume persistence, and development overrides.
version: 1.0.0
tags: [universal, devops, docker, compose-v2, healthchecks, networking, orchestration]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Compose Patterns

## 🎯 Objetivo

Design, configure, and maintain production-grade multi-container environments using modern Compose v2 standards (`compose.yaml`), strict readiness dependency chaining (`condition: service_healthy`), isolated bridge networks, and distroless healthcheck sidecars.

## 🕒 Cuándo usar

- Al crear o refactorizar arquitecturas multi-contenedor en Docker Compose.
- Al resolver condiciones de carrera durante el arranque entre aplicaciones y bases de datos.
- Al configurar comprobaciones de salud nativas (`healthcheck`) para PostgreSQL, Redis, MySQL o microservicios.
- Al implementar patrones de sobreescritura para desarrollo (`compose.override.yaml`) frente a producción.
- Al estructurar redes internas privadas versus redes públicas expuestas.

## 🛡️ Principios Universales

1. **Canonical Compose v2:** El archivo principal siempre debe nombrarse `compose.yaml` (no el legado `docker-compose.yml`). No incluir `version:` en la raíz.
2. **Readiness Dependency Chaining:** Nunca usar `depends_on: [db]` plano (solo espera que el contenedor inicie, no que acepte conexiones). Usar siempre `condition: service_healthy`.
3. **Native Healthchecks:** Cada servicio dependiente debe tener un healthcheck explícito:
   - PostgreSQL: `test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]`
   - Redis: `test: ["CMD", "redis-cli", "ping"]`
   - MySQL: `test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]`
4. **Sidecar Pattern para Distroless:** En contenedores sin curl ni shell, acoplar un contenedor sidecar con `network_mode: "service:<target>"` para ejecutar el probe de salud HTTP sobre localhost.
5. **Network Isolation:** Separar redes frontend (accesibles externamente) de backend/data (privadas, sin puertos expuestos al host en producción).
6. **Zero Plaintext Secrets:** Utilizar interpolación de entorno o la directiva `secrets:` de Compose en lugar de hardcodear contraseñas.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Validar sintaxis y configuración renderizada
docker compose config
# Levantar stack en segundo plano y esperar estado healthy
docker compose up -d --wait
```

### ▶️ Si estás en Hermes Agent:
```python
# Inspeccionar estado de los servicios orquestados
result = terminal(command="docker compose ps --format json", timeout=60)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Ejecutar validación de orquestación
const result = await shell.exec("docker compose config --quiet");
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Solicitar al usuario la verificación de salud del stack:
# "Ejecuta 'docker compose ps' y verifica que todos los servicios tengan el estado '(healthy)'."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Diseña la plantilla `compose.yaml` con las dependencias `condition: service_healthy`.
2. Provee un archivo `.env.example` con los nombres de variables requeridas.
3. Genera el comando `docker compose up -d` y pide al usuario confirmar que los servicios alcancen el estado saludable.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Validar sintaxis | `docker compose config` | Revisión estática de indentación y claves YAML |
| Monitorear arranque | `docker compose ps` | Pedir salida de `docker compose ps` |
| Ver logs agregados | `docker compose logs -f` | Pedir al usuario filtrar logs por servicio |

---

## ✅ Verificación

- El archivo se llama `compose.yaml`.
- Todos los servicios de base de datos definen un `healthcheck` funcional.
- Las aplicaciones web declaran `depends_on` con `condition: service_healthy`.
- Los puertos de bases de datos internas no están mapeados al host en entornos de producción.
- No hay credenciales en texto plano en el manifiesto.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
