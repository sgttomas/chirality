#!/usr/bin/env python3
"""Candidate regression tests for APP-HOLD-1."""

from __future__ import annotations

import csv
import json
import os
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
FIXTURE = json.loads((HERE / "fixtures" / "expected_held.json").read_text())
ENTRY_FIXTURE = json.loads((HERE / "fixtures" / "entry_paths.json").read_text())
BOOTSTRAP_FIXTURE = json.loads(
    (HERE / "fixtures" / "bootstrap_expected.json").read_text()
)


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
            "record_kind": "HOLD",
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
            "allowed_operation": "NONE",
            "allowed_entry_paths": "NONE",
            "decomposition_sha256": "NONE",
            "companion_register_sha256": "NONE",
            "pointer_sha256": "NONE",
            "target_folder": "NONE",
            "allowed_scaffold_paths": "NONE",
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


class StructuralBootstrapTests(unittest.TestCase):
    def setUp(self) -> None:
        # Preserve D-APP-104 compatibility against its immutable proposal row;
        # the live row now governs the later PROJECT_SETUP initialization.
        self.register = SOW_ROOT / "_Coordination/_PROPOSALS/APP-HOLD-1_DEL-09-07_BOOTSTRAP_2026-09-04/APP_HOLD_REGISTER.csv"
        rows = TOOL_MODULE.load_register(self.register)
        _, bootstraps = TOOL_MODULE.partition_register_rows(rows)
        self.row = dict(bootstraps[BOOTSTRAP_FIXTURE["target"]])
        self.known = {
            row["deliverable_id"]: row
            for row in TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)["contracts"]
            if row["deliverable_id"] != BOOTSTRAP_FIXTURE["target"]
        }

    def fake_root(self) -> tempfile.TemporaryDirectory[str]:
        return tempfile.TemporaryDirectory(prefix="app-hold-bootstrap-test-")

    def patch_hashes(self, root: Path, wrong: str | None = None):
        expected = {
            (root / TOOL_MODULE.BOOTSTRAP_DECOMPOSITION_PATH).resolve():
                BOOTSTRAP_FIXTURE["decomposition_sha256"],
            (root / TOOL_MODULE.BOOTSTRAP_COMPANION_PATH).resolve():
                BOOTSTRAP_FIXTURE["companion_register_sha256"],
            (root / TOOL_MODULE.BOOTSTRAP_POINTER_PATH).resolve():
                BOOTSTRAP_FIXTURE["pointer_sha256"],
        }
        if wrong:
            expected[(root / wrong).resolve()] = "0" * 64

        def fake(path: Path) -> tuple[str | None, str | None]:
            return expected[path.resolve()], None

        return mock.patch.object(TOOL_MODULE, "_regular_file_sha256", side_effect=fake)

    def test_live_candidate_row_is_valid_but_dormant_on_preimage_basis(self) -> None:
        result = invoke("scan", "--require-register-match")
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["verdict"], "PASS")
        self.assertEqual(payload["register"]["active_hold_deliverables"], [])
        self.assertEqual(
            payload["register"]["structural_bootstrap_deliverables"],
            [],
        )
        admission = TOOL_MODULE.inspect_bootstrap_admission(REPO_ROOT, self.row, self.known)
        self.assertEqual(admission["state"], "INACTIVE")
        self.assertFalse(admission["conditions"]["pointer_preimage_hash_matches"])

    def test_live_preimage_basis_blocks_bootstrap_dispatch(self) -> None:
        payload = TOOL_MODULE.evaluate_bootstrap_target(
            REPO_ROOT, self.row, self.known, operation="dispatch",
            entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
        )
        self.assertEqual(payload["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")

    def test_exact_postimages_allow_both_tokens_with_absent_or_subset_folder(self) -> None:
        for subset in ((), ("_CONTEXT.md",), tuple(BOOTSTRAP_FIXTURE["allowed_scaffold_paths"])):
            with self.subTest(subset=subset), self.fake_root() as temporary:
                root = Path(temporary)
                folder = root / self.row["target_folder"]
                if subset:
                    folder.mkdir(parents=True)
                    for name in subset:
                        (folder / name).write_text("fixture\n", encoding="utf-8")
                with self.patch_hashes(root):
                    for token in BOOTSTRAP_FIXTURE["allowed_entry_paths"]:
                        result = TOOL_MODULE.evaluate_bootstrap_target(
                            root,
                            self.row,
                            self.known,
                            operation="dispatch",
                            entry_path=token,
                        )
                        self.assertEqual(result["verdict"], "ALLOW", result)
                        self.assertEqual(
                            result["admission_kind"], "STRUCTURAL_BOOTSTRAP"
                        )

    def test_wrong_operation_and_entry_token_fail_closed(self) -> None:
        with self.fake_root() as temporary:
            root = Path(temporary)
            with self.patch_hashes(root):
                wrong_operation = TOOL_MODULE.evaluate_bootstrap_target(
                    root,
                    self.row,
                    self.known,
                    operation="reliance",
                    entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
                )
                wrong_token = TOOL_MODULE.evaluate_bootstrap_target(
                    root,
                    self.row,
                    self.known,
                    operation="dispatch",
                    entry_path="SCA-APP-009:GATE5:PREPARATION:OTHER",
                )
        self.assertEqual(wrong_operation["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
        self.assertFalse(wrong_operation["operation_matches"])
        self.assertEqual(wrong_token["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
        self.assertFalse(wrong_token["entry_path_matches"])

    def test_each_authority_or_pointer_hash_drift_expires_admission(self) -> None:
        for path, condition in (
            (TOOL_MODULE.BOOTSTRAP_DECOMPOSITION_PATH, "decomposition_hash_matches"),
            (TOOL_MODULE.BOOTSTRAP_COMPANION_PATH, "companion_register_hash_matches"),
            (TOOL_MODULE.BOOTSTRAP_POINTER_PATH, "pointer_preimage_hash_matches"),
        ):
            with self.subTest(path=path), self.fake_root() as temporary:
                root = Path(temporary)
                with self.patch_hashes(root, wrong=path):
                    result = TOOL_MODULE.evaluate_bootstrap_target(
                        root,
                        self.row,
                        self.known,
                        operation="dispatch",
                        entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
                    )
                self.assertEqual(result["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
                self.assertFalse(result["bootstrap"]["conditions"][condition])

    def test_scope_of_work_appearance_expires_admission(self) -> None:
        with self.fake_root() as temporary:
            root = Path(temporary)
            sow = root / self.row["sow_path"]
            sow.parent.mkdir(parents=True)
            sow.write_text("not consumed\n", encoding="utf-8")
            with self.patch_hashes(root):
                result = TOOL_MODULE.evaluate_bootstrap_target(
                    root,
                    self.row,
                    self.known,
                    operation="dispatch",
                    entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
                )
        self.assertEqual(result["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
        self.assertFalse(result["bootstrap"]["conditions"]["scope_of_work_absent"])

    def test_scope_of_work_scan_collision_is_register_drift(self) -> None:
        scan = TOOL_MODULE.scan_corpus(REPO_ROOT, SOW_ROOT)
        scan["contracts"] = [r for r in scan["contracts"] if r["deliverable_id"] != "DEL-09-07"]
        scan["contracts"].append(
            {
                "deliverable_id": BOOTSTRAP_FIXTURE["target"],
                "package_id": BOOTSTRAP_FIXTURE["package_id"],
                "sow_path": self.row["sow_path"],
                "decomposition_basis": "fixture@307addf",
                "basis_commit": "307addf",
                "status": "CLEAR",
            }
        )
        comparison = TOOL_MODULE.compare_register(scan, self.register)
        self.assertFalse(comparison["match"])
        self.assertEqual(
            comparison["bootstrap_contract_collisions"],
            [BOOTSTRAP_FIXTURE["target"]],
        )

    def test_extra_nested_and_symlink_folder_content_fail_closed(self) -> None:
        cases = ("extra", "nested", "symlink")
        for case in cases:
            with self.subTest(case=case), self.fake_root() as temporary:
                root = Path(temporary)
                folder = root / self.row["target_folder"]
                folder.mkdir(parents=True)
                if case == "extra":
                    (folder / "MEMORY.md").write_text("extra\n", encoding="utf-8")
                elif case == "nested":
                    (folder / "_CONTEXT.md").mkdir()
                else:
                    (folder / "target").write_text("target\n", encoding="utf-8")
                    (folder / "_CONTEXT.md").symlink_to(folder / "target")
                with self.patch_hashes(root):
                    result = TOOL_MODULE.evaluate_bootstrap_target(
                        root,
                        self.row,
                        self.known,
                        operation="dispatch",
                        entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
                    )
                self.assertEqual(result["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
                self.assertTrue(result["bootstrap"]["folder_errors"])

    def test_symlink_target_folder_fails_closed(self) -> None:
        with self.fake_root() as temporary:
            root = Path(temporary)
            real = root / "real"
            real.mkdir()
            folder = root / self.row["target_folder"]
            folder.parent.mkdir(parents=True)
            folder.symlink_to(real, target_is_directory=True)
            with self.patch_hashes(root):
                result = TOOL_MODULE.evaluate_bootstrap_target(
                    root,
                    self.row,
                    self.known,
                    operation="dispatch",
                    entry_path=BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
                )
        self.assertEqual(result["verdict"], "BLOCK_STRUCTURAL_BOOTSTRAP")
        self.assertIn("TARGET_FOLDER_SYMLINK", result["bootstrap"]["folder_errors"])

    def test_authority_symlink_is_not_hashed(self) -> None:
        with self.fake_root() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.write_text("authority\n", encoding="utf-8")
            link = root / "link"
            link.symlink_to(source)
            actual, error = TOOL_MODULE._regular_file_sha256(link)
        self.assertIsNone(actual)
        self.assertIsNotNone(error)

    def test_wrong_target_package_or_row_constant_is_rejected(self) -> None:
        mutations = {
            "deliverable_id": "DEL-09-08",
            "package_id": "PKG-08",
            "sow_path": "wrong/ScopeOfWork.md",
            "allowed_operation": "reliance",
            "allowed_entry_paths": "OTHER",
            "decomposition_sha256": "0" * 64,
            "companion_register_sha256": "0" * 64,
            "pointer_sha256": "0" * 64,
            "target_folder": "wrong",
            "allowed_scaffold_paths": "_CONTEXT.md|ScopeOfWork.md",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                row = dict(self.row)
                row[field] = value
                with self.assertRaises(TOOL_MODULE.HoldError):
                    TOOL_MODULE._validate_bootstrap_row(row)

    def test_duplicate_bootstrap_or_hold_collision_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="app-hold-register-test-") as temporary:
            path = Path(temporary) / "register.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=TOOL_MODULE.REGISTER_FIELDS)
                writer.writeheader()
                writer.writerow(self.row)
                writer.writerow(self.row)
            with self.assertRaises(TOOL_MODULE.HoldError):
                TOOL_MODULE.load_register(path)

    def test_unknown_nonbootstrap_target_stays_fail_closed(self) -> None:
        result = invoke(
            "check",
            "--operation",
            "dispatch",
            "--entry-path",
            BOOTSTRAP_FIXTURE["allowed_entry_paths"][0],
            "--target",
            "DEL-09-99",
        )
        self.assertEqual(result.returncode, 2, result.stderr or result.stdout)
        self.assertIn("unknown target deliverables", result.stderr)


class SowInitializationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="app-hold-init-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.row = TOOL_MODULE.load_register(REGISTER)[0]
        self.folder = self.root / TOOL_MODULE.BOOTSTRAP_TARGET_FOLDER
        self.folder.mkdir(parents=True)
        for relative in (
            TOOL_MODULE.BOOTSTRAP_DECOMPOSITION_PATH,
            TOOL_MODULE.BOOTSTRAP_COMPANION_PATH,
            TOOL_MODULE.BOOTSTRAP_POINTER_PATH,
            *(f"{TOOL_MODULE.BOOTSTRAP_TARGET_FOLDER}/{name}" for name in TOOL_MODULE.INIT_SCAFFOLD_HASHES),
            REGISTER.relative_to(REPO_ROOT).as_posix(),
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if relative == REGISTER.relative_to(REPO_ROOT).as_posix():
                target.write_bytes(REGISTER.read_bytes())
            else:
                # Keep transition tests independent of later accepted source
                # or scaffold changes after the real contract is initialized.
                target.write_bytes(subprocess.check_output([
                    "git", "-C", str(REPO_ROOT), "show",
                    f"95b5687a7c9a4c6fe6e655f628495dec08ce04d8:{relative}",
                ]))
        for arguments in (("init", "-q"), ("add", "."),
                          ("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "fixture")):
            subprocess.run(["git", "-C", str(self.root), *arguments], check=True, capture_output=True)
        self.basis = subprocess.check_output(["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()
        other = self.root / "projects/chirality-app-dev/execution/PKG-99/DEL-99-01/ScopeOfWork.md"
        other.parent.mkdir(parents=True)
        other.write_text(self.contract("DEL-99-01", "PKG-99"))

    def contract(self, target="DEL-09-07", package="PKG-09", basis=None):
        return (f"---\ndeliverable_id: {target}\npackage_id: {package}\n"
                f"decomposition_basis: {TOOL_MODULE.BOOTSTRAP_DECOMPOSITION_PATH}@{basis or self.basis}\n---\n")

    def check(self, operation="dispatch", token=TOOL_MODULE.INIT_ENTRY_PATH):
        args = TOOL_MODULE.build_parser().parse_args([
            "check", "--repo-root", str(self.root), "--operation", operation,
            "--entry-path", token, "--target", "DEL-09-07",
        ])
        with mock.patch.object(TOOL_MODULE, "write_json") as output:
            code = TOOL_MODULE.command_check(args)
        return code, output.call_args.args[0]

    def test_exact_init_and_run_records_allowed(self):
        records = self.folder / "_run_records/INIT"
        records.mkdir(parents=True)
        (records / "brief.md").write_text("fixture evidence")
        code, result = self.check()
        self.assertEqual(code, 0, result)
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["results"][0]["admission_kind"], "SOW_INITIALIZATION")

    def test_wrong_operation_or_token_blocked(self):
        for operation, token in (("reliance", TOOL_MODULE.INIT_ENTRY_PATH),
                                 ("dispatch", "PROJECT_SETUP:SCOPE_OF_WORK:VERIFY"),
                                 ("checking-promotion", TOOL_MODULE.INIT_ENTRY_PATH),
                                 ("accepted-dependency-consumption", TOOL_MODULE.INIT_ENTRY_PATH)):
            with self.subTest(operation=operation, token=token):
                self.assertEqual(self.check(operation, token)[0], 3)

    def test_each_source_drift_blocks(self):
        paths = [self.root / p for p in (TOOL_MODULE.BOOTSTRAP_DECOMPOSITION_PATH,
                 TOOL_MODULE.BOOTSTRAP_COMPANION_PATH, TOOL_MODULE.BOOTSTRAP_POINTER_PATH)]
        paths += [self.folder / name for name in TOOL_MODULE.INIT_SCAFFOLD_HASHES]
        for path in paths:
            with self.subTest(path=path):
                original = path.read_bytes()
                path.write_bytes(original + b"drift")
                self.assertEqual(self.check()[0], 3)
                path.write_bytes(original)

    def test_missing_extra_and_non_directory_run_records_block(self):
        path = self.folder / "_CONTEXT.md"
        original = path.read_bytes()
        path.unlink()
        self.assertEqual(self.check()[0], 3)
        path.write_bytes(original)
        for name in ("extra.md", "_run_records"):
            path = self.folder / name
            path.write_text("extra")
            self.assertEqual(self.check()[0], 3)
            path.unlink()

    def test_symlink_sources_ancestors_and_run_records_block(self):
        for path in (self.folder / "_CONTEXT.md", self.folder.parent,
                     (self.root / TOOL_MODULE.BOOTSTRAP_POINTER_PATH).parent):
            with self.subTest(path=path):
                moved = path.with_name(path.name + "-real")
                path.rename(moved)
                path.symlink_to(moved, target_is_directory=moved.is_dir())
                self.assertEqual(self.check()[0], 3)
                path.unlink()
                moved.rename(path)
        records = self.folder / "_run_records"
        records.mkdir()
        (records / "escape").symlink_to(self.root)
        self.assertEqual(self.check()[0], 3)

    def test_fifo_source_rejected_without_blocking(self):
        path = self.folder / "_CONTEXT.md"
        path.unlink()
        os.mkfifo(path)
        self.assertEqual(self.check()[0], 3)

    def test_valid_sow_consumes_admission_and_allows_ordinary_verifier(self):
        (self.folder / "ScopeOfWork.md").write_text(self.contract())
        code, result = self.check(token="PROJECT_SETUP:SCOPE_OF_WORK:VERIFY")
        self.assertEqual(code, 0, result)
        self.assertEqual(len(result["results"]), 1)
        self.assertNotIn("admission_kind", result["results"][0])
        self.assertEqual(result["results"][0]["contract_status"], "CLEAR")
        comparison = TOOL_MODULE.compare_register(
            TOOL_MODULE.scan_corpus(self.root, TOOL_MODULE.default_paths(self.root)[0]),
            TOOL_MODULE.default_paths(self.root)[1])
        self.assertEqual(comparison["sow_initialization_admissions"][0]["state"], "CONSUMED")

    def test_held_sow_blocks_even_with_initializer_row(self):
        (self.folder / "ScopeOfWork.md").write_text(self.contract(basis="0" * 40))
        code, result = self.check()
        self.assertEqual(code, 4)
        self.assertEqual(result["register"]["missing_from_register"], ["DEL-09-07"])

    def test_malformed_sow_and_symlink_sow_block(self):
        sow = self.folder / "ScopeOfWork.md"
        sow.write_text("malformed")
        with self.assertRaises(TOOL_MODULE.HoldError):
            self.check()
        sow.unlink()
        os.mkfifo(sow)
        with self.assertRaises(TOOL_MODULE.HoldError):
            self.check()
        sow.unlink()
        source = self.root / "source.md"
        source.write_text(self.contract())
        sow.symlink_to(source)
        with self.assertRaises(TOOL_MODULE.HoldError):
            self.check()

    def test_known_target_wrong_package_or_path_blocks(self):
        sow = self.folder / "ScopeOfWork.md"
        sow.write_text(self.contract(package="PKG-08"))
        self.assertEqual(self.check()[0], 4)
        sow.write_text(self.contract())
        sow.rename(self.folder.parent / "ScopeOfWork.md")
        self.assertEqual(self.check()[0], 4)

    def test_row_tampering_fails_closed(self):
        for field, value in (("target_folder", "../escape"), ("allowed_entry_paths", "OTHER"),
                             ("package_id", "PKG-08"), ("pointer_sha256", "0" * 64)):
            row = dict(self.row, **{field: value})
            with self.subTest(field=field), self.assertRaises(TOOL_MODULE.HoldError):
                TOOL_MODULE._validate_initialization_row(row)


if __name__ == "__main__":
    unittest.main(verbosity=2)
