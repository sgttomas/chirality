"""D-PEC-89 probe battery (P1_STORE_GUARD_03 author evidence).

Usage: python3 probe_d89.py <path-to-v2-tree>

Reimplemented from the probe matrix in
D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md (33 cases).
Every case runs against a fresh temporary Git checkout created with
``tempfile`` (outside any repository checkout). The v2 tree is only imported,
never written; ``sys.dont_write_bytecode`` is set so no ``__pycache__`` is
produced.

A case is OPEN when the defect the matrix names is observable: a record is
admitted, caller text is persisted, an exception other than a port error
escapes, or a returned failure carries a non-exact string or caller text.
It is CLOSED when the input is rejected by a constructor ``ValueError`` or a
located failure with only exact-``str`` attributes and no residue, or (E-2)
when the adapter raises the port-level error chained to the engine/OS error.
C2-4 is expected to stay OPEN: it is outside the guard's threat boundary.
"""

from __future__ import annotations

import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

sys.dont_write_bytecode = True

if len(sys.argv) != 2:
    sys.exit("usage: probe_d89.py <path-to-v2-tree>")
V2 = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(V2 / "src"))

import pec_v2.core.ports.store as port  # noqa: E402
from pec_v2.adapters.storage.sqlite_store import SqliteMetadataStore  # noqa: E402
from pec_v2.core.content_minimal_guard import (  # noqa: E402
    ContentHash,
    FieldClass,
    HashAlgorithm,
    KnownState,
    MetadataField,
    MetadataRecord,
    RepositoryPath,
    ShaAlgorithm,
    ShaDigest,
)

PAYLOAD = "SECRET FILE BODY\n+diff line two"
NEEDLES = ("SECRET FILE BODY", "+diff line two", "etc/passwd")


class Sneaky(str):
    """str subclass whose adaptation and rendering hooks return the payload."""

    def __conform__(self, protocol: object) -> str:
        return PAYLOAD

    def __format__(self, spec: str) -> str:
        return PAYLOAD

    def __str__(self) -> str:
        return PAYLOAD

    def __repr__(self) -> str:
        return PAYLOAD


class Liar(str):
    """str subclass overriding the methods the normalization checks call."""

    def startswith(self, *args: object, **kwargs: object) -> bool:  # type: ignore[override]
        return False

    def __ne__(self, other: object) -> bool:
        return False

    __hash__ = str.__hash__

    def split(self, *args: object, **kwargs: object) -> list[str]:  # type: ignore[override]
        return ["liar"]


class HexLen(str):
    """A 400-character hex buffer whose len() reports 40."""

    def __len__(self) -> int:
        return 40


class ConformingInt(int):
    def __conform__(self, protocol: object) -> str:
        return PAYLOAD


class LyingTuple(tuple):
    """Reports length 1 but iterates nothing."""

    def __len__(self) -> int:
        return 1

    def __iter__(self):  # type: ignore[override]
        return iter(())


class NeverEqual(str):
    """Field-name subclass whose hash/equality never match."""

    def __eq__(self, other: object) -> bool:
        return False

    def __hash__(self) -> int:
        return id(self)


class ClassSpoof:
    """Non-str object whose __class__ property claims to be str."""

    @property  # type: ignore[misc]
    def __class__(self):  # type: ignore[override]
        return str


def forged(wrapper_type: type, **attributes: object) -> object:
    value = object.__new__(wrapper_type)
    for name, attribute in attributes.items():
        object.__setattr__(value, name, attribute)
    return value


def forged_state() -> KnownState:
    state = str.__new__(KnownState, "PROSE")
    object.__setattr__(state, "_name_", "FORGED")
    object.__setattr__(state, "_value_", "PROSE")
    return state


def count_field(name: object = "count") -> MetadataField:
    return MetadataField(name, FieldClass.COUNT, 1)  # type: ignore[arg-type]


def record(
    record_id: object = "probe-1",
    source_path: object = None,
    fields: object = None,
    source_sha: object = None,
) -> MetadataRecord:
    return MetadataRecord(
        record_id,  # type: ignore[arg-type]
        RepositoryPath("docs/source.md") if source_path is None else source_path,  # type: ignore[arg-type]
        (count_field(),) if fields is None else fields,  # type: ignore[arg-type]
        source_sha,  # type: ignore[arg-type]
    )


class Checkout:
    def __enter__(self) -> Path:
        self._temporary = tempfile.TemporaryDirectory(prefix="probe_d89_")
        root = Path(self._temporary.name) / "checkout"
        root.mkdir()
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        (root / ".gitignore").write_text("/.pec-v2/\n", encoding="utf-8")
        self.root = root
        return root

    def __exit__(self, *exc: object) -> None:
        for path in (self.root, *self.root.rglob("*")):
            try:
                if path.is_dir() and not path.is_symlink():
                    os.chmod(path, 0o755)
            except OSError:
                pass
        self._temporary.cleanup()


def safe(value: object) -> str:
    """Render without invoking caller-controlled hooks."""
    if value is None:
        return "None"
    if type(value) is str:
        text = str.__repr__(value)
        return text if len(text) <= 48 else text[:45] + "..."
    return f"<{type(value).__name__}>"


def raw_cells(root: Path) -> tuple[list[object], bytes]:
    database = root / ".pec-v2" / "record_store.sqlite3"
    cells: list[object] = []
    blob = b""
    if database.exists():
        raw = sqlite3.connect(f"{database.as_uri()}?mode=ro", uri=True)
        try:
            for table in ("metadata_records", "metadata_fields"):
                for row in raw.execute(f"SELECT * FROM {table}"):
                    cells.extend(row)
        finally:
            raw.close()
    for suffix in ("", "-journal", "-wal", "-shm"):
        artifact = Path(f"{database}{suffix}")
        if artifact.is_file():
            blob += artifact.read_bytes()
    return cells, blob


def persisted_needles(root: Path) -> list[str]:
    cells, blob = raw_cells(root)
    found = []
    for needle in NEEDLES:
        in_cells = any(isinstance(cell, str) and needle in cell for cell in cells)
        if in_cells or needle.encode("utf-8") in blob:
            found.append(needle)
    return found


def failure_leaks(failures: tuple, forbidden: tuple[str, ...]) -> list[str]:
    leaks = []
    for index, failure in enumerate(failures):
        for attribute in ("record_id", "field_name", "code", "message", "constraint"):
            value = object.__getattribute__(failure, attribute)
            if attribute == "constraint" and value is None:
                continue
            if type(value) is not str:
                leaks.append(f"failure[{index}].{attribute} is {type(value).__name__}")
                continue
            rendered = (value, f"{value}", repr(value))
            if any(text in form for text in forbidden for form in rendered):
                leaks.append(f"failure[{index}].{attribute} echoes caller text")
    return leaks


def guard_case(build, forbidden_echo: tuple[str, ...] = ()) -> tuple[str, bool]:
    """Admit one candidate built by ``build``; return (outcome, is_open)."""
    try:
        candidate = build()
    except ValueError as error:
        return f"constructor ValueError ({safe(str(error))})", False
    except Exception as error:  # noqa: BLE001
        return f"constructor raised {type(error).__name__}", True
    with Checkout() as root:
        store = SqliteMetadataStore(root)
        try:
            try:
                result = store.admit_batch((candidate,))
            except Exception as error:  # noqa: BLE001
                return f"{type(error).__name__} escapes admit_batch", True
            located = [
                (safe(f.record_id), safe(f.field_name), safe(f.code)) for f in result.failures
            ]
            persisted = persisted_needles(root)
            leaks = failure_leaks(result.failures, (*NEEDLES, *forbidden_echo))
            codes = [object.__getattribute__(f, "code") for f in result.failures]
            outcome = f"accepted={result.accepted} rejected={result.rejected} failures={located}"
            if persisted:
                outcome += f" PERSISTED={persisted}"
            if leaks:
                outcome += f" LEAKS={leaks}"
            is_open = (
                result.accepted > 0
                or bool(persisted)
                or bool(leaks)
                or "DUPLICATE_RECORD" in codes
            )
            return outcome, is_open
        finally:
            store.close()


def port_error_outcome(error: BaseException | None, expected: type, cause: type) -> tuple[str, bool]:
    if error is None:
        return "no exception raised", True
    cause_value = error.__cause__
    text = (
        f"raised {type(error).__module__}.{type(error).__name__}"
        f" (cause {type(cause_value).__name__ if cause_value is not None else None})"
    )
    closed = type(error) is expected and isinstance(cause_value, cause)
    if not closed:
        text += " RAW" if not isinstance(error, RuntimeError) else ""
    return text, not closed


# --------------------------------------------------------------------------
# Cases
# --------------------------------------------------------------------------

VALID_PATH = "docs/readme.md"


def e1_01():
    return guard_case(lambda: record(fields=(MetadataField("locator", FieldClass.PATH, RepositoryPath(Sneaky(VALID_PATH))),)))


def e1_02():
    return guard_case(lambda: record(source_path=RepositoryPath(Sneaky(VALID_PATH))))


def e1_03():
    return guard_case(lambda: record(fields=(MetadataField("locator", FieldClass.PATH, forged(RepositoryPath, value=Sneaky(VALID_PATH))),)))


def e1_04():
    return guard_case(lambda: record(source_path=forged(RepositoryPath, value=Sneaky(VALID_PATH))))


def e1_05():
    return guard_case(lambda: record(record_id=Sneaky("probe-1")))


def e1_06():
    return guard_case(lambda: record(fields=(count_field(Sneaky("count")),)))


def e1_07():
    return guard_case(lambda: record(source_sha=ShaDigest(ShaAlgorithm.SHA1, Sneaky("a" * 40))))


def e1_08():
    return guard_case(lambda: record(source_sha=forged(ShaDigest, algorithm=ShaAlgorithm.SHA1, hex_digest=Sneaky("a" * 40))))


def e1_09():
    return guard_case(lambda: record(fields=(MetadataField("commit", FieldClass.SHA, ShaDigest(ShaAlgorithm.SHA1, Sneaky("b" * 40))),)))


def e1_10():
    return guard_case(lambda: record(fields=(MetadataField("commit", FieldClass.SHA, forged(ShaDigest, algorithm=ShaAlgorithm.SHA1, hex_digest=Sneaky("b" * 40))),)))


def e1_11():
    return guard_case(lambda: record(fields=(MetadataField("snapshot", FieldClass.HASH, ContentHash(HashAlgorithm.BLAKE2B_256, Sneaky("c" * 64))),)))


def e1_12():
    return guard_case(lambda: record(fields=(MetadataField("snapshot", FieldClass.HASH, forged(ContentHash, algorithm=HashAlgorithm.BLAKE2B_256, hex_digest=Sneaky("c" * 64))),)))


def c2_2a():
    def build():
        path = RepositoryPath(Liar("../../etc/passwd"))
        return record(source_path=path, fields=(MetadataField("locator", FieldClass.PATH, path),))
    return guard_case(build)


def c2_2b():
    def build():
        path = RepositoryPath(Liar("/etc/passwd"))
        return record(source_path=path, fields=(MetadataField("locator", FieldClass.PATH, path),))
    return guard_case(build)


def c2_2c():
    def build():
        path = forged(RepositoryPath, value=Liar("a/../../etc/passwd"))
        return record(source_path=path, fields=(MetadataField("locator", FieldClass.PATH, path),))
    return guard_case(build)


def len_1():
    return guard_case(lambda: record(fields=(MetadataField("commit", FieldClass.SHA, forged(ShaDigest, algorithm=ShaAlgorithm.SHA1, hex_digest=HexLen("d" * 400))),)))


def cnt_1():
    return guard_case(lambda: record(fields=(MetadataField("items", FieldClass.COUNT, True),)))


def cnt_2():
    return guard_case(lambda: record(fields=(MetadataField("items", FieldClass.COUNT, ConformingInt(3)),)))


def st_1():
    return guard_case(lambda: record(fields=(MetadataField("lifecycle", FieldClass.STATE, forged_state()),)))


def st_2():
    return guard_case(lambda: record(fields=(MetadataField("lifecycle", FieldClass.STATE, Sneaky("IN_PROGRESS")),)))


def fc_1():
    return guard_case(lambda: record(fields=(MetadataField("locator", Sneaky("path"), RepositoryPath(VALID_PATH)),)))  # type: ignore[arg-type]


def tup_1():
    return guard_case(lambda: record(fields=LyingTuple((count_field(),))))


def dup_1():
    return guard_case(lambda: record(fields=(count_field(NeverEqual("count")), MetadataField(NeverEqual("count"), FieldClass.COUNT, 2))))


def spf_1():
    return guard_case(lambda: record(record_id=ClassSpoof()))


def e3_1():
    return guard_case(lambda: record(record_id=PAYLOAD))


def e3_2():
    return guard_case(lambda: record(fields=(count_field(PAYLOAD),)))


def e3_3():
    return guard_case(lambda: record(record_id=Sneaky("bad id!")), forbidden_echo=("bad id!",))


def e3_4():
    return guard_case(lambda: record(fields=(count_field(Sneaky("bad name")),)), forbidden_echo=("bad name",))


def c2_4():
    target = "docs/target.md"

    def adapt(value: str) -> str:
        return PAYLOAD if value == target else value

    sqlite3.register_adapter(str, adapt)
    try:
        outcome, is_open = guard_case(lambda: record(source_path=RepositoryPath(target)))
    finally:
        sqlite3.adapters.pop((str, sqlite3.PrepareProtocol), None)
    return outcome + " [outside the threat boundary by design]", is_open


def e2_1():
    with Checkout() as root:
        store = SqliteMetadataStore(root)
        raised: list[BaseException] = []

        def close_elsewhere() -> None:
            try:
                store.close()
            except BaseException as error:  # noqa: BLE001
                raised.append(error)

        worker = threading.Thread(target=close_elsewhere)
        worker.start()
        worker.join()
        outcome, is_open = port_error_outcome(raised[0] if raised else None, port.StoreDataError, sqlite3.Error)
        try:
            handle_kept = store.read_all() == ()
        except Exception as error:  # noqa: BLE001
            handle_kept = f"read_all {type(error).__name__}"
        try:
            store.close()
            owner_close = "owner close ok"
        except Exception as error:  # noqa: BLE001
            owner_close = f"owner close {type(error).__name__}"
        try:
            store.read_all()
            after = "read_all after owner close succeeded"
        except port.StoreClosedError:
            after = "read_all after owner close -> StoreClosedError"
        return f"{outcome}; handle kept={handle_kept}; {owner_close}; {after}", is_open


def e2_2():
    with Checkout() as root:
        (root / ".pec-v2").write_bytes(b"regular file")
        error = None
        try:
            SqliteMetadataStore(root).close()
        except BaseException as caught:  # noqa: BLE001
            error = caught
        return port_error_outcome(error, port.StoreConfigurationError, OSError)


def e2_3():
    with Checkout() as root:
        store = SqliteMetadataStore(root)
        store.close()
        shutil.rmtree(root / ".pec-v2")
        os.chmod(root, 0o555)
        error = None
        try:
            store.reopen()
        except BaseException as caught:  # noqa: BLE001
            error = caught
        finally:
            os.chmod(root, 0o755)
        outcome, is_open = port_error_outcome(error, port.StoreConfigurationError, OSError)
        state = "closed" if getattr(store, "_connection") is None else "open"
        return f"{outcome}; store {state}", is_open


def e2_4():
    with Checkout() as root:
        store = SqliteMetadataStore(root)
        journal = root / ".pec-v2" / "record_store.sqlite3-journal"
        journal.mkdir()
        error = None
        try:
            store.delete()
        except BaseException as caught:  # noqa: BLE001
            error = caught
        outcome, is_open = port_error_outcome(error, port.StoreDataError, OSError)
        journal.rmdir()
        try:
            store.reset()
            recovered = f"reset then read_all={store.read_all()!r}"
            store.close()
        except Exception as caught:  # noqa: BLE001
            recovered = f"reset {type(caught).__name__}"
        return f"{outcome}; {recovered}", is_open


CASES = (
    ("E1-01", "PATH field, public RepositoryPath(Sneaky)", e1_01),
    ("E1-02", "source_path, public RepositoryPath(Sneaky)", e1_02),
    ("E1-03", "PATH field, forged shell with Sneaky", e1_03),
    ("E1-04", "source_path, forged shell with Sneaky", e1_04),
    ("E1-05", "record ID as Sneaky", e1_05),
    ("E1-06", "field name as Sneaky", e1_06),
    ("E1-07", "source SHA digest, public ShaDigest(Sneaky)", e1_07),
    ("E1-08", "source SHA digest, forged shell with Sneaky", e1_08),
    ("E1-09", "SHA field digest, public ShaDigest(Sneaky)", e1_09),
    ("E1-10", "SHA field digest, forged shell with Sneaky", e1_10),
    ("E1-11", "HASH field digest, public ContentHash(Sneaky)", e1_11),
    ("E1-12", "HASH field digest, forged shell with Sneaky", e1_12),
    ("C2-2a", "public RepositoryPath(Liar('../../etc/passwd'))", c2_2a),
    ("C2-2b", "public RepositoryPath(Liar('/etc/passwd'))", c2_2b),
    ("C2-2c", "forged RepositoryPath(Liar('a/../../etc/passwd'))", c2_2c),
    ("LEN-1", "HexLen SHA1 digest (400 hex, len() says 40)", len_1),
    ("CNT-1", "bool count", cnt_1),
    ("CNT-2", "int subclass count with __conform__", cnt_2),
    ("ST-1", "forged KnownState member", st_1),
    ("ST-2", "Sneaky('IN_PROGRESS') as state", st_2),
    ("FC-1", "Sneaky('path') as field class", fc_1),
    ("TUP-1", "tuple subclass fields: len 1, iterates nothing", tup_1),
    ("DUP-1", "two field names as never-equal str subclass", dup_1),
    ("SPF-1", "non-str record ID with __class__ -> str", spf_1),
    ("E3-1", "exact-str payload as record ID", e3_1),
    ("E3-2", "exact-str payload as field name", e3_2),
    ("E3-3", "invalid Sneaky record ID", e3_3),
    ("E3-4", "invalid Sneaky field name", e3_4),
    ("C2-4", "sqlite3.register_adapter(str) rewrites one exact path", c2_4),
    ("E2-1", "close() from a non-owning thread", e2_1),
    ("E2-2", ".pec-v2 is a regular file at construction", e2_2),
    ("E2-3", "reopen() in a read-only checkout", e2_3),
    ("E2-4", "delete() with a sidecar name that is a directory", e2_4),
)


def main() -> int:
    print(f"probe_d89: v2 tree {V2}")
    print(f"interpreter {sys.executable} {sys.version.split()[0]}")
    open_ids = []
    for case_id, description, run in CASES:
        try:
            outcome, is_open = run()
        except Exception as error:  # noqa: BLE001
            outcome, is_open = f"probe harness error {type(error).__name__}: {safe(str(error))}", True
        status = "OPEN" if is_open else "CLOSED"
        if is_open:
            open_ids.append(case_id)
        print(f"{case_id:<6} {status:<6} {description} :: {outcome}")
    print(f"TOTAL OPEN {len(open_ids)} / {len(CASES)}: {', '.join(open_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
