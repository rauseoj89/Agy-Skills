# Hardened Container & Kubernetes Security Directives

When designing, deploying, auditing, or reviewing Docker containers or Kubernetes workloads, the following security standards must be strictly enforced:

### 1. Non-Root Container Execution
Running containers as root is the most common and dangerous container misconfiguration. All container workloads must enforce non-root execution at the pod and container specification level.
- **Docker:** Explicitly define a non-root user in the Dockerfile:
  ```dockerfile
  RUN groupadd -r appgroup && useradd -r -g appgroup -s /sbin/nologin appuser
  USER appuser
  ```
- **Kubernetes:** Enforce via security context on every pod spec:
  ```yaml
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    runAsGroup: 1001
  ```
  *Rule:* Never deploy a pod spec without an explicit `securityContext`. Default is root.

### 2. Read-Only Root Filesystems
Containers with writable root filesystems allow attackers to install tools, modify binaries, or persist malware after a breach.
- **Docker:** Use `--read-only` flag or specify in Compose:
  ```yaml
  services:
    app:
      read_only: true
      tmpfs:
        - /tmp   # Mount writable tmpfs only for directories that truly need it
  ```
- **Kubernetes:**
  ```yaml
  securityContext:
    readOnlyRootFilesystem: true
  ```
  *Rule:* If the application writes temporary files, mount a specific `emptyDir` or `tmpfs` volume for that path — do not make the entire root filesystem writable.

### 3. Kubernetes RBAC Least Privilege
Kubernetes Role-Based Access Control must follow the least-privilege principle. Broad cluster-level permissions are a critical escalation vector.
- **Namespace Scoping:** Always use `Role` (namespace-scoped) rather than `ClusterRole` unless cluster-wide access is explicitly required and justified.
- **No ClusterAdmin Grants:** Never bind the `cluster-admin` ClusterRole to a service account or human user unless it is a break-glass emergency account with strict audit logging.
- **Service Account Isolation:** Every application should run under its own dedicated service account, never the `default` service account:
  ```yaml
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: app-service-account
    namespace: production
  ---
  # Pod spec
  spec:
    serviceAccountName: app-service-account
  ```
- **Token Automounting:** Disable automatic service account token mounting when the pod does not call the Kubernetes API:
  ```yaml
  spec:
    automountServiceAccountToken: false
  ```

### 4. Container Image Scanning & Vulnerability Management
Every container image in the build pipeline must be scanned for known CVEs before deployment.
- **Scanning Tools:** Use industry-standard scanners such as **Trivy** or **Grype**:
  ```bash
  # Scan an image with Trivy before pushing
  trivy image --exit-code 1 --severity CRITICAL myapp:latest
  ```
- **Blocking Policy:** Images with **CRITICAL** severity CVEs must be blocked from deployment. HIGH severity CVEs must be tracked and remediated within the sprint cycle.
- **Base Image Hygiene:** Always use minimal, regularly-patched base images (e.g., `alpine`, `distroless`). Avoid `latest` tags in production — pin to a specific digest:
  ```dockerfile
  FROM node:20-alpine@sha256:abc123...
  ```
- **Multi-Stage Builds:** Use multi-stage builds to exclude build-time dependencies, source code, and credentials from the final production image.

### 5. Secrets Management in Kubernetes
Kubernetes environment variables expose secrets in pod definitions, event logs, and process listings. This is prohibited.
- **Prohibited Pattern:** Never inject secrets as environment variables in pod specs:
  ```yaml
  # WRONG - secret exposed in pod spec and logs
  env:
    - name: DB_PASSWORD
      value: "supersecret"
  ```
- **Correct Pattern — Volume Mount:** Mount secrets as files into a read-only volume:
  ```yaml
  volumes:
    - name: db-creds
      secret:
        secretName: database-credentials
  containers:
    - name: app
      volumeMounts:
        - name: db-creds
          mountPath: /run/secrets/db
          readOnly: true
  ```
- **External Vaults:** For production workloads, integrate with an external secret manager (e.g., Vault Bridge MCP, AWS Secrets Manager, or Azure Key Vault) using a secrets injection sidecar or CSI driver rather than native Kubernetes Secrets, which are only base64-encoded by default.
- *Rule:* All secret volume mounts must specify `readOnly: true`.

### 6. Default-Deny Network Policies
By default, Kubernetes pods can communicate freely with all other pods in the cluster. This violates network least-privilege and enables lateral movement after a breach.
- **Default Deny All:** Apply a default-deny NetworkPolicy to every namespace:
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: default-deny-all
    namespace: production
  spec:
    podSelector: {}   # Selects all pods in namespace
    policyTypes:
      - Ingress
      - Egress
  ```
- **Explicit Allow Rules:** Add explicit policies only for required communication paths:
  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: allow-app-to-db
    namespace: production
  spec:
    podSelector:
      matchLabels:
        app: database
    ingress:
      - from:
          - podSelector:
              matchLabels:
                app: backend
        ports:
          - port: 5432
  ```

### 7. Runtime Threat Detection (Falco)
Static configuration hardening is insufficient. Runtime behavioral monitoring is required to detect privilege escalation, unexpected syscalls, and container breakouts.
- **Falco Integration:** Deploy Falco or an equivalent runtime security tool as a DaemonSet on all nodes:
  - Monitor for: shell spawning inside containers, privilege escalation attempts, sensitive file reads (`/etc/shadow`, `/etc/passwd`), unexpected network connections
- **Alert Rules (Examples):**
  ```yaml
  - rule: Shell Spawned in Container
    desc: Detect shell execution inside a running container
    condition: spawned_process and container and proc.name in (shell_binaries)
    output: "Shell spawned in container (user=%user.name container=%container.name)"
    priority: WARNING
  ```
- **Response:** Falco alerts must feed into the SIEM/alerting pipeline. Critical alerts (e.g., container escape attempts) must trigger automated pod termination or quarantine.

### 8. Destructive Container Operations Gate
The following container operations are classified as **destructive** and require explicit user confirmation before execution:

| Operation | Risk Level | Requires Confirmation |
|---|---|---|
| `docker rm <container>` | High — data loss if volume not persisted | Yes |
| `docker-compose down -v` | Critical — permanently deletes named volumes | Yes |
| `kubectl delete namespace <ns>` | Critical — deletes all resources in namespace | Yes |
| `kubectl delete pod <pod>` (stateful) | High — potential service disruption | Yes |
| Docker image pruning (`docker image prune -a`) | Medium — removes untagged images | Yes |
| Volume deletion (`docker volume rm`) | Critical — permanent data loss | Yes |

*Rule:* Before suggesting or executing any of these operations, the Security Engineer must display the exact command, describe the data at risk, and request explicit user confirmation. This gate cannot be bypassed by automation scripts or runbooks.
