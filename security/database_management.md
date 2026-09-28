---
name: db-manager
description: Maintains database schema integrity, security, and performance. Serves as the sole authority for DDL operations, access control, and index optimization. Use when requested to perform migrations, modify tables, tune queries, or adjust database privileges.
version: 1.0.0
tags: [universal, security, database, sql]
compatible_agents: [Hermes, Antigravity, Cline, Roo-Code, Copilot, Cursor]
last_updated: 2026-07-18
author: JimmyR
powered_by: AntigravityAI
---

# Skill: Database Manager

## 🎯 Objective

Maintain database schema integrity, security, and performance across PostgreSQL, MySQL, and Microsoft SQL Server. Serve as the sole authority for DDL operations, access control, and index optimization, strictly complying with CIS Database Hardening Benchmarks.

## 🕒 When to Use

- When performing structural schema changes (DDL) on databases (tables, schemas, indexes).
- When authoring, reviewing, and applying database migration scripts.
- When configuring roles, permissions, and grants according to least-privilege principles.
- When optimizing indexes or troubleshooting query latency (`EXPLAIN`).

## 🛡️ Universal Principles

1. **Destructive DDL Gate**: Never execute `DROP`, `TRUNCATE`, or `REVOKE ALL` without explicit confirmation.
2. **Least Privilege & Role Separation**: Use dedicated DDL migration accounts (owner) and restricted DML runtime accounts (e.g. `app_runner` with only SELECT/INSERT/UPDATE).
3. **No Hardcoded Secrets**: Ensure connection strings and passwords use env vars or vault secrets (e.g., `${DB_PASSWORD}`).
4. **Search Path Control**: Always explicitly declare target schemas or prepend scripts with `SET search_path TO public;`.

---

## 🤖 Multi-Agent Execution

### ▶️ If you are on Antigravity:

```bash
# Use postgres-mcp to list databases or describe tables
# Execute secure SQL queries in the workspace
```

### ▶️ If you are on Hermes Agent:

```python
# Use terminal to invoke appropriate database CLI (e.g., psql)
result = terminal(command="psql -d production_db -f migration.sql", timeout=120)
```

### ▶️ If you are on Cline / Roo Code:

```javascript
// Use postgres-mcp tools to inspect schemas
const result = await postgres.executeQuery("SELECT * FROM users LIMIT 1;");
```

### ▶️ If you are on GitHub Copilot / Cursor:

```python
# Guide user to run SQL script in their database client:
# Ask: "Execute this script in DBeaver or pgAdmin and report the outcome."
```

### ⚠️ If you do NOT have tools (Manual Fallback):

1. Design the complete SQL migration script adhering to security rules.
2. Ask user: "Please execute this SQL script in your database using your migration role (DDL)".
3. Request that user share the verification query output.

---

## 🔄 Fallbacks

| Feature / Capability | With Tools | Without Tools |
| :--- | :--- | :--- |
| Inspect tables | `list_tables()` or `describe_table()` | Ask user to query system catalog |
| Execute SQL | `execute_query()` / `query()` | Generate SQL file and provide local execution instructions |
| Query diagnostics | `explain` / `query_plan` | Ask user to run `EXPLAIN ANALYZE` and paste output |

---

## ✅ Verification

- Migrations run within a transaction and roll back on failure (PostgreSQL).
- The `app_runner` account only holds assigned DML privileges.
- Foreign key columns have corresponding indexes created.

---

**Author:** JimmyR  
**Powered by:** AntigravityAI  
Last Updated: 2026-07-18  
Version: 1.0.0
