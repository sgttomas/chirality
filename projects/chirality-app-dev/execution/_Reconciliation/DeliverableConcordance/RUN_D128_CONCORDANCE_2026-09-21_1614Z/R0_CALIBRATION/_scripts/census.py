#!/usr/bin/env python3
"""Census of all R0 ledgers/reverse files. Prints markdown tables. No judgment."""
import csv, os, glob, collections, hashlib, re
H = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.dirname(H)
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n").split("\n")
    if t and t[-1].strip() == "#END": t = t[:-1]
    return list(csv.DictReader(t))
print("| Unit | Rows | Base keys | Split keys | LOW | Dispositions | Causes | PostRelease YES | HDN≠NO |")
print("|---|---|---|---|---|---|---|---|---|")
tot = collections.Counter(); totc = collections.Counter(); others = set()
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_claims.csv"))):
    rs = rows(f); u = os.path.basename(os.path.dirname(f))
    b = collections.Counter(re.sub(r"\.\d+$", "", r["ClaimKey"]) for r in rs)
    d = collections.Counter(r["Disposition"] for r in rs); c = collections.Counter(r["CauseTag"] for r in rs)
    tot.update(d); totc.update(c); others |= {x for x in c if x.startswith("OTHER:")}
    print(f"| {u} | {len(rs)} | {len(b)} | {sum(1 for v in b.values() if v>1)} | {sum(r['Confidence']=='LOW' for r in rs)} | "
          + "; ".join(f"{k} {v}" for k, v in d.most_common()) + " | " + "; ".join(f"{k} {v}" for k, v in c.most_common())
          + f" | {sum(r['PostReleaseBasis']=='YES' for r in rs)} | {sum(r['HumanDecisionNeeded'] not in ('NO','') for r in rs)} |")
print("\nTOTAL dispositions:", dict(tot.most_common())); print("TOTAL causes:", dict(totc.most_common())); print("OTHER tokens:", sorted(others))
print("\nClaimType x unit:")
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_claims.csv"))):
    print(os.path.basename(os.path.dirname(f)), dict(collections.Counter(r["ClaimType"] for r in rows(f))), "tier", dict(collections.Counter(r["AuthorityTier"] for r in rows(f))))
print("\nReverse:")
capf = os.path.join(R0, "SURFACES", "HARNESS_capabilities.csv")
caps = [r["CapabilityID"] for r in rows(capf)] if os.path.exists(capf) else []
claimed = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(R0, "DEL-*", "*_reverse.csv"))):
    rs = rows(f); u = os.path.basename(os.path.dirname(f))
    print(u, dict(collections.Counter(r["Response"] for r in rs)))
    for r in rs:
        if r["Response"] != "NOT_MINE": claimed[r["CapabilityID"]].append(f"{u}:{r['Response']}")
print("Unclaimed capabilities:", [c for c in caps if c not in claimed])
print("Multiply claimed (>1 unit, excluding A/B double):", {c: v for c, v in claimed.items() if len({x.split(':')[0].replace('_A','').replace('_B','') for x in v}) > 1})
