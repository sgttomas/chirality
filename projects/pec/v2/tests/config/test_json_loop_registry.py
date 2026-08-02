from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = V2_ROOT / "src"
CONFIG_ROOT = V2_ROOT / "config"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(SRC_ROOT))

from pec_v2.adapters.config.loop_registry import (  # noqa: E402
    JsonLoopRegistry,
    LoopRegistryConfigError,
)
from pec_v2.core.ports.loop_registry import RegisteredLoop  # noqa: E402


class JsonLoopRegistryTests(unittest.TestCase):
    def test_checked_in_default_has_exactly_the_pec_loop(self) -> None:
        loops = JsonLoopRegistry(CONFIG_ROOT / "loops.json").registered_loops()
        self.assertEqual(
            loops,
            (RegisteredLoop("pec", "_DomainEngines/pec/LOOP_INIT.md"),),
        )

    def test_schema_documents_every_field_and_the_exact_default(self) -> None:
        schema = json.loads((CONFIG_ROOT / "loops.schema.json").read_text(encoding="utf-8"))
        document = json.loads((CONFIG_ROOT / "loops.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(schema["properties"]["schema_version"]["const"], 1)
        self.assertEqual(document["schema_version"], 1)
        self.assertEqual(len(document["loops"]), 1)
        for field in ("schema_version", "loops"):
            self.assertTrue(schema["properties"][field]["description"])
        for field in ("loop_id", "loop_init_path"):
            self.assertTrue(schema["properties"]["loops"]["items"]["properties"][field]["description"])

    def test_missing_loop_id_is_rejected_with_location(self) -> None:
        with self.assertRaisesRegex(LoopRegistryConfigError, r"\$\.loops\[0\]\.loop_id"):
            JsonLoopRegistry(FIXTURES / "missing_loop_id.json").registered_loops()

    def test_duplicate_loop_id_is_rejected_with_location(self) -> None:
        with self.assertRaisesRegex(LoopRegistryConfigError, r"\$\.loops\[1\]\.loop_id"):
            JsonLoopRegistry(FIXTURES / "duplicate_loop_id.json").registered_loops()

    def test_malformed_json_is_rejected_with_line_and_column(self) -> None:
        with self.assertRaisesRegex(
            LoopRegistryConfigError, r"malformed\.json: malformed JSON at line [0-9]+, column [0-9]+"
        ):
            JsonLoopRegistry(FIXTURES / "malformed.json").registered_loops()

    def test_absent_file_is_rejected_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            missing = Path(temporary) / "absent.json"
            with self.assertRaisesRegex(LoopRegistryConfigError, r"absent\.json: configuration file does not exist"):
                JsonLoopRegistry(missing).registered_loops()

    def test_unreadable_path_is_rejected_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "not-a-file.json"
            directory.mkdir()
            with self.assertRaisesRegex(LoopRegistryConfigError, r"configuration file is unreadable"):
                JsonLoopRegistry(directory).registered_loops()

    def test_invalid_document_never_returns_partial_or_empty_set(self) -> None:
        for fixture in ("missing_loop_id.json", "duplicate_loop_id.json", "malformed.json"):
            with self.subTest(fixture=fixture):
                with self.assertRaises(LoopRegistryConfigError):
                    JsonLoopRegistry(FIXTURES / fixture).registered_loops()


if __name__ == "__main__":
    unittest.main()
