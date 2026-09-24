#!/usr/bin/env python3
"""Route hosted jobs using the existing registered affected-check selector."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess

from select_affected_checks import select_checks
from software_workflow_common import load_profile, matches

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "tools/hosted-ci-routing.json"


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE).decode("utf-8")


def select_paths(paths: list[str], profile: dict) -> dict:
    selection = select_checks(profile, paths)
    checks = set(selection["checks"])
    unmatched = [p for p in paths if not any(matches(p, rule["paths"]) for rule in profile["path_rules"])]
    for path in unmatched:
        owners = (["app"] if path.startswith("projects/chirality-app-dev/") else
                  ["pec"] if path.startswith("projects/pec/") else ["app", "pec"])
        checks.update(owners)
        for owner in owners:
            selection["reasons"].setdefault(owner, []).append(path)
    selection.update(checks=sorted(checks), unmatched_paths=unmatched)
    selection["modes"] = {
        "app": "full" if "app" in checks else "instructions" if "instructions" in checks else "not-applicable",
        "pec": "full" if "pec" in checks else "not-applicable",
    }
    return selection


def make_plan(root: Path, profile: dict, event: str, base: str, head: str) -> dict:
    resolved_head = git(root, "rev-parse", "--verify", head + "^{commit}").strip()
    plan = {"schema": "chirality-hosted-ci/v1", "event": event,
            "target_base": base, "head": resolved_head, "base": None,
            "paths": [], "checks": ["app", "pec"], "reasons": {}, "unmatched_paths": [],
            "modes": {"app": "full", "pec": "full"}, "selection_reason": "Explicit full workflow dispatch"}
    if event != "pull_request":
        return plan
    try:
        if not base:
            raise ValueError("missing base")
        merge_base = git(root, "merge-base", base, resolved_head).strip()
        # --no-renames includes both sides of renames; NUL delimiters preserve paths.
        paths = git(root, "diff", "--name-only", "--no-renames", "-z", merge_base, resolved_head, "--").split("\0")
        paths = sorted(p for p in paths if p)
    except (subprocess.CalledProcessError, UnicodeError, ValueError):
        plan["selection_reason"] = "Unavailable complete PR diff; full product coverage"
        return plan
    plan.update(select_paths(paths, profile))
    plan.update(schema="chirality-hosted-ci/v1", base=merge_base,
                selection_reason="Complete PR diff and registered path rules; unmatched inputs use full coverage")
    return plan


def aggregate(suite: str, mode: str, selection: str, product: str, instructions: str = "skipped") -> bool:
    if selection != "success":
        return False
    if mode == "full":
        return product == "success"
    if mode == "instructions" and suite == "app":
        return instructions == "success" and product == "skipped"
    return mode == "not-applicable" and product == "skipped" and instructions == "skipped"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan_parser = commands.add_parser("plan")
    plan_parser.add_argument("--event", required=True)
    plan_parser.add_argument("--base", default="")
    plan_parser.add_argument("--head", default="HEAD")
    plan_parser.add_argument("--suite", choices=["app", "pec"], required=True)
    plan_parser.add_argument("--output", required=True)
    result_parser = commands.add_parser("aggregate")
    result_parser.add_argument("--suite", choices=["app", "pec"], required=True)
    result_parser.add_argument("--mode", required=True)
    result_parser.add_argument("--selection", required=True)
    result_parser.add_argument("--product", required=True)
    result_parser.add_argument("--instructions", default="skipped")
    args = parser.parse_args()
    if args.command == "aggregate":
        passed = aggregate(args.suite, args.mode, args.selection, args.product, args.instructions)
        print(f"{args.suite}: mode={args.mode}, selection={args.selection}, product={args.product}, instructions={args.instructions}")
        if passed and args.mode == "not-applicable":
            print("No product inputs changed; product suites were not run.")
        return 0 if passed else 1
    _, profile = load_profile(PROFILE)
    plan = make_plan(ROOT, profile, args.event, args.base, args.head)
    if git(ROOT, "rev-parse", "HEAD").strip() != plan["head"]:
        raise ValueError("Selection checkout differs from requested candidate")
    Path(args.output).write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n")
    mode = plan["modes"][args.suite]
    print(json.dumps(plan, indent=2, sort_keys=True))
    if os.getenv("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write(f"mode={mode}\n")
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as stream:
            stream.write(f"### {args.suite} CI selection: {mode}\n\n{plan['selection_reason']}. "
                         f"Candidate `{plan['head']}`; {len(plan['paths'])} changed paths.\n\n"
                         f"Selection and reasons are retained in `{args.output}`.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
