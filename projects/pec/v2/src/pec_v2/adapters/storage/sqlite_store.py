"""Standard-library SQLite adapter for guarded PEC metadata envelopes."""

from __future__ import annotations

import sqlite3
import subprocess
from pathlib import Path
from typing import Iterable

from ...core.content_minimal_guard import (
    AdmissionFailure,
    ContentMinimalGuard,
    FieldClass,
    GuardedField,
    GuardedRecord,
    MetadataRecord,
)
from ...core.ports.store import AdmissionResult, StoreClosedError


_STORE_DIRECTORY = ".pec-v2"
_STORE_FILENAME = "record_store.sqlite3"
_IGNORE_RULE = "/.pec-v2/"
_DATABASE_SUFFIXES = ("", "-journal", "-shm", "-wal")


class StoreConfigurationError(RuntimeError):
    """The checkout does not provide the required gitignore boundary."""


class StoreDataError(RuntimeError):
    """Stored bytes do not satisfy the guarded metadata envelope."""


class SqliteMetadataStore:
    """Disposable store rooted at the fixed project-local default location."""

    def __init__(self, checkout_root: str | Path) -> None:
        self._checkout_root = Path(checkout_root).resolve()
        self._database_path = self._checkout_root / _STORE_DIRECTORY / _STORE_FILENAME
        self._connection: sqlite3.Connection | None = None
        self._guard = ContentMinimalGuard()
        self.reopen()

    def admit_batch(self, records: Iterable[MetadataRecord]) -> AdmissionResult:
        connection = self._require_open()
        candidates = tuple(records)
        accepted_ids: list[str] = []
        failures: list[AdmissionFailure] = []
        decisions = [self._guard.guard(candidate) for candidate in candidates]

        connection.execute("BEGIN IMMEDIATE")
        try:
            for index, decision in enumerate(decisions):
                if not decision.accepted:
                    failures.extend(decision.failures)
                    continue
                record = decision.record
                assert record is not None
                savepoint = f"record_{index}"
                connection.execute(f"SAVEPOINT {savepoint}")
                try:
                    self._insert_guarded(connection, record)
                except sqlite3.IntegrityError:
                    connection.execute(f"ROLLBACK TO {savepoint}")
                    failures.append(
                        AdmissionFailure(
                            record.record_id,
                            "<record>",
                            "DUPLICATE_RECORD",
                            "record id already exists; existing data was preserved",
                        )
                    )
                else:
                    accepted_ids.append(record.record_id)
                finally:
                    connection.execute(f"RELEASE {savepoint}")
            connection.commit()
        except BaseException:
            connection.rollback()
            raise

        attempted = len(candidates)
        accepted = len(accepted_ids)
        return AdmissionResult(
            attempted=attempted,
            accepted=accepted,
            rejected=attempted - accepted,
            accepted_record_ids=tuple(accepted_ids),
            failures=tuple(failures),
        )

    def read_all(self) -> tuple[GuardedRecord, ...]:
        connection = self._require_open()
        record_rows = connection.execute(
            "SELECT record_id, source_path, source_sha_algorithm, source_sha_digest "
            "FROM metadata_records ORDER BY record_id"
        ).fetchall()
        output: list[GuardedRecord] = []
        for record_id, source_path, sha_algorithm, sha_digest in record_rows:
            field_rows = connection.execute(
                "SELECT name, field_class, value FROM metadata_fields "
                "WHERE record_id = ? ORDER BY ordinal",
                (record_id,),
            ).fetchall()
            try:
                fields = tuple(
                    GuardedField(name, FieldClass(field_class), value)
                    for name, field_class, value in field_rows
                )
            except (TypeError, ValueError) as error:
                raise StoreDataError(f"stored record {record_id!r} has an invalid field envelope") from error
            output.append(
                GuardedRecord(record_id, source_path, sha_algorithm, sha_digest, fields)
            )
        return tuple(output)

    def close(self) -> None:
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def reopen(self) -> None:
        if self._connection is not None:
            return
        self._verify_ignore_rule()
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self._database_path)
        try:
            connection.execute("PRAGMA foreign_keys = ON")
            connection.execute("PRAGMA journal_mode = WAL")
            self._create_schema(connection)
            connection.commit()
        except BaseException:
            connection.close()
            raise
        self._connection = connection

    def delete(self) -> None:
        self.close()
        for suffix in _DATABASE_SUFFIXES:
            try:
                Path(f"{self._database_path}{suffix}").unlink()
            except FileNotFoundError:
                pass

    def reset(self) -> None:
        self.delete()
        self.reopen()

    def _require_open(self) -> sqlite3.Connection:
        if self._connection is None:
            raise StoreClosedError("metadata store is closed")
        return self._connection

    def _verify_ignore_rule(self) -> None:
        ignore_path = self._checkout_root / ".gitignore"
        try:
            rules = ignore_path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as error:
            raise StoreConfigurationError(
                f"checkout ignore file is absent or unreadable: {ignore_path}"
            ) from error
        if _IGNORE_RULE not in (line.strip() for line in rules):
            raise StoreConfigurationError(
                f"required checked-in ignore rule {_IGNORE_RULE!r} is absent from {ignore_path}"
            )
        try:
            tracked = subprocess.run(
                ["git", "-C", str(self._checkout_root), "ls-files", "--", _STORE_DIRECTORY],
                check=False,
                capture_output=True,
                text=True,
            )
        except OSError as error:
            raise StoreConfigurationError(
                "tracked store-artifact status could not be verified"
            ) from error
        if tracked.returncode != 0:
            detail = tracked.stderr.strip()
            raise StoreConfigurationError(
                "tracked store-artifact status could not be verified"
                + (f": {detail}" if detail else "")
            )
        tracked_paths = tuple(line for line in tracked.stdout.splitlines() if line)
        if tracked_paths:
            raise StoreConfigurationError(
                "tracked store artifact is forbidden: " + ", ".join(tracked_paths)
            )
        candidates = (
            f"{_STORE_DIRECTORY}/{_STORE_FILENAME}",
            f"{_STORE_DIRECTORY}/{_STORE_FILENAME}-journal",
            f"{_STORE_DIRECTORY}/{_STORE_FILENAME}-shm",
            f"{_STORE_DIRECTORY}/{_STORE_FILENAME}-wal",
            f"{_STORE_DIRECTORY}/write.tmp",
        )
        for candidate in candidates:
            try:
                result = subprocess.run(
                    [
                        "git",
                        "-C",
                        str(self._checkout_root),
                        "check-ignore",
                        "--no-index",
                        "-q",
                        "--",
                        candidate,
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                )
            except OSError as error:
                raise StoreConfigurationError(
                    "effective Git ignore policy could not be verified"
                ) from error
            if result.returncode != 0:
                detail = result.stderr.strip()
                raise StoreConfigurationError(
                    f"effective Git ignore policy does not cover {candidate!r}"
                    + (f": {detail}" if detail else "")
                )

    @staticmethod
    def _create_schema(connection: sqlite3.Connection) -> None:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS metadata_records (
                record_id TEXT PRIMARY KEY,
                source_path TEXT NOT NULL,
                source_sha_algorithm TEXT,
                source_sha_digest TEXT,
                CHECK ((source_sha_algorithm IS NULL) = (source_sha_digest IS NULL))
            );
            CREATE TABLE IF NOT EXISTS metadata_fields (
                record_id TEXT NOT NULL REFERENCES metadata_records(record_id) ON DELETE CASCADE,
                ordinal INTEGER NOT NULL CHECK (ordinal >= 0),
                name TEXT NOT NULL,
                field_class TEXT NOT NULL CHECK (field_class IN ('path', 'count', 'sha', 'state', 'hash')),
                value TEXT NOT NULL,
                PRIMARY KEY (record_id, name),
                UNIQUE (record_id, ordinal)
            );
            """
        )

    @staticmethod
    def _insert_guarded(connection: sqlite3.Connection, record: GuardedRecord) -> None:
        connection.execute(
            "INSERT INTO metadata_records "
            "(record_id, source_path, source_sha_algorithm, source_sha_digest) VALUES (?, ?, ?, ?)",
            (
                record.record_id,
                record.source_path,
                record.source_sha_algorithm,
                record.source_sha_digest,
            ),
        )
        connection.executemany(
            "INSERT INTO metadata_fields (record_id, ordinal, name, field_class, value) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                (record.record_id, index, field.name, field.field_class.value, field.value)
                for index, field in enumerate(record.fields)
            ),
        )
