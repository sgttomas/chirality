#!/usr/bin/env python3
"""Materialize the Gate-3 register candidate from the sealed Agent-2 return."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


SCA = Path(__file__).resolve().parent
SOURCE = (
    SCA
    / "Agent2_Returns"
    / "Register_Mapper"
    / "candidate_contract_invariant_coverage_register.csv"
)
CANDIDATE_DECOMP = (
    SCA
    / "Candidate_Tree"
    / "projects"
    / "chirality-app-dev"
    / "execution"
    / "_Decomposition"
    / "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
OUTPUT = (
    SCA
    / "Candidate_Tree"
    / "projects"
    / "chirality-app-dev"
    / "execution"
    / "_Decomposition"
    / "contract_invariant_coverage_register.csv"
)
DECOMP_REPO_PATH = (
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    expected_source = (
        "490322cc9d17c10501ecb3838516f88ae8261506d1b5e37d417737e6482cb92b"
    )
    if sha256(SOURCE) != expected_source:
        raise SystemExit("sealed register-mapper return identity mismatch")

    expected_decomp = (
        "dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83"
    )
    actual_decomp = sha256(CANDIDATE_DECOMP)
    if actual_decomp != expected_decomp:
        raise SystemExit("candidate decomposition identity mismatch")

    with SOURCE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        if not fieldnames or "AppDecompositionBasis" not in fieldnames:
            raise SystemExit("register schema lacks AppDecompositionBasis")
        rows = list(reader)

    ids = {row["InvariantID"] for row in rows}
    families = {row["InvariantFamily"] for row in rows}
    if len(rows) != 81 or len(ids) != 81 or len(families) != 48:
        raise SystemExit("register population is not 81 unique IDs / 48 families")

    basis = f"{DECOMP_REPO_PATH}#candidate-sha256={actual_decomp}"
    for row in rows:
        row["AppDecompositionBasis"] = basis
        if row["SemanticOwnerProduct"] == "ROOT":
            row["OwnerAuthorityRef"] = row["OwnerAuthorityRef"].replace(
                "D-GOV-28_root_runtime_stewardship.md#Outcome",
                "D-GOV-28_root_runtime_stewardship.md#Effects",
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"PASS rows={len(rows)} families={len(families)}")
    print(f"candidate_decomposition_sha256={actual_decomp}")
    print(f"candidate_register_sha256={sha256(OUTPUT)}")


if __name__ == "__main__":
    main()
