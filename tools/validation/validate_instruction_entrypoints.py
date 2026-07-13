#!/usr/bin/env python3
"""Validate root instruction entrypoints and the Claude import contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_CLAUDE = "@AGENTS.md\n"
PROJECTS = ("chirality-app-dev", "chirality-piping")


def validate(repo_root: Path) -> list[str]:
    findings: list[str] = []
    agents = repo_root / "AGENTS.md"
    claude = repo_root / "CLAUDE.md"
    if not agents.is_file():
        findings.append("missing root AGENTS.md")
    if not claude.is_file():
        findings.append("missing root CLAUDE.md")
    elif claude.read_text(encoding="utf-8") != EXPECTED_CLAUDE:
        findings.append("CLAUDE.md must contain exactly '@AGENTS.md\\n'")
    for project_name in PROJECTS:
        project_root = repo_root / "projects" / project_name
        if not project_root.is_dir():
            continue
        project_agents = project_root / "AGENTS.md"
        loop_init = project_root / "loop" / "LOOP_INIT.md"
        profile = project_root / "software-workflow.json"
        for required in (project_agents, loop_init, profile):
            if not required.is_file():
                findings.append(f"{required.relative_to(repo_root)} is missing")
        if project_agents.is_file():
            text = project_agents.read_text(encoding="utf-8").lower()
            for phrase in (
                "one package-scoped instance",
                "terminal fan-out/fan-in",
                "supervised many-to-many",
                "software_workflow_profile.md",
            ):
                if phrase not in text:
                    findings.append(f"{project_agents.relative_to(repo_root)} is missing '{phrase}'")
        if loop_init.is_file():
            text = loop_init.read_text(encoding="utf-8")
            for phrase in (
                "HUMAN | AGENT_0 | AGENT_1",
                "TERMINAL_FAN_OUT_IN | SUPERVISED_MANY_TO_MANY | MIXED",
                "execution/_Coordination/AgentRuns/<RunID>/",
                "defer the multi-agent stage",
            ):
                if phrase not in text:
                    findings.append(f"{loop_init.relative_to(repo_root)} is missing '{phrase}'")
            if "when the managed runtime is active" in text:
                findings.append(f"{loop_init.relative_to(repo_root)} retains the retired pre-bridge fallback")
        if profile.is_file():
            try:
                payload = json.loads(profile.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                findings.append(f"{profile.relative_to(repo_root)} is not valid JSON")
            else:
                if payload.get("schema") != "chirality-software-workflow/v1":
                    findings.append(f"{profile.relative_to(repo_root)} has the wrong schema")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", nargs="?", default=".")
    args = parser.parse_args()
    findings = validate(Path(args.repo_root).resolve())
    if findings:
        for finding in findings:
            print(f"FAIL: {finding}")
        return 1
    print("PASS: root instruction entrypoints are canonical")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
