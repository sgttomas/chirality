import json, hashlib, sys, os
R, T = sys.argv[1], sys.argv[2]
P = R + "/projects/pec/execution"
D = P + "/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures"
led = P + "/_Coordination/D1_PREMISE_AMEND_2026-09-27/premise/"
ok = True
for key, pre, cur in [("DEL-00-01_ADR", T+"/pre/ADRs.md", D+"/artifacts/v2/ADRs.md"),
                      ("DEL-00-01_SOW", T+"/pre/ScopeOfWork.md", D+"/ScopeOfWork.md")]:
    L = json.load(open(led + key + ".json"))
    text = open(pre, encoding="utf-8").read()
    assert hashlib.sha256(text.encode()).hexdigest() == L["preimage_sha256"], key + " preimage hash mismatch"
    for h in L["hunks"]:
        n = text.count(h["pre"])
        if n != 1:
            print(key, h["id"], "pre occurrences", n); ok = False; continue
        text = text.replace(h["pre"], h["post"])
    curb = open(cur, encoding="utf-8").read()
    same = curb == text
    print(key, "hunks", len(L["hunks"]), "rendering equals current bytes:", same,
          "sha", hashlib.sha256(text.encode()).hexdigest())
    ok &= same
print("RESULT", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
