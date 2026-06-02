# Hardened MySQL Security Directives

When creating, managing, or querying MySQL databases, the following security standards must be strictly enforced:

### 1. Data Safety & Strict SQL Mode
By default, MySQL can silently truncate long data strings or accept invalid values without throwing errors. This behavior can bypass application-level validation and lead to security vulnerabilities.
- **Enforcement:** Ensure strict SQL mode is enabled in the server configuration (`my.cnf`):
  ```ini
  [mysqld]
  sql-mode = "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE"
  ```
- **Verification:** Ensure your runtime application session enforces these modes to prevent silent data alterations.

### 2. Disabling Local File Loading (`local_infile`)
The MySQL command `LOAD DATA LOCAL INFILE` allows reading client-side files and storing them in the database. Attackers exploiting an SQL Injection vulnerability can leverage this feature to read sensitive server files.
- **Server Hardening:** Explicitly disable local infile loading in the server configuration:
  ```ini
  [mysqld]
  local_infile = 0
  ```
- **Client Hardening:** Set `local_infile=0` in connection string parameters (e.g., in Python or PHP PDO connection arrays) to block client-side exploitation.

### 3. Least Privilege & Role Separation
Never deploy an application using administrative accounts or permissions.
- **User Segregation:**
  - **DDL User:** Executes migrations. Owns tables and schemas. Has permissions like `CREATE`, `ALTER`, `DROP`.
  - **DML User:** Runs the web application. Has only `SELECT`, `INSERT`, `UPDATE`, `DELETE` grants.
  - **Global Privileges:** The application DML user must never have global privileges (e.g., `SUPER`, `PROCESS`, `FILE`, `GRANT OPTION`).
- **Targeted Grants:** Grant access only to the specific application database:
  ```sql
  GRANT SELECT, INSERT, UPDATE, DELETE ON app_db.* TO 'app_runner'@'%';
  ```

### 4. Transport Security (Enforced SSL)
Unencrypted connections leak queries, secrets, and data over the network.
- **Server Enforcement:** Enforce SSL connection requirements when creating database roles:
  ```sql
  ALTER USER 'app_runner'@'%' REQUIRE SSL;
  ```
- **Client Configuration:** Require SSL in the client application configuration:
  ```python
  # Example Python connection setup
  conn = pymysql.connect(
      host='db.example.com',
      user='app_runner',
      password='secure_password',
      database='app_db',
      ssl={'ca': '/path/to/ca.pem'}
  )
  ```

### 5. Network Hardening & Administration
- **Local Network Scoping:** Restrict binding to internal interfaces only. Bind to localhost if the database resides on the same machine:
  ```ini
  [mysqld]
  bind-address = 127.0.0.1
  ```
- **Anonymous Users:** Explicitly delete all anonymous users and default `test` databases during installation:
  ```sql
  DELETE FROM mysql.user WHERE User='';
  DROP DATABASE IF EXISTS test;
  FLUSH PRIVILEGES;
  ```

### 6. Destructive MySQL Guard
The following MySQL operations are classified as **destructive** and require explicit user confirmation before execution.

**Destructive MySQL Operations:**

| Operation | Risk |
|---|---|
| `DROP TABLE app_db.<table>` | Permanent deletion of table and all data |
| `TRUNCATE TABLE app_db.<table>` | Permanent deletion of all rows (bypasses foreign key checks) |
| `DELETE FROM app_db.<table>` without `WHERE` | Permanent deletion of all rows |
| `DROP DATABASE app_db` | Permanent deletion of entire database |
| `DELETE FROM mysql.user WHERE User=''` | Deletes anonymous users — verify scope before running |
| `DROP DATABASE test` | Deletes the test database — verify no legitimate data exists |
| `FLUSH PRIVILEGES` | Reloads grant tables — use only after deliberate privilege changes |

**Confirmation Protocol:**
Before any destructive operation:
1. Present the exact SQL statement.
2. State the number of rows or objects affected (run a `SELECT COUNT(*)` or `SHOW TABLES` preview first).
3. Request explicit user confirmation before execution.

```sql
-- SAFE APPROACH: preview before destruction
SELECT COUNT(*) FROM app_db.sessions; -- Confirm scope
-- Only after user confirms:
TRUNCATE TABLE app_db.sessions;
```

*Rule:* `DELETE FROM mysql.user WHERE User=''` and `DROP DATABASE IF EXISTS test` must always be presented to the user as a confirmation dialog even when run as part of a standard MySQL hardening script.
