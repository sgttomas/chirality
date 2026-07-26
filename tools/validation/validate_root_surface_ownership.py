#!/usr/bin/env python3
"""G2 — static root surface-ownership register (D-GOV-21 §5.3, mechanism M1).

Deterministic guard shipped by the D-GOV-21 guard-capability tranche (packet
§6 step 6) and wired into governance-harness CI. It checks the static register
that maps root packages and deliverables to declared write targets finer than
the checkout (M1). The register itself is instantiated later, by root Project
Setup (packet §6 step 8); this tranche ships capability only.

Design of record (state surface, schema, semantics)
---------------------------------------------------
State surface: `{REPO_ROOT}/execution/_harness/surface_ownership.yaml`,
co-located with G0's `root_guards.yaml` and G1's `adapter.yaml`.
Schema id: `root-surface-ownership/v1`. All paths are repo-root-relative
POSIX paths or globs; absolute paths and `..` are rejected. Shape::

    schema: root-surface-ownership/v1
    decomposition: TBD          # or a repo-relative path to the accepted
                                # root decomposition once one exists
    entries:
      - id: PKG-01_Example      # PKG-* or DEL-* identifier
        kind: package           # package | deliverable
        decomposition_ref: TBD  # or the identifier carried by the accepted
                                # decomposition surface
        write_targets:
          - execution/PKG-01_Example/**
        instruction_surface: false   # true iff a write target intersects the
                                     # instruction surface (M2 applies)
        serialization: null          # or free text naming the accepted
                                     # predecessor / declared integration owner

Static facts only; **no concurrency claims**. Overlapping write targets
between entries are reported as INFO and never BLOCK here — whether two nodes
are concurrently active, and whether an overlap is serialized, is G3's
question against an accepted work graph, not the register's.

Behavior (severity semantics per D-GOV-02)
------------------------------------------
- No `PKG-*`/`DEL-*` under root `execution/` and no register: PASS idle
  (exit 0) — the lawful pre-instantiation condition.
- `PKG-*`/`DEL-*` structure exists and the register is absent: BLOCK (exit 1).
- Register present: BLOCK (exit 1) on any of — malformed/unknown schema;
  malformed entries; absolute or parent-escaping write targets; an entry that
  does not declare its own package/deliverable tree (undeclared write target);
  a materialized `execution/PKG-*` or `execution/DEL-*` child with no register
  entry (unregistered materialized package); an instruction-surface-intersecting
  write target not marked `instruction_surface: true`; or a
  register/decomposition mismatch. Otherwise PASS.
- PyYAML unimportable while the register exists: operational error (exit 2).

Register/decomposition mismatch is evaluated **only against what is declared**
— never inferred. While `decomposition: TBD` (no accepted root decomposition
exists yet) entries may carry `decomposition_ref: TBD`. Once `decomposition`
names a path, that path must exist, every entry must carry a non-TBD
`decomposition_ref`, and each such reference must appear literally in the
declared decomposition surface. Deeper structural cross-checking waits on an
accepted decomposition format and is a recorded open item, not a silent claim.

Observation boundary
--------------------
The register's recorded fields; the names of direct `PKG-*`/`DEL-*` children
of root `execution/`; the existence of the declared decomposition path and the
literal presence of declared reference strings within it. No package contents,
no other working root, no runtime state. This guard holds no authority and
confers none (K-AUTH-1).

Registration entry it will assert in `execution/_harness/root_guards.yaml`
(written by root Project Setup, never by this tranche)::

    guards:
      G2:
        registered: true
        status: passing
        validator: tools/validation/validate_root_surface_ownership.py
        tests: tools/validation/test_validate_root_surface_ownership.py
        state_surface: execution/_harness/surface_ownership.yaml
        schema: root-surface-ownership/v1
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

REGISTER_RELPATH = Path("execution/_harness/surface_ownership.yaml")
REGISTER_SCHEMA = "root-surface-ownership/v1"

VALID_KINDS = ("package", "deliverable")
TBD = "TBD"

# The shared instruction surface, per the `docs/SPEC.md` §0.2.1 enumeration as
# amended by D-GOV-26: `AGENTS.md`, `CLAUDE.md`, `agents/`, `skills/`, `tools/`,
# root `docs/`, `init/`, `.github/workflows/`. `CLAUDE.md` (the session-init
# instruction pointer importing `AGENTS.md`) and `.github/workflows/` (the CI
# workflow definitions that gate merges) were ratified into the enumeration by
# D-GOV-26 item 2; `.github/workflows/` had previously been guarded on the Lane B
# characterization in
# `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`
# ("G1-G4 touch tools/, .github/workflows/, and possibly root docs/ - the
# protected instruction surface"). Additions beyond these require a named basis.
INSTRUCTION_SURFACE_FILES = ("AGENTS.md", "CLAUDE.md")
INSTRUCTION_SURFACE_DIRS = (
    "agents/",
    "skills/",
    "tools/",
    "docs/",
    "init/",
    ".github/workflows/",
)

ID_RE = re.compile(r"^(PKG|DEL)-[A-Za-z0-9._-]+$")


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(out.stdout.strip())


def materialized_children(root: Path) -> list[str]:
    execution = root / "execution"
    if not execution.is_dir():
        return []
    return sorted(
        child.name
        for child in execution.iterdir()
        if child.is_dir()
        and (child.name.startswith("PKG-") or child.name.startswith("DEL-"))
    )


def is_repo_relative(value: str) -> bool:
    if not value or value.startswith("/") or value.startswith("~"):
        return False
    if re.match(r"^[A-Za-z]:[\\/]", value):
        return False
    return ".." not in PurePosixPath(value).parts


def normalize_target(target: str) -> str:
    """Strip leading `./` segments only — never a leading dot of `.github/`."""
    normalized = target.strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def intersects_instruction_surface(target: str) -> bool:
    """True if a declared write target (path or glob) touches the instruction surface."""
    normalized = normalize_target(target)
    if normalized in ("*", "**", "**/*"):
        # A repo-wide glob reaches every instruction surface.
        return True
    if normalized in INSTRUCTION_SURFACE_FILES:
        return True
    return any(normalized.startswith(prefix) for prefix in INSTRUCTION_SURFACE_DIRS)


def covers_own_tree(entry_id: str, write_targets: list[str]) -> bool:
    """True if some declared target covers `execution/<id>/`, the entry's own tree."""
    own = f"execution/{entry_id}"
    for target in write_targets:
        normalized = normalize_target(target)
        base = normalized.split("*", 1)[0].rstrip("/")
        if normalized == own or base == own or normalized.startswith(own + "/"):
            return True
    return False


def check(root: Path) -> tuple[int, list[str]]:
    """Returns (exit_code, report_lines). 0 PASS, 1 BLOCK, 2 operational."""
    lines: list[str] = []
    path = root / REGISTER_RELPATH
    children = materialized_children(root)

    if not path.is_file():
        if children:
            lines.append(
                f"G2 BLOCK: surface-ownership register {REGISTER_RELPATH.as_posix()} "
                "is absent while PKG-*/DEL-* structure exists under root execution/ "
                "(" + ", ".join(children) + "); every root package and deliverable "
                "must declare write targets finer than the checkout (D-GOV-21 M1)."
            )
            return 1, lines
        lines.append(
            f"G2 PASS: no PKG-*/DEL-* under root execution/ and no register at "
            f"{REGISTER_RELPATH.as_posix()}; guard idle (pre-instantiation "
            "condition — Project Setup instantiates the register)."
        )
        return 0, lines

    try:
        import yaml  # type: ignore
    except ImportError:
        lines.append(
            "G2 OPERATIONAL (exit 2): PyYAML is not importable, so the present "
            f"register {REGISTER_RELPATH.as_posix()} cannot be observed; this guard "
            "asserts nothing."
        )
        return 2, lines

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - any parse failure is a malformed surface.
        lines.append(
            f"G2 BLOCK: register {REGISTER_RELPATH.as_posix()} is unparseable: {exc}"
        )
        return 1, lines

    if not isinstance(data, dict):
        lines.append(
            f"G2 BLOCK: register {REGISTER_RELPATH.as_posix()} top level is not a mapping."
        )
        return 1, lines

    failures: list[str] = []
    notes: list[str] = []

    if data.get("schema") != REGISTER_SCHEMA:
        failures.append(
            f"schema is {data.get('schema')!r}; this guard understands "
            f"{REGISTER_SCHEMA!r}"
        )

    decomposition = data.get("decomposition", TBD)
    decomposition_text: str | None = None
    if decomposition != TBD:
        if not isinstance(decomposition, str) or not is_repo_relative(decomposition):
            failures.append(
                f"decomposition is not 'TBD' or a repo-relative path: {decomposition!r}"
            )
            decomposition = TBD
        elif not (root / decomposition).exists():
            failures.append(
                f"decomposition points at {decomposition!r}, which does not exist"
            )
            decomposition = TBD
        else:
            target = root / decomposition
            if target.is_file():
                try:
                    decomposition_text = target.read_text(
                        encoding="utf-8", errors="replace"
                    )
                except OSError as exc:
                    failures.append(f"decomposition {decomposition!r} is unreadable: {exc}")

    entries = data.get("entries")
    if not isinstance(entries, list):
        failures.append("entries must be a list (may be empty)")
        entries = []

    seen_ids: set[str] = set()
    registered_ids: set[str] = set()
    target_owners: dict[str, list[str]] = {}

    for index, entry in enumerate(entries):
        label = f"entries[{index}]"
        if not isinstance(entry, dict):
            failures.append(f"{label}: not a mapping")
            continue
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not ID_RE.match(entry_id):
            failures.append(f"{label}: id {entry_id!r} is not a PKG-*/DEL-* identifier")
            entry_id = f"<{label}>"
        else:
            label = f"entry {entry_id}"
            if entry_id in seen_ids:
                failures.append(f"{label}: duplicate register entry")
            seen_ids.add(entry_id)
            registered_ids.add(entry_id)

        kind = entry.get("kind")
        if kind not in VALID_KINDS:
            failures.append(f"{label}: kind {kind!r} not in {list(VALID_KINDS)}")

        write_targets = entry.get("write_targets")
        if (
            not isinstance(write_targets, list)
            or not write_targets
            or not all(isinstance(t, str) and t for t in write_targets)
        ):
            failures.append(f"{label}: write_targets must be a non-empty list of strings")
            write_targets = []

        bad_targets = [t for t in write_targets if not is_repo_relative(t)]
        for target in bad_targets:
            failures.append(
                f"{label}: write target {target!r} is not a repo-relative POSIX path"
            )
        clean_targets = [t for t in write_targets if t not in bad_targets]

        if clean_targets and isinstance(entry.get("id"), str) and ID_RE.match(str(entry.get("id"))):
            if not covers_own_tree(str(entry["id"]), clean_targets):
                failures.append(
                    f"{label}: undeclared write target — no declared target covers "
                    f"the entry's own tree execution/{entry['id']}/"
                )

        marked = entry.get("instruction_surface", False)
        if not isinstance(marked, bool):
            failures.append(f"{label}: instruction_surface must be a boolean")
            marked = bool(marked)
        touching = [t for t in clean_targets if intersects_instruction_surface(t)]
        if touching and not marked:
            failures.append(
                f"{label}: write target(s) {touching} intersect the instruction "
                "surface but instruction_surface is not true (D-GOV-21 M2)"
            )
        if marked and not touching:
            notes.append(
                f"{label}: instruction_surface is true though no declared target "
                "intersects the instruction surface (over-declaration; non-blocking)"
            )

        ref = entry.get("decomposition_ref", TBD)
        if not isinstance(ref, str) or not ref:
            failures.append(f"{label}: decomposition_ref must be a string or 'TBD'")
        elif decomposition == TBD:
            if ref != TBD:
                notes.append(
                    f"{label}: decomposition_ref {ref!r} declared while the register "
                    "declares no decomposition (non-blocking; unverifiable)"
                )
        else:
            if ref == TBD:
                failures.append(
                    f"{label}: register/decomposition mismatch — decomposition "
                    f"{decomposition!r} is declared but decomposition_ref is 'TBD'"
                )
            elif decomposition_text is not None and ref not in decomposition_text:
                failures.append(
                    f"{label}: register/decomposition mismatch — decomposition_ref "
                    f"{ref!r} does not appear in {decomposition!r}"
                )

        for target in clean_targets:
            target_owners.setdefault(target, []).append(str(entry.get("id", label)))

    unregistered = [child for child in children if child not in registered_ids]
    for child in unregistered:
        failures.append(
            f"unregistered materialized package: execution/{child} exists with no "
            "register entry"
        )

    for target, owners in sorted(target_owners.items()):
        if len(owners) > 1:
            notes.append(
                f"identical write target {target!r} declared by {sorted(owners)} — "
                "recorded as a static fact only; this guard makes no concurrency "
                "claim (serialization is G3's question)"
            )

    if failures:
        lines.append(
            f"G2 BLOCK: surface-ownership register {REGISTER_RELPATH.as_posix()} is invalid:"
        )
        lines.extend(f"  - {failure}" for failure in failures)
        lines.extend(f"  INFO: {note}" for note in notes)
        return 1, lines

    lines.append(
        f"G2 PASS: surface-ownership register {REGISTER_RELPATH.as_posix()} is "
        f"schema-valid ({REGISTER_SCHEMA}); {len(registered_ids)} entr(ies) declare "
        f"write targets; {len(children)} materialized PKG-*/DEL-* child(ren) all "
        f"registered; decomposition={decomposition!r}."
    )
    lines.extend(f"  INFO: {note}" for note in notes)
    return 0, lines


def main() -> int:
    root = repo_root()
    code, lines = check(root)
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
