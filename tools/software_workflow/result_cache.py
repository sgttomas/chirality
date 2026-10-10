#!/usr/bin/env python3
"""Fingerprint successful Piping verification, never substitute a nearby cache key."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def included(path):
    parts = Path(path).parts
    # Match the product jobs' sparse checkout: execution records are unavailable.
    if parts[0] == 'execution' or (len(parts) > 2 and parts[0] == 'projects' and parts[2] == 'execution'):
        return False
    # Conservative first version: every other tracked input participates,
    # including Python tests and fixtures. No inferred dependency exclusions.
    return True


def fingerprint(root, suite, commands, environment):
    tree = subprocess.check_output(['git', '-C', str(root), 'ls-tree', '-r', '-z', 'HEAD'])
    entries = [entry.decode() for entry in tree.split(b'\0') if entry and included(entry.split(b'\t', 1)[1].decode())]
    payload = dict(version=1, suite=suite, tree=entries, commands=commands, environment=environment)
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['key', 'save', 'reuse'])
    parser.add_argument('--suite', choices=['numerical', 'browser'], required=True)
    parser.add_argument('--plan', type=Path)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    if args.action == 'key':
        commands = ['production-build', 'chromium-desktop:r2-smoke,b3b-project-persistence']
        if args.suite == 'numerical':
            path = ROOT / 'projects/chirality-piping/tools/ci/numerical_ci.py'
            spec = importlib.util.spec_from_file_location('numerical_cache_plan', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plan = json.loads(args.plan.read_text())
            _, commands = module.cargo_plan(ROOT / 'projects/chirality-piping', plan.get('paths'))
        environment = {key: os.environ.get(key, '') for key in ['ImageOS', 'ImageVersion', 'RUNNER_OS', 'RUNNER_ARCH']}
        # Missing runner identity cannot establish equivalent execution conditions.
        if not all(environment.values()):
            raise SystemExit('Runner image identity unavailable; cannot key verification reuse')
        environment['python'] = platform.python_version()
        if args.suite == 'browser':
            environment['node'] = subprocess.check_output(['node', '--version'], text=True).strip()
        key = 'verified-v1-' + args.suite + '-' + fingerprint(ROOT, args.suite, commands, environment)
        with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
            stream.write('key=' + key + '\n')
        print(key)
        return
    key = os.environ['RESULT_KEY']
    if args.action == 'save':
        args.record.parent.mkdir(parents=True, exist_ok=True)
        record = dict(key=key, conclusion='success', head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                      run=f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}")
        args.record.write_text(json.dumps(record))
    else:
        record = json.loads(args.record.read_text())
        if record.get('key') != key or record.get('conclusion') != 'success' or not record.get('run'):
            raise SystemExit('Cached verification record does not match these inputs')
        message = f"Reused successful {args.suite} verification from {record['run']} (source head {record['head']}); exact input/environment key {key}. No tests executed in this job."
        print(message)
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as stream:
            stream.write(message + '\n')


if __name__ == '__main__':
    main()
