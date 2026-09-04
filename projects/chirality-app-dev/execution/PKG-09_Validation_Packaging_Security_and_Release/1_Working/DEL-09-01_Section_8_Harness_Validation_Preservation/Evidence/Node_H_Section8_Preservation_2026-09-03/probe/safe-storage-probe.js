const { app, safeStorage } = require('electron');
app.setActivationPolicy && process.platform === 'darwin' && app.setActivationPolicy('prohibited');
app.whenReady().then(() => {
  const t0 = Date.now();
  console.log('ready; calling safeStorage.isEncryptionAvailable()');
  const ok = safeStorage.isEncryptionAvailable();
  console.log(`isEncryptionAvailable=${ok} in ${Date.now() - t0}ms`);
  app.exit(0);
});
