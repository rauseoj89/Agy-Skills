# Hardened Redis Security Directives

When writing configurations or using Redis instances, the following security standards must be strictly enforced:

### 1. Enforce Authentication
- **Rule:** Never run Redis without access credentials. Set the `requirepass` password parameter in `redis.conf`, or configure Redis ACLs (Access Control Lists).

### 2. Disable Dangerous Commands
Admin commands are vulnerable to command injection and remote service disruption.
- **Rule:** Rename or disable risky commands inside the `redis.conf` configuration:
  ```text
  rename-command FLUSHALL ""
  rename-command FLUSHDB ""
  rename-command CONFIG ""
  rename-command KEYS ""
  ```
- **Network Isolation:** Only bind Redis to internal loopback adapters (`bind 127.0.0.1 ::1`) or private subnets.
