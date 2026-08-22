#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


EXPECTED_GROUPS = {
    "1_compatibility_and_semantic_package",
    "2_source_and_release_identities",
    "3_affected_clients",
    "4_conformance_or_migration_evidence",
    "5_root_semantic_and_regression_evidence",
    "6_census_relationship_routing_notice_and_findings",
    "7_cutover_rollback_replay_and_indeterminate_disposition",
    "8_accountable_human_acts",
}

EXPECTED_MEMBERS = {
    "AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md": "2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13",
    "DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md": "7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153",
    "EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md": "d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a",
    "OWNER_DECISION_RECORD_CANDIDATE_V2.md": "2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c",
    "ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md": "cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1",
    "ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md": "9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8",
}

EXPECTED = {
    "schema": "chirality-del02-compatibility-completion-candidate/v1",
    "status": "PREPARATION_ONLY_UNACCEPTED",
    "repository_commit": "1b375af4f1219ecfc00fc2755854aa7fd4220901",
    "scope_of_work_sha256": "dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146",
    "semantic_snapshot_sha256": "3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa",
    "package_manifest_sha256": "6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2",
    "candidate_identity": "root-runtime-1",
    "compatibility_epoch": 1,
}

HOLD_FIELDS = {"identity", "status", "reason", "owner", "gate", "blocking_posture"}
RESERVED_IDENTITY_SUFFIXES = {"0", "latest", "current", "next", "dev", "test", "unknown", "tbd", "unresolved"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def held_objects(value: Any) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    if isinstance(value, dict):
        if value.get("status") == "HELD_UNAVAILABLE":
            found.append(value)
        for child in value.values():
            found.extend(held_objects(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(held_objects(child))
    return found


def validate_bytes(raw: bytes) -> tuple[dict[str, Any] | None, list[str]]:
    issues: list[str] = []
    try:
        document = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, [f"invalid JSON: {error}"]

    canonical = (json.dumps(document, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if raw != canonical:
        issues.append("candidate is not canonical indent-2 sorted-key JSON with exactly one terminal LF")

    for key in ("schema", "status", "candidate_identity", "compatibility_epoch", "prepared_against", "binding_groups"):
        if key not in document:
            issues.append(f"missing top-level key: {key}")
    if issues:
        return document, issues

    if document["schema"] != EXPECTED["schema"]:
        issues.append("schema mismatch")
    if document["status"] != EXPECTED["status"]:
        issues.append("candidate must remain PREPARATION_ONLY_UNACCEPTED")
    if document["compatibility_epoch"] != EXPECTED["compatibility_epoch"] or isinstance(document["compatibility_epoch"], bool):
        issues.append("epoch must be integer 1")
    identity = document["candidate_identity"]
    if identity != EXPECTED["candidate_identity"] or not re.fullmatch(r"root-runtime-[1-9][0-9]*", str(identity)):
        issues.append("identity must be canonical root-runtime-1")
    if str(identity).removeprefix("root-runtime-").lower() in RESERVED_IDENTITY_SUFFIXES:
        issues.append("identity uses a reserved suffix")

    prepared = document["prepared_against"]
    for key in ("repository_commit", "scope_of_work_sha256", "accepted_semantic_snapshot_sha256"):
        if key not in prepared:
            issues.append(f"prepared_against missing {key}")
    if prepared.get("repository_commit") != EXPECTED["repository_commit"]:
        issues.append("repository basis mismatch")
    if prepared.get("scope_of_work_sha256") != EXPECTED["scope_of_work_sha256"]:
        issues.append("Scope of Work identity mismatch")
    if prepared.get("accepted_semantic_snapshot_sha256") != EXPECTED["semantic_snapshot_sha256"]:
        issues.append("accepted semantic snapshot mismatch")

    groups = document["binding_groups"]
    if set(groups) != EXPECTED_GROUPS:
        issues.append("binding group set is not exactly the eight required groups")

    group1 = groups.get("1_compatibility_and_semantic_package", {})
    if group1.get("compatibility_identity") != identity:
        issues.append("group 1 identity does not match top-level identity")
    members = group1.get("semantic_members", [])
    observed_members: dict[str, str] = {}
    for member in members:
        name = Path(str(member.get("path", ""))).name
        if name in observed_members:
            issues.append(f"duplicate semantic member: {name}")
        observed_members[name] = member.get("sha256")
    if observed_members != EXPECTED_MEMBERS:
        issues.append("semantic member names/hashes are not exactly the accepted six")
    manifest = group1.get("sorted_package_manifest", {})
    if manifest.get("sha256") != EXPECTED["package_manifest_sha256"]:
        issues.append("sorted six-member package manifest identity mismatch")

    holds = held_objects(groups)
    if len(holds) != 10:
        issues.append(f"expected exactly 10 HELD_UNAVAILABLE objects; found {len(holds)}")
    for index, hold in enumerate(holds, start=1):
        if not HOLD_FIELDS.issubset(hold):
            issues.append(f"held object {index} lacks required fields")
        if hold.get("identity") is not None:
            issues.append(f"held object {index} identity must be null")
        for field in ("reason", "owner", "gate", "blocking_posture"):
            if not isinstance(hold.get(field), str) or not hold[field].strip():
                issues.append(f"held object {index} has empty {field}")

    return document, issues


def validate_paths(repo_root: Path, candidate: Path) -> list[str]:
    raw = candidate.read_bytes()
    document, issues = validate_bytes(raw)
    if document is None:
        return issues

    if hashlib.sha256(raw).hexdigest() != "e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c":
        issues.append("prepared candidate SHA-256 mismatch")

    snapshot = repo_root / "execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003/ACCEPTED_SEMANTIC_SNAPSHOT.md"
    manifest = repo_root / "execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-SEMANTIC-CANDIDATE-002/manifests/V2_CANDIDATE_PACKAGE_MANIFEST.sha256"
    if sha256(snapshot) != EXPECTED["semantic_snapshot_sha256"]:
        issues.append("live accepted semantic snapshot drift")
    if sha256(manifest) != EXPECTED["package_manifest_sha256"]:
        issues.append("live accepted six-member manifest drift")

    for member in document["binding_groups"]["1_compatibility_and_semantic_package"]["semantic_members"]:
        path = repo_root / member["path"]
        if not path.is_file() or path.is_symlink():
            issues.append(f"member missing or non-regular: {member['path']}")
        elif sha256(path) != member["sha256"]:
            issues.append(f"member hash drift: {member['path']}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", type=Path)
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    issues = validate_paths(args.repo_root.resolve(), args.candidate.resolve())
    result = {"valid": not issues, "issues": issues}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
