# Hardened GraphQL Security Directives

When designing, implementing, or auditing GraphQL APIs, the following security standards must be strictly enforced:

### 1. Depth Limiting & Complexity Analysis
Unlike REST APIs, GraphQL allows users to request arbitrary nested trees, enabling nested recursion DoS attacks.
- **Rule:** Enforce a maximum query depth limit to prevent deeply nested recursive requests (e.g., maximum depth of 5-8):
  ```typescript
  // Node.js Apollo Server Example
  import depthLimit from 'graphql-depth-limit';

  const server = new ApolloServer({
      schema,
      validationRules: [depthLimit(6)] // Rejects queries with nestings deeper than 6
  });
  ```
- **Complexity Scopes:** For heavy resource queries, apply complexity limits (assign points per field and cap the maximum allowed score per query).

### 2. Introspection and Playground Control
Leaving introspection enabled in production exposes the entire database schema structure to attackers.
- **Rule:** Explicitly disable GraphQL Introspection and schema visualizers (Playground, Sandbox) in production:
  ```typescript
  // Apollo Server production configuration
  const server = new ApolloServer({
      schema,
      introspection: process.env.NODE_ENV !== 'production',
      plugins: [
          process.env.NODE_ENV === 'production' 
              ? ApolloServerPluginLandingPageDisabled() 
              : ApolloServerPluginLandingPageLocalDefault()
      ]
  });
  ```

### 3. Field-Level Authorization (No trusting of Root Resolvers)
GraphQL endpoints have a single HTTP entry point. Checking permissions only on root queries is unsafe.
- **Rule:** Enforce authorization rules inside specific field resolvers, or use directive-based middlewares to verify token permissions before returning nested objects.
