#!/usr/bin/env python3
"""D-PEC-96 bound act: PEC loop-registry schema v2 with closed feed profiles.

Writes exactly the pinned postimages of the ruled option into
projects/pec/ of the repository given by --repo, after checking every pinned
preimage and every must-remain file. Writes nothing and exits 1 on any
failure, including a second run. Stdlib only.

  python3 apply_d96.py --repo <REPO_ROOT> [--pec-row migrated|remaining] [--check-only]

--pec-row migrated (default) is option A; --pec-row remaining is option A-R.
--check-only runs every check and reports without writing.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import sys
from pathlib import Path

PEC = Path("projects/pec")

# @@PINNED@@


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> int:
    print(f"FAIL {message}; nothing written")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pec-row", choices=["migrated", "remaining"], default="migrated")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo).resolve() / PEC
    if not root.is_dir():
        return fail(f"{root} is not a directory")
    postimages = POSTIMAGES_A if args.pec_row == "migrated" else POSTIMAGES_AR
    if set(postimages) != set(PREIMAGES):
        return fail("postimage set differs from the grant")

    for rel, expected in sorted(UNCHANGED.items()):
        path = root / rel
        if not path.is_file() or sha(path.read_bytes()) != expected:
            return fail(f"must-remain file differs: {rel}")
        print(f"UNCHANGED {rel} {expected}")

    for rel, expected in sorted(PREIMAGES.items()):
        path = root / rel
        if expected is None:
            if path.exists():
                return fail(f"path to create already exists: {rel}")
            print(f"READ {rel} absent")
            continue
        if not path.is_file():
            return fail(f"preimage missing: {rel}")
        actual = sha(path.read_bytes())
        if actual != expected:
            return fail(f"preimage mismatch {rel}: {actual} != {expected}")
        print(f"READ {rel} {actual}")

    rendered: dict[str, bytes] = {}
    for rel, digest in sorted(postimages.items()):
        data = base64.b64decode("".join(BLOBS[digest]))
        if sha(data) != digest:
            return fail(f"embedded postimage corrupt: {rel}")
        rendered[rel] = data

    for rel, data in sorted(rendered.items()):
        if args.check_only:
            print(f"RENDER {rel} {sha(data)}")
            continue
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    if not args.check_only:
        for rel, digest in sorted(postimages.items()):
            actual = sha((root / rel).read_bytes())
            if actual != digest:
                print(f"FAIL postimage mismatch after write {rel}: {actual}")
                return 1
            print(f"WRITE {rel} {actual}")
    print(f"OK option={'A' if args.pec_row == 'migrated' else 'A-R'} files={len(rendered)} "
          f"mode={'check-only' if args.check_only else 'written'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
