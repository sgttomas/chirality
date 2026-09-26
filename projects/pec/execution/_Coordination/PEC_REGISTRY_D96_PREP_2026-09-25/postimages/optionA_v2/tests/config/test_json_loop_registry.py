from __future__ import annotations

import copy
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
    FEED_PROFILE_SURFACES,
    FEED_PROFILE_VERSIONS,
    JsonLoopRegistry,
    LoopRegistryConfigError,
)
from pec_v2.core.ports.loop_registry import (  # noqa: E402
    FeedProfile,
    FeedProfileState,
    RegisteredLoop,
)


PEC_LOOP_INIT = "projects/pec/loop/LOOP_INIT.md"
PEC_AGENTS = "projects/pec/AGENTS.md"
D_PEC_94 = (
    "projects/pec/execution/_Coordination/_DECISIONS/"
    "D-PEC-94_owner_direction_loop_migration_2026-09-25.md"
)


def valid_document() -> dict:
    return {
        "schema_version": 2,
        "loops": [
            {
                "loop_id": "pec",
                "loop_init_path": PEC_LOOP_INIT,
                "feed_profiles": [
                    {"profile": "shared-dev-loop", "version": 1, "state": "live", "basis": D_PEC_94},
                    {"profile": "remaining-items", "version": 1, "state": "live", "basis": PEC_AGENTS},
                    {"profile": "loop-receipts-ledger", "version": 1, "state": "historical", "basis": PEC_AGENTS},
                    {"profile": "agentruns-json", "version": 1, "state": "historical", "basis": D_PEC_94},
                ],
            }
        ],
    }


class JsonLoopRegistryTests(unittest.TestCase):
    def load(self, document: object) -> tuple[RegisteredLoop, ...]:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "candidate.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            return JsonLoopRegistry(path).registered_loops()

    def test_checked_in_default_has_exactly_the_pec_loop(self) -> None:
        loops = JsonLoopRegistry(CONFIG_ROOT / "loops.json").registered_loops()
        self.assertEqual(
            loops,
            (
                RegisteredLoop(
                    "pec",
                    PEC_LOOP_INIT,
                    (
                        FeedProfile("shared-dev-loop", 1, FeedProfileState.LIVE, D_PEC_94),
                        FeedProfile("remaining-items", 1, FeedProfileState.LIVE, PEC_AGENTS),
                        FeedProfile("loop-receipts-ledger", 1, FeedProfileState.HISTORICAL, PEC_AGENTS),
                        FeedProfile("agentruns-json", 1, FeedProfileState.HISTORICAL, D_PEC_94),
                    ),
                ),
            ),
        )

    def test_schema_documents_every_field_and_the_exact_default(self) -> None:
        schema = json.loads((CONFIG_ROOT / "loops.schema.json").read_text(encoding="utf-8"))
        document = json.loads((CONFIG_ROOT / "loops.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(schema["$id"], "https://chirality.local/pec/v2/config/loops.schema.v2.json")
        self.assertEqual(schema["properties"]["schema_version"]["const"], 2)
        self.assertEqual(document["schema_version"], 2)
        self.assertEqual(len(document["loops"]), 1)
        for field in ("schema_version", "loops"):
            self.assertTrue(schema["properties"][field]["description"])
        row = schema["properties"]["loops"]["items"]
        self.assertEqual(sorted(row["required"]), ["feed_profiles", "loop_id", "loop_init_path"])
        for field in ("loop_id", "loop_init_path", "feed_profiles"):
            self.assertTrue(row["properties"][field]["description"])
        entry = row["properties"]["feed_profiles"]["items"]
        self.assertFalse(entry["additionalProperties"])
        self.assertEqual(sorted(entry["required"]), ["basis", "profile", "state", "version"])
        for field in ("profile", "version", "state", "basis"):
            self.assertTrue(entry["properties"][field]["description"])
        declared = {option["const"]: option["description"] for option in entry["properties"]["profile"]["oneOf"]}
        self.assertEqual(set(declared), set(FEED_PROFILE_VERSIONS))
        self.assertEqual(set(FEED_PROFILE_SURFACES), set(FEED_PROFILE_VERSIONS))
        for profile, description in declared.items():
            with self.subTest(profile=profile):
                _, _, listed = description.rstrip(".").partition(" Surfaces: ")
                self.assertEqual(set(listed.split(", ")), set(FEED_PROFILE_SURFACES[profile]))
        self.assertEqual({entry["properties"]["version"]["const"]}, set().union(*FEED_PROFILE_VERSIONS.values()))
        self.assertEqual(
            set(entry["properties"]["state"]["enum"]),
            {member.value for member in FeedProfileState},
        )

    def test_schema_version_1_is_rejected_with_location(self) -> None:
        with self.assertRaisesRegex(
            LoopRegistryConfigError,
            r"schema_version_1\.json:\$\.schema_version: expected integer constant 2",
        ):
            JsonLoopRegistry(FIXTURES / "schema_version_1.json").registered_loops()

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

    def test_invalid_feed_profiles_are_rejected_with_location(self) -> None:
        row = "$.loops[0]"
        entry = f"{row}.feed_profiles[0]"

        def without(mapping: dict, key: str) -> dict:
            return {name: value for name, value in mapping.items() if name != key}

        cases = {
            "row missing feed_profiles": (lambda d: d["loops"].__setitem__(0, without(d["loops"][0], "feed_profiles")), f"{row}.feed_profiles", "required field is missing"),
            "row unknown field": (lambda d: d["loops"][0].__setitem__("grammar", "x"), f"{row}.grammar", "field is not defined by schema v2"),
            "feed_profiles not an array": (lambda d: d["loops"][0].__setitem__("feed_profiles", {}), f"{row}.feed_profiles", "expected an array"),
            "feed_profiles empty": (lambda d: d["loops"][0].__setitem__("feed_profiles", []), f"{row}.feed_profiles", "expected at least one feed profile"),
            "entry not an object": (lambda d: d["loops"][0]["feed_profiles"].__setitem__(0, "shared-dev-loop"), entry, "expected an object"),
            "entry missing basis": (lambda d: d["loops"][0]["feed_profiles"].__setitem__(0, without(d["loops"][0]["feed_profiles"][0], "basis")), f"{entry}.basis", "required field is missing"),
            "entry unknown field": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("paths", ["x"]), f"{entry}.paths", "field is not defined by schema v2"),
            "unknown profile": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("profile", "adapter-yaml"), f"{entry}.profile", "closed feed-profile vocabulary"),
            "profile not a string": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("profile", 1), f"{entry}.profile", "closed feed-profile vocabulary"),
            "duplicate profile": (lambda d: d["loops"][0]["feed_profiles"][1].__setitem__("profile", "shared-dev-loop"), f"{row}.feed_profiles[1].profile", "duplicate feed profile first declared at"),
            "unsupported version": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("version", 2), f"{entry}.version", "supported integer version"),
            "boolean version": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("version", True), f"{entry}.version", "supported integer version"),
            "string version": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("version", "1"), f"{entry}.version", "supported integer version"),
            "unknown state": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("state", "active"), f"{entry}.state", "expected live or historical"),
            "state not a string": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("state", 1), f"{entry}.state", "expected live or historical"),
            "profile null": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("profile", None), f"{entry}.profile", "closed feed-profile vocabulary"),
            "ledger live and historical": (lambda d: d["loops"][0].__setitem__("feed_profiles", [dict(d["loops"][0]["feed_profiles"][2], profile="remaining-loop", state="live"), d["loops"][0]["feed_profiles"][2]]), f"{row}.feed_profiles[1].profile", "surface receipt-ledger is already covered by"),
            "two live lifecycle readers": (lambda d: d["loops"][0].__setitem__("feed_profiles", [d["loops"][0]["feed_profiles"][0], dict(d["loops"][0]["feed_profiles"][0], profile="remaining-loop")]), f"{row}.feed_profiles[1].profile", "surface decision-registers is already covered by"),
            "remaining read twice": (lambda d: d["loops"][0].__setitem__("feed_profiles", [dict(d["loops"][0]["feed_profiles"][0], profile="remaining-loop"), d["loops"][0]["feed_profiles"][1]]), f"{row}.feed_profiles[1].profile", "surface status-remaining is already covered by"),
            "no live profile": (lambda d: [entry.__setitem__("state", "historical") for entry in d["loops"][0]["feed_profiles"]], f"{row}.feed_profiles", "expected at least one live feed profile"),
            "empty basis": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("basis", ""), f"{entry}.basis", "expected a non-empty string"),
            "absolute basis": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("basis", "/etc/passwd"), f"{entry}.basis", "normalized repository-relative path"),
            "traversing basis": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("basis", "projects/../x.md"), f"{entry}.basis", "normalized repository-relative path"),
            "backslash basis": (lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("basis", "projects\\pec\\AGENTS.md"), f"{entry}.basis", "normalized repository-relative path"),
        }
        for name, (mutate, location, message) in cases.items():
            with self.subTest(case=name):
                document = copy.deepcopy(valid_document())
                mutate(document)
                with self.assertRaises(LoopRegistryConfigError) as raised:
                    self.load(document)
                text = str(raised.exception)
                self.assertIn(f":{location}: ", text)
                self.assertIn(message, text)

    def test_failures_do_not_echo_document_values(self) -> None:
        sentinel = "zzsentinelzz"
        cases = {
            "loop_id": lambda d: d["loops"][0].__setitem__("loop_id", sentinel.upper()),
            "loop_init_path": lambda d: d["loops"][0].__setitem__("loop_init_path", f"/{sentinel}"),
            "profile": lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("profile", sentinel),
            "version": lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("version", sentinel),
            "state": lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("state", sentinel),
            "basis": lambda d: d["loops"][0]["feed_profiles"][0].__setitem__("basis", f"../{sentinel}"),
        }
        for name, mutate in cases.items():
            with self.subTest(field=name):
                document = copy.deepcopy(valid_document())
                mutate(document)
                with self.assertRaises(LoopRegistryConfigError) as raised:
                    self.load(document)
                self.assertNotIn(sentinel, str(raised.exception).lower())

    def test_additional_loops_need_entries_only(self) -> None:
        document = valid_document()
        document["loops"].append(
            {
                "loop_id": "second-loop",
                "loop_init_path": "projects/second/loop/LOOP_INIT.md",
                "feed_profiles": [
                    {"profile": profile, "version": 1, "state": state, "basis": "projects/second/AGENTS.md"}
                    for profile, state in (
                        ("shared-dev-loop", "live"),
                        ("loop-receipts-ledger", "historical"),
                        ("agentruns-json", "historical"),
                    )
                ],
            }
        )
        loops = self.load(document)
        self.assertEqual([loop.loop_id for loop in loops], ["pec", "second-loop"])
        self.assertEqual(
            [profile.profile for profile in loops[1].feed_profiles],
            ["shared-dev-loop", "loop-receipts-ledger", "agentruns-json"],
        )
        self.assertEqual(loops[1].feed_profiles[2].state, FeedProfileState.HISTORICAL)

    def test_invalid_document_never_returns_partial_or_empty_set(self) -> None:
        for fixture in (
            "schema_version_1.json",
            "missing_loop_id.json",
            "duplicate_loop_id.json",
            "malformed.json",
        ):
            with self.subTest(fixture=fixture):
                with self.assertRaises(LoopRegistryConfigError):
                    JsonLoopRegistry(FIXTURES / fixture).registered_loops()
        document = valid_document()
        document["loops"].append(copy.deepcopy(document["loops"][0]))
        document["loops"][1]["loop_id"] = "second-loop"
        document["loops"][1]["feed_profiles"][0]["state"] = "stale"
        with self.assertRaisesRegex(LoopRegistryConfigError, r"\$\.loops\[1\]\.feed_profiles\[0\]\.state"):
            self.load(document)


if __name__ == "__main__":
    unittest.main()
