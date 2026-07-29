#!/usr/bin/env python3
"""Validate the OD8-RAT / D-APP-82 App current-state ratification package.

Two stages are supported.

`--stage prepared` (the state this package is committed in) checks that the
packet is internally consistent and that the decision record still carries
exactly the expected owner-return fences, one per enumerated decision plus the
D-APP-78 selection token.

`--stage completed` (the default) is the post-owner-session check: zero
placeholder fences remain anywhere in the decision record, the D-APP-82
register row exists and has left `AWAITING_RULING`, and every path in
`LIVE_SURFACE_MANIFEST.csv` reproduces its recorded postimage SHA-256 — the
ruling record included, so the manifest and the record cannot drift apart.

The tool is read-only. Exit 0 means the requested stage is conformant, exit 1
means one or more violations, exit 2 means an operational failure. Conformance
is structural evidence only; it does not authenticate any owner return.

The expected fence strings are assembled from fragments below so that this
file never itself contains a literal placeholder string; a repository-wide
search for the fences therefore stays clean once the record is completed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


PACKAGE_RELDIR = (
    "projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/"
    "OD8-RAT_APP_RATIFICATION_2026-07-28"
)
DECISION_RELPATH = (
    "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "D-APP-82_RULING_OD8_RATIFICATION_2026-07-28.md"
)
REGISTER_RELPATH = (
    "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md"
)

DECISION_ID = "D-APP-82"
RATIFIED_IDS = ["D-APP-78", "D-APP-79", "D-APP-80", "D-APP-81"]

_OPEN = "<" + "<"
_CLOSE = ">" + ">"
_RULING_FENCE = "RULING PLACEHOLDER — OWNER RETURN VERBATIM: "
_TOKEN_FENCE = (
    "TOKEN RETURN PLACEHOLDER — OWNER RETURNS VERBATIM: APPROVE OD6-G2-T1-A"
)
EXPECTED_FENCES = [f"{_OPEN}{_RULING_FENCE}{did}{_CLOSE}" for did in RATIFIED_IDS]
EXPECTED_FENCES.append(f"{_OPEN}{_TOKEN_FENCE}{_CLOSE}")

FENCE_PATTERN = re.compile(re.escape(_OPEN) + r"[^<>]*PLACEHOLDER[^<>]*" + re.escape(_CLOSE))

PENDING_TOKEN = "PENDING_OWNER_SESSION"
DEFERRED_TOKEN = "SEE_ARTIFACT_HASHES"
ABSENT_TOKEN = "ABSENT"
HASHLIST_NAME = "ARTIFACT_HASHES.sha256"
MANIFEST_NAME = "LIVE_SURFACE_MANIFEST.csv"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest(package: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with (package / MANIFEST_NAME).open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if not row.get("path") or row["path"].startswith("#"):
                continue
            rows.append({k: (v or "").strip() for k, v in row.items()})
    return rows


def read_hashlist(package: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in (package / HASHLIST_NAME).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, _, name = line.partition("  ")
        entries[name.strip()] = digest.strip()
    return entries


def register_row(repo_root: Path) -> list[str] | None:
    text = (repo_root / REGISTER_RELPATH).read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith(f"| {DECISION_ID} |"):
            cells = [cell.strip() for cell in line.split("|")]
            return cells[1:-1]
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage",
        choices=("prepared", "completed"),
        default="completed",
        help="which lifecycle stage of the package to validate",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="repository root (default: derived from this file's location)",
    )
    args = parser.parse_args(argv)

    try:
        repo_root = (
            Path(args.repo_root).resolve()
            if args.repo_root
            else Path(__file__).resolve().parents[6]
        )
        package = repo_root / PACKAGE_RELDIR
        decision_path = repo_root / DECISION_RELPATH
        if not package.is_dir():
            print(f"operational failure: package not found at {package}")
            return 2
        if not decision_path.is_file():
            print(f"operational failure: decision record not found at {decision_path}")
            return 2
        manifest = read_manifest(package)
        decision_text = decision_path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - operational path
        print(f"operational failure: {exc}")
        return 2

    violations: list[str] = []
    pending: list[str] = []

    # 1. placeholder fences
    found = FENCE_PATTERN.findall(decision_text)
    if args.stage == "completed":
        if found:
            violations.append(
                f"{len(found)} placeholder fence(s) remain in the decision record"
            )
    else:
        for fence in EXPECTED_FENCES:
            count = decision_text.count(fence)
            if count != 1:
                violations.append(
                    f"expected exactly one occurrence of a fence for "
                    f"{fence[len(_OPEN):-len(_CLOSE)]!r}, found {count}"
                )
        if len(found) != len(EXPECTED_FENCES):
            violations.append(
                f"expected {len(EXPECTED_FENCES)} placeholder fences, found {len(found)}"
            )

    # 2. every ratified decision is enumerated in the record
    for did in RATIFIED_IDS:
        if did not in decision_text:
            violations.append(f"decision record does not enumerate {did}")

    # 3. register row
    cells = register_row(repo_root)
    if cells is None:
        violations.append(f"no {DECISION_ID} row found in the decision register")
        state = None
    elif len(cells) != 6:
        violations.append(
            f"{DECISION_ID} register row has {len(cells)} columns, expected 6"
        )
        state = None
    else:
        state = cells[3]
        if DECISION_RELPATH.split("_DECISIONS/")[-1] not in cells[5]:
            violations.append(
                f"{DECISION_ID} register row does not cite the ruling record"
            )
        if args.stage == "completed" and state == "AWAITING_RULING":
            violations.append(
                f"{DECISION_ID} register row still reads AWAITING_RULING"
            )
        if args.stage == "prepared" and state != "AWAITING_RULING":
            violations.append(
                f"{DECISION_ID} register row reads {state!r}, expected AWAITING_RULING"
            )

    # 4. manifest postimages, including the ruling record itself
    hashlist: dict[str, str] = {}
    if (package / HASHLIST_NAME).is_file():
        hashlist = read_hashlist(package)
    elif args.stage == "completed":
        violations.append(f"{HASHLIST_NAME} is missing")

    for row in manifest:
        rel = row["path"]
        target = repo_root / rel
        if not target.is_file():
            violations.append(f"manifest path does not exist: {rel}")
            continue
        actual = sha256_file(target)
        expected = row["postimage_sha256"]
        if expected == PENDING_TOKEN:
            pending.append(rel)
            if args.stage == "completed":
                violations.append(
                    f"manifest postimage for {rel} is still {PENDING_TOKEN}"
                )
            continue
        if expected == DEFERRED_TOKEN:
            name = Path(rel).name
            if name == HASHLIST_NAME:
                continue
            recorded = hashlist.get(name)
            if recorded is None:
                if hashlist:
                    violations.append(f"{name} is absent from {HASHLIST_NAME}")
                continue
            if recorded != actual:
                violations.append(
                    f"{name} does not match its {HASHLIST_NAME} entry"
                )
            continue
        if expected != actual:
            violations.append(
                f"postimage mismatch for {rel}: manifest {expected}, actual {actual}"
            )

    # 5. hash list covers the package
    if hashlist:
        for path in sorted(package.iterdir()):
            if not path.is_file() or path.name == HASHLIST_NAME:
                continue
            recorded = hashlist.get(path.name)
            if recorded is None:
                violations.append(f"{path.name} is absent from {HASHLIST_NAME}")
            elif recorded != sha256_file(path):
                violations.append(f"{path.name} does not match {HASHLIST_NAME}")

    result = {
        "stage": args.stage,
        "repo_root": str(repo_root),
        "manifest_rows": len(manifest),
        "placeholder_fences_found": len(found),
        "register_state": state,
        "pending_postimages": pending,
        "violations": violations,
        "verdict": "PASS" if not violations else "FAIL",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not violations else 1


if __name__ == "__main__":
    sys.exit(main())
