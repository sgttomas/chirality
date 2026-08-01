"""Tests for taskmgmt v0 (scan/validate)."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import taskmgmt  # noqa: E402


def write_register(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=taskmgmt.CANONICAL_COLUMNS, quoting=csv.QUOTE_ALL,
            lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def good_row(**overrides) -> dict:
    row = {c: "" for c in taskmgmt.CANONICAL_COLUMNS}
    row.update(
        RegisterSchemaVersion="1.0", ActionItemID="TM-TEST-001", Title="t",
        Concern="c", SourceRef="a/b.md", SourceSha="0" * 40,
        CandidateRef="DIRECT", DomainLenses="Decisions", AssociatedWith="x",
        NoticeRef="NONE", ScaRef="NONE", Assignment="TBD", Priority="TBD",
        PriorityBasis="TBD", Status="OPEN", Opened="2026-07-31",
    )
    row.update(overrides)
    return row


def run_validate(root: Path, register: Path):
    return taskmgmt.validate_register(root, register)


class TestValidate:
    def test_pass_on_conforming_register(self, tmp_path):
        reg = tmp_path / "REGISTER.csv"
        write_register(reg, [
            good_row(),
            good_row(ActionItemID="TM-TEST-002", Status="DEFERRED",
                     Trigger="an event"),
            good_row(ActionItemID="TM-TEST-003", Status="CLOSED",
                     Disposition="OBE", EvidenceRef="e.md",
                     EvidenceSha="1" * 40, Closed="2026-07-31"),
            good_row(ActionItemID="TM-TEST-004", Status="ELEVATED",
                     ElevatedTo="TM-OTHER-001"),
        ])
        code, lines = run_validate(tmp_path, reg)
        assert code == 0, lines

    @pytest.mark.parametrize("overrides,needle", [
        (dict(Status="CLOSED", EvidenceRef="e", EvidenceSha="1" * 40,
              Closed="2026-07-31"), "valid Disposition"),
        (dict(Status="CLOSED", Disposition="OBE", EvidenceSha="1" * 40,
              Closed="2026-07-31"), "without EvidenceRef"),
        (dict(Status="CLOSED", Disposition="OBE", EvidenceRef="e",
              Closed="2026-07-31"), "without EvidenceSha"),
        (dict(Status="DEFERRED"), "DEFERRED without Trigger"),
        (dict(Status="ELEVATED"), "ELEVATED without ElevatedTo"),
        (dict(Status="IN_PROGRESS"), "Status"),
        (dict(Disposition="OBE"), "non-CLOSED"),
        (dict(ActionItemID="BADID"), "not TM-<LOOP>-<seq>"),
        (dict(SourceSha=""), "SourceSha empty"),
        (dict(Opened="July 31"), "not YYYY-MM-DD"),
    ])
    def test_block_on_rule_violation(self, tmp_path, overrides, needle):
        reg = tmp_path / "REGISTER.csv"
        write_register(reg, [good_row(**overrides)])
        code, lines = run_validate(tmp_path, reg)
        assert code == 1
        assert any(needle in line for line in lines), lines

    def test_block_on_duplicate_id(self, tmp_path):
        reg = tmp_path / "REGISTER.csv"
        write_register(reg, [good_row(), good_row()])
        code, lines = run_validate(tmp_path, reg)
        assert code == 1
        assert any("duplicate" in line for line in lines)

    def test_block_on_wrong_header(self, tmp_path):
        reg = tmp_path / "REGISTER.csv"
        reg.write_text("A,B,C\n1,2,3\n", encoding="utf-8")
        code, lines = run_validate(tmp_path, reg)
        assert code == 1
        assert any("header" in line for line in lines)

    def test_operational_on_missing_file(self, tmp_path):
        code, lines = run_validate(tmp_path, tmp_path / "nope.csv")
        assert code == 2


class TestScan:
    def build_tree(self, root: Path) -> None:
        co = root / "execution" / "_Coordination"
        (co / "_DECISIONS").mkdir(parents=True)
        (co / "_DECISIONS" / "_REGISTER.md").write_text(
            "| D-9 | thing | basis | AWAITING_RULING | link | note |\n"
            "| D-8 | done | basis | RULED | link | note |\n",
            encoding="utf-8")
        (co / "NOTICE_STATUS_X.csv").write_text(
            "NoticePath,SHA256,DeliveryState,AcknowledgementState,ClosureEffect\n"
            "a/NOTICE_ONE.md,ff,DELIVERED,TRACKED_OPEN,NON_GATING\n"
            "a/NOTICE_TWO.md,ee,DELIVERED,ACKNOWLEDGED,NON_GATING\n",
            encoding="utf-8")
        (co / "NOTICE_LOOSE.md").write_text("# loose notice\n", encoding="utf-8")
        ev = root / "execution" / "_Evaluation" / "SNAP"
        ev.mkdir(parents=True)
        (ev / "FINDINGS.csv").write_text(
            "FindingID,Concern,Status\nF-1,open thing,OPEN_ROUTED\n"
            "F-2,closed thing,CLOSED\n", encoding="utf-8")
        # canonical-vs-copy: same ledger copied into _Evaluation
        (ev / "NOTICE_STATUS_X.csv").write_text(
            (co / "NOTICE_STATUS_X.csv").read_text(), encoding="utf-8")
        pk = root / "domains" / "d" / "_Research" / "R1"
        pk.mkdir(parents=True)
        (pk / "Open_Questions.csv").write_text(
            "OpenQuestionID,Question,Status\nOQ-1,why,OPEN\nOQ-2,ok,RESOLVED\n",
            encoding="utf-8")
        (pk / "Amendment_Candidates.csv").write_text(
            "AmendmentID,Description,HumanRuling\nAC-1,change,TBD\n",
            encoding="utf-8")
        au = root / "projects" / "p" / "_audit"
        au.mkdir(parents=True)
        (au / "X_TBD_Register.csv").write_text(
            "TBDID,Question\nTBD-1,how\n", encoding="utf-8")
        (root / "projects" / "p" / "HANDOFF_STATE.md").write_text(
            "Remaining blockers: none.\n", encoding="utf-8")
        (root / "projects" / "p2").mkdir(parents=True)
        (root / "projects" / "p2" / "HANDOFF_STATE.md").write_text(
            "Remaining blockers: waiting on X.\n", encoding="utf-8")
        # excluded tree must not be scanned
        ex = root / "domains" / "d" / "_Decomposition" / "dispatch_briefs"
        ex.mkdir(parents=True)
        (ex / "FINDINGS.csv").write_text(
            "FindingID,Concern,Status\nF-X,noise,OPEN\n", encoding="utf-8")

    def test_scan_classes_dedup_and_exclusions(self, tmp_path):
        self.build_tree(tmp_path)
        out = tmp_path / "out.json"
        code, lines = taskmgmt.scan(
            tmp_path, tmp_path / "missing_register.csv", out)
        assert code == 0
        data = json.loads(out.read_text())
        counts = data["counts"]
        assert counts["decision-non-ruled"] == 1
        assert counts["notice-tracked-open"] == 2  # original + copy, pre-dedup
        assert data["dedup_dropped_copies"] == 1
        kept = [c for c in data["candidates"]
                if c["class"] == "notice-tracked-open"]
        assert len(kept) == 1
        assert "_Coordination" in kept[0]["source"]  # canonical wins
        assert counts["notice-not-in-ledger"] == 1
        assert counts["evaluation-finding-open"] == 1  # excluded tree unseen
        assert counts["packet-field-open"] == 2  # OQ-1 open + AC-1 TBD
        assert counts["tbd-register-row"] == 1
        assert counts["handoff-blocker"] == 1
        assert all(c["authority"] == "observed" for c in data["candidates"])

    def test_scan_marks_register_known_refs(self, tmp_path):
        self.build_tree(tmp_path)
        reg = tmp_path / "REGISTER.csv"
        write_register(reg, [good_row(
            SourceRef="projects/p/_audit/X_TBD_Register.csv row TBD-1")])
        out = tmp_path / "out.json"
        code, _ = taskmgmt.scan(tmp_path, reg, out)
        assert code == 0
        data = json.loads(out.read_text())
        tbd = [c for c in data["candidates"]
               if c["class"] == "tbd-register-row"]
        assert tbd and tbd[0]["known_to_register"] is True
