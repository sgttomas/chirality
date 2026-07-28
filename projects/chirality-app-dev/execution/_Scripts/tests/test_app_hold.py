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
            payload["held_deliverables"], FIXTURE["scan_held_deliverables"]
        )
        self.assertEqual(payload["held_count"], 0)
        self.assertTrue(payload["register"]["match"])
        self.assertEqual(
            payload["register"]["missing_repair_pending_from_register"], []
        )
        self.assertEqual(payload["register"]["active_hold_deliverables"], [])
        self.assertEqual(len(payload["scan_fingerprint_sha256"]), 64)

    def test_released_targets_allowed_for_every_operation_and_entry_path(self) -> None:
        for target in FIXTURE["released_deliverables"]:
            for operation in ENTRY_FIXTURE["operations"]:
                for entry_path in ENTRY_FIXTURE["entry_paths"]:
                    with self.subTest(
                        target=target,
                        operation=operation,
                        entry_path=entry_path,
                    ):
                        result = invoke(
                            "check",
                            "--operation",
                            operation,
                            "--entry-path",
                            entry_path,
                            "--target",
                            target,
                        )
                        self.assertEqual(
                            result.returncode, 0, result.stderr or result.stdout
                        )
                        payload = json.loads(result.stdout)
                        self.assertEqual(payload["verdict"], "ALLOW")
                        self.assertEqual(payload["results"][0]["verdict"], "ALLOW")
                        self.assertEqual(
                            payload["results"][0]["hold_status"], "NOT_HELD"
                        )

    def test_released_target_cannot_be_reactivated_by_register_only(self) -> None:
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
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn(
            "released target cannot appear in the active hold register",
            result.stderr,
        )

    def test_released_target_is_clear_and_allowed(self) -> None:
        target = FIXTURE["released_deliverables"][0]
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        known = {row["deliverable_id"]: row for row in scan["contracts"]}
        self.assertEqual(known[target]["status"], "CLEAR")
        comparison = TOOL_MODULE.compare_register(scan, REGISTER)
        self.assertTrue(comparison["match"], comparison)
        results = TOOL_MODULE.evaluate_targets(
            known,
            {},
            operation="reliance",
            entry_path="OD6-G5:POST-RELEASE-VALIDATION",
            targets=[target],
        )
        self.assertEqual(results[0]["contract_status"], "CLEAR")
        self.assertEqual(results[0]["hold_status"], "NOT_HELD")
        self.assertEqual(results[0]["verdict"], "ALLOW")

    def test_scan_derived_held_target_missing_register_fails_closed(self) -> None:
        target = FIXTURE["unaffected_target"]
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        for contract in scan["contracts"]:
            if contract["deliverable_id"] == target:
                contract["status"] = "HELD"
                contract["reason"] = "SIMULATED_UNRESOLVABLE_BASIS"
        scan["held_deliverables"] = [target]
        scan["held_count"] = 1
        comparison = TOOL_MODULE.compare_register(scan, REGISTER)
        self.assertFalse(comparison["match"])
        self.assertEqual(comparison["missing_from_register"], [target])

    def test_scan_derived_held_state_cannot_survive_basis_resolution(self) -> None:
        target = FIXTURE["unaffected_target"]
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        known = {row["deliverable_id"]: row for row in scan["contracts"]}
        row = {
            "hold_id": f"APP-HOLD-1-{target}",
            "deliverable_id": target,
            "package_id": known[target]["package_id"],
            "sow_path": known[target]["sow_path"],
            "decomposition_basis": known[target]["decomposition_basis"],
            "basis_commit": known[target]["basis_commit"],
            "status": "HELD",
            "prohibited_operations": "|".join(TOOL_MODULE.OPERATIONS),
            "entry_path_scope": "ANY",
            "repin_posture": "NO_REPIN",
            "authority_basis": "D-APP-75",
        }
        original_loader = TOOL_MODULE.load_register
        TOOL_MODULE.load_register = lambda _path: [row]
        try:
            comparison = TOOL_MODULE.compare_register(scan, REGISTER)
        finally:
            TOOL_MODULE.load_register = original_loader
        self.assertFalse(comparison["match"])
        self.assertEqual(
            comparison["status_mismatches"],
            [{"deliverable_id": target, "scan": "CLEAR", "register": "HELD"}],
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

    def test_mixed_fanin_dependency_set_allowed_after_release(self) -> None:
        released = FIXTURE["released_deliverables"][0]
        result = invoke(
            "check",
            "--operation",
            "accepted-dependency-consumption",
            "--entry-path",
            "WORKING_ITEMS:FAN-IN:RUN-POSITIVE-2",
            "--target",
            FIXTURE["unaffected_target"],
            "--target",
            released,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "ALLOW")
        self.assertEqual(
            {row["deliverable_id"]: row["verdict"] for row in payload["results"]},
            {FIXTURE["unaffected_target"]: "ALLOW", released: "ALLOW"},
        )

    def test_no_generic_owner_exception_bypass_exists(self) -> None:
        result = invoke(
            "check",
            "--exceptions",
            "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-81_RULING_2026-07-28.md",
            "--operation",
            "dispatch",
            "--entry-path",
            "DIRECT_HUMAN_SESSION:RUN-NEGATIVE-5",
            "--target",
            FIXTURE["released_deliverables"][0],
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
