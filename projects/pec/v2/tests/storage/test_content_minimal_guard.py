from __future__ import annotations

import inspect
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import cast


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
        candidates = (
            self.record("file-body", MetadataField("state", FieldClass.STATE, "full file body")),
            self.record("diff-hunk", MetadataField("metadata", FieldClass.STATE, "@@ -1 +1 @@")),
            self.record("register-prose", MetadataField("path", FieldClass.PATH, "owner directed prose")),
            self.record("unknown", MetadataField("value", cast(FieldClass, "content"), "payload")),
            self.record(
                "mixed",
                MetadataField("count", FieldClass.COUNT, 1),
                MetadataField("prose", FieldClass.STATE, "looks approved"),
            ),
        )
        result = self.store.admit_batch(candidates)
        self.assertEqual((result.attempted, result.accepted, result.rejected), (5, 0, 5))
        self.assertEqual(self.store.read_all(), ())
        self.assertEqual({failure.record_id for failure in result.failures}, {row.record_id for row in candidates})

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

    def test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary(self) -> None:
        """VER-006: three future shapes receive identical fixed-policy rejection."""
        def reconciler() -> MetadataRecord:
            return self.record("reconciler", MetadataField("state", FieldClass.STATE, "parsed prose"))

        def presence() -> MetadataRecord:
            return self.record("presence", MetadataField("state", FieldClass.STATE, "heartbeat narrative"))

        def event() -> MetadataRecord:
            return self.record("event", MetadataField("state", FieldClass.STATE, "event payload"))

        results = [self.store.admit_batch((factory(),)) for factory in (reconciler, presence, event)]
        self.assertEqual([(item.accepted, item.rejected) for item in results], [(0, 1)] * 3)
        self.assertEqual({item.failures[0].constraint for item in results}, {"CON-001"})
        self.assertEqual(self.store.read_all(), ())

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
        )
        for index, field in enumerate(invalid_values):
            with self.subTest(field=field.name):
                decision = ContentMinimalGuard().guard(self.record(f"invalid-{index}", field))
                self.assertFalse(decision.accepted)
                self.assertEqual(decision.failures[0].field_name, field.name)
        for bad_path in ("/absolute", "../escape", "a/../b", "a//b", "a\\b", "./a"):
            with self.subTest(path=bad_path):
                with self.assertRaises(ValueError):
                    RepositoryPath(bad_path)
        with self.assertRaises(ValueError):
            ShaDigest(ShaAlgorithm.SHA256, "A" * 64)
        with self.assertRaises(ValueError):
            ContentHash(HashAlgorithm.BLAKE2B_256, "a" * 63)

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

        result = self.store.admit_batch((*candidates, forged_source_path, forged_source_sha))
        self.assertEqual((result.attempted, result.accepted, result.rejected), (11, 0, 11))
        self.assertEqual(self.store.read_all(), ())
        self.assertEqual(
            {(failure.record_id, failure.field_name) for failure in result.failures},
            {
                *{(f"forged-{index}", name) for index, (name, _, _) in enumerate(field_cases)},
                ("forged-source-path", "<source_path>"),
                ("forged-source-sha", "<source_sha>"),
            },
        )


if __name__ == "__main__":
    unittest.main()
