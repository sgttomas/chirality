#!/usr/bin/env python3
"""Exercise group3_finalize.py in a scratch copy outside every git work tree.

Run from the repository root on the group-3 candidate. It copies the 12
candidate files, `_LATEST.md`, `Brief.md`, `Decision_Log.md`,
`Handoff_State.md` and the group-2 pointer (never `.git`) into a temporary
root, then checks the refusals (no decision, draft heading, wrong date, owner
act not verbatim, bad UTC stamp, missing group-2 pointer, a file that is not
the reviewed candidate), a dry run that writes nothing, one finalize with a
test decision whose outputs are compared byte for byte with the templates,
that nothing else changed, that a rerun is refused, and that this checkout is
unchanged. It also prints the date-only post-image hashes for a given
--expect-date (default 2026-09-27). Exit 1 on any FAIL.
"""
import argparse, csv, hashlib, importlib.util, os, shutil, subprocess, sys, tempfile

SNAP = ("projects/chirality-app-dev/execution/_ScopeChange/"
        "SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement")
G3 = os.path.join(SNAP, "Evidence/Group3/group3_finalize.py")
CSVP = os.path.join(SNAP, "Evidence/Group2/PREIMAGE_POSTIMAGE.csv")
SC = "projects/chirality-app-dev/execution/_ScopeChange"
DECOMP = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
spec = importlib.util.spec_from_file_location("g3", G3)
g3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g3)
rows = list(csv.DictReader(open(CSVP, newline="", encoding="utf-8")))
EXTRA = [g3.LATEST, g3.BRIEF, g3.DLOG, g3.HANDOFF, g3.POINTER2]
FILES = [r["File"] for r in rows] + EXTRA
ACT = 'I accept SCA-APP-012 checkpoint group 3 (test, with "quotes")'


def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(root, *a):
    p = subprocess.run([sys.executable, G3, *a, "--root", root], capture_output=True, text=True, env=dict(os.environ, GIT_DIR="/nonexistent"))
    print("$ group3_finalize.py", " ".join(x if len(x) < 50 else x[:47] + "..." for x in a), "-> rc", p.returncode)
    print("   " + (p.stdout + p.stderr).strip()[-600:].replace("\n", "\n   "))
    return p.returncode, p.stdout


def decision(root, date, heading, act=ACT):
    d = os.path.join(root, SC, f"checkpoint_snapshots/SCA-APP-012_GROUP-3_{date}")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "DECISION.md"), "w").write(f"{heading}\n\n## The owner's act (verbatim)\n\n> {act}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expect-date", default="2026-09-27")
    args = ap.parse_args()
    before = {f: h(f) for f in FILES}
    base = tempfile.mkdtemp(prefix="sca012-g3-")
    root = os.path.join(base, "scratch")
    for f in FILES:
        d = os.path.join(root, f)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy(f, d)
    date, utc = "2099-01-02", "20990102T000000Z"
    res = {}
    try:
        res["scratch root outside every git work tree"] = subprocess.run(
            ["git", "-C", root, "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True,
            env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")}).returncode != 0
        res["refused: no decision"] = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)[0] == 3
        decision(root, date, "# SCA-APP-012 checkpoint group 3 — draft")
        res["refused: draft heading"] = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)[0] == 3
        decision(root, date, "# SCA-APP-012 checkpoint group 3 — accepted (test)")
        res["refused: date differs from the decision folder"] = run(root, "--date", "2099-01-03", "--owner-act", ACT, "--utc", utc)[0] == 3
        res["refused: owner act not verbatim"] = run(root, "--date", date, "--owner-act", ACT + ".", "--utc", utc)[0] == 3
        res["refused: bad UTC stamp"] = run(root, "--date", date, "--owner-act", ACT, "--utc", "today")[0] == 3
        p2 = os.path.join(root, g3.POINTER2)
        os.rename(p2, p2 + ".off")
        res["refused: group-2 pointer absent"] = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)[0] == 3
        os.rename(p2 + ".off", p2)
        spec_path = os.path.join(root, rows[1]["File"])
        orig = open(spec_path, encoding="utf-8").read()
        open(spec_path, "w", encoding="utf-8").write(orig + "x\n")
        res["refused: a file is not the reviewed candidate"] = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)[0] == 1
        open(spec_path, "w", encoding="utf-8").write(orig)
        snap = {f: h(os.path.join(root, f)) for f in FILES}
        rc, out = run(root, "--date", date, "--owner-act", ACT, "--utc", utc, "--dry-run")
        res["dry run writes nothing"] = rc == 0 and {f: h(os.path.join(root, f)) for f in FILES} == snap
        rc, out = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)
        res["finalize ok"] = rc == 0
        after = {f: h(os.path.join(root, f)) for f in FILES}
        changed = sorted(f for f in FILES if after[f] != snap[f])
        res["exactly the five files changed"] = changed == sorted([DECOMP, g3.LATEST, g3.BRIEF, g3.DLOG, g3.HANDOFF])
        cand = open(DECOMP, encoding="utf-8").read()
        fin = open(os.path.join(root, DECOMP), encoding="utf-8").read()
        exp = cand.replace("| Revision | v3.2 source-governed working surface amended by SCA-APP-011 |\n| Date | 2026-09-27 |\n",
                           f"| Revision | v3.2 source-governed working surface amended by SCA-APP-012 |\n| Date | {date} |\n", 1)
        res["E26 only, in the decomposition"] = fin == exp and fin != cand
        res["_LATEST.md equals the filled template"] = open(os.path.join(root, g3.LATEST), encoding="utf-8").read() == \
            g3.fill(open(g3.LATEST_TEMPLATE, encoding="utf-8").read(), date)
        bl = open(os.path.join(root, g3.BRIEF), encoding="utf-8").read().split("\n")
        ob = open(g3.BRIEF, encoding="utf-8").read().split("\n")
        res["Brief line 3 exact, other lines unchanged"] = bl[2] == g3.fill(g3.BRIEF_AFTER, date, ACT) and bl[:2] + bl[3:] == ob[:2] + ob[3:]
        dl = open(os.path.join(root, g3.DLOG), encoding="utf-8").read().split("\n")
        od = open(g3.DLOG, encoding="utf-8").read().split("\n")
        i = [n for n, ln in enumerate(od) if ln.startswith(g3.G3_BEFORE_PREFIX)][0]
        res["Decision_Log G3 row exact, other lines unchanged"] = dl[i] == g3.fill(g3.G3_AFTER, date, ACT) and dl[:i] + dl[i + 1:] == od[:i] + od[i + 1:]
        res["Handoff_State equals the filled template"] = open(os.path.join(root, g3.HANDOFF), encoding="utf-8").read() == \
            g3.fill(open(g3.HANDOFF_TEMPLATE, encoding="utf-8").read(), date, ACT, utc)
        res["refused: rerun"] = run(root, "--date", date, "--owner-act", ACT, "--utc", utc)[0] == 1
        # Date-only post-image hashes for the expected acceptance date.
        e = args.expect_date
        print(f"expected after --date {e}: decomposition",
              hashlib.sha256(cand.replace("amended by SCA-APP-011 |\n| Date | 2026-09-27 |\n",
                                          f"amended by SCA-APP-012 |\n| Date | {e} |\n", 1).encode()).hexdigest())
        print(f"expected after --date {e}: _LATEST.md",
              hashlib.sha256(g3.fill(open(g3.LATEST_TEMPLATE, encoding="utf-8").read(), e).encode()).hexdigest())
    finally:
        shutil.rmtree(base, ignore_errors=True)
    res["this checkout unchanged"] = {f: h(f) for f in FILES} == before
    for k, v in res.items():
        print("PASS" if v else "FAIL", k)
    print(f"{sum(res.values())}/{len(res)} PASS")
    sys.exit(0 if all(res.values()) else 1)


if __name__ == "__main__":
    main()
