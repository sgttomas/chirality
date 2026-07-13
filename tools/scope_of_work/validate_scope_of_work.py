#!/usr/bin/env python3
"""Validate candidate ScopeOfWork.md documents and resolve deliverable format."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import SowError, VARIANCE_REF_RE, parse_sow, resolve_format, validate_document


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="ScopeOfWork.md or its deliverable directory")
    parser.add_argument("--pilot-variance", action="store_true")
    parser.add_argument("--variance-ref", default="")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    deliverable = args.target if args.target.is_dir() else args.target.parent
    sow_path = deliverable / "ScopeOfWork.md" if args.target.is_dir() else args.target
    format_state = resolve_format(deliverable, args.pilot_variance, args.variance_ref)
    issues: list[str] = []
    if args.pilot_variance and not VARIANCE_REF_RE.fullmatch(args.variance_ref.strip()):
        issues.append("--variance-ref must match D-GOV-15@<accepted-sha>")
    if format_state in {"INVALID", "AMBIGUOUS"}:
        issues.append(f"format state is {format_state}")
    if sow_path.is_file():
        try:
            doc = parse_sow(sow_path)
            issues.extend(validate_document(doc))
            if format_state == "PILOT_DUAL":
                marker = f"<!-- pilot-variance: {args.variance_ref.strip()} -->"
                if marker not in doc.body:
                    issues.append("candidate pilot-variance marker does not match --variance-ref")
        except (OSError, UnicodeError, SowError) as exc:
            issues.append(str(exc))
    elif format_state not in {"LEGACY_FOUR_DOC"}:
        issues.append(f"missing ScopeOfWork.md: {sow_path}")

    report = {"target": str(args.target), "format": format_state, "valid": not issues, "issues": issues}
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(("PASS" if not issues else "FAIL") + f" format={format_state} target={args.target}")
        for issue in issues:
            print(f"- {issue}")
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
