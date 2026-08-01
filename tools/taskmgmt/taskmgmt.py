#!/usr/bin/env python3
"""taskmgmt v0 — deterministic scan/validate for Task Management registers.

Stage-A step-8 tool (adopted TM PRD §9; D-GOV-32; workplan step 8). Two
subcommands, both deterministic and judgment-free (PRD §9.3: promotion,
prioritization, disposition, closure, and escalation are human acts — this
tool validates form and harvests candidates, never makes the call):

  validate [--register PATH]   Schema and referential conformance of one
                               register CSV (default: the root program
                               register). Exit 0 PASS, 1 BLOCK, 2
                               operational (D-GOV-02 severity semantics).
  scan [--out PATH] [--register PATH]
                               Harvest candidates from the PRD §5.1
                               structured surfaces into a derived,
                               rebuildable candidate inventory (JSON).
                               The output is a gitignored projection
                               (D-GOV-01) and never authority. Exit 0 on
                               a completed scan (candidate count is data,
                               not a verdict), 2 operational.

Scanner precision rules implemented (PRD §9.2): structured surfaces by
filename/schema only — no free-text tree scanning; a declared exclusion
set reported in every output; canonical-vs-copy dedup preferring
`_Coordination/` originals over `_Evaluation/` copies; `TRACKED_OPEN`
presented as open concern, never gating; no silent caps — whatever the
scan skips, it says it skipped.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

DEFAULT_REGISTER = Path("execution/_Coordination/_TaskManagement/REGISTER.csv")
DEFAULT_SCAN_OUT = Path(
    "execution/_Coordination/_TaskManagement/.candidates/scan.json"
)

CANONICAL_COLUMNS = [
    "RegisterSchemaVersion", "ActionItemID", "Title", "Concern", "SourceRef",
    "SourceSha", "CandidateRef", "DomainLenses", "AssociatedWith", "NoticeRef",
    "ScaRef", "Assignment", "Priority", "PriorityBasis", "Status", "Trigger",
    "ElevatedTo", "Disposition", "EvidenceRef", "EvidenceSha", "EvidenceQuote",
    "Opened", "LastReviewed", "Closed", "Notes",
]
VALID_STATUS = ("OPEN", "DEFERRED", "ELEVATED", "CLOSED")
VALID_DISPOSITIONS = (
    "RESOLVED_WITH_CHANGE", "RESOLVED_BY_DECISION", "INFORMATIONAL_NO_ACTION",
    "DUPLICATE", "REJECTED", "SUPERSEDED_BY_SCOPE_CHANGE", "OBE",
)
ID_RE = re.compile(r"^TM-[A-Z0-9]+-\d{3,}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# PRD §9.2 exclusion set — declared in configuration, reported in every output.
EXCLUDED_DIR_PARTS = (
    "dispatch_briefs", "dispatch_outputs", "gate5_coverage",
    "source_review_html", "atom_review_html", "source_section_nodes",
    "_Sources", ".archive", ".git", "node_modules",
)
EXCLUDED_PATH_SUBSTRINGS = (
    "_pdf2md_work", "docs/thesis/", "plans/chirality-task-management/",
)
# tools/** test fixtures are excluded wholesale by excluding tools/ from scan
# roots; the scanner never enumerates tools/.
SCAN_ROOTS = ("execution", "projects", "domains", "_DomainEngines")

# Structured-surface statuses treated as open at source.
OPEN_DECISION_STATUSES = ("AWAITING_RULING", "PROPOSED", "OPEN", "PENDING")
CLOSED_FINDING_STATUSES = ("CLOSED", "RESOLVED", "DONE", "RETIRED")


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(out.stdout.strip())


def excluded(path: Path) -> bool:
    posix = path.as_posix()
    if any(part in EXCLUDED_DIR_PARTS for part in path.parts):
        return True
    return any(sub in posix for sub in EXCLUDED_PATH_SUBSTRINGS)


# ---------------------------------------------------------------- validate

def validate_register(root: Path, register: Path) -> tuple[int, list[str]]:
    """Returns (exit_code, report_lines)."""
    lines: list[str] = []
    reg_path = register if register.is_absolute() else root / register
    if not reg_path.is_file():
        return 2, [f"taskmgmt validate OPERATIONAL (exit 2): no register at "
                   f"{register}"]
    try:
        with open(reg_path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            header = reader.fieldnames or []
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        return 2, [f"taskmgmt validate OPERATIONAL (exit 2): unreadable "
                   f"register: {exc}"]

    failures: list[str] = []
    if header != CANONICAL_COLUMNS:
        missing = [c for c in CANONICAL_COLUMNS if c not in header]
        extra = [c for c in header if c not in CANONICAL_COLUMNS]
        detail = []
        if missing:
            detail.append(f"missing {missing}")
        if extra:
            detail.append(f"unknown {extra}")
        if not detail:
            detail.append("column order differs from the schema-1.0 order")
        if header and header[0] != "RegisterSchemaVersion":
            detail.append("RegisterSchemaVersion is not column 1")
        failures.append("header: " + "; ".join(detail))

    seen_ids: set[str] = set()
    for i, row in enumerate(rows, start=2):  # header is line 1
        rid = (row.get("ActionItemID") or "").strip()
        where = f"line {i} ({rid or 'no id'})"
        if not (row.get("RegisterSchemaVersion") or "").strip():
            failures.append(f"{where}: RegisterSchemaVersion empty")
        if not ID_RE.match(rid):
            failures.append(f"{where}: ActionItemID {rid!r} not TM-<LOOP>-<seq>")
        if rid in seen_ids:
            failures.append(f"{where}: duplicate ActionItemID {rid}")
        seen_ids.add(rid)
        status = (row.get("Status") or "").strip()
        if status not in VALID_STATUS:
            failures.append(f"{where}: Status {status!r} not in {VALID_STATUS}")
        disposition = (row.get("Disposition") or "").strip()
        if status == "CLOSED":
            if disposition not in VALID_DISPOSITIONS:
                failures.append(
                    f"{where}: CLOSED without a valid Disposition "
                    f"(got {disposition!r})")
            if not (row.get("EvidenceRef") or "").strip():
                failures.append(f"{where}: CLOSED without EvidenceRef")
            if not (row.get("EvidenceSha") or "").strip():
                failures.append(f"{where}: CLOSED without EvidenceSha")
            if not (row.get("Closed") or "").strip():
                failures.append(f"{where}: CLOSED without Closed date")
        elif disposition:
            failures.append(
                f"{where}: Disposition {disposition!r} on non-CLOSED row")
        if status == "DEFERRED" and not (row.get("Trigger") or "").strip():
            failures.append(f"{where}: DEFERRED without Trigger")
        if status == "ELEVATED" and not (row.get("ElevatedTo") or "").strip():
            failures.append(f"{where}: ELEVATED without ElevatedTo")
        if not (row.get("SourceRef") or "").strip():
            failures.append(f"{where}: SourceRef empty (K-PROV-1)")
        if not (row.get("SourceSha") or "").strip():
            failures.append(f"{where}: SourceSha empty (K-AUTH-2 posture)")
        for col in ("Opened", "LastReviewed", "Closed"):
            value = (row.get(col) or "").strip()
            if col == "Opened" and not value:
                failures.append(f"{where}: Opened empty")
            if value and not DATE_RE.match(value):
                failures.append(f"{where}: {col} {value!r} not YYYY-MM-DD")

    if failures:
        lines.append(f"taskmgmt validate BLOCK: {register} — "
                     f"{len(failures)} finding(s):")
        lines.extend(f"  - {f}" for f in failures)
        return 1, lines
    lines.append(
        f"taskmgmt validate PASS: {register} — {len(rows)} row(s), schema "
        "columns and referential rules conform. Form only; content judgment "
        "stays human (PRD §9.3).")
    return 0, lines


# -------------------------------------------------------------------- scan

def iter_files(root: Path, pattern: str):
    for scan_root in SCAN_ROOTS:
        base = root / scan_root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob(pattern)):
            if not excluded(path.relative_to(root)):
                yield path


def candidate(source_class: str, path: Path, root: Path, ident: str,
              summary: str) -> dict:
    return {
        "class": source_class,
        "source": path.relative_to(root).as_posix(),
        "id": ident,
        "summary": " ".join(summary.split())[:240],
        "authority": "observed",  # candidates are observations, never authority
    }


def scan_decision_registers(root: Path) -> list[dict]:
    found = []
    for path in iter_files(root, "_REGISTER.md"):
        if "_DECISIONS" not in path.parts:
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            statuses = [c for c in cells if c in OPEN_DECISION_STATUSES]
            if statuses:
                found.append(candidate(
                    "decision-non-ruled", path, root, cells[0],
                    f"{statuses[0]}: {' / '.join(cells[1:2])}"))
    return found


def scan_notice_ledgers(root: Path) -> tuple[list[dict], list[dict]]:
    """Returns (tracked_open, notices_not_in_any_ledger)."""
    tracked, ledgered_names = [], set()
    for path in iter_files(root, "*NOTICE_STATUS*.csv"):
        try:
            rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
        except (OSError, csv.Error):
            continue
        for row in rows:
            notice = (row.get("NoticePath") or "").strip()
            if notice:
                ledgered_names.add(PurePosixPath(notice).name)
            if (row.get("AcknowledgementState") or "").strip() == "TRACKED_OPEN":
                tracked.append(candidate(
                    "notice-tracked-open", path, root, notice,
                    "TRACKED_OPEN in ledger; presented as open concern, "
                    "never gating"))
    unregistered = []
    for path in iter_files(root, "NOTICE_*.md"):
        if "_Coordination" in path.parts and path.name not in ledgered_names:
            unregistered.append(candidate(
                "notice-not-in-ledger", path, root, path.name,
                "notice present on a coordination surface but absent from "
                "every notice ledger"))
    return tracked, unregistered


def scan_findings(root: Path) -> list[dict]:
    found = []
    for path in iter_files(root, "FINDINGS.csv"):
        if "_Evaluation" not in path.parts:
            continue
        try:
            rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
        except (OSError, csv.Error):
            continue
        for row in rows:
            status = (row.get("Status") or row.get("Disposition") or "").strip()
            if status and status.upper() not in CLOSED_FINDING_STATUSES:
                found.append(candidate(
                    "evaluation-finding-open", path, root,
                    (row.get("FindingID") or "row").strip(),
                    f"{status}: {(row.get('Concern') or '')}"))
    return found


def scan_packet_fields(root: Path) -> list[dict]:
    found = []
    for pattern, id_cols in (
        ("Open_Questions.csv", ("OpenQuestionID", "QuestionID")),
        ("Conflicts.csv", ("ConflictID", "ID")),
        ("Amendment_Candidates.csv", ("AmendmentID", "CandidateID", "ID")),
    ):
        for path in iter_files(root, pattern):
            try:
                rows = list(csv.DictReader(open(path, newline="",
                                                encoding="utf-8")))
            except (OSError, csv.Error):
                continue
            for row in rows:
                status = (row.get("Status") or "").strip().upper()
                ruling = (row.get("HumanRuling") or
                          row.get("HumanDisposition") or "").strip().upper()
                # TBD only in disposition-bearing columns (PRD §5.1); Status
                # open values for question schemas.
                is_open = ruling == "TBD" or (
                    pattern == "Open_Questions.csv"
                    and status in ("OPEN", "PARTIAL", ""))
                if is_open:
                    ident = next((row[c] for c in id_cols if row.get(c)), "row")
                    found.append(candidate(
                        "packet-field-open", path, root, ident,
                        (row.get("Question") or row.get("Description") or
                         row.get("Conflict") or "")))
    return found


def scan_tbd_registers(root: Path) -> list[dict]:
    found = []
    for path in iter_files(root, "*TBD_Register*.csv"):
        try:
            rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
        except (OSError, csv.Error):
            continue
        for row in rows:
            found.append(candidate(
                "tbd-register-row", path, root,
                (row.get("TBDID") or "row").strip(),
                (row.get("Question") or "")))
    return found


def scan_handoff_blockers(root: Path) -> list[dict]:
    found = []
    for path in iter_files(root, "HANDOFF_STATE.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            lowered = line.lower()
            if "remaining blockers" in lowered and "none" not in lowered:
                found.append(candidate(
                    "handoff-blocker", path, root, "remaining-blockers",
                    line.strip()))
    return found


def dedup_canonical(cands: list[dict]) -> tuple[list[dict], int]:
    """Canonical-vs-copy: prefer _Coordination/ paths over _Evaluation/ copies
    sharing (source basename, class, id)."""
    by_key: dict[tuple, dict] = {}
    dropped = 0
    for cand in cands:
        key = (PurePosixPath(cand["source"]).name, cand["class"], cand["id"])
        kept = by_key.get(key)
        if kept is None:
            by_key[key] = cand
            continue
        dropped += 1
        if ("/_Coordination/" in "/" + cand["source"]
                and "/_Coordination/" not in "/" + kept["source"]):
            by_key[key] = cand
    return list(by_key.values()), dropped


def load_register_refs(root: Path, register: Path) -> set[str]:
    reg_path = register if register.is_absolute() else root / register
    refs: set[str] = set()
    if not reg_path.is_file():
        return refs
    try:
        for row in csv.DictReader(open(reg_path, newline="", encoding="utf-8")):
            refs.add((row.get("SourceRef") or "").strip())
    except (OSError, csv.Error):
        pass
    return refs


def scan(root: Path, register: Path, out: Path) -> tuple[int, list[str]]:
    tracked, unregistered = scan_notice_ledgers(root)
    classes = {
        "decision-non-ruled": scan_decision_registers(root),
        "notice-tracked-open": tracked,
        "notice-not-in-ledger": unregistered,
        "evaluation-finding-open": scan_findings(root),
        "packet-field-open": scan_packet_fields(root),
        "tbd-register-row": scan_tbd_registers(root),
        "handoff-blocker": scan_handoff_blockers(root),
    }
    all_cands = [c for group in classes.values() for c in group]
    deduped, dropped = dedup_canonical(all_cands)

    register_refs = load_register_refs(root, register)
    for cand in deduped:
        cand["known_to_register"] = any(
            cand["source"] in ref for ref in register_refs)

    payload = {
        "generated_by": "tools/taskmgmt/taskmgmt.py scan (v0)",
        "authority": "derived, rebuildable, gitignored projection (D-GOV-01); "
                     "never citable as authority; candidates are observations "
                     "and create no duty anywhere (K-TM-3/K-TM-4)",
        "scan_roots": list(SCAN_ROOTS),
        "exclusions_declared": {
            "dir_parts": list(EXCLUDED_DIR_PARTS),
            "path_substrings": list(EXCLUDED_PATH_SUBSTRINGS),
            "note": "tools/ is never enumerated; free-text token scanning "
                    "is out of scope for v0 (per-document mode only, "
                    "not implemented)",
        },
        "dedup_dropped_copies": dropped,
        "counts": {name: len(group) for name, group in classes.items()},
        "candidates": sorted(
            deduped, key=lambda c: (c["class"], c["source"], str(c["id"]))),
    }
    out_path = out if out.is_absolute() else root / out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"taskmgmt scan COMPLETE: {len(deduped)} candidate(s) "
        f"({dropped} canonical-copy duplicate(s) folded) -> "
        f"{out_path.relative_to(root).as_posix() if not out.is_absolute() else out_path}",
    ]
    for name, group in classes.items():
        lines.append(f"  {name}: {len(group)}")
    known = sum(1 for c in deduped if c.get("known_to_register"))
    lines.append(f"  known_to_register (SourceRef overlap): {known}")
    lines.append("  exclusions declared in output; no silent caps — classes "
                 "not implemented in v0 (run-record markers, review-report "
                 "sections, per-document token mode) are skipped and named "
                 "here.")
    return 0, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p_val = sub.add_parser("validate", help="validate one register CSV")
    p_val.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    p_scan = sub.add_parser("scan", help="harvest candidates (PRD §5.1)")
    p_scan.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    p_scan.add_argument("--out", type=Path, default=DEFAULT_SCAN_OUT)
    args = parser.parse_args(argv)

    try:
        root = repo_root()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"taskmgmt OPERATIONAL (exit 2): git unavailable: {exc}")
        return 2

    if args.command == "validate":
        code, lines = validate_register(root, args.register)
    else:
        code, lines = scan(root, args.register, args.out)
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
