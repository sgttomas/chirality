from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "render_approval.py"
SPEC = importlib.util.spec_from_file_location("render_approval", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_exact_frozen_candidate_verifies() -> None:
    MODULE.verify()


def test_rendered_outputs_are_exact_and_deterministic() -> None:
    assert MODULE.QUESTION_OUTPUT.read_bytes() == MODULE.render_question()
    assert MODULE.RULING_OUTPUT.read_bytes() == MODULE.render_ruling("Yes")
    assert MODULE.render_question() == MODULE.render_question()
    assert MODULE.render_ruling("Yes") == MODULE.render_ruling("Yes")
    assert MODULE.approval_root().encode() in MODULE.render_question()
    assert MODULE.artifact_digest().encode() in MODULE.render_question()
    assert MODULE.approval_root().encode() in MODULE.render_ruling("Yes")
    assert MODULE.artifact_digest().encode() in MODULE.render_ruling("Yes")


def test_artifact_manifest_uses_exact_acyclic_exclusions() -> None:
    rows = MODULE.parse_hash_manifest(MODULE.ARTIFACT_MANIFEST)
    assert set(rows) == set(MODULE.expected_fileset()) - MODULE.ARTIFACT_EXCLUSIONS
    assert MODULE.ARTIFACT_EXCLUSIONS == {
        "ARTIFACT_HASHES.sha256",
        "OWNER_QUESTION.md",
        MODULE.RULING_RELATIVE,
    }


@pytest.mark.parametrize("answer", ["No", "yes", "Yes.", "I approve", ""])
def test_non_exact_owner_answers_cannot_render_ruling(answer: str) -> None:
    with pytest.raises(MODULE.ApprovalError):
        MODULE.render_ruling(answer)


def test_hash_manifest_rejects_duplicate_path(tmp_path: Path) -> None:
    digest = "0" * 64
    manifest = tmp_path / "manifest.sha256"
    manifest.write_text(
        f"{digest}  one.md\n{digest}  one.md\n",
        encoding="utf-8",
    )
    with pytest.raises(MODULE.ApprovalError):
        MODULE.parse_hash_manifest(manifest)


def test_hash_manifest_rejects_unsafe_path(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.sha256"
    manifest.write_text(f"{'0' * 64}  ../escape.md\n", encoding="utf-8")
    with pytest.raises(MODULE.ApprovalError):
        MODULE.parse_hash_manifest(manifest)


def test_literal_fileset_is_exact() -> None:
    assert MODULE.expected_fileset() == MODULE.observed_fileset()


def test_bytecode_containment_is_required(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(MODULE.sys, "dont_write_bytecode", False)
    monkeypatch.delenv("PYTHONPYCACHEPREFIX", raising=False)
    with pytest.raises(MODULE.ApprovalError):
        MODULE.require_bytecode_containment()

    monkeypatch.setenv("PYTHONPYCACHEPREFIX", str(MODULE.PROPOSAL / "cache"))
    with pytest.raises(MODULE.ApprovalError):
        MODULE.require_bytecode_containment()

    monkeypatch.setenv("PYTHONPYCACHEPREFIX", str(tmp_path / "cache"))
    MODULE.require_bytecode_containment()

    monkeypatch.setenv("PYTHONPYCACHEPREFIX", "relative-cache")
    with pytest.raises(MODULE.ApprovalError):
        MODULE.require_bytecode_containment()


def test_cache_directories_are_rejected(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    proposal = tmp_path / "proposal"
    (proposal / "tests" / "__pycache__").mkdir(parents=True)
    monkeypatch.setattr(MODULE, "PROPOSAL", proposal)
    with pytest.raises(MODULE.ApprovalError):
        MODULE.observed_fileset()


def test_unlisted_fifo_is_rejected_with_path_diagnostic(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    proposal = tmp_path / "proposal"
    proposal.mkdir()
    sentinel = proposal / "UNLISTED_NONREGULAR_SENTINEL"
    os.mkfifo(sentinel)
    monkeypatch.setattr(MODULE, "PROPOSAL", proposal)
    with pytest.raises(MODULE.ApprovalError) as caught:
        MODULE.observed_fileset()
    diagnostic = str(caught.value)
    assert "nonregular entry" in diagnostic
    assert "UNLISTED_NONREGULAR_SENTINEL" in diagnostic


def test_application_contract_requires_final_contained_fileset_gate() -> None:
    instructions = (MODULE.PROPOSAL / "APPLICATION_AND_ROLLBACK.md").read_text()
    assert "Every Python command" in instructions
    assert "last filesystem-sensitive check before `git add`" in instructions
