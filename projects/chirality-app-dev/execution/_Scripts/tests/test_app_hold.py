#!/usr/bin/env python3
"""Candidate regression tests for APP-HOLD-1."""

from __future__ import annotations

import json
import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
FIXTURE = json.loads((HERE / "fixtures" / "expected_held.json").read_text())
ENTRY_FIXTURE = json.loads((HERE / "fixtures" / "entry_paths.json").read_text())


def resolve_layout(test_root: Path) -> dict[str, Path | str]:
    candidate = "_PROPOSALS" in test_root.parts
    git_probe = test_root.parent if candidate else test_root
    repo_root = Path(
        subprocess.run(
            ["git", "-C", str(git_probe), "rev-parse", "--show-toplevel"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        ).stdout.strip()
    )
    app_execution = repo_root / "projects" / "chirality-app-dev" / "execution"
    if candidate:
        proposal = test_root.parent
        return {
            "mode": "candidate",
            "repo_root": repo_root,
            "sow_root": app_execution,
            "tool": proposal / "tools" / "app_hold.py",
            "register": proposal / "APP_HOLD_REGISTER.csv",
        }
    return {
        "mode": "live",
        "repo_root": repo_root,
        "sow_root": app_execution,
        "tool": test_root.parent / "app_hold.py",
        "register": app_execution / "_Coordination" / "APP_HOLD_REGISTER.csv",
    }


LAYOUT = resolve_layout(HERE)
TOOL = Path(LAYOUT["tool"])
REPO_ROOT = Path(LAYOUT["repo_root"])
SOW_ROOT = Path(LAYOUT["sow_root"])
REGISTER = Path(LAYOUT["register"])

TOOL_SPEC = importlib.util.spec_from_file_location("app_hold_candidate", TOOL)
assert TOOL_SPEC and TOOL_SPEC.loader
TOOL_MODULE = importlib.util.module_from_spec(TOOL_SPEC)
TOOL_SPEC.loader.exec_module(TOOL_MODULE)


def invoke(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(TOOL),
            *arguments,
            "--repo-root",
            str(REPO_ROOT),
            "--sow-root",
            str(SOW_ROOT),
            "--register",
            str(REGISTER),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class AppHoldCandidateTests(unittest.TestCase):
    def test_live_scan_matches_expected_held_set(self) -> None:
        result = invoke("scan", "--require-register-match")
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "PASS")
        self.assertEqual(
            payload["held_deliverables"], FIXTURE["held_deliverables"]
        )
        self.assertEqual(payload["held_count"], 6)
        self.assertTrue(payload["register"]["match"])
        self.assertEqual(len(payload["scan_fingerprint_sha256"]), 64)

    def test_held_target_blocked_for_every_operation_and_entry_path(self) -> None:
        target = FIXTURE["held_deliverables"][0]
        for operation in ENTRY_FIXTURE["operations"]:
            for entry_path in ENTRY_FIXTURE["entry_paths"]:
                with self.subTest(operation=operation, entry_path=entry_path):
                    result = invoke(
                        "check",
                        "--operation",
                        operation,
                        "--entry-path",
                        entry_path,
                        "--target",
                        target,
                    )
                    self.assertEqual(result.returncode, 3, result.stderr or result.stdout)
                    payload = json.loads(result.stdout)
                    self.assertEqual(payload["verdict"], "BLOCK_APP_HOLD")
                    self.assertEqual(
                        payload["results"][0]["verdict"], "BLOCK_APP_HOLD"
                    )
                    self.assertEqual(
                        payload["results"][0]["hold_status"],
                        "REPAIR_VALIDATION_PENDING",
                    )

    def test_repair_pending_target_stays_blocked_after_basis_resolves(self) -> None:
        target = FIXTURE["held_deliverables"][0]
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        known = {row["deliverable_id"]: row for row in scan["contracts"]}
        known[target]["status"] = "CLEAR"
        known[target]["reason"] = "BASIS_RESOLVES"
        scan["contracts"] = list(known.values())
        scan["held_deliverables"] = [
            item for item in scan["held_deliverables"] if item != target
        ]
        scan["held_count"] -= 1

        comparison = TOOL_MODULE.compare_register(scan, REGISTER)
        self.assertTrue(comparison["match"], comparison)

        registered = {
            row["deliverable_id"]: row
            for row in TOOL_MODULE.load_register(REGISTER)
        }
        results = TOOL_MODULE.evaluate_targets(
            known,
            registered,
            operation="reliance",
            entry_path="OD6-G4:POST-REPIN-VALIDATION",
            targets=[target],
        )
        self.assertEqual(results[0]["contract_status"], "CLEAR")
        self.assertEqual(
            results[0]["hold_status"], "REPAIR_VALIDATION_PENDING"
        )
        self.assertEqual(results[0]["verdict"], "BLOCK_APP_HOLD")

    def test_scan_derived_held_state_cannot_survive_basis_resolution(self) -> None:
        target = FIXTURE["held_deliverables"][0]
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        for contract in scan["contracts"]:
            if contract["deliverable_id"] == target:
                contract["status"] = "CLEAR"
                contract["reason"] = "BASIS_RESOLVES"
        scan["held_deliverables"] = [
            item for item in scan["held_deliverables"] if item != target
        ]
        scan["held_count"] -= 1

        rows = TOOL_MODULE.load_register(REGISTER)
        for row in rows:
            if row["deliverable_id"] == target:
                row["status"] = "HELD"
                row["authority_basis"] = "D-APP-75"

        original_loader = TOOL_MODULE.load_register
        TOOL_MODULE.load_register = lambda _path: rows
        try:
            comparison = TOOL_MODULE.compare_register(scan, REGISTER)
        finally:
            TOOL_MODULE.load_register = original_loader

        self.assertFalse(comparison["match"])
        self.assertEqual(
            comparison["status_mismatches"],
            [
                {
                    "deliverable_id": target,
                    "scan": "CLEAR",
                    "register": "HELD",
                }
            ],
        )

    def test_unaffected_target_allowed(self) -> None:
        result = invoke(
            "check",
            "--operation",
            "dispatch",
            "--entry-path",
            "WORKING_ITEMS:PKG-03:RUN-POSITIVE-1",
            "--target",
            FIXTURE["unaffected_target"],
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "ALLOW")
        self.assertEqual(payload["results"][0]["verdict"], "ALLOW")
        self.assertEqual(len(payload["scan_fingerprint_sha256"]), 64)

    def test_mixed_fanin_dependency_set_rejected(self) -> None:
        result = invoke(
            "check",
            "--operation",
            "accepted-dependency-consumption",
            "--entry-path",
            "WORKING_ITEMS:FAN-IN:RUN-NEGATIVE-4",
            "--target",
            FIXTURE["unaffected_target"],
            "--target",
            FIXTURE["held_deliverables"][0],
        )
        self.assertEqual(result.returncode, 3, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "BLOCK_APP_HOLD")
        verdicts = {
            row["deliverable_id"]: row["verdict"] for row in payload["results"]
        }
        self.assertEqual(
            verdicts[FIXTURE["held_deliverables"][0]], "BLOCK_APP_HOLD"
        )
        self.assertEqual(verdicts[FIXTURE["unaffected_target"]], "ALLOW")

    def test_register_drift_fails_closed(self) -> None:
        drifted = HERE / "fixtures" / "APP_HOLD_REGISTER_DRIFT.csv"
        result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "scan",
                "--repo-root",
                str(REPO_ROOT),
                "--sow-root",
                str(SOW_ROOT),
                "--register",
                str(drifted),
                "--require-register-match",
                "--test-fixture-mode",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 4, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "BLOCK_REGISTER_DRIFT")
        self.assertEqual(
            payload["register"]["missing_from_register"], ["DEL-08-03"]
        )

    def test_no_generic_owner_exception_bypass_exists(self) -> None:
        result = invoke(
            "check",
            "--exceptions",
            "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md",
            "--operation",
            "dispatch",
            "--entry-path",
            "DIRECT_HUMAN_SESSION:RUN-NEGATIVE-5",
            "--target",
            FIXTURE["held_deliverables"][0],
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("unrecognized arguments: --exceptions", result.stderr)

    def test_candidate_and_live_layout_resolution(self) -> None:
        expected_mode = "candidate" if "_PROPOSALS" in HERE.parts else "live"
        self.assertEqual(LAYOUT["mode"], expected_mode)
        simulated_live = (
            REPO_ROOT
            / "projects"
            / "chirality-app-dev"
            / "execution"
            / "_Scripts"
            / "tests"
        )
        live = resolve_layout(simulated_live)
        self.assertEqual(live["mode"], "live")
        self.assertEqual(
            live["tool"],
            REPO_ROOT
            / "projects"
            / "chirality-app-dev"
            / "execution"
            / "_Scripts"
            / "app_hold.py",
        )
        self.assertEqual(
            live["register"],
            REPO_ROOT
            / "projects"
            / "chirality-app-dev"
            / "execution"
            / "_Coordination"
            / "APP_HOLD_REGISTER.csv",
        )

    def test_duplicate_front_matter_fails_closed(self) -> None:
        with self.assertRaises(TOOL_MODULE.HoldError):
            TOOL_MODULE.parse_front_matter(
                HERE / "fixtures" / "MALFORMED_DUPLICATE_FRONT_MATTER.md"
            )

    def test_malformed_register_header_fails_closed(self) -> None:
        malformed = HERE / "fixtures" / "MALFORMED_HOLD_REGISTER.csv"
        result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "scan",
                "--repo-root",
                str(REPO_ROOT),
                "--sow-root",
                str(SOW_ROOT),
                "--register",
                str(malformed),
                "--require-register-match",
                "--test-fixture-mode",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("invalid hold-register header", result.stderr)

    def test_preparation_only_authority_fails_closed(self) -> None:
        wrong_authority = (
            HERE / "fixtures" / "MALFORMED_HOLD_REGISTER_AUTHORITY.csv"
        )
        result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "scan",
                "--repo-root",
                str(REPO_ROOT),
                "--sow-root",
                str(SOW_ROOT),
                "--register",
                str(wrong_authority),
                "--require-register-match",
                "--test-fixture-mode",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("hold authority must be D-APP-75", result.stderr)

    def test_noncanonical_repo_root_fails_closed(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "scan",
                "--repo-root",
                str(REPO_ROOT / "projects"),
                "--sow-root",
                str(SOW_ROOT),
                "--register",
                str(REGISTER),
                "--require-register-match",
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("canonical Git top level", result.stderr)

    def test_output_escape_fails_before_write(self) -> None:
        forbidden = Path("/tmp/APP-HOLD-1-FORBIDDEN-OUTPUT.json")
        result = subprocess.run(
            [
                sys.executable,
                str(TOOL),
                "scan",
                "--repo-root",
                str(REPO_ROOT),
                "--sow-root",
                str(SOW_ROOT),
                "--register",
                str(REGISTER),
                "--require-register-match",
                "--output",
                str(forbidden),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("outside an allowed evidence root", result.stderr)
        self.assertFalse(forbidden.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
