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
