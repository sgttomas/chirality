#!/usr/bin/env python3
"""Route hosted jobs using the existing registered affected-check selector."""
from __future__ import annotations

import argparse
import json
import importlib.util
import os
from pathlib import Path
import subprocess

from select_affected_checks import select_checks
from software_workflow_common import load_profile, matches

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "tools/hosted-ci-routing.json"
SUITES = ("app-v4", "piping", "piping-numerical", "piping-python")


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE).decode("utf-8")


def numerical_module(root: Path):
    path = root / "projects/chirality-piping/tools/ci/numerical_ci.py"
    if not path.is_file():
        raise ValueError("Numerical selector unavailable")
    spec = importlib.util.spec_from_file_location("hosted_numerical_selection", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def numerical_plan(root: Path, paths: list[str] | None, profile: dict) -> dict:
    manifests = []
    try:
        module = numerical_module(root)
        project = root / "projects/chirality-piping"
        manifests = module.readiness.discover_cargo_manifests(project)
        ignored = []
        for path in paths or []:
            rules = [rule for rule in profile["path_rules"] if matches(path, rule["paths"])]
            if rules and not any("piping-numerical" in rule["checks"] for rule in rules):
                ignored.append(path)
        desktop = profile.get("piping_desktop_resources", {})
        if desktop:
            if desktop.get("pointer") != "cases.fixture":
                raise ValueError("Unresolved desktop resource declaration")
            source = (project / desktop["source"]).resolve()
            source.relative_to(project.resolve())
            cases = json.loads(source.read_text())["cases"]
            actual = {case["fixture"] for case in cases}
            if actual != set(desktop.get("files", [])):
                raise ValueError("Stale desktop resource declaration")
            resources = {"projects/chirality-piping/" + path for path in actual}
            for path in resources:
                target = (root / path).resolve()
                target.relative_to(project.resolve())
                if not target.is_file():
                    raise ValueError("Unresolved desktop fixture: " + path)
            ignored.extend(p for p in paths or [] if p in resources)
        return module.numerical_selection(project, manifests, paths,
                                          profile.get("piping_runtime_reads", {}), ignored)
    except (ValueError, OSError, KeyError, TypeError, AttributeError, ImportError) as exc:
        return {"version": 2, "classification": "full-fallback", "manifests": [m.as_posix() for m in manifests],
                "reasons": [], "fallback_reasons": [str(exc)]}


def select_paths(paths: list[str], profile: dict, root: Path = ROOT) -> dict:
    selection = select_checks(profile, paths)
    checks = set(selection["checks"])
    unmatched = [p for p in paths if not any(matches(p, rule["paths"]) for rule in profile["path_rules"])]
    for path in unmatched:
        owners = ([] if path.startswith("projects/chirality-app-dev/") else
                  [] if path.startswith("projects/pec/") else
                  ["app-v4"] if path.startswith("projects/chirality-app-v4/") else
                  ["piping", "piping-numerical", "piping-python"] if path.startswith("projects/chirality-piping/") else
                  [] if path.startswith("projects/chirality-runtime/") else list(SUITES))
        checks.update(owners)
        for owner in owners:
            selection["reasons"].setdefault(owner, []).append(path)
    selection.update(checks=sorted(checks), unmatched_paths=unmatched)
    selection["modes"] = {suite: "full" if suite in checks else "not-applicable" for suite in SUITES}
    if "piping-numerical" in checks or any(p.startswith("projects/chirality-piping/") for p in paths):
        numerical = numerical_plan(root, paths, profile)
        selected = numerical["classification"] == "full-fallback" or bool(numerical["manifests"])
        selection["modes"]["piping-numerical"] = "full" if selected else "not-applicable"
        if selected:
            checks.add("piping-numerical")
            # A source consumed by Rust may occur in a records/desktop path rule.
            checks.add("piping-python")
            selection["modes"]["piping-python"] = "full"
        else:
            checks.discard("piping-numerical")
        selection["piping_numerical_selection"] = numerical
        selection["checks"] = sorted(checks)
    return selection


def make_plan(root: Path, profile: dict, event: str, base: str, head: str) -> dict:
    resolved_head = git(root, "rev-parse", "--verify", head + "^{commit}").strip()
    plan = {"schema": "chirality-hosted-ci/v1", "event": event,
            "target_base": base, "head": resolved_head, "base": None,
            "paths": [], "checks": list(SUITES), "reasons": {}, "unmatched_paths": [],
            "modes": {suite: "full" for suite in SUITES}, "selection_reason": "Explicit full workflow dispatch",
            "piping_numerical_selection": numerical_plan(root, None, profile)}
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
    plan.update(select_paths(paths, profile, root))
    if "piping_numerical_selection" not in plan or not any(p.startswith("projects/chirality-piping/") for p in paths) and "piping-numerical" not in plan["checks"]:
        plan["piping_numerical_selection"] = {"version": 2, "classification": "not-applicable", "manifests": [], "reasons": [], "fallback_reasons": []}
    plan.update(schema="chirality-hosted-ci/v1", base=merge_base,
                selection_reason="Complete PR diff and registered path rules; unmatched inputs use full coverage")
    return plan


def validate_plan(root: Path, plan: dict) -> None:
    """Recompute candidate diff, routing, graph and exact manifest identity."""
    if plan.get("schema") != "chirality-hosted-ci/v1":
        raise ValueError("Unknown selection schema")
    if git(root, "rev-parse", "HEAD").strip() != plan.get("head"):
        raise ValueError("Selection does not name the checked-out candidate")
    _, profile = load_profile(root / "tools/hosted-ci-routing.json")
    expected = make_plan(root, profile, plan.get("event", ""), plan.get("target_base", ""), plan["head"])
    if plan != expected:
        raise ValueError("Selection differs from the complete candidate diff or current reachability inputs")


def aggregate(suite: str, mode: str, selection: str, product: str, instructions: str = "skipped") -> bool:
    if selection != "success":
        return False
    if mode == "full":
        return product == "success"
    return mode == "not-applicable" and product == "skipped" and instructions == "skipped"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan_parser = commands.add_parser("plan")
    plan_parser.add_argument("--event", required=True)
    plan_parser.add_argument("--base", default="")
    plan_parser.add_argument("--head", default="HEAD")
    plan_parser.add_argument("--suite", choices=SUITES, required=True)
    plan_parser.add_argument("--output", required=True)
    result_parser = commands.add_parser("aggregate")
    result_parser.add_argument("--suite", choices=SUITES, required=True)
    result_parser.add_argument("--mode", required=True)
    result_parser.add_argument("--selection", required=True)
    result_parser.add_argument("--product", required=True)
    result_parser.add_argument("--instructions", default="skipped")
    args = parser.parse_args()
    if args.command == "aggregate":
        passed = aggregate(args.suite, args.mode, args.selection, args.product, args.instructions)
        print(f"{args.suite}: mode={args.mode}, selection={args.selection}, product={args.product}, instructions={args.instructions}")
        if passed and args.mode == "not-applicable":
            print(f"No inputs selected for {args.suite}; this suite was not run.")
        elif not passed and args.product in ("skipped", "", "cancelled"):
            print("Selected coverage did not complete; this is not a pass.")
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
                         "Selection and reasons are printed in this job’s log.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
