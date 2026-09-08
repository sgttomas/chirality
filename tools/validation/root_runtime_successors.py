"""Exact Root-adopted Runtime revisions; recognition never grants execution.

Migration history and current owning acceptance are separate proof subjects.
Adding an adoption requires a new Root-reviewed policy/source identity; there
is no caller override, automatic latest-file acceptance or fixture bypass.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

POLICY = 'execution/_Coordination/AgentRuns/ROOT_RUNTIME_ACCOUNT_AUTHORITY_ADOPTION_2026-09-07/SUCCESSOR_ADOPTIONS.json'
POLICY_SHA = 'b95b60481a08124aa6f1a8c3625e5f1cea3931794c616e8c305be8c72254736d'
SUPPLEMENT = 'projects/chirality-runtime/execution/_Decomposition/CUSTODY_DISPOSITION_D36.md'
ACCOUNT_SUPPLEMENT = 'projects/chirality-runtime/execution/_Decomposition/ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md'


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

    def absent(path):
        return not safe_path(root, path, allow_missing=True).exists()

    if (all(current(p) == sha for p, sha in baseline.items()) and
            absent(SUPPLEMENT) and absent(ACCOUNT_SUPPLEMENT)):
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
                if path not in baseline and path not in {SUPPLEMENT, ACCOUNT_SUPPLEMENT}:
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
        if 'acceptance_manifest' in adoption:
            return _verify_accepted_chain(root, adoption, acceptance, subject, payload)
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


def _verify_members(root: Path, payload: dict, base: str) -> tuple[dict[str, str], bool]:
    """Verify one immutable manifest's members and return original-name hashes."""
    from root_governance_state import reference
    members = payload['members'] if 'members' in payload else payload['files']
    if not isinstance(members, list) or not members:
        raise ValueError('empty manifest members')
    by_path = {}
    published = True
    for item in members:
        original = item['path']
        if original in by_path:
            raise ValueError('duplicate manifest member')
        path = original if original.startswith('projects/') else str(Path(base) / original)
        normalized = {'path': path, 'sha256': item['sha256']}
        member = reference(root, normalized)
        by_path[original] = item['sha256']
        published &= published_bytes(root, path, member.read_bytes())
    return by_path, bool(published)


def _verify_accepted_chain(root: Path, adoption: dict, acceptance: Path,
                           subject: Path, subject_payload: dict) -> bool:
    """Verify the exact Runtime SCA-002 to SCA-003 Gate 5 acceptance chain."""
    from root_governance_state import reference
    if subject_payload.get('schema') != 'runtime-sca003-gate5-poststate-decision/v1':
        raise ValueError('unknown accepted chain subject')
    subject_base = str(Path(adoption['subject']['path']).parent.parent)
    subject_members, published = _verify_members(root, subject_payload, subject_base)

    manifest = reference(root, adoption['acceptance_manifest'])
    package = json.loads(manifest.read_text())
    if package.get('schema') != 'runtime-scope-change-gate5-acceptance/v1':
        raise ValueError('unknown acceptance package')
    package_members, package_published = _verify_members(
        root, package, str(Path(adoption['acceptance_manifest']['path']).parent))
    if package_members.get('OWNER_ACCEPTANCE.md') != adoption['acceptance']['sha256']:
        raise ValueError('acceptance package does not contain owner acceptance')
    accepted_subject = package.get('acceptedSubject', {})
    if (accepted_subject.get('path') != adoption['subject']['path'] or
            accepted_subject.get('sha256') != adoption['subject']['sha256']):
        raise ValueError('acceptance package does not bind exact subject')

    snapshots = adoption['snapshot_manifests']
    if not isinstance(snapshots, list) or len(snapshots) != 2:
        raise ValueError('accepted chain requires two snapshots')
    snapshot_payloads = []
    snapshots_published = True
    for item in snapshots:
        snapshot = reference(root, item)
        payload = json.loads(snapshot.read_text())
        _, members_published = _verify_members(root, payload, str(Path(item['path']).parent))
        snapshot_payloads.append(payload)
        snapshots_published &= members_published
        snapshots_published &= published_bytes(root, item['path'], snapshot.read_bytes())

    chain = package.get('chain', {})
    if (chain.get('sca002SnapshotManifestSha256') != snapshots[0]['sha256'] or
            chain.get('sca003SnapshotManifestSha256') != snapshots[1]['sha256']):
        raise ValueError('acceptance package snapshot chain differs from policy')
    if subject_members.get(snapshots[1]['path']) != snapshots[1]['sha256']:
        raise ValueError('accepted subject does not contain SCA-003 snapshot')

    changes = {Path(item['path']).name: item for item in adoption['changes']}
    final = package.get('canonicalPostimages', {})
    if set(final) != set(changes) or any(
            final[name] != item['after'] for name, item in changes.items()):
        raise ValueError('acceptance package canonical postimages differ from policy')
    sca002 = snapshot_payloads[0].get('canonical_postimages', {})
    if (sca002.get('ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md') !=
            changes['ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md']['after'] or
            sca002.get('Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md') !=
            changes['Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md']['after']):
        raise ValueError('SCA-002 snapshot canonical postimages differ from policy')
    sca003 = snapshot_payloads[1].get('canonicalPostimage', {})
    if (sca003.get('path') != adoption['changes'][2]['path'] or
            sca003.get('sha256') != adoption['changes'][2]['after']):
        raise ValueError('SCA-003 snapshot canonical postimage differs from policy')

    published &= package_published and snapshots_published
    published &= published_bytes(root, adoption['acceptance']['path'], acceptance.read_bytes())
    published &= published_bytes(root, adoption['subject']['path'], subject.read_bytes())
    published &= published_bytes(root, adoption['acceptance_manifest']['path'], manifest.read_bytes())
    return bool(published)
