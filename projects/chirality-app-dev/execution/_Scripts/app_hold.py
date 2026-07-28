#!/usr/bin/env python3
"""Deterministic APP-HOLD-1 corpus scanner and operation gate candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


OPERATIONS = (
    "reliance",
    "dispatch",
    "checking-promotion",
    "accepted-dependency-consumption",
)
ACTIVE_HOLD_STATES = ("HELD", "REPAIR_VALIDATION_PENDING")
FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z0-9_]+):\s*(.*?)\s*$")
DELIVERABLE_RE = re.compile(r"^DEL-\d{2}-\d{2}$")
PACKAGE_RE = re.compile(r"^PKG-\d{2}$")
GIT_OBJECT_RE = re.compile(r"^[0-9a-f]{7,40}$")


class HoldError(RuntimeError):
    """A deterministic validation failure."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def resolve_repo_root(explicit: str | None) -> Path:
    requested = Path(explicit).resolve() if explicit else Path.cwd().resolve()
    proc = git(requested, "rev-parse", "--show-toplevel")
    if proc.returncode != 0:
        raise HoldError(f"not a Git working tree: {requested}")
    canonical = Path(proc.stdout.strip()).resolve()
    if explicit and requested != canonical:
        raise HoldError(
            f"--repo-root must equal the canonical Git top level: {canonical}"
        )
    return canonical


def default_paths(repo_root: Path) -> tuple[Path, Path]:
    app_root = repo_root / "projects" / "chirality-app-dev"
    sow_root = app_root / "execution"
    register = app_root / "execution" / "_Coordination" / "APP_HOLD_REGISTER.csv"
    return sow_root, register


def candidate_root() -> Path | None:
    tool = Path(__file__).resolve()
    if tool.parent.name == "tools" and tool.parent.parent.name.startswith("APP-HOLD-1_"):
        return tool.parent.parent
    return None


def require_exact_path(path: Path, expected: Path, label: str) -> None:
    if path.resolve() != expected.resolve():
        raise HoldError(f"{label} must be exactly {expected.resolve()}: {path.resolve()}")


def require_contained(path: Path, root: Path, label: str) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise HoldError(f"{label} escapes {root.resolve()}: {path.resolve()}") from error


def validate_input_paths(
    repo_root: Path,
    sow_root: Path,
    register: Path,
    *,
    command: str,
    test_fixture_mode: bool,
) -> None:
    default_sow, default_register = default_paths(repo_root)
    require_exact_path(sow_root, default_sow, "SOW root")
    proposal = candidate_root()
    allowed_registers = {default_register.resolve()}
    if proposal:
        require_contained(proposal, repo_root, "candidate root")
        allowed_registers.add((proposal / "APP_HOLD_REGISTER.csv").resolve())
    if test_fixture_mode and command == "scan":
        fixture_roots = [
            repo_root
            / "projects"
            / "chirality-app-dev"
            / "execution"
            / "_Scripts"
            / "tests"
            / "fixtures"
        ]
        if proposal:
            fixture_roots.append(proposal / "tests" / "fixtures")
        if not any(
            _is_relative_to(register.resolve(), root.resolve()) for root in fixture_roots
        ):
            raise HoldError("test fixture register is outside an allowed fixture root")
    elif register.resolve() not in allowed_registers:
        raise HoldError(f"register path is not an allowed APP-HOLD-1 register: {register}")


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise HoldError(f"missing YAML front matter: {path}")
    values: dict[str, str] = {}
    for line_number, line in enumerate(match.group(1).splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace():
            continue
        field = FIELD_RE.match(line)
        if not field:
            raise HoldError(f"malformed top-level front matter at {path}:{line_number}")
        key = field.group(1)
        if key in values:
            raise HoldError(f"duplicate front-matter key {key} at {path}:{line_number}")
        values[key] = field.group(2).strip().strip('"').strip("'")
    required = ("deliverable_id", "package_id", "decomposition_basis")
    missing = [name for name in required if not values.get(name)]
    if missing:
        raise HoldError(f"missing fields {','.join(missing)}: {path}")
    if not DELIVERABLE_RE.fullmatch(values["deliverable_id"]):
        raise HoldError(f"invalid deliverable_id in {path}: {values['deliverable_id']}")
    if not PACKAGE_RE.fullmatch(values["package_id"]):
        raise HoldError(f"invalid package_id in {path}: {values['package_id']}")
    return values


def split_basis(value: str, source: Path) -> tuple[str, str]:
    if "@" not in value:
        raise HoldError(f"decomposition_basis lacks @object in {source}: {value}")
    basis_path, object_id = value.rsplit("@", 1)
    if not basis_path or not GIT_OBJECT_RE.fullmatch(object_id):
        raise HoldError(f"invalid decomposition_basis in {source}: {value}")
    return basis_path, object_id


def inspect_contract(repo_root: Path, path: Path) -> dict[str, Any]:
    values = parse_front_matter(path)
    basis_path, object_id = split_basis(values["decomposition_basis"], path)
    commit_check = git(repo_root, "cat-file", "-e", f"{object_id}^{{commit}}")
    commit_resolves = commit_check.returncode == 0
    path_resolves = False
    if commit_resolves:
        path_check = git(repo_root, "cat-file", "-e", f"{object_id}:{basis_path}")
        path_resolves = path_check.returncode == 0
    status = "CLEAR" if commit_resolves and path_resolves else "HELD"
    if not commit_resolves:
        reason = "UNRESOLVABLE_BASIS_OBJECT"
    elif not path_resolves:
        reason = "BASIS_PATH_MISSING_AT_OBJECT"
    else:
        reason = "BASIS_RESOLVES"
    return {
        "deliverable_id": values["deliverable_id"],
        "package_id": values["package_id"],
        "sow_path": path.relative_to(repo_root).as_posix(),
        "decomposition_basis": values["decomposition_basis"],
        "basis_path": basis_path,
        "basis_commit": object_id,
        "basis_commit_resolves": commit_resolves,
        "basis_path_resolves": path_resolves,
        "status": status,
        "reason": reason,
    }


def scan_corpus(repo_root: Path, sow_root: Path) -> dict[str, Any]:
    if not sow_root.is_dir():
        raise HoldError(f"SOW root does not exist: {sow_root}")
    contracts = [
        inspect_contract(repo_root, path)
        for path in sorted(sow_root.rglob("ScopeOfWork.md"))
        if "_PROPOSALS" not in path.parts
    ]
    if not contracts:
        raise HoldError(f"no ScopeOfWork.md files found below {sow_root}")
    ids = [row["deliverable_id"] for row in contracts]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        raise HoldError(f"duplicate deliverable IDs: {','.join(duplicates)}")
    held = [row for row in contracts if row["status"] == "HELD"]
    basis_proc = git(repo_root, "rev-parse", "HEAD")
    if basis_proc.returncode != 0:
        raise HoldError(f"cannot resolve HEAD: {basis_proc.stderr.strip()}")
    payload = {
        "schema": "chirality-app-hold-scan/v1",
        "repo_head": basis_proc.stdout.strip(),
        "sow_root": sow_root.relative_to(repo_root).as_posix(),
        "contract_count": len(contracts),
        "held_count": len(held),
        "held_deliverables": sorted(row["deliverable_id"] for row in held),
        "contracts": contracts,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    payload["scan_fingerprint_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def load_register(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise HoldError(f"hold register does not exist: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = [
            "hold_id",
            "deliverable_id",
            "package_id",
            "sow_path",
            "decomposition_basis",
            "basis_commit",
            "status",
            "prohibited_operations",
            "entry_path_scope",
            "repin_posture",
            "authority_basis",
        ]
        if reader.fieldnames != required:
            raise HoldError(f"invalid hold-register header: {path}")
        rows = list(reader)
    ids = [row["deliverable_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise HoldError(f"duplicate hold-register deliverable ID: {path}")
    hold_ids = [row["hold_id"] for row in rows]
    if len(hold_ids) != len(set(hold_ids)):
        raise HoldError(f"duplicate hold_id: {path}")
    for row in rows:
        if None in row or any(value is None or not value.strip() for value in row.values()):
            raise HoldError(f"missing or extra hold-register field: {path}")
        if row["hold_id"] != f"APP-HOLD-1-{row['deliverable_id']}":
            raise HoldError(f"hold_id mismatch: {row['deliverable_id']}")
        if not DELIVERABLE_RE.fullmatch(row["deliverable_id"]):
            raise HoldError(f"invalid hold deliverable ID: {row['deliverable_id']}")
        if not PACKAGE_RE.fullmatch(row["package_id"]):
            raise HoldError(f"invalid hold package ID: {row['package_id']}")
        if not GIT_OBJECT_RE.fullmatch(row["basis_commit"]):
            raise HoldError(f"invalid hold basis commit: {row['deliverable_id']}")
        if row["status"] not in ACTIVE_HOLD_STATES:
            raise HoldError(
                f"invalid active hold state {row['status']}: "
                f"{row['deliverable_id']}"
            )
        if row["repin_posture"] != "NO_REPIN":
            raise HoldError(f"invalid repin posture: {row['deliverable_id']}")
        if set(row["prohibited_operations"].split("|")) != set(OPERATIONS):
            raise HoldError(f"operation set mismatch: {row['deliverable_id']}")
        if row["entry_path_scope"] != "ANY":
            raise HoldError(f"hold must bind every entry path: {row['deliverable_id']}")
        expected_authority = (
            "D-APP-75" if row["status"] == "HELD" else "D-APP-79"
        )
        if row["authority_basis"] != expected_authority:
            raise HoldError(
                f"hold authority must be {expected_authority}: "
                f"{row['deliverable_id']}"
            )
    return rows


def compare_register(scan: dict[str, Any], register_path: Path) -> dict[str, Any]:
    rows = load_register(register_path)
    scanned_all = {row["deliverable_id"]: row for row in scan["contracts"]}
    scanned = {
        deliverable_id: row
        for deliverable_id, row in scanned_all.items()
        if row["status"] == "HELD"
    }
    registered = {row["deliverable_id"]: row for row in rows}
    missing = sorted(set(scanned) - set(registered))
    extra = sorted(set(registered) - set(scanned_all))
    field_mismatches: list[dict[str, str]] = []
    status_mismatches: list[dict[str, str]] = []
    for deliverable_id in sorted(set(scanned_all) & set(registered)):
        source = scanned_all[deliverable_id]
        row = registered[deliverable_id]
        for field in (
            "package_id",
            "sow_path",
            "decomposition_basis",
            "basis_commit",
        ):
            if source[field] != row[field]:
                field_mismatches.append(
                    {
                        "deliverable_id": deliverable_id,
                        "field": field,
                        "scan": source[field],
                        "register": row[field],
                    }
                )
        if source["status"] == "CLEAR" and row["status"] == "HELD":
            status_mismatches.append(
                {
                    "deliverable_id": deliverable_id,
                    "scan": source["status"],
                    "register": row["status"],
                }
            )
    match = (
        not missing
        and not extra
        and not field_mismatches
        and not status_mismatches
    )
    return {
        "register_path": register_path.relative_to(register_path.parents[4]).as_posix()
        if len(register_path.parents) > 4
        else str(register_path),
        "register_sha256": sha256_file(register_path),
        "match": match,
        "missing_from_register": missing,
        "extra_in_register": extra,
        "field_mismatches": field_mismatches,
        "status_mismatches": status_mismatches,
        "active_hold_deliverables": sorted(registered),
    }


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo-root")
    parser.add_argument("--sow-root")
    parser.add_argument("--register")
    parser.add_argument("--test-fixture-mode", action="store_true")


def write_json(
    payload: dict[str, Any],
    output: str | None,
    repo_root: Path,
) -> None:
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if output:
        output_path = Path(output).resolve()
        app_execution = (
            repo_root / "projects" / "chirality-app-dev" / "execution"
        ).resolve()
        allowed_roots = [
            app_execution / "_Coordination" / "AgentRuns",
            app_execution / "_Evaluation",
        ]
        proposal = candidate_root()
        if proposal:
            allowed_roots.append(proposal)
        if not any(_is_relative_to(output_path, root.resolve()) for root in allowed_roots):
            raise HoldError(f"output path is outside an allowed evidence root: {output_path}")
        if output_path.suffix != ".json":
            raise HoldError(f"output path must end in .json: {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(encoded, encoding="utf-8")
    else:
        sys.stdout.write(encoded)


def command_scan(args: argparse.Namespace) -> int:
    repo_root = resolve_repo_root(args.repo_root)
    default_sow, default_register = default_paths(repo_root)
    sow_root = Path(args.sow_root).resolve() if args.sow_root else default_sow
    register = Path(args.register).resolve() if args.register else default_register
    validate_input_paths(
        repo_root,
        sow_root,
        register,
        command="scan",
        test_fixture_mode=args.test_fixture_mode,
    )
    scan = scan_corpus(repo_root, sow_root)
    if args.require_register_match or register.exists():
        comparison = compare_register(scan, register)
        scan["register"] = comparison
        if not comparison["match"]:
            scan["verdict"] = "BLOCK_REGISTER_DRIFT"
            write_json(scan, args.output, repo_root)
            return 4
    scan["verdict"] = "PASS"
    write_json(scan, args.output, repo_root)
    return 0


def evaluate_targets(
    known: dict[str, dict[str, Any]],
    registered: dict[str, dict[str, str]],
    *,
    operation: str,
    entry_path: str,
    targets: list[str],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for target in sorted(set(targets)):
        contract = known[target]
        result: dict[str, Any] = {
            "deliverable_id": target,
            "contract_status": contract["status"],
            "hold_status": (
                registered[target]["status"]
                if target in registered
                else "NOT_HELD"
            ),
            "operation": operation,
            "entry_path": entry_path,
        }
        if target in registered:
            result.update({"verdict": "BLOCK_APP_HOLD"})
        else:
            result.update({"verdict": "ALLOW"})
        results.append(result)
    return results


def command_check(args: argparse.Namespace) -> int:
    repo_root = resolve_repo_root(args.repo_root)
    default_sow, default_register = default_paths(repo_root)
    sow_root = Path(args.sow_root).resolve() if args.sow_root else default_sow
    register = Path(args.register).resolve() if args.register else default_register
    validate_input_paths(
        repo_root,
        sow_root,
        register,
        command="check",
        test_fixture_mode=args.test_fixture_mode,
    )
    scan = scan_corpus(repo_root, sow_root)
    comparison = compare_register(scan, register)
    if not comparison["match"]:
        payload = {
            "schema": "chirality-app-hold-check/v1",
            "verdict": "BLOCK_REGISTER_DRIFT",
            "operation": args.operation,
            "entry_path": args.entry_path,
            "targets": sorted(set(args.target)),
            "scan": scan,
            "register": comparison,
        }
        write_json(payload, args.output, repo_root)
        return 4
    known = {row["deliverable_id"]: row for row in scan["contracts"]}
    registered = {
        row["deliverable_id"]: row for row in load_register(register)
    }
    unknown = sorted(set(args.target) - set(known))
    if unknown:
        raise HoldError(f"unknown target deliverables: {','.join(unknown)}")
    results = evaluate_targets(
        known,
        registered,
        operation=args.operation,
        entry_path=args.entry_path,
        targets=args.target,
    )
    allowed = all(
        row["verdict"] == "ALLOW" for row in results
    )
    payload = {
        "schema": "chirality-app-hold-check/v1",
        "repo_head": scan["repo_head"],
        "scan_fingerprint_sha256": scan["scan_fingerprint_sha256"],
        "scan_held_deliverables": scan["held_deliverables"],
        "active_hold_deliverables": sorted(registered),
        "register_sha256": comparison["register_sha256"],
        "operation": args.operation,
        "entry_path": args.entry_path,
        "targets": sorted(set(args.target)),
        "results": results,
        "verdict": "ALLOW" if allowed else "BLOCK_APP_HOLD",
    }
    write_json(payload, args.output, repo_root)
    return 0 if allowed else 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan = subparsers.add_parser("scan")
    add_common_arguments(scan)
    scan.add_argument("--require-register-match", action="store_true")
    scan.add_argument("--output")
    scan.set_defaults(handler=command_scan)
    check = subparsers.add_parser("check")
    add_common_arguments(check)
    check.add_argument("--operation", required=True, choices=OPERATIONS)
    check.add_argument("--entry-path", required=True)
    check.add_argument("--target", action="append", required=True)
    check.add_argument("--output")
    check.set_defaults(handler=command_check)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except HoldError as error:
        sys.stderr.write(f"APP_HOLD_ERROR: {error}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
