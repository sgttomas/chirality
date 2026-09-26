#!/usr/bin/env python3
"""B6 Lane C1: exact-write containment (Propagation_Plan.md §C1, brief B6 C1).

Input: a file listing `git diff --name-status <basis> HEAD` (plus any
uncommitted paths), produced separately. Checks every changed path against the
Lane A allowlist, asserts planned postimage hashes under the slot rule, and
asserts checkpoint-1/2 artifacts byte-unchanged.
Usage: c1_containment.py <name-status-file>
"""
import fnmatch, hashlib, json, pathlib, sys
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
SNAP = "projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912"
def sha(p): return hashlib.sha256((R / p).read_bytes()).hexdigest()
ALLOW = [
 "projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md",
 "projects/pec/execution/_Decomposition/ScopeLedger.csv",
 "projects/pec/execution/_Decomposition/Deliverables.csv",
 "projects/pec/execution/_Decomposition/ContextBudgetQA.csv",
 "projects/pec/execution/_Decomposition/Companion_Inventory.csv",
 "projects/pec/docs/PRD.md",
 "projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md",
 "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md",
 "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md",
 "projects/pec/AGENTS.md",
 "docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml",
 "execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 "projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 "projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 f"{SNAP}/*",
 "projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_*/*",
 "projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B6_SCA006_CHECKPOINT3.md",
 "projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B6_VERIFIER_VERDICT_[0-9][0-9].md",
]
POST = {
 "projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md": "3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59",
 "projects/pec/execution/_Decomposition/ScopeLedger.csv": "1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e",
 "projects/pec/execution/_Decomposition/Deliverables.csv": "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805",
 "projects/pec/execution/_Decomposition/ContextBudgetQA.csv": "93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c",
 "projects/pec/execution/_Decomposition/Companion_Inventory.csv": "1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662",
 "projects/pec/docs/PRD.md": "ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe",
 "projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md": "b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22",
 "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md": "74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22",
 "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md": "95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5",
 "projects/pec/AGENTS.md": "4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c",
 "docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml": "2b29af181947ba0ed75cd83a286c56a2863802d1d6a7e5b3ca9ab82330cdee74",  # after the approval update of group2_amendment_1 (first written f7f48690...)
 "execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md": "b3c60bf489e41d45465bd38a0a7f3f3ca73ea4d392f987eff84a95bd888fc601",
 "projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md": "af4f63426b55a96c4f18fee702b9af8eb5394b2b531dfddef3f8f090622f68ef",
 "projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md": "e883efac1829f0f2a10cceae778c92cd6baec6a37d1f4e6349442dd4c8f7bb93",
}
FROZEN = {  # checkpoint-1 / checkpoint-2 artifacts that must stay byte-unchanged
 f"{SNAP}/Brief.md": "205a46c04f2db6d34bead78db3064a02ff9d9d66a5e54fa9ff06b5c6314a1831",
 f"{SNAP}/Impact_Assessment.md": "93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691",
 f"{SNAP}/Amendment_Actions.csv": "c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891",
 f"{SNAP}/Pre_Change_Coverage.json": "b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d",
 f"{SNAP}/Amendment_Preview.md": "737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4",
 f"{SNAP}/Propagation_Plan.md": "f95d00d154610d44a37d4aeabfae3fff29aac6c0a0c016bb1241810ebc87d7d8",
 f"{SNAP}/Amendment_Actions_CP2.csv": "d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de",
 f"{SNAP}/Supersession_Delta.csv": "e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b",
 f"{SNAP}/PRD_V2_4_SUCCESSOR_DIFF.md": "a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c",
 f"{SNAP}/AGENTS_MD_CANDIDATE_DIFF.md": "7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158",
 f"{SNAP}/CP2_CANDIDATE/docs/PRD.md": "ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe",
 f"{SNAP}/CP2_CANDIDATE/AGENTS.candidate.md": "49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d",
 f"{SNAP}/CP2_CANDIDATE/AGENTS.candidate_without_I1.md": "a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188",
 f"{SNAP}/CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md": "4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71",
 f"{SNAP}/CP2_CANDIDATE/_Decomposition/ScopeLedger.csv": "1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e",
 f"{SNAP}/CP2_CANDIDATE/_Decomposition/Deliverables.csv": "94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805",
 f"{SNAP}/CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv": "93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c",
 f"{SNAP}/CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv": "1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662",
 "projects/pec/execution/_ScopeChange/_LATEST.md": "e92b3b16a48cd72288c8b6eddc08d62e3e79e0c9bec521864ee7d5484a307d24",
 "projects/pec/execution/_Decomposition/_LATEST.md": "626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd",
}
SNAP_MUTABLE = {f"{SNAP}/Decision_Log.md", f"{SNAP}/Handoff_State.md"}
lines = [l.split("\t") for l in pathlib.Path(sys.argv[1]).read_text().splitlines() if l.strip()]
changed = [(s[0], s[-1]) for s in lines]
fails, rows = 0, []
for status, path in changed:
    allowed = any(fnmatch.fnmatchcase(path, pat) for pat in ALLOW)
    if path in FROZEN:
        allowed = False
    if status.startswith("D"):
        allowed = False
    if path.startswith(f"{SNAP}/") and status.startswith("M") and path not in SNAP_MUTABLE:
        allowed = False  # only additive files or the two living logs may change
    rows.append({"status": status, "path": path, "allowed": allowed})
    fails += (not allowed)
hash_rows = []
for p, h in POST.items():
    got = sha(p); ok = got == h; fails += (not ok)
    hash_rows.append({"path": p, "expected": h, "observed": got, "ok": ok})
for p, h in FROZEN.items():
    got = sha(p); ok = got == h; fails += (not ok)
    hash_rows.append({"path": p, "expected": h, "observed": got, "ok": ok, "frozen": True})
missing = [p for p in POST if p not in {c[1] for c in changed}]
fails += len(missing)
print(json.dumps({"changed_paths": len(changed), "not_allowed": [r for r in rows if not r["allowed"]],
                  "hash_checks": len(hash_rows), "hash_failures": [r for r in hash_rows if not r["ok"]],
                  "planned_writes_missing_from_diff": missing, "fails": fails, "paths": rows}, indent=1))
sys.exit(1 if fails else 0)
