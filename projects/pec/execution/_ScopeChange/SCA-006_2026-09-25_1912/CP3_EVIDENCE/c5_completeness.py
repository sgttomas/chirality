#!/usr/bin/env python3
"""B6 Lane C5: snapshot and handoff completeness (Propagation_Plan.md §C5)."""
import hashlib, pathlib, sys, json
S = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c/projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912")
REQ = ["Brief.md", "Impact_Assessment.md", "Amendment_Preview.md", "Propagation_Plan.md",
       "Amendment_Actions.csv", "Amendment_Actions_CP2.csv", "Supersession_Delta.csv", "Supersession_Map.csv",
       "Pre_Change_Coverage.json", "Post_Change_Coverage.json", "Decision_Log.md", "Handoff_State.md",
       "RUN_SUMMARY.md", "PRD_V2_4_SUCCESSOR_DIFF.md", "AGENTS_MD_CANDIDATE_DIFF.md", "CP2_CANDIDATE"]
out, missing = {}, []
for n in REQ:
    p = S / n
    if not p.exists():
        missing.append(n); continue
    if p.is_dir():
        out[n] = {str(f.relative_to(S)): hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p.rglob("*")) if f.is_file()}
    else:
        out[n] = hashlib.sha256(p.read_bytes()).hexdigest()
extra = sorted(str(f.relative_to(S)) for f in S.rglob("*") if f.is_file() and f.relative_to(S).parts[0] not in REQ)
rs = (S / "RUN_SUMMARY.md").read_text() if (S / "RUN_SUMMARY.md").exists() else ""
fields = ["DecompositionTruthState", "DerivativePackageState", "ContentRemediationState", "DownstreamRerunState",
          "MetadataAlignmentState", "AuditState", "ReadyForNextPhase"]
fmiss = [f for f in fields if f"`{f}`" not in rs]
hs = (S / "Handoff_State.md").read_text()
hmiss = [f for f in fields if f"`{f}`" not in hs.split("## Checkpoint-3 preparation")[-1]] if "## Checkpoint-3 preparation" in hs else ["checkpoint-3 section absent"]
print(json.dumps({"missing": missing, "state_fields_missing_in_RUN_SUMMARY": fmiss,
                  "state_fields_missing_in_Handoff_checkpoint3_section": hmiss,
                  "hashes": out, "additional_files": extra}, indent=1))
sys.exit(1 if (missing or fmiss or hmiss) else 0)
