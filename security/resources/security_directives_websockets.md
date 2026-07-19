# Hardened WebSocket Security Directives

When implementing or auditing WebSocket connections, the following security standards must be strictly enforced:

### 1. Cross-Site WebSocket Hijacking (CSWSH) Prevention
WebSockets do not automatically validate CORS policies, allowing hostile websites to initiate connection handshakes.
- **Rule:** Validate the `Origin` header during the HTTP connection handshake. Reject handshakes from unknown domains:
  ```go
  // Go Example
  var upgrader = websocket.Upgrader{
      CheckOrigin: func(r *http.Request) bool {
          return r.Header.Get("Origin") == "https://trustedapp.com"
      },
  }
  ```

### 2. Connection Handshake Authentication
WebSockets are persistent TCP connections. Authenticators must run before handshaking.
- **Rule:** Validate user authentication tokens (e.g., JWT) in the initial HTTP Upgrade request before initiating the socket session.
