#!/usr/bin/env python3
"""Fault-injection tests for apply_d1p.py (D1 premise amendment, provisional D-PEC-105).

Usage: test_apply_d1p.py <export root> <candidates dir> [--script <apply_d1p.py>]
  <export root>     a `git archive` export of the basis commit (only its projects/pec is copied)
  <candidates dir>  the candidate files at their repository-relative paths
  --script          the rendered act script (default: apply_d1p.py next to this file)

Each case runs on a fresh copy of projects/pec from the export, in a temporary
directory under $TMPDIR, and the copy is deleted afterwards. Prints one line per
case and `RESULT PASS n/n` (exit 0) or `RESULT FAIL k/n` (exit 1). Stdlib only;
never writes to the export or the candidates directory.
"""
import argparse, hashlib, importlib.util, io, os, shutil, sys, tempfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock
sys.dont_write_bytecode = True  # importing the act script must leave no __pycache__ beside it

ap = argparse.ArgumentParser()
ap.add_argument("export"); ap.add_argument("candidates"); ap.add_argument("--script")
ap.add_argument("-v", "--verbose", action="store_true", help="show the act's own output")
args = ap.parse_args()
base, cand = Path(args.export).resolve(), Path(args.candidates).resolve()
SCRIPT = Path(args.script).resolve() if args.script else Path(__file__).resolve().with_name("apply_d1p.py")

def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path)
    mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
m = load(SCRIPT, "apply_d1p")
A = [r for r, v in m.TARGETS.items() if v[0] == "A"]
P = [r for r, v in m.TARGETS.items() if v[0] == "P"]
ALL = list(m.TARGETS)
assert A and P, "the tests expect at least one group-A and one group-P target"

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pre_of(r): return m.TARGETS[r][2]
def post_of(r): return m.TARGETS[r][3]
def no_tmp(repo): return not any((repo / (r + m.TMP_SUFFIX)).exists() for r in ALL)
def pristine(repo):
    """every target holds its preimage and no temporary file remains"""
    return all(h(repo / r) == pre_of(r) for r in ALL) and no_tmp(repo)
def applied(repo, rels):
    """rels hold their postimages, every other target its preimage, no temporary"""
    return all(h(repo / r) == (post_of(r) if r in rels else pre_of(r)) for r in ALL) and no_tmp(repo)
def snapshot(repo):
    out = {}
    for dp, dn, fn in os.walk(repo / "projects/pec"):
        dn[:] = [d for d in dn if d != "__pycache__"]
        for f in fn:
            p = Path(dp) / f; out[p.relative_to(repo).as_posix()] = h(p)
    return out
def diff(a, b):
    return sorted(set(a) ^ set(b)) + sorted(k for k in set(a) & set(b) if a[k] != b[k])
def run(repo, *extra, mod=None, candidates=None):
    mod = mod or m
    argv = ["apply_d1p.py", "--repo", str(repo), "--candidates", str(candidates or cand), *extra]
    buf = io.StringIO()
    with mock.patch.object(sys, "argv", argv), redirect_stdout(buf):
        rc = mod.main()
    run.last = buf.getvalue()
    if args.verbose: print(run.last, end="")
    return rc
run.last = ""
def said(text): return text in run.last

results = []
def case(name, fn):
    with tempfile.TemporaryDirectory(prefix="d1ptest.") as td:
        repo = Path(td) / "r"; shutil.copytree(base / "projects/pec", repo / "projects/pec", symlinks=True)
        try: ok = bool(fn(repo, Path(td)))
        except Exception as e:
            ok = False; print(f"  exception: {e!r}")
        results.append((ok, name)); print(("PASS " if ok else "FAIL ") + name)
        if not ok and not args.verbose: print("  last act output:\n    " + run.last.strip().replace("\n", "\n    "))

# --- happy paths --------------------------------------------------------------
def happy_a(repo, td):
    s0 = snapshot(repo)
    ok = run(repo, "--check-only") == 0 and said("CHECK preflight passed") and snapshot(repo) == s0
    ok = ok and run(repo) == 0 and applied(repo, A)
    d = diff(s0, snapshot(repo))
    return ok and d == sorted(A) and len(d) == len(A) == 3
def happy_ap(repo, td):
    s0 = snapshot(repo)
    ok = run(repo, "--with-addon-p", "--check-only") == 0 and said("CHECK preflight passed") and snapshot(repo) == s0
    ok = ok and run(repo, "--with-addon-p") == 0 and applied(repo, A + P)
    d = diff(s0, snapshot(repo))
    return ok and d == sorted(A + P) and len(d) == 4
def a_only_without_p_candidate(repo, td):  # A-only mode never reads the P candidate; P stays at its preimage
    cd = td / "cand_a_only"; shutil.copytree(cand, cd)
    for r in P: (cd / r).unlink()
    s0 = snapshot(repo)
    ok = run(repo, candidates=cd) == 0 and applied(repo, A) and all(h(repo / r) == pre_of(r) for r in P)
    return ok and diff(s0, snapshot(repo)) == sorted(A)
def ap_without_p_candidate(repo, td):  # --with-addon-p without the P candidate refuses before any write
    cd = td / "cand_a_only"; shutil.copytree(cand, cd)
    for r in P: (cd / r).unlink()
    return run(repo, "--with-addon-p", candidates=cd) == 1 and said("candidate missing") and pristine(repo)

# --- reruns -------------------------------------------------------------------
def rerun_a(repo, td):
    return (run(repo) == 0 and run(repo) == 1 and said("already applied or changed") and applied(repo, A)
            and run(repo, "--with-addon-p") == 1 and applied(repo, A))
def rerun_ap(repo, td):
    return run(repo, "--with-addon-p") == 0 and run(repo, "--with-addon-p") == 1 and run(repo) == 1 and applied(repo, A + P)

# --- preflight refusals (nothing written) -------------------------------------
def wrong_candidate_hash(repo, td):
    ok = True
    for r in (A[-1], P[0]):
        cd = td / ("cand_bad_" + str(len(r))); shutil.rmtree(cd, ignore_errors=True); shutil.copytree(cand, cd)
        (cd / r).write_bytes((cd / r).read_bytes() + b"x")
        s0 = snapshot(repo)
        ok = ok and run(repo, "--with-addon-p", candidates=cd) == 1 and said("candidate hash mismatch") \
            and said("nothing written") and snapshot(repo) == s0 and pristine(repo)
    return ok
def changed_preimage(repo, td):
    r0 = A[0]; (repo / r0).write_bytes((repo / r0).read_bytes() + b"\n")
    s0 = snapshot(repo)
    rc = run(repo)
    return rc == 1 and said("does not hold its preimage") and snapshot(repo) == s0
def p_changed_in_a_mode(repo, td):  # the unselected P target must hold its preimage even in A-only mode
    r0 = P[0]; (repo / r0).write_bytes((repo / r0).read_bytes() + b"\n")
    s0 = snapshot(repo)
    return run(repo) == 1 and said("unselected target changed") and snapshot(repo) == s0
def pinned_drift(repo, td):  # every pinned file, one at a time
    ok = True
    for rel in m.PINNED:
        f = repo / rel; keep = f.read_bytes(); f.write_bytes(keep + b" ")
        s0 = snapshot(repo)
        ok = ok and run(repo, "--with-addon-p") == 1 and said(f"pinned hash mismatch: {rel}") and snapshot(repo) == s0
        f.write_bytes(keep)
    return ok and pristine(repo) and len(m.PINNED) == 18
def pinned_missing(repo, td):
    rel = list(m.PINNED)[-1]; (repo / rel).unlink()
    return run(repo) == 1 and said("pinned file missing") and pristine(repo)
def stray_temp(repo, td):  # a temporary sibling of any target refuses, whichever mode
    ok = True
    for r, extra in ((A[1], ()), (P[0], ()), (P[0], ("--with-addon-p",))):
        t = repo / (r + m.TMP_SUFFIX); t.write_bytes(b"stray\n")
        s0 = snapshot(repo)
        ok = ok and run(repo, *extra) == 1 and said("temporary already exists") and snapshot(repo) == s0
        t.unlink()
    return ok and pristine(repo)
def candidate_missing(repo, td):
    cd = td / "cand_missing"; shutil.copytree(cand, cd); (cd / A[0]).unlink()
    return run(repo, candidates=cd) == 1 and said("candidate missing") and pristine(repo)

# --- failures after the first write: full rollback -----------------------------
def io_failure(repo, td):  # rename fails on the last selected target, after the others were replaced
    ok = True
    for extra, sel in (((), A), (("--with-addon-p",), A + P)):
        real = os.replace; n = {"i": 0}
        def flaky(a, b):
            n["i"] += 1
            if n["i"] == len(sel): raise OSError("injected rename failure")
            return real(a, b)
        with mock.patch.object(m.os, "replace", flaky): rc = run(repo, *extra)
        ok = ok and rc == 1 and said("injected rename failure") and said("restored") and pristine(repo)
    return ok
def write_failure(repo, td):  # the temporary write itself fails on the second target
    real = Path.write_bytes; n = {"i": 0}
    def flaky(self, data):
        if str(self).endswith(m.TMP_SUFFIX):
            n["i"] += 1
            if n["i"] == 2: raise OSError("injected write failure (disk full)")
        return real(self, data)
    with mock.patch.object(Path, "write_bytes", flaky): rc = run(repo, "--with-addon-p")
    return rc == 1 and said("injected write failure") and pristine(repo)
def temp_hash_mismatch(repo, td):  # temporary-file hash check fails on the last selected target
    real = m.sha; last = A[-1]
    def bad(p):
        if str(p).endswith(last + m.TMP_SUFFIX): return "f" * 64
        return real(p)
    with mock.patch.object(m, "sha", bad): rc = run(repo)
    return rc == 1 and said("temporary hash mismatch") and pristine(repo)
def extra_file_during_write(repo, td):  # a real file appears under projects/pec during the write
    real = os.replace; stray = repo / "projects/pec/execution/_Coordination/stray_during_act.md"
    def creating(a, b):
        if not stray.exists(): stray.write_text("stray\n")
        return real(a, b)
    with mock.patch.object(m.os, "replace", creating): rc = run(repo)
    return rc == 1 and said("write set differs from grant") and said("stray_during_act.md") and pristine(repo)
def unexpected_modified_during_write(repo, td):  # a non-target file changes during the write
    real = os.replace; victim = repo / "projects/pec/docs/STATUS.md"
    def touching(a, b):
        victim.write_bytes(victim.read_bytes() + b" ")
        return real(a, b)
    with mock.patch.object(m.os, "replace", touching): rc = run(repo)
    return rc == 1 and said("write set differs from grant") and pristine(repo)
def p_modified_during_a_write(repo, td):  # the unselected P target changes during an A-only write
    real = os.replace; pt = repo / P[0]
    def touching(a, b):
        if h(pt) == pre_of(P[0]): pt.write_bytes(pt.read_bytes() + b"\n")
        return real(a, b)
    with mock.patch.object(m.os, "replace", touching): rc = run(repo)
    return rc == 1 and said("write set differs from grant") and all(h(repo / r) == pre_of(r) for r in A) and no_tmp(repo)
def pinned_changed_during_write(repo, td):  # a pinned file changes after the first write
    real = os.replace; pin = repo / list(m.PINNED)[0]
    def touching(a, b):
        pin.write_bytes(pin.read_bytes() + b" ")
        return real(a, b)
    with mock.patch.object(m.os, "replace", touching): rc = run(repo, "--with-addon-p")
    return rc == 1 and pristine(repo)
def mocked_inventory_extra(repo, td):  # post-write inventory reports an extra file (S4 c3 form)
    real = m.inventory; n = {"i": 0}
    def inv(r):
        d = real(r); n["i"] += 1
        if n["i"] == 2: d["projects/pec/execution/_Coordination/stray.md"] = "1" * 64
        return d
    with mock.patch.object(m, "inventory", inv): rc = run(repo, "--with-addon-p")
    return rc == 1 and pristine(repo)
def rollback_incomplete(repo, td):  # every rename after the first fails, including the rollback's: exit 2
    real = os.replace; n = {"i": 0}
    def broken(a, b):
        n["i"] += 1
        if n["i"] >= 2: raise OSError("injected persistent rename failure")
        return real(a, b)
    with mock.patch.object(m.os, "replace", broken): rc = run(repo)
    return rc == 2 and said("ROLLBACK INCOMPLETE")

# --- run-root guard --------------------------------------------------------------
def guard_bad_placement(repo, td):
    ok = True
    for bad in ("projects/pec/tools/x", "projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_X", "projects/pec"):
        od = repo / bad; od.mkdir(parents=True, exist_ok=True)
        shutil.copy(SCRIPT, od / "apply_d1p.py")
        mm = load(od / "apply_d1p.py", "apply_d1p_bad")
        s0 = snapshot(repo)
        ok = ok and run(repo, mod=mm) == 1 and said("is not a run root") and diff(s0, snapshot(repo)) == []
        (od / "apply_d1p.py").unlink()
    return ok and pristine(repo)
def guard_good_run_root(repo, td):  # a run root is accepted and its evidence stays outside the inventory
    rr = repo / "projects/pec/execution/_Coordination/D1_PREMISE_AMEND_TEST"; rr.mkdir(parents=True)
    shutil.copy(SCRIPT, rr / "apply_d1p.py"); shutil.copytree(cand, rr / "candidates")
    mm = load(rr / "apply_d1p.py", "apply_d1p_rr")
    real = os.replace; n = {"i": 0}
    def logging_replace(a, b):
        n["i"] += 1; (rr / f"act_log_{n['i']}.txt").write_text("evidence\n")
        return real(a, b)
    with mock.patch.object(mm.os, "replace", logging_replace):
        rc = run(repo, "--with-addon-p", mod=mm, candidates=rr / "candidates")
    return rc == 0 and applied(repo, A + P) and (rr / "act_log_1.txt").exists()

case("happy path A: check-only writes nothing, apply exits 0, exactly the 3 group-A files change", happy_a)
case("happy path A+P: check-only writes nothing, apply exits 0, exactly the 4 files change", happy_ap)
case("A-only mode with no P candidate present: 3 files change, P byte-identical at its preimage", a_only_without_p_candidate)
case("--with-addon-p without the P candidate: preflight exit 1, nothing written", ap_without_p_candidate)
case("rerun after A refuses at preflight (both modes); state unchanged", rerun_a)
case("rerun after A+P refuses at preflight (both modes); state unchanged", rerun_ap)
case("wrong candidate hash (A and P): preflight exit 1 before any write", wrong_candidate_hash)
case("a target not at its preimage: preflight exit 1, nothing written", changed_preimage)
case("the P target not at its preimage in A-only mode: preflight exit 1, nothing written", p_changed_in_a_mode)
case("drift in each of the 18 pinned files: preflight exit 1, nothing written", pinned_drift)
case("a pinned file missing: preflight exit 1, nothing written", pinned_missing)
case("stray temporary sibling (A target; P target in either mode): preflight exit 1", stray_temp)
case("a selected candidate missing: preflight exit 1, nothing written", candidate_missing)
case("rename failure on the last selected target (A; A+P): exit 1, all restored, no temporary", io_failure)
case("temporary write failure on the second target: exit 1, all restored", write_failure)
case("temporary hash mismatch on the last target: exit 1, all restored", temp_hash_mismatch)
case("an extra file created under projects/pec during the write: exit 1, rolled back", extra_file_during_write)
case("a non-target file modified during the write: exit 1, rolled back", unexpected_modified_during_write)
case("the unselected P target modified during an A-only write: exit 1, A rolled back", p_modified_during_a_write)
case("a pinned file changed during the write: exit 1, rolled back", pinned_changed_during_write)
case("post-write inventory reports an extra file (mocked): exit 1, rolled back", mocked_inventory_extra)
case("rollback itself fails: exit 2 with ROLLBACK INCOMPLETE", rollback_incomplete)
case("run-root guard refuses bad in-tree placements (tools/, the prep folder, projects/pec)", guard_bad_placement)
case("a D1_PREMISE_AMEND_ run root is accepted; evidence written there does not trip the inventory", guard_good_run_root)
bad = [n for ok, n in results if not ok]
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(results) - len(bad)}/{len(results)}")
sys.exit(1 if bad else 0)
