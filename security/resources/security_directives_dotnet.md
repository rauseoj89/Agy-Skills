# Hardened C# & .NET Security Directives

When writing, generating, or auditing C# or .NET applications, the following security standards must be strictly enforced:

### 1. Entity Framework parameterization
String formatting inside raw SQL methods invites SQL injection.
- **Rule:** Never use raw interpolation in raw query commands. Use parameter objects or FormattableStrings:
  ```csharp
  // CORRECT:
  var user = context.Users.FromSqlInterpolated($"SELECT * FROM Users WHERE Email = {email}").FirstOrDefault();
  ```

### 2. ASP.NET Anti-Forgery Tokens
Stateless APIs and Controller endpoints are vulnerable to Cross-Site Request Forgery (CSRF).
- **Rule:** Enforce `[ValidateAntiForgeryToken]` globally or on state-modifying actions (`POST`, `PUT`, `DELETE`).
- **Razor / Tag Helpers:** Ensure forms are generated with framework helpers which automatically insert tokens.
