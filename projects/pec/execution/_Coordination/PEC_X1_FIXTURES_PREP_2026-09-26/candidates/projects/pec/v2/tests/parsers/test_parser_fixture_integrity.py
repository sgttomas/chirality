"""Fixture-side integrity tests for the PKG-02 parser fixture suites.

These tests check the fixtures themselves, not any parser: no parser exists
yet. They implement the fixture-side part of DEL-02-03 VER-017, DEL-02-08
VER-016 and VER-017, and DEL-02-09 VER-014. Later parser packets add the golden
tests that run each parser over these fixtures and apply the same
no-source-text assertion to the parser output.

Pinned fixtures are read only through read-only Git plumbing (cat-file,
ls-tree, rev-parse, merge-base and config --get), with lazy fetching and
replacement objects disabled. A pin that cannot be resolved fails the suite;
nothing is skipped and nothing is re-pinned.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import unittest
from pathlib import Path


PARSERS_ROOT = Path(__file__).resolve().parent
FIXTURES = PARSERS_ROOT / "fixtures"
PINNED = FIXTURES / "pinned"
SYNTHETIC = FIXTURES / "synthetic"

PINNED_SCHEMA = "pec-v2-parser-fixtures-pinned/v1"
GOLDEN_SCHEMA = "pec-v2-parser-fixtures-golden/v1"
SYNTHETIC_SCHEMA = "pec-v2-parser-fixtures-synthetic/v1"

GIT_ALLOWED = ("cat-file", "ls-tree", "rev-parse", "merge-base", "config")
GIT_ENV = {
    "GIT_NO_LAZY_FETCH": "1",
    "GIT_NO_REPLACE_OBJECTS": "1",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_OPTIONAL_LOCKS": "0",
}

FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
HEX_SHA = re.compile(r"^[0-9a-f]{7,40}$")
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
LABEL = re.compile(r"^[a-z][a-z0-9-]*$")
KEY = re.compile(r"^[a-z][a-z0-9_]*$")
ID = re.compile(r"^[A-Z][A-Z0-9-]*(\.[A-Za-z0-9-]+)*$")
BIND = re.compile(r"^DEL-02-0[389]/(REQ|AC|VER|CON|TBD)-[0-9]{3}$")
VERIFICATION = re.compile(r"^DEL-02-0[389]/VER-[0-9]{3}$")
DELIVERABLE = re.compile(r"^DEL-02-0[389]$")
TOKEN = re.compile(r"^\S{1,200}$")
BOUNDARY = b"A-Za-z0-9_"

TEST_TO_VERIFICATION = {
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_manifests_and_goldens_are_well_formed": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_every_record_binds_a_requirement_criterion_and_verification": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-08/VER-017", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_pins_resolve_by_read_only_plumbing_on_integrated_history": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_tree_expectations_hold_at_their_pinned_commits": ("DEL-02-03/VER-016", "DEL-02-03/VER-017"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_golden_source_values_are_grounded_in_their_pinned_blobs": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_goldens_are_content_minimal_and_hold_no_source_text_run": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_no_fixture_source_is_copied_into_the_tree": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-08/VER-017", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_synthetic_cases_cover_the_contract_minimums": ("DEL-02-03/VER-017", "DEL-02-08/VER-017", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_git_access_is_read_only_and_allowlisted": ("DEL-02-03/VER-017", "DEL-02-08/VER-016", "DEL-02-09/VER-014"),
    "test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_loaded_suite_has_exact_verification_mapping": ("DEL-02-03/VER-013", "DEL-02-08/VER-020", "DEL-02-09/VER-016"),
}

# Minimum synthetic cases each contract names (DEL-02-08 REQ-017, DEL-02-09
# REQ-014, DEL-02-03 REQ-017), keyed by the case label the synthetic manifest uses.
REQUIRED_SYNTHETIC_CASES = {
    "DEL-02-08": (
        "missing-run-identity",
        "duplicated-run-identity",
        "unrecognized-state-token",
        "no-node-table",
        "unresolved-pr-number",
        "two-graphs-bind-one-deliverable",
    ),
    "DEL-02-09": (
        "template-table-form",
        "entry-without-readable-run-token",
        "unreadable-date",
        "file-without-run-index-entry",
        "deliverable-without-memory-file",
        "runs-section-mixed-with-dated-sections",
    ),
    "DEL-02-03": (
        "marker-carrying-ledger-entry",
        "prose-structured-ledger-entry",
        "receipt-without-examined-through",
        "malformed-ledger",
        "unreadable-file",
        "undeclared-loop",
    ),
}

WRITE_CALLS = {"write_text", "write_bytes", "unlink", "rmtree", "remove", "rename", "replace", "mkdir", "system", "Popen"}


class GitError(AssertionError):
    """A read-only Git query failed; the message names the command and cause."""


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run one allowlisted, read-only Git plumbing query from the v2 tree."""
    if not args or args[0] not in GIT_ALLOWED:
        raise ValueError(f"git subcommand not allowlisted: {args[:1]}")
    if args[0] == "config" and (len(args) != 3 or args[1] != "--get"):
        raise ValueError("git config is allowlisted only as 'config --get <key>'")
    env = dict(os.environ)
    env.update(GIT_ENV)
    result = subprocess.run(
        ["git", "-C", str(PARSERS_ROOT), *args],
        capture_output=True,
        env=env,
        check=False,
    )
    if check and result.returncode != 0:
        raise GitError(
            f"git {' '.join(args)} exited {result.returncode}: "
            f"{result.stderr.decode('utf-8', 'replace').strip()}"
        )
    return result


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def git_blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def runs(text: str, width: int) -> set:
    tokens = text.split()
    return {tuple(tokens[i : i + width]) for i in range(len(tokens) - width + 1)}


def leaves(value, path: str = "$"):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaves(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from leaves(item, f"{path}[{index}]")
    else:
        yield path, value


def is_token(value) -> bool:
    return isinstance(value, str) and bool(TOKEN.match(value)) and "://" not in value


def is_expect_value(value) -> bool:
    """An expectation value: a boolean, an integer, one token, or a list of tokens."""
    if isinstance(value, (bool, int)):
        return True
    if isinstance(value, list):
        return all(is_token(item) for item in value)
    return is_token(value)


def json_text_runs(value, width: int) -> set:
    """Word runs of a JSON fixture's string leaves, except repository paths."""
    found = set()
    for path, leaf in leaves(value):
        if isinstance(leaf, str) and not path.endswith((".path", ".tree")):
            found |= runs(leaf, width)
    return found


def unreachable(pin: dict, cause: str) -> str:
    return (
        f"PIN UNREACHABLE {pin['id']} ({pin['commit']}:{pin['path']}): {cause}. "
        "The fixture suite needs a full, non-shallow clone without a partial-clone "
        "filter. If the commit is gone from the canonical repository, the fixture "
        "must be re-pinned by a new owner-ruled packet; nothing re-pins automatically."
    )


class ParserFixtureIntegrityTests(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.pinned = load_json(PINNED / "MANIFEST.json")
        cls.synthetic = load_json(SYNTHETIC / "MANIFEST.json")
        cls.goldens = {path.stem: load_json(path) for path in sorted((PINNED / "goldens").glob("*.json"))}
        cls.blob_cache = {}

    # -- helpers -------------------------------------------------------------

    def assert_repository_can_hold_pins(self) -> None:
        shallow = git("rev-parse", "--is-shallow-repository").stdout.decode().strip()
        self.assertEqual(shallow, "false", "shallow clone: pinned fixtures cannot be resolved")
        partial = git("config", "--get", "extensions.partialclone", check=False)
        self.assertNotEqual(partial.returncode, 0, "partial clone: pinned blobs may be absent and lazy fetching is disabled")

    def blob(self, entry: dict) -> bytes:
        if entry["blob"] not in self.blob_cache:
            result = git("cat-file", "blob", entry["blob"], check=False)
            if result.returncode != 0:
                self.fail(unreachable(entry, "blob not present in the local object store"))
            self.blob_cache[entry["blob"]] = result.stdout
        return self.blob_cache[entry["blob"]]

    def all_pins(self) -> list:
        return list(self.pinned["templates"]) + list(self.pinned["pins"])

    def expectations(self):
        for fixture, golden in sorted(self.goldens.items()):
            for expectation in golden["expectations"]:
                yield fixture, expectation

    def source_runs(self, width: int) -> set:
        found = set()
        for pin in self.pinned["pins"]:
            found |= runs(self.blob(pin).decode("utf-8", "replace"), width)
        return found

    # -- tests ---------------------------------------------------------------

    def test_manifests_and_goldens_are_well_formed(self) -> None:
        pinned = self.pinned
        self.assertEqual(pinned["schema"], PINNED_SCHEMA)
        self.assertEqual(set(pinned), {"schema", "policy", "templates", "pins", "trees"})
        policy = pinned["policy"]
        self.assertEqual(set(policy), {"source_run_words", "copy_run_words"})
        self.assertIs(type(policy["source_run_words"]), int)
        self.assertIs(type(policy["copy_run_words"]), int)
        self.assertGreaterEqual(policy["source_run_words"], 2)
        self.assertGreater(policy["copy_run_words"], policy["source_run_words"])

        ids = set()
        for entry in self.all_pins():
            self.assertRegex(entry["id"], ID)
            self.assertNotIn(entry["id"], ids, "duplicate pin id")
            ids.add(entry["id"])
            self.assertRegex(entry["commit"], FULL_SHA)
            self.assertRegex(entry["blob"], FULL_SHA)
            path = entry["path"]
            self.assertFalse(path.startswith("/") or "\\" in path or path != path.strip(), path)
            self.assertNotIn("..", path.split("/"), path)
        for entry in pinned["templates"]:
            self.assertEqual(set(entry), {"id", "commit", "path", "blob"})
        fixtures = set()
        for entry in pinned["pins"]:
            self.assertEqual(set(entry), {"id", "fixture", "project", "kind", "commit", "path", "blob", "serves"})
            self.assertRegex(entry["kind"], LABEL)
            self.assertTrue(entry["serves"])
            for deliverable in entry["serves"]:
                self.assertRegex(deliverable, DELIVERABLE)
            fixtures.add(entry["fixture"])
        self.assertEqual(fixtures, set(self.goldens), "every fixture has exactly one golden file")

        for tree in pinned["trees"]:
            self.assertLessEqual(set(tree), {"id", "fixture", "commit", "tree", "present", "absent", "tree_absent", "binds"})
            self.assertTrue({"id", "fixture", "commit", "tree", "binds"} <= set(tree))
            self.assertRegex(tree["id"], ID)
            self.assertNotIn(tree["id"], ids)
            ids.add(tree["id"])
            self.assertIn(tree["fixture"], fixtures)
            self.assertRegex(tree["commit"], FULL_SHA)
            if tree.get("tree_absent"):
                self.assertFalse(tree.get("present") or tree.get("absent"), tree["id"])
            else:
                self.assertTrue(tree.get("present") or tree.get("absent"), tree["id"])

        pins = {entry["id"]: entry for entry in pinned["pins"]}
        for fixture, golden in self.goldens.items():
            self.assertEqual(golden["schema"], GOLDEN_SCHEMA)
            self.assertEqual(set(golden), {"schema", "fixture", "expectations"})
            self.assertEqual(golden["fixture"], fixture)
            self.assertTrue(golden["expectations"])
            for expectation in golden["expectations"]:
                self.assertLessEqual(set(expectation), {"id", "pin", "tier", "fact", "source", "expect", "binds"})
                self.assertTrue({"id", "pin", "tier", "fact", "binds"} <= set(expectation))
                self.assertRegex(expectation["id"], ID)
                self.assertNotIn(expectation["id"], ids)
                ids.add(expectation["id"])
                self.assertIn(expectation["pin"], pins, expectation["id"])
                self.assertEqual(pins[expectation["pin"]]["fixture"], fixture, expectation["id"])
                self.assertIn(expectation["tier"], ("fixed", "observed"))
                self.assertRegex(expectation["fact"], LABEL)
                self.assertTrue(expectation.get("source") or expectation.get("expect"), expectation["id"])
        bound = {pin_id: set() for pin_id in pins}
        for _, expectation in self.expectations():
            bound[expectation["pin"]] |= {bind.split("/")[0] for bind in expectation["binds"]}
        served = {pin_id: set(entry["serves"]) for pin_id, entry in pins.items()}
        self.assertEqual(bound, served, "each pin serves exactly the deliverables its expectations bind")

    def test_every_record_binds_a_requirement_criterion_and_verification(self) -> None:
        records = [(e["id"], e["binds"]) for _, e in self.expectations()]
        records += [(t["id"], t["binds"]) for t in self.pinned["trees"]]
        records += [(c["id"], c["binds"]) for c in self.synthetic["cases"]]
        for record_id, binds in records:
            with self.subTest(record=record_id):
                self.assertTrue(binds)
                self.assertEqual(len(binds), len(set(binds)))
                for bind in binds:
                    self.assertRegex(bind, BIND)
                for deliverable in {bind.split("/")[0] for bind in binds}:
                    kinds = {bind.split("/")[1].split("-")[0] for bind in binds if bind.startswith(deliverable + "/")}
                    self.assertTrue({"REQ", "AC", "VER"} <= kinds, f"{deliverable} lacks a REQ, AC or VER binding")

    def test_pins_resolve_by_read_only_plumbing_on_integrated_history(self) -> None:
        self.assert_repository_can_hold_pins()
        for entry in self.all_pins():
            with self.subTest(pin=entry["id"]):
                commit = git("cat-file", "-e", entry["commit"] + "^{commit}", check=False)
                if commit.returncode != 0:
                    self.fail(unreachable(entry, "commit not present in the local object store"))
                ancestor = git("merge-base", "--is-ancestor", entry["commit"], "HEAD", check=False)
                self.assertEqual(ancestor.returncode, 0, unreachable(entry, "commit is not an ancestor of HEAD"))
                resolved = git("rev-parse", "--verify", "--quiet", f"{entry['commit']}:{entry['path']}", check=False)
                self.assertEqual(resolved.returncode, 0, unreachable(entry, "path absent at the pinned commit"))
                self.assertEqual(resolved.stdout.decode().strip(), entry["blob"], "blob differs at the pinned commit")
                self.assertEqual(git("cat-file", "-t", entry["blob"]).stdout.decode().strip(), "blob")
                self.assertEqual(git_blob_id(self.blob(entry)), entry["blob"])

    def test_tree_expectations_hold_at_their_pinned_commits(self) -> None:
        self.assert_repository_can_hold_pins()
        for tree in self.pinned["trees"]:
            with self.subTest(tree=tree["id"]):
                listing = git("ls-tree", "--full-tree", "--name-only", tree["commit"], tree["tree"] + "/")
                names = {line.rsplit("/", 1)[-1] for line in listing.stdout.decode("utf-8").splitlines()}
                if tree.get("tree_absent"):
                    self.assertEqual(names, set(), "tree exists at the pinned commit")
                    parent, _, leaf = tree["tree"].rpartition("/")
                    siblings = git("ls-tree", "--full-tree", "--name-only", tree["commit"], parent + "/")
                    siblings = {line.rsplit("/", 1)[-1] for line in siblings.stdout.decode("utf-8").splitlines()}
                    self.assertTrue(siblings, "the parent of an absent tree must exist at the pinned commit")
                    self.assertNotIn(leaf, siblings)
                    continue
                self.assertTrue(names, "tree missing at the pinned commit")
                for name in tree.get("present", []):
                    self.assertIn(name, names)
                for name in tree.get("absent", []):
                    self.assertNotIn(name, names)

    def test_golden_source_values_are_grounded_in_their_pinned_blobs(self) -> None:
        pins = {entry["id"]: entry for entry in self.pinned["pins"]}
        for _, expectation in self.expectations():
            data = self.blob(pins[expectation["pin"]])
            for key, value in expectation.get("source", {}).items():
                with self.subTest(expectation=expectation["id"], key=key):
                    self.assertRegex(key, KEY)
                    self.assertIsNot(type(value), bool, "booleans belong in 'expect'")
                    if type(value) is int:
                        self.assertTrue(key == "pr" or key.endswith("_pr"), "integer source values are PR numbers")
                        pattern = rb"(?:#|/pull/)%d(?![0-9])" % value
                    else:
                        self.assertIs(type(value), str)
                        pattern = b"(?<![" + BOUNDARY + b"])" + re.escape(value.encode("utf-8")) + b"(?![" + BOUNDARY + b"])"
                    self.assertIsNotNone(re.search(pattern, data), f"{value!r} does not occur in {expectation['pin']}")
            commit = expectation.get("expect", {}).get("local_merge_commit")
            if commit is not None:
                with self.subTest(expectation=expectation["id"], key="local_merge_commit"):
                    self.assertEqual(git("cat-file", "-t", commit).stdout.decode().strip(), "commit")
                    parents = git("rev-parse", commit + "^@").stdout.decode().split()
                    self.assertGreaterEqual(len(parents), 2, "not a merge commit")
                    ancestor = git("merge-base", "--is-ancestor", commit, pins[expectation["pin"]]["commit"], check=False)
                    self.assertEqual(ancestor.returncode, 0, "merge is not integrated at the pinned commit")

    def test_goldens_are_content_minimal_and_hold_no_source_text_run(self) -> None:
        width = self.pinned["policy"]["source_run_words"]
        source = self.source_runs(width)
        for fixture, golden in sorted(self.goldens.items()):
            for path, value in leaves(golden):
                with self.subTest(fixture=fixture, path=path):
                    self.assertTrue(value is None or type(value) in (bool, int, str), type(value))
                    if type(value) is not str:
                        continue
                    self.assertRegex(value, TOKEN, "golden strings are single tokens")
                    self.assertNotIn("://", value, "golden strings hold no URL")
                    if path.endswith("_sha"):
                        self.assertRegex(value, HEX_SHA)
                    if path.endswith(".date"):
                        self.assertRegex(value, DATE)
                    if path.endswith(".local_merge_commit"):
                        self.assertRegex(value, FULL_SHA)
                    self.assertFalse(runs(value, width) & source, "source-text run in a golden")
        for _, expectation in self.expectations():
            for key, value in expectation.get("expect", {}).items():
                with self.subTest(expectation=expectation["id"], key=key):
                    self.assertRegex(key, KEY)
                    self.assertTrue(is_expect_value(value), f"not a boolean, integer or token: {value!r}")
                    if key == "local_merge_commit":
                        self.assertRegex(value, FULL_SHA)

    def test_no_fixture_source_is_copied_into_the_tree(self) -> None:
        pinned_ids = {entry["blob"] for entry in self.pinned["pins"]}
        width = self.pinned["policy"]["copy_run_words"]
        shared = set()
        for template in self.pinned["templates"]:
            shared |= runs(self.blob(template).decode("utf-8", "replace"), width)
        copied = self.source_runs(width) - shared
        for path in sorted(p for p in FIXTURES.rglob("*") if p.is_file()):
            relative = path.relative_to(FIXTURES).as_posix()
            with self.subTest(path=relative):
                data = path.read_bytes()
                self.assertNotIn(git_blob_id(data), pinned_ids, "a pinned source is copied into the tree")
                if path.suffix == ".json":
                    text_runs = json_text_runs(json.loads(data.decode("utf-8")), width)
                else:
                    text_runs = runs(data.decode("utf-8", "replace"), width)
                overlap = text_runs & copied
                self.assertFalse(overlap, f"{len(overlap)} copied {width}-word runs, e.g. {sorted(overlap)[:1]}")

    def test_synthetic_cases_cover_the_contract_minimums(self) -> None:
        synthetic = self.synthetic
        self.assertEqual(synthetic["schema"], SYNTHETIC_SCHEMA)
        self.assertEqual(set(synthetic), {"schema", "cases"})
        seen, files = set(), set()
        labels = {deliverable: set() for deliverable in REQUIRED_SYNTHETIC_CASES}
        for case in synthetic["cases"]:
            with self.subTest(case=case.get("id")):
                self.assertLessEqual(set(case), {"id", "case", "files", "construction", "expect", "binds"})
                self.assertTrue({"id", "case", "files", "expect", "binds"} <= set(case))
                self.assertRegex(case["id"], ID)
                self.assertNotIn(case["id"], seen)
                seen.add(case["id"])
                self.assertRegex(case["case"], LABEL)
                self.assertIsInstance(case["files"], list)
                if not case["files"]:
                    self.assertIsInstance(case.get("construction"), str, "a case without files is constructed at test time")
                    self.assertTrue(case["construction"].strip())
                for name in case["files"]:
                    self.assertNotIn("..", name.split("/"))
                    self.assertTrue(name.endswith(".md"), name)
                    self.assertTrue((SYNTHETIC / name).is_file(), name)
                    files.add(name)
                self.assertTrue(case["expect"])
                for key, value in case["expect"].items():
                    self.assertRegex(key, KEY)
                    self.assertTrue(is_expect_value(value), f"{key}: {value!r}")
                for deliverable in {bind.split("/")[0] for bind in case["binds"]}:
                    if deliverable in labels:
                        labels[deliverable].add(case["case"])
        for deliverable, required in REQUIRED_SYNTHETIC_CASES.items():
            self.assertLessEqual(set(required), labels[deliverable], deliverable)
        on_disk = {p.relative_to(SYNTHETIC).as_posix() for p in SYNTHETIC.rglob("*") if p.is_file()} - {"MANIFEST.json"}
        self.assertEqual(on_disk, files, "every synthetic file is listed, and every listed file exists")

    def test_git_access_is_read_only_and_allowlisted(self) -> None:
        for forbidden in (("checkout", "HEAD"), ("fetch",), ("update-ref", "HEAD", "HEAD"), ("config", "core.x", "y"), ("config", "--get"), ()):
            with self.subTest(args=forbidden):
                with self.assertRaises(ValueError):
                    git(*forbidden)
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
        subprocess_calls, writes = [], []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if isinstance(func, ast.Attribute):
                if isinstance(func.value, ast.Name) and func.value.id == "subprocess":
                    subprocess_calls.append(func.attr)
                if func.attr in WRITE_CALLS:
                    writes.append(func.attr)
            if isinstance(func, ast.Name) and func.id == "open":
                writes.append("open")
        self.assertEqual(subprocess_calls, ["run"], "one subprocess call site, inside git()")
        self.assertEqual(writes, [], "the fixture suite writes nothing")

    def test_loaded_suite_has_exact_verification_mapping(self) -> None:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ParserFixtureIntegrityTests)
        loaded = {f"{Path(__file__).stem}.{type(test).__name__}.{test._testMethodName}" for test in suite}
        self.assertEqual(loaded, set(TEST_TO_VERIFICATION))
        for mapped in TEST_TO_VERIFICATION.values():
            for bind in mapped:
                self.assertRegex(bind, VERIFICATION)


if __name__ == "__main__":
    unittest.main()
