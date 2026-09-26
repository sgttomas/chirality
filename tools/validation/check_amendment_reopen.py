#!/usr/bin/env python3
"""Check that an accepted scope-change amendment authorizes reopening an
``ISSUED`` deliverable (``ISSUED -> IN_PROGRESS``; SPEC section 3.3, D-GOV-50,
D-GOV-51).

Usage::

    python3 tools/validation/check_amendment_reopen.py \\
        --deliverable <DEL-ID | deliverable folder> \\
        --amendment <AMENDMENT_ID | amendment snapshot path> \\
        [--scope-change-root <dir>] [--project-root <dir>] [--json]

The amendment is admitted only when all of these hold:

1. **Group 3 accepted.** ``checkpoint_snapshots/<ID>_GROUP-3_*/`` under the
   scope-change root holds ``ACCEPTED_MANIFEST.csv`` and a ``DECISION.md``
   whose first heading reads ``# <ID> checkpoint group 3 — accepted ...``.
   Group-1 or group-2 decisions and candidate ``SCA-*`` snapshots do not
   count.
2. **Register bound by hash.** The amendment's group-2 decision snapshot
   (``checkpoint_snapshots/<ID>_GROUP-2_*/ACCEPTED_MANIFEST.csv``) binds one
   action register: the row whose file name begins ``Amendment_Actions`` and
   ends ``.csv`` (where several such rows exist, the one whose ``Role`` names
   the ``action register``). That file lies inside the scope-change root and
   its current SHA-256 equals the bound value.
3. **Qualifying row.** A register row has ``EntityType`` ``DELIVERABLE`` and
   ``EntityID`` equal to the deliverable ID (or the ID followed by ``_`` and a
   label), ``AmendmentID`` equal to the amendment (when the column is
   filled), and ``ActionType`` ``MODIFY``, or ``RECLASSIFY`` with
   ``ScopeChanging`` ``YES``. A register without the ``ScopeChanging`` column
   is a legacy register: its ``RECLASSIFY`` rows are refused, and the human
   records that reopening directly; its ``MODIFY`` rows are admitted.

Every path is resolved inside the project root (the git top level by
default). The amendment records must lie inside the scope-change root;
paths or symlinks that leave it are refused. When the deliverable is given as
a folder, the scope-change root must belong to the same execution root.

Limits: the check reads recorded structure and hashes. It does not establish
that the human's act was genuine or interpret the decision text beyond the
heading; it grants nothing (K-AUTH-1). A run that records group 3 only by
moving ``_LATEST.md``, or has no hash-bound group-2 decision snapshot, is
refused; the human then records a lawful reopening directly.

Exit codes: 0 admitted; 1 refused (``REFUSE <CODE>: <reason>`` on stderr, or
the JSON object on stdout with ``--json``); 2 usage or operational error.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

ADMITTED = "ADMITTED"

# Refusal codes (stable; mirrored by consumers such as the App validator).
AMENDMENT_UNRESOLVED = "AMENDMENT_UNRESOLVED"
SCOPE_CHANGE_ROOT_NOT_FOUND = "SCOPE_CHANGE_ROOT_NOT_FOUND"
PATH_ESCAPE = "PATH_ESCAPE"
AMENDMENT_OUTSIDE_DELIVERABLE_ROOT = "AMENDMENT_OUTSIDE_DELIVERABLE_ROOT"
GROUP3_NOT_ACCEPTED = "GROUP3_NOT_ACCEPTED"
GROUP2_MANIFEST_MISSING = "GROUP2_MANIFEST_MISSING"
MANIFEST_SCHEMA = "MANIFEST_SCHEMA"
REGISTER_NOT_BOUND = "REGISTER_NOT_BOUND"
REGISTER_AMBIGUOUS = "REGISTER_AMBIGUOUS"
REGISTER_MISSING = "REGISTER_MISSING"
REGISTER_HASH_MISMATCH = "REGISTER_HASH_MISMATCH"
REGISTER_SCHEMA = "REGISTER_SCHEMA"
NO_DELIVERABLE_ACTION = "NO_DELIVERABLE_ACTION"
RECLASSIFY_LEGACY_REGISTER = "RECLASSIFY_LEGACY_REGISTER"
RECLASSIFY_NOT_SCOPE_CHANGING = "RECLASSIFY_NOT_SCOPE_CHANGING"
ACTION_NOT_AUTHORIZING = "ACTION_NOT_AUTHORIZING"

AMENDMENT_ID_RE = re.compile(r"^SCA-(?:[A-Z][A-Z0-9]*-)*\d+$")
DELIVERABLE_ID_RE = re.compile(r"^DEL-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)+$")
FOLDER_ID_RE = re.compile(r"^(SCA-(?:[A-Z][A-Z0-9]*-)*\d+)_")
GROUP_FOLDER_RE = re.compile(r"^(SCA-(?:[A-Z][A-Z0-9]*-)*\d+)_GROUP-([123])_")
REFUSING_WORDS_RE = re.compile(r"\b(not accepted|rejected|returned|withdrawn|refused)\b", re.I)
REGISTER_NAME_RE = re.compile(r"^Amendment_Actions[^/]*\.csv$")


class UsageError(Exception):
    """Unusable arguments or an operational failure (exit 2)."""


@dataclass
class ReopenDecision:
    admitted: bool
    code: str
    reason: str
    deliverable_id: str = ""
    amendment_id: str = ""
    scope_change_root: str = ""
    group3_snapshot: str = ""
    group3_decision: str = ""
    group2_manifest: str = ""
    register_path: str = ""
    register_sha256: str = ""
    action_seq: str = ""
    action_type: str = ""
    scope_changing: str | None = None
    notes: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return asdict(self)


class _Refusal(Exception):
    def __init__(self, code: str, reason: str) -> None:
        super().__init__(reason)
        self.code = code
        self.reason = reason


def _git_toplevel(start: Path) -> Path | None:
    probe = start if start.is_dir() else start.parent
    try:
        out = subprocess.run(
            ["git", "-C", str(probe), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if out.returncode != 0 or not out.stdout.strip():
        return None
    return Path(out.stdout.strip())


def _inside(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _real(path: Path) -> Path:
    return Path(os.path.realpath(path))


def _rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _contained(path: Path, root: Path, what: str) -> Path:
    """Return the real path of ``path``; refuse it when it leaves ``root``."""
    real = _real(path)
    if not _inside(real, root):
        raise _Refusal(PATH_ESCAPE, f"{what} {path} resolves outside {root} (path or symlink escape)")
    return real


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _normalize_deliverable(deliverable: str, cwd: Path) -> tuple[str, Path | None]:
    candidate = Path(deliverable)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    if candidate.is_dir():
        name = _real(candidate).name
        del_id = name.split("_", 1)[0]
        if not DELIVERABLE_ID_RE.match(del_id):
            raise UsageError(f"deliverable folder name does not start with a deliverable ID: {name}")
        return del_id, candidate
    del_id = deliverable.strip().split("_", 1)[0]
    if not DELIVERABLE_ID_RE.match(del_id):
        raise UsageError(f"--deliverable is neither a folder nor a deliverable ID: {deliverable!r}")
    return del_id, None


def _find_scope_change_root(start: Path, project_root: Path) -> Path | None:
    current = _real(start)
    while _inside(current, project_root):
        candidate = current / "_ScopeChange"
        if candidate.is_dir():
            return candidate
        if current == project_root:
            break
        current = current.parent
    return None


def _resolve_amendment(
    amendment: str, cwd: Path, project_root: Path
) -> tuple[str, Path | None, Path | None]:
    """Return (amendment_id, scope_change_root or None, pinned group-3 folder or None)."""
    value = amendment.strip()
    if AMENDMENT_ID_RE.match(value):
        return value, None, None
    candidate = Path(value)
    options = [candidate] if candidate.is_absolute() else [cwd / candidate, project_root / candidate]
    target = next((p for p in options if p.exists()), None)
    if target is None:
        raise _Refusal(AMENDMENT_UNRESOLVED, f"--amendment is neither an amendment ID nor an existing path: {amendment!r}")
    real = _contained(target, project_root, "--amendment path")
    if real.is_file():
        if real.name != "DECISION.md":
            raise _Refusal(AMENDMENT_UNRESOLVED, f"--amendment file must be a group-3 DECISION.md: {amendment!r}")
        real = real.parent
    group = GROUP_FOLDER_RE.match(real.name)
    if group and real.parent.name == "checkpoint_snapshots":
        if group.group(2) != "3":
            raise _Refusal(
                GROUP3_NOT_ACCEPTED,
                f"{real.name} is a group-{group.group(2)} decision; only an accepted checkpoint-group-3 decision authorizes reopening",
            )
        return group.group(1), real.parent.parent, real
    folder = FOLDER_ID_RE.match(real.name)
    if folder and real.parent.name == "_ScopeChange":
        return folder.group(1), real.parent, None
    raise _Refusal(
        AMENDMENT_UNRESOLVED,
        f"--amendment path is not an amendment snapshot or group-3 decision folder under _ScopeChange/: {amendment!r}",
    )


def _first_heading(path: Path) -> str:
    with path.open(encoding="utf-8-sig") as handle:
        for line in handle:
            if line.startswith("# "):
                return line[2:].strip()
    return ""


def _group_folders(root: Path, amendment_id: str, group: str) -> list[Path]:
    snapshots = root / "checkpoint_snapshots"
    if not snapshots.is_dir():
        return []
    found = []
    for entry in sorted(snapshots.iterdir()):
        match = GROUP_FOLDER_RE.match(entry.name)
        if match and match.group(1) == amendment_id and match.group(2) == group and entry.is_dir():
            found.append(entry)
    return found


def _accepted_group3(root: Path, amendment_id: str, pinned: Path | None) -> Path:
    folders = [pinned] if pinned is not None else _group_folders(root, amendment_id, "3")
    problems = []
    heading_re = re.compile(
        rf"^{re.escape(amendment_id)}\s+checkpoint group 3\b.*\baccepted\b", re.IGNORECASE
    )
    for folder in folders:
        real = _contained(folder, root, "group-3 decision folder")
        decision = real / "DECISION.md"
        manifest = real / "ACCEPTED_MANIFEST.csv"
        if not decision.is_file() or not manifest.is_file():
            problems.append(f"{folder.name} lacks DECISION.md or ACCEPTED_MANIFEST.csv")
            continue
        _contained(decision, root, "group-3 DECISION.md")
        _contained(manifest, root, "group-3 ACCEPTED_MANIFEST.csv")
        heading = _first_heading(decision)
        if heading_re.match(heading) and not REFUSING_WORDS_RE.search(heading):
            return real
        problems.append(f"{folder.name}/DECISION.md heading does not record group-3 acceptance: {heading!r}")
    if problems:
        detail = "; ".join(problems)
    else:
        earlier = [p.name for g in ("1", "2") for p in _group_folders(root, amendment_id, g)]
        detail = (
            f"no checkpoint_snapshots/{amendment_id}_GROUP-3_* decision snapshot"
            + (f" (only {', '.join(earlier)}; a group-1 or group-2 decision does not authorize reopening)" if earlier else "")
        )
    raise _Refusal(GROUP3_NOT_ACCEPTED, detail)


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [{(k or "").strip(): (v or "").strip() if isinstance(v, str) else "" for k, v in row.items()} for row in reader]
        header = [h.strip() for h in (reader.fieldnames or [])]
    return header, rows


def _manifest_binding(manifest: Path, root: Path, project_root: Path) -> tuple[Path, str] | None:
    header, rows = _read_csv(manifest)
    lookup = {h.lower().replace("-", ""): h for h in header}
    path_col = lookup.get("path")
    sha_col = lookup.get("sha256")
    role_col = lookup.get("role")
    if not path_col or not sha_col:
        raise _Refusal(MANIFEST_SCHEMA, f"{_rel(manifest, project_root)} has no Path and SHA256 columns")
    candidates = [r for r in rows if REGISTER_NAME_RE.match(Path(r.get(path_col, "")).name)]
    if len(candidates) > 1 and role_col:
        named = [r for r in candidates if "action register" in r.get(role_col, "").lower()]
        if len(named) == 1:
            candidates = named
    if not candidates:
        return None
    if len({(r[path_col], r[sha_col].lower()) for r in candidates}) > 1:
        raise _Refusal(
            REGISTER_AMBIGUOUS,
            f"{_rel(manifest, project_root)} binds several Amendment_Actions*.csv files and no single row's Role names the action register",
        )
    raw_path = candidates[0][path_col]
    bound_sha = candidates[0][sha_col].lower()
    if Path(raw_path).is_absolute():
        raise _Refusal(PATH_ESCAPE, f"register path in {_rel(manifest, project_root)} is absolute: {raw_path}")
    # Manifest paths are project-root relative; accept execution-root-parent
    # relative paths too. A missing file resolves to the in-root candidate so
    # the refusal names the missing register rather than an escape.
    options = [project_root / raw_path, root.parent.parent / raw_path]
    inside = [p for p in options if _inside(_real(p), root)]
    target = next((p for p in options if p.exists() or p.is_symlink()), (inside or options)[0])
    real = _real(target)
    if not _inside(real, root):
        raise _Refusal(
            PATH_ESCAPE,
            f"register {raw_path} bound in {_rel(manifest, project_root)} resolves outside the scope-change root (path or symlink escape)",
        )
    return real, bound_sha


def _bound_register(root: Path, amendment_id: str, project_root: Path) -> tuple[Path, str, Path]:
    manifests = []
    for folder in _group_folders(root, amendment_id, "2"):
        manifest = folder / "ACCEPTED_MANIFEST.csv"
        if manifest.is_file():
            manifests.append(_contained(manifest, root, "group-2 ACCEPTED_MANIFEST.csv"))
    if not manifests:
        raise _Refusal(
            GROUP2_MANIFEST_MISSING,
            f"no checkpoint_snapshots/{amendment_id}_GROUP-2_*/ACCEPTED_MANIFEST.csv binds the accepted register",
        )
    bindings = []
    for manifest in manifests:
        binding = _manifest_binding(manifest, root, project_root)
        if binding is not None:
            bindings.append((binding[0], binding[1], manifest))
    if not bindings:
        raise _Refusal(REGISTER_NOT_BOUND, f"no group-2 ACCEPTED_MANIFEST.csv of {amendment_id} binds an Amendment_Actions*.csv register")
    if len({(b[0], b[1]) for b in bindings}) > 1:
        raise _Refusal(REGISTER_AMBIGUOUS, f"group-2 manifests of {amendment_id} bind different registers or hashes")
    return bindings[0]


def _matches_deliverable(entity_id: str, del_id: str) -> bool:
    return entity_id == del_id or entity_id.startswith(del_id + "_")


def _qualifying_row(register: Path, amendment_id: str, del_id: str, project_root: Path) -> tuple[dict, bool]:
    header, rows = _read_csv(register)
    missing = [c for c in ("ActionType", "EntityType", "EntityID") if c not in header]
    if missing:
        raise _Refusal(REGISTER_SCHEMA, f"{_rel(register, project_root)} lacks column(s) {', '.join(missing)}")
    has_scope = "ScopeChanging" in header
    named = [
        r
        for r in rows
        if r.get("EntityType", "").upper() == "DELIVERABLE"
        and _matches_deliverable(r.get("EntityID", ""), del_id)
        and (not r.get("AmendmentID") or r.get("AmendmentID") == amendment_id)
    ]
    if not named:
        raise _Refusal(NO_DELIVERABLE_ACTION, f"no {amendment_id} register row names DELIVERABLE {del_id}")
    for row in named:
        action = row.get("ActionType", "").upper()
        if action == "MODIFY":
            return row, has_scope
        if action == "RECLASSIFY" and has_scope and row.get("ScopeChanging", "").upper() == "YES":
            return row, has_scope
    reclassify = [r for r in named if r.get("ActionType", "").upper() == "RECLASSIFY"]
    seqs = ", ".join(f"{r.get('ActionSeq') or '?'} {r.get('ActionType') or '?'}" for r in named)
    if reclassify and not has_scope:
        raise _Refusal(
            RECLASSIFY_LEGACY_REGISTER,
            f"{del_id} is named only by RECLASSIFY in a register without the ScopeChanging column (legacy); "
            "the human records a scope-changing reopening directly, citing the accepted snapshot",
        )
    if reclassify:
        values = ", ".join(repr(r.get("ScopeChanging", "")) for r in reclassify)
        raise _Refusal(RECLASSIFY_NOT_SCOPE_CHANGING, f"{del_id} RECLASSIFY row(s) record ScopeChanging {values}, not YES")
    raise _Refusal(
        ACTION_NOT_AUTHORIZING,
        f"rows naming {del_id} ({seqs}) are not MODIFY or scope-changing RECLASSIFY",
    )


def check_reopen(
    deliverable: str,
    amendment: str,
    *,
    scope_change_root: str | os.PathLike | None = None,
    project_root: str | os.PathLike | None = None,
    cwd: str | os.PathLike | None = None,
) -> ReopenDecision:
    """Decide whether ``amendment`` authorizes reopening ``deliverable``.

    Raises ``UsageError`` for unusable input; every other outcome is a
    ``ReopenDecision`` whose ``admitted`` is True only when all checks pass.
    """
    base = Path(cwd) if cwd is not None else Path.cwd()
    del_id, del_path = _normalize_deliverable(deliverable, base)
    decision = ReopenDecision(False, "", "", deliverable_id=del_id)

    if project_root is not None:
        proj = Path(project_root)
        if not proj.is_absolute():
            proj = base / proj
    else:
        anchor = del_path or (Path(scope_change_root) if scope_change_root else base)
        if not anchor.is_absolute():
            anchor = base / anchor
        proj = _git_toplevel(anchor)
        if proj is None:
            raise UsageError("cannot resolve the project root (not a git checkout); pass --project-root")
    if not proj.is_dir():
        raise UsageError(f"project root is not a directory: {proj}")
    proj = _real(proj)

    try:
        if del_path is not None:
            del_real = _contained(del_path, proj, "deliverable folder")
        else:
            del_real = None
        amendment_id, derived_root, pinned = _resolve_amendment(amendment, base, proj)
        decision.amendment_id = amendment_id

        root: Path | None = None
        if scope_change_root is not None:
            given = Path(scope_change_root)
            if not given.is_absolute():
                given = base / given
            if not given.is_dir():
                raise _Refusal(SCOPE_CHANGE_ROOT_NOT_FOUND, f"--scope-change-root is not a directory: {scope_change_root}")
            root = _contained(given, proj, "--scope-change-root")
        if derived_root is not None:
            derived_real = _contained(derived_root, proj, "scope-change root")
            if root is not None and root != derived_real:
                raise _Refusal(AMENDMENT_UNRESOLVED, "--amendment path is not under --scope-change-root")
            root = derived_real
        if root is None:
            if del_real is None:
                raise _Refusal(
                    SCOPE_CHANGE_ROOT_NOT_FOUND,
                    "an amendment ID with a deliverable ID needs --scope-change-root or a deliverable folder",
                )
            found = _find_scope_change_root(del_real, proj)
            if found is None:
                raise _Refusal(SCOPE_CHANGE_ROOT_NOT_FOUND, f"no _ScopeChange/ folder above {_rel(del_real, proj)}")
            root = _contained(found, proj, "scope-change root")
        decision.scope_change_root = _rel(root, proj)
        if del_real is not None and not _inside(del_real, root.parent):
            raise _Refusal(
                AMENDMENT_OUTSIDE_DELIVERABLE_ROOT,
                f"{decision.scope_change_root} does not belong to the execution root of {_rel(del_real, proj)}",
            )

        group3 = _accepted_group3(root, amendment_id, pinned)
        decision.group3_snapshot = _rel(group3, proj)
        decision.group3_decision = _rel(group3 / "DECISION.md", proj)

        register, bound_sha, manifest = _bound_register(root, amendment_id, proj)
        decision.group2_manifest = _rel(manifest, proj)
        decision.register_path = _rel(register, proj)
        if not register.is_file():
            raise _Refusal(REGISTER_MISSING, f"bound register {decision.register_path} does not exist")
        actual = _sha256(register)
        decision.register_sha256 = actual
        if actual != bound_sha:
            raise _Refusal(
                REGISTER_HASH_MISMATCH,
                f"{decision.register_path} SHA-256 {actual} differs from {bound_sha} bound in {decision.group2_manifest}",
            )

        row, has_scope = _qualifying_row(register, amendment_id, del_id, proj)
        if not has_scope:
            decision.notes.append("legacy register without ScopeChanging: RECLASSIFY is not admitted by this tool")
        decision.action_seq = row.get("ActionSeq", "")
        decision.action_type = row.get("ActionType", "").upper()
        decision.scope_changing = row.get("ScopeChanging") if has_scope else None
    except _Refusal as refusal:
        decision.code = refusal.code
        decision.reason = refusal.reason
        return decision
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        raise UsageError(f"cannot read amendment records: {exc}") from exc

    decision.admitted = True
    decision.code = ADMITTED
    decision.reason = (
        f"{amendment_id} accepted at group 3 ({decision.group3_snapshot}); register "
        f"{decision.register_path} matches its group-2 hash; ActionSeq {decision.action_seq or '?'} "
        f"{decision.action_type} names {del_id}"
    )
    return decision


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("--deliverable", required=True, help="deliverable ID or deliverable folder")
    parser.add_argument("--amendment", required=True, help="amendment ID (SCA-NNN, SCA-APP-NNN) or snapshot path")
    parser.add_argument("--scope-change-root", help="the _ScopeChange/ folder (default: found above the deliverable folder)")
    parser.add_argument("--project-root", help="containment root (default: git top level)")
    parser.add_argument("--json", action="store_true", help="print the decision as JSON on stdout")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        decision = check_reopen(
            args.deliverable,
            args.amendment,
            scope_change_root=args.scope_change_root,
            project_root=args.project_root,
        )
    except UsageError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(decision.to_json(), indent=2, sort_keys=True))
    elif decision.admitted:
        print(f"ADMIT: {decision.reason}")
    if not decision.admitted:
        print(f"REFUSE {decision.code}: {decision.reason}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
