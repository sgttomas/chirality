#!/usr/bin/env python3
"""practitioner harness — governed read-mostly project observation CLI.

Subcommands: status, drift, self-check, brief. Markdown report always to
stdout; optional JSON report and brief files are contained to the declared
generated root `{REPO_ROOT}/_harness_generated/` (D-GOV-01 / K-WRITE-2).

Exit codes (D-GOV-02): 0 = ran, no BLOCK; 1 = >=1 BLOCK (or >=1 REVIEW under
--strict); 2 = operational error or refusal.

Everything emitted is a generated view — not authority; the cited source
files govern on any disagreement (K-AUTH-1).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cmd_brief
import cmd_drift
import cmd_self_check
import cmd_status
from harness_common import (
    EXIT_OPERATIONAL,
    GENERATED_ROOT_NAME,
    HarnessOperationalError,
    Report,
    compute_exit_code,
    resolve_repo_root,
)

PROJECT_ALIASES: dict[str, str] = {
    "app-dev": "projects/chirality-app-dev",
    "chirality-app-dev": "projects/chirality-app-dev",
    "piping": "projects/chirality-piping",
    "chirality-piping": "projects/chirality-piping",
}


def _project_root(repo_root: Path, name: str) -> Path:
    rel = PROJECT_ALIASES.get(name)
    if rel is None:
        raise HarnessOperationalError(
            f"Unknown --project {name!r}; known: {sorted(set(PROJECT_ALIASES))}")
    root = repo_root / rel
    if not root.is_dir():
        raise HarnessOperationalError(f"Project root absent: {root}")
    return root


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo-root", default=argparse.SUPPRESS,
                        help="Repo root (default: git rev-parse --show-toplevel, "
                             "else walk up for .git)")
    common.add_argument("--strict", action="store_true", default=argparse.SUPPRESS,
                        help="Treat REVIEW findings as exit-1")
    common.add_argument("--json-report", default=argparse.SUPPRESS,
                        help=f"Write the JSON report at this path (must be inside "
                             f"{GENERATED_ROOT_NAME}/)")
    common.add_argument("--out-dir", default=argparse.SUPPRESS,
                        help=f"Generated-output directory (default: "
                             f"{{REPO_ROOT}}/{GENERATED_ROOT_NAME}; all file writes "
                             "contained to the generated root)")

    parser = argparse.ArgumentParser(
        prog="harness.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[common],
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_status = sub.add_parser("status", parents=[common],
                              help="One-page sourced posture view")
    g = p_status.add_mutually_exclusive_group(required=True)
    g.add_argument("--project", choices=sorted(set(PROJECT_ALIASES)))
    g.add_argument("--domain-engines", action="store_true")

    p_drift = sub.add_parser("drift", parents=[common],
                             help="Current State vs history-assertion drift audit")
    p_drift.add_argument("--project", choices=sorted(set(PROJECT_ALIASES)))
    p_drift.add_argument("--all", action="store_true",
                         help="Audit both pilot projects (default)")
    p_drift.add_argument("--include-domain-engines", action="store_true",
                         help="Fold in the domain-engine control-area surface audit")

    p_check = sub.add_parser("self-check", parents=[common],
                             help="Consistency audit over the pilot scope")
    p_check.add_argument("--root", help="Audit only this root (default: pilot scope)")

    p_brief = sub.add_parser("brief", parents=[common],
                             help="Emit a CANDIDATE tranche brief (never adopts)")
    p_brief.add_argument("--project", required=True, choices=sorted(set(PROJECT_ALIASES)))
    p_brief.add_argument("--deliverable", required=True, metavar="DEL-NN-MM")
    p_brief.add_argument("--objective", default=None)
    p_brief.add_argument("--tranche-id", default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    strict = bool(getattr(args, "strict", False))
    json_report: str | None = getattr(args, "json_report", None)
    try:
        repo_root = resolve_repo_root(getattr(args, "repo_root", None))
        out_dir = Path(getattr(args, "out_dir", repo_root / GENERATED_ROOT_NAME))

        report: Report
        if args.command == "status":
            if getattr(args, "domain_engines", False):
                report = cmd_status.run_status_domain_engines(repo_root)
            else:
                report = cmd_status.run_status_project(
                    repo_root, _project_root(repo_root, args.project))
        elif args.command == "drift":
            if args.project and not args.all:
                roots = [_project_root(repo_root, args.project)]
            else:
                roots = [_project_root(repo_root, "app-dev"),
                         _project_root(repo_root, "piping")]
            report = cmd_drift.run_drift(
                repo_root, roots,
                include_domain_engines=getattr(args, "include_domain_engines", False))
        elif args.command == "self-check":
            root_filter = Path(args.root) if getattr(args, "root", None) else None
            if root_filter is not None and not root_filter.is_absolute():
                root_filter = repo_root / root_filter
            report, refusal = cmd_self_check.run_self_check(repo_root, root_filter)
            if refusal is not None:
                sys.stdout.write(report.render_markdown())
                if json_report:
                    report.write_json(json_report, repo_root)
                print(refusal, file=sys.stderr)
                return EXIT_OPERATIONAL
        elif args.command == "brief":
            project_root = _project_root(repo_root, args.project)
            others = sorted(
                {repo_root / rel for rel in PROJECT_ALIASES.values()} - {project_root})
            report = cmd_brief.run_brief(
                repo_root, project_root, [p for p in others if p.is_dir()],
                deliverable=args.deliverable, objective=args.objective,
                tranche_id=getattr(args, "tranche_id", None), out_dir=out_dir)
        else:  # pragma: no cover - argparse enforces the choices.
            raise HarnessOperationalError(f"Unknown command {args.command!r}")

        sys.stdout.write(report.render_markdown())
        if json_report:
            report.write_json(json_report, repo_root)
        if report.summary.get("identity_refusal"):
            print(str(report.summary["identity_refusal"]), file=sys.stderr)
            return EXIT_OPERATIONAL
        return compute_exit_code(report.findings, strict=strict)
    except HarnessOperationalError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_OPERATIONAL


if __name__ == "__main__":
    sys.exit(main())
