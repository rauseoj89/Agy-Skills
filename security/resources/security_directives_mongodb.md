# Hardened MongoDB Security Directives

When writing, generating, or auditing MongoDB configurations or query implementations, the following security standards must be strictly enforced:

### 1. NoSQL Injection Mitigation
NoSQL queries construct syntax trees using objects. Passing raw client inputs (objects) to queries allows bypassing filters.
- **Vulnerability Example:** If user inputs are parsed directly as objects, passing `{"username": {"$gt": ""}}` bypasses password matches.
- **Rule:** Sanitize input parameters or cast parameters explicitly to strings before query execution:
  ```javascript
  // Express + MongoDB Example
  // WRONG:
  // db.users.find({ username: req.body.username, password: req.body.password })

  // CORRECT:
  const username = String(req.body.username);
  const password = String(req.body.password);
  db.users.find({ username: username, password: password });
  ```
- **Mongoose Sanitization:** Use Mongoose's built-in schema validation or apply libraries like `mongo-sanitize` to strip `$` prefix keys from requests.

### 2. Prohibited Operators (`$where` & `$eval`)
The `$where` operator and `$eval` function execute arbitrary JavaScript strings inside the MongoDB engine, creating severe Server-Side JavaScript Injection vulnerabilities.
- **Prohibited:** Never use the `$where` operator with user inputs, and disable Javascript execution on the MongoDB server config (`security.javascriptEnabled: false`).
- **Approved Safe Pattern:** Use standard query operators (`$eq`, `$expr`, `$match`).
