from pathlib import Path

import validate_instruction_entrypoints as validator


def test_accepts_exact_import(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("# doctrine\n", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    assert validator.validate(tmp_path) == []


def test_rejects_added_instruction_layer(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("# doctrine\n", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\nextra\n", encoding="utf-8")
    assert validator.validate(tmp_path) == [
        "CLAUDE.md must contain exactly '@AGENTS.md\\n'"
    ]


def _write_project(
    tmp_path: Path,
    loop_text: str,
    workplan_text: str = "# Standing workplan\n",
) -> Path:
    (tmp_path / "AGENTS.md").write_text("# doctrine\n", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    project = tmp_path / "projects" / "chirality-app-dev"
    (project / "init").mkdir(parents=True)
    (project / "loop").mkdir()
    (project / "AGENTS.md").write_text(
        "one package-scoped instance\nTerminal fan-out/fan-in\n"
        "supervised many-to-many\nSOFTWARE_WORKFLOW_PROFILE.md\n",
        encoding="utf-8",
    )
    prompt = (
        "<init-prompt>\n"
        "Read `{REPO_ROOT}/AGENTS.md`.\n"
        "Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.\n"
        "Act as `HELP_HUMAN` for `{WORKING_ROOT}`.\n"
        f"Set project path to `projects/{project.name}`.\n"
        "Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it.\n"
        "</init-prompt>\n"
    )
    (project / "init" / "init-prompt.md").write_text(prompt, encoding="utf-8")
    (tmp_path / "init").mkdir()
    (tmp_path / "init" / "init-prompt.md").write_text(
        f"# Root launcher catalog\n\n{prompt}", encoding="utf-8"
    )
    (project / "loop" / "LOOP_INIT.md").write_text(loop_text, encoding="utf-8")
    (project / "loop" / "WORKPLAN_2026-07-17_test.md").write_text(
        workplan_text, encoding="utf-8"
    )
    (project / "software-workflow.json").write_text(
        '{"schema":"chirality-software-workflow/v1"}\n', encoding="utf-8"
    )
    return project


def test_accepts_help_human_entry_with_separated_loop(tmp_path: Path) -> None:
    _write_project(tmp_path, "# Loop\n\n## 7. Per-run steer\n")
    assert validator.validate(tmp_path) == []


def test_rejects_orchestration_duplication_in_help_human_loop(tmp_path: Path) -> None:
    project = _write_project(
        tmp_path,
        "# Loop\n\nBuild the current work graph, then fan out bounded children.\n",
    )
    rel = project.relative_to(tmp_path)
    findings = validator.validate(tmp_path)
    assert any(
        finding.startswith(f"{rel}/loop/LOOP_INIT.md duplicates canonical work-graph mechanics")
        for finding in findings
    )
    assert any("fan-out/fan-in mechanics" in finding for finding in findings)


def test_rejects_orchestration_duplication_in_current_workplan(tmp_path: Path) -> None:
    project = _write_project(
        tmp_path,
        "# Loop\n\n## 7. Per-run steer\n",
        "WORKING_ITEMS selects TASK children through managed delegation.\n"
        "Assign a capability tier before dispatch.\n",
    )
    rel = project.relative_to(tmp_path)
    findings = validator.validate(tmp_path)
    assert any(
        finding.startswith(
            f"{rel}/loop/WORKPLAN_2026-07-17_test.md duplicates canonical named Agent 1 routing"
        )
        for finding in findings
    )
    assert any("named Agent 2 routing" in finding for finding in findings)
    assert any("managed-child mechanics" in finding for finding in findings)
    assert any("model-assignment mechanics" in finding for finding in findings)


def test_rejects_root_project_launcher_drift(tmp_path: Path) -> None:
    project = _write_project(tmp_path, "# Loop\n")
    (tmp_path / "init" / "init-prompt.md").write_text(
        "# Root launcher catalog\n\n"
        "<init-prompt>\n"
        "Set project path to `projects/chirality-app-dev`.\n"
        "Act as `HELP_HUMAN` for a divergent root launcher.\n"
        "</init-prompt>\n",
        encoding="utf-8",
    )
    assert validator.validate(tmp_path) == [
        f"{project.relative_to(tmp_path)}/init/init-prompt.md does not byte-match the "
        "tagged root launcher for projects/chirality-app-dev"
    ]


def test_stale_copy_cannot_mask_drift_in_tagged_root_launcher(tmp_path: Path) -> None:
    project = _write_project(tmp_path, "# Loop\n")
    local_prompt = (project / "init" / "init-prompt.md").read_text(encoding="utf-8")
    (tmp_path / "init" / "init-prompt.md").write_text(
        "# Root launcher catalog\n\n"
        f"Stale untagged copy follows:\n{local_prompt.replace('<init-prompt>', '<stale-copy>').replace('</init-prompt>', '</stale-copy>')}\n"
        "Actual tagged launcher follows:\n"
        "<init-prompt>\n"
        "Set project path to `projects/chirality-app-dev`.\n"
        "Act as `HELP_HUMAN` for a divergent root launcher.\n"
        "</init-prompt>\n",
        encoding="utf-8",
    )
    assert validator.validate(tmp_path) == [
        f"{project.relative_to(tmp_path)}/init/init-prompt.md does not byte-match the "
        "tagged root launcher for projects/chirality-app-dev"
    ]


def test_help_human_detection_uses_actual_role_selection(tmp_path: Path) -> None:
    project = _write_project(tmp_path, "# Loop\n")
    prompt_path = project / "init" / "init-prompt.md"
    prompt = prompt_path.read_text(encoding="utf-8").replace(
        "Act as `HELP_HUMAN` for `{WORKING_ROOT}`.",
        "Act as `WORKING_ITEMS` for `{WORKING_ROOT}`.",
    )
    prompt_path.write_text(prompt, encoding="utf-8")
    (tmp_path / "init" / "init-prompt.md").write_text(prompt, encoding="utf-8")
    assert validator.validate(tmp_path) == []
