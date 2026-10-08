"""I100 B3 addendum 01: the sourced-case probes on the preview route, from PP's pinned milestone successors.
Appends the two milestone successors to the scratch archive's corpus as bases `milestone_<mode>` (scratch only), and
writes the probes in the shared corpus grammar (invocation edits on the sourced case, rehash all; DEF-O's H).
Usage: add1_probes.py <archive P root> <probes.json>"""
import hashlib
import json
import sys

P = sys.argv[1]
PINNED = {"sparse_interactive": "ac6986b0680e0df9d88c33a5bf4635372fc3b83cbb9080da44e6d32dbdca59dc",
          "dense_scrutiny": "6cd1d249e5352aaffbd2b7d7349c74a1d0e0572df35500f66be49c3cad95c9b5"}
corpus_path = f"{P}/fixtures/results/retained_precision_cases.json"
corpus = json.load(open(corpus_path))
assert not any(c["id"].startswith("milestone_") for c in corpus["cases"])
for mode, sha in PINNED.items():
    raw = open(f"{P}/fixtures/results/retained_precision_milestone_successor_{mode}.json", "rb").read()
    assert hashlib.sha256(raw).hexdigest() == sha
    doc = json.loads(raw)
    corpus["cases"].append({"id": f"milestone_{mode}", "source": doc["source"], "invocation": doc["invocation"]})
json.dump(corpus, open(corpus_path, "w"))
CASE = ["request", "model", "load_cases", 0]
VALUES = [
    ("analysis_state", "object", {"kind": "load_reference_state"}),
    ("analysis_state", "null", None),
    ("analysis_state", "empty object", {}),
    ("pressure", "quantity", {"value": 1000.0, "unit": "Pa"}),
    ("pressure", "null", None),
    ("pressure", "zero", 0),
    ("pressure_regions", "string", "x"),
    ("pressure_regions", "empty object", {}),
    ("pressure_regions", "object", {"id": "region:x"}),
    ("pressure_regions", "zero", 0),
    ("pressure_regions", "one", 1),
    ("pressure_regions", "true", True),
    ("pressure_regions", "false", False),
    ("pressure_regions", "empty string", ""),
    ("pressure_regions", "empty array (B3D-11)", []),
    ("pressure_regions", "null", None),
    ("pressure_regions", "one region", [{"id": "region:x", "member_pipe_ids": ["M1"]}]),
    ("equivalent_static", "empty object", {}),
    ("equivalent_static", "false", False),
    ("equivalent_static", "zero", 0),
    ("equivalent_static", "null", None),
    ("notes", "an unknown key (control)", "free text"),
]
probes = []
for mode in PINNED:
    for key, label, value in VALUES:
        probes.append({"id": f"add1 {key} = {label} [{mode.split('_')[0]}]", "base": f"milestone_{mode}", "edits": [],
                       "invocation_edits": [{"path": CASE + [key], "op": "set", "value": value}], "rehash": "all"})
json.dump(probes, open(sys.argv[2], "w"), indent=1)
print(len(probes), "probes")
