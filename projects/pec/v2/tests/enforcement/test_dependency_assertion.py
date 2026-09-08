from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = V2_ROOT.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "dependency"
TOOL = V2_ROOT / "tools" / "check_service_core_posture.py"
SPEC = importlib.util.spec_from_file_location("service_core_posture_checker_dependency", TOOL)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)


def evaluate_fixture(name: str, admitted: list[str] | None = None):
    root = FIXTURES / name
    with tempfile.TemporaryDirectory() as directory:
        config = Path(directory) / "config.json"
        config.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "target": "core",
                    "pec_local_source_root": ".",
                    "workspace_runtime_contract_packages": admitted or [],
                }
            ),
            encoding="utf-8",
        )
        return CHECKER.evaluate(
            argparse.Namespace(
                config=str(config),
                workflow=str(PROJECT_ROOT / "software-workflow.json"),
                project_root=str(root),
                induce_tool_failure=False,
            )
        )


def evaluate_source(source: str, admitted: list[str] | None = None):
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        core = root / "core"
        core.mkdir()
        (core / "app.py").write_text(source, encoding="utf-8")
        config = root / "config.json"
        config.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "target": "core",
                    "pec_local_source_root": ".",
                    "workspace_runtime_contract_packages": admitted or [],
                }
            ),
            encoding="utf-8",
        )
        return CHECKER.evaluate(
            argparse.Namespace(
                config=str(config),
                workflow=str(PROJECT_ROOT / "software-workflow.json"),
                project_root=str(root),
                induce_tool_failure=False,
            )
        )


class DependencyAssertionTests(unittest.TestCase):
    def test_conforming_standard_library_fixture_passes(self):
        result = evaluate_fixture("conforming")
        self.assertEqual(result["assertions"]["dependency"], "PASS")

    def test_explicit_workspace_contract_fixture_passes(self):
        result = evaluate_fixture("workspace_contract", ["chirality_contracts"])
        self.assertEqual(result["assertions"]["dependency"], "PASS")

    def test_direct_third_party_dependency_fails_with_location(self):
        result = evaluate_fixture("third_party_direct")
        findings = [item for item in result["findings"] if item["assertion"] == "dependency"]
        self.assertEqual(result["assertions"]["dependency"], "BLOCK")
        self.assertTrue(any(item["code"] == "THIRD_PARTY_RUNTIME_DEPENDENCY" for item in findings))
        self.assertTrue(any(item.get("dependency") == "requests" for item in findings))
        self.assertTrue(all(item.get("importer") and item.get("line") for item in findings))

    def test_transitive_third_party_dependency_fails_with_importer(self):
        result = evaluate_fixture("third_party_transitive")
        findings = [item for item in result["findings"] if item["assertion"] == "dependency"]
        self.assertEqual(result["assertions"]["dependency"], "BLOCK")
        self.assertTrue(any(item.get("dependency") == "yaml" for item in findings))
        self.assertTrue(any("core/helper.py" in item.get("importer", "") for item in findings))

    def test_unclassifiable_dynamic_import_fails_closed(self):
        result = evaluate_source("module = __import__(name)\n")
        self.assertTrue(
            any(item["code"] == "UNCLASSIFIABLE_DYNAMIC_IMPORT" for item in result["findings"])
        )

    def test_import_derived_dynamic_callable_aliases_fail_once_with_location(self):
        exact_source = 'from importlib import import_module as load\nload("requests")\n'
        self.assertEqual(
            hashlib.sha256(exact_source.encode("utf-8")).hexdigest(),
            "b9bf8faa1bc575f9e5ffe3fb680a7bccc03c57681612fc94931f5666304eeeb2",
        )
        cases = {
            "exact_aliased_from_import": exact_source,
            "module_alias": 'import importlib as lib\nlib.import_module("requests")\n',
            "unaliased_from_import": 'from importlib import import_module\nimport_module("requests")\n',
            "assignment_alias": (
                "from importlib import import_module\n"
                "load = import_module\n"
                'load("requests")\n'
            ),
        }
        for name, source in cases.items():
            with self.subTest(name=name):
                result = evaluate_source(source)
                findings = [
                    item
                    for item in result["findings"]
                    if item["code"] == "UNCLASSIFIABLE_DYNAMIC_IMPORT"
                ]
                self.assertEqual(result["assertions"]["dependency"], "BLOCK")
                self.assertEqual(len(findings), 1)
                self.assertEqual(findings[0]["dependency"], "importlib.import_module")
                self.assertEqual(findings[0]["importer"], "core/app.py")
                self.assertEqual(findings[0]["line"], len(source.splitlines()))

    def test_recognized_dynamic_imports_remain_blocked_for_every_argument_class(self):
        source = (
            "import importlib\n"
            'importlib.import_module("json")\n'
            'importlib.import_module("chirality_contracts")\n'
            "importlib.import_module(module_name)\n"
        )
        result = evaluate_source(source, ["chirality_contracts"])
        findings = [
            item for item in result["findings"] if item["code"] == "UNCLASSIFIABLE_DYNAMIC_IMPORT"
        ]
        self.assertEqual(result["assertions"]["dependency"], "BLOCK")
        self.assertEqual([item["line"] for item in findings], [2, 3, 4])
        self.assertTrue(all(item["dependency"] == "importlib.import_module" for item in findings))

    def test_static_controls_and_unrelated_local_callable_are_not_newly_blocked(self):
        sources = {
            "stdlib": "import json\n",
            "workspace": "import chirality_contracts\n",
            "unrelated_callable": (
                "def load(name):\n"
                "    return name\n"
                'load("requests")\n'
            ),
        }
        for name, source in sources.items():
            with self.subTest(name=name):
                result = evaluate_source(source, ["chirality_contracts"])
                self.assertEqual(result["assertions"]["dependency"], "PASS")


if __name__ == "__main__":
    unittest.main()
