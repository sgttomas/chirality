#!/usr/bin/env python3
"""Create a lossless candidate ScopeOfWork.md from one legacy four-document kit."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from common import (
    LEGACY_FILES,
    SCHEMA,
    SowError,
    VARIANCE_REF_RE,
    demote_headings,
    load_catalog,
    parse_sow,
    read_lifecycle_state,
    sha256_file,
    split_source_sections,
    validate_document,
)

SECTION_CONFIG = (
    ("Datasheet.md", "Deliverable Definition — Ontology", "CLM"),
    ("Specification.md", "Completion and Reliance Basis — Epistemology", "CLM"),
    ("Procedure.md", "Production and Verification Method — Praxeology", "CLM"),
    ("Guidance.md", "Governing Values and Decisions — Axiology", "CLM"),
)


def inline_list(values: list[str]) -> str:
    return "[" + ", ".join(values) + "]"


def convert(args: argparse.Namespace) -> str:
    deliverable = args.deliverable.resolve()
    missing = [name for name in LEGACY_FILES if not (deliverable / name).is_file()]
    if missing:
        raise SowError("missing legacy source documents: " + ", ".join(missing))
    if not args.pilot_variance or not VARIANCE_REF_RE.fullmatch(args.variance_ref.strip()):
        raise SowError(
            "candidate dual-format conversion requires --pilot-variance and "
            "--variance-ref D-GOV-15@<accepted-sha>"
        )
    state = read_lifecycle_state(deliverable)
    if state == "ISSUED":
        raise SowError("Stage-1 converter refuses ISSUED deliverables")
    if state != "IN_PROGRESS":
        raise SowError(f"Stage-1 converter requires IN_PROGRESS, found {state or 'UNKNOWN'}")
    target = deliverable / "ScopeOfWork.md"
    if target.exists() and not args.force:
        raise SowError(f"target exists; refuse overwrite without --force: {target}")
    status = deliverable / "_STATUS.md"
    status_before = sha256_file(status)

    catalog = load_catalog()
    counters = {prefix: 1 for prefix in catalog.definitions}
    source_sections: dict[str, list[str]] = {}
    defined: dict[str, list[str]] = {}
    for filename, heading, prefix in SECTION_CONFIG:
        path = deliverable / filename
        source_sha = sha256_file(path)
        rendered: list[str] = []
        defined[filename] = []
        for line_start, line_end, source_heading, source_text in split_source_sections(
            path.read_text(encoding="utf-8")
        ):
            local_id = f"{prefix}-{counters[prefix]:03d}"
            counters[prefix] += 1
            defined[filename].append(local_id)
            marker = {
                "disposition": "PRESERVED",
                "file": filename,
                "line_end": line_end,
                "line_start": line_start,
                "source_sha256": source_sha,
                "target_id": local_id,
            }
            rendered.extend(
                [
                    f"### {local_id} — {source_heading}",
                    "",
                    "<!-- sow-source-begin " + json.dumps(marker, sort_keys=True, separators=(",", ":")) + " -->",
                    demote_headings(source_text),
                    "<!-- sow-source-end -->",
                    "",
                ]
            )
        source_sections[heading] = rendered

    out_id, ac_id, ver_id = "OUT-001", "AC-001", "VER-001"
    project_refs = args.project_scope_ref
    package_refs = args.package_objective_ref
    matrix_objectives = " ".join(project_refs + package_refs)
    lines = [
        "---",
        f"schema: {SCHEMA}",
        f"deliverable_id: {args.deliverable_id}",
        f"package_id: {args.package_id}",
        f"decomposition_basis: {args.decomposition_basis}",
        f"project_scope_refs: {inline_list(project_refs)}",
        f"package_objective_refs: {inline_list(package_refs)}",
        "---",
        "",
        f"# Scope of Work — {args.deliverable_id}",
        "",
        "## Purpose and Objective Traceability",
        "",
        f"This candidate defines `{args.deliverable_id}` in service of project scope {inline_list(project_refs)} and package objectives {inline_list(package_refs)}.",
        "",
        f"- **{out_id}** — {args.output_description}",
        "",
    ]
    for _, heading, _ in SECTION_CONFIG:
        lines.extend([f"## {heading}", ""])
        lines.extend(source_sections[heading])
        if heading == "Completion and Reliance Basis — Epistemology":
            lines.extend([f"- **{ac_id}** — {args.acceptance_criterion}", ""])
        if heading == "Production and Verification Method — Praxeology":
            lines.extend([f"- **{ver_id}** — {args.verification_method}", ""])
    first_req = defined["Specification.md"][0]
    lines.extend(
        [
            "## Output and Evaluation Matrix",
            "",
            "| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |",
            "|---|---|---|---|---|---|",
            f"| {out_id} | {matrix_objectives} | {first_req} | {ac_id} | {ver_id} | Claim map, parity report, and applicable verification evidence |",
            "",
            f"<!-- pilot-variance: {args.variance_ref.strip()} -->",
            "",
        ]
    )
    output = "\n".join(lines)
    issues = validate_document(parse_sow_from_text(target, output))
    if issues:
        raise SowError("generated candidate failed validation: " + "; ".join(issues))
    if sha256_file(status) != status_before:
        raise SowError("_STATUS.md changed during conversion; refusing output")
    return output


def parse_sow_from_text(target: Path, text: str):
    """Validate generated text using the production parser without writing the target."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / target.name
        path.write_text(text, encoding="utf-8", newline="\n")
        return parse_sow(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deliverable", type=Path, required=True)
    parser.add_argument("--deliverable-id", required=True)
    parser.add_argument("--package-id", required=True)
    parser.add_argument("--decomposition-basis", required=True)
    parser.add_argument("--project-scope-ref", action="append", required=True)
    parser.add_argument("--package-objective-ref", action="append", required=True)
    parser.add_argument("--output-description", required=True)
    parser.add_argument("--acceptance-criterion", required=True)
    parser.add_argument("--verification-method", required=True)
    parser.add_argument("--pilot-variance", action="store_true")
    parser.add_argument("--variance-ref", default="")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    try:
        output = convert(args)
        target = args.deliverable / "ScopeOfWork.md"
        target.write_text(output, encoding="utf-8", newline="\n")
        print(target)
        return 0
    except (OSError, UnicodeError, SowError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
