#!/usr/bin/env python3
"""Fail-closed Gate-5 N1 reconstruction and collision census."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
from pathlib import Path


EXPECTED = {
    "decomposition": ("932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f", 112419),
    "contract": ("842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9", 34877),
    "register": ("62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3", 98230),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section(text: str, heading: str, next_heading: str | None) -> str:
    start = text.index(heading)
    end = text.index(next_heading, start) if next_heading else len(text)
    return text[start:end]


def fenced_blocks(text: str) -> list[str]:
    return [match + "\n" for match in re.findall(r"```text\n(.*?)\n```", text, re.S)]


def post_image(text: str) -> str:
    tail = text[text.index("### POST-IMAGE") :]
    blocks = fenced_blocks(tail)
    if not blocks:
        raise ValueError("POST-IMAGE block missing")
    return blocks[0]


def replace_once(data: str, old: str, new: str, label: str, counts: dict[str, int]) -> str:
    count = data.count(old)
    counts[label] = count
    if count != 1:
        raise ValueError(f"{label}: expected one anchor, found {count}")
    return data.replace(old, new, 1)


def verify_output(name: str, data: bytes) -> dict[str, object]:
    digest = sha256(data)
    expected_digest, expected_bytes = EXPECTED[name]
    if digest != expected_digest or len(data) != expected_bytes:
        raise ValueError(
            f"{name}: got {digest}/{len(data)}, expected {expected_digest}/{expected_bytes}"
        )
    return {"sha256": digest, "bytes": len(data)}


def invariant_row_count(text: str, invariant_id: str) -> int:
    pattern = re.compile(rf"^\| \*\*{re.escape(invariant_id)}\*\* \|", re.M)
    return len(pattern.findall(text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    args = parser.parse_args()

    repo = args.repo.resolve()
    candidate_dir = args.candidate_dir.resolve()
    candidate_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(candidate_dir, 0o700)

    app = repo / "projects/chirality-app-dev"
    snapshot = app / "execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway"
    gate3_path = snapshot / "Gate3/GATE3_AMENDMENT_PACKAGE.md"
    gate3 = gate3_path.read_text()
    counts: dict[str, int] = {}

    # Decomposition D-01..D-04 replacements and D-05 insertions.
    decomp_path = app / "execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
    decomp = decomp_path.read_text()
    d_heads = [f"## Transaction D-0{i}" for i in range(1, 6)]
    for idx in range(4):
        sec = section(gate3, d_heads[idx], d_heads[idx + 1])
        blocks = fenced_blocks(sec)
        if len(blocks) != 2:
            raise ValueError(f"D-0{idx + 1}: expected two fenced blocks, found {len(blocks)}")
        decomp = replace_once(decomp, blocks[0], blocks[1], f"D-0{idx + 1}", counts)
    d05 = section(gate3, d_heads[4], "## Contract transaction set")
    blocks = fenced_blocks(d05)
    if len(blocks) != 4:
        raise ValueError(f"D-05: expected four fenced blocks, found {len(blocks)}")
    decomp = replace_once(decomp, blocks[0], blocks[0] + blocks[1], "D-05-decision", counts)
    decomp = replace_once(decomp, blocks[2], blocks[2] + blocks[3], "D-05-change-log", counts)
    decomp_bytes = decomp.encode()
    decomp_identity = verify_output("decomposition", decomp_bytes)
    decomp_out = candidate_dir / "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
    decomp_out.write_bytes(decomp_bytes)
    os.chmod(decomp_out, 0o600)

    # Contract C-01..C-11 with owner-approved C-01 and C-06 substitutions.
    contract_path = app / "docs/CONTRACT.md"
    contract = contract_path.read_text()
    c_heads = [f"## Transaction C-{i:02d}" for i in range(1, 12)]
    replacement_overrides = {
        1: post_image((snapshot / "Phase2b/K_CONTROL_1_REGENERATED_CONTRACT_ROW_CANDIDATE.md").read_text()),
        6: post_image((snapshot / "Phase2b/K_EVENT_4_REPINNED_CONTRACT_ROW_CANDIDATE.md").read_text()),
    }
    override_identities = {
        f"C-{number:02d}": sha256(value.encode()) for number, value in replacement_overrides.items()
    }
    for number in range(1, 8):
        next_heading = c_heads[number] if number < 11 else "## D-APP-103 interaction"
        sec = section(gate3, c_heads[number - 1], next_heading)
        blocks = fenced_blocks(sec)
        if len(blocks) != 2:
            raise ValueError(f"C-{number:02d}: expected two fenced blocks, found {len(blocks)}")
        replacement = replacement_overrides.get(number, blocks[1])
        contract = replace_once(contract, blocks[0], replacement, f"C-{number:02d}", counts)

    c08 = section(gate3, c_heads[7], c_heads[8])
    blocks = fenced_blocks(c08)
    if len(blocks) != 3:
        raise ValueError(f"C-08: expected three fenced blocks, found {len(blocks)}")
    basis_count = contract_path.read_text().count(blocks[0])
    counts["C-08-basis-pre-anchor-in-live"] = basis_count
    if basis_count != 1:
        raise ValueError(f"C-08 basis pre-anchor: expected one live anchor, found {basis_count}")
    post_c04_basis_count = contract.count(blocks[0])
    counts["C-08-basis-pre-anchor-post-C04"] = post_c04_basis_count
    if post_c04_basis_count != 0:
        raise ValueError(
            f"C-08 basis pre-anchor remained after C-04: found {post_c04_basis_count}"
        )
    contract = replace_once(contract, blocks[1], blocks[1] + blocks[2], "C-08-application-anchor", counts)

    for number in range(9, 12):
        next_heading = c_heads[number] if number < 11 else "## D-APP-103 interaction"
        sec = section(gate3, c_heads[number - 1], next_heading)
        blocks = fenced_blocks(sec)
        if len(blocks) != 2:
            raise ValueError(f"C-{number:02d}: expected two fenced blocks, found {len(blocks)}")
        contract = replace_once(contract, blocks[0], blocks[0] + blocks[1], f"C-{number:02d}", counts)

    contract_bytes = contract.encode()
    contract_identity = verify_output("contract", contract_bytes)
    contract_out = candidate_dir / "CONTRACT.md"
    contract_out.write_bytes(contract_bytes)
    os.chmod(contract_out, 0o600)

    register_source = snapshot / "Phase5/CORRECTED_COMPANION_REGISTER_CANDIDATE.csv"
    register_bytes = register_source.read_bytes()
    register_identity = verify_output("register", register_bytes)
    register_out = candidate_dir / "contract_invariant_coverage_register.csv"
    register_out.write_bytes(register_bytes)
    os.chmod(register_out, 0o600)

    # Collision census is against live pre-images, not reconstructed post-images.
    live_app_contract = contract_path.read_text()
    live_register_text = (app / "execution/_Decomposition/contract_invariant_coverage_register.csv").read_text()
    root_contract_path = repo / "docs/CONTRACT.md"
    root_contract = root_contract_path.read_text()
    with (app / "execution/_Decomposition/contract_invariant_coverage_register.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        register_rows = list(reader)
        fieldnames = reader.fieldnames or []
    id_column = next((name for name in fieldnames if name.lower() in {"invariantid", "invariant_id"}), None)
    if id_column is None:
        raise ValueError(f"register invariant ID column unresolved: {fieldnames}")

    census: dict[str, dict[str, object]] = {}
    for invariant_id in ("K-CONSENT-1", "K-UNTYPED-1"):
        entry = {
            "app_contract_exact_row_count": invariant_row_count(live_app_contract, invariant_id),
            "app_contract_literal_count": live_app_contract.count(invariant_id),
            "companion_register_id_count": sum(row[id_column] == invariant_id for row in register_rows),
            "companion_register_literal_count": live_register_text.count(invariant_id),
            "root_contract_exact_row_count": invariant_row_count(root_contract, invariant_id),
            "root_contract_literal_count": root_contract.count(invariant_id),
        }
        if any(entry.values()):
            raise ValueError(f"{invariant_id}: collision or ambiguous incidental prose: {entry}")
        census[invariant_id] = entry

    report = {
        "status": "PASS",
        "candidate_directory": str(candidate_dir),
        "candidate_directory_mode": oct(candidate_dir.stat().st_mode & 0o777),
        "transactions": counts,
        "overrides": override_identities,
        "outputs": {
            "decomposition": decomp_identity,
            "contract": contract_identity,
            "register": register_identity,
        },
        "collision_census": census,
    }
    report_path = candidate_dir / "N1_RECONSTRUCTION_RESULT.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    os.chmod(report_path, 0o600)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
