# Hardened Java & Spring Security Directives

When writing, generating, or auditing Java or Spring Boot applications, the following security standards must be strictly enforced:

### 1. XML External Entity (XXE) Protection
By default, standard Java XML parsers resolve external entities, exposing the host to local file disclosure and SSRF.
- **Rule:** Explicitly disable DTDs (Document Type Definitions) in XML parsers:
  ```java
  DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
  dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
  ```

### 2. Spring Security Authentication and `@PreAuthorize`
Methods securing business layers must be protected from authentication bypasses.
- **Rule:** Apply `@PreAuthorize` annotations on Service layer methods using SpEL, and verify access roles:
  ```java
  @PreAuthorize("hasRole('ROLE_ADMIN')")
  public void deleteSystemRecord(Long recordId) { ... }
  ```

### 3. Log4j and JNDI Injections
Using dynamic strings in log engines (e.g., Log4j) can trigger remote code executions.
- **Rule:** Always sanitise inputs before logging, keep dependencies updated, and block JNDI lookups in logging setups.
