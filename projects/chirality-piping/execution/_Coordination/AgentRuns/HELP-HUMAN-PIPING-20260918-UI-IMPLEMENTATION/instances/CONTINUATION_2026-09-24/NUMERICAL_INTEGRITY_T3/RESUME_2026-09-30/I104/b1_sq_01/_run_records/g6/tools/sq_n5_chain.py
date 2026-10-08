"""I104 SQ G6 (RV112 N-5, with B1's two other adapter reservations): price SP's capture-owned
reservations that I82's emulation has no owner for, in a copy of the G5 chain (mcr_b1q).

Rows added to producer_caps.py, after I82's per-case scaling (so they are not scaled again):
  T11.8  SP's parked case slots: `park_case`'s one adapter reservation of c - 1 `CaseSlot`s
         (retained_product.rs park_case), at c >= 2;
  T11.9  SP's per-case observation counters: `bind_observations_by_case` reserves c `[usize; 2]`
         through the adapter, at the finish and again at custody (two reservations), at c >= 2;
  T13.3  SP's batch native sources: `native_call` reserves |A| `PrimitiveSource`s through the
         adapter for a batch of |A| >= 2 (the sources move in; only the vector is new).
The adapter tally never decreases, so T11.8 and T11.9 count in capture_bytes (G-B, G-C) as live.
Atoms bound in-build in g5_profile.py; ASSUMED values are illustrative only.
Usage: python3 sq_n5_chain.py <chain dir> <out dir>
"""
import json, os, shutil, sys

src, dst = sys.argv[1:3]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)
LOG = []


def patch(fname, old, new, count=1):
    p = os.path.join(dst, fname)
    t = open(p).read()
    k = t.count(old)
    if k != count:
        raise SystemExit(f"PATCH FAILED {fname}: expected {count} match(es), found {k}: {old[:80]!r}")
    open(p, "w").write(t.replace(old, new))
    LOG.append((fname, old[:70].replace("\n", " "), k))


patch("producer_caps.py", '''out = {"which": which, "counts": dict(n=n, m=m, s=sp, r=r, l=l, g=g, N=N, F=F, k=k, Q=Q, U=U, P=P, Zu=Zu, H=Hp,''',
      '''# I104 SQ (RV112 N-5): SP's adapter reservations, after the per-case scaling above.
if CC > 1:
    rows["T11.8 SP parked case slots (park_case: c - 1 CaseSlot, one adapter reservation)"] = s("CaseSlot") * (CC - 1)
    rows["T11.9 SP per-case observation counters (bind_observations_by_case, finish and custody: 2 x c [usize;2])"] = s("[usize;2]") * (2 * CC)
if AA > 1:
    rows["T13.3 SP batch native sources (native_call: |A| PrimitiveSource, one adapter reservation)"] = s("PrimitiveSource") * AA
ASM.update({"s(CaseSlot)": 1560, "s([usize;2])": 16, "s(PrimitiveSource)": 1024})
out = {"which": which, "counts": dict(n=n, m=m, s=sp, r=r, l=l, g=g, N=N, F=F, k=k, Q=Q, U=U, P=P, Zu=Zu, H=Hp,''')
patch("g5_profile.py", '''forms = tree["forms"]; exprs = tree["exprs"]; phases = tree["phases"]''',
      '''BIND.update({   # I104 SQ (RV112 N-5): SP's adapter-reserved owners
    "s(CaseSlot)": sz("crate::retained_product::CaseSlot"), "s([usize;2])": sz("[usize; 2]"),
    "s(PrimitiveSource)": sz("open_pipe_stress_frame_kernel::structural::retained_api::PrimitiveSource")})
forms = tree["forms"]; exprs = tree["exprs"]; phases = tree["phases"]''')
json.dump({"patches": LOG}, open(os.path.join(dst, "SQ_N5_PATCHES.json"), "w"), indent=1)
print(json.dumps({"patches": len(LOG)}))
