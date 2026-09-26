#!/usr/bin/env python3
"""Preparation aid: build the bound D-PEC-96 act script from reviewed postimage trees.

Usage: build_apply_d96.py <post-tree A> <post-tree A-R overrides> <preimages.txt> <out apply_d96.py>
"""

from __future__ import annotations

import base64
import hashlib
import sys
from pathlib import Path

PEC = "projects/pec/"
MODIFIED = [
    "v2/config/loops.json",
    "v2/config/loops.schema.json",
    "v2/src/pec_v2/core/ports/loop_registry.py",
    "v2/src/pec_v2/core/ports/__init__.py",
    "v2/src/pec_v2/core/__init__.py",
    "v2/src/pec_v2/adapters/config/loop_registry.py",
    "v2/tests/config/test_json_loop_registry.py",
    "v2/tests/config/test_loop_registry_contract.py",
    "v2/tests/config/fixtures/duplicate_loop_id.json",
    "v2/tests/config/fixtures/missing_loop_id.json",
]
CREATED = ["v2/tests/config/fixtures/schema_version_1.json"]
UNCHANGED = [
    "v2/tests/config/fixtures/malformed.json",
    "v2/src/pec_v2/adapters/config/__init__.py",
    "v2/src/pec_v2/adapters/__init__.py",
    "v2/src/pec_v2/__init__.py",
    "software-workflow.json",
    "v2/config/service_core_posture.json",
]
AR_OVERRIDES = ["v2/config/loops.json", "v2/tests/config/test_json_loop_registry.py"]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    post_a, post_ar, pre_file, out = (Path(p) for p in sys.argv[1:5])
    pre = {}
    for line in pre_file.read_text().splitlines():
        digest, path = line.split("  ", 1)
        pre[path.removeprefix(PEC)] = digest
    payload_a = {rel: (post_a / rel).read_bytes() for rel in MODIFIED + CREATED}
    payload_ar = dict(payload_a)
    for rel in AR_OVERRIDES:
        payload_ar[rel] = (post_ar / rel).read_bytes()
    blobs = {}
    for data in list(payload_a.values()) + list(payload_ar.values()):
        blobs[sha(data)] = base64.b64encode(data).decode("ascii")
    lines = []
    lines.append("PREIMAGES = {")
    for rel in MODIFIED:
        lines.append(f"    {rel!r}: {pre[rel]!r},")
    for rel in CREATED:
        lines.append(f"    {rel!r}: None,")
    lines.append("}")
    lines.append("UNCHANGED = {")
    for rel in UNCHANGED:
        lines.append(f"    {rel!r}: {pre[rel]!r},")
    lines.append("}")
    for name, payload in (("POSTIMAGES_A", payload_a), ("POSTIMAGES_AR", payload_ar)):
        lines.append(f"{name} = {{")
        for rel in MODIFIED + CREATED:
            lines.append(f"    {rel!r}: {sha(payload[rel])!r},")
        lines.append("}")
    lines.append("BLOBS = {")
    for digest in sorted(blobs):
        lines.append(f"    {digest!r}: (")
        text = blobs[digest]
        for start in range(0, len(text), 76):
            lines.append(f"        {text[start:start + 76]!r}")
        lines.append("    ),")
    lines.append("}")
    template = (Path(__file__).parent / "apply_d96.template.py").read_text(encoding="utf-8")
    marker = "# @@PINNED@@\n"
    if template.count(marker) != 1:
        raise SystemExit("template marker missing")
    out.write_text(template.replace(marker, "\n".join(lines) + "\n"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
