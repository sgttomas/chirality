#!/usr/bin/env python3
"""Validate explicitly discoverable workflow entrypoints and optional execution policy."""
import argparse
import json
import re
from pathlib import Path
import yaml

ROLES={'HELP_HUMAN','HELPS_HUMANS','WORKING_ITEMS','TASK'}


def validate_workflow_dir(folder, repo_root):
    issues=[]
    try:
        text=(folder/'WORKFLOW.md').read_text()
        if not text.startswith('---\n'):
            raise ValueError('WORKFLOW.md must start with YAML frontmatter')
        data=yaml.safe_load(text.split('---',2)[1])
        if not isinstance(data,dict):
            raise ValueError('frontmatter must be a mapping')
        if data.get('name')!=folder.name or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}',folder.name):
            issues.append('name must match the lowercase-hyphen folder name')
        if not isinstance(data.get('description'),str) or not data['description'].strip():
            issues.append('description must be a nonempty string')
        companion=folder/'execution.json'
        if companion.exists():
            config=json.loads(companion.read_text())
            if config.get('schema_version')!=1: issues.append('execution schema_version must be 1')
            if 'stages' in config: issues.append('stage role overrides are unsupported; select a bounded workflow or brief')
            stages={}
            if not isinstance(stages,dict): raise ValueError('stages must be a mapping')
            for item in [config,*stages.values()]:
                compatible=item.get('compatible_roles')
                if compatible is not None and (not isinstance(compatible,list) or not compatible or not set(compatible)<=ROLES): issues.append('invalid compatible_roles')
                tools=item.get('tools',{})
                if not isinstance(tools,dict) or set(tools)-{'capabilities','commands'}: raise ValueError('invalid tools mapping')
                for kind,values in tools.items():
                    if not isinstance(values,list) or any(not isinstance(x,str) for x in values): raise ValueError('tool restrictions must be string lists')
                    if kind=='commands':
                        for command in values:
                            parts=command.rsplit(':',1)
                            if len(parts)!=2 or len(parts[0].split())!=2 or not parts[1]: raise ValueError('invalid command/scope expression')
                            tool=parts[0].split()[1]
                            path=(repo_root/tool).resolve()
                            if not tool.startswith('tools/') or not path.is_relative_to((repo_root/'tools').resolve()) or not path.is_file(): issues.append(f'unresolved command: {tool}')
    except (OSError, ValueError, TypeError, AttributeError, yaml.YAMLError) as exc:
        issues.append(str(exc))
    return {'workflow':folder.name,'valid':not issues,'issues':issues}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[2]/'workflows')
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args(); root=args.root.resolve()
    if not root.is_dir(): parser.exit(2,f'ERROR: missing workflows root {root}\n')
    results=[validate_workflow_dir(p,root.parent) for p in sorted(root.iterdir()) if p.is_dir() and not p.name.startswith('.')]
    report={'checked_workflow_count':len(results),'invalid_workflow_count':sum(not r['valid'] for r in results),'results':results}
    print(json.dumps(report,indent=2) if args.json else '\n'.join(f"{'PASS' if r['valid'] else 'FAIL'} {r['workflow']}: {'; '.join(r['issues'])}" for r in results))
    return int(bool(report['invalid_workflow_count'] or not results))

if __name__=='__main__': raise SystemExit(main())
