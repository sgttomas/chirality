#!/usr/bin/env python3
"""Validate and materialize the D-APP-81 APP-HOLD release evidence."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


BASE_COMMIT = "b0b673dc3d65a4cfff9a045fda6c1fefa060645c"
TERMINAL_COMMIT = "7b0be4d8772a16e5a4774a17988479587d00acca"
TERMINAL_PATH = (
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
TERMINAL_BASIS = f"{TERMINAL_PATH}@{TERMINAL_COMMIT}"
RELEASED_IDS = {
    "DEL-02-01",
    "DEL-02-02",
    "DEL-02-04",
    "DEL-05-04",
    "DEL-08-02",
    "DEL-08-03",
}
CONTROL_IDS = {"DEL-00-01", "DEL-00-02"}
RELEASE_SURFACES = [
    "projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv",
    "projects/chirality-app-dev/execution/_Scripts/app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/expected_held.json",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/MALFORMED_HOLD_REGISTER_AUTHORITY.csv",
]
CLOSEOUTS = [
    {
        "decision_id": "D-APP-78",
        "application_commit": "63777c0f447536c6a0aecbe8c545339edf8973fb",
        "merge_commit": "23b3b07d1122ae065affe69346c53bac78289a2e",
        "pr": "393",
        "decision_path": (
            "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
            "D-APP-78_OD6_G2_T1_TERMINAL_APP_BASIS_2026-07-28.md"
        ),
    },
    {
        "decision_id": "D-APP-79",
        "application_commit": "c19fa656a434e4cf38bffeafe0ec15a3274d7262",
        "merge_commit": "deb01644e324af2b39cff7b52abae43784cd071b",
        "pr": "394",
        "decision_path": (
            "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
            "D-APP-79_RULING_OD6_G3_H0A_REPAIR_VALIDATION_HOLD_2026-07-28.md"
        ),
    },
    {
        "decision_id": "D-APP-80",
        "application_commit": "0410a15df4c8be0e8a768fbca6080a8f7b637c10",
        "merge_commit": "b0b673dc3d65a4cfff9a045fda6c1fefa060645c",
        "pr": "397",
        "decision_path": (
            "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
            "D-APP-80_RULING_OD6_G4_CONTRACT_CONCORDANCE_2026-07-28.md"
        ),
    },
]


def proc(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(
        args,
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        raise RuntimeError(
            f"{' '.join(args)} failed: {result.stderr.decode(errors='replace').strip()}"
        )
    return result


def text(repo: Path, *args: str) -> str:
    return proc(repo, *args).stdout.decode()


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def front_matter(value: str) -> dict[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", value, re.DOTALL)
    if not match:
        raise RuntimeError("missing front matter")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line[0].isspace():
            key, entry = line.split(":", 1)
            result[key] = entry.strip()
    return result


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
    repo = Path(text(package, "git", "rev-parse", "--show-toplevel").strip())
    proc(repo, "git", "merge-base", "--is-ancestor", BASE_COMMIT, "HEAD")

    app_execution = repo / "projects/chirality-app-dev/execution"
    contracts = sorted(app_execution.glob("PKG-*/1_Working/DEL-*/ScopeOfWork.md"))
    if len(contracts) != 53:
        raise RuntimeError(f"expected 53 contracts, found {len(contracts)}")
    terminal_count = 0
    control_count = 0
    contract_ids: set[str] = set()
    for contract in contracts:
        values = front_matter(contract.read_text())
        deliverable_id = values["deliverable_id"]
        contract_ids.add(deliverable_id)
        basis = values["decomposition_basis"]
        if deliverable_id in CONTROL_IDS:
            if "/PKG-00_DAG_Closure_and_Project_Control/README.md@" not in basis:
                raise RuntimeError(f"{deliverable_id} control basis drift")
            control_count += 1
        elif basis == TERMINAL_BASIS:
            terminal_count += 1
        else:
            raise RuntimeError(f"{deliverable_id} is not on terminal basis")
    if terminal_count != 51 or control_count != 2:
        raise RuntimeError("terminal/control population mismatch")

    historical_path = (
        app_execution
        / "_Coordination/_PROPOSALS/"
        "OD6-G4_APP_CONTRACT_CONCORDANCE_2026-07-28/HISTORICAL_RELATIONS.csv"
    )
    with historical_path.open(newline="", encoding="utf-8") as handle:
        historical = list(csv.DictReader(handle))
    if len(historical) != 6:
        raise RuntimeError("historical UNKNOWN count mismatch")
    if {row["deliverable_id"] for row in historical} != RELEASED_IDS:
        raise RuntimeError("historical UNKNOWN identity mismatch")
    if {row["historical_relation"] for row in historical} != {
        "HISTORICAL_RELATION_UNKNOWN"
    }:
        raise RuntimeError("historical relation was reconstructed")
    if {row["history_reconstructed"] for row in historical} != {"false"}:
        raise RuntimeError("history reconstruction marker drift")

    register = app_execution / "_Coordination/APP_HOLD_REGISTER.csv"
    with register.open(newline="", encoding="utf-8") as handle:
        register_rows = list(csv.DictReader(handle))
    if register_rows:
        raise RuntimeError("released active-hold register must be header-only")
    guard = (app_execution / "_Scripts/app_hold.py").read_text()
    for deliverable_id in RELEASED_IDS:
        if f'"{deliverable_id}"' not in guard:
            raise RuntimeError(f"guard lacks released identity: {deliverable_id}")
    if "released target cannot appear in the active hold register" not in guard:
        raise RuntimeError("guard lacks deterministic released-target fence")

    closeout_rows: list[dict[str, str]] = []
    for item in CLOSEOUTS:
        application = item["application_commit"]
        merge = item["merge_commit"]
        parents = text(repo, "git", "show", "-s", "--format=%P", merge).split()
        if len(parents) != 2 or parents[1] != application:
            raise RuntimeError(f"{item['decision_id']} merge parent mismatch")
        proc(repo, "git", "merge-base", "--is-ancestor", merge, "HEAD")
        paths = text(
            repo,
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            application,
        ).splitlines()
        identity = proc(
            repo,
            "git",
            "diff",
            "--exit-code",
            application,
            merge,
            "--",
            *paths,
            check=False,
        )
        if identity.returncode:
            raise RuntimeError(f"{item['decision_id']} application/merge drift")
        source_bytes = proc(
            repo, "git", "show", f"{application}:{item['decision_path']}"
        ).stdout
        current_bytes = (repo / item["decision_path"]).read_bytes()
        if source_bytes != current_bytes:
            raise RuntimeError(f"{item['decision_id']} decision bytes drift")
        closeout_rows.append(
            {
                **item,
                "application_path_count": str(len(paths)),
                "application_merge_byte_identity": "PASS",
                "merge_is_current_ancestor": "PASS",
                "decision_sha256": sha256(current_bytes),
                "decision_current_byte_identity": "PASS",
            }
        )

    released_rows = [
        {
            "deliverable_id": row["deliverable_id"],
            "historical_declared_basis": row["historical_declared_basis"],
            "historical_relation": "HISTORICAL_RELATION_UNKNOWN",
            "current_basis": row["prospective_current_basis"],
            "release_disposition": "RELEASED_D_APP_81",
            "active_hold_row": "ABSENT",
            "history_reconstructed": "false",
        }
        for row in historical
    ]
    surfaces: list[dict[str, str]] = []
    for relative in RELEASE_SURFACES:
        before = proc(repo, "git", "show", f"{BASE_COMMIT}:{relative}").stdout
        after = (repo / relative).read_bytes()
        if before == after:
            raise RuntimeError(f"release surface unchanged: {relative}")
        surfaces.append(
            {
                "path": relative,
                "preimage_sha256": sha256(before),
                "postimage_sha256": sha256(after),
            }
        )

    proof = {
        "schema": "chirality-app-hold-release-proof/v1",
        "basis_commit": BASE_COMMIT,
        "contract_count": 53,
        "terminal_basis_count": terminal_count,
        "pkg00_control_count": control_count,
        "historical_relation_unknown_count": len(historical),
        "released_target_count": len(RELEASED_IDS),
        "active_hold_row_count": len(register_rows),
        "release_surface_count": len(surfaces),
        "closeout_identity_count": len(closeout_rows),
        "verdict": "PASS",
    }
    if args.write:
        write_csv(
            package / "RELEASED_TARGETS.csv",
            list(released_rows[0]),
            released_rows,
        )
        write_csv(
            package / "LIVE_SURFACE_MANIFEST.csv",
            list(surfaces[0]),
            surfaces,
        )
        write_csv(
            package / "CLOSEOUT_IDENTITY.csv",
            list(closeout_rows[0]),
            closeout_rows,
        )
        (package / "POST_MERGE_PROOF.json").write_text(
            json.dumps(proof, indent=2, sort_keys=True) + "\n"
        )
    print(json.dumps(proof, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
