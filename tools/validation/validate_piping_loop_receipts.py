#!/usr/bin/env python3
"""Validate the D-44 / DEC-075 chirality-piping receipt contract.

The tool is read-only. Exit 0 means structural conformance, exit 1 means one
or more contract violations, and exit 2 means an operational/input failure.
Structural conformance is evidence only; it does not authenticate owner
directions or decide whether prose is semantically non-reconstructible.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


RECEIPTS_RELPATH = Path("projects/chirality-piping/loop/LOOP_RECEIPTS.md")
FROZEN_THROUGH = 44
FROZEN_PREFIX_BYTES = 74168
FROZEN_PREFIX_SHA256 = (
    "671a1f722a56d98bbc52bb5a3062d0bf7c25bc37312384fc63526bc43c2ca59f"
)
MARKER = (
    "<!-- receipt-contract-v2 frozen-through=Receipt-44 "
    "prefix-bytes=74168 "
    "prefix-sha256=671a1f722a56d98bbc52bb5a3062d0bf7c25bc37312384fc63526bc43c2ca59f -->"
)

MAX_RECORDS = 12
MAX_BODY_BYTES = 4096

HEADING_RE = re.compile(
    r"^- \*\*(\d{4}-\d{2}-\d{2}) — Receipt ([1-9]\d*)\*\* "
    r"\(([^)\n]+)\)\.$"
)
RECORD_RE = re.compile(r"^  - ([A-Za-z][A-Za-z-]*):(?:\s+(.*))?$")
RECEIPT_ID_RE = re.compile(r"^`Receipt-([1-9]\d*)`$")
SHA_RE = re.compile(r"^`([0-9a-f]{40})`$")
GATE_RE = re.compile(r"^`(STOPPED|EXECUTED|AWAITING_OWNER)` — \S.+$")

ALLOWED_FIELDS = {
    "Receipt-ID",
    "Examined-Through",
    "Parent-Receipt",
    "Owner-Direction",
    "Stale-Map-Delta",
    "Pointers",
    "Checks",
    "Model-Attribution",
    "Gate-Outcome",
}
REQUIRED_FIELDS = {
    "Receipt-ID",
    "Examined-Through",
    "Parent-Receipt",
    "Gate-Outcome",
}
OWNER_TRANSCRIPTION_LABEL = "CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING"
LIFECYCLE_TOKENS_RE = re.compile(
    r"\b(?:IN_PROGRESS|CHECKING|ISSUED|AWAITING_RULING|NOT_PREPARED|RULED)\b"
)
COUNT_PATTERNS = (
    re.compile(r"\b\d+\s*/\s*\d+\b"),
    re.compile(
        r"\b\d+\s+(?:passed|failed|skipped|tests?|cases?|rows?|claims?)\b",
        re.IGNORECASE,
    ),
)


@dataclass(frozen=True)
class ReceiptIssue:
    code: str
    message: str
    line: int | None = None


@dataclass(frozen=True)
class ParsedReceipt:
    heading_id: int
    heading_line: int
    records: dict[str, list[tuple[str, int]]]
    body_bytes: int


def _issue(code: str, message: str, line: int | None = None) -> ReceiptIssue:
    return ReceiptIssue(code=code, message=message, line=line)


def _git_check(
    repo_root: Path,
    sha: str,
    validation_commit: str,
) -> tuple[str | None, str | None]:
    exists = subprocess.run(
        ["git", "-C", str(repo_root), "cat-file", "-e", f"{sha}^{{commit}}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if exists.returncode != 0:
        return "COMMIT_NOT_FOUND", f"Examined-Through commit does not resolve: {sha}"

    ancestor = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "merge-base",
            "--is-ancestor",
            sha,
            validation_commit,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if ancestor.returncode == 1:
        return (
            "COMMIT_NOT_ANCESTOR",
            f"Examined-Through {sha} is not an ancestor of {validation_commit}",
        )
    if ancestor.returncode != 0:
        detail = ancestor.stderr.strip() or "git merge-base failed"
        return "GIT_CHECK_FAILED", detail
    return None, None


def _parse_records(
    body_lines: list[str],
    first_body_line: int,
) -> tuple[dict[str, list[tuple[str, int]]], list[ReceiptIssue]]:
    records: dict[str, list[tuple[str, int]]] = {}
    issues: list[ReceiptIssue] = []
    current_field: str | None = None
    current_parts: list[str] = []
    current_line: int | None = None

    def finish_record() -> None:
        nonlocal current_field, current_parts, current_line
        if current_field is None or current_line is None:
            return
        value = " ".join(part for part in current_parts if part).strip()
        records.setdefault(current_field, []).append((value, current_line))
        current_field = None
        current_parts = []
        current_line = None

    for offset, line in enumerate(body_lines):
        line_no = first_body_line + offset
        if not line.strip():
            continue
        stripped = line.lstrip()
        if stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("```"):
            issues.append(_issue(
                "PROHIBITED_STRUCTURE",
                "Versioned receipts may not contain headings, tables, or code fences",
                line_no,
            ))
            continue
        if line.startswith("    -"):
            issues.append(_issue(
                "NESTED_RECORD",
                "Nested bullets are not allowed in a versioned receipt",
                line_no,
            ))
            continue

        match = RECORD_RE.match(line)
        if match:
            finish_record()
            current_field = match.group(1)
            current_parts = [match.group(2) or ""]
            current_line = line_no
            continue

        if line.startswith("    ") and current_field is not None:
            current_parts.append(line.strip())
            continue

        issues.append(_issue(
            "INVALID_RECORD_LINE",
            "Receipt content must be a top-level record or four-space continuation",
            line_no,
        ))

    finish_record()
    return records, issues


def _parse_versioned_receipts(
    text: str,
    first_line: int,
) -> tuple[list[ParsedReceipt], list[ReceiptIssue]]:
    lines = text.splitlines()
    issues: list[ReceiptIssue] = []
    headings: list[tuple[int, re.Match[str]]] = []

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, match))

    if not headings:
        return [], [_issue(
            "NO_VERSIONED_RECEIPT",
            "The v2 contract marker is not followed by a versioned receipt",
            first_line,
        )]

    if any(line.strip() for line in lines[: headings[0][0]]):
        issues.append(_issue(
            "CONTENT_BEFORE_FIRST_RECEIPT",
            "Nonblank content appears between the contract marker and first receipt",
            first_line,
        ))

    parsed: list[ParsedReceipt] = []
    for position, (start, match) in enumerate(headings):
        end = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
        heading_line = first_line + start
        try:
            date.fromisoformat(match.group(1))
        except ValueError:
            issues.append(_issue(
                "INVALID_RECEIPT_DATE",
                f"Invalid ISO receipt date: {match.group(1)}",
                heading_line,
            ))

        body_lines = lines[start + 1 : end]
        body_bytes = len("\n".join(body_lines).strip("\n").encode("utf-8"))
        records, record_issues = _parse_records(body_lines, heading_line + 1)
        issues.extend(record_issues)
        parsed.append(ParsedReceipt(
            heading_id=int(match.group(2)),
            heading_line=heading_line,
            records=records,
            body_bytes=body_bytes,
        ))
    return parsed, issues


def validate_receipts(
    receipts_path: Path,
    repo_root: Path,
    validation_commit: str = "HEAD",
) -> list[ReceiptIssue]:
    raw = receipts_path.read_bytes()
    issues: list[ReceiptIssue] = []

    marker_bytes = MARKER.encode("utf-8")
    marker_positions = [
        match.start() for match in re.finditer(re.escape(marker_bytes), raw)
    ]
    if len(marker_positions) != 1:
        return [_issue(
            "CONTRACT_MARKER_COUNT",
            f"Expected exactly one D-44 contract marker; found {len(marker_positions)}",
        )]

    marker_start = marker_positions[0]
    prefix = raw[:marker_start]
    marker_line = prefix.count(b"\n") + 1
    if len(prefix) != FROZEN_PREFIX_BYTES:
        issues.append(_issue(
            "FROZEN_PREFIX_LENGTH",
            f"Frozen prefix is {len(prefix)} bytes; expected {FROZEN_PREFIX_BYTES}",
            marker_line,
        ))
    digest = hashlib.sha256(prefix).hexdigest()
    if digest != FROZEN_PREFIX_SHA256:
        issues.append(_issue(
            "FROZEN_PREFIX_HASH",
            f"Frozen prefix SHA-256 is {digest}; expected {FROZEN_PREFIX_SHA256}",
            marker_line,
        ))

    marker_end = raw.find(b"\n", marker_start)
    if marker_end == -1:
        return issues + [_issue(
            "MARKER_NOT_TERMINATED",
            "Contract marker must end with a newline",
            marker_line,
        )]
    actual_marker = raw[marker_start:marker_end].decode("utf-8", errors="replace")
    if actual_marker != MARKER:
        issues.append(_issue(
            "CONTRACT_MARKER_MISMATCH",
            "Contract marker fields do not match the ruled frozen-prefix constants",
            marker_line,
        ))

    try:
        versioned_text = raw[marker_end + 1 :].decode("utf-8")
    except UnicodeDecodeError as exc:
        return issues + [_issue(
            "INVALID_UTF8",
            f"Versioned receipt text is not UTF-8: {exc}",
            marker_line + 1,
        )]

    receipts, parse_issues = _parse_versioned_receipts(
        versioned_text,
        marker_line + 1,
    )
    issues.extend(parse_issues)

    seen_ids = set(range(FROZEN_THROUGH + 1))
    previous_heading_id = FROZEN_THROUGH
    for receipt in receipts:
        records = receipt.records
        record_count = sum(len(values) for values in records.values())
        if record_count > MAX_RECORDS:
            issues.append(_issue(
                "RECEIPT_RECORD_LIMIT",
                f"Receipt-{receipt.heading_id} has {record_count} records; maximum is {MAX_RECORDS}",
                receipt.heading_line,
            ))
        if receipt.body_bytes > MAX_BODY_BYTES:
            issues.append(_issue(
                "RECEIPT_BYTE_LIMIT",
                f"Receipt-{receipt.heading_id} body is {receipt.body_bytes} bytes; maximum is {MAX_BODY_BYTES}",
                receipt.heading_line,
            ))
        if receipt.heading_id <= previous_heading_id:
            issues.append(_issue(
                "RECEIPT_ORDER",
                "Versioned receipt heading IDs must increase in physical append order",
                receipt.heading_line,
            ))
        previous_heading_id = receipt.heading_id

        for field in records:
            if field not in ALLOWED_FIELDS:
                line = records[field][0][1]
                issues.append(_issue(
                    "UNKNOWN_RECORD_FIELD",
                    f"Field is not admitted by the D-44 contract: {field}",
                    line,
                ))
        for field in REQUIRED_FIELDS:
            count = len(records.get(field, []))
            if count != 1:
                issues.append(_issue(
                    "REQUIRED_FIELD_COUNT",
                    f"Receipt-{receipt.heading_id} requires exactly one {field}; found {count}",
                    receipt.heading_line,
                ))
        for field, values in records.items():
            if len(values) > 1:
                issues.append(_issue(
                    "DUPLICATE_RECORD_FIELD",
                    f"Receipt-{receipt.heading_id} repeats {field}",
                    values[1][1],
                ))

        receipt_id_values = records.get("Receipt-ID", [])
        if len(receipt_id_values) == 1:
            value, line = receipt_id_values[0]
            match = RECEIPT_ID_RE.match(value)
            if not match:
                issues.append(_issue(
                    "INVALID_RECEIPT_ID",
                    "Receipt-ID must be exactly `Receipt-<positive decimal integer>`",
                    line,
                ))
            else:
                record_id = int(match.group(1))
                if record_id != receipt.heading_id:
                    issues.append(_issue(
                        "RECEIPT_ID_MISMATCH",
                        f"Heading Receipt-{receipt.heading_id} conflicts with Receipt-ID {value}",
                        line,
                    ))
                if record_id in seen_ids:
                    issues.append(_issue(
                        "DUPLICATE_RECEIPT_ID",
                        f"Receipt identity already exists: {value}",
                        line,
                    ))

        parent_values = records.get("Parent-Receipt", [])
        if len(parent_values) == 1:
            value, line = parent_values[0]
            match = RECEIPT_ID_RE.match(value)
            if not match:
                issues.append(_issue(
                    "INVALID_PARENT_RECEIPT",
                    "Parent-Receipt must be exactly `Receipt-<positive decimal integer>`",
                    line,
                ))
            elif int(match.group(1)) not in seen_ids:
                issues.append(_issue(
                    "PARENT_RECEIPT_NOT_FOUND",
                    f"Parent receipt is not an earlier accepted ledger entry: {value}",
                    line,
                ))

        examined_values = records.get("Examined-Through", [])
        if len(examined_values) == 1:
            value, line = examined_values[0]
            match = SHA_RE.match(value)
            if not match:
                issues.append(_issue(
                    "INVALID_EXAMINED_THROUGH",
                    "Examined-Through must be one full lowercase 40-character Git SHA in backticks",
                    line,
                ))
            else:
                code, message = _git_check(repo_root, match.group(1), validation_commit)
                if code and message:
                    issues.append(_issue(code, message, line))

        gate_values = records.get("Gate-Outcome", [])
        if len(gate_values) == 1:
            value, line = gate_values[0]
            if not GATE_RE.match(value):
                issues.append(_issue(
                    "INVALID_GATE_OUTCOME",
                    "Gate-Outcome must use `STOPPED`, `EXECUTED`, or `AWAITING_OWNER` plus an em-dash reason",
                    line,
                ))

        owner_values = records.get("Owner-Direction", [])
        if len(owner_values) == 1:
            value, line = owner_values[0]
            if OWNER_TRANSCRIPTION_LABEL not in value:
                issues.append(_issue(
                    "OWNER_DIRECTION_STATUS",
                    f"Owner-Direction must include {OWNER_TRANSCRIPTION_LABEL!r}",
                    line,
                ))

        for field, values in records.items():
            for value, line in values:
                if field != "Owner-Direction":
                    for pattern in COUNT_PATTERNS:
                        if pattern.search(value):
                            issues.append(_issue(
                                "DUPLICATED_MEASUREMENT",
                                f"Exact count/measurement is not admissible in {field}; point to its owning artifact",
                                line,
                            ))
                            break
                if (
                    field not in {"Gate-Outcome", "Stale-Map-Delta", "Owner-Direction"}
                    and LIFECYCLE_TOKENS_RE.search(value)
                ):
                    issues.append(_issue(
                        "STATUS_OUTSIDE_ALLOWED_RECORD",
                        f"Governed status vocabulary is not admissible in {field}",
                        line,
                    ))

        seen_ids.add(receipt.heading_id)

    return issues


def _resolve_under_repo(repo_root: Path, candidate: Path) -> Path:
    root = repo_root.resolve()
    path = candidate if candidate.is_absolute() else root / candidate
    resolved = path.resolve()
    if resolved != root and root not in resolved.parents:
        raise ValueError(f"receipt path resolves outside repo root: {resolved}")
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--receipts", type=Path, default=RECEIPTS_RELPATH)
    parser.add_argument("--validation-commit", default="HEAD")
    args = parser.parse_args(argv)

    try:
        repo_root = args.repo_root.resolve()
        receipts_path = _resolve_under_repo(repo_root, args.receipts)
        if not receipts_path.is_file():
            raise ValueError(f"receipt file does not exist: {receipts_path}")
        issues = validate_receipts(
            receipts_path=receipts_path,
            repo_root=repo_root,
            validation_commit=args.validation_commit,
        )
    except (OSError, ValueError) as exc:
        print(f"OPERATIONAL_ERROR: {exc}", file=sys.stderr)
        return 2

    if issues:
        for issue in issues:
            location = f":{issue.line}" if issue.line is not None else ""
            print(f"INVALID {issue.code} {receipts_path}{location}: {issue.message}")
        return 1

    print(
        f"VALID {receipts_path}: frozen through Receipt-{FROZEN_THROUGH}; "
        "versioned receipt contract satisfied"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
