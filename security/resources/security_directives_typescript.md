# Hardened TypeScript Security Directives

When writing, generating, or auditing TypeScript code, the following security standards must be strictly enforced:

### 1. Strict Typing and the `any` Danger
Bypassing the type compiler with `any` strips away compilation-time safety guarantees, hiding potential runtime errors and security bugs.
- **Prohibited:** Never use the `any` type for parameters, return values, or variables.
- **Enforcement:** Enforce `"noImplicitAny": true` in `tsconfig.json`.
- **Safe Alternative:** Use `unknown` for values of unknown types. Perform type narrowing (e.g., using `typeof`, `instanceof`, or custom type guards) before operating on them:
  ```typescript
  // CORRECT:
  function processInput(input: unknown) {
      if (typeof input === "string") {
          console.log(input.trim()); // Safe type-narrowed execution
      }
  }
  ```

### 2. Secure Type Assertions
Type assertions (`as Type` or `<Type>`) override TypeScript's static analysis. Inappropriate assertions can hide missing validation.
- **Rule:** Never force-assert a broad dictionary/object (e.g., parsed JSON from API) to a typed interface without schema validation:
  ```typescript
  // WRONG:
  const user = JSON.parse(userInput) as User; // Vulnerable if properties are missing/malformed

  // CORRECT:
  import { z } from 'zod';
  const UserSchema = z.object({ id: z.string(), email: z.string().email() });
  const user = UserSchema.parse(JSON.parse(userInput)); // Validated at runtime
  ```

### 3. Non-Null Assertions
The non-null assertion operator `!` tells the compiler to ignore `null` and `undefined` checks.
- **Prohibited:** Never use `obj!.property` to bypass strict null checks.
- **Approved Safe Pattern:** Use optional chaining (`obj?.property`) or explicit conditional guards:
  ```typescript
  // CORRECT:
  const email = user?.contactInfo?.email ?? "default@example.com";
  ```

### 4. Direct Run-time Custom Type Guards
TypeScript's types are erased at compile time. Ensure type guards validate structure at runtime:
```typescript
interface SecuredPayload {
    token: string;
    expires: number;
}

// CORRECT: Runtime verification is required
function isSecuredPayload(obj: any): obj is SecuredPayload {
    return (
        obj &&
        typeof obj.token === 'string' &&
        typeof obj.expires === 'number'
    );
}
```
