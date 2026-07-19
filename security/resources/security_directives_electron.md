# Hardened Electron Security Directives

When developing or auditing Electron desktop applications, the following security standards must be strictly enforced:

### 1. Disable Node.js Integration in Renderer Processes
- **Rule:** Set `nodeIntegration: false` in BrowserWindow webPreferences. Enabling Node integration inside renderers allows web vulnerabilities (e.g., XSS) to escalate into full OS shell takeovers.

### 2. Enable Context Isolation
- **Rule:** Set `contextIsolation: true` in BrowserWindow webPreferences. This creates distinct JS execution contexts for Electron internal preload scripts and website scripts.
  ```javascript
  const mainWindow = new BrowserWindow({
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true
    }
  })
  ```
