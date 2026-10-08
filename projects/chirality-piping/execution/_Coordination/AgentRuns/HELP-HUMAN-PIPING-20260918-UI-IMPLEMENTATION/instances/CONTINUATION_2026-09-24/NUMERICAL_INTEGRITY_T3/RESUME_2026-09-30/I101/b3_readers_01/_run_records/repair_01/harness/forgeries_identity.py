"""I101 repair 01: the four forgeries as materialized by the RS test (B3B_INPUTS_OUT) against RV120's input lines: value
equality, and RV120's own input_sha256 (sha256 of json.dumps([source, invocation], sort_keys=True, separators=(",", ":"))).
Usage: forgeries_identity.py <rs inputs dump> <RV120 forge_eg_inputs.jsonl> <RV120 INPUTS_INDEX.jsonl>"""
import hashlib, json, sys
mine = [d for d in map(json.loads, open(sys.argv[1])) if d["name"].startswith("RV120 F2: ")]
rv = {d["name"]: d for d in (json.loads(l) for l in open(sys.argv[2]) if l.strip())}
idx = {d["name"]: d["input_sha256"] for d in map(json.loads, open(sys.argv[3])) if d["set"] == "inputs/forge_eg.jsonl"}
assert len(mine) == 4
for d in mine:
    key = f"forge {'E' if ': E ' in d['name'] else 'G'}-hat+1ulp, every copy, native hashes resealed [{d['base']}]"
    sha = hashlib.sha256(json.dumps([d["source"], d["invocation"]], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print(f"{d['name']} [{d['base']}]: equal to RV120's input {[d['source'], d['invocation']] == [rv[key]['source'], rv[key]['invocation']]}; "
          f"RV120's input_sha256 {sha == idx[key]} ({sha[:12]}…)")
