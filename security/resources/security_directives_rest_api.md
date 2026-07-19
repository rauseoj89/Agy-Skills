# Hardened REST API Security Directives

When designing, implementing, or auditing RESTful APIs, the following security standards must be strictly enforced:

### 1. Robust Authentication & Token Validation (JWT)
JSON Web Tokens (JWT) are commonly misconfigured, leading to session spoofing.
- **Algorithm Verification:** Never trust the `alg` header of incoming tokens. Explicitly enforce the target validation algorithm (e.g., `HS256`, `RS256`) in the verification library:
  ```typescript
  // Node.js example
  jwt.verify(token, publicKey, { algorithms: ['RS256'] });
  ```
- **Prohibited:** Never support or accept the `none` algorithm inside signature verification blocks.
- **Expiration and Revocation:** Always enforce strict expiration (`exp` claim) and validate token lifetimes.

### 2. Authorization (BOLA/IDOR Defense)
Broken Object Level Authorization (BOLA) occurs when users can access resources they do not own by swapping resource IDs.
- **Rule:** Never retrieve or mutate resource entries based solely on user-provided path IDs. Always check resource ownership against the authenticated context:
  ```python
  # Flask / SQLAlchemy Example
  # WRONG:
  # order = Order.query.get(order_id)
  
  # CORRECT:
  order = Order.query.filter_by(id=order_id, owner_id=current_user.id).first()
  if not order:
      return {"error": "Not Found or Unauthorized"}, 404
  ```

### 3. Rate Limiting & DoS Defense
Unauthenticated or heavy API endpoints are vulnerable to Denial of Service and Brute-force attacks.
- **Rule:** Implement rate limiting on all public API routes, especially authentication, password resets, and search endpoints.
- **Configuration:** Enforce dynamic limit windows (e.g., maximum 100 requests per 15 minutes per IP address).

### 4. Robust CORS Configurations
Loose Cross-Origin Resource Sharing (CORS) configurations allow malicious browser domains to read API payloads.
- **Prohibited:** Never use wildcard origins `Access-Control-Allow-Origin: *` in combination with `Access-Control-Allow-Credentials: true`.
- **Approved Safe Pattern:** Explicitly validate incoming origin headers against an environmental domain whitelist before returning access headers.
