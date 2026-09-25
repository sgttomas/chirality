from __future__ import annotations

import ast
import inspect
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


V2_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = V2_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

import pec_v2.adapters.storage as adapter_package  # noqa: E402
import pec_v2.adapters.storage.sqlite_store as adapter_module  # noqa: E402
import pec_v2.core.ports.store as port_module  # noqa: E402
from pec_v2.adapters.storage.sqlite_store import (  # noqa: E402
    SqliteMetadataStore,
    StoreConfigurationError,
)
from pec_v2.core.content_minimal_guard import (  # noqa: E402
    FieldClass,
    KnownState,
    MetadataField,
    MetadataRecord,
    RepositoryPath,
)
from pec_v2.core.ports.store import MetadataStore, StoreClosedError, StoreDataError  # noqa: E402


TEST_TO_VERIFICATION = {
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_004_admission_and_readback_preserve_all_five_typed_classes": ("VER-004", "VER-005"),
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically": ("VER-004",),
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution": ("VER-005",),
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary": ("VER-006",),
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing": ("VER-004", "VER-008"),
    "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_policy_is_fixed_finite_and_domain_checked": ("VER-008",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_001_database_journal_and_temp_artifacts_are_ignored": ("VER-001",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_001_force_tracked_store_artifact_fails_before_any_write": ("VER-001",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_001_later_negation_of_the_rule_fails_before_store_creation": ("VER-001",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation": ("VER-002",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface": ("VER-003", "VER-007"),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call": ("VER-007",),
    "test_store_lifecycle.StoreLifecycleTests.test_ver_009_loaded_suite_has_exact_execution_mapping": ("VER-009",),
}


class ScratchCheckoutTest(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.checkout = Path(self._temporary.name) / "checkout"
        self.checkout.mkdir()
        subprocess.run(["git", "init", "-q", str(self.checkout)], check=True)
        (self.checkout / ".gitignore").write_text("/.pec-v2/\n", encoding="utf-8")

    def tearDown(self) -> None:
        self._temporary.cleanup()

    @staticmethod
    def record(record_id: str = "DEL-01-03") -> MetadataRecord:
        return MetadataRecord(
            record_id=record_id,
            source_path=RepositoryPath("projects/pec/execution/status.md"),
            fields=(MetadataField("lifecycle", FieldClass.STATE, KnownState.IN_PROGRESS),),
        )


class StoreLifecycleTests(ScratchCheckoutTest):
    def test_ver_001_database_journal_and_temp_artifacts_are_ignored(self) -> None:
        """VER-001: the checked-in root rule covers every store artifact shape."""
        store = SqliteMetadataStore(self.checkout)
        store.admit_batch((self.record(),))
        database = self.checkout / ".pec-v2" / "record_store.sqlite3"
        artifacts = [database, Path(f"{database}-wal"), Path(f"{database}-shm"), Path(f"{database}-journal"), database.parent / "write.tmp"]
        for artifact in artifacts:
            artifact.touch(exist_ok=True)
            result = subprocess.run(
                ["git", "-C", str(self.checkout), "check-ignore", "-q", str(artifact)],
                check=False,
            )
            self.assertEqual(result.returncode, 0, artifact)
        status = subprocess.run(
            ["git", "-C", str(self.checkout), "status", "--porcelain", "--untracked-files=all", "--", ".pec-v2"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(status.stdout, "")
        store.close()

    def test_ver_001_later_negation_of_the_rule_fails_before_store_creation(self) -> None:
        """VER-001: a literal rule is insufficient when later policy undoes it."""
        (self.checkout / ".gitignore").write_text(
            "/.pec-v2/\n!/.pec-v2/\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(StoreConfigurationError, "does not cover"):
            SqliteMetadataStore(self.checkout)
        self.assertFalse((self.checkout / ".pec-v2").exists())

    def test_ver_001_force_tracked_store_artifact_fails_before_any_write(self) -> None:
        """VER-001: tracked store bytes are rejected even when the ignore rule matches."""
        database = self.checkout / ".pec-v2" / "record_store.sqlite3"
        database.parent.mkdir()
        database.write_bytes(b"sentinel-not-a-database")
        subprocess.run(
            ["git", "-C", str(self.checkout), "add", "-f", ".pec-v2/record_store.sqlite3"],
            check=True,
        )
        with self.assertRaisesRegex(StoreConfigurationError, "tracked store artifact"):
            SqliteMetadataStore(self.checkout)
        self.assertEqual(database.read_bytes(), b"sentinel-not-a-database")

    def test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation(self) -> None:
        """VER-002: every local lifecycle reaches a valid empty recreation."""
        store = SqliteMetadataStore(self.checkout)
        self.assertEqual(store.read_all(), ())
        store.admit_batch((self.record(),))
        store.close()
        with self.assertRaises(StoreClosedError):
            store.read_all()

        restarted = SqliteMetadataStore(self.checkout)
        self.assertEqual([row.record_id for row in restarted.read_all()], ["DEL-01-03"])
        self.assertTrue((self.checkout / ".pec-v2" / "record_store.sqlite3").is_file())
        restarted.reset()
        self.assertEqual(restarted.read_all(), ())
        restarted.admit_batch((self.record("DEL-01-03-B"),))
        restarted.delete()
        restarted.reopen()
        self.assertEqual(restarted.read_all(), ())
        restarted.close()
        restarted.delete()
        restarted.reopen()
        self.assertEqual(restarted.read_all(), ())
        restarted.close()

        # External deletion of the store directory while a handle is open.
        external = SqliteMetadataStore(self.checkout)
        external.admit_batch((self.record("DEL-01-03-C"),))
        shutil.rmtree(self.checkout / ".pec-v2")
        external.close()
        recreated = SqliteMetadataStore(self.checkout)
        self.assertEqual(recreated.read_all(), ())
        recreated.admit_batch((self.record("DEL-01-03-D"),))
        recreated.close()

        # A deliberately corrupted scratch database fails with the port-level error.
        database = self.checkout / ".pec-v2" / "record_store.sqlite3"
        image = bytearray(database.read_bytes())
        page_size = int.from_bytes(image[16:18], "big")
        page_size = 65536 if page_size == 1 else page_size
        self.assertGreater(len(image), page_size)
        image[page_size:] = b"\xff" * (len(image) - page_size)
        database.write_bytes(bytes(image))
        corrupted = SqliteMetadataStore(self.checkout)
        with self.assertRaises(StoreDataError) as raised:
            corrupted.read_all()
        self.assertIs(type(raised.exception), port_module.StoreDataError)
        self.assertNotIsInstance(raised.exception, sqlite3.Error)
        self.assertIsInstance(raised.exception.__cause__, sqlite3.Error)
        corrupted.reset()
        self.assertEqual(corrupted.read_all(), ())
        corrupted.close()

    def test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface(self) -> None:
        """VER-003: consumer methods leak no engine/path and writes call one guard."""
        public = [name for name in vars(MetadataStore) if not name.startswith("_")]
        self.assertEqual(public, ["admit_batch", "read_all", "close", "reopen", "delete", "reset"])
        signatures = " ".join(str(inspect.signature(getattr(MetadataStore, name))) for name in public)
        for forbidden in ("sqlite", "connection", "engine", "Path"):
            self.assertNotIn(forbidden, signatures)

        adapter_path = SRC_ROOT / "pec_v2" / "adapters" / "storage" / "sqlite_store.py"
        source = adapter_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        methods = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        self.assertEqual(methods.count("admit_batch"), 1)
        self.assertEqual(methods.count("_insert_guarded"), 1)

        calls: list[tuple[str | None, ast.Call]] = []

        def collect(node: ast.AST, owner: str | None) -> None:
            for child in ast.iter_child_nodes(node):
                child_owner = child.name if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) else owner
                if isinstance(child, ast.Call):
                    calls.append((child_owner, child))
                collect(child, child_owner)

        collect(tree, None)

        def is_guard_call(call: ast.Call) -> bool:
            func = call.func
            return (
                isinstance(func, ast.Attribute)
                and func.attr == "guard"
                and isinstance(func.value, ast.Attribute)
                and func.value.attr == "_guard"
                and isinstance(func.value.value, ast.Name)
                and func.value.value.id == "self"
            )

        insert_references = [
            node for node in ast.walk(tree) if isinstance(node, ast.Attribute) and node.attr == "_insert_guarded"
        ]
        self.assertEqual(len(insert_references), 1)
        self.assertFalse(
            [node for node in ast.walk(tree) if isinstance(node, ast.Name) and node.id == "_insert_guarded"]
        )
        self.assertFalse(
            [node for node in ast.walk(tree) if isinstance(node, ast.Constant) and node.value == "_insert_guarded"]
        )
        insert_calls = [
            (owner, call)
            for owner, call in calls
            if isinstance(call.func, ast.Attribute) and call.func.attr == "_insert_guarded"
        ]
        guard_calls = [(owner, call) for owner, call in calls if is_guard_call(call)]
        self.assertEqual([owner for owner, _ in insert_calls], ["admit_batch"])
        self.assertEqual([owner for owner, _ in guard_calls], ["admit_batch"])
        guard_call, insert_call = guard_calls[0][1], insert_calls[0][1]
        self.assertLess(
            (guard_call.lineno, guard_call.col_offset),
            (insert_call.lineno, insert_call.col_offset),
        )

        def static_sql(argument: ast.expr) -> str:
            if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                return argument.value
            if isinstance(argument, ast.JoinedStr):
                return "".join(
                    part.value
                    for part in argument.values
                    if isinstance(part, ast.Constant) and isinstance(part.value, str)
                )
            self.fail(f"SQL at line {argument.lineno} is not statically inspectable")

        dml_owners: list[str | None] = []
        ddl_owners: list[str | None] = []
        for owner, call in calls:
            if not (isinstance(call.func, ast.Attribute) and call.func.attr in {"execute", "executemany", "executescript"}):
                continue
            self.assertTrue(call.args, f"SQL call at line {call.lineno} has no positional statement")
            statement = re.sub(r"\bON\s+(DELETE|UPDATE)\b", " ", static_sql(call.args[0]).upper())
            if re.search(r"\b(INSERT|UPDATE|DELETE|REPLACE)\b", statement):
                dml_owners.append(owner)
            if re.search(r"\b(CREATE|DROP|ALTER)\b", statement):
                ddl_owners.append(owner)
        self.assertEqual(dml_owners, ["_insert_guarded", "_insert_guarded"])
        self.assertEqual(ddl_owners, ["_create_schema"])

        classes = {node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)}
        for name in ("StoreConfigurationError", "StoreDataError"):
            with self.subTest(port_error=name):
                port_error = vars(port_module)[name]
                self.assertEqual(port_error.__module__, "pec_v2.core.ports.store")
                self.assertTrue(issubclass(port_error, RuntimeError))
                self.assertIs(getattr(adapter_module, name), port_error)
                self.assertIs(getattr(adapter_package, name), port_error)
                self.assertNotIn(name, classes)

    def test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call(self) -> None:
        """VER-007: implementation is local, stdlib-only, and port-isolated."""
        production = [
            SRC_ROOT / "pec_v2" / "core" / "content_minimal_guard.py",
            SRC_ROOT / "pec_v2" / "core" / "ports" / "store.py",
            SRC_ROOT / "pec_v2" / "adapters" / "storage" / "sqlite_store.py",
        ]
        forbidden = {"socket", "urllib", "http", "requests", "aiohttp"}
        for path in production:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            roots: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    roots.update(alias.name.split(".", 1)[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    roots.add(node.module.split(".", 1)[0])
            self.assertFalse(roots & forbidden, (path, roots))
            self.assertTrue(roots <= set(sys.stdlib_module_names) | {"pec_v2"}, (path, roots))

    def test_ver_009_loaded_suite_has_exact_execution_mapping(self) -> None:
        """VER-009: every discovered test ID is mapped and every VER is covered."""
        suite = unittest.defaultTestLoader.discover(
            str(Path(__file__).resolve().parent), pattern="test_*.py"
        )

        def identities(node: unittest.TestSuite) -> set[str]:
            found: set[str] = set()
            for item in node:
                if isinstance(item, unittest.TestSuite):
                    found.update(identities(item))
                else:
                    found.add(item.id())
            return found

        discovered = identities(suite)
        self.assertEqual(discovered, set(TEST_TO_VERIFICATION))
        mapped = {verification for values in TEST_TO_VERIFICATION.values() for verification in values}
        self.assertEqual(mapped, {f"VER-{number:03d}" for number in range(1, 10)})


if __name__ == "__main__":
    unittest.main()
