from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = V2_ROOT.parent
TOOL = V2_ROOT / "tools" / "check_service_core_posture.py"
SPEC = importlib.util.spec_from_file_location("service_core_posture_checker_registration", TOOL)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)


def evaluate(config: Path, workflow: Path, induce_tool_failure: bool = False):
    return CHECKER.evaluate(
        argparse.Namespace(
            config=str(config),
            workflow=str(workflow),
            project_root=str(PROJECT_ROOT),
            induce_tool_failure=induce_tool_failure,
        )
    )


class GateRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.config = PROJECT_ROOT / "v2" / "config" / "service_core_posture.json"
        self.workflow = PROJECT_ROOT / "software-workflow.json"

    def test_live_registration_and_release_binding_pass(self):
        result = evaluate(self.config, self.workflow)
        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["assertions"]["registration"], "PASS")
        self.assertEqual(result["release_force"], "PEC_RELEASE_BLOCKING")
        self.assertRegex(result["evaluated"]["core_tree_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(result["evaluated"]["config_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(result["evaluated"]["workflow_sha256"], r"^[0-9a-f]{64}$")

    def test_removed_registration_fails_closed(self):
        document = json.loads(self.workflow.read_text(encoding="utf-8"))
        document["checks"].pop("v2-core-posture")
        document["always_checks"].remove("v2-core-posture")
        document["path_rules"] = [
            rule for rule in document["path_rules"] if rule.get("checks") != ["v2-core-posture"]
        ]
        with tempfile.TemporaryDirectory() as directory:
            workflow = Path(directory) / "workflow.json"
            workflow.write_text(json.dumps(document), encoding="utf-8")
            result = evaluate(self.config, workflow)
        self.assertEqual(result["assertions"]["registration"], "BLOCK")
        self.assertTrue(
            any(item["code"] == "MISSING_OR_DISABLED_REGISTRATION" for item in result["findings"])
        )

    def test_disabled_registration_fails_closed(self):
        document = json.loads(self.workflow.read_text(encoding="utf-8"))
        document["checks"]["v2-core-posture"]["enabled"] = False
        with tempfile.TemporaryDirectory() as directory:
            workflow = Path(directory) / "workflow.json"
            workflow.write_text(json.dumps(document), encoding="utf-8")
            result = evaluate(self.config, workflow)
        self.assertEqual(result["assertions"]["registration"], "BLOCK")

    def test_absent_and_malformed_inputs_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            absent = evaluate(root / "absent.json", self.workflow)
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = evaluate(malformed_path, self.workflow)
        self.assertEqual(absent["verdict"], "BLOCK")
        self.assertEqual(malformed["verdict"], "BLOCK")
        self.assertTrue(all(value != "PASS" for value in absent["assertions"].values()))

    def test_absent_core_and_induced_tool_failure_fail_closed(self):
        document = json.loads(self.config.read_text(encoding="utf-8"))
        document["target"] = "v2/src/pec_v2/missing-core"
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "config.json"
            config.write_text(json.dumps(document), encoding="utf-8")
            absent_core = evaluate(config, self.workflow)
        induced = evaluate(self.config, self.workflow, induce_tool_failure=True)
        self.assertEqual(absent_core["verdict"], "BLOCK")
        self.assertEqual(induced["verdict"], "BLOCK")
        self.assertTrue(any(item["code"] == "EVALUATION_FAILURE" for item in induced["findings"]))


if __name__ == "__main__":
    unittest.main()
