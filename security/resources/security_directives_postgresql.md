# Hardened PostgreSQL Security Directives

When creating, managing, or querying PostgreSQL databases, the following security standards must be strictly enforced:

### 1. Search Path Hijacking Prevention
PostgreSQL resolves unqualified function and table calls using the `search_path`. If an attacker can write to a schema in the search path (such as `public` or `pg_temp`), they can intercept calls or execute malicious functions.
- **Migration Policy:** Every migration or DDL script must explicitly set the search path at the start of the transaction:
  ```sql
  SET search_path TO public;
  ```
- **Application Connections:** Prepend connection initializations with `SET search_path TO public;` or explicitly qualify every table name in queries (e.g., `SELECT * FROM public.users`).

### 2. Strict Role Separation (Least Privilege)
Never connect the application web server using the table owner or superuser credentials.
- **DDL Role (Migration Executor):**
  - Owns all tables, schemas, and indices.
  - Used strictly for executing schema updates and migrations.
- **DML Role (App Runner):**
  - Limited role used by the web application at runtime.
  - Granted only the minimum required privileges (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) on target tables:
    ```sql
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.users TO app_runner;
    GRANT USAGE, SELECT ON SEQUENCE public.users_id_seq TO app_runner;
    ```
  - Has absolutely no DDL permissions (`CREATE`, `ALTER`, `DROP`).

### 3. Public Schema & Catalog Hardening
- **Revoke Public Creation:** By default, PostgreSQL allows all users to create objects in the `public` schema. This must be explicitly revoked:
  ```sql
  REVOKE CREATE ON SCHEMA public FROM PUBLIC;
  ```
- **Metadata Protection:** Revoke access to system directories that contain metadata or sensitive structures (such as `pg_authid`):
  ```sql
  REVOKE ALL ON pg_authid FROM PUBLIC;
  ```

### 4. Encrypted Transport (SSL/TLS)
Database connections must be protected in transit to prevent data interception.
- **Enforcement:** Configure the database server to only accept SSL connections (`ssl = on` in `postgresql.conf`).
- **Connection Strings:** Application connection parameters must require SSL verification:
  ```ini
  sslmode=verify-full
  sslrootcert=/path/to/server-ca.crt
  ```

### 5. Detailed Audit Logs & pgAudit
- **pgAudit Configuration:** Enable the `pgAudit` extension in the server configuration to log specific DDL changes, privilege updates (`GRANT`/`REVOKE`), and administrative operations:
  ```ini
  # postgresql.conf
  shared_preload_libraries = 'pgaudit'
  pgaudit.log = 'ddl, role, write'
  ```
- **Query Logging:** Enable slow query logging via `log_min_duration_statement = 250` (log queries taking longer than 250ms) to detect performance degradation, ensuring no plaintext passwords appear in the logs.

### 6. Row-Level Security (RLS)
For multi-tenant systems or applications where data access is partitioned by user, enforce access controls directly at the database engine layer:
- **Enable RLS:**
  ```sql
  ALTER TABLE public.user_profiles ENABLE ROW LEVEL SECURITY;
  ```
- **Define Access Policies:** Create policies that restrict rows visible to the runtime role based on the current session user context:
  ```sql
  CREATE POLICY profile_isolation ON public.user_profiles
      FOR ALL
      USING (owner_username = current_setting('app.current_user'));
  ```

### 7. Destructive SQL Guard
The following PostgreSQL operations are classified as **destructive** and must never be auto-executed. The Security Engineer must always present the exact SQL statement to the user, describe the scope of data at risk, and receive explicit confirmation before proceeding.

**Destructive PostgreSQL Operations:**

| Operation | Risk |
|---|---|
| `DROP TABLE public.<table>` | Permanent deletion of table structure and all data |
| `DROP DATABASE <db>` | Permanent deletion of entire database |
| `TRUNCATE public.<table>` | Permanent deletion of all rows (cannot be rolled back outside a transaction) |
| `DELETE FROM public.<table>` without `WHERE` | Permanent deletion of all rows |
| `REVOKE ALL ON TABLE ... FROM PUBLIC` | May break application access if mis-targeted |
| `DROP SCHEMA <schema> CASCADE` | Cascades deletion to all objects in the schema |

**Confirmation display format:**
```
⚠️  DESTRUCTIVE SQL OPERATION
Statement: TRUNCATE public.sessions;
Risk: Permanently deletes ALL rows in the sessions table. This cannot be undone outside a transaction.
Do you confirm execution? [type CONFIRM to proceed]
```

*Rule:* If a destructive statement must be executed as part of a migration, it must be wrapped in an explicit transaction with a documented rollback path:
```sql
BEGIN;
  TRUNCATE public.temp_import_staging;
  -- Verify impact
  SELECT COUNT(*) FROM public.temp_import_staging; -- Should be 0
COMMIT; -- Only after explicit user review
```
