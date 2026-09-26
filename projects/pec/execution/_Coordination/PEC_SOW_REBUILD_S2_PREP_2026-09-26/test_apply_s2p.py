#!/usr/bin/env python3
"""Fault-injection tests for apply_s2p.py.
Usage: test_apply_s2p.py <base_export> <candidates_dir>
Each case runs on a fresh copy of projects/pec from the export. Exit 0 when all pass."""
import hashlib, importlib.util, os, shutil, sys, tempfile
from pathlib import Path
from unittest import mock

base, cand = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("apply_s2p", Path(__file__).with_name("apply_s2p.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
FIRST_PIN = next(iter(m.PINNED))

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pristine(repo):
    """every target holds its preimage and no temporary file remains"""
    return all(h(repo / r) == pre and not (repo / (r + m.TMP_SUFFIX)).exists() for r, (pre, _) in m.TARGETS.items())
def applied(repo):
    return all(h(repo / r) == post and not (repo / (r + m.TMP_SUFFIX)).exists() for r, (_, post) in m.TARGETS.items())
def run(repo, *extra):
    with mock.patch.object(sys, "argv", ["apply_s2p.py", "--repo", str(repo), "--candidates", str(cand), *extra]):
        return m.main()
results = []
def case(name, fn):
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td) / "r"; shutil.copytree(base / "projects/pec", repo / "projects/pec")
        ok = fn(repo); results.append((ok, name)); print(("PASS " if ok else "FAIL ") + name)

def c1(repo):  # rename fails on the fourth target, after three replacements
    real = os.replace; n = {"i": 0}
    def flaky(a, b):
        n["i"] += 1
        if n["i"] == 4: raise OSError("injected rename failure")
        return real(a, b)
    with mock.patch.object(m.os, "replace", flaky): rc = run(repo)
    return rc == 1 and pristine(repo)
def c2(repo):  # post-write inventory reports an unexpected modified file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/docs/PRD.md"] = "0" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and pristine(repo)
def c3(repo):  # post-write inventory reports an extra file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and pristine(repo)
def c4(repo):  # a pinned basis file changed before the run
    (repo / FIRST_PIN).write_bytes(b"changed\n")
    return run(repo) == 1 and pristine(repo)
def c5(repo):  # a target no longer holds its preimage
    r0 = next(iter(m.TARGETS)); (repo / r0).write_bytes((repo / r0).read_bytes() + b"\n")
    rc = run(repo)
    others = all(h(repo / r) == pre for r, (pre, _) in list(m.TARGETS.items())[1:])
    return rc == 1 and others
def c6(repo):  # temporary-file hash check fails on the last target
    real = m.sha; n = {"i": 0}; last = list(m.TARGETS)[-1]
    def bad(p):
        if str(p).endswith(last + m.TMP_SUFFIX): return "f" * 64
        return real(p)
    with mock.patch.object(m, "sha", bad): rc = run(repo)
    return rc == 1 and pristine(repo)
def c7(repo):  # check-only writes nothing; apply succeeds; second run refuses
    return (run(repo, "--check-only") == 0 and pristine(repo)
            and run(repo) == 0 and applied(repo) and run(repo) == 1 and applied(repo))
case("rename failure on the fourth target: exit 1, all targets restored, no temporary left", c1)
case("post-write inventory shows an unexpected modified file: exit 1, rolled back", c2)
case("post-write inventory shows an extra file: exit 1, rolled back", c3)
case("pinned basis file changed: preflight exit 1, nothing written", c4)
case("target not at its preimage: preflight exit 1, nothing written", c5)
case("temporary hash mismatch on the last target: exit 1, rolled back", c6)
case("check-only writes nothing; apply succeeds; second run refuses", c7)
bad = [n for ok, n in results if not ok]
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(results)-len(bad)}/{len(results)}")
sys.exit(1 if bad else 0)
