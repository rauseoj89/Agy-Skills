---
name: docker-destructive-guardrails
description: Safety guardrails and policies for destructive or irreversible Docker operations. Use before running or recommending commands that delete, prune, wipe, or reset containers, volumes, builder cache, or system images.
version: 1.0.0
tags: [universal, devops, docker, safety, risk-management, guardrails]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-09-26
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Docker Destructive Guardrails

## 🎯 Objetivo

Prevent accidental data loss, unexpected downtime, and destructive actions when managing Docker environments by enforcing a strict 3-tier risk classification and explicit user confirmation gates.

## 🕒 Cuándo usar

- Antes de ejecutar o recomendar `docker rm`, `docker rm -f`, `docker compose down -v`, `docker volume prune`, `docker builder prune` o `docker system prune`.
- Cuando el usuario o un script solicita "limpiar espacio", "resetear el entorno", "empezar de cero" o "borrar la caché".
- Para identificar alternativas seguras de limpieza antes de recurrir a la destrucción de volúmenes o capas de compilación.

## 🛡️ Principios Universales

1. **Mandatory Confirmation Gate:** Nunca ejecutar operaciones destructivas automáticamente ni por reflejo. En operaciones Tier 3, pausar y solicitar confirmación explícita detallando los recursos afectados.
2. **Present Non-Destructive Alternatives:** Proponer siempre la alternativa de menor impacto antes de ejecutar una eliminación masiva.
3. **Volume Protection:** Tratar los volúmenes de Docker como bases de datos en producción. Una eliminación de volumen es irreversible.
4. **Targeted Pruning:** Preferir la eliminación de contenedores huérfanos o capas `<none>` puntuales sobre prunes globales con flag `-a`.

---

## 🚦 Clasificación de Riesgo en 3 Niveles

| Nivel | Riesgo | Comandos Típicos | Política de Acción |
| :--- | :--- | :--- | :--- |
| **Tier 1** | Bajo | `docker stop`, `docker rm <test-container>` | Proceder tras validar que el contenedor es efímero. |
| **Tier 2** | Medio | `docker compose down` (sin `-v`), `docker image prune` (sin `-a`), `docker network prune` | Informar qué contenedores o redes se detendrán; verificar que no hay datos en juego. |
| **Tier 3** | Alto / Crítico | `docker compose down -v`, `docker volume rm`, `docker volume prune`, `docker system prune -a`, `docker builder prune -a` | **ALTO:** Detallar volúmenes y caches exactos a destruir. Requerir confirmación explícita del usuario. |

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:
```bash
# Diagnosticar uso de disco antes de proponer prunes
docker system df
# Listar volúmenes para identificar huérfanos específicos
docker volume ls -qf dangling=true
```

### ▶️ Si estás en Hermes Agent:
```python
# Inspeccionar volúmenes antes de proponer acciones destructivas
result = terminal(command="docker volume ls", timeout=30)
```

### ▶️ Si estás en Cline / Roo Code:
```javascript
// Solicitar confirmación al usuario antes de llamar a shell con comandos Tier 3
// "Se eliminarán los siguientes volúmenes: [lista]. ¿Confirmas continuar?"
```

### ▶️ Si estás en GitHub Copilot / Cursor:
```python
# Proporcionar comandos acotados y seguros explicando el impacto:
# "Para liberar espacio sin borrar datos persistentes, ejecuta 'docker image prune' en lugar de 'system prune -a'."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):
1. Formula el plan de limpieza escalonado (identificar primero imágenes huérfanas, luego contenedores detenidos).
2. Pide al usuario que corra `docker system df` y reporte el espacio ocupado.
3. Genera el comando más restrictivo posible para mitigar riesgos de pérdida de datos.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Inspección de espacio | `docker system df` vía terminal | Pedir al usuario salida de `docker system df` |
| Verificación de volúmenes | `docker volume ls` | Pedir confirmación visual de volúmenes existentes |
| Limpieza de bajo riesgo | `docker image prune` | Instruir al usuario a ejecutar comando acotado |

---

## ✅ Verificación

- Se evaluó el riesgo del comando según la matriz Tier 1, 2 o 3.
- Se presentó una alternativa no destructiva antes de proceder.
- En comandos Tier 3, se detallaron exactamente los volúmenes o cachés que se perderán y se obtuvo aprobación expresa.
- El sistema Docker permanece estable y operativo post-mantenimiento.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-09-26  
Version: 1.0.0
