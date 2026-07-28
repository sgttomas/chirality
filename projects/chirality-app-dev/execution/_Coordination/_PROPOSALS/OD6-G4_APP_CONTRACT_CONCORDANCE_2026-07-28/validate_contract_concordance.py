#!/usr/bin/env python3
"""Validate and materialize the D-APP-80 contract-concordance evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


BASE_COMMIT = "deb01644e324af2b39cff7b52abae43784cd071b"
TERMINAL_COMMIT = "7b0be4d8772a16e5a4774a17988479587d00acca"
MISSING_HISTORICAL_COMMIT = "416b29033bbacb0bc3648d84033272b7ab4e6e11"
TERMINAL_PATH = (
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
TERMINAL_BASIS = f"{TERMINAL_PATH}@{TERMINAL_COMMIT}"
CONTROL_IDS = {"DEL-00-01", "DEL-00-02"}
HELD_IDS = {
    "DEL-02-01",
    "DEL-02-02",
    "DEL-02-04",
    "DEL-05-04",
    "DEL-08-02",
    "DEL-08-03",
}
SEMANTIC_DELTAS = {
    "DEL-02-05": ("SOW-023", "SUPPORTED"),
    "DEL-04-02": ("SOW-076", "OUT_BOUNDARY_ONLY"),
    "DEL-06-02": ("SOW-064", "SUPPORTED"),
    "DEL-06-03": ("SOW-064", "SUPPORTED"),
    "DEL-07-01": ("SOW-075", "SUPPORTED"),
    "DEL-07-06": ("SOW-077", "OUT_BOUNDARY_ONLY"),
    "DEL-09-04": ("SOW-078", "OUT_BOUNDARY_ONLY"),
}
AUXILIARY_SURFACES = [
    "projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv",
    "projects/chirality-app-dev/execution/_Scripts/app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/expected_held.json",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/APP_HOLD_REGISTER_DRIFT.csv",
]


def run(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        args,
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        raise RuntimeError(f"{' '.join(args)}: {proc.stderr.strip()}")
    return proc.stdout


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def preimage(repo: Path, relative: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{BASE_COMMIT}:{relative}"],
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout


def front_matter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        raise RuntimeError("ScopeOfWork.md lacks front matter")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line[0].isspace():
            key, value = line.split(":", 1)
            result[key] = value.strip()
    return result


def list_value(value: str) -> list[str]:
    if not value.startswith("[") or not value.endswith("]"):
        raise RuntimeError(f"expected inline list: {value}")
    content = value[1:-1].strip()
    return [] if not content else content.split(", ")


def context_scope_refs(path: Path) -> list[str]:
    match = re.search(
        r"^\| CoversScopeItems \| (.*?) \|$", path.read_text(), re.MULTILINE
    )
    if not match:
        raise RuntimeError(f"missing CoversScopeItems row: {path}")
    return match.group(1).split(", ")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    package = Path(__file__).resolve().parent
    repo = Path(run(package, "git", "rev-parse", "--show-toplevel").strip())
    app_execution = repo / "projects/chirality-app-dev/execution"
    sow_paths = sorted(
        path
        for path in app_execution.glob("PKG-*/1_Working/DEL-*/ScopeOfWork.md")
        if "_PROPOSALS" not in path.parts
    )
    if len(sow_paths) != 53:
        raise RuntimeError(f"expected 53 contracts, found {len(sow_paths)}")
    run(repo, "git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD")
    run(repo, "git", "cat-file", "-e", f"{TERMINAL_COMMIT}:{TERMINAL_PATH}")
    missing = subprocess.run(
        ["git", "cat-file", "-e", f"{MISSING_HISTORICAL_COMMIT}^{{commit}}"],
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if missing.returncode == 0:
        raise RuntimeError("historical missing-basis object unexpectedly resolves")

    concordance: list[dict[str, str]] = []
    historical: list[dict[str, str]] = []
    surface_paths: list[str] = []
    seen: set[str] = set()
    semantic_review_count = 0
    for sow in sow_paths:
        relative = sow.relative_to(repo).as_posix()
        current = front_matter(sow.read_text())
        prior = front_matter(preimage(repo, relative).decode())
        deliverable_id = current["deliverable_id"]
        if deliverable_id in seen:
            raise RuntimeError(f"duplicate deliverable: {deliverable_id}")
        seen.add(deliverable_id)
        current_refs = list_value(current["project_scope_refs"])
        expected_refs = context_scope_refs(sow.with_name("_CONTEXT.md"))
        if current_refs != expected_refs:
            raise RuntimeError(
                f"{deliverable_id} scope refs differ from _CONTEXT: "
                f"{current_refs} != {expected_refs}"
            )
        if deliverable_id in CONTROL_IDS:
            disposition = "CONTROL_OUTSIDE_REPIN"
            if current["decomposition_basis"] != prior["decomposition_basis"]:
                raise RuntimeError(f"{deliverable_id} control basis changed")
            relation = "NOT_APPLICABLE"
        else:
            disposition = "REPINS_TO_TERMINAL_BASIS"
            surface_paths.append(relative)
            if current["decomposition_basis"] != TERMINAL_BASIS:
                raise RuntimeError(f"{deliverable_id} does not pin terminal basis")
            relation = (
                "HISTORICAL_RELATION_UNKNOWN"
                if deliverable_id in HELD_IDS
                else "HISTORICAL_RELATION_RESOLVABLE"
            )
        semantic = "UNCHANGED_AND_CONCORDANT"
        if deliverable_id in SEMANTIC_DELTAS:
            added_ref, relation_kind = SEMANTIC_DELTAS[deliverable_id]
            if added_ref not in current_refs:
                raise RuntimeError(f"{deliverable_id} lacks {added_ref}")
            if "D-APP-80 concordance note" not in sow.read_text():
                raise RuntimeError(f"{deliverable_id} lacks D-APP-80 note")
            semantic = f"REVIEWED_{relation_kind}_{added_ref}"
            semantic_review_count += 1
        concordance.append(
            {
                "deliverable_id": deliverable_id,
                "package_id": current["package_id"],
                "sow_path": relative,
                "pre_basis": prior["decomposition_basis"],
                "post_basis": current["decomposition_basis"],
                "basis_disposition": disposition,
                "scope_refs": "|".join(current_refs),
                "scope_concordance": semantic,
                "hold_state": (
                    "REPAIR_VALIDATION_PENDING"
                    if deliverable_id in HELD_IDS
                    else "NOT_HELD"
                ),
                "historical_relation": relation,
            }
        )
        if deliverable_id in HELD_IDS:
            if not prior["decomposition_basis"].endswith(
                f"@{MISSING_HISTORICAL_COMMIT}"
            ):
                raise RuntimeError(
                    f"{deliverable_id} preimage lacks missing historical basis"
                )
            historical.append(
                {
                    "deliverable_id": deliverable_id,
                    "historical_declared_basis": prior["decomposition_basis"],
                    "historical_relation": "HISTORICAL_RELATION_UNKNOWN",
                    "prospective_current_basis": current["decomposition_basis"],
                    "hold_state": "REPAIR_VALIDATION_PENDING",
                    "history_reconstructed": "false",
                }
            )

    if seen != {row["deliverable_id"] for row in concordance}:
        raise RuntimeError("population identity mismatch")
    if len(surface_paths) != 51 or semantic_review_count != 7 or len(historical) != 6:
        raise RuntimeError("population class count mismatch")

    surface_paths.extend(AUXILIARY_SURFACES)
    surfaces: list[dict[str, str]] = []
    for relative in sorted(surface_paths):
        path = repo / relative
        before = sha256_bytes(preimage(repo, relative))
        after = sha256_file(path)
        if before == after:
            raise RuntimeError(f"declared application surface did not change: {relative}")
        surfaces.append(
            {
                "path": relative,
                "preimage_sha256": before,
                "postimage_sha256": after,
            }
        )
    if len(surfaces) != 56:
        raise RuntimeError(f"expected 56 application surfaces, found {len(surfaces)}")

    validation = {
        "schema": "chirality-app-contract-concordance-validation/v1",
        "basis_commit": BASE_COMMIT,
        "terminal_decomposition_basis": TERMINAL_BASIS,
        "contract_count": 53,
        "decomposition_derived_count": 51,
        "pkg00_control_count": 2,
        "semantic_review_count": 7,
        "historical_unknown_count": 6,
        "active_repair_pending_hold_count": 6,
        "scan_held_expected_count": 0,
        "application_surface_count": 56,
        "verdict": "PASS",
    }
    if args.write:
        write_csv(
            package / "CONTRACT_CONCORDANCE.csv",
            list(concordance[0]),
            concordance,
        )
        write_csv(
            package / "HISTORICAL_RELATIONS.csv",
            list(historical[0]),
            historical,
        )
        write_csv(
            package / "LIVE_SURFACE_MANIFEST.csv",
            list(surfaces[0]),
            surfaces,
        )
        (package / "VALIDATION.json").write_text(
            json.dumps(validation, indent=2, sort_keys=True) + "\n"
        )
    print(json.dumps(validation, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
