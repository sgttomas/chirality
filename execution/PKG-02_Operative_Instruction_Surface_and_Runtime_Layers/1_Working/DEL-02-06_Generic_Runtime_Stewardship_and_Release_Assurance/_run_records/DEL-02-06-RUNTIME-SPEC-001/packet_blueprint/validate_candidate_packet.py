#!/usr/bin/env python3
"""Validate a post-S2 DEL-02-06 six-file candidate without mutation."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from io import StringIO
from pathlib import Path


CONTENT_FILES = {
    "ROOT_COMPATIBILITY_POLICY_CANDIDATE.md",
    "DEGRADED_MODE_CONTRACT_CANDIDATE.md",
    "OPEN_ITEMS.csv",
    "OWNER_SELECTION.md",
    "OWNER_GATE.md",
}
MANIFEST = "CANDIDATE_SET_MANIFEST.sha256"
SOW_SHA = "dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146"
RULING_SHA = "9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6"
CURRENT_BASIS_IDENTITIES = {
    "Git HEAD 2b7a7d828e9173836e5b0a71fc015e4f45024215 with exact applied S5/S6 worktree bytes",
    "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    "d64272d9c25b3ee21d622a7dc16a5cc20dea0979252e0b899f189ff95a51f508",
    "a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8",
    "625f5e93c8e657785910e31bfc9e179d4aa83896e5e5f9fe1dca98119a9f23f6",
    "33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de",
    "ee10313f42c99bc9432d3999b148d81ef0d959c58fa8e58d6df3dc40470420e1",
    "05395c308e81d31362dbc87d6d61b7073a3dbffc0b2b3172aba596e7e551f40f",
}
OPEN_HEADER = [
    "PacketRowID",
    "ScopeTBDID",
    "ScopeAlias",
    "Status",
    "Question",
    "CurrentBasisDisposition",
    "OwningLaterGate",
    "SourceRef",
    "SourceSha",
]
MANIFEST_RE = re.compile(r"^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$")
ABSOLUTE_PATH_RE = re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\\\)")
OWNER_TOKEN_RE = re.compile(
    r"^ACCEPT DEL-02-06 INPUT PACKET [0-9a-f]{64} — Ryan Tufts \d{4}-\d{2}-\d{2}$",
    re.MULTILINE,
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def text_checks(name: str, data: bytes, issues: list[str]) -> str:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        issues.append(f"{name}: not UTF-8: {error}")
        return ""
    if b"\r" in data:
        issues.append(f"{name}: CR byte present; LF required")
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        issues.append(f"{name}: require exactly one terminal newline")
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.endswith((" ", "\t")):
            issues.append(f"{name}:{line_number}: trailing whitespace")
    if "{{" in text or "}}" in text:
        issues.append(f"{name}: unresolved template placeholder")
    if ABSOLUTE_PATH_RE.search(text):
        issues.append(f"{name}: machine-absolute path detected")
    return text


def require(text: str, needle: str, name: str, issues: list[str]) -> None:
    if needle not in text:
        issues.append(f"{name}: missing required text: {needle}")


def validate_content(directory: Path, issues: list[str]) -> dict[str, str]:
    texts: dict[str, str] = {}
    hashes: dict[str, str] = {}
    for name in sorted(CONTENT_FILES):
        path = directory / name
        if not path.is_file() or path.is_symlink():
            issues.append(f"{name}: missing regular non-symlink file")
            continue
        data = path.read_bytes()
        texts[name] = text_checks(name, data, issues)
        hashes[name] = sha256(data)

    for name in sorted(CONTENT_FILES - {"OPEN_ITEMS.csv"}):
        text = texts.get(name, "")
        require(text, SOW_SHA, name, issues)
        require(text, "NOT ACCEPTED", name, issues)
        require(text, "FRESH", name, issues)
        for identity in sorted(CURRENT_BASIS_IDENTITIES):
            require(text, identity, name, issues)
    for name in (
        "ROOT_COMPATIBILITY_POLICY_CANDIDATE.md",
        "DEGRADED_MODE_CONTRACT_CANDIDATE.md",
        "OWNER_SELECTION.md",
    ):
        require(texts.get(name, ""), RULING_SHA, name, issues)

    root = texts.get("ROOT_COMPATIBILITY_POLICY_CANDIDATE.md", "")
    for req in range(1, 10):
        require(root, f"REQ-{req:03d}", "ROOT_COMPATIBILITY_POLICY_CANDIDATE.md", issues)
    for phrase in (
        "exactly one",
        "before the daemon exposes admission or",
        "prompt replay",
        "compatibility-epoch effect",
    ):
        require(root, phrase, "ROOT_COMPATIBILITY_POLICY_CANDIDATE.md", issues)

    degraded = texts.get("DEGRADED_MODE_CONTRACT_CANDIDATE.md", "")
    for req in range(17, 27):
        require(degraded, f"REQ-{req:03d}", "DEGRADED_MODE_CONTRACT_CANDIDATE.md", issues)
    for phrase in ("never silently replays", "exactly one terminal", "startup closed"):
        require(degraded, phrase, "DEGRADED_MODE_CONTRACT_CANDIDATE.md", issues)

    selection = texts.get("OWNER_SELECTION.md", "")
    require(selection, "No semantic selection", "OWNER_SELECTION.md", issues)
    gate = texts.get("OWNER_GATE.md", "")
    require(gate, "contains no owner token", "OWNER_GATE.md", issues)
    require(gate, "packet_acceptance/PACKET_OWNER_ACCEPTANCE.md", "OWNER_GATE.md", issues)
    if OWNER_TOKEN_RE.search(gate):
        issues.append("OWNER_GATE.md: embedded owner acceptance token is forbidden")

    open_text = texts.get("OPEN_ITEMS.csv", "")
    if open_text:
        rows = list(csv.reader(StringIO(open_text)))
        if not rows or rows[0] != OPEN_HEADER:
            issues.append("OPEN_ITEMS.csv: exact header mismatch")
        data_rows = rows[1:]
        if len(data_rows) != 16:
            issues.append(f"OPEN_ITEMS.csv: expected 16 rows, found {len(data_rows)}")
        for index, row in enumerate(data_rows, start=1):
            if len(row) != len(OPEN_HEADER):
                issues.append(f"OPEN_ITEMS.csv row {index}: expected {len(OPEN_HEADER)} fields")
                continue
            expected_tbd = f"TBD-{index:03d}"
            expected_alias = f"OD6-OPEN-{index:03d}"
            if row[1] != expected_tbd or row[2] != expected_alias:
                issues.append(f"OPEN_ITEMS.csv row {index}: identity mismatch")
            if row[7] != f"ScopeOfWork.md#{expected_tbd}" or row[8] != SOW_SHA:
                issues.append(f"OPEN_ITEMS.csv row {index}: source binding mismatch")
    return hashes


def validate_manifest(directory: Path, content_hashes: dict[str, str], issues: list[str]) -> str:
    path = directory / MANIFEST
    if not path.is_file() or path.is_symlink():
        issues.append(f"{MANIFEST}: missing regular non-symlink file")
        return ""
    data = path.read_bytes()
    text = text_checks(MANIFEST, data, issues)
    lines = text.splitlines()
    if len(lines) != 5 or lines != sorted(lines):
        issues.append(f"{MANIFEST}: require exactly five sorted lines")
    seen: set[str] = set()
    for line in lines:
        match = MANIFEST_RE.fullmatch(line)
        if match is None:
            issues.append(f"{MANIFEST}: invalid line: {line!r}")
            continue
        digest, name = match.groups()
        seen.add(name)
        if name not in CONTENT_FILES:
            issues.append(f"{MANIFEST}: unexpected filename {name}")
        elif content_hashes.get(name) != digest:
            issues.append(f"{MANIFEST}: digest mismatch for {name}")
    if seen != CONTENT_FILES:
        issues.append(f"{MANIFEST}: membership mismatch")
    return sha256(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_dir", type=Path)
    parser.add_argument("--content-only", action="store_true")
    args = parser.parse_args()
    directory = args.candidate_dir.resolve()
    issues: list[str] = []
    expected = CONTENT_FILES if args.content_only else CONTENT_FILES | {MANIFEST}
    if not directory.is_dir() or directory.is_symlink():
        issues.append("candidate directory is absent or is a symlink")
        actual: set[str] = set()
    else:
        actual = {entry.name for entry in directory.iterdir()}
        if actual != expected:
            issues.append(f"exact membership mismatch: expected={sorted(expected)} actual={sorted(actual)}")
    content_hashes = validate_content(directory, issues) if directory.is_dir() else {}
    manifest_sha = "" if args.content_only else validate_manifest(directory, content_hashes, issues)
    result = {
        "schema": "chirality.del0206-input-packet-validation/v1",
        "valid": not issues,
        "content_only": args.content_only,
        "candidate_dir": str(directory),
        "content_hashes": content_hashes,
        "manifest_sha256": manifest_sha,
        "issues": issues,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
