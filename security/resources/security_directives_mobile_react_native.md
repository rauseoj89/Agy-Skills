# Hardened Mobile React Native Security Directives

When developing or auditing React Native mobile applications, the following security standards must be strictly enforced:

### 1. Secure Data Storage
Standard storage mechanisms (e.g., AsyncStorage) write values to device disks in plaintext.
- **Rule:** Never store JWTs, API secrets, or PII in AsyncStorage.
- **Safe Alternative:** Use platform Keychain/Keystore wrappers (e.g., `react-native-keychain` or `expo-secure-store`).

### 2. Certificate Pinning
Mobile applications are vulnerable to Man-in-the-Middle (MITM) attacks via user-installed root certificates.
- **Rule:** Enforce SSL Pinning for backend APIs using libraries (e.g., `react-native-ssl-pinning` or native network trust managers) to validate exact certificate hashes.
