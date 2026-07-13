from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VARIANCE_REF = "D-GOV-15@0123456"
CONVERT = HERE / "convert_four_documents_to_scope_of_work.py"
VALIDATE = HERE / "validate_scope_of_work.py"
RENDER = HERE / "render_scope_of_work.py"
MAP = HERE / "map_scope_of_work_claims.py"
PARITY = HERE / "report_scope_of_work_parity.py"


def run(tool: Path, *args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(tool), *(str(arg) for arg in args)], text=True, capture_output=True)


def fixture(tmp_path: Path, state: str = "IN_PROGRESS") -> Path:
    deliverable = tmp_path / "PKG-07" / "DEL-07-03_Test"
    deliverable.mkdir(parents=True)
    sources = {
        "Datasheet.md": "# Datasheet\n\n## Identification\n\nA bounded output.\n",
        "Specification.md": "# Specification\n\n## Requirements\n\nThe output shall be traceable.\n",
        "Procedure.md": "# Procedure\n\n## Verification\n\nRun the parity check.\n",
        "Guidance.md": "# Guidance\n\n## Principles\n\nPrefer source fidelity.\n",
    }
    for name, text in sources.items():
        (deliverable / name).write_text(text, encoding="utf-8")
    (deliverable / "_STATUS.md").write_text(f"# Status\n\n**Current State:** {state}\n\n## Remaining\n", encoding="utf-8")
    return deliverable


def convert(deliverable: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return run(
        CONVERT,
        "--deliverable", deliverable,
        "--deliverable-id", "DEL-07-03",
        "--package-id", "PKG-07",
        "--decomposition-basis", "execution/_Decomposition/SOFTWARE_DECOMP.md@abc123",
        "--project-scope-ref", "SOW-001",
        "--package-objective-ref", "OBJ-007",
        "--output-description", "A traceable deliverable contract.",
        "--acceptance-criterion", "The mapped source content is complete and internally resolvable.",
        "--verification-method", "Run the deterministic claim map and parity report.",
        *extra,
    )


def test_converter_requires_variance_and_preserves_lifecycle(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    status_before = hashlib.sha256((deliverable / "_STATUS.md").read_bytes()).hexdigest()
    denied = convert(deliverable)
    assert denied.returncode == 1
    assert "pilot-variance" in denied.stderr
    assert not (deliverable / "ScopeOfWork.md").exists()

    result = convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert result.returncode == 0, result.stderr
    assert hashlib.sha256((deliverable / "_STATUS.md").read_bytes()).hexdigest() == status_before
    for name in ("Datasheet.md", "Specification.md", "Procedure.md", "Guidance.md"):
        assert (deliverable / name).is_file()


def test_converter_refuses_issued(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path, "ISSUED")
    result = convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert result.returncode == 1
    assert "refuses ISSUED" in result.stderr


def test_format_resolution_fails_ambiguous_without_variance(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    ambiguous = run(VALIDATE, deliverable, "--json")
    assert ambiguous.returncode == 1
    assert json.loads(ambiguous.stdout)["format"] == "AMBIGUOUS"
    allowed = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF, "--json")
    assert allowed.returncode == 0, allowed.stdout
    assert json.loads(allowed.stdout)["format"] == "PILOT_DUAL"
    wrong_ref = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", "D-GOV-15:wrong", "--json")
    assert wrong_ref.returncode == 1
    assert "accepted-sha" in " ".join(json.loads(wrong_ref.stdout)["issues"])


def test_legacy_and_sow_only_formats_are_valid_but_partial_legacy_is_not(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    legacy = run(VALIDATE, deliverable, "--json")
    assert legacy.returncode == 0
    assert json.loads(legacy.stdout)["format"] == "LEGACY_FOUR_DOC"

    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    for name in ("Datasheet.md", "Specification.md", "Procedure.md", "Guidance.md"):
        (deliverable / name).unlink()
    sow_only = run(VALIDATE, deliverable, "--json")
    assert sow_only.returncode == 0, sow_only.stdout
    assert json.loads(sow_only.stdout)["format"] == "SOW_V1"

    (deliverable / "Datasheet.md").write_text("# orphan\n", encoding="utf-8")
    partial = run(VALIDATE, deliverable, "--json")
    assert partial.returncode == 1
    assert json.loads(partial.stdout)["format"] == "INVALID"


def test_claim_map_and_parity_cover_every_source_line(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    mapping = tmp_path / "claim_map.csv"
    parity = tmp_path / "parity.json"
    map_result = run(MAP, "--scope-of-work", deliverable / "ScopeOfWork.md", "--source-dir", deliverable, "--output-csv", mapping)
    assert map_result.returncode == 0, map_result.stderr
    rows = list(csv.DictReader(mapping.open(encoding="utf-8")))
    assert rows and {row["SourceFile"] for row in rows} == {
        "Datasheet.md", "Specification.md", "Procedure.md", "Guidance.md"
    }
    parity_result = run(PARITY, "--scope-of-work", deliverable / "ScopeOfWork.md", "--source-dir", deliverable, "--output-json", parity)
    assert parity_result.returncode == 0, parity_result.stderr
    assert json.loads(parity.read_text(encoding="utf-8"))["pass"] is True


def test_renderer_is_deterministic_source_bound_and_script_free(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    first = tmp_path / "first.html"
    second = tmp_path / "second.html"
    for output in (first, second):
        result = run(RENDER, deliverable / "ScopeOfWork.md", "--output", output)
        assert result.returncode == 0, result.stderr
    assert first.read_bytes() == second.read_bytes()
    rendered = first.read_text(encoding="utf-8")
    source_hash = hashlib.sha256((deliverable / "ScopeOfWork.md").read_bytes()).hexdigest()
    assert source_hash in rendered
    assert "<script" not in rendered.lower()
    assert "http://" not in rendered.lower() and "https://" not in rendered.lower()


def test_catalog_drives_unknown_reference_detection(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    sow = deliverable / "ScopeOfWork.md"
    sow.write_text(sow.read_text(encoding="utf-8") + "\nReference CLM-999.\n", encoding="utf-8")
    result = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert result.returncode == 1
    assert "CLM-999" in result.stdout


def test_legacy_id_like_text_does_not_collide_with_candidate_catalog(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    specification = deliverable / "Specification.md"
    specification.write_text(
        specification.read_text(encoding="utf-8") + "\nLegacy review note AC-999 remains historical text.\n",
        encoding="utf-8",
    )
    result = convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert result.returncode == 0, result.stderr
    validation = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert validation.returncode == 0, validation.stdout


def test_orphan_output_acceptance_and_verification_definitions_fail(tmp_path: Path) -> None:
    for definition, expected in (
        ("- **OUT-999** — Orphan output.", "OUT-999"),
        ("- **AC-999** — Orphan acceptance criterion.", "AC-999"),
        ("- **VER-999** — Orphan verification method.", "VER-999"),
    ):
        deliverable = fixture(tmp_path / expected)
        assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
        sow = deliverable / "ScopeOfWork.md"
        sow.write_text(sow.read_text(encoding="utf-8") + f"\n{definition}\n", encoding="utf-8")
        result = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
        assert result.returncode == 1
        assert expected in result.stdout


def test_explicit_human_review_can_replace_verification_definition(tmp_path: Path) -> None:
    deliverable = fixture(tmp_path)
    assert convert(deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF).returncode == 0
    sow = deliverable / "ScopeOfWork.md"
    text = sow.read_text(encoding="utf-8")
    text = text.replace("- **VER-001** — Run the deterministic claim map and parity report.\n", "")
    text = text.replace("| AC-001 | VER-001 |", "| AC-001 | HUMAN_REVIEW: owner inspection |")
    sow.write_text(text, encoding="utf-8")
    result = run(VALIDATE, deliverable, "--pilot-variance", "--variance-ref", VARIANCE_REF)
    assert result.returncode == 0, result.stdout
