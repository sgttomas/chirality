#!/usr/bin/env python3
"""Deterministic APP-HOLD-1 corpus scanner and operation gate candidate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import stat
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
REGISTER_FIELDS = (
    "hold_id",
    "record_kind",
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
    "allowed_operation",
    "allowed_entry_paths",
    "decomposition_sha256",
    "companion_register_sha256",
    "pointer_sha256",
    "target_folder",
    "allowed_scaffold_paths",
)
RECORD_KINDS = ("HOLD", "STRUCTURAL_BOOTSTRAP", "SOW_INITIALIZATION")
NONE = "NONE"
BOOTSTRAP_TARGET = "DEL-09-07"
BOOTSTRAP_PACKAGE = "PKG-09"
BOOTSTRAP_AUTHORITY = "D-APP-104"
BOOTSTRAP_OPERATION = "dispatch"
BOOTSTRAP_ENTRY_PATHS = (
    "SCA-APP-009:GATE5:PREPARATION:CANDIDATE_MIRROR",
    "SCA-APP-009:GATE5:PREPARATION:ACTUAL_WORKTREE",
)
BOOTSTRAP_DECOMPOSITION_PATH = (
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
BOOTSTRAP_COMPANION_PATH = (
    "projects/chirality-app-dev/execution/_Decomposition/"
    "contract_invariant_coverage_register.csv"
)
BOOTSTRAP_POINTER_PATH = (
    "projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md"
)
BOOTSTRAP_TARGET_FOLDER = (
    "projects/chirality-app-dev/execution/"
    "PKG-09_Validation_Packaging_Security_and_Release/1_Working/"
    "DEL-09-07_Two-Job_Runtime-Control_Installer_Migration_and_Rollback"
)
BOOTSTRAP_SOW_PATH = f"{BOOTSTRAP_TARGET_FOLDER}/ScopeOfWork.md"
BOOTSTRAP_SCAFFOLD_PATHS = (
    "_CONTEXT.md",
    "_STATUS.md",
    "_REFERENCES.md",
    "_DEPENDENCIES.md",
    "_SEMANTIC.md",
)
BOOTSTRAP_DECOMPOSITION_SHA256 = (
    "e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97"
)
BOOTSTRAP_COMPANION_SHA256 = (
    "e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70"
)
BOOTSTRAP_POINTER_SHA256 = (
    "12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b"
)
INIT_ENTRY_PATH = "PROJECT_SETUP:SCOPE_OF_WORK:INIT"
INIT_POINTER_SHA256 = "f235ced4526aac51c4e7f5307ac619f3500e824c3549960b106bb80b67a6e17c"
INIT_SCAFFOLD_HASHES = {
    "_CONTEXT.md": "5d7b947877629933a0028eed9cec66a7e6257424b6197a38f12337c341c50e82",
    "_DEPENDENCIES.md": "b0ef360385c7a2619fd1df2add22dbde41dca7ad8fb1989ad56a23b430a4aecb",
    "_REFERENCES.md": "1449ed503ccafe13897f0e589104826ab4386b99fb4d18b42e382529a50a5f1d",
    "_SEMANTIC.md": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "_STATUS.md": "b2602ef75ff4f9f57e722081849b0061cdc494a58c92b38a283175beb5323dab",
}
RELEASED_IDS = frozenset(
    {
        "DEL-02-01",
        "DEL-02-02",
        "DEL-02-04",
        "DEL-05-04",
        "DEL-08-02",
        "DEL-08-03",
    }
)
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
    if path == repo_root / BOOTSTRAP_SOW_PATH:
        if not _no_symlink_components(repo_root, path) or not path.is_file():
            raise HoldError(f"SOW-initialization contract path is not regular: {path}")
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
        if reader.fieldnames != list(REGISTER_FIELDS):
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
        if row["record_kind"] not in RECORD_KINDS:
            raise HoldError(
                f"invalid APP-HOLD-1 record kind {row['record_kind']}: "
                f"{row['deliverable_id']}"
            )
        if not DELIVERABLE_RE.fullmatch(row["deliverable_id"]):
            raise HoldError(f"invalid hold deliverable ID: {row['deliverable_id']}")
        if not PACKAGE_RE.fullmatch(row["package_id"]):
            raise HoldError(f"invalid hold package ID: {row['package_id']}")
        if row["repin_posture"] != "NO_REPIN":
            raise HoldError(f"invalid repin posture: {row['deliverable_id']}")
        if row["record_kind"] == "HOLD":
            _validate_hold_row(row)
        elif row["record_kind"] == "STRUCTURAL_BOOTSTRAP":
            _validate_bootstrap_row(row)
        else:
            _validate_initialization_row(row)
    return rows


def _validate_hold_row(row: dict[str, str]) -> None:
    target = row["deliverable_id"]
    if row["hold_id"] != f"APP-HOLD-1-{target}":
        raise HoldError(f"hold_id mismatch: {target}")
    if target in RELEASED_IDS:
        raise HoldError(
            f"released target cannot appear in the active hold register: {target}"
        )
    if not GIT_OBJECT_RE.fullmatch(row["basis_commit"]):
        raise HoldError(f"invalid hold basis commit: {target}")
    if row["status"] not in ACTIVE_HOLD_STATES:
        raise HoldError(f"invalid active hold state {row['status']}: {target}")
    if set(row["prohibited_operations"].split("|")) != set(OPERATIONS):
        raise HoldError(f"operation set mismatch: {target}")
    if row["entry_path_scope"] != "ANY":
        raise HoldError(f"hold must bind every entry path: {target}")
    expected_authority = "D-APP-75" if row["status"] == "HELD" else "D-APP-79"
    if row["authority_basis"] != expected_authority:
        raise HoldError(f"hold authority must be {expected_authority}: {target}")
    for field in (
        "allowed_operation",
        "allowed_entry_paths",
        "decomposition_sha256",
        "companion_register_sha256",
        "pointer_sha256",
        "target_folder",
        "allowed_scaffold_paths",
    ):
        if row[field] != NONE:
            raise HoldError(f"hold row has bootstrap field {field}: {target}")


def _validate_bootstrap_row(row: dict[str, str]) -> None:
    expected = {
        "hold_id": f"APP-HOLD-1-BOOTSTRAP-{BOOTSTRAP_TARGET}",
        "deliverable_id": BOOTSTRAP_TARGET,
        "package_id": BOOTSTRAP_PACKAGE,
        "sow_path": BOOTSTRAP_SOW_PATH,
        "decomposition_basis": NONE,
        "basis_commit": NONE,
        "status": "STRUCTURAL_BOOTSTRAP",
        "prohibited_operations": NONE,
        "entry_path_scope": "EXACT",
        "authority_basis": BOOTSTRAP_AUTHORITY,
        "allowed_operation": BOOTSTRAP_OPERATION,
        "allowed_entry_paths": "|".join(BOOTSTRAP_ENTRY_PATHS),
        "decomposition_sha256": BOOTSTRAP_DECOMPOSITION_SHA256,
        "companion_register_sha256": BOOTSTRAP_COMPANION_SHA256,
        "pointer_sha256": BOOTSTRAP_POINTER_SHA256,
        "target_folder": BOOTSTRAP_TARGET_FOLDER,
        "allowed_scaffold_paths": "|".join(BOOTSTRAP_SCAFFOLD_PATHS),
    }
    for field, value in expected.items():
        if row[field] != value:
            raise HoldError(
                f"structural-bootstrap {field} mismatch: "
                f"{row['deliverable_id']}"
            )


def partition_register_rows(
    rows: list[dict[str, str]],
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    holds = {
        row["deliverable_id"]: row
        for row in rows
        if row["record_kind"] == "HOLD"
    }
    bootstraps = {
        row["deliverable_id"]: row
        for row in rows
        if row["record_kind"] == "STRUCTURAL_BOOTSTRAP"
    }
    return holds, bootstraps


def _validate_initialization_row(row: dict[str, str]) -> None:
    """One closed, typed admission; no caller-supplied exception parameters."""
    expected = dict(row)
    expected.update({
        "record_kind": "STRUCTURAL_BOOTSTRAP",
        "hold_id": f"APP-HOLD-1-BOOTSTRAP-{BOOTSTRAP_TARGET}",
        "status": "STRUCTURAL_BOOTSTRAP",
        "authority_basis": BOOTSTRAP_AUTHORITY,
        "allowed_entry_paths": "|".join(BOOTSTRAP_ENTRY_PATHS),
        "pointer_sha256": BOOTSTRAP_POINTER_SHA256,
    })
    _validate_bootstrap_row(expected)
    for field, value in {
        "record_kind": "SOW_INITIALIZATION",
        "hold_id": "APP-HOLD-1-INIT-DEL-09-07",
        "status": "SOW_INITIALIZATION",
        "authority_basis": "D-APP-107",
        "allowed_entry_paths": INIT_ENTRY_PATH,
        "pointer_sha256": INIT_POINTER_SHA256,
    }.items():
        if row[field] != value:
            raise HoldError(f"SOW-initialization {field} mismatch: {row['deliverable_id']}")


def _no_symlink_components(root: Path, path: Path) -> bool:
    """Reject lexical traversal and every symlink below the canonical checkout."""
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    if ".." in relative.parts:
        return False
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            return False
    return True


def inspect_initialization_admission(
    repo_root: Path, row: dict[str, str], known: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    _validate_initialization_row(row)
    folder = repo_root / row["target_folder"]
    sow = repo_root / row["sow_path"]
    errors: list[str] = []
    paths = {
        BOOTSTRAP_DECOMPOSITION_PATH: row["decomposition_sha256"],
        BOOTSTRAP_COMPANION_PATH: row["companion_register_sha256"],
        BOOTSTRAP_POINTER_PATH: row["pointer_sha256"],
        **{f"{row['target_folder']}/{name}": digest
           for name, digest in INIT_SCAFFOLD_HASHES.items()},
    }
    for relative, expected in paths.items():
        path = repo_root / relative
        if not _no_symlink_components(repo_root, path):
            errors.append(f"SYMLINK_OR_ESCAPE:{relative}")
            continue
        actual, error = _regular_file_sha256(path)
        if error or actual != expected:
            errors.append(f"SOURCE_HASH_MISMATCH:{relative}")
    if not _no_symlink_components(repo_root, folder) or not folder.is_dir():
        errors.append("TARGET_FOLDER_INVALID")
    else:
        # INIT may persist evidence before dispatch. Only regular files and
        # directories inside _run_records are permitted beyond the five inputs.
        for directory, directories, files in os.walk(
            folder, followlinks=False,
            onerror=lambda error: errors.append(f"UNREADABLE_DIRECTORY:{error.errno}"),
        ):
            parent = Path(directory)
            for name in directories + files:
                path = parent / name
                relative = path.relative_to(folder)
                if path.is_symlink():
                    errors.append(f"SYMLINK:{relative}")
                elif relative.parts[0] == "_run_records":
                    if len(relative.parts) == 1 and not path.is_dir():
                        errors.append("RUN_RECORDS_NOT_DIRECTORY")
                    elif not (path.is_dir() or path.is_file()):
                        errors.append(f"NOT_REGULAR:{relative}")
                elif len(relative.parts) != 1 or name not in INIT_SCAFFOLD_HASHES:
                    errors.append(f"EXTRA_PATH:{relative}")
    absent = not sow.exists() and not sow.is_symlink()
    eligible = absent and BOOTSTRAP_TARGET not in known and not errors
    return {
        "admission_kind": "SOW_INITIALIZATION",
        "state": "ELIGIBLE" if eligible else "INACTIVE",
        "eligible": eligible,
        "scope_of_work_absent": absent,
        "errors": errors,
    }


def evaluate_initialization_target(
    repo_root: Path, row: dict[str, str], known: dict[str, dict[str, Any]],
    *, operation: str, entry_path: str,
) -> dict[str, Any]:
    admission = inspect_initialization_admission(repo_root, row, known)
    admitted = (admission["eligible"] and operation == "dispatch"
                and entry_path == INIT_ENTRY_PATH)
    return {
        "deliverable_id": row["deliverable_id"],
        "admission_kind": "SOW_INITIALIZATION",
        "initialization": admission,
        "operation": operation,
        "entry_path": entry_path,
        "verdict": "ALLOW" if admitted else "BLOCK_SOW_INITIALIZATION",
    }


def _regular_file_sha256(path: Path) -> tuple[str | None, str | None]:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | os.O_NONBLOCK
    try:
        descriptor = os.open(path, flags)
    except FileNotFoundError:
        return None, "MISSING_OR_NOT_REGULAR"
    except OSError as error:
        return None, f"UNREADABLE_OR_SYMLINK:{error.errno}"
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            return None, "MISSING_OR_NOT_REGULAR"
        digest = hashlib.sha256()
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
        return digest.hexdigest(), None
    except OSError as error:
        return None, f"UNREADABLE_OR_SYMLINK:{error.errno}"
    finally:
        os.close(descriptor)


def inspect_bootstrap_admission(
    repo_root: Path,
    row: dict[str, str],
    known: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    target = row["deliverable_id"]
    authority_paths = {
        "decomposition": repo_root / BOOTSTRAP_DECOMPOSITION_PATH,
        "companion_register": repo_root / BOOTSTRAP_COMPANION_PATH,
        "pointer": repo_root / BOOTSTRAP_POINTER_PATH,
    }
    expected_hashes = {
        "decomposition": row["decomposition_sha256"],
        "companion_register": row["companion_register_sha256"],
        "pointer": row["pointer_sha256"],
    }
    authority: dict[str, dict[str, Any]] = {}
    for label, path in authority_paths.items():
        actual, error = _regular_file_sha256(path)
        authority[label] = {
            "path": path.relative_to(repo_root).as_posix(),
            "expected_sha256": expected_hashes[label],
            "actual_sha256": actual,
            "match": actual == expected_hashes[label],
            "error": error,
        }

    sow = repo_root / row["sow_path"]
    sow_absent = not sow.exists() and not sow.is_symlink()
    folder = repo_root / row["target_folder"]
    allowed_names = set(row["allowed_scaffold_paths"].split("|"))
    folder_errors: list[str] = []
    observed_names: list[str] = []
    try:
        folder_metadata = folder.lstat()
    except FileNotFoundError:
        folder_metadata = None
    except OSError as error:
        folder_metadata = None
        folder_errors.append(f"TARGET_FOLDER_UNREADABLE:{error.errno}")
    if folder_metadata is not None:
        if stat.S_ISLNK(folder_metadata.st_mode):
            folder_errors.append("TARGET_FOLDER_SYMLINK")
        elif not stat.S_ISDIR(folder_metadata.st_mode):
            folder_errors.append("TARGET_FOLDER_NOT_DIRECTORY")
        else:
            try:
                with os.scandir(folder) as iterator:
                    entries = sorted(iterator, key=lambda item: item.name)
                for child in entries:
                    observed_names.append(child.name)
                    if child.name not in allowed_names:
                        folder_errors.append(f"EXTRA_PATH:{child.name}")
                    elif child.is_symlink():
                        folder_errors.append(
                            f"AUTHORIZED_PATH_SYMLINK:{child.name}"
                        )
                    elif not child.is_file(follow_symlinks=False):
                        folder_errors.append(
                            f"AUTHORIZED_PATH_NOT_REGULAR:{child.name}"
                        )
            except OSError as error:
                folder_errors.append(f"TARGET_FOLDER_UNREADABLE:{error.errno}")

    conditions = {
        "target_is_exact": target == BOOTSTRAP_TARGET,
        "package_is_exact": row["package_id"] == BOOTSTRAP_PACKAGE,
        "target_unknown_to_sow_scan": target not in known,
        "scope_of_work_absent": sow_absent,
        "decomposition_hash_matches": authority["decomposition"]["match"],
        "companion_register_hash_matches": authority["companion_register"]["match"],
        "pointer_preimage_hash_matches": authority["pointer"]["match"],
        "target_folder_shape_allowed": not folder_errors,
    }
    eligible = all(conditions.values())
    return {
        "admission_kind": "STRUCTURAL_BOOTSTRAP",
        "state": "ELIGIBLE" if eligible else "INACTIVE",
        "eligible": eligible,
        "conditions": conditions,
        "authority": authority,
        "scope_of_work_path": row["sow_path"],
        "target_folder": row["target_folder"],
        "observed_scaffold_paths": observed_names,
        "allowed_scaffold_paths": sorted(allowed_names),
        "folder_errors": folder_errors,
    }


def evaluate_bootstrap_target(
    repo_root: Path,
    row: dict[str, str],
    known: dict[str, dict[str, Any]],
    *,
    operation: str,
    entry_path: str,
) -> dict[str, Any]:
    admission = inspect_bootstrap_admission(repo_root, row, known)
    operation_matches = operation == row["allowed_operation"]
    entry_path_matches = entry_path in row["allowed_entry_paths"].split("|")
    admitted = admission["eligible"] and operation_matches and entry_path_matches
    return {
        "deliverable_id": row["deliverable_id"],
        "contract_status": "ABSENT",
        "hold_status": "NOT_HELD",
        "operation": operation,
        "entry_path": entry_path,
        "admission_kind": "STRUCTURAL_BOOTSTRAP",
        "operation_matches": operation_matches,
        "entry_path_matches": entry_path_matches,
        "bootstrap": admission,
        "verdict": "ALLOW" if admitted else "BLOCK_STRUCTURAL_BOOTSTRAP",
    }


def compare_register(scan: dict[str, Any], register_path: Path) -> dict[str, Any]:
    rows = load_register(register_path)
    scanned_all = {row["deliverable_id"]: row for row in scan["contracts"]}
    scanned = {
        deliverable_id: row
        for deliverable_id, row in scanned_all.items()
        if row["status"] == "HELD"
    }
    registered, bootstraps = partition_register_rows(rows)
    missing = sorted(set(scanned) - set(registered))
    extra = sorted(set(registered) - set(scanned_all))
    bootstrap_contract_collisions = sorted(set(bootstraps) & set(scanned_all))
    field_mismatches: list[dict[str, str]] = []
    initializations = {row["deliverable_id"]: row for row in rows
                       if row["record_kind"] == "SOW_INITIALIZATION"}
    for target in sorted(set(initializations) & set(scanned_all)):
        for field in ("package_id", "sow_path"):
            if scanned_all[target][field] != initializations[target][field]:
                field_mismatches.append({"deliverable_id": target, "field": field,
                                         "scan": scanned_all[target][field],
                                         "register": initializations[target][field]})
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
        and not bootstrap_contract_collisions
    )
    root_proc = git(register_path.parent, "rev-parse", "--show-toplevel")
    if root_proc.returncode != 0:
        raise HoldError(
            f"cannot resolve repository for hold register: {register_path}"
        )
    repo_root = Path(root_proc.stdout.strip()).resolve()
    bootstrap_admissions = [
        inspect_bootstrap_admission(repo_root, row, scanned_all)
        for row in bootstraps.values()
    ]
    return {
        "register_path": register_path.relative_to(register_path.parents[4]).as_posix()
        if len(register_path.parents) > 4
        else str(register_path),
        "register_sha256": sha256_file(register_path),
        "match": match,
        "missing_from_register": missing,
        "missing_repair_pending_from_register": [],
        "extra_in_register": extra,
        "field_mismatches": field_mismatches,
        "status_mismatches": status_mismatches,
        "active_hold_deliverables": sorted(registered),
        "structural_bootstrap_deliverables": sorted(bootstraps),
        "bootstrap_contract_collisions": bootstrap_contract_collisions,
        "bootstrap_admissions": bootstrap_admissions,
        "sow_initialization_deliverables": sorted(initializations),
        "sow_initialization_admissions": [
            {"admission_kind": "SOW_INITIALIZATION", "state": "CONSUMED",
             "eligible": False, "deliverable_id": target}
            if target in scanned_all else inspect_initialization_admission(repo_root, row, scanned_all)
            for target, row in initializations.items()
        ],
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
    rows = load_register(register)
    registered, bootstraps = partition_register_rows(rows)
    initializations = {row["deliverable_id"]: row for row in rows
                       if row["record_kind"] == "SOW_INITIALIZATION"}
    unknown = sorted(set(args.target) - set(known) - set(bootstraps) - set(initializations))
    if unknown:
        raise HoldError(f"unknown target deliverables: {','.join(unknown)}")
    ordinary_targets = [target for target in args.target if target in known]
    results = evaluate_targets(
        known,
        registered,
        operation=args.operation,
        entry_path=args.entry_path,
        targets=ordinary_targets,
    )
    for target in sorted(set(args.target) & set(bootstraps)):
        results.append(
            evaluate_bootstrap_target(
                repo_root,
                bootstraps[target],
                known,
                operation=args.operation,
                entry_path=args.entry_path,
            )
        )
    for target in sorted(set(args.target) & set(initializations) - set(known)):
        results.append(evaluate_initialization_target(
            repo_root, initializations[target], known,
            operation=args.operation, entry_path=args.entry_path,
        ))
    results.sort(key=lambda row: row["deliverable_id"])
    allowed = all(row["verdict"] == "ALLOW" for row in results)
    blocked_verdict = (
        "BLOCK_APP_HOLD"
        if any(row["verdict"] == "BLOCK_APP_HOLD" for row in results)
        else "BLOCK_SOW_INITIALIZATION"
        if any(row["verdict"] == "BLOCK_SOW_INITIALIZATION" for row in results)
        else "BLOCK_STRUCTURAL_BOOTSTRAP"
    )
    payload = {
        "schema": "chirality-app-hold-check/v1",
        "repo_head": scan["repo_head"],
        "scan_fingerprint_sha256": scan["scan_fingerprint_sha256"],
        "scan_held_deliverables": scan["held_deliverables"],
        "active_hold_deliverables": sorted(registered),
        "structural_bootstrap_deliverables": sorted(bootstraps),
        "register_sha256": comparison["register_sha256"],
        "operation": args.operation,
        "entry_path": args.entry_path,
        "targets": sorted(set(args.target)),
        "results": results,
        "verdict": "ALLOW" if allowed else blocked_verdict,
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
