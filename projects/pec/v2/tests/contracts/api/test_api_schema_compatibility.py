from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
BASELINE = HERE.parents[2] / "contracts" / "api" / "v1" / "schema.json"
FIXTURES = HERE / "fixtures"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def pointer(path: tuple[str, ...]) -> str:
    if not path:
        return "/"
    return "/" + "/".join(part.replace("~", "~0").replace("/", "~1") for part in path)


def compare_additive(baseline: Any, candidate: Any) -> list[str]:
    """Return located incompatibilities; an empty result is additive."""

    findings: list[str] = []

    def compare(expected: Any, actual: Any, path: tuple[str, ...]) -> None:
        location = pointer(path)
        if type(expected) is not type(actual):
            findings.append(
                f"{location}: published element type changed from "
                f"{type(expected).__name__} to {type(actual).__name__}"
            )
            return

        if isinstance(expected, dict):
            for key in expected:
                if key not in actual:
                    findings.append(f"{pointer(path + (key,))}: published element was removed")
                    continue
                compare(expected[key], actual[key], path + (key,))

            for key in actual.keys() - expected.keys():
                if path and path[-1] in {"$defs", "properties"}:
                    continue
                findings.append(
                    f"{pointer(path + (key,))}: new element is not classifiable as "
                    "a definition or optional property"
                )
            return

        if isinstance(expected, list):
            if expected != actual:
                findings.append(
                    f"{location}: published ordered values changed from "
                    f"{expected!r} to {actual!r}"
                )
            return

        if expected != actual:
            label = "published meaning" if path and path[-1] == "x-pec-meaning" else "published value"
            findings.append(f"{location}: {label} changed from {expected!r} to {actual!r}")

    compare(baseline, candidate, ())

    baseline_defs = baseline.get("$defs", {}) if isinstance(baseline, dict) else {}
    candidate_defs = candidate.get("$defs", {}) if isinstance(candidate, dict) else {}
    for definition_name, definition in candidate_defs.items():
        if definition_name in baseline_defs or not isinstance(definition, dict):
            continue
        if "x-pec-meaning" not in definition:
            findings.append(
                f"/$defs/{definition_name}: new definition lacks x-pec-meaning and fails closed"
            )

    def check_optional_additions(expected: Any, actual: Any, path: tuple[str, ...]) -> None:
        if not isinstance(expected, dict) or not isinstance(actual, dict):
            return
        expected_properties = expected.get("properties")
        actual_properties = actual.get("properties")
        if isinstance(expected_properties, dict) and isinstance(actual_properties, dict):
            added = actual_properties.keys() - expected_properties.keys()
            required = actual.get("required", [])
            if not isinstance(required, list):
                findings.append(f"{pointer(path + ('required',))}: required is not a list")
                required = []
            for name in sorted(added):
                prop_path = path + ("properties", name)
                if name in required:
                    findings.append(
                        f"{pointer(prop_path)}: new property is required rather than optional"
                    )
                prop_schema = actual_properties[name]
                if not isinstance(prop_schema, dict) or "x-pec-meaning" not in prop_schema:
                    findings.append(
                        f"{pointer(prop_path)}: new property lacks x-pec-meaning and fails closed"
                    )
        for key in expected.keys() & actual.keys():
            check_optional_additions(expected[key], actual[key], path + (key,))

    check_optional_additions(baseline, candidate, ())
    return findings


class ApiSchemaCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = load_json(BASELINE)

    def test_baseline_declares_draft_and_integer_version(self) -> None:
        self.assertEqual(self.baseline["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(self.baseline["api_schema_version"], 1)
        for name in ("CapabilityRequest", "CapabilityResponse"):
            version = self.baseline["$defs"][name]["properties"]["api_schema_version"]
            self.assertEqual(version["type"], "integer")
            self.assertEqual(version["const"], 1)

    def test_additive_candidate_passes(self) -> None:
        candidate = load_json(FIXTURES / "v1_additive_candidate.json")
        self.assertEqual(compare_additive(self.baseline, candidate), [])

    def test_removed_element_candidate_fails_with_location(self) -> None:
        candidate = load_json(FIXTURES / "v1_removed_element_candidate.json")
        findings = compare_additive(self.baseline, candidate)
        self.assertTrue(findings)
        self.assertTrue(
            any("/$defs/CapabilityRequest/properties/use_case" in finding for finding in findings),
            findings,
        )

    def test_meaning_changed_candidate_fails_with_location(self) -> None:
        candidate = load_json(FIXTURES / "v1_meaning_changed_candidate.json")
        findings = compare_additive(self.baseline, candidate)
        self.assertTrue(findings)
        self.assertTrue(
            any(
                "/$defs/CapabilityRequest/properties/capability/x-pec-meaning" in finding
                and "published meaning changed" in finding
                for finding in findings
            ),
            findings,
        )

    def test_unclassifiable_change_fails_closed(self) -> None:
        candidate = json.loads(json.dumps(self.baseline))
        candidate["unregistered_contract_surface"] = {}
        findings = compare_additive(self.baseline, candidate)
        self.assertTrue(any("not classifiable" in finding for finding in findings), findings)

    def test_new_required_property_is_not_additive(self) -> None:
        candidate = load_json(FIXTURES / "v1_additive_candidate.json")
        candidate["$defs"]["CapabilityRequest"]["required"].append("metadata")
        findings = compare_additive(self.baseline, candidate)
        self.assertTrue(any("required rather than optional" in finding for finding in findings), findings)


if __name__ == "__main__":
    unittest.main()
