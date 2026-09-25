"""D-PEC-91 (A-53) F-1 reproduction probe (P1_STORE_GUARD_04 author evidence).

Usage: PYTHONDONTWRITEBYTECODE=1 python3 probe_d91.py <path-to-v2-tree>

Imports the guard and the SQLite adapter from <v2-tree>/src (read only) and,
at interpreter integer-to-string digit limits default (4300), 640 and 0,
exercises ContentMinimalGuard().guard() and SqliteMetadataStore.admit_batch
((good, big)) on COUNT values. Every store lives in a fresh temporary Git
checkout outside the repository, removed on exit. Values are labelled by
name so the probe itself never renders an oversized int. For each case it
reports admitted + rendered value (digit count and, when short, the text), a
located failure tuple, or the escaping exception type, and for admit_batch
also what persisted (read back through a fresh store handle).
"""

from __future__ import annotations

import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True


class SubInt(int):
    """An int subclass (must be rejected under the exact-type rule)."""


VALUES = (
    ("2**53 - 1", 2**53 - 1),
    ("2**53", 2**53),
    ("2**63", 2**63),
    ("2**64", 2**64),
    ("10**639", 10**639),
    ("10**4300", 10**4300),
    ("10**5000", 10**5000),
    ("-1", -1),
    ("True", True),
    ("SubInt(5)", SubInt(5)),
)
LIMITS = (("default", None), ("640", 640), ("0", 0))


def describe_text(text: str) -> str:
    return f"rendered {text!r}" if len(text) <= 24 else f"rendered {len(text)}-char text"


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: probe_d91.py <path-to-v2-tree>")
    tree = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(tree / "src"))
    from pec_v2.adapters.storage.sqlite_store import SqliteMetadataStore
    from pec_v2.core.content_minimal_guard import (
        ContentMinimalGuard,
        FieldClass,
        MetadataField,
        MetadataRecord,
        RepositoryPath,
        ShaAlgorithm,
        ShaDigest,
    )

    print(f"probe_d91: v2 tree {tree}")
    print(f"interpreter {sys.executable} {sys.version.split()[0]}; sqlite {sqlite3.sqlite_version}")
    default_limit = sys.get_int_max_str_digits()
    print(f"default int max str digits {default_limit}; smallest nonzero {sys.int_info.str_digits_check_threshold}")

    def record(record_id: str, value: object) -> MetadataRecord:
        return MetadataRecord(
            record_id=record_id,
            source_path=RepositoryPath("projects/pec/execution/source.json"),
            source_sha=ShaDigest(ShaAlgorithm.SHA256, "a" * 64),
            fields=(MetadataField("items", FieldClass.COUNT, value),),
        )

    def failures_of(items) -> list[tuple[str, str, str]]:  # type: ignore[no-untyped-def]
        return [(item.record_id, item.field_name, item.code) for item in items]

    with tempfile.TemporaryDirectory(prefix="probe_d91_") as scratch:
        scratch_root = Path(scratch)
        case = 0
        try:
            for limit_name, limit in LIMITS:
                sys.set_int_max_str_digits(default_limit if limit is None else limit)
                print(f"== limit {limit_name} (sys.get_int_max_str_digits() = {sys.get_int_max_str_digits()})")
                for label, value in VALUES:
                    try:
                        decision = ContentMinimalGuard().guard(record("r", value))
                    except Exception as error:  # noqa: BLE001
                        guard_out = f"RAISES {type(error).__name__}"
                    else:
                        if decision.accepted:
                            assert decision.record is not None
                            guard_out = f"ADMITTED {describe_text(decision.record.fields[0].value)}"
                        else:
                            guard_out = f"LOCATED {failures_of(decision.failures)}"
                    print(f"  guard  COUNT {label:<10} -> {guard_out}")

                    case += 1
                    checkout = scratch_root / f"checkout-{case}"
                    checkout.mkdir()
                    subprocess.run(["git", "init", "-q", str(checkout)], check=True)
                    (checkout / ".gitignore").write_text("/.pec-v2/\n", encoding="utf-8")
                    store = SqliteMetadataStore(checkout)
                    try:
                        result = store.admit_batch((record("good", 1), record("big", value)))
                    except Exception as error:  # noqa: BLE001
                        batch_out = f"RAISES {type(error).__name__}"
                    else:
                        batch_out = (
                            f"(attempted, accepted, rejected)=({result.attempted}, {result.accepted}, {result.rejected}) "
                            f"failures={failures_of(result.failures)}"
                        )
                    store.close()
                    reader = SqliteMetadataStore(checkout)
                    persisted = [
                        (row.record_id, describe_text(row.fields[0].value)) for row in reader.read_all()
                    ]
                    reader.close()
                    print(f"  batch  (good, {label:<10}) -> {batch_out}; persisted={persisted}")
        finally:
            sys.set_int_max_str_digits(default_limit)
    print("probe_d91: done; temporary checkouts removed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
