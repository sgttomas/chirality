# Probe runner (retained so the probe logs are regenerable)

Each log was produced from `{REPO_ROOT}/projects/chirality-app-dev/frontend`
by this Node `spawnSync` wrapper with a 20 s timeout and `SIGKILL` on expiry
(`status null signal SIGKILL error ETIMEDOUT` in a log means the call never
returned within 20 s):

```
node -e "
const {spawnSync}=require('child_process');
const r=spawnSync('./node_modules/.bin/electron',[<ARGS>,'--user-data-dir=/private/tmp/chirality-s8-probe','<this folder>/safe-storage-probe.js'],{timeout:20000,encoding:'utf8',killSignal:'SIGKILL'});
console.log('status',r.status,'signal',r.signal,'error',r.error&&r.error.code);
console.log('stdout:',r.stdout);console.log('stderr:',r.stderr.slice(0,800));
"
rm -rf /private/tmp/chirality-s8-probe
```

| Log | `<ARGS>` | Session sandbox | Result |
|---|---|---|---|
| (not retained — first attempt) | none | in-sandbox | hung; the wrapper's own 20 s timeout was overrun and the tool call timed out at 60 s (the first run used the default `SIGTERM`, which the hung Electron ignored) |
| `safe-storage-probe.escalated.log` | none | escalated (`dangerouslyDisableSandbox`, human-approved per command) | `status null signal SIGKILL error ETIMEDOUT` after `ready; calling safeStorage.isEncryptionAvailable()` — hangs without the sandbox too |
| `safe-storage-probe.mock-keychain.sandbox.log` | `'--use-mock-keychain'` | in-sandbox | `isEncryptionAvailable=true in 1ms`, exit 0 |

Electron 43.2.0 from `node_modules/electron/dist/Electron.app` (unsigned development binary).
