# Hardened Microsoft SQL Server (MSSQL) Security Directives

When creating, managing, or querying Microsoft SQL Server databases, the following security standards must be strictly enforced:

### 1. Secure Parameterization & T-SQL Safety
Dynamic T-SQL string execution is the primary source of SQL Injection in SQL Server environments.
- **Parameterization:** Enforce strict parameterization using drivers (e.g., `pyodbc` or `mssql` client libraries):
  ```python
  # CORRECT:
  cursor.execute("SELECT id, name FROM users WHERE email = ?", (user_email,))
  ```
- **Dynamic SQL (Stored Procedures):** Never concatenate parameters inside stored procedures. If dynamic T-SQL is necessary, execute it strictly through `sp_executesql` with defined parameter types:
  ```sql
  -- CORRECT:
  DECLARE @SQL NVARCHAR(MAX) = N'SELECT id FROM app.users WHERE status = @status';
  EXEC sp_executesql @SQL, N'@status VARCHAR(50)', @status = @status_param;
  ```
  *Rule:* Never execute dynamic statements via raw `EXEC(@SQL_STRING)`.

### 2. Disabling Dangerous OS Integrations
SQL Server provides built-in system procedures that can access the underlying Windows Operating System. These must be deactivated.
- **xp_cmdshell:** This procedure allows executing Windows command shell operations directly from the database engine. It must be permanently disabled:
  ```sql
  EXEC sp_configure 'show advanced options', 1;
  RECONFIGURE;
  EXEC sp_configure 'xp_cmdshell', 0;
  RECONFIGURE;
  ```
- **Ad Hoc Distributed Queries:** Disable remote data source querying to prevent outbound credential-harvesting attacks:
  ```sql
  EXEC sp_configure 'Ad Hoc Distributed Queries', 0;
  RECONFIGURE;
  ```

### 3. Integrated Windows Authentication
Avoid hardcoding database usernames and passwords in cleartext application files.
- **Preferred Method:** Enforce **Windows Authentication** (Integrated Security) or Azure AD Managed Identities. The web server process logs directly into the SQL Server under its machine identity.
  - *ODBC String:* `Driver={ODBC Driver 18 for SQL Server};Server=db_server;Database=app_db;Trusted_Connection=yes;`
- **SQL Logins Hardening:** If SQL Server Logins must be used:
  - Disable the default system administrator (`sa`) account or rename it and assign a complex, randomized password.
  - Enforce password policies:
    ```sql
    ALTER LOGIN app_user WITH PASSWORD = 'secure_password' MUST_CHANGE, CHECK_EXPIRATION = ON, CHECK_POLICY = ON;
    ```

### 4. Custom Schema Scoping & Privileges
Do not run user applications in the default `dbo` schema, which has broad admin associations.
- **Custom Schema Creation:** Create a dedicated schema for application tables and restrict access to it:
  ```sql
  CREATE SCHEMA app;
  ```
- **Least Privilege Grants:** Create a database user (not a login) and grant rights solely on that schema:
  ```sql
  CREATE USER app_user FOR LOGIN app_login;
  GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::app TO app_user;
  ```
  *Rule:* The application user must **never** be a member of administrative roles like `sysadmin` or `db_owner`.

### 5. TDS Connection Encryption
The Tabular Data Stream (TDS) protocol must be encrypted to prevent snooping and interception.
- **Enforce Encryption:** Configure the database engine to require encryption (`Force Encryption = Yes` in SQL Server Configuration Manager).
- **Client Requirements:** Client connection strings must require encryption and server certificate validation:
  ```ini
  Encrypt=yes
  TrustServerCertificate=no
  ```

### 6. SQL Server Auditing
- **Audit Trails:** Implement a SQL Server Audit to log logins, failed access attempts, changes to database roles, and DDL modifications:
  ```sql
  CREATE SERVER AUDIT AppDbAudit TO APPLICATION_LOG;
  CREATE SERVER AUDIT SPECIFICATION AppDbAuditSpec
      FOR SERVER AUDIT AppDbAudit
      ADD (FAILED_LOGIN_GROUP),
      ADD (DATABASE_ROLE_MEMBER_CHANGE_GROUP);
  ALTER SERVER AUDIT AppDbAudit WITH (STATE = ON);
  ```

### 7. Destructive T-SQL Guard
The following SQL Server operations are classified as **destructive** and require explicit user confirmation before execution or suggestion.

**Destructive MSSQL Operations:**

| Operation | Risk |
|---|---|
| `DROP TABLE app.<table>` | Permanent deletion of table and all data |
| `TRUNCATE TABLE app.<table>` | Permanent deletion of all rows |
| `DELETE FROM app.<table>` without `WHERE` | Permanent deletion of all rows |
| `DROP DATABASE <db>` | Permanent deletion of the entire database |
| `REVOKE ... FROM <user>` | May break application access |
| `EXEC sp_configure 'xp_cmdshell', 1` | Re-enables OS command execution — critical risk |
| `ALTER SERVER AUDIT ... WITH (STATE = OFF)` | Disables audit trail — compliance violation |

**Protocol:**
Before executing any of the above:
1. Display the exact T-SQL statement.
2. State the specific risk (rows affected, permissions changed, features enabled).
3. Request explicit user confirmation.
4. Wrap DDL in a transaction where possible:
```sql
BEGIN TRANSACTION;
  DROP TABLE app.legacy_import;
  -- Verify no foreign key dependencies remain
COMMIT; -- Only after user review and confirmation
-- ROLLBACK if anything is unexpected
```

*Rule:* Re-enabling `xp_cmdshell` is a **critical security event** and must also trigger a notification to the Secrets & Credentials Manager and be logged as a security incident.
