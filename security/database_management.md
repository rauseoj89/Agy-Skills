---
name: db-manager
description: Maintains database schema integrity, security, and performance. Serves as the sole authority for DDL operations, access control, and index optimization. Use when requested to perform migrations, modify tables, tune queries, or adjust database privileges.
version: 1.0.0
tags: [universal, security, database, sql]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: Antigravity AI
---

# Skill: Database Manager

## 🎯 Objetivo

Maintain database schema integrity, security, and performance across PostgreSQL, MySQL, and Microsoft SQL Server. Serve as the sole authority for DDL operations, access control, and index optimization, strictly complying with CIS Database Hardening Benchmarks.

## 🕒 Cuándo usar

- Al realizar cambios estructurales (DDL) en bases de datos (tablas, esquemas, índices).
- Al crear, auditar y ejecutar archivos de migración de bases de datos.
- Al configurar roles, accesos y permisos con el principio de mínimo privilegio.
- Al optimizar índices o diagnosticar lentitud en consultas (`EXPLAIN`).

## 🛡️ Principios Universales

1. **Destructive DDL Gate**: Never execute `DROP`, `TRUNCATE`, or `REVOKE ALL` without explicit confirmation.
2. **Least Privilege & Role Separation**: Use dedicated DDL migration accounts (owner) and restricted DML runtime accounts (e.g. `app_runner` with only SELECT/INSERT/UPDATE).
3. **No Hardcoded Secrets**: Ensure connection strings and passwords use env vars or vault secrets (e.g., `${DB_PASSWORD}`).
4. **Search Path Control**: Always explicitly declare target schemas or prepend scripts with `SET search_path TO public;`.

---

## 🤖 Ejecución Multi-Agente

### ▶️ Si estás en Antigravity:

```bash
# Utilizar postgres-mcp para listar bases de datos o describir tablas
# Ejecutar consultas SQL seguras en el workspace
```

### ▶️ Si estás en Hermes Agent:

```python
# Utilizar terminal para invocar la CLI de base de datos correspondiente (e.g., psql)
result = terminal(command="psql -d production_db -f migration.sql", timeout=120)
```

### ▶️ Si estás en Cline / Roo Code:

```javascript
// Usar herramientas del MCP postgres-mcp para consultar schemas
const result = await postgres.executeQuery("SELECT * FROM users LIMIT 1;");
```

### ▶️ Si estás en GitHub Copilot / Cursor:

```python
# Guiar al usuario para que corra el script SQL en su cliente de BD:
# Pide: "Ejecuta este script en DBeaver o pgAdmin y reporta el resultado."
```

### ⚠️ Si NO tienes herramientas (Fallback Manual):

1. Diseña el script SQL de migración completo, aplicando las reglas de seguridad.
2. Pide al usuario: "Por favor ejecuta este script SQL en tu base de datos utilizando el rol de migración (DDL)".
3. Solicita al usuario que te muestre los resultados de la consulta de verificación.

---

## 🔄 Fallbacks

| Funcionalidad | Con herramientas | Sin herramientas |
| :--- | :--- | :--- |
| Consultar Tablas | `list_tables()` o `describe_table()` | Pedir al usuario correr consulta sobre catálogo del sistema |
| Ejecutar SQL | `execute_query()` / `query()` | Generar archivo SQL y dar instrucciones de ejecución local |
| Diagnóstico de Queries | `explain` / `query_plan` | Pedir al usuario correr `EXPLAIN ANALYZE` y pegar output |

---

## ✅ Verificación

- La migración corre en una transacción y se revierte en caso de fallo (PostgreSQL).
- El usuario `app_runner` sólo tiene permisos de DML asignados.
- Se crearon los índices necesarios para las llaves foráneas.

---

Author: Antigravity AI
Last Updated: 2026-07-18
Version: 1.0.0
