#!/usr/bin/env python3
"""Validate an external exact-manifest owner acceptance record."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


TOKEN_RE = re.compile(
    r"^ACCEPT DEL-02-06 INPUT PACKET ([0-9a-f]{64}) — Ryan Tufts (\d{4}-\d{2}-\d{2})$",
    re.MULTILINE,
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_dir", type=Path)
    parser.add_argument("acceptance_record", type=Path)
    args = parser.parse_args()
    issues: list[str] = []
    manifest = args.candidate_dir.resolve() / "CANDIDATE_SET_MANIFEST.sha256"
    record = args.acceptance_record.resolve()
    if not manifest.is_file() or manifest.is_symlink():
        issues.append("candidate manifest is absent or not a regular non-symlink file")
        manifest_sha = ""
    else:
        manifest_sha = sha256(manifest.read_bytes())
    try:
        record_bytes = record.read_bytes()
        record_text = record_bytes.decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        issues.append(f"acceptance record unreadable: {error}")
        record_bytes = b""
        record_text = ""
    tokens = TOKEN_RE.findall(record_text)
    if len(tokens) != 1:
        issues.append(f"expected exactly one acceptance token, found {len(tokens)}")
        bound_sha = ""
        ruling_date = ""
    else:
        bound_sha, ruling_date = tokens[0]
        if bound_sha != manifest_sha:
            issues.append("acceptance token does not bind the candidate manifest SHA-256")
    if "| Decision | `ACCEPT` |" not in record_text:
        issues.append("acceptance record does not state Decision ACCEPT")
    if manifest_sha and manifest_sha not in record_text:
        issues.append("acceptance record omits the bound manifest SHA-256")
    result = {
        "schema": "chirality.del0206-input-packet-owner-acceptance/v1",
        "valid": not issues,
        "manifest_sha256": manifest_sha,
        "bound_manifest_sha256": bound_sha,
        "ruling_date": ruling_date,
        "acceptance_record_sha256": sha256(record_bytes),
        "issues": issues,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
