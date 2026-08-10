'use strict';

const { app, safeStorage } = require('electron');
const { createHash } = require('node:crypto');

const PUBLIC_CONSTANT = 'DAPP94_OPTION_C_PUBLIC_CONSTANT_V1';

if (process.platform === 'darwin') {
  app.setActivationPolicy('prohibited');
}

app.whenReady().then(() => {
  const available = safeStorage.isEncryptionAvailable();
  if (!available) {
    process.stdout.write(JSON.stringify({
      electron: process.versions.electron,
      chrome: process.versions.chrome,
      platform: process.platform,
      isEncryptionAvailable: false,
      roundTrip: false,
      publicConstantSha256: createHash('sha256').update(PUBLIC_CONSTANT).digest('hex')
    }) + '\n');
    app.exit(2);
    return;
  }

  const encrypted = safeStorage.encryptString(PUBLIC_CONSTANT);
  const decrypted = safeStorage.decryptString(encrypted);
  const roundTrip = decrypted === PUBLIC_CONSTANT;
  process.stdout.write(JSON.stringify({
    electron: process.versions.electron,
    chrome: process.versions.chrome,
    platform: process.platform,
    isEncryptionAvailable: true,
    roundTrip,
    ciphertextBytes: encrypted.byteLength,
    publicConstantSha256: createHash('sha256').update(PUBLIC_CONSTANT).digest('hex')
  }) + '\n');
  app.exit(roundTrip ? 0 : 3);
}).catch((error) => {
  process.stderr.write(`DAPP94_PROBE_ERROR:${error instanceof Error ? error.message : String(error)}\n`);
  app.exit(4);
});
