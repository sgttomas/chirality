"""I100 B3 addendum 01: a scratch corpus whose bases are materialized exact-route shapes, for the RV113 harnesses'
census mode (bases are read raw, so the exact route's preparation hash stands). Bases: lane P's m3x successor and
the synthetic m3x, each with x08 (an analysis_state member), p02 (a case-level pressure key) and no edit, both modes.
Usage: add1_exact_corpus.py <P root with B3's tests> <archive corpus path>"""
import json
import sys

P = sys.argv[1]
sys.path[:0] = [P, P + "/tests"]
import test_retained_precision_b3 as t  # noqa: E402

LABELS = {"x08": "x08 a case with analysis_state", "p02": "p02 a case-level pressure key (PP's typed case has none; addendum 01)"}
cases = []
for mode in t.MODES:
    for kind in t.KINDS:
        cases.append({"id": f"exact {kind} base [{mode}]", "source": t.exact_base(mode, kind)[0], "invocation": t.exact_base(mode, kind)[1]})
        for short, label in LABELS.items():
            source, invocation = t.exact_shape(mode, label, kind)
            cases.append({"id": f"exact {kind} {short} [{mode}]", "source": source, "invocation": invocation})
corpus = json.load(open(sys.argv[2]))
corpus.update(cases=cases, mutations=[], must_pass=[])
json.dump(corpus, open(sys.argv[2], "w"))
print(len(cases), "exact bases")
