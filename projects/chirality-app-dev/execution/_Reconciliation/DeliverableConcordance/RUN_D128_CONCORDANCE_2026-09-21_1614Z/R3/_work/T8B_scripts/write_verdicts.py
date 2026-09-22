"""Write T8B_VERDICTS.csv from the sample file and the hand-recorded verdicts below."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R3 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(R3, "_scripts"))
from r3lib import read_csv, write_csv  # noqa: E402

AD = "projects/chirality-app-dev"
RT = "projects/chirality-runtime"
FE = AD + "/frontend"
PREF_HASH = "docs/PRD.md recomputes to 17ca3f3c… at the frozen basis, not the recorded 8649ccba…"

C = "CONFIRMED"
V = {
    "S1-082": (C, "", f"{AD}/docs/harness/reliance_boundary_register.md:143; {RT}/packages/daemon/src/runtime-daemon.ts:287-293 listen on socket path then chmod 0o600; {RT}/packages/daemon/src/app-owned-composition.ts:252 token dir 0o700; {FE}/electron/runtime-service-host.ts:122-127; no TCP listen in daemon src"),
    "S1-083": (C, "", f"{AD}/docs/RELEASE_QUALITY_GATES.md:46-59 is a process rule for docs-only tranches; nothing in it is contradicted at the frozen basis"),
    "S1-084": (C, "", f"{AD}/execution/_Coordination/_DECISIONS/D-APP-111_RULING_SCA_APP_010_POINTER_ACCEPTANCE_2026-09-05.md:22-44 effects 1-4 match {AD}/execution/_Reconciliation/DepClosure/_LATEST.md:1, _Evaluation/DecompCoverage/_LATEST.md:1, _Reconciliation/_LATEST.md:1-3 and SCA-APP-010 Handoff_State.md:12"),
    "S1-085": (C, "", f"{AD}/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:455 maps SOW-052 to DEL-04-02; DEL-04-02 ScopeOfWork.md cites SOW-052"),
    "S1-086": (C, "", f"{FE}/package.json:30 instruction-root:integrity; {FE}/scripts/verify-instruction-root-integrity.mjs:739-782 writes summary.json"),
    "S1-087": (C, "", f"{FE}/package.json:29; {FE}/scripts/validate-release-quality-evidence.mjs:8 imports validate-harness-premerge run, :22-30 writes artifacts/harness/release-quality/latest/summary.json"),
    "S1-088": (C, "", f"No non-test importer of @chirality/harness-contract in {FE}/src or {FE}/electron; {FE}/package.json:51 depends on runtime-contracts only; {FE}/scripts/assert-harness-contract-deps.mjs:110-122 guards against re-adding the facade"),
    "S1-089": (C, "", f"Live chain forwards maxTurns ({FE}/src/lib/harness/toolkit.ts:139-148; {RT}/packages/core/src/turn-coordinator.ts:182) but the Codex adapter reads only opts.model and opts.mode ({RT}/packages/core/src/delegated-engine-adapter.ts:116-121,203-206); no live guard. Other reading: forwarded but inert input as PARTIALLY_IMPLEMENTED; not preferred because the input has no effect"),
    "S1-090": (C, "", f"{FE}/docs/harness/tool_catalog.md:57-87 describes SDK/in-process MCP exposure and an 'Anthropic-only runtime policy'; live tool policy is the Codex path ({RT}/packages/core/src/runtime-method-service.ts:507-518; {RT}/packages/core/src/runtime-service.ts:580 mcpServers: [])"),
    "S1-091": (C, "", f"{AD}/docs/harness/reliance_boundary_register.md:47,66 name SDK transcript linkage; live linkage is the Codex thread (codex-supervisor thread/start and thread/resume) with Chirality events canonical: another mechanism"),
    "S1-092": (C, "", f"{AD}/docs/BUILD_AND_RELEASE.md:127-129 heading followed directly by §8.1"),
    "S1-093": (C, "", f"contextReferences is referenced only in {FE}/src/lib/woven-dialogue/woven-workspace-state.ts:127,515,546,589 (no consumer in src or electron); explicit chips and attachments exist, so part is met"),
    "S1-094": (C, "", f"{RT}/packages/contracts/src/application-tools.ts:47 collision key on the live path; {RT}/packages/core/src/runtime-service.ts:580 mcpServers: []; wrappers only in legacy read-tools.ts"),
    "S1-095": (C, "", f"{AD}/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md:159-174 supersedes D-APP-107 in whole and keeps DEL-09-07 and D-APP-104 as immutable history; _REGISTER.md:152"),
    "S1-096": (C, "", f"{FE}/docs/harness/TRACEABILITY.md:22 lists a 13-ID 'current deterministic ID set'; {FE}/scripts/validate-harness-section9.mjs:29-46 defines 16 IDs"),
    "S1-097": (C, "", f"{AD}/docs/BUILD_AND_RELEASE.md:64 says unsigned/unnotarized and omits the codex-pin step; {FE}/package.json:43 adds desktop:verify-codex-pin --after-signing; {FE}/scripts/pack-electron.mjs:80-95 signs when an identity is set"),
    "S1-098": (C, "", f"DEL-06-02 ScopeOfWork.md:500-504 restates the D-APP-56 roster split; no contrary record found"),
    "S1-099": (C, "", f"{RT}/packages/core/src/session-store.ts:825-905 replays the full events.jsonl; truncate calls at :750,:807 are transaction rollback of the tail being written, not compaction; no runtime compaction step deletes events"),
    "S1-100": (C, "", f"{RT}/packages/core/src/delegated-engine-adapter.ts:265-266 caps each tool.progress delta at 65536 chars; no live preview or artifact store for command output; artifact store only in legacy {FE}/src/lib/harness/tool-result-artifacts.ts"),
    "S1-101": (C, "", f"DEL-06-01 ScopeOfWork.md:156 REQ-015; live approvals come from Codex server requests ({RT}/packages/daemon/src/codex-supervisor.ts:714), not the legacy overlay input contract"),
    "S1-102": (C, "", f"{RT}/packages/core/src/runtime-method-service.ts:507-518 filters by mode, role and method, no registry lookup; {RT}/packages/core/src/delegated-engine-adapter.ts:116-121 ignores opts.tools"),
    "S1-103": (C, "", f"DEL-06-04 ScopeOfWork.md:31-42 matches decomposition row {AD}/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:349; nothing false to report"),
    "S1-104": (C, "", "DEL-06-05 ScopeOfWork.md:354-360 purpose statement; non-normative"),
    "S1-105": (C, "", f"Symlink/regular-file checks exist in legacy chirality-hooks.ts and tool-path-policy.ts; live App write surface {FE}/electron/plan-export-dialog.ts:19-31 refuses symlink segments. HumanDecisionNeeded note: LIVE code meets part of the claim, so rule 3 (CONVENTIONS §2.4) may not call for R4-Q1"),
    "S1-106": (C, "", f"{RT}/packages/core/src/delegated-engine-adapter.ts:265-266 one combined outputDelta stream; separate fields only in legacy tool-evidence.ts"),
    "S1-107": (C, "", f"DEL-06-03 _DEPENDENCIES.md:14,18 'TBD - no accepted dependency edges' while Dependencies.csv holds 18 ACTIVE rows; register bookkeeping lag (tie-break rule 2b)"),
    "S1-108": (C, "", f"DEL-06-04 _CONTEXT.md:48 calls Claude Agent SDK the current path; the live engine is Codex"),
    "S1-109": (C, "", PREF_HASH + "; the text restates MATCH as current (tie-break rule 3)"),
    "S1-110": (C, "", f"DEL-06-02 ScopeOfWork.md:215,217 say implementation paths remain TBD; resolver and registry exist ({RT}/packages/contracts/src/harness/tool-descriptor.ts; {FE}/src/lib/harness/tool-pool.ts)"),
    "S1-111": (C, "", PREF_HASH),
    "S1-112": ("REFUTED", "IMPLEMENTED_DIFFERENTLY", f"DEL-06-04 ScopeOfWork.md:413 states what the SPEC inventory names, and {AD}/docs/SPEC.md:814-823 still names status_transition/deps_write as write-gated and scaffold as gated, so no stated fact is false (STALE_SPECIFICATION needs a now-false state, CONVENTIONS §2.6). The requirement part diverges: no Chirality MCP tools on the live path ({RT}/packages/core/src/runtime-service.ts:580 mcpServers: []); legacy classifies scaffold as read-only scaffold_preview ({RT}/packages/contracts/src/harness/tool-descriptor.ts:606-611) and gates writes by a handler wrapper, not the SDK Write/Edit hook sequence ({FE}/docs/harness/tool_catalog.md:72-73). Keep R4-Q1"),
    "S1-113": (C, "", f"DEL-07-06 ScopeOfWork.md:72 matches {AD}/docs/CONTRACT.md K-AUTH-1 and DIRECTIVE §2.4; judged as a documentation-convention condition of a conventions deliverable"),
    "S1-114": (C, "", f"{FE}/src/lib/dependencies/register-writer.ts:54-95 fills absent columns with empty strings and passes values through; no value is guessed"),
    "S1-115": (C, "", "DEL-07-06 ScopeOfWork.md:188 verification approach is conditional ('TBD unless separately verified'); nothing contradicted"),
    "S1-116": (C, "", f"Live runtime picks known opts keys and drops others silently ({RT}/packages/core/src/turn-coordinator.ts:127-187); no warning on the live path. HumanDecisionNeeded note: SPEC §13.1 ({AD}/docs/SPEC.md:780) governs harness opts, and legacy {FE}/src/lib/harness/options.ts:7-22 does warn, so rule 3 would add R4-Q1"),
    "S1-117": (C, "", f"{RT}/packages/daemon/src/app-owned-composition.ts:226 builds RuntimeService without a scaffold port; {RT}/packages/core/src/runtime-service.ts:619-623 throws ENGINE_UNAVAILABLE 501; creation code reached only from tests"),
    "S1-118": (C, "", "DEL-07-01 ScopeOfWork.md CLM-007 reference list; cited sections exist; non-normative"),
    "S1-119": (C, "", "DEL-07-06 ScopeOfWork.md:328-332 Pass 3 method notes; non-normative"),
    "S1-120": (C, "", f"{FE}/src/lib/runtime-client/runtime-daemon-harness-port.ts:602-618 live containsPath check covers containment; live scaffold has no instruction-root check. HumanDecisionNeeded note: the row's own verifier correction says 'no R4-Q1 (LIVE code meets part)' but the checked value is R4-Q1"),
    "S1-121": (C, "", f"Live register writer/reader and deliverable-contracts cover validation, retention, warnings, containment and symlink; permission/hook policy only in legacy read-tools.ts; target existence and instruction-root checks not found live"),
    "S1-122": (C, "", f"DEL-07-04 ScopeOfWork.md:206 REQ-016; route tests assert shapes only; no schema fixture tests for all listed schemas"),
    "S1-123": (C, "", "DEL-07-04 _DEPENDENCIES.md TBD placeholders and TBD=1 summary lag its own P45 block and Dependencies.csv; bookkeeping lag (tie-break rule 2b)"),
    "S1-124": (C, "", PREF_HASH),
    "S1-125": (C, "", PREF_HASH),
    "S1-126": (C, "", PREF_HASH),
    "S1-127": (C, "", f"docs/PRD.md 17ca3f3c… and docs/CONTRACT.md 57411f8d… recompute differently from the MATCH values in DEL-07-05 _REFERENCES.md:8,9,12 (SPEC also recomputes differently); register asserts a now-false fact (§2.7)"),
    "S1-128": (C, "", f"DEL-07-06 ScopeOfWork.md:316-319 lists Datasheet/Specification/Guidance/Procedure.md and REF-006 MATCH; none of the four files is in the frozen folder; PRD hash differs"),
    "S1-129": (C, "", f"DEL-08-03 ScopeOfWork.md:18-48 SCA-APP-010 Gate-5 Current Contract (controlling) retires the Pipeline presentation, code retained; D-APP-108 Q3 keeps /pipeline reachable but unlisted; selectors exist only in the unrendered surface"),
    "S1-130": (C, "", "Listed bridge, admission, retirement tests and path records exist in legacy modules and _run_records; module-level documentation claim"),
    "S1-131": (C, "", f"{FE}/src/components/woven-dialogue/woven-dialogue-route.tsx:14-20 discards the legacy surface; pipeline-dispatch-contract has no non-test importer"),
    "S1-132": (C, "", "Exclusion; no lifecycle, parentage or panel code in the DEL-08-03 modules"),
    "S1-133": (C, "", f"DEL-08-02 is not an SCA-APP-010 carrier (no Gate-5 section); its ScopeOfWork.md:71,167 still require coming-soon variants; the only coming-soon options sit in the unrendered Pipeline surface"),
    "S1-134": (C, "", f"16 KiB / 512 KiB limits exist only in {RT}/packages/contracts/src/harness/tool-descriptor.ts:190-196 and legacy tool-result-artifacts.ts; no live child-output artifact store"),
    "S1-135": (C, "", f"{RT}/packages/core/src/method-catalog.ts:620-626 defines TASK as type 2 on the live path; AGENT_TYPE/AGENT_CLASS frontmatter checks only in legacy subagent-governance.ts"),
    "S1-136": (C, "", f"{FE}/src/lib/shell/persona-resolution.ts:6-9 two aliases only; others fall back to HELP_HUMAN"),
    "S1-137": (C, "", "DEL-08-03 ScopeOfWork.md:459-467 Pass 3 method notes; non-normative"),
    "S1-138": (C, "", "DEL-08-01 ScopeOfWork.md:254-257 heading only"),
    "S1-139": (C, "", "DEL-08-04 ScopeOfWork.md:395-398 heading only"),
    "S1-140": (C, "", "No live re-hosted consumer uses the shared contract; the unrendered Pipeline surface keeps a parallel local copy; part holds only in TEST_ONLY code"),
    "S1-141": (C, "", f"DEL-08-01 ScopeOfWork.md:330-338; integrity script live, conformance checks legacy, REF-006 MATCH line false ({PREF_HASH})"),
    "S1-142": (C, "", f"Live turn route has no pipeline-intent channel ({FE}/src/app/api/harness/turn/route.ts:13-23); pass evidence exercises only the TEST_ONLY contract ({FE}/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts:28-48)"),
    "S1-143": (C, "", "DEL-08-03 _STATUS.md History says retained while Remaining is empty; bookkeeping lag"),
    "S1-144": (C, "", f"DEL-08-01 ScopeOfWork.md:116-118 restates REF-006 MATCH and no downstream edges; {PREF_HASH}"),
    "S1-145": (C, "", "docs/CONTRACT.md recomputes to 57411f8d…, not the recorded fa8fc9dc… MATCH"),
    "S1-146": (C, "", PREF_HASH),
    "S1-147": (C, "", f"{FE}/scripts/validate-harness-premerge.mjs exists and is readable"),
    "S1-148": (C, "", "Repeat of DEL-09-02#CLM-007, which carries the same Disposition in CLAIM_CONCORDANCE.csv; section9 manifest has 16 IDs incl. domain_profile_validation"),
    "S1-149": (C, "", f"{FE}/scripts/validate-harness-premerge.mjs:275 logs HARNESS_PREMERGE_SECTION9_REPORT_ONLY=true"),
    "S1-150": (C, "", f"{FE}/package.json:43 desktop:dist"),
    "S1-151": (C, "", f"{FE}/scripts/harness-section9-manifest.json:108-113 targets legacy subagent-governance.ts; live descendants are Codex-native child threads"),
    "S1-152": (C, "", "DEL-09-03 CLM-014 purpose statement; non-normative"),
    "S1-153": (C, "", "DEL-09-05 ScopeOfWork.md:290-297 purpose; cited sections exist"),
    "S1-154": (C, "", "Route tests drive live routes with a fake port; overlay and hook tests exercise legacy modules; no live denied-write/denied-Bash integration test found"),
    "S1-155": (C, "", f"{FE}/scripts/prepare-packaged-instruction-root.mjs:11-26 omits docs/PLAN.md etc. listed in {AD}/docs/SPEC.md:39-41; other principles met"),
    "S1-156": (C, "", "TBD placeholders (upload name, runbook, evidence location) lag an in-root non-executing workflow and a runbook candidate; nothing false about the product"),
    "S1-157": (C, "", "Open Items TBD list lags the same in-root workflow; bookkeeping lag"),
    "S1-158": (C, "", "D-APP-127 ruling :159-174 retires DEL-09-07 and keeps its folder and ScopeOfWork as immutable history"),
    "S1-159": (C, "", "As S1-158"),
    "S1-160": (C, "", f"DEL-09-02 ScopeOfWork.md:281-291 say status enum, runner, command and paths are TBD; {FE}/scripts/harness-section9-manifest.json:7 and {FE}/package.json:20 now define them"),
    "S1-161": (C, "", "DEL-09-03 Dependencies.csv rows are SATISFIED and _DEPENDENCIES.md summary shows TBD 0, against 'all satisfaction TBD'; PRD hash differs"),
    "S1-162": (C, "", f"{AD}/docs/SPEC.md:881-884 (amended for the Codex path) says the whole set is validated before dispatch and partial failure is legacy only; {RT}/packages/core/src/runtime-attachment-resolver.ts:10-49 returns errors: []; the SoW REQ-006 partial-failure test clause is stale wording under the amended SPEC"),
    "S1-163": (C, "", "DEL-09-03 Dependencies.csv TargetLocation line anchors (e.g. :269) no longer point at the rows; DEP-013 EvidenceFile Guidance.md is absent; register asserts now-false facts"),
    "S1-164": (C, "", f"{AD}/docs/SPEC.md:693-703 supersedes the fixed eight-name SSE set; {FE}/src/lib/harness/http.ts:57-87 streams Runtime frame types"),
    "S1-165": (C, "", f"DEL-10-01 ScopeOfWork.md:206 verification is 'Future path policy'; D-APP-49 (_REGISTER.md:64) rules types and guards only, no runtime behaviour"),
    "S1-166": (C, "", "_DomainEngines/profiles holds open_pipe_stress.yaml and pec.yaml; no *.adapter.yaml; api routes are harness, project, working-root only"),
    "S1-167": (C, "", "As S1-166"),
    "S1-168": (C, "", "DEL-10-05 ScopeOfWork.md:148-149 keeps schema and solver standards TBD"),
    "S1-169": (C, "", "No domain-operation apply path on any path; proposal tools legacy only"),
    "S1-170": (C, "", "Heading only"),
    "S1-171": (C, "", "Heading only"),
    "S1-172": ("UNDECIDED", "", f"The row's evidence is only that DEL-10-03 ScopeOfWork.md:369 omits 'ready-for-construction' from the {AD}/docs/CONTRACT.md:152 K-DOMAIN-4 list. Reading 1: a narrower restatement of a governing clause counts as partial coverage (PARTIALLY_IMPLEMENTED stands). Reading 2: PARTIALLY_IMPLEMENTED describes code, and no product-side professional claim was checked; the omission is a text defect (STALE_SPECIFICATION does not fit either, as nothing stated is false)"),
    "S1-173": (C, "", f"{FE}/src/__tests__/lib/domain-profile.test.ts:206-243 and operation-proposal.test.ts:98-128 cover some negative cases; no overlapping-path or core-coupling case"),
    "S1-174": (C, "", "DEL-10-05 Dependencies.csv TargetLocation uses stable anchors (#PKG-10, #SOW-071); the stale line numbers and SHAs sit in dated D-APP-53 notes (LastSeen 2026-07-10): metadata lag, unlike DEL-09-03's live line anchors"),
    "S1-175": (C, "", f"{AD}/docs/SPEC.md:1134 assigns the manifest path and schema id under D-APP-58, so 'adapter manifest schema TBD' is overtaken; glob syntax still undefined ({AD}/docs/TYPES.md:622)"),
    "S1-176": (C, "", "The four-document kit is absent from the DEL-10-04 folder; the verification text expects it. Other reading: STALE_VERIFICATION, which the rulebook does not define"),
    "S1-177": (C, "", "DEL-10-05 ScopeOfWork.md:70 quotes 86cb6f…/fb1c73…; _REFERENCES.md now records 8649ccba… MATCH; recompute is 17ca3f3c…"),
    "S1-178": (C, "", "_DomainEngines/profiles/open_pipe_stress.yaml:25 profile_status ADOPTED contradicts 'no accepted engine profile … exists'"),
}

_, rows = read_csv(os.path.join(R3, "_work", "SPOT_S1_B.csv"))
out = []
missing = []
for r in rows:
    sid = r["SampleID"]
    if sid not in V:
        missing.append(sid)
        continue
    verdict, proposed, ev = V[sid]
    out.append({
        "SampleID": sid, "ClaimKey": r["ClaimKey"], "CheckField": r["CheckField"],
        "CheckedValue": r[r["CheckField"]], "Verdict": verdict, "ProposedValue": proposed, "Evidence": ev,
    })
assert not missing, missing
assert len(out) == len(rows) == len(V)
for o in out:
    assert "/private/" not in o["Evidence"] and "/Users/" not in o["Evidence"]
write_csv(os.path.join(R3, "_work", "T8B_VERDICTS.csv"),
          ["SampleID", "ClaimKey", "CheckField", "CheckedValue", "Verdict", "ProposedValue", "Evidence"], out)
from collections import Counter
print(Counter(o["Verdict"] for o in out), len(out))
