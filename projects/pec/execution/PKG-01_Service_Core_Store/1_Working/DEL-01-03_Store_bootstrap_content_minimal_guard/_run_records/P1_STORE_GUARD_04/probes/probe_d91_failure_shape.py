"""D-PEC-91 R15 failure-shape check (P1_STORE_GUARD_04 author evidence).

Usage: PYTHONDONTWRITEBYTECODE=1 python3 probe_d91_failure_shape.py <path-to-v2-tree>

Prints the full AdmissionFailure (record, field, code, message, constraint)
for an over-domain COUNT (2**53 and 10**5000) and for the preexisting -1
case, so the out-of-domain path can be compared with the existing else-branch
shape: INVALID_VALUE at the field name, message "value does not satisfy the
runtime domain for count", no constraint. Guard only; no store is created.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.dont_write_bytecode = True


def main() -> int:
    tree = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(tree / "src"))
    from pec_v2.core.content_minimal_guard import (
        ContentMinimalGuard,
        FieldClass,
        MetadataField,
        MetadataRecord,
        RepositoryPath,
    )

    print(f"probe_d91_failure_shape: v2 tree {tree}")
    for label, value in (("-1", -1), ("2**53", 2**53), ("10**5000", 10**5000)):
        decision = ContentMinimalGuard().guard(
            MetadataRecord("r", RepositoryPath("projects/pec/source.md"), (MetadataField("n", FieldClass.COUNT, value),))
        )
        shapes = [
            (failure.record_id, failure.field_name, failure.code, failure.message, failure.constraint)
            for failure in decision.failures
        ]
        print(f"COUNT {label}: accepted={decision.accepted} failures={shapes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
