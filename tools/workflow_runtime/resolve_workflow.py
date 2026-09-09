#!/usr/bin/env python3
"""Resolve explicitly selected context. This utility reports policy; it is not a sandbox."""
from __future__ import annotations
import argparse
import hashlib
import fnmatch
import posixpath
import json
import re
from pathlib import Path

NAME = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')


def contained(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f'missing or escaping resource: {relative}')
    return path


def fingerprint(path: Path, root: Path, content: bool = False) -> dict:
    raw = path.read_bytes()
    item = {'path': str(path.relative_to(root)), 'source_root': str(root), 'sha256': hashlib.sha256(raw).hexdigest()}
    if content:
        item['content'] = raw.decode('utf-8')
    return item


def intersect(*policies):
    """None inherits; [] denies. Exact command expressions remain conservative."""
    if any(not isinstance(p, list) or any(not isinstance(x, str) for x in p) for p in policies if p is not None):
        raise ValueError('tool restrictions must be lists of strings')
    present = [set(p) for p in policies if p is not None]
    return sorted(set.intersection(*present)) if present else None


def resolve_tool(tool_root: Path, tool: str) -> str:
    if not tool.startswith('tools/'):
        raise ValueError('repository commands must name tools/ paths')
    resolved = contained(tool_root, tool)
    allowed = (tool_root / 'tools').resolve()
    if not allowed.is_relative_to(tool_root.resolve()) or not resolved.is_relative_to(allowed):
        raise ValueError('command path escapes declared tools directory')
    return str(resolved)


def command_constraints(layers, root, bindings):
    groups = []
    resolved = []
    for layer in layers:
        commands = layer.get('commands')
        if commands is None:
            continue
        if not isinstance(commands, list) or any(not isinstance(x, str) for x in commands):
            raise ValueError('command restrictions must be string lists')
        group = []
        for expression in commands:
            try:
                bound = expression.format_map(bindings)
            except (KeyError, ValueError) as exc:
                raise ValueError(f'unbound command expression: {expression}') from exc
            parts = bound.rsplit(':', 1)
            if len(parts) != 2 or not parts[1] or len(parts[0].split()) != 2:
                raise ValueError(f'invalid command expression: {expression}')
            interpreter, tool = parts[0].split()
            absolute = resolve_tool(root, tool)
            group.append(bound)
            resolved.append({'expression': bound, 'interpreter': interpreter, 'tool': absolute, 'scope': parts[1]})
        groups.append(group)
    return {'all_of': groups}, resolved


def command_allowed(constraints, interpreter, tool, targets):
    """Evaluate explicit command/target claims; a host must extract actual effects.

    Each present policy is conjunctive. Alternatives within one policy are OR.
    Empty policy denies; no policies inherit. Every target must satisfy each layer.
    """
    targets = [posixpath.normpath(target) for target in targets]
    for alternatives in constraints['all_of']:
        matches = []
        for expression in alternatives:
            prefix, scope = expression.rsplit(':', 1)
            if prefix.split() == [interpreter, tool]:
                matches.append(scope)
        if not matches or not targets or not all(any(fnmatch.fnmatchcase(target, scope) for scope in matches) for target in targets):
            return False
    return True


def resolve(root: Path, role: str, workflow=None, task_skill=None, resources=(), stage=None, policy=None, legacy_agent=None):
    root = root.resolve()
    registry_path = contained(root, 'agents/registry.json')
    registry = json.loads(registry_path.read_text())
    if not isinstance(registry, dict) or registry.get('schema_version') != 1 or not isinstance(registry.get('roles'), dict) or role not in registry['roles']:
        raise ValueError('unsupported registry or unknown role')
    # Historical underscore spelling is accepted only for TaskSkill.
    if task_skill is not None:
        task_skill = task_skill.replace('_', '-')
    selected = [v for v in (workflow, task_skill) if v is not None]
    alias = None
    if legacy_agent:
        aliases = json.loads(contained(root, 'workflows/legacy-agents.json').read_text())
        alias = aliases['aliases'].get(legacy_agent)
        if alias is None or alias['role'] != role:
            raise ValueError('unknown legacy agent or incompatible target role')
        if alias.get('workflow'):
            selected.append(alias['workflow'])
        if stage and alias.get('stage') and stage != alias['stage']:
            raise ValueError('conflicting legacy stage')
        stage = stage or alias.get('stage')
    if len(set(selected)) > 1:
        raise ValueError('conflicting Workflow/TaskSkill/legacy-agent selections')
    name = selected[0] if selected else None
    role_config = registry['roles'][role]
    if not isinstance(role_config, dict) or not isinstance(role_config.get('tools'), list) or not isinstance(role_config.get('instruction'), str):
        raise ValueError('malformed role configuration')
    context = [fingerprint(contained(root, role_config['instruction']), root, True)]
    basis = [fingerprint(registry_path, root)]
    if legacy_agent:
        basis.append(fingerprint(contained(root, 'workflows/legacy-agents.json'), root))
    execution = {}
    stage_config = {}
    if name:
        if not NAME.fullmatch(name):
            raise ValueError('invalid workflow name')
        package = (root / 'workflows' / name).resolve()
        if not package.is_relative_to((root / 'workflows').resolve()) or not package.is_relative_to(root):
            raise ValueError('workflow package escapes declared root')
        context.append(fingerprint(contained(package, 'WORKFLOW.md'), root, True))
        companion = package / 'execution.json'
        if companion.exists():
            execution = json.loads(contained(package, 'execution.json').read_text())
            if execution.get('schema_version') != 1:
                raise ValueError('unsupported execution schema')
            basis.append(fingerprint(companion.resolve(), root))
        if stage:
            raise ValueError('select bounded workflow resources explicitly; stage overrides are unsupported')
        compatible = execution.get('compatible_roles')
        if compatible is not None and role not in compatible:
            raise ValueError('workflow/stage incompatible with role')
        for resource in dict.fromkeys(resources):
            context.append(fingerprint(contained(package, resource), root, True))
    elif resources or stage:
        raise ValueError('resources and stage require a workflow')
    policy = policy or {}
    if not isinstance(policy,dict):raise ValueError('policy must be a mapping')
    tool_policies = [policy.get('host', {}), {'capabilities': role_config['tools']}, execution.get('tools', {}), stage_config.get('tools', {}), policy.get('brief', {})]
    if not isinstance(policy, dict) or any(not isinstance(p, dict) for p in tool_policies):
        raise ValueError('policy layers must be mappings')
    commands, resolved_commands = command_constraints(tool_policies, root, policy.get('bindings', {}))
    effective = {'capabilities': intersect(*(p.get('capabilities') for p in tool_policies)), 'commands': commands}
    return {'schema_version':1, 'role':role, 'workflow':name, 'stage':stage, 'legacy_alias':alias, 'role_configuration':role_config, 'execution':execution, 'effective_tools':effective, 'resolved_commands':resolved_commands, 'context':context, 'configuration_basis':basis, 'instruction_root':str(root), 'tool_root':str(root / 'tools'), 'context_evidence':'mechanically-recorded resolver inputs; host context delivery unverified', 'enforcement':'instruction-asserted; host must enforce effective restrictions'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    p.add_argument('--role',required=True)
    p.add_argument('--workflow'); p.add_argument('--task-skill'); p.add_argument('--legacy-agent')
    p.add_argument('--brief',type=Path,help='Structured inline brief JSON; explicit paths are rooted at --repo-root')
    p.add_argument('--repo-root',type=Path,help='Active writable checkout root, required with --brief')
    p.add_argument('--resource',action='append',default=[]); p.add_argument('--policy',type=Path)
    args=p.parse_args()
    try:
        policy=json.loads(args.policy.read_text()) if args.policy else {}
        brief=None
        if args.brief:
            from normalize_brief import load_brief
            if not args.repo_root:raise ValueError('--brief requires --repo-root')
            brief=load_brief(json.loads(args.brief.read_text()),args.repo_root,args.root)
            for cli, field in [('workflow','Workflow'),('task_skill','TaskSkill')]:
                supplied=getattr(args,cli)
                if supplied and brief.get(field) and supplied!=brief[field]:raise ValueError(f'CLI/brief disagree on {field}')
                setattr(args,cli,supplied or brief.get(field))
            policy.setdefault('bindings',{}).update({'scope_path':brief['ScopePath'],'WORKING_ROOT':brief['WorkingRoot'],'INSTRUCTION_ROOT':str(args.root.resolve()),'REPO_ROOT':str(args.repo_root.resolve())})
            if 'AllowedTools' in brief:
                inherited=policy.setdefault('brief',{})
                if 'commands' in inherited and inherited['commands']!=brief['AllowedTools']:raise ValueError('brief command policy has conflicting sources')
                inherited['commands']=brief['AllowedTools']
        result=resolve(args.root,args.role,args.workflow,args.task_skill,args.resource,None,policy,args.legacy_agent)
        if args.policy:
            result['configuration_basis'].append(fingerprint(args.policy.resolve(),args.policy.resolve().parent))
        if brief:
            if result['role_configuration'].get('write_scope') == 'none':
                brief['AllowedWriteTargets'] = []
            result['brief']=brief
            result['configuration_basis'].append(fingerprint(args.brief.resolve(),args.brief.resolve().parent))
            if brief.get('file_brief'):
                path=Path(brief['file_brief'])
                result['configuration_basis'].append(fingerprint(path,path.parent))
    except (ValueError, KeyError, OSError, TypeError, AttributeError) as exc:
        p.exit(2,f'ERROR: {exc}\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
