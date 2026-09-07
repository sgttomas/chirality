"""Exact Root-adopted Runtime revisions; recognition never grants execution.

Migration history and current owning acceptance are separate proof subjects.
Adding an adoption requires a new Root-reviewed policy/source identity; there
is no caller override, automatic latest-file acceptance or fixture bypass.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

POLICY = 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_SUCCESSOR_RECOGNITION_2026-09-06/SUCCESSOR_ADOPTIONS.json'
POLICY_SHA = '0c224adac116ffc3931db85cc17050174397a0f447198709ba629b36fa592ea9'
SUPPLEMENT = 'projects/chirality-runtime/execution/_Decomposition/CUSTODY_DISPOSITION_D36.md'


def published_bytes(root: Path, relative: str, expected: bytes) -> bool:
    result = subprocess.run(['git', '-C', str(root), 'show', 'origin/main:' + relative],
                            capture_output=True, check=False)
    return result.returncode == 0 and result.stdout == expected


def recognize(root: Path, baseline: dict[str, str]) -> dict:
    """Validate baseline or an exact owning-accepted revision, without a grant."""
    from root_governance_state import GovernanceError, digest, reference, safe_path

    def current(path):
        p = safe_path(root, path, allow_missing=True)
        return digest(p) if p.is_file() else None

    if all(current(p) == sha for p, sha in baseline.items()) and current(SUPPLEMENT) is None:
        return {'state': 'migration-baseline', 'adoptions': [], 'published': True,
                'current_bindings': dict(baseline), 'execution_authority': False}

    policy_file = reference(root, {'path': POLICY, 'sha256': POLICY_SHA})
    try:
        policy = json.loads(policy_file.read_text())
        if policy['schema'] != 'root-runtime-successor-adoptions/v1':
            raise ValueError('unknown schema')
        reference(root, policy['root_owner_act'])
        adoptions = policy['adoptions']
        if not isinstance(adoptions, list) or not adoptions:
            raise ValueError('empty adoptions')
    except (KeyError, TypeError, ValueError) as exc:
        raise GovernanceError('invalid Root Runtime successor adoption policy') from exc

    expected = dict(baseline)
    chain = []
    for adoption in adoptions:
        try:
            changes = adoption['changes']
            if not isinstance(changes, list) or not changes:
                raise ValueError('empty changes')
            paths = [item['path'] for item in changes]
            if len(paths) != len(set(paths)):
                raise ValueError('duplicate change')
            for item in changes:
                path = item['path']
                if path not in baseline and path != SUPPLEMENT:
                    raise ValueError('outside Runtime successor scope')
                safe_path(root, path, allow_missing=True)
                if expected.get(path) != item['before']:
                    raise ValueError('wrong amendment predecessor')
                if not isinstance(item['after'], str) or len(item['after']) != 64:
                    raise ValueError('invalid postimage identity')
                expected[path] = item['after']
            chain.append(adoption)
        except (KeyError, TypeError, ValueError) as exc:
            raise GovernanceError('invalid bounded Runtime successor change') from exc
        if all(current(p) == sha for p, sha in expected.items()):
            publication = []
            for selected in chain:
                publication.append(_verify_adoption(root, selected))
            # Publication is observed for the exact current files as well as
            # acceptance evidence; branch-local validation is not main effect.
            published = all(publication) and all(
                published_bytes(root, p, safe_path(root, p).read_bytes()) for p in expected)
            return {'state': 'accepted-published' if published else 'accepted-pending-publication',
                    'adoptions': [a['id'] for a in chain], 'published': published,
                    'current_bindings': expected, 'execution_authority': False}
    raise GovernanceError('Runtime current bytes do not match baseline or an exact accepted successor')


def _verify_adoption(root: Path, adoption: dict) -> bool:
    from root_governance_state import GovernanceError, reference, safe_path
    try:
        acceptance = reference(root, adoption['acceptance'])
        subject = reference(root, adoption['subject'])
        if adoption['subject']['sha256'] not in acceptance.read_text():
            raise ValueError('acceptance does not bind subject')
        payload = json.loads(subject.read_text())
        if payload.get('pathBase') != 'repository root':
            raise ValueError('unknown subject path base')
        members = payload['files']
        if not isinstance(members, list) or not members:
            raise ValueError('empty subject')
        by_path = {}
        published = published_bytes(root, adoption['acceptance']['path'], acceptance.read_bytes())
        published &= published_bytes(root, adoption['subject']['path'], subject.read_bytes())
        for item in members:
            if item['path'] in by_path:
                raise ValueError('duplicate subject member')
            member = reference(root, item)
            by_path[item['path']] = item['sha256']
            published &= published_bytes(root, item['path'], member.read_bytes())
        index_ref = adoption['postimage_index']
        if by_path.get(index_ref['path']) != index_ref['sha256']:
            raise ValueError('postimage index is not in accepted subject')
        index = json.loads(reference(root, index_ref).read_text())
        projected = [{'path': row['target'], 'before': row['preimageSha256'],
                      'after': row['postimageSha256']} for row in index]
        if projected != adoption['changes']:
            raise ValueError('accepted postimage index differs from Root adoption')
        # Live current bytes were checked against the same accepted hashes by
        # recognize(); index-local candidate postimage paths confer no grants.
        return bool(published)
    except (KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, GovernanceError):
            raise
        raise GovernanceError('invalid owning Runtime acceptance evidence') from exc
