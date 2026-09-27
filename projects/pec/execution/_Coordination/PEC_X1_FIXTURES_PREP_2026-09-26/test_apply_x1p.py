#!/usr/bin/env python3
"""Fault-injection tests for apply_x1p.py.
Usage: test_apply_x1p.py <base_export> <candidates_dir>
Each case runs on a fresh copy of projects/pec from the export. Exit 0 when all pass."""
import hashlib, importlib.util, os, shutil, sys, tempfile
from pathlib import Path
from unittest import mock

base, cand = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("apply_x1p", Path(__file__).with_name("apply_x1p.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
FIRST_PIN = next(iter(m.PINNED))
MODIFIED = [r for r, (pre, _) in m.TARGETS.items() if pre is not None]
CREATED = [r for r, (pre, _) in m.TARGETS.items() if pre is None]

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot(repo):
    out = {}
    for p in sorted((repo / "projects/pec").rglob("*")):
        out[p.relative_to(repo).as_posix()] = h(p) if p.is_file() else "<dir>"
    return out
def no_tmp(repo): return not any(str(p).endswith(m.TMP_SUFFIX) for p in (repo / "projects/pec").rglob("*"))
def applied(repo):
    return all((repo / r).is_file() and h(repo / r) == post for r, (_, post) in m.TARGETS.items()) and no_tmp(repo)
def run(repo, *extra, mod=None):
    mod = mod or m
    with mock.patch.object(sys, "argv", ["apply_x1p.py", "--repo", str(repo), "--candidates", str(cand), *extra]):
        return mod.main()
results = []
SCRATCH = Path(os.environ.get("TMPDIR") or Path(__file__).resolve().parent / ".scratch")  # never /tmp
SCRATCH.mkdir(parents=True, exist_ok=True)
def case(name, fn):
    with tempfile.TemporaryDirectory(dir=SCRATCH) as td:
        repo = Path(td) / "r"; shutil.copytree(base / "projects/pec", repo / "projects/pec")
        before = snapshot(repo)
        ok = fn(repo, before); results.append((ok, name)); print(("PASS " if ok else "FAIL ") + name)

def c1(repo, before):  # rename fails on the fourth target, after three writes (dirs created)
    real = os.replace; n = {"i": 0}
    def flaky(a, b):
        n["i"] += 1
        if n["i"] == 4: raise OSError("injected rename failure")
        return real(a, b)
    with mock.patch.object(m.os, "replace", flaky): rc = run(repo)
    return rc == 1 and snapshot(repo) == before
def c2(repo, before):  # post-write inventory reports an unexpected modified file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/docs/PRD.md"] = "0" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and snapshot(repo) == before
def c3(repo, before):  # post-write inventory reports an extra file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo)
    return rc == 1 and snapshot(repo) == before
def c4(repo, before):  # a pinned basis file changed before the run
    (repo / FIRST_PIN).write_bytes(b"changed\n"); before = snapshot(repo)
    return run(repo) == 1 and snapshot(repo) == before
def c5(repo, before):  # the modified target no longer holds its preimage
    r0 = MODIFIED[0]; (repo / r0).write_bytes((repo / r0).read_bytes() + b"\n"); before = snapshot(repo)
    return run(repo) == 1 and snapshot(repo) == before
def c6(repo, before):  # the new directory already exists (a created target would collide)
    (repo / m.NEW_DIR).mkdir(parents=True); before = snapshot(repo)
    return run(repo) == 1 and snapshot(repo) == before
def c7(repo, before):  # temporary-file hash check fails on the last target
    real = m.sha; last = list(m.TARGETS)[-1]
    def bad(p):
        if str(p).endswith(last + m.TMP_SUFFIX): return "f" * 64
        return real(p)
    with mock.patch.object(m, "sha", bad): rc = run(repo)
    return rc == 1 and snapshot(repo) == before
def c8(repo, before):  # check-only writes nothing; apply succeeds; second run refuses and changes nothing
    ok = run(repo, "--check-only") == 0 and snapshot(repo) == before and run(repo) == 0 and applied(repo)
    after = snapshot(repo)
    return ok and run(repo) == 1 and snapshot(repo) == after
def c9(repo, before):  # evidence written into the run root during the act does not trip the write-set check
    rr = repo / "projects/pec/execution/_Coordination/X1_FIXTURES_TEST"; rr.mkdir(parents=True)
    shutil.copy(Path(__file__).with_name("apply_x1p.py"), rr / "apply_x1p.py")
    sp = importlib.util.spec_from_file_location("apply_x1p_rr", rr / "apply_x1p.py")
    mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm)
    real = os.replace; n = {"i": 0}
    def logging_replace(a, b):
        n["i"] += 1; (rr / f"act_log_{n['i']}.txt").write_text("evidence\n")
        return real(a, b)
    with mock.patch.object(mm.os, "replace", logging_replace): rc = run(repo, mod=mm)
    return rc == 0 and applied(repo) and (rr / "act_log_1.txt").exists()
def c10(repo, before):  # the bound copy placed in projects/pec outside a run root is refused at preflight
    od = repo / "projects/pec/tools/x"; od.mkdir(parents=True)
    shutil.copy(Path(__file__).with_name("apply_x1p.py"), od / "apply_x1p.py"); before = snapshot(repo)
    sp = importlib.util.spec_from_file_location("apply_x1p_bad", od / "apply_x1p.py")
    mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm)
    return run(repo, mod=mm) == 1 and snapshot(repo) == before
def c11(repo, before):  # a write failure on the last created file, after the modify and earlier creates
    real = m.put; last = CREATED[-1]
    def bad(r, rel, data, want):
        if rel == last and want == m.TARGETS[rel][1]: raise OSError("injected write failure")
        return real(r, rel, data, want)
    with mock.patch.object(m, "put", bad): rc = run(repo)
    return rc == 1 and snapshot(repo) == before
case("rename failure on the fourth target: exit 1, tree restored exactly", c1)
case("post-write inventory shows an unexpected modified file: exit 1, tree restored exactly", c2)
case("post-write inventory shows an extra file: exit 1, tree restored exactly", c3)
case("pinned basis file changed: preflight exit 1, nothing written", c4)
case("modified target not at its preimage: preflight exit 1, nothing written", c5)
case("new directory already present: preflight exit 1, nothing written", c6)
case("temporary hash mismatch on the last target: exit 1, tree restored exactly", c7)
case("check-only writes nothing; apply succeeds; second run refuses and changes nothing", c8)
case("run-root evidence written during the act is outside the inventory: apply succeeds", c9)
case("bound copy inside projects/pec but outside a run root: preflight exit 1, nothing written", c10)
case("write failure on the last created file after the modify: exit 1, modify restored, created files and directories removed", c11)
bad = [n for ok, n in results if not ok]
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(results)-len(bad)}/{len(results)}")
sys.exit(1 if bad else 0)
