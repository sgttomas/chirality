#!/usr/bin/env python3
"""Fault-injection tests for apply_d98.py. Usage: test_apply_d98.py <base_export> <candidates_dir>
Each case runs on a fresh copy of the export. Exit 0 when all cases pass."""
import importlib.util, os, shutil, sys, tempfile
from pathlib import Path
from unittest import mock

base, cand = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("apply_d98", Path(__file__).with_name("apply_d98.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def leftovers(repo):
    return [r for r in m.TARGETS if (repo / r).exists() or (repo / (r + m.TMP_SUFFIX)).exists()]
def run(repo, *extra):
    with mock.patch.object(sys, "argv", ["apply_d98.py", "--repo", str(repo), "--candidates", str(cand), *extra]):
        return m.main()
results = []
def case(name, fn):
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td) / "r"; shutil.copytree(base / "projects/pec", repo / "projects/pec")
        ok = fn(repo); results.append((ok, name)); print(("PASS " if ok else "FAIL ") + name)
def c1(repo):
    real = os.replace; calls = {"n": 0}
    def flaky(a, b):
        calls["n"] += 1
        if calls["n"] == 2: raise OSError("injected rename failure")
        return real(a, b)
    with mock.patch.object(m.os, "replace", flaky): rc = run(repo)
    return rc == 1 and not leftovers(repo)
def c2(repo):
    real = m.inventory; calls = {"n": 0}
    def inv(r):
        d = real(r); calls["n"] += 1
        if calls["n"] == 2: d["projects/pec/docs/PRD.md"] = "0" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and not leftovers(repo)
def c3(repo):
    real = m.inventory; calls = {"n": 0}
    def inv(r):
        d = real(r); calls["n"] += 1
        if calls["n"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and not leftovers(repo)
def c4(repo):
    (repo / "projects/pec/docs/PRD.md").write_bytes(b"changed\n")
    return run(repo) == 1 and not leftovers(repo)
def c5(repo):
    return run(repo, "--check-only") == 0 and not leftovers(repo) and run(repo) == 0 and run(repo) == 1
case("rename failure on second target: exit 1, no target or temporary left", c1)
case("post-write inventory shows a modified file: exit 1, rolled back", c2)
case("post-write inventory shows an extra file: exit 1, rolled back", c3)
case("pinned basis file changed: preflight exit 1, nothing written", c4)
case("check-only writes nothing; apply succeeds; second run refuses", c5)
bad = [n for ok, n in results if not ok]
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(results)-len(bad)}/{len(results)}")
sys.exit(1 if bad else 0)
