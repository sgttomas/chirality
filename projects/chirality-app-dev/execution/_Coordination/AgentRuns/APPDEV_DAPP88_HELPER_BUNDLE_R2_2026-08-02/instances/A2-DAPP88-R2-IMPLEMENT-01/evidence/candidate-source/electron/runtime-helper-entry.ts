/**
 * Standalone runtime-helper entry.
 *
 * This file is compiled as the `main` of the independently built helper app.
 * It selects the existing App-owned daemon posture before loading the shared
 * desktop main module. The helper is therefore a complete Electron product,
 * not a copied or post-mutated Chirality GUI bundle.
 */
import { app } from 'electron';

// The helper never creates a BrowserWindow. Keeping Chromium services in this
// process avoids an otherwise unnecessary GPU/network child topology and, on
// macOS, preserves Electron's first-signal `before-quit` funnel for the daemon.
// The separately built bundle still carries the matching builder-generated
// child applications required by Electron's native package contract.
app.commandLine.appendSwitch('single-process');
app.commandLine.appendSwitch('disable-gpu');

if (!process.argv.includes('--runtime-daemon')) {
  process.argv.push('--runtime-daemon');
}

void import('./main');
