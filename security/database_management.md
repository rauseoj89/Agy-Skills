---
name: "Database Management"
description: "Maintains schema integrity, performs SQL audits, structures migrations, and enforces DDL access separation."
category: "generic/security"
tools_required: ["postgres-mcp"]
last_updated: 2026-06-15
---

# 🧠 Skill: Database Security Administrator

## 🎯 Goal
Govern database schemas, perform safe SQL migrations, index performance columns, and isolate data access permissions using secure parameterization.

## 📊 Inputs Required
- Proposed database schema modifications (DDL).
- Active DB connection configurations.

## 🛠️ Step-by-Step Instructions
1. **Schema Audits & Normalization**:
   - Audit all database tables to verify they comply with normalized structures (up to 3NF).
   - Ensure foreign key constraints map referential integrity rules (e.g. `ON DELETE RESTRICT`).
2. **Access Control & Least Privilege**:
   - Revoke default public role credentials. Grant DML rights (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) solely to the application runner account.
   - Enforce distinct ownership: the application runner must never own database tables.
3. **Migration Safe Execution**:
   - Wrap SQL updates inside transaction scopes (`BEGIN; ... COMMIT;`).
   - Prepend all migration scripts with an explicit search path initialization: `SET search_path TO public;`.
4. **Destructive SQL Gate**:
   - Stop immediately if any migration file contains `DROP`, `TRUNCATE`, or `DELETE` commands without a `WHERE` clause.
   - Show the statement to the user, list risks, and wait for confirmation.

## 🛡️ Verification & Security Checklist
1. **Parameterization Check**: Ensure zero SQL commands utilize dynamic string concatenation or unparameterized queries.
2. **Search Path Verification**: Confirm that the target schema name is explicitly stated in all query actions.
3. **Credentials Hardening**: Ensure no plaintext passwords or server credentials leak in logs.

---
*Created by Efficiency Core*
