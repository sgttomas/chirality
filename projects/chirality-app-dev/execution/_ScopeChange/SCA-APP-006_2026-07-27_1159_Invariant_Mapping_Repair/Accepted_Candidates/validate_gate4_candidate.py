#!/usr/bin/env python3
"""Validate the frozen SCA-APP-006 Gate-4 propagation candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


BASIS = "9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2"
GATE3_BASIS = "c487b7dd57a378e2f74417118e78e7f61a161629"

EXPECTED_CONTEXT_HASHES = {
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

EXPECTED_SCOPE_ITEMS = {
    "DEL-02-05": "SOW-013, SOW-019, SOW-023",
    "DEL-04-02": "SOW-016, SOW-045, SOW-047, SOW-052, SOW-076",
    "DEL-06-02": "SOW-047, SOW-049, SOW-050, SOW-064",
    "DEL-06-03": "SOW-048, SOW-050, SOW-064",
    "DEL-07-01": "SOW-002, SOW-027, SOW-075",
    "DEL-07-06": "SOW-032, SOW-033, SOW-034, SOW-077",
    "DEL-09-04": "SOW-030, SOW-072, SOW-073, SOW-078",
}

EXPECTED_PKG02 = {
    "PackageName": "Woven Dialogue Shell, Navigation, and Operator State",
    "ScopeDescription": "Dialogue-centred shell, Woven Dialogue artifact presentation, Navigator, Work/Agents Coordination Panel, activity shelf, re-hosted Workbench/Pipeline/toolkit/settings, compatibility surfaces, and non-authoritative local UI state.",
    "InclusionCriteria": "Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior.",
    "Exclusions": "Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority.",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def table_value(text: str, field: str) -> str | None:
    match = re.search(rf"^\| {re.escape(field)} \| (.*?) \|$", text, re.MULTILINE)
    return match.group(1) if match else None


def bold_value(text: str, field: str) -> str | None:
    match = re.search(rf"^\*\*{re.escape(field)}:\*\* (.*?)$", text, re.MULTILINE)
    return match.group(1) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    args = parser.parse_args()

    package = Path(__file__).resolve().parent
    repo = args.repo_root.resolve()
    errors: list[str] = []

    basis_check = git(repo, "cat-file", "-e", f"{BASIS}^{{commit}}")
    if basis_check.returncode:
        errors.append(f"missing basis commit {BASIS}")

    source_paths = list(EXPECTED_CONTEXT_HASHES)
    source_paths.append(
        "projects/chirality-app-dev/execution/_Decomposition/"
        "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
    )
    drift = git(repo, "diff", "--quiet", GATE3_BASIS, BASIS, "--", *source_paths)
    if drift.returncode:
        errors.append("Gate-3 basis and Gate-4 basis differ on governed source paths")

    found_ids: set[str] = set()
    actual_context_hashes: dict[str, str] = {}
    for relative, expected_hash in EXPECTED_CONTEXT_HASHES.items():
        candidate = package / "Candidate_Metadata_Tree" / relative
        if not candidate.is_file():
            errors.append(f"missing candidate context {relative}")
            continue
        actual_hash = sha256(candidate)
        actual_context_hashes[relative] = actual_hash
        if actual_hash != expected_hash:
            errors.append(f"candidate hash mismatch {relative}")

        text = candidate.read_text(encoding="utf-8")
        deliverable_id = table_value(text, "DeliverableID")
        if not deliverable_id:
            errors.append(f"missing DeliverableID {relative}")
            continue
        found_ids.add(deliverable_id)
        expected_scope = EXPECTED_SCOPE_ITEMS.get(deliverable_id)
        if table_value(text, "CoversScopeItems") != expected_scope:
            errors.append(f"CoversScopeItems mismatch {deliverable_id}")

        source = git(repo, "show", f"{BASIS}:{relative}")
        if source.returncode:
            errors.append(f"missing basis source {relative}")

        if deliverable_id == "DEL-02-05":
            observed = {
                "PackageName": table_value(text, "PackageName"),
                "ScopeDescription": bold_value(text, "ScopeDescription"),
                "InclusionCriteria": bold_value(text, "InclusionCriteria"),
                "Exclusions": bold_value(text, "Exclusions"),
            }
            if observed != EXPECTED_PKG02:
                errors.append("DEL-02-05 PKG-02 descriptive-field parity failed")

    if found_ids != set(EXPECTED_SCOPE_ITEMS):
        errors.append("candidate deliverable set mismatch")

    with (package / "Gate_4_Amendment_Actions.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        actions = list(csv.DictReader(handle))
    if len(actions) != 12:
        errors.append("Gate-4 action register must contain 12 rows")
    if [row["ActionSeq"] for row in actions] != [str(i) for i in range(1, 13)]:
        errors.append("Gate-4 action sequence mismatch")
    joined_files = ";".join(row["AffectedFiles"] for row in actions)
    for relative in EXPECTED_CONTEXT_HASHES:
        if relative not in joined_files:
            errors.append(f"action register omits {relative}")

    gate3 = subprocess.run(
        ["sha256sum", "-c", "Gate_3_Artifact_Hashes.sha256"],
        cwd=package,
        text=True,
        capture_output=True,
        check=False,
    )
    if gate3.returncode:
        errors.append("accepted Gate-3 manifest no longer reproduces")

    report = {
        "accepted_gate3_candidate_set_sha256":
            "e029dbcfcfb8c72323c2517462cc29a94c7506c839d4d4f9f441ba0168ab083d",
        "accepted_gate3_manifest_sha256":
            "61a447e4160da4dd2213b30cdd687ca321101259af468c5a7155c43424583326",
        "action_rows": len(actions),
        "basis": BASIS,
        "basis_paths_unchanged_from_gate3": not bool(drift.returncode),
        "candidate_context_hashes": actual_context_hashes,
        "candidate_contexts": len(actual_context_hashes),
        "errors": errors,
        "gate3_manifest_reproduced": not bool(gate3.returncode),
        "status": "PASS" if not errors else "BLOCKED",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
