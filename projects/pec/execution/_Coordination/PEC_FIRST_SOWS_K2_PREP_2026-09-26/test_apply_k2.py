#!/usr/bin/env python3
"""Fault-injection tests for apply_k2.py (option A) and apply_k2_c8.py (add-on C8).
Usage: test_apply_k2.py <base_export> <candidates_dir> <c8_dir>
Each case runs on a fresh copy of projects/pec and _DomainEngines/profiles from
the export. Exit 0 when all pass. Stdlib only."""
import hashlib, importlib.util, os, shutil, sys, tempfile
from pathlib import Path
from unittest import mock

base, cand, c8dir = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
HERE = Path(__file__).resolve().parent
def load(name, path):
    s = importlib.util.spec_from_file_location(name, path); mm = importlib.util.module_from_spec(s); s.loader.exec_module(mm); return mm
m = load("apply_k2", HERE / "apply_k2.py")
c8 = load("apply_k2_c8", HERE / "apply_k2_c8.py")

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pristine(repo):
    return all(not (repo / r).exists() and not (repo / (r + m.TMP_SUFFIX)).exists() for r in m.TARGETS)
def applied(repo):
    return all((repo / r).is_file() and h(repo / r) == want and not (repo / (r + m.TMP_SUFFIX)).exists()
               for r, want in m.TARGETS.items())
def c8_pre(repo): return h(repo / c8.TARGET) == c8.PRE and not (repo / (c8.TARGET + c8.TMP_SUFFIX)).exists()
def c8_post(repo): return h(repo / c8.TARGET) == c8.POST and not (repo / (c8.TARGET + c8.TMP_SUFFIX)).exists()
def run(mod, repo, cdir, *extra):
    with mock.patch.object(sys, "argv", ["x", "--repo", str(repo), "--candidates", str(cdir), *extra]):
        return mod.main()
results = []
def case(name, fn):
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td) / "r"
        shutil.copytree(base / "projects/pec", repo / "projects/pec")
        shutil.copytree(base / "_DomainEngines/profiles", repo / "_DomainEngines/profiles")
        ok = bool(fn(repo)); results.append((ok, name)); print(("PASS " if ok else "FAIL ") + name)

def a1(repo):  # rename fails on the second target, after the first was created
    real = os.replace; n = {"i": 0}
    def flaky(x, y):
        n["i"] += 1
        if n["i"] == 2: raise OSError("injected rename failure")
        return real(x, y)
    with mock.patch.object(m.os, "replace", flaky): rc = run(m, repo, cand)
    return rc == 1 and pristine(repo)
def a2(repo):  # post-write inventory reports an unexpected modified file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/docs/PRD.md"] = "0" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(m, repo, cand)
    return rc == 1 and pristine(repo)
def a3(repo):  # post-write inventory reports an extra file
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(m, repo, cand)
    return rc == 1 and pristine(repo)
def a4(repo):  # a pinned register changed before the run
    (repo / next(iter(m.PINNED))).write_bytes(b"changed\n")
    return run(m, repo, cand) == 1 and pristine(repo)
def a5(repo):  # the pinned tier-0 profile (outside projects/pec) changed before the run
    p = repo / "_DomainEngines/profiles/pec.yaml"; p.write_bytes(p.read_bytes() + b"\n")
    return run(m, repo, cand) == 1 and pristine(repo)
def a6(repo):  # a target already exists (foreign file): preflight refuses and leaves it untouched
    r0 = next(iter(m.TARGETS)); (repo / r0).write_bytes(b"foreign\n")
    rc = run(m, repo, cand)
    return rc == 1 and (repo / r0).read_bytes() == b"foreign\n" and not (repo / list(m.TARGETS)[1]).exists()
def a7(repo):  # temporary-file hash check fails on the last target
    real = m.sha; last = list(m.TARGETS)[-1]
    def bad(p):
        if str(p).endswith(last + m.TMP_SUFFIX): return "f" * 64
        return real(p)
    with mock.patch.object(m, "sha", bad): rc = run(m, repo, cand)
    return rc == 1 and pristine(repo)
def a8(repo):  # check-only writes nothing; apply succeeds; second run refuses
    return (run(m, repo, cand, "--check-only") == 0 and pristine(repo)
            and run(m, repo, cand) == 0 and applied(repo) and run(m, repo, cand) == 1 and applied(repo))
def a9(repo):  # evidence written into the run root during the act does not trip the write-set check
    rr = repo / "projects/pec/execution/_Coordination/SOW_INIT_K2_TEST"; rr.mkdir(parents=True)
    shutil.copy(HERE / "apply_k2.py", rr / "apply_k2.py")
    mm = load("apply_k2_rr", rr / "apply_k2.py")
    real = os.replace; n = {"i": 0}
    def logging_replace(x, y):
        n["i"] += 1; (rr / f"act_log_{n['i']}.txt").write_text("evidence\n")
        return real(x, y)
    with mock.patch.object(mm.os, "replace", logging_replace):
        rc = run(mm, repo, cand)
    return rc == 0 and applied(repo) and (rr / "act_log_1.txt").exists()
def a10(repo):  # the bound copy placed below projects/pec outside a run root is refused
    od = repo / "projects/pec/tools/x"; od.mkdir(parents=True)
    shutil.copy(HERE / "apply_k2.py", od / "apply_k2.py")
    return run(load("apply_k2_bad", od / "apply_k2.py"), repo, cand) == 1 and pristine(repo)
def a11(repo):  # the bound copy placed directly in projects/pec is refused
    shutil.copy(HERE / "apply_k2.py", repo / "projects/pec/apply_k2.py")
    return run(load("apply_k2_top", repo / "projects/pec/apply_k2.py"), repo, cand) == 1 and pristine(repo)
def c1(repo):  # C8 before A: refused (the DEL-10-13 contract pin fails), nothing written
    return run(c8, repo, c8dir) == 1 and c8_pre(repo)
def c2(repo):  # C8 after A: check-only, apply, second run refuses
    return (run(m, repo, cand) == 0 and run(c8, repo, c8dir, "--check-only") == 0 and c8_pre(repo)
            and run(c8, repo, c8dir) == 0 and c8_post(repo) and run(c8, repo, c8dir) == 1 and c8_post(repo))
def c3(repo):  # C8 post-write inventory shows an extra file: target restored
    if run(m, repo, cand) != 0: return False
    real = c8.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(c8, "inventory", inv): rc = run(c8, repo, c8dir)
    return rc == 1 and c8_pre(repo)
def c4(repo):  # C8 rename fails: target keeps its preimage, no temporary left
    if run(m, repo, cand) != 0: return False
    with mock.patch.object(c8.os, "replace", mock.Mock(side_effect=OSError("injected"))): rc = run(c8, repo, c8dir)
    return rc == 1 and c8_pre(repo)

case("A: rename failure on the second target: exit 1, no target or temporary left", a1)
case("A: post-write inventory shows an unexpected modified file: exit 1, cleaned up", a2)
case("A: post-write inventory shows an extra file: exit 1, cleaned up", a3)
case("A: pinned register changed: preflight exit 1, nothing written", a4)
case("A: pinned tier-0 profile changed: preflight exit 1, nothing written", a5)
case("A: a target already exists: preflight exit 1, existing file untouched", a6)
case("A: temporary hash mismatch on the last target: exit 1, cleaned up", a7)
case("A: check-only writes nothing; apply succeeds; second run refuses", a8)
case("A: run-root evidence written during the act is outside the inventory: apply succeeds", a9)
case("A: bound copy below projects/pec outside a run root: preflight exit 1", a10)
case("A: bound copy directly in projects/pec: preflight exit 1", a11)
case("C8: run before A: preflight exit 1, nothing written", c1)
case("C8: after A, check-only writes nothing; apply succeeds; second run refuses", c2)
case("C8: post-write inventory shows an extra file: exit 1, preimage restored", c3)
case("C8: rename failure: exit 1, preimage kept, no temporary left", c4)
bad = [n for ok, n in results if not ok]
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(results)-len(bad)}/{len(results)}")
sys.exit(1 if bad else 0)
