"""I104 SQ (PLAN_v2 §3.6): the RSS/time batch lists. Dev/test: the registered challenge binary (one
entry per input, mode and route, and the process floor). Release: the release lib test binary's
witnesses for the same inputs (W1 milestone as the control), the ordinary-route controls and the floor.
Usage: mk_rss_lists.py <challenge bin> <release lib bin> <out dir>"""
import os, sys
ch, rel, out = sys.argv[1:4]
inputs = [("milestone", "sd"), ("w_c2", "sd"), ("w_c2_ac", "s"), ("w2", "sd"), ("b2_k1e3", "sd"), ("c1", "sd"), ("i3_three_case", "sd")]
M = {"s": "sparse", "d": "dense"}
dev = {"devA": ["floor " + ch + " process_floor"], "devB": [], "devC": []}
for name, modes in inputs:
    batch = "devC" if name == "i3_three_case" else ("devB" if name in ("b2_k1e3", "c1") else "devA")
    for m in modes:
        for route in ("direct", "ordinary"):
            dev[batch].append(f"dev.{name}.{M[m]}.{route} {ch} {name}::{M[m]}::{route}")
W = "retained_memory::witness_tests::"
wit = {"milestone": "witness_w1_milestone", "w_c2": "witness_w_c2_publishes", "w2": "witness_w2_cap_maximal",
       "b2_k1e3": "witness_w2b_replacement_b2_k1e3", "c1": "witness_c1_cap_maximal_publishes", "i3_three_case": "witness_i3_three_case"}
rel_lines = [f"rel.floor {rel} {W}control_process_floor", f"rel.w_c2_ac.sparse.witness {rel} {W}witness_w_c2_ac_publishes_sparse"]
for name, modes in inputs:
    if name == "w_c2_ac":
        continue
    for m in modes:
        rel_lines.append(f"rel.{name}.{M[m]}.witness {rel} {W}{wit[name]}::{M[m]}")
        rel_lines.append(f"rel.{name}.{M[m]}.ordinary {rel} {W}control_ordinary_{name}::{M[m]}")
os.makedirs(out, exist_ok=True)
for k, v in list(dev.items()) + [("rel", rel_lines)]:
    open(os.path.join(out, f"{k}.list"), "w").write("\n".join(v) + "\n")
    print(k, len(v))
