#!/usr/bin/env python3
"""Deterministic tests for PEC-HOLD-001 preflight."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOOL = HERE.parent / "pec_reliance_hold.py"
TARGET = (
    "execution/PKG-00_Architecture_Runway_Contracts/1_Working/"
    "DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md"
)
REGISTER = (
    "HoldID,Status,TargetPath,TargetClauses,ProhibitedActs,AllowedActs,"
    "Authority,ReleaseRule\n"
    f"PEC-HOLD-001,ACTIVE,{TARGET},CLM-005|REQ-004,"
    "\"rely for production|dispatch for production|promote|consume\","
    "\"historical read-only inspection|exact correction preparation|candidate validation\","
    "D-PEC-67,\"separate owner act\"\n"
)


class HoldTests(unittest.TestCase):
    def run_gate(self, operation: str, clause: str = "CLM-005") -> subprocess.CompletedProcess:
        with tempfile.TemporaryDirectory() as directory:
            register = Path(directory) / "holds.csv"
            register.write_text(REGISTER, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(TOOL),
                    "--register",
                    str(register),
                    "--target",
                    TARGET,
                    "--clause",
                    clause,
                    "--operation",
                    operation,
                ],
                capture_output=True,
                text=True,
            )

    def test_production_reliance_blocks(self) -> None:
        self.assertEqual(self.run_gate("rely-for-production").returncode, 4)

    def test_dispatch_blocks(self) -> None:
        self.assertEqual(self.run_gate("dispatch-for-production").returncode, 4)

    def test_promotion_blocks(self) -> None:
        self.assertEqual(self.run_gate("promote").returncode, 4)

    def test_consumption_blocks(self) -> None:
        self.assertEqual(self.run_gate("consume").returncode, 4)

    def test_correction_preparation_allowed(self) -> None:
        self.assertEqual(self.run_gate("exact-correction-preparation").returncode, 0)

    def test_historical_inspection_allowed(self) -> None:
        self.assertEqual(self.run_gate("historical-read-only-inspection").returncode, 0)

    def test_unrelated_clause_allowed(self) -> None:
        self.assertEqual(self.run_gate("consume", "CLM-999").returncode, 0)


if __name__ == "__main__":
    unittest.main()
