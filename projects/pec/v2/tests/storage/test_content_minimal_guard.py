from __future__ import annotations

import ast
import inspect
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Iterable, cast


V2_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = V2_ROOT / "src"
sys.path.insert(0, str(SRC_ROOT))

from pec_v2.adapters.storage.sqlite_store import SqliteMetadataStore  # noqa: E402
from pec_v2.core.content_minimal_guard import (  # noqa: E402
    ContentHash,
    ContentMinimalGuard,
    FieldClass,
    HashAlgorithm,
    KnownState,
    MetadataField,
    MetadataRecord,
    RepositoryPath,
    ShaAlgorithm,
    ShaDigest,
)


MULTILINE_PATH_FIXTURE = "line one\n+line two"
CORPUS_PAYLOADS = (
    "full file body",
    "@@ -1 +1 @@",
    "owner directed prose",
    "payload",
    "looks approved",
    MULTILINE_PATH_FIXTURE,
    "line one",
    "+line two",
)


def forged_path(value: object) -> RepositoryPath:
    """A RepositoryPath shell whose value never passed the constructor check."""
    path = object.__new__(RepositoryPath)
    object.__setattr__(path, "value", value)
    return path


SUBCLASS_PAYLOAD = "SECRET FILE BODY\n+diff line two"


class SubclassPayload(str):
    """A str subclass whose adaptation and rendering hooks return other text."""

    def __conform__(self, protocol: object) -> str:
        return SUBCLASS_PAYLOAD

    def __format__(self, format_spec: str) -> str:
        return SUBCLASS_PAYLOAD

    def __str__(self) -> str:
        return SUBCLASS_PAYLOAD

    def __repr__(self) -> str:
        return SUBCLASS_PAYLOAD


class MethodLiar(str):
    """A str subclass overriding the methods the normalization checks call."""

    __hash__ = str.__hash__

    def startswith(self, *args: object, **kwargs: object) -> bool:  # type: ignore[override]
        return False

    def __ne__(self, other: object) -> bool:
        return False

    def split(self, *args: object, **kwargs: object) -> list[str]:  # type: ignore[override]
        return ["liar"]


class LengthLiar(str):
    """A str subclass whose len() reports a digest length it does not have."""

    def __len__(self) -> int:
        return 40


class LyingTuple(tuple):
    """A tuple subclass that reports one item and iterates none."""

    def __len__(self) -> int:
        return 1

    def __iter__(self):  # type: ignore[no-untyped-def]
        return iter(())


class ClassSpoof:
    """A non-str object whose __class__ claims to be str."""

    @property  # type: ignore[misc]
    def __class__(self):  # type: ignore[no-untyped-def,override]
        return str


class ConformingInt(int):
    """An int subclass whose adaptation hook returns text."""

    def __conform__(self, protocol: object) -> str:
        return SUBCLASS_PAYLOAD


def rejection_corpus() -> tuple[tuple[str, tuple[MetadataField, ...]], ...]:
    """Shared VER-004/VER-006 fixtures covering STATE, PATH, and an unknown class."""
    return (
        ("file-body", (MetadataField("state", FieldClass.STATE, "full file body"),)),
        ("diff-hunk", (MetadataField("metadata", FieldClass.STATE, "@@ -1 +1 @@"),)),
        ("register-prose", (MetadataField("path", FieldClass.PATH, "owner directed prose"),)),
        ("unknown", (MetadataField("value", cast(FieldClass, "content"), "payload"),)),
        (
            "mixed",
            (
                MetadataField("count", FieldClass.COUNT, 1),
                MetadataField("prose", FieldClass.STATE, "looks approved"),
            ),
        ),
        ("multiline-path", (MetadataField("locator", FieldClass.PATH, forged_path(MULTILINE_PATH_FIXTURE)),)),
    )


class ContentMinimalGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.checkout = Path(self._temporary.name) / "checkout"
        self.checkout.mkdir()
        subprocess.run(["git", "init", "-q", str(self.checkout)], check=True)
        (self.checkout / ".gitignore").write_text("/.pec-v2/\n", encoding="utf-8")
        self.store = SqliteMetadataStore(self.checkout)

    def tearDown(self) -> None:
        self.store.close()
        self._temporary.cleanup()

    def record(self, record_id: str, *fields: MetadataField) -> MetadataRecord:
        return MetadataRecord(
            record_id=record_id,
            source_path=RepositoryPath("projects/pec/execution/source.json"),
            source_sha=ShaDigest(ShaAlgorithm.SHA256, "a" * 64),
            fields=tuple(fields),
        )

    def assert_no_persisted_residue(self, fixtures: Iterable[str]) -> None:
        """Raw engine dump and raw store-file bytes carry no fixture string."""
        needles = tuple(fixtures)
        database = self.checkout / ".pec-v2" / "record_store.sqlite3"
        raw = sqlite3.connect(f"{database.as_uri()}?mode=ro", uri=True)
        try:
            schema = raw.execute("SELECT type, name, tbl_name, sql FROM sqlite_master").fetchall()
            tables = [name for kind, name, _, _ in schema if kind == "table"]
            self.assertTrue({"metadata_records", "metadata_fields"} <= set(tables))
            cells: list[object] = [cell for row in schema for cell in row]
            for table in tables:
                quoted = '"' + table.replace('"', '""') + '"'
                cells.extend(cell for row in raw.execute(f"SELECT * FROM {quoted}") for cell in row)
        finally:
            raw.close()
        for needle in needles:
            encoded = needle.encode("utf-8")
            for cell in cells:
                if isinstance(cell, str):
                    self.assertNotIn(needle, cell)
                elif isinstance(cell, bytes):
                    self.assertNotIn(encoded, cell)
            for suffix in ("", "-journal", "-wal", "-shm"):
                artifact = Path(f"{database}{suffix}")
                if artifact.exists():
                    self.assertNotIn(encoded, artifact.read_bytes(), artifact.name)

    def test_ver_004_admission_and_readback_preserve_all_five_typed_classes(self) -> None:
        candidate = self.record(
            "record-1",
            MetadataField("locator", FieldClass.PATH, RepositoryPath("projects/pec/loop/LOOP_INIT.md")),
            MetadataField("items", FieldClass.COUNT, 3),
            MetadataField("commit", FieldClass.SHA, ShaDigest(ShaAlgorithm.SHA1, "b" * 40)),
            MetadataField("lifecycle", FieldClass.STATE, KnownState.INITIALIZED),
            MetadataField("snapshot", FieldClass.HASH, ContentHash(HashAlgorithm.BLAKE2B_256, "c" * 64)),
        )
        result = self.store.admit_batch((candidate,))
        self.assertEqual((result.attempted, result.accepted, result.rejected), (1, 1, 0))
        stored = self.store.read_all()[0]
        self.assertEqual(stored.record_id, "record-1")
        self.assertEqual(stored.source_path, "projects/pec/execution/source.json")
        self.assertEqual(
            [(field.name, field.field_class, field.value) for field in stored.fields],
            [
                ("locator", FieldClass.PATH, "projects/pec/loop/LOOP_INIT.md"),
                ("items", FieldClass.COUNT, "3"),
                ("commit", FieldClass.SHA, f"sha1:{'b' * 40}"),
                ("lifecycle", FieldClass.STATE, "INITIALIZED"),
                ("snapshot", FieldClass.HASH, f"blake2b-256:{'c' * 64}"),
            ],
        )

    def test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically(self) -> None:
        """VER-004: prohibited values leave no field or record residue."""
        candidates = tuple(self.record(key, *fields) for key, fields in rejection_corpus())
        result = self.store.admit_batch(candidates)
        self.assertEqual((result.attempted, result.accepted, result.rejected), (6, 0, 6))
        self.assertEqual(self.store.read_all(), ())
        self.assertEqual({failure.record_id for failure in result.failures}, {row.record_id for row in candidates})
        self.assert_no_persisted_residue((*CORPUS_PAYLOADS, *(row.record_id for row in candidates)))

    def test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution(self) -> None:
        """VER-005: attempted equals accepted plus rejected with located failures."""
        accepted = self.record("accepted", MetadataField("count", FieldClass.COUNT, 0))
        rejected = self.record("rejected", MetadataField("count", FieldClass.COUNT, True))
        result = self.store.admit_batch((accepted, rejected))
        self.assertEqual(result.attempted, result.accepted + result.rejected)
        self.assertEqual((result.accepted, result.rejected), (1, 1))
        self.assertEqual(result.accepted_record_ids, ("accepted",))
        self.assertEqual([(item.record_id, item.field_name) for item in result.failures], [("rejected", "count")])
        self.assertEqual([row.record_id for row in self.store.read_all()], ["accepted"])

        duplicate = self.store.admit_batch((accepted,))
        self.assertEqual((duplicate.accepted, duplicate.rejected), (0, 1))
        self.assertEqual(duplicate.failures[0].code, "DUPLICATE_RECORD")
        self.assertEqual(self.store.read_all()[0].fields[0].value, "0")

        count = MetadataField("count", FieldClass.COUNT, 1)
        batch: tuple[object, ...] = (
            self.record("fresh", MetadataField("count", FieldClass.COUNT, 2)),
            "not a record",
            self.record("bad id!", count),
            MetadataRecord("bad-source", forged_path("../escape"), (count,)),
            self.record("empty"),
            self.record("field-type", cast(MetadataField, "count")),
            self.record("field-name", MetadataField("bad name", FieldClass.COUNT, 1)),
            self.record("duplicate-field", count, MetadataField("count", FieldClass.COUNT, 2)),
            self.record("unknown-class", MetadataField("value", cast(FieldClass, "content"), 1)),
            self.record("invalid-value", MetadataField("count", FieldClass.COUNT, True)),
            42,
            self.record(
                "two-failures",
                MetadataField("count", FieldClass.COUNT, -1),
                MetadataField("lifecycle", FieldClass.STATE, "prose"),
            ),
            self.record("fresh", MetadataField("count", FieldClass.COUNT, 3)),
            MetadataRecord(cast(str, 7), RepositoryPath("projects/pec/source.md"), (count,)),
        )
        located = self.store.admit_batch(cast(tuple[MetadataRecord, ...], batch))
        self.assertEqual(
            [(item.record_id, item.field_name, item.code) for item in located.failures],
            [
                ("<input:1>", "<record>", "RECORD_TYPE"),
                ("<input:2>", "<record_id>", "INVALID_IDENTIFIER"),
                ("bad-source", "<source_path>", "SOURCE_CITATION"),
                ("empty", "<record>", "EMPTY_RECORD"),
                ("field-type", "<field:0>", "FIELD_TYPE"),
                ("field-name", "<field:0>", "INVALID_FIELD_NAME"),
                ("duplicate-field", "count", "DUPLICATE_FIELD"),
                ("unknown-class", "value", "UNKNOWN_FIELD_CLASS"),
                ("invalid-value", "count", "INVALID_VALUE"),
                ("<input:10>", "<record>", "RECORD_TYPE"),
                ("two-failures", "count", "INVALID_VALUE"),
                ("two-failures", "lifecycle", "INVALID_VALUE"),
                ("fresh", "<record>", "DUPLICATE_RECORD"),
                ("<input:13>", "<record_id>", "INVALID_IDENTIFIER"),
            ],
        )
        self.assertEqual(
            {item.code for item in located.failures} - {"DUPLICATE_RECORD"},
            {
                "RECORD_TYPE",
                "INVALID_IDENTIFIER",
                "SOURCE_CITATION",
                "EMPTY_RECORD",
                "FIELD_TYPE",
                "INVALID_FIELD_NAME",
                "DUPLICATE_FIELD",
                "UNKNOWN_FIELD_CLASS",
                "INVALID_VALUE",
            },
        )
        self.assertNotIn("<unknown>", {item.record_id for item in located.failures})
        self.assertEqual((located.attempted, located.accepted, located.rejected), (14, 1, 13))
        self.assertEqual(located.rejected, len({item.record_id for item in located.failures}))
        self.assertNotEqual(located.rejected, len(located.failures))
        self.assertEqual(located.attempted, located.accepted + located.rejected)
        self.assertEqual(located.accepted_record_ids, ("fresh",))
        self.assertEqual(
            [(row.record_id, row.fields[0].value) for row in self.store.read_all()],
            [("accepted", "0"), ("fresh", "2")],
        )

    def test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary(self) -> None:
        """VER-006: three future shapes send one shared corpus and receive identical rejection."""
        def reconciler(key: str, fields: tuple[MetadataField, ...]) -> MetadataRecord:
            return MetadataRecord(
                f"reconciler-{key}",
                RepositoryPath("projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md"),
                fields,
                ShaDigest(ShaAlgorithm.SHA1, "d" * 40),
            )

        def presence(key: str, fields: tuple[MetadataField, ...]) -> MetadataRecord:
            return MetadataRecord(f"presence-{key}", RepositoryPath("projects/pec/presence/worktree.json"), fields)

        def event(key: str, fields: tuple[MetadataField, ...]) -> MetadataRecord:
            return MetadataRecord(
                f"event-{key}",
                RepositoryPath("projects/pec/loop/LOOP_RECEIPTS.md"),
                fields,
                ShaDigest(ShaAlgorithm.SHA256, "e" * 64),
            )

        corpus = rejection_corpus()
        observed: dict[str, dict[str, tuple[tuple[str, str, str | None], ...]]] = {}
        for shape_name, shape in (("reconciler", reconciler), ("presence", presence), ("event", event)):
            result = self.store.admit_batch(tuple(shape(key, fields) for key, fields in corpus))
            self.assertEqual((result.attempted, result.accepted, result.rejected), (len(corpus), 0, len(corpus)))
            per_fixture = {
                key: tuple(
                    (failure.field_name, failure.code, failure.constraint)
                    for failure in result.failures
                    if failure.record_id == f"{shape_name}-{key}"
                )
                for key, _ in corpus
            }
            self.assertEqual(sum(len(entries) for entries in per_fixture.values()), len(result.failures))
            observed[shape_name] = per_fixture

        expected = {
            "file-body": (("state", "INVALID_VALUE", "CON-001"),),
            "diff-hunk": (("metadata", "INVALID_VALUE", "CON-001"),),
            "register-prose": (("path", "INVALID_VALUE", None),),
            "unknown": (("value", "UNKNOWN_FIELD_CLASS", None),),
            "mixed": (("prose", "INVALID_VALUE", "CON-001"),),
            "multiline-path": (("locator", "INVALID_VALUE", None),),
        }
        self.assertEqual(observed["reconciler"], expected)
        self.assertEqual(observed["presence"], expected)
        self.assertEqual(observed["event"], expected)
        self.assertEqual(self.store.read_all(), ())
        self.assert_no_persisted_residue(
            (*CORPUS_PAYLOADS, *(f"{shape}-{key}" for shape in observed for key, _ in corpus))
        )

    def test_ver_008_policy_is_fixed_finite_and_domain_checked(self) -> None:
        """VER-008: field classes and state vocabulary are finite and non-extensible by callers."""
        self.assertEqual({item.value for item in FieldClass}, {"path", "count", "sha", "state", "hash"})
        self.assertEqual(
            {item.value for item in KnownState},
            {"OPEN", "INITIALIZED", "SEMANTIC_READY", "IN_PROGRESS", "CHECKING", "ISSUED"},
        )
        self.assertEqual(len(inspect.signature(ContentMinimalGuard).parameters), 0)
        invalid_values = (
            MetadataField("negative", FieldClass.COUNT, -1),
            MetadataField("boolean", FieldClass.COUNT, False),
            MetadataField("raw_path", FieldClass.PATH, "projects/pec/file"),
            MetadataField("raw_sha", FieldClass.SHA, "a" * 64),
            MetadataField("raw_hash", FieldClass.HASH, "b" * 64),
            MetadataField("raw_state", FieldClass.STATE, "IN_PROGRESS"),
            MetadataField("conforming", FieldClass.COUNT, ConformingInt(3)),
        )
        for index, field in enumerate(invalid_values):
            with self.subTest(field=field.name):
                decision = ContentMinimalGuard().guard(self.record(f"invalid-{index}", field))
                self.assertFalse(decision.accepted)
                self.assertEqual(decision.failures[0].field_name, field.name)
        over_segment = "x/" + "y" * 256
        over_total = "y/" * 2048 + "y"
        over_segment_multibyte = "x/" + "\u00e9" * 128
        self.assertEqual(len(over_total.encode("utf-8")), 4097)
        self.assertEqual(len(over_segment_multibyte.split("/")[1].encode("utf-8")), 256)
        over_total_multibyte = "/".join(["\u00e9" * 127] * 16) + "/" + "y" * 17
        self.assertEqual(len(over_total_multibyte.encode("utf-8")), 4097)
        self.assertLessEqual(len(over_total_multibyte), 4096)
        self.assertLessEqual(max(len(part.encode("utf-8")) for part in over_total_multibyte.split("/")), 255)
        bad_paths = (
            "/absolute",
            "../escape",
            "a/../b",
            "a//b",
            "a\\b",
            "./a",
            "a\nb",
            "a\rb",
            "a\tb",
            "a\x00b",
            "a\x7fb",
            "a\x85b",
            "a\u2028b",
            "a\u2029b",
            "a\ud800b",
            over_segment,
            over_total,
            over_segment_multibyte,
            over_total_multibyte,
        )
        for bad_path in bad_paths:
            with self.subTest(path=repr(bad_path)[:40]):
                with self.assertRaises(ValueError):
                    RepositoryPath(bad_path)
                decision = ContentMinimalGuard().guard(
                    MetadataRecord(
                        "bad-path",
                        forged_path(bad_path),
                        (MetadataField("locator", FieldClass.PATH, forged_path(bad_path)),),
                    )
                )
                self.assertFalse(decision.accepted)
                self.assertEqual(
                    {(failure.record_id, failure.field_name, failure.code) for failure in decision.failures},
                    {("bad-path", "<source_path>", "SOURCE_CITATION"), ("bad-path", "locator", "INVALID_VALUE")},
                )
        full_segment = "x/" + "y" * 255
        full_total = "y/" * 2047 + "yy"
        full_segment_multibyte = "x/" + "\u00e9" * 127 + "y"
        self.assertEqual(len(full_total.encode("utf-8")), 4096)
        self.assertEqual(len(full_segment_multibyte.split("/")[1].encode("utf-8")), 255)
        for good_path in ("docs/a b.md", full_segment, full_total, full_segment_multibyte):
            with self.subTest(admitted=repr(good_path)[:40]):
                path = RepositoryPath(good_path)
                decision = ContentMinimalGuard().guard(
                    MetadataRecord("good-path", path, (MetadataField("locator", FieldClass.PATH, path),))
                )
                self.assertTrue(decision.accepted)
                assert decision.record is not None
                self.assertEqual(decision.record.source_path, good_path)
                self.assertEqual(decision.record.fields[0].value, good_path)
        with self.assertRaises(ValueError):
            ShaDigest(ShaAlgorithm.SHA256, "A" * 64)
        with self.assertRaises(ValueError):
            ContentHash(HashAlgorithm.BLAKE2B_256, "a" * 63)
        with self.assertRaises(ValueError):
            RepositoryPath(SubclassPayload("docs/readme.md"))
        with self.assertRaises(ValueError):
            RepositoryPath(MethodLiar("../../etc/passwd"))
        with self.assertRaises(ValueError):
            ShaDigest(ShaAlgorithm.SHA1, SubclassPayload("b" * 40))
        with self.assertRaises(ValueError):
            ContentHash(HashAlgorithm.BLAKE2B_256, SubclassPayload("c" * 64))

        guard_path = SRC_ROOT / "pec_v2" / "core" / "content_minimal_guard.py"
        guard_tree = ast.parse(guard_path.read_text(encoding="utf-8"), filename=str(guard_path))
        loose_type_checks = [
            node.lineno
            for node in ast.walk(guard_tree)
            if isinstance(node, ast.Call)
            and (
                (isinstance(node.func, ast.Name) and node.func.id == "isinstance")
                or (isinstance(node.func, ast.Attribute) and node.func.attr == "isinstance")
            )
            and (
                len(node.args) < 2
                or {"str", "int", "tuple"}
                & {inner.id for inner in ast.walk(node.args[1]) if isinstance(inner, ast.Name)}
            )
        ]
        self.assertEqual(loose_type_checks, [], "guard must use exact type checks for str, int, and tuple")

    def test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing(self) -> None:
        """VER-004/008: forged typed shells cannot bypass admission domains."""
        def forged(wrapper_type: type[object], **attributes: object) -> object:
            value = object.__new__(wrapper_type)
            for name, attribute in attributes.items():
                object.__setattr__(value, name, attribute)
            return value

        forged_state = str.__new__(KnownState, "PROSE")
        object.__setattr__(forged_state, "_name_", "FORGED")
        object.__setattr__(forged_state, "_value_", "PROSE")

        field_cases = (
            ("forged-path", FieldClass.PATH, forged(RepositoryPath, value="../escape")),
            ("missing-path", FieldClass.PATH, forged(RepositoryPath)),
            ("sha-algorithm", FieldClass.SHA, forged(ShaDigest, algorithm="sha256", hex_digest="a" * 64)),
            ("sha-digest", FieldClass.SHA, forged(ShaDigest, algorithm=ShaAlgorithm.SHA256, hex_digest="A" * 64)),
            ("missing-sha", FieldClass.SHA, forged(ShaDigest, algorithm=ShaAlgorithm.SHA256)),
            ("hash-algorithm", FieldClass.HASH, forged(ContentHash, algorithm="blake2b-256", hex_digest="b" * 64)),
            ("hash-digest", FieldClass.HASH, forged(ContentHash, algorithm=HashAlgorithm.BLAKE2B_256, hex_digest="b" * 63)),
            ("missing-hash", FieldClass.HASH, forged(ContentHash, algorithm=HashAlgorithm.BLAKE2B_256)),
            ("forged-state", FieldClass.STATE, forged_state),
            ("multiline-path", FieldClass.PATH, forged(RepositoryPath, value=MULTILINE_PATH_FIXTURE)),
        )
        candidates = tuple(
            self.record(
                f"forged-{index}",
                MetadataField(name, field_class, cast(object, value)),
            )
            for index, (name, field_class, value) in enumerate(field_cases)
        )
        forged_source_path = MetadataRecord(
            "forged-source-path",
            cast(RepositoryPath, forged(RepositoryPath, value="../../prose")),
            (MetadataField("count", FieldClass.COUNT, 1),),
        )
        forged_source_sha = MetadataRecord(
            "forged-source-sha",
            RepositoryPath("projects/pec/source.md"),
            (MetadataField("count", FieldClass.COUNT, 1),),
            cast(ShaDigest, forged(ShaDigest, algorithm="sha256", hex_digest="c" * 64)),
        )
        forged_multiline_source_path = MetadataRecord(
            "forged-multiline-source-path",
            cast(RepositoryPath, forged(RepositoryPath, value=MULTILINE_PATH_FIXTURE)),
            (MetadataField("count", FieldClass.COUNT, 1),),
        )

        result = self.store.admit_batch(
            (*candidates, forged_source_path, forged_source_sha, forged_multiline_source_path)
        )
        self.assertEqual((result.attempted, result.accepted, result.rejected), (13, 0, 13))
        self.assertEqual(self.store.read_all(), ())
        self.assertEqual(
            {(failure.record_id, failure.field_name) for failure in result.failures},
            {
                *{(f"forged-{index}", name) for index, (name, _, _) in enumerate(field_cases)},
                ("forged-source-path", "<source_path>"),
                ("forged-source-sha", "<source_sha>"),
                ("forged-multiline-source-path", "<source_path>"),
            },
        )
        multiline_index = len(field_cases) - 1
        self.assertEqual(
            {
                (failure.record_id, failure.field_name, failure.code)
                for failure in result.failures
                if failure.record_id in {f"forged-{multiline_index}", "forged-multiline-source-path"}
            },
            {
                (f"forged-{multiline_index}", "multiline-path", "INVALID_VALUE"),
                ("forged-multiline-source-path", "<source_path>", "SOURCE_CITATION"),
            },
        )
        self.assert_no_persisted_residue(
            (MULTILINE_PATH_FIXTURE, "line one", "+line two", "../escape", "../../prose", "PROSE")
        )

        # D-PEC-89 R9/R10: non-exact caller strings and containers, and invalid identifiers.
        count = MetadataField("count", FieldClass.COUNT, 1)
        valid_source = RepositoryPath("projects/pec/source.md")
        exact_type_batch: tuple[object, ...] = (
            MetadataRecord(cast(str, SubclassPayload("subclass-record-id")), valid_source, (count,)),
            self.record("subclass-field-name", MetadataField(cast(str, SubclassPayload("count")), FieldClass.COUNT, 1)),
            MetadataRecord(
                "subclass-source-path",
                cast(RepositoryPath, forged(RepositoryPath, value=SubclassPayload("docs/source.md"))),
                (count,),
            ),
            MetadataRecord(
                "subclass-source-sha",
                valid_source,
                (count,),
                cast(ShaDigest, forged(ShaDigest, algorithm=ShaAlgorithm.SHA256, hex_digest=SubclassPayload("a" * 64))),
            ),
            self.record(
                "subclass-path",
                MetadataField("locator", FieldClass.PATH, cast(object, forged(RepositoryPath, value=SubclassPayload("docs/a.md")))),
            ),
            self.record(
                "subclass-sha",
                MetadataField(
                    "commit",
                    FieldClass.SHA,
                    cast(object, forged(ShaDigest, algorithm=ShaAlgorithm.SHA1, hex_digest=SubclassPayload("b" * 40))),
                ),
            ),
            self.record(
                "subclass-hash",
                MetadataField(
                    "snapshot",
                    FieldClass.HASH,
                    cast(object, forged(ContentHash, algorithm=HashAlgorithm.BLAKE2B_256, hex_digest=SubclassPayload("c" * 64))),
                ),
            ),
            self.record(
                "liar-path",
                MetadataField("locator", FieldClass.PATH, cast(object, forged(RepositoryPath, value=MethodLiar("../../etc/passwd")))),
            ),
            MetadataRecord(
                "liar-source-path",
                cast(RepositoryPath, forged(RepositoryPath, value=MethodLiar("../../etc/passwd"))),
                (count,),
            ),
            self.record(
                "length-liar",
                MetadataField(
                    "commit",
                    FieldClass.SHA,
                    cast(object, forged(ShaDigest, algorithm=ShaAlgorithm.SHA1, hex_digest=LengthLiar("d" * 400))),
                ),
            ),
            MetadataRecord("lying-tuple", valid_source, cast(tuple[MetadataField, ...], LyingTuple((count,)))),
            MetadataRecord(cast(str, ClassSpoof()), valid_source, (count,)),
            MetadataRecord(SUBCLASS_PAYLOAD, valid_source, (count,)),
            self.record("payload-field-name", MetadataField(SUBCLASS_PAYLOAD, FieldClass.COUNT, 1)),
        )
        exact = self.store.admit_batch(cast(tuple[MetadataRecord, ...], exact_type_batch))
        self.assertEqual((exact.attempted, exact.accepted, exact.rejected), (14, 0, 14))
        self.assertEqual(
            [(failure.record_id, failure.field_name, failure.code) for failure in exact.failures],
            [
                ("<input:0>", "<record_id>", "INVALID_IDENTIFIER"),
                ("subclass-field-name", "<field:0>", "INVALID_FIELD_NAME"),
                ("subclass-source-path", "<source_path>", "SOURCE_CITATION"),
                ("subclass-source-sha", "<source_sha>", "SOURCE_CITATION"),
                ("subclass-path", "locator", "INVALID_VALUE"),
                ("subclass-sha", "commit", "INVALID_VALUE"),
                ("subclass-hash", "snapshot", "INVALID_VALUE"),
                ("liar-path", "locator", "INVALID_VALUE"),
                ("liar-source-path", "<source_path>", "SOURCE_CITATION"),
                ("length-liar", "commit", "INVALID_VALUE"),
                ("lying-tuple", "<record>", "EMPTY_RECORD"),
                ("<input:11>", "<record_id>", "INVALID_IDENTIFIER"),
                ("<input:12>", "<record_id>", "INVALID_IDENTIFIER"),
                ("payload-field-name", "<field:0>", "INVALID_FIELD_NAME"),
            ],
        )
        for failure in exact.failures:
            for attribute in ("record_id", "field_name", "code", "message", "constraint"):
                value = getattr(failure, attribute)
                if attribute == "constraint" and value is None:
                    continue
                with self.subTest(failure=failure.code, attribute=attribute):
                    self.assertIs(type(value), str)
                    for rendering in (value, f"{value}", repr(value)):
                        self.assertNotIn("SECRET FILE BODY", rendering)
                        self.assertNotIn("+diff line two", rendering)
        self.assertEqual(self.store.read_all(), ())
        self.assert_no_persisted_residue(
            (SUBCLASS_PAYLOAD, "SECRET FILE BODY", "+diff line two", "etc/passwd", "d" * 400)
        )


if __name__ == "__main__":
    unittest.main()
