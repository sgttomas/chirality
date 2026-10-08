"""RV124: b2_k1e3's failing row verdicts by kind and unit, from freeze_case's own I51_FROZEN_REFUSAL line (cfg(test)) in the witness runs."""
import json, collections
S = "WT/scratch/rv124_rvq/logs/wit/"
PROJ = {"mm": "/1000 (mm->SI, NC-1)", "MPa": "x1e6 (MPa->Pa)", "Pa": "none", "N": "none", "N*m": "none", "rad": "none"}
for mode in ("sparse", "dense"):
    for line in open(S + f"witness_w2b_replacement_b2_k1e3__{mode}.log"):
        i = line.find("I51_FROZEN_REFUSAL ")
        if i < 0:
            continue
        d = json.loads(line[i + len("I51_FROZEN_REFUSAL "):])
        rows, ver = d["rows"], d["verdicts"]
        fails = [v for v in ver if not v["passed"]]
        c = collections.Counter((rows[v["row"]]["kind"], rows[v["row"]]["unit"], str(v["predicates"])) for v in fails)
        print(f"b2_k1e3 {mode}: rows {len(rows)}, verdicts {len(ver)}, failing {len(fails)}")
        for (kind, unit, pred), n in c.most_common():
            print(f"  {n:3d}  {kind:45s} {unit:4s} projection {PROJ.get(unit, '?'):22s} predicates {pred}")
        u = collections.Counter(PROJ.get(rows[v["row"]]["unit"], "?") for v in fails)
        print("  by projection:", dict(u))
