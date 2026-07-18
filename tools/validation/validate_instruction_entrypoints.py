#!/usr/bin/env python3
"""Validate root instruction entrypoints and the Claude import contract."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EXPECTED_CLAUDE = "@AGENTS.md\n"
PROJECTS = ("chirality-app-dev", "chirality-piping")
ORCHESTRATION_PATTERNS = (
    ("named Agent 0 routing", re.compile(r"\bHELP_HUMAN\b", re.IGNORECASE)),
    ("named Agent 1 routing", re.compile(r"\bWORKING_ITEMS\b", re.IGNORECASE)),
    ("named Agent 2 routing", re.compile(r"\bTASK\b", re.IGNORECASE)),
    ("agent-layer routing", re.compile(r"\bAgent\s+[012]\b", re.IGNORECASE)),
    ("multi-agent mechanics", re.compile(r"\bmulti[- ]agent\b", re.IGNORECASE)),
    ("orchestration mechanics", re.compile(r"\borchestrat\w*\b", re.IGNORECASE)),
    ("work-graph mechanics", re.compile(r"\bwork[- ]graph\b", re.IGNORECASE)),
    ("fan-out/fan-in mechanics", re.compile(r"\bfan[- ](?:out|in)\b", re.IGNORECASE)),
    (
        "managed-child mechanics",
        re.compile(r"\bmanaged\s+(?:delegation|runtime|child(?:ren| sessions?)?)\b", re.IGNORECASE),
    ),
    ("child-session mechanics", re.compile(r"\bchild sessions?\b", re.IGNORECASE)),
    ("parent-mediated mechanics", re.compile(r"\bparent-mediated\b", re.IGNORECASE)),
    ("sibling-message mechanics", re.compile(r"\bsibling messag\w*\b", re.IGNORECASE)),
    ("selection-authority mechanics", re.compile(r"\bselection authority\b", re.IGNORECASE)),
    (
        "model-assignment mechanics",
        re.compile(
            r"\b(?:named[- ]model|model[- ]agnostic|capability tier|"
            r"model substitution|model assignment)\w*\b",
            re.IGNORECASE,
        ),
    ),
)


def _project_launchers(root_init_text: str, project_name: str) -> list[str]:
    blocks = re.findall(
        r"(?ms)^<init-prompt>\n.*?^</init-prompt>\n?",
        root_init_text,
    )
    project_token = f"projects/{project_name}"
    return [block for block in blocks if project_token in block]


def validate(repo_root: Path) -> list[str]:
    findings: list[str] = []
    agents = repo_root / "AGENTS.md"
    claude = repo_root / "CLAUDE.md"
    root_init = repo_root / "init" / "init-prompt.md"
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
        project_init = project_root / "init" / "init-prompt.md"
        loop_init = project_root / "loop" / "LOOP_INIT.md"
        workplans = sorted((project_root / "loop").glob("WORKPLAN_*.md"))
        current_workplan = workplans[-1] if workplans else None
        profile = project_root / "software-workflow.json"
        for required in (project_agents, project_init, loop_init, profile):
            if not required.is_file():
                findings.append(f"{required.relative_to(repo_root)} is missing")
        if current_workplan is None:
            findings.append(f"{(project_root / 'loop').relative_to(repo_root)} has no WORKPLAN_*.md")
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
        help_human_entry = False
        if project_init.is_file():
            text = project_init.read_text(encoding="utf-8")
            help_human_entry = bool(
                re.search(r"Act as\s+`?HELP_HUMAN`?\s+for\s+`?\{WORKING_ROOT\}`?", text)
            )
            if not root_init.is_file():
                findings.append("missing root init/init-prompt.md")
            else:
                catalog_launchers = _project_launchers(
                    root_init.read_text(encoding="utf-8"), project_name
                )
                if len(catalog_launchers) != 1:
                    findings.append(
                        "root init/init-prompt.md must contain exactly one tagged "
                        f"launcher for projects/{project_name}; found {len(catalog_launchers)}"
                    )
                elif text != catalog_launchers[0]:
                    findings.append(
                        f"{project_init.relative_to(repo_root)} does not byte-match the "
                        f"tagged root launcher for projects/{project_name}"
                    )
            if help_human_entry:
                for phrase in (
                    "Read `{REPO_ROOT}/AGENTS.md`.",
                    "Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.",
                    "Act as `HELP_HUMAN` for `{WORKING_ROOT}`.",
                    "Read `{WORKING_ROOT}/loop/LOOP_INIT.md`",
                ):
                    if phrase not in text:
                        findings.append(
                            f"{project_init.relative_to(repo_root)} is missing '{phrase}'"
                        )
        loop_surfaces = [path for path in (loop_init, current_workplan) if path and path.is_file()]
        for loop_surface in loop_surfaces:
            text = loop_surface.read_text(encoding="utf-8")
            if help_human_entry:
                for label, pattern in ORCHESTRATION_PATTERNS:
                    match = pattern.search(text)
                    if match:
                        findings.append(
                            f"{loop_surface.relative_to(repo_root)} duplicates canonical "
                            f"{label}: '{match.group(0)}'"
                        )
        if loop_init.is_file():
            text = loop_init.read_text(encoding="utf-8")
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
