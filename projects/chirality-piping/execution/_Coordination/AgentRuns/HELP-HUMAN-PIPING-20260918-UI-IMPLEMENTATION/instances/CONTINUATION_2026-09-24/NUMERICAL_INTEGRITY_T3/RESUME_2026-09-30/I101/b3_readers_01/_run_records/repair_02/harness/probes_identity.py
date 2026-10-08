"""I101 repair 02: RV120's N2 and F1 probes as materialized by the RS test (B3B_INPUTS_OUT) against RV120's input index
(input_sha256 = sha256 of json.dumps([source, invocation], sort_keys=True, separators=(",", ":"))).
Usage: probes_identity.py <rs inputs dump> <RV120 INPUTS_INDEX.jsonl>"""
import hashlib, json, sys
idx = {d["name"]: d["input_sha256"] for d in map(json.loads, open(sys.argv[2]))}
names = {"RV120 N2: an exact_cases entry for a case not in the invocation": "X G8: an exact_cases entry for a case not in the invocation",
         "RV120 F1 control: case 0's evidence As_m2 one ulp": "X G5b control: case 0's evidence As_m2 one ulp",
         "RV120 F1 control: case 1's body_scales force one ulp": "X G5b control: case 1's body_scales force one ulp",
         "RV120 F1 order: case 0's evidence As_m2 and case 1's body_scales force": "X G5b order: case 0's evidence As_m2 and case 1's body_scales force",
         "RV120 F1 order: case 0's evidence As_m2 and case 1's section term area": "X G5b order: case 0's evidence As_m2 and case 1's section term area"}
n = 0
for d in map(json.loads, open(sys.argv[1])):
    if d["name"] not in names: continue
    key = f"{names[d['name']]} [{d['base']}]"
    sha = hashlib.sha256(json.dumps([d["source"], d["invocation"]], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print(f"{d['name']} [{d['base']}]: RV120's input_sha256 {sha == idx.get(key)} ({sha[:12]}…)"); n += 1
print(n, "probes")
