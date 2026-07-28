#!/usr/bin/env python3
"""Freeze the exact Gate-3 candidate set and complete SCA artifact population."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


SCA = Path(__file__).resolve().parent
CANDIDATE_SET = [
    "Gate_2_Acceptance.md",
    "Gate_3_Basis_Update.md",
    "Gate_3_Exact_Amendment.md",
    "Gate_3_Exact_Decomposition.patch",
    "Register_Enums.json",
    "prepare_register_candidate.py",
    "build_exact_decomposition_patch.py",
    "validate_gate3_candidate.py",
    "compare_scope_traceability.py",
    "Gate_3_Validation.json",
    "Gate_3_Traceability_Comparison.json",
    "Gate_3_Adversarial_Backcheck.md",
    (
        "Candidate_Tree/projects/chirality-app-dev/execution/_Decomposition/"
        "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
    ),
    (
        "Candidate_Tree/projects/chirality-app-dev/execution/_Decomposition/"
        "contract_invariant_coverage_register.csv"
    ),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    missing = [path for path in CANDIDATE_SET if not (SCA / path).is_file()]
    if missing:
        raise SystemExit(f"missing Gate-3 candidate artifacts: {missing}")

    manifest = {
        "status": "PREPARED_NOT_ACCEPTED",
        "sca_id": "SCA-APP-006",
        "accepted_gate2_basis": "4214915d9fcfecdc2952626421bf50b0e5f7845b",
        "non_drifting_current_basis": "c487b7dd57a378e2f74417118e78e7f61a161629",
        "authoritative_application_performed": False,
        "gate4_opened": False,
        "candidate_artifacts": [
            {
                "path": path,
                "sha256": sha256(SCA / path),
                "size": (SCA / path).stat().st_size,
            }
            for path in CANDIDATE_SET
        ],
    }
    candidate_manifest = SCA / "Gate_3_Candidate_Set.json"
    candidate_manifest.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    artifact_manifest = SCA / "Gate_3_Artifact_Hashes.sha256"
    files = sorted(
        path
        for path in SCA.rglob("*")
        if path.is_file() and path != artifact_manifest
    )
    artifact_manifest.write_text(
        "".join(f"{sha256(path)}  {path.relative_to(SCA).as_posix()}\n" for path in files),
        encoding="utf-8",
    )
    print(f"candidate_set_sha256={sha256(candidate_manifest)}")
    print(f"artifact_hash_entries={len(files)}")
    print(f"artifact_hash_manifest_sha256={sha256(artifact_manifest)}")


if __name__ == "__main__":
    main()
