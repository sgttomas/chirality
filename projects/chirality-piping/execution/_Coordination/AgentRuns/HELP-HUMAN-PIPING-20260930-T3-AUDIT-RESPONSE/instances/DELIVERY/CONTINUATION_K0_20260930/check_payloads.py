#!/usr/bin/env python3
"""Source-derived payload arithmetic only; no model, compiler or source write."""
import hashlib
import json
from pathlib import Path
import subprocess
root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
p = root / "projects/chirality-piping/core/solver/performance_harness/observations/k6b/counts.jsonl"
expected = "fab0466a846ef26b1c530a261a6f1d134fc32ba1d70f57682010877a52373c05"
if hashlib.sha256(p.read_bytes()).hexdigest() != expected:
    raise SystemExit("counts input drift")
rows = [json.loads(line) for line in p.read_text().splitlines() if line]
results = []
for x in rows:
    N, m, t, r, loads = (x["w1_" + key] for key in ("nodes", "members", "stations", "constraints", "loads"))
    q = 7*N + 12*m + 6*t + r
    payload_base = 38 + 24*N + 84*m + 13*r + 16*t + 17*loads
    ids = x["w1_source_encoding_len"] - payload_base
    ids_max = loads * (3 + len(str(max(0, 6*N-1))))
    assert q == x["w1_rows"], x["model"]
    assert 4*loads <= ids <= ids_max, x["model"]
    results.append({"model": x["model"], "q": q, "K4SRC_id_bytes": ids,
                    "K4STF": 26+24*N+84*m+5*r,
                    "K4LED_upper": 10+562*loads,
                    "K4RST_by_width": {str(W): 22+(6*N+6*m)*(9+8*W) for W in (4,8,16)}})
print(json.dumps({"source_counts_sha256": expected, "models_checked":len(results),
                  "result":"PASS source cardinality/payload checks", "rows":results,
                  "limits":"Payloads are not capacities or final E_max; no runtime/model performed."}, indent=2))
