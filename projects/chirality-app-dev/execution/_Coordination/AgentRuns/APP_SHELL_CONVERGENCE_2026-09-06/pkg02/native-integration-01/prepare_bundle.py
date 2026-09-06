"""Owned bundle preparation only; never launches an application."""
from pathlib import Path
import hashlib, json, plistlib, subprocess
here = Path(__file__).resolve().parent
config = json.loads((here / 'ISOLATION_PREPARATION.json').read_text())
root = Path(config['scratch']).resolve()
assert root.parent == Path('/private/tmp') and root.name.startswith('chirality-native-shell-')
archive = Path(config['archive'])
assert hashlib.sha256(archive.read_bytes()).hexdigest() == config['archiveSha256']
bundle = Path(config['bundlePath'])
assert bundle.parent == root and not bundle.exists()
commands = []
def run(args):
    result = subprocess.run(args, capture_output=True, text=True, timeout=120)
    commands.append({'args': args, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    (here / 'BUNDLE_PREPARATION_COMMANDS.json').write_text(json.dumps(commands, indent=2) + '\n')
    result.check_returncode()
run(['/usr/bin/ditto', '-x', '-k', str(archive), str(root / 'distribution')])
(root / 'distribution/Electron.app').rename(bundle)
changes = []
for p in sorted(bundle.rglob('Info.plist')):
    data = plistlib.loads(p.read_bytes())
    old = data.get('CFBundleIdentifier')
    if not old: continue
    # Every application/helper/framework identity gets its own proof domain.
    data['CFBundleIdentifier'] = config['bundleIdentifier'] + ('' if p == bundle / 'Contents/Info.plist' else '.' + hashlib.sha256(str(p.relative_to(bundle)).encode()).hexdigest()[:12])
    if p == bundle / 'Contents/Info.plist':
        data['CFBundleName'] = config['bundleName']
        data['CFBundleDisplayName'] = config['bundleName']
    p.write_bytes(plistlib.dumps(data))
    changes.append({'path': str(p), 'oldIdentifier': old, 'identifier': data['CFBundleIdentifier']})
# Preserve source archive; only this owned copy is ad hoc signed.
run(['/usr/bin/codesign', '--force', '--deep', '--sign', '-', str(bundle)])
run(['/usr/bin/codesign', '--verify', '--deep', '--strict', str(bundle)])
run(['/usr/bin/codesign', '-d', '--verbose=4', str(bundle)])
(here / 'BUNDLE_IDENTITY.json').write_text(json.dumps({'status': 'PREPARED_NOT_LAUNCHED', 'changes': changes, 'bundle': str(bundle), 'executableSha256': hashlib.sha256((bundle / 'Contents/MacOS/Electron').read_bytes()).hexdigest()}, indent=2) + '\n')
