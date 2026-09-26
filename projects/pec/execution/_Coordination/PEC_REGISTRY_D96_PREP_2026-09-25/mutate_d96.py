#!/usr/bin/env python3
"""Apply D-PEC-96 mutations one at a time to scratch copies and confirm the registry suite catches each.

Usage: mutate_d96.py <projects/pec root of an applied tree> [--pec-row migrated|remaining]
--pec-row names the option applied to the tree: migrated (A, default) or
remaining (A-R). M1-M10 and M12-M18 are the same for both; M11 and M19 act on
the checked-in default and have one variant per option.
Exit 0 only when the baseline passes and every mutation is caught.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ADAPTER = "v2/src/pec_v2/adapters/config/loop_registry.py"
PORT = "v2/src/pec_v2/core/ports/loop_registry.py"
SCHEMA = "v2/config/loops.schema.json"
DEFAULT = "v2/config/loops.json"


def replace(rel: str, old: str, new: str):
    def apply(root: Path) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        if text.count(old) != 1:
            raise RuntimeError(f"mutation anchor not unique in {rel}: {old!r}")
        path.write_text(text.replace(old, new), encoding="utf-8")
    return apply


def edit_json(rel: str, change):
    def apply(root: Path) -> None:
        path = root / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return apply


def schema_version_const_1(data):
    data["properties"]["schema_version"]["const"] = 1


def default_profiles_swapped_to_remaining_loop(data):
    # A: keep the first entry's basis and state; only the profile identifier changes.
    first = data["loops"][0]["feed_profiles"][0]
    data["loops"][0]["feed_profiles"] = [dict(first, profile="remaining-loop")]


def default_profile_swapped_to_shared_dev_loop(data):
    # A-R: same basis, state and version; only the profile identifier changes.
    data["loops"][0]["feed_profiles"][0]["profile"] = "shared-dev-loop"


def default_drops_remaining_items(data):
    # A: the Remaining sections silently drop out of the default.
    data["loops"][0]["feed_profiles"].pop(1)


def default_remaining_loop_historical(data):
    # A-R: the only profile turns historical, so the default has no live profile.
    data["loops"][0]["feed_profiles"][0]["state"] = "historical"


MUTATIONS = {
    "M1 accept schema version 1": replace(ADAPTER, "version != _SCHEMA_VERSION", "version not in (1, _SCHEMA_VERSION)"),
    "M2 drop duplicate-profile check": replace(ADAPTER, "            if profile in seen:\n", "            if False:\n"),
    "M3 skip basis path check": replace(ADAPTER, 'basis = self._repository_path(entry["basis"], f"{entry_location}.basis")', 'basis = entry["basis"]'),
    "M4 widen vocabulary": replace(ADAPTER, '    "shared-dev-loop": frozenset({1}),\n}', '    "shared-dev-loop": frozenset({1}),\n    "adapter-yaml": frozenset({1}),\n}'),
    "M5 admit bool version": replace(ADAPTER, "if type(version) is not int or version not in FEED_PROFILE_VERSIONS[profile]", "if not isinstance(version, int) or version not in FEED_PROFILE_VERSIONS[profile]"),
    "M6 admit empty feed_profiles": replace(ADAPTER, '        if not value:\n            self._fail(location, "expected at least one feed profile")\n', ""),
    "M7 feed_profiles optional": replace(ADAPTER, 'row, {"loop_id", "loop_init_path", "feed_profiles"}, location', 'row, {"loop_id", "loop_init_path"} | ({"feed_profiles"} & row.keys()), location'),
    "M8 unlocated state failure": replace(ADAPTER, '                self._fail(f"{entry_location}.state", "expected live or historical")\n', "                pass\n"),
    "M9 admit version 2 of every profile": replace(ADAPTER, '"shared-dev-loop": frozenset({1}),', '"shared-dev-loop": frozenset({1, 2}),'),
    "M10 schema const reverts to 1": edit_json(SCHEMA, schema_version_const_1),
    "M11 default profile identifier swapped": {
        "migrated": edit_json(DEFAULT, default_profiles_swapped_to_remaining_loop),
        "remaining": edit_json(DEFAULT, default_profile_swapped_to_shared_dev_loop),
    },
    "M12 RegisteredLoop field order": replace(PORT, "    loop_init_path: str\n    feed_profiles: tuple[FeedProfile, ...]\n", "    feed_profiles: tuple[FeedProfile, ...]\n    loop_init_path: str\n"),
    "M13 allow traversing loop_init_path": replace(ADAPTER, 'if locator.is_absolute() or ".." in locator.parts or "\\\\" in value:', 'if locator.is_absolute() or "\\\\" in value:'),
    "M14 drop surface-disjointness check": replace(ADAPTER, "                if surface in covered:\n", "                if False:\n"),
    "M15 drop at-least-one-live rule": replace(ADAPTER, "        if not any(item.state is FeedProfileState.LIVE for item in profiles):\n", "        if False:\n"),
    "M16 remaining-loop no longer claims the ledger": replace(ADAPTER, '            "receipt-ledger",\n            "status-lifecycle",\n            "status-remaining",\n', '            "status-lifecycle",\n            "status-remaining",\n'),
    "M17 overlap allowed between live and historical only": replace(ADAPTER, "                if surface in covered:\n", "                if surface in covered and entry[\"state\"] == profiles[covered[surface]].state.value:\n"),
    "M18 echo the invalid state value": replace(ADAPTER, 'self._fail(f"{entry_location}.state", "expected live or historical")', 'self._fail(f"{entry_location}.state", f"expected live or historical, got {state!r}")'),
    "M19 default loses a declared surface or its live profile": {
        "migrated": edit_json(DEFAULT, default_drops_remaining_items),
        "remaining": edit_json(DEFAULT, default_remaining_loop_historical),
    },
}


def run_suite(root: Path) -> int:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "v2/tests/config", "-p", "test_*.py"],
        cwd=root, env=env, capture_output=True, text=True,
    )
    return result.returncode


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("pec_root")
    parser.add_argument("--pec-row", choices=["migrated", "remaining"], default="migrated")
    args = parser.parse_args()
    source = Path(args.pec_root).resolve()
    print(f"OPTION {'A' if args.pec_row == 'migrated' else 'A-R'}")
    ok = True
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary) / "base"
        shutil.copytree(source / "v2", base / "v2")
        code = run_suite(base)
        print(f"BASELINE exit={code}")
        ok &= code == 0
        for name, mutate in MUTATIONS.items():
            work = Path(temporary) / "work"
            if work.exists():
                shutil.rmtree(work)
            shutil.copytree(base, work)
            if isinstance(mutate, dict):
                mutate = mutate[args.pec_row]
            try:
                mutate(work)
            except Exception as error:  # a mutation that cannot apply is a runner defect
                print(f"{name}: NOT_APPLIED ({error.__class__.__name__}: {error})")
                ok = False
                continue
            code = run_suite(work)
            caught = code != 0
            print(f"{name}: {'CAUGHT' if caught else 'SURVIVED'} (exit={code})")
            ok &= caught
    print("RESULT", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
