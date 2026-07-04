#!/usr/bin/env python3
"""Tests for the generated bridge-status view."""

from __future__ import annotations

import harness
import cmd_bridge_status
from test_self_check_fixtures import build_mini_repo


def _append(path, text: str) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def test_bridge_status_derives_open_rows_profile_and_receipt(tmp_path):
    repo = build_mini_repo(tmp_path)
    app_register = (
        repo
        / "projects"
        / "chirality-app-dev"
        / "execution"
        / "_Coordination"
        / "_DECISIONS"
        / "_REGISTER.md"
    )
    piping_register = (
        repo
        / "projects"
        / "chirality-piping"
        / "execution"
        / "_Coordination"
        / "_DECISIONS"
        / "_REGISTER.md"
    )
    profile = repo / "_DomainEngines" / "profiles" / "open_pipe_stress.DRAFT.yaml"
    receipts = repo / "_DomainEngines" / "bridge" / "LOOP_RECEIPTS.md"
    receipts.parent.mkdir(parents=True, exist_ok=True)

    _append(app_register, "| D-APP-99 | Fixture bridge packet | AWAITING_RULING |\n")
    _append(piping_register, "| D-06 | Fixture release matrix | NOT_PREPARED |\n")
    _append(piping_register, "| D-21 | Fixture scoped gate | RULED |\n")
    _append(
        profile,
        '\n  open_issues:\n'
        '    - "Live binding (L2-L3) gated x4: tier-0 adoption, app-dev F3, '
        'piping D-21, DEC-041 automation condition."\n',
    )
    receipts.write_text(
        "# Bridge Loop Receipts\n\n"
        "## Receipts\n\n"
        "- **2026-07-02 - Receipt 0**\n"
        "  - Gate outcome: historical fixture.\n"
        "- **2026-07-03 - Receipt 1**\n"
        "  - Owner direction of record: fixture direction.\n"
        "  - Gate outcome: fixture gate waits on owner merge.\n"
        "  - Parked lanes: fixture lane remains owner-directed.\n",
        encoding="utf-8",
    )

    report = cmd_bridge_status.run_bridge_status(repo)
    md = report.render_markdown()

    assert report.summary["open_register_rows"] == 2
    assert report.summary["latest_receipt"] == "2026-07-03 - Receipt 1"
    assert report.summary["owner_act_rows"] >= 5
    assert report.summary["parked_lane_rows"] == 1
    assert report.summary["parked_lane_receipt_only"] == 1
    assert report.summary["live_binding_gate_rows"] == 4
    assert "D-APP-99" in md
    assert "D-06" in md
    assert "Live binding (L2-L3) gated x4" in md
    assert "piping D-21" in md
    assert "D-21 State=RULED" in md
    assert "fixture gate waits on owner merge" in md
    assert "fixture lane remains owner-directed" in md
    assert "receipt-only" in md
    assert "tool never selects" in md


def test_bridge_status_warns_on_latest_receipt_label_drift(tmp_path):
    repo = build_mini_repo(tmp_path)
    receipts = repo / "_DomainEngines" / "bridge" / "LOOP_RECEIPTS.md"
    receipts.parent.mkdir(parents=True, exist_ok=True)
    receipts.write_text(
        "# Bridge Loop Receipts\n\n"
        "## Receipts\n\n"
        "- **2026-07-03 - Receipt 1**\n"
        "  - Owner directions of record: pluralized fixture direction.\n"
        "  - Gate outcome: fixture gate.\n"
        "  - Parked lanes: PR #42.\n",
        encoding="utf-8",
    )

    report = cmd_bridge_status.run_bridge_status(repo)

    hits = [f for f in report.findings if f.code == "RECEIPT_BULLET_LABEL_DRIFT"]
    assert len(hits) == 1
    assert hits[0].severity.value == "WARN"
    assert "Owner direction of record" in hits[0].message


def test_bridge_status_cli_runs_on_minimal_fixture(tmp_path, capsys):
    repo = build_mini_repo(tmp_path)

    rc = harness.main(["--repo-root", str(repo), "bridge-status"])

    out = capsys.readouterr().out
    assert rc == 0
    assert "Generated view" in out
    assert "# Bridge status - owner-shaped act pick-list" in out
