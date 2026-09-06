from pathlib import Path
import json
import os
import shutil
import subprocess

working_root = Path(__file__).resolve().parents[5]
frontend = working_root / 'frontend'
output = Path(__file__).resolve().parent / 'release-quality-v2-host'
output.mkdir()
argv = ['npm', 'run', 'validate:release-quality', '--', '--skip-premerge',
        'Current frozen Workflows source registered premerge returned actual HTTP 503 for session list/create/boot without configured runtime daemon binding. App AGENTS permits configured PR CI deferral; this is not premerge PASS.']
assert (frontend / 'package.json').is_file()
result = subprocess.run(argv, cwd=frontend, text=True, capture_output=True)
(output / 'stdout.log').write_text(result.stdout)
(output / 'stderr.log').write_text(result.stderr)
(output / 'COMMAND.json').write_text(json.dumps({
    'argv': argv, 'cwd': str(frontend), 'exit_code': result.returncode,
    'host_escalation': 'Approved fixture checks require isolated loopback services',
    'binding_environment_present': {name: bool(os.environ.get(name)) for name in [
        'CHIRALITY_RUNTIME_SOCKET_PATH', 'CHIRALITY_RUNTIME_TOKEN_FILE',
        'CHIRALITY_RUNTIME_PROJECT_ID', 'CHIRALITY_RUNTIME_PROJECT_ROOT']}
}, indent=2) + '\n')
artifacts = frontend / 'artifacts/harness/release-quality/latest'
if artifacts.exists():
    shutil.copytree(artifacts, output / 'artifacts')
print(json.dumps({'exit_code': result.returncode, 'output': str(output)}))
raise SystemExit(result.returncode)
