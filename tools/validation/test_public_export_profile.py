from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPORTER = REPO_ROOT / "exports" / "chirality-app" / "export_public.py"


def load_exporter():
    if not EXPORTER.exists():
        pytest.skip("public export intentionally excludes the private export profile")
    spec = importlib.util.spec_from_file_location("chirality_public_export", EXPORTER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_public_export_excludes_private_runtime_surfaces(tmp_path: Path) -> None:
    exporter = load_exporter()
    stage = tmp_path / "stage"
    exporter.build_stage(stage)

    assert (stage / 'agents/registry.json').is_file()
    assert len(list((stage / 'agents').glob('AGENT_*.md'))) == 4
    assert len(list((stage / 'workflows').glob('*/WORKFLOW.md'))) == 71
    assert (stage / 'ADOPTION_HOLD.json').is_file()
    assert not (stage / 'skills').exists()
    assert not (stage / ".github/workflows/harness-premerge.yml").exists()
    assert not any((stage / "docs/governance_harness/briefs").glob("*"))
    assert not (stage / "tools/practitioner_harness/BACKLOG.md").exists()

    prompt = (stage / "init/init-prompt.md").read_text(encoding="utf-8")
    assert "does not include project loop entrypoints" in prompt
    assert "projects/chirality-app-dev" not in prompt
    assert "projects/chirality-piping" not in prompt

    public_readme = (stage / "README.md").read_text(encoding="utf-8")
    dedicated_readme = (exporter.PROFILE_DIR / "PUBLIC_README.md").read_text(encoding="utf-8")
    canonical_readme = (exporter.REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert public_readme == dedicated_readme
    assert public_readme != canonical_readme
    for marker in exporter.PUBLIC_README_REQUIRED_MARKERS:
        assert marker in public_readme
    for marker in exporter.PUBLIC_README_FORBIDDEN_MARKERS:
        assert marker.casefold() not in public_readme.casefold()

    # The private project's governance scaffold must not enter the public
    # runtime workspace, and an ignored old runtime/ cannot mask an empty export.
    assert (stage / "runtime/package.json").read_bytes() == (
        REPO_ROOT / "projects/chirality-runtime/package.json"
    ).read_bytes()
    assert (stage / "runtime/packages/core/src/runtime-service.ts").is_file()
    assert not (stage / "runtime/chirality.project.json").exists()
    assert not (stage / "runtime/AGENTS.md").exists()
    assert not (stage / "runtime/execution").exists()
    assert not (stage / "runtime/loop").exists()
    assert not (stage / "runtime/docs").exists()

    assert exporter.boundary_findings(stage) == []


def test_public_export_rejects_private_canonical_readme_framing(tmp_path: Path) -> None:
    exporter = load_exporter()
    stage = tmp_path / "stage"
    stage.mkdir()
    (stage / "README.md").write_text(
        "\n".join(exporter.PUBLIC_README_REQUIRED_MARKERS)
        + "\n## Private Canonical Repository\n",
        encoding="utf-8",
    )

    assert (
        "private canonical README marker in public README: ## Private Canonical Repository"
        in exporter.boundary_findings(stage)
    )


def test_adoption_hold_blocks_apply(tmp_path):
    import json
    import pytest
    exporter=load_exporter()
    stage=tmp_path/'stage';stage.mkdir()
    (stage/'ADOPTION_HOLD.json').write_text(json.dumps({'status':'HELD'}))
    with pytest.raises(SystemExit,match='adoption held'):exporter.apply_target(stage,tmp_path/'target')
