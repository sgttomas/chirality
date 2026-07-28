#!/usr/bin/env python3
"""Deterministic closure validator for SCA-APP-006."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path


EXPECTED_CONTENT_HASHES = {
    "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md":
        "dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83",
    "projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv":
        "84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1",
    "projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_CONTEXT.md":
        "904d29af0e98a438b5e963822dd285ced684bb1fbbb0c7ebf5d45233f4579c66",
    "projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_CONTEXT.md":
        "305b4bf3f650508293af9c34256ea4066489f50bc8e9f1dc855918ef561c58cd",
    "projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_CONTEXT.md":
        "055b5384dbfcbe9e195ba447b9f859dc1f06d0c8f220d78357c62721e17311d6",
    "projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_CONTEXT.md":
        "d084845c45a369736af9f1667d2773f2e45839ec924baf4f54945692f73e79bf",
    "projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/_CONTEXT.md":
        "8c3a38899b3664bd7ec15e7b613ac6a0ccdbe09760c29077f135cc434ee76a87",
    "projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/_CONTEXT.md":
        "c65e22a18a345ee171c8f6df968efe072c30e59749311a2e8c6f1f42bacf5f4c",
    "projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_CONTEXT.md":
        "1b4d01dc1c83103ac60e8b772e48ba064ffbc59435ba2ebd452fd28eae0926b3",
}

SNAPSHOT = (
    "projects/chirality-app-dev/execution/_ScopeChange/"
    "SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair"
)

REQUIRED_SNAPSHOT_FILES = {
    "Amendment_Actions.csv",
    "Amendment_Preview.md",
    "Brief.md",
    "Decision_Log.md",
    "Gate_4_Acceptance.md",
    "Gate_5_Application_Record.md",
    "Gate_5_Closure_Validation.json",
    "Gate_5_Owner_Confirmation.md",
    "Handoff_State.md",
    "Impact_Assessment.md",
    "Post_Change_Coverage.json",
    "Pre_Change_Coverage.json",
    "Propagation_Plan.md",
    "RUN_SUMMARY.md",
    "Supersession_Delta.csv",
    "Supersession_Map.csv",
    "validate_gate5_state.py",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command, cwd=cwd, text=True, capture_output=True, check=False
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--audit-summary", type=Path)
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    snapshot = repo / SNAPSHOT
    errors: list[str] = []

    content_hashes: dict[str, str] = {}
    for relative, expected in EXPECTED_CONTENT_HASHES.items():
        target = repo / relative
        if not target.is_file():
            errors.append(f"missing authoritative target {relative}")
            continue
        actual = sha256(target)
        content_hashes[relative] = actual
        if actual != expected:
            errors.append(f"authoritative target hash mismatch {relative}")

    missing_snapshot = sorted(
        name for name in REQUIRED_SNAPSHOT_FILES if not (snapshot / name).is_file()
    )
    if missing_snapshot:
        errors.append(f"missing snapshot files: {missing_snapshot}")

    accepted = snapshot / "Accepted_Candidates"
    gate3 = run(["sha256sum", "-c", "Gate_3_Artifact_Hashes.sha256"], accepted)
    gate4 = run(["sha256sum", "-c", "Gate_4_Artifact_Hashes.sha256"], accepted)
    if gate3.returncode:
        errors.append("accepted Gate-3 candidate manifest does not reproduce")
    if gate4.returncode:
        errors.append("accepted Gate-4 candidate manifest does not reproduce")

    with (snapshot / "Amendment_Actions.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        actions = list(csv.DictReader(handle))
    if len(actions) != 12:
        errors.append("canonical amendment action register must have 12 rows")

    with (snapshot / "Supersession_Delta.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        delta_rows = list(csv.DictReader(handle))
    with (snapshot / "Supersession_Map.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        map_rows = list(csv.DictReader(handle))
    if delta_rows:
        errors.append("SCA-APP-006 supersession delta must be header-only")
    if len(map_rows) != 16:
        errors.append("cumulative supersession map must carry 16 prior rows")

    pointer = (
        repo
        / "projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md"
    ).read_text(encoding="utf-8")
    if "SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair/" not in pointer:
        errors.append("SCOPE_CHANGE pointer does not identify SCA-APP-006")
    if "**Status:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`" not in pointer:
        errors.append("SCOPE_CHANGE pointer does not carry the closed state")

    exact_owner_confirmation = (
        "I confirm the SCA-APP-006 post-change state and accept it as "
        "CLOSED_FOR_SCOPE_CHANGE_ONLY, with the invariant register and seven "
        "context amendments current, APP-HOLD-1 unchanged, and all "
        "ScopeOfWork, repinning, implementation, runtime, dependency, "
        "estimate, schedule, lifecycle, release, and Git work remaining "
        "separately governed."
    )
    owner_confirmation = (snapshot / "Gate_5_Owner_Confirmation.md").read_text(
        encoding="utf-8"
    )
    if exact_owner_confirmation not in owner_confirmation:
        errors.append("verbatim Gate-5 owner confirmation is absent")

    handoff = (snapshot / "Handoff_State.md").read_text(encoding="utf-8")
    run_summary = (snapshot / "RUN_SUMMARY.md").read_text(encoding="utf-8")
    for name, content in (
        ("Handoff_State.md", handoff),
        ("RUN_SUMMARY.md", run_summary),
    ):
        if "CLOSED_FOR_SCOPE_CHANGE_ONLY" not in content:
            errors.append(f"{name} does not carry the closed state")
    if "**NextOwner:** `CHANGE`" not in handoff:
        errors.append("handoff does not route bounded closeout to CHANGE")
    if "**ReadyForNextPhase:** `NO`" not in handoff:
        errors.append("handoff does not preserve the downstream phase hold")

    changed = run(["git", "diff", "--name-only", "HEAD"], repo)
    changed_paths = [line for line in changed.stdout.splitlines() if line]
    allowed_prefixes = (
        f"{SNAPSHOT}/",
        "projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/",
    )
    exact_allowed = set(EXPECTED_CONTENT_HASHES) | {
        "projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md"
    }
    unexpected = [
        path
        for path in changed_paths
        if path not in exact_allowed
        and not any(path.startswith(prefix) for prefix in allowed_prefixes)
    ]
    if unexpected:
        errors.append(f"unexpected changed paths: {unexpected}")

    audit = None
    if args.audit_summary:
        audit_path = args.audit_summary.resolve()
        if not audit_path.is_file():
            errors.append(f"missing audit summary {audit_path}")
        else:
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            if audit.get("issues_blocker") != 0:
                errors.append("post-change audit has blockers")
            if audit.get("partitions_declared") != 10:
                errors.append("post-change audit package count mismatch")
            if audit.get("production_units_declared") != 51:
                errors.append("post-change audit deliverable count mismatch")

    report = {
        "accepted_gate3_manifest": gate3.returncode == 0,
        "accepted_gate4_manifest": gate4.returncode == 0,
        "action_rows": len(actions),
        "audit_summary": audit,
        "authoritative_content_hashes": content_hashes,
        "changed_paths": changed_paths,
        "errors": errors,
        "snapshot_required_files": len(REQUIRED_SNAPSHOT_FILES),
        "supersession_delta_rows": len(delta_rows),
        "supersession_map_rows": len(map_rows),
        "unexpected_changed_paths": unexpected,
        "status": "PASS" if not errors else "BLOCKED",
        "closure_state": "CLOSED_FOR_SCOPE_CHANGE_ONLY",
        "owner_confirmation_verbatim": exact_owner_confirmation in owner_confirmation,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
