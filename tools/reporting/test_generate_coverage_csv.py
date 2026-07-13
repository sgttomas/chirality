from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).with_name("generate_coverage_csv.py")


def test_coverage_reports_legacy_and_candidate_format_states(tmp_path: Path) -> None:
    execution = tmp_path / "execution"
    working = execution / "PKG-01_Test" / "1_Working"
    legacy = working / "DEL-01-01_Legacy"
    pilot = working / "DEL-01-02_Pilot"
    for deliverable in (legacy, pilot):
        deliverable.mkdir(parents=True)
        for name in ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"):
            (deliverable / name).write_text("# source\n", encoding="utf-8")
    (pilot / "ScopeOfWork.md").write_text("# candidate\n", encoding="utf-8")
    output = tmp_path / "coverage.csv"

    subprocess.run([sys.executable, str(SCRIPT), str(execution), str(output)], check=True)
    with output.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert rows[0]["ProductionFormatState"] == "LEGACY_FOUR_DOC"
    assert rows[0]["HasScopeOfWork"] == "N"
    assert rows[1]["ProductionFormatState"] == "AMBIGUOUS"
    assert rows[1]["HasScopeOfWork"] == "Y"
