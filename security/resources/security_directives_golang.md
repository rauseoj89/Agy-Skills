# Hardened Go Security Directives

When writing, generating, or auditing Go code, the following security standards must be strictly enforced:

### 1. Database Parameterization (No String Formatting in SQL)
Concatenating raw strings in queries triggers critical SQL injections.
- **Rule:** Use placeholders (`?`, `$1`) in query functions. Never use `fmt.Sprintf` or string additions to build SQL:
  ```go
  // CORRECT:
  rows, err := db.QueryContext(ctx, "SELECT id, name FROM users WHERE age = ?", targetAge)
  ```
- **ORM Parameters (GORM):** Ensure conditions use query templates:
  ```go
  // CORRECT:
  db.Where("email = ?", userInput).First(&user)
  ```

### 2. Command Execution Safety
Spawning OS commands with raw shell executables invites shell injections.
- **Rule:** Never execute raw user inputs via a command shell interpreter (e.g., `sh -c`). Use exact arguments in arrays:
  ```go
  // CORRECT:
  cmd := exec.CommandContext(ctx, "git", "checkout", branchName)
  err := cmd.Run()
  ```

### 3. Safe Path Handling & File Traversal Prevention
Dynamic filepath additions are susceptible to directory traversals.
- **Rule:** Do not rely on simple string checks. Use `filepath.Clean` and check directory prefixes:
  ```go
  // CORRECT:
  cleanPath := filepath.Clean(userInputPath)
  if !strings.HasPrefix(cleanPath, safeBaseDir) {
      return errors.New("unauthorized file access attempt")
  }
  ```
