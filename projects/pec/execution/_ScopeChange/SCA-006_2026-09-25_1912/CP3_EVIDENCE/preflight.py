#!/usr/bin/env python3
"""Run pec_reliance_hold.py for every B6 write target (cwd projects/pec)."""
import subprocess, sys, json
D = "2026-09-26"
DC = "20260926"
T = [
 "execution/_Decomposition/SOFTWARE_DECOMP.md",
 "execution/_Decomposition/ScopeLedger.csv",
 "execution/_Decomposition/Deliverables.csv",
 "execution/_Decomposition/ContextBudgetQA.csv",
 "execution/_Decomposition/Companion_Inventory.csv",
 "docs/PRD.md",
 "execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md",
 "execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md",
 "execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md",
 "AGENTS.md",
 f"../../docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-{DC}.yaml",
 f"../../execution/_Coordination/NOTICE_{D}_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 f"../chirality-app-dev/execution/_Coordination/NOTICE_{D}_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 f"../chirality-runtime/execution/_Coordination/NOTICE_{D}_PEC_SCA-006_OPERATIONAL_RELIANCE.md",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/AGENTS_MD_AMENDMENT1_DIFF.md",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/Supersession_Map.csv",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/Post_Change_Coverage.json",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/RUN_SUMMARY.md",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/Decision_Log.md",
 "execution/_ScopeChange/SCA-006_2026-09-25_1912/Handoff_State.md",
 "execution/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_",
 "execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/B6_SCA006_CHECKPOINT3.md",
]
ops = sys.argv[1:] or ["exact-correction-preparation", "candidate-validation", "dispatch-for-production"]
bad = 0
n = 0
for op in ops:
    for t in T:
        r = subprocess.run([sys.executable, "execution/_Scripts/pec_reliance_hold.py", "--register",
                            "execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv", "--target", t,
                            "--operation", op], capture_output=True, text=True)
        n += 1
        st = json.loads(r.stdout)["status"] if r.stdout.strip() else "NO-OUTPUT"
        if r.returncode != 0 or st != "ALLOW":
            bad += 1
            print("BLOCK", op, t, r.returncode, r.stdout, r.stderr)
    print(f"{op}: {len(T)} targets checked")
print(f"total {n} runs, non-ALLOW {bad}")
sys.exit(1 if bad else 0)
