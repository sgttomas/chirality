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


def test_accepts_project_loop_orchestration_contract(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("# doctrine\n", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    project = tmp_path / "projects" / "chirality-app-dev"
    (project / "loop").mkdir(parents=True)
    (project / "AGENTS.md").write_text(
        "one package-scoped instance\nTerminal fan-out/fan-in\n"
        "supervised many-to-many\nSOFTWARE_WORKFLOW_PROFILE.md\n",
        encoding="utf-8",
    )
    (project / "loop" / "LOOP_INIT.md").write_text(
        "HUMAN | AGENT_0 | AGENT_1\n"
        "TERMINAL_FAN_OUT_IN | SUPERVISED_MANY_TO_MANY | MIXED\n"
        "execution/_Coordination/AgentRuns/<RunID>/\n"
        "defer the multi-agent stage\n",
        encoding="utf-8",
    )
    (project / "software-workflow.json").write_text(
        '{"schema":"chirality-software-workflow/v1"}\n', encoding="utf-8"
    )
    assert validator.validate(tmp_path) == []
