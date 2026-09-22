"""T8C: build T8C_VERDICTS.csv from the sample file plus the hand-recorded verdicts below.
Checked values are copied from SPOT_S2S3.csv by script, never retyped."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from load import load
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_scripts'))
from r3lib import write_csv

APP = 'projects/chirality-app-dev'
RT = 'projects/chirality-runtime'
FE = APP + '/frontend'
C, R, U, D = 'CONFIRMED', 'REFUTED', 'UNVERIFIABLE', 'UNDECIDED'
HASH = 'R2/PKG-04/EVIDENCE_PACK/REFERENCE_HASHES.csv (PRD recorded 8649ccba MATCH, recomputed 17ca3f3c, Match=NO)'

# S3: SampleID -> (verdict, proposed, evidence)
S3 = {
 'S3-001': (C, '', f'{APP}/execution/PKG-04*/DEL-04-04*/ScopeOfWork.md:438 states "REF-006 is MATCH under D-APP-38" as present fact, no snapshot named; {HASH}; CONVENTIONS 2.6 tie-break rules 1 and 3'),
 'S3-002': (D, 'R4', f'Row turns on {APP}/docs/DIRECTIVE.md:320-330 (s.8 per-user daemon, D-GOV-20) versus D-GOV-43 A2. Reading A: s.8 is not among the clauses R4-Q6 names (s.2.8, 2.10, 4.1, 4.2, K-PERM-1/6), so plain R4. Reading B: RUN_BASIS Addendum 9 broadens R4-Q6 to the DIRECTIVE-versus-D-GOV-43 cluster, so R4; R4-Q6. Compare S2-010 (same A2 daemon issue, plain R4)'),
 'S3-003': (C, '', f'{FE}/src/__tests__/lib/tool-descriptor.test.ts:2 imports lib/harness/tool-pool and :552 exercises resolveHarnessToolPool; turn-engine.test.ts:5 imports lib/harness/turn-engine; both LEGACY_ONLY in R2/_shared/EVIDENCE_PACK/REACHABILITY.csv'),
 'S3-004': (C, '', f'VER-001 is a migration-process check with no record in the folder (UNKNOWN by absence, Addendum 10); the mechanism is a missing record, not an open gate. Same tag as sibling rows DEL-00-01#CLM-018.2, DEL-00-02#CLM-021.2, DEL-10-01#CLM-022.2. LIFECYCLE_GATE_PENDING is a weaker fit'),
 'S3-005': (C, '', f'{APP}/execution/PKG-02*/DEL-02-01*/ScopeOfWork.md:380 "PORTAL shows 3 rows and 4 columns"; live {FE}/src/components/portal/agent-matrix.tsx:9-61 renders a role list (rendered via components/shell/tertiary-sidebar-tabs.tsx:13). D-APP-108 ruling record has no clause permitting matrix removal, so ACCEPTED_DIVERGENCE has no governing basis'),
 'S3-006': (C, '', f'Matrix retired by the v3 four-role adoption (9b005c23a), not by a register ruling; that is R4-Q4 (CONVENTIONS 2.4). agent-matrix.tsx:37 "Retained export name keeps legacy Portal routes"'),
 'S3-007': (C, '', f'R2/SURFACES/RTCONTRACT_capabilities.csv CAP-RTCONTRACT-040: domain-profile.ts "REACH=TEST_ONLY (pack LIVE only via contracts barrel; no non-test consumer)"; grep of {RT}/packages and {FE}/src finds its symbols only in __tests__ files (legacy registry does not import it). PACK_MANIFEST.md limit 1 lets capability files refine barrel reach'),
 'S3-008': (C, '', f'Consistent with ALIGNED. Read-only git check: 233 of 234 non-blank lines of the four legacy documents at e9b9e302c^ appear verbatim in the frozen ScopeOfWork.md; the one exception (DEL-05-03-R14) is a later governed amendment (ScopeOfWork.md:163, D-APP-68 ruling 7). Script T8C_scripts/parity.py. The row IE "NONE_FOUND" understates this'),
 'S3-009': (C, '', f'{APP}/execution/PKG-04*/DEL-04-01*/ScopeOfWork.md:210 and :224 state REF-006 hash status MATCH "reconciled under D-APP-38" as current, no snapshot; a verification-table note, not a Remaining item; R2/PKG-04/EVIDENCE_PACK/REFERENCE_HASHES.csv DEL-04-01,PRD Match=NO; tie-break rule 1'),
 'S3-010': (C, '', f'REQ-002/007/013 cite K-ENGINE-4 and SPEC s.10.3 ({APP}/execution/PKG-03*/DEL-03-01*/ScopeOfWork.md:146,151,157), the unamended side of R4-Q5; live {RT}/packages/core/src/delegated-engine-adapter.ts:282-289 carries Codex payloads as received. REQ-002 also cites DIRECTIVE s.2.8/2.10, so R4-Q6 could be added'),
 'S3-011': (C, '', f'sdk-message-mapper.ts, chirality-hooks.ts, session-events.ts, tool-result-artifacts.ts are LEGACY_ONLY in R2/_shared/EVIDENCE_PACK/REACHABILITY.csv; the added text only names the tested modules'),
 'S3-012': (C, '', 'CauseTag NONE is required on ALIGNED rows (CONVENTIONS 2.3); ALIGNED is supported by the git parity check noted at S3-008'),
 'S3-013': (C, '', f'ScopeOfWork.md:382 column labels GUIDING/APPLYING/JUDGING/REVIEWING; live agent-matrix.tsx:9-35 shows no columns; the only live GUIDING is a default query value at {FE}/src/components/workbench/workbench-surface.tsx:178. Labels absent, so DOCUMENTED_UNIMPLEMENTED; no governing ruling permits it'),
 'S3-014': (C, '', f'Row cites CONTRACT K-PERM-1 ({APP}/docs/CONTRACT.md:90, names ChiralityPermissionOverlay, unamended), which R4-Q6 names; live permission path is Codex approval relay {RT}/packages/daemon/src/codex-supervisor.ts:700-727'),
 'S3-015': (C, '', 'Same basis as S3-007 (CAP-RTCONTRACT-040 symbol-level TEST_ONLY)'),
 'S3-016': (C, '', f'CONVENTIONS 2.7: a REGISTER row takes STALE_SPECIFICATION when the register asserts a now-false fact; R2/PKG-08/EVIDENCE_PACK/REFERENCE_HASHES.csv DEL-08-04,CONTRACT recorded fa8fc9dc MATCH, recomputed 57411f8d, Match=NO'),
 'S3-017': (C, '', f'Settings isolation (DIRECTIVE s.4.2 "load ambient user/global Claude Code settings", K-SDK-1) versus live shared Codex home {RT}/packages/daemon/src/codex-app-server-client.ts:51-57; R4-Q6 names the unfiltered ~/.codex link. Plain R4 has no separate unframed question'),
 'S3-018': (C, '', f'{FE}/src/lib/harness/session-manager.ts: LIVE routes (app/api/working-root/*/route.ts:3) import only assertProjectRootAccessible; FileSessionManager (:632) is constructed only at lib/harness/runtime.ts:158 (LEGACY_ONLY). R2/SURFACES/HARNESS_capabilities.csv CAP-HARNESS-037 records the same symbol-level split'),
 'S3-019': (C, '', 'CauseTag NONE is invalid on an UNKNOWN row (CONVENTIONS 2.3); missing parity record in the folder is a record defect (DOC_HYGIENE). The cited parity record lies in Root execution/, outside the evidence roots'),
 'S3-020': (C, '', f'RB-PERMISSION restates K-PERM-1 ({APP}/docs/CONTRACT.md:90, unamended, overlay and hard-deny precedence). D-GOV-43 leaves approval and sandbox policy to the user without naming K-PERM-1; live {RT}/packages/contracts/src/delegated.ts:322-330 maps bypass to danger-full-access. Ruling undercuts an unamended clause: AUTHORITY_CONFLICT (CONVENTIONS 1); matches S2-001 on the same register'),
 'S3-021': (C, '', f'Row cites DIRECTIVE s.2.8 ({APP}/docs/DIRECTIVE.md:115-136, Claude key-aware default and Chirality-owned permission policy), which R4-Q6 names; live engine Codex {RT}/packages/daemon/src/app-owned-composition.ts:17-20'),
 'S3-022': (C, '', f'R2/SURFACES/BUILD_capabilities.csv CAP-BUILD-024 tags validate-release-quality-evidence.mjs REACH=TEST_ONLY (CI validation harness); scripts are not product entry points (R2/_shared/EVIDENCE_PACK/PACK_MANIFEST.md Item 2 limit 3); invoked by {FE}/package.json:29'),
 'S3-023': (C, '', 'VER-001 asserts a process (validation, mapping, parity report, checklist, human review) happened; the only evidence is absence of records in the evidence roots, so UNKNOWN, not DOCUMENTED_UNIMPLEMENTED (CONVENTIONS 2.6, Addendum 10)'),
 'S3-024': (C, '', f'DEL-05-01-R010 (ScopeOfWork.md:227, D-APP-73) is met in full only by LEGACY {FE}/src/lib/harness/session-manager.ts:563-621; live {RT}/packages/core/src/session-store.ts:937-981 differs. That is R4-Q1 by rule 3. The live gap is a repair item under a governing ruling, not an unframed owner question, so plain R4 adds nothing'),
 'S3-025': (C, '', f'{FE}/src/lib/lifecycle/transition.ts:32-38 error codes have no policy/path denial; {FE}/src/lib/harness/mcp/read-tools.ts:925-945 statusTransitionTool wraps it in runMutatingMcpToolWithEvidence; read-tools.ts LEGACY_ONLY in REACHABILITY.csv. Function starts at :925 (the :934 anchor is inside it)'),
 'S3-026': (C, '', 'CauseTag NONE is invalid on an IMPLEMENTED_DIFFERENTLY row. The coordination class and managed-delegation validation are the Type 2 bridge; the live path uses Codex-native descendants: NATIVE_DELEGATION (CONVENTIONS 4). CODEX_SOLE_ENGINE is the weaker alternative'),
 'S3-027': (C, '', 'Deterministic validation has a positive record (TASK_RUN_2026-07-19 :21); the other parts (claim map, parity, checklist, human review) rest only on absent records. A PARTIALLY_IMPLEMENTED verdict would rest on that absence, so UNKNOWN (Addendum 10). Other reading: PARTIALLY_IMPLEMENTED from the positive part'),
 'S3-028': (C, '', f'Row cites DIRECTIVE s.4.2 (bash out of scope before gates), which R4-Q6 names; live {RT}/packages/contracts/src/delegated.ts:322-330 and composer "Full access" ({FE}/src/components/shell/chat-panel.tsx:133), the R4-Q6 Full access option'),
 'S3-029': (C, '', 'Same basis as S3-007 (CAP-RTCONTRACT-040: domain-profile.ts symbol-level TEST_ONLY)'),
 'S3-030': (C, '', f'{APP}/execution/PKG-04*/DEL-04-04*/ScopeOfWork.md:262 "REF-006 docs/PRD.md is MATCH under D-APP-38 ... describe current source state"; {HASH}; tie-break rules 1 and 3'),
}

MIG = 'VER-001 asserts a SoW-migration process (validation, claim map, parity report, checklist, human review) took place; only absence of records within the roots, so UNKNOWN (CONVENTIONS 2.6, Addendum 10); OWNER_CHECK belongs in Notes, not HumanDecisionNeeded'
HDN_NO = 'No governing conflict and no legacy-only code evidence; NO is right'
Q6DIR = f'{APP}/docs/DIRECTIVE.md:115-136 s.2.8 (Claude/Anthropic key-aware default, unamended) versus amended K-ENGINE-3 ({APP}/docs/CONTRACT.md:63, Codex sole engine) and D-GOV-43'
EVT = f'{APP}/docs/SPEC.md:693-712 s.11 and {APP}/docs/TYPES.md s.7.4 are both "Revised under D-GOV-43 (A2)" and keep the eight UIEvent names "as compatibility history"'

# S2: SampleID -> ((disp verdict, proposed, evidence), (hdn verdict, proposed, evidence))
S2 = {
 'S2-001': ((C, '', f'RB-PERMISSION restates K-PERM-1 ({APP}/docs/CONTRACT.md:90, unamended); D-GOV-43 leaves approval/sandbox policy to the user without naming it; live {RT}/packages/contracts/src/delegated.ts:322-330'),
            (C, '', 'R4-Q6 names K-PERM-1; Chirality-owned deny-first enforcement exists only in LEGACY permission-overlay.ts/permission-broker.ts (REACHABILITY.csv), so R4-Q1 by rule 3')),
 'S2-002': ((C, '', 'Packaged S-6/S-8 are manual owner checks; the record shows S-1..S-8 on the source-run App only. Absence of a packaged record never refutes UNKNOWN (Addendum 10)'), (C, '', HDN_NO)),
 'S2-003': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-004': ((C, '', f'_CONTEXT assertion restates {Q6DIR}; which text binds is the R4-Q6 question, not the worker\'s'),
            (C, '', 'R4-Q6 names DIRECTIVE s.2.8; the Claude path is met only by LEGACY claude-agent-sdk-manager.ts and engine-claude (REACHABILITY.csv), so R4-Q1')),
 'S2-005': ((C, '', MIG + '; validate_scope_of_work PASS covers one part only'), (C, '', HDN_NO)),
 'S2-006': ((C, '', f'R01 is met by LIVE {FE}/electron/api-key-ipc.ts:185 and api-key-storage.ts:50,75; whether the Anthropic key path still binds under D-GOV-43 (Codex custodies credentials) is the question R4-Q6 frames ("Anthropic API-key UI")'), (C, '', 'R4-Q6 covers the Anthropic API-key UI; live code meets the claim, so no R4-Q1')),
 'S2-007': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-008': ((C, '', f'SPEC s.10.3 and DIRECTIVE s.2.10 (unamended) versus amended K-EVENT-1/6 and SPEC s.11; live {RT}/packages/core/src/delegated-engine-adapter.ts:282-289 passes codex.notification method and params through'), (C, '', 'R4-Q5 (payloads as received versus translated) and R4-Q6 (DIRECTIVE s.2.10); live code partly meets, so no R4-Q1')),
 'S2-009': ((C, '', Q6DIR), (R, 'R4-Q1; R4-Q6', f'The row turns on App DIRECTIVE s.2.8 versus D-GOV-43, the first clause R4-Q6 names (CONVENTIONS 2.4; RUN_BASIS Addendum 9 lists PKG-04 DEL-04-05). R4-Q1 is right: Claude SDK code is LEGACY_ONLY')),
 'S2-010': ((C, '', f'_CONTEXT restates the governing decomposition (daemon-centralized sessions, Root-owned); D-GOV-43 supersedes D-GOV-20 items 2-4 (docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/RULING_CANDIDATE.md:67) without naming the decomposition row; live store under App userData {FE}/electron/runtime-service-host.ts:75'), (C, '', 'No named question covers daemon topology versus the decomposition; plain R4. See S3-002 for the R4-Q6 reading of the same cluster')),
 'S2-011': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-012': ((C, '', f'K-HOOK-1 / SPEC s.15.2 unamended versus D-GOV-43 (no Chirality hooks on live path, {RT}/packages/daemon/src/codex-supervisor.ts:729-735)'), (C, '', 'R4-Q1 names K-HOOK and SPEC s.15.2; fail-closed hooks only in LEGACY chirality-hooks.ts:589-603')),
 'S2-013': ((C, '', f'K-ROOT-2 unamended versus D-GOV-43 user-chosen policy; live sandbox {RT}/packages/daemon/src/codex-supervisor.ts:104-110 and delegated.ts:318-326'),
            (R, 'R4-Q1; R4-Q6', f'In workspaceWrite the live sandbox (writableRoots=[cwd]) and project-registry.ts:100-121 keep the instruction root unwritten; the row diverges only through the composer "Full access" option (danger-full-access, {FE}/src/components/shell/chat-panel.tsx:133), which R4-Q6 names. R4-Q1 (K-ROOT) stays')),
 'S2-014': ((C, '', f'SoW REQ-002 cites TYPES s.10 for lowercase statuses, but {APP}/docs/TYPES.md:537 (changed c9734a6ee, 2026-07-11, no ruling cited) defines LAUNCHED|RUNNING|COMPLETED|FAILED|BLOCKED, while D-APP-56 R5 P45 UPD-138 records the lowercase implemented contract; two governing sources disagree and the authority order does not rank a ruling record against TYPES. MEDIUM confidence: the other reading is STALE_SPECIFICATION against current TYPES s.10'),
            (C, '', 'Plain R4 (no named question) plus R4-Q1: only LEGACY agent-runtime-contract.ts:27-33 meets it')),
 'S2-015': ((C, '', 'K-PERM-1..5 unamended versus D-GOV-43 user policy; live emits tool.permission deny events ({RT}/packages/core/src/delegated-engine-adapter.ts:309-310) but Chirality deny precedence is legacy'), (C, '', 'R4-Q6 (K-PERM-1); R4-Q1 because Chirality-owned denial is met only in LEGACY permission-overlay.ts:112. Live deny events meet part of the claim, so R4-Q1 is arguable')),
 'S2-016': ((C, '', 'A binary-architecture inspection is a manual step; the only evidence is no lipo/file record, so UNKNOWN (Addendum 10); package.json:159-165 targets arm64'), (C, '', HDN_NO)),
 'S2-017': ((C, '', f'D-APP-50/D-APP-53 (ruled) authorize a proposal-transport tranche on the in-process MCP lane; D-GOV-43 removes that lane from the live path (Codex supervisor refuses dynamic tools, {RT}/tests/codex-supervisor.test.ts:123) and D-APP-127 does not name D-APP-50/53 among superseded decisions ({APP}/execution/_Coordination/_DECISIONS/_REGISTER.md:152)'), (C, '', 'R4-Q1: host modules domain-proposal-tools.ts / domain-profile-registry.ts are LEGACY_ONLY')),
 'S2-018': ((C, '', MIG + '; parity markers existed in 9ccbbea99 (positive for mapping only), human review unrecorded'), (C, '', HDN_NO)),
 'S2-019': ((C, '', f'RB-SETTINGS restates K-SDK-1 / DIRECTIVE s.4.2 settings isolation; live composes the user\'s shared Codex home (D-GOV-43) without naming those clauses'), (C, '', 'R4-Q6 (unfiltered ~/.codex link); R4-Q1: settingSources [] only in LEGACY sdk-options-builder.ts')),
 'S2-020': ((C, '', MIG + '; same row as S3-027'), (C, '', HDN_NO)),
 'S2-021': ((C, '', f'K-SDK-1, K-PERM-6, DIRECTIVE s.4.2 (unamended) versus live "Full access" = danger-full-access {FE}/src/components/shell/chat-panel.tsx:133'), (C, '', 'R4-Q6 names K-PERM-6 and the Full access option; R4-Q1: guarded bypass only in LEGACY sdk-options-builder.ts')),
 'S2-022': ((C, '', f'Records table is checkable and holds (seven artifacts present in the DEL-01-01 folder; run records exist); VER-001 (ScopeOfWork.md:295) is a process claim with no record, so UNKNOWN (Addendum 10)'), (C, '', HDN_NO)),
 'S2-023': ((C, '', 'Same basis as S2-006: met by LIVE electron/api-key-ipc.ts and api-key-storage.ts; binding of the Anthropic key path is R4-Q6'), (C, '', 'R4-Q6 (Anthropic API-key UI)')),
 'S2-024': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-025': ((C, '', 'DIRECTIVE s.2.10 and SPEC s.10.3 (unamended) versus amended K-EVENT-1/6, SPEC s.11; live adapter passes upstream names through'), (C, '', 'R4-Q5 and R4-Q6 (s.2.10)')),
 'S2-026': ((C, '', f'DIRECTIVE s.2.8 and K-ENGINE-1..5 read against D-GOV-43 (Codex custodies credentials; upstream notifications preserved)'), (C, '', 'R4-Q5 (event semantics) and R4-Q6 (s.2.8)')),
 'S2-027': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-028': ((C, '', f'K-PERM-4/5/6 and SPEC s.15.1 (unamended) versus live mode mapping {RT}/packages/contracts/src/delegated.ts:320-330 (bypass = danger-full-access, no deny hooks)'),
            (R, 'R4-Q1; R4-Q6', f'The row cites K-PERM-6 and its divergence is the live Full access mapping; R4-Q6 names both (CONVENTIONS 2.4). Same deliverable row DEL-06-05#CLM-004.2 carries R4-Q1; R4-Q6 (S3-028)')),
 'S2-029': ((C, '', 'K-HOOK-1 unamended versus D-GOV-43; no Chirality hooks on the live path'), (C, '', 'R4-Q1 (K-HOOK); fail-closed only in LEGACY chirality-hooks.ts:589-600')),
 'S2-030': ((C, '', 'Same basis as S2-014: D-APP-56 R5 P45 UPD-138 contractVersion string versus TYPES s.10 schema v2 record; legacy code numeric 1'), (C, '', 'Plain R4 plus R4-Q1 (only LEGACY agent-runtime-contract.ts)')),
 'S2-031': ((D, 'STALE_SPECIFICATION', f'Reading A: {APP}/docs/CONTRACT.md:17 (preamble, D-GOV-43) names K-RELEASE-1 ("read with D-GOV-43 items 1 and 4") and states "bundle signing and notarization" apply, so the governing text resolves the point and the SoW "unsigned/adhoc posture acceptable" is stale. Reading B: K-RELEASE-1 table text (CONTRACT.md:138, "unsigned/unnotarized unless amended") is unchanged and "read with" states no outcome, so AUTHORITY_CONFLICT'),
            (D, 'NO', 'Follows the Disposition: NO (or D-GOV-43) under reading A; R4 under reading B')),
 'S2-032': ((C, '', 'AC-001 asks for CI-step and manual-item status (off-code events); only a folder search with no result, so UNKNOWN (Addendum 10)'), (C, '', HDN_NO)),
 'S2-033': ((C, '', f'D-APP-49..52 (ruled) staged-live surface versus D-GOV-43 without naming them; the named tools are reachable only through LEGACY {FE}/src/lib/harness/mcp/*. Other reading: "are live" is a now-false present fact, STALE_SPECIFICATION'), (C, '', 'R4-Q1: only LEGACY code meets the claim')),
 'S2-034': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-035': ((C, '', 'Same basis as S2-019 (RB-SETTINGS boundary row)'), (C, '', 'R4-Q6; R4-Q1 as S2-019')),
 'S2-036': ((C, '', f'DIRECTIVE s.4.2 excludes remote MCP/plugins/marketplace; live {RT}/packages/daemon/src/codex-effective-home.ts:41-89 links the user\'s ~/.codex plugins and MCP definitions under D-GOV-43'), (C, '', 'R4-Q6 names the unfiltered ~/.codex link and s.4.2')),
 'S2-037': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-038': ((R, 'ALIGNED', f'{EVT}, so no unamended text conflicts and the authority is not in doubt. The claim "existing browser-facing event names remain compatible" holds on the live path: {FE}/src/components/shell/chat-panel.tsx:1016-1037 handles chat:complete, turn:error, process:exit. ALSO: STALE_SPECIFICATION if "existing names" is read as the current contract'),
            (R, 'NO', 'R4-Q5 concerns stored payloads under unamended K-ENGINE-4 / SPEC s.10.3, which this row does not cite; no owner question remains')),
 'S2-039': ((C, '', MIG + '; same row as S3-004'), (C, '', HDN_NO)),
 'S2-040': ((C, '', 'DIRECTIVE s.2.10 and K-ENGINE-4 (unamended) versus amended K-EVENT-1/6; live adapter preserves upstream payloads'), (C, '', 'R4-Q5; R4-Q6 (s.2.10)')),
 'S2-041': ((C, '', Q6DIR + '; SDK 0.3.150 consumed only by LEGACY claude-agent-sdk-manager.ts:80'), (C, '', 'R4-Q1 (legacy only) and R4-Q6 (s.2.8)')),
 'S2-042': ((C, '', f'Governing decomposition scope for the in-process MCP read slice versus D-GOV-43; live runtime-service.ts:580 records mcpServers: []'), (C, '', 'R4-Q1: read-tools.ts LEGACY_ONLY')),
 'S2-043': ((C, '', 'PRD FR-051 / TYPES s.8.2 instruction-root write block versus D-GOV-43 user policy'),
            (R, 'R4-Q1; R4-Q6', f'"Blocked even when a permissive mode would allow" turns directly on the live Full access option (danger-full-access, {RT}/packages/contracts/src/delegated.ts:318-326; {FE}/src/components/shell/chat-panel.tsx:133), which R4-Q6 names')),
 'S2-044': ((C, '', 'Same basis as S2-014 (TYPES s.10 versus D-APP-40/D-APP-56 field set)'), (C, '', 'Plain R4 plus R4-Q1 (LEGACY agent-runtime-contract.ts:71-85 only)')),
 'S2-045': ((C, '', 'K-HOOK-1, K-PATH-2/3, SPEC s.15.2 unamended versus D-GOV-43'), (C, '', 'R4-Q1 names K-PATH, K-HOOK, SPEC s.15.2; checks target LEGACY tool-path-policy.ts, chirality-hooks.ts')),
 'S2-046': ((C, '', 'Mapping evidence "before readiness is claimed" concerns a release review step (off-code); absence only, so UNKNOWN'), (C, '', HDN_NO)),
 'S2-047': ((D, '', 'Not settled in budget. Reading A: D-APP-56 R4-P27 assigns pec.yaml ownership to DEL-10-04 while PEC-loop commits b1074e7a4/ca49b846d author it under D-APP-70 mapping, a governing disagreement (AUTHORITY_CONFLICT). Reading B: ownership text is a deliverable-level record gone stale (STALE_SPECIFICATION). D-APP-70 ruling record not read'),
            (C, '', 'R4-Q1 is supported by evidence: pec registry entry only in LEGACY domain-profile-registry.ts:85-114')),
 'S2-048': ((C, '', MIG + '; the cited 30/30 parity record is in Root execution/, outside the evidence roots'), (C, '', HDN_NO)),
 'S2-049': ((C, '', 'Same row as S3-020'), (C, '', 'Same basis as S2-001')),
 'S2-050': ((C, '', Q6DIR + '; BOUNDARY_REVIEW_CHECKLISTS.md:25'), (C, '', 'R4-Q6 (s.2.8); R4-Q1: Anthropic default only in LEGACY anthropic-agent-sdk-manager.ts')),
 'S2-051': ((C, '', MIG + '; _STATUS approval SHA predates the migration'), (C, '', HDN_NO)),
 'S2-052': ((R, 'ALIGNED', f'{EVT}. turn:error and process:exit are still produced and consumed on the live path: {RT}/packages/core/src/turn-coordinator.ts:249-253; {FE}/src/components/shell/chat-panel.tsx:1022,1037. No unamended governing text conflicts'),
            (R, 'NO', 'Row cites only SPEC s.11 and TYPES s.7.4, both amended; R4-Q5 turns on unamended K-ENGINE-4 / SPEC s.10.3')),
 'S2-053': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-054': ((C, '', 'SPEC s.10.3 and K-ENGINE-4 (unamended) versus amended K-EVENT-1 / SPEC s.11; live codex.notification carries upstream method and params (delegated-engine-adapter.ts:282,289)'), (C, '', 'R4-Q5 exactly')),
 'S2-055': ((C, '', 'K-HOOK-1 / SPEC s.15.2 unamended versus D-GOV-43; no hooks on live path'), (C, '', 'R4-Q1 (K-HOOK)')),
 'S2-056': ((C, '', 'K-PATH-2 unamended versus D-GOV-43 user policy'), (C, '', 'R4-Q1 names K-PATH. The Full access mapping in the IE could also bring R4-Q6, but the path divergence (Codex reads outside the root in any mode) does not rest on it alone')),
 'S2-057': ((C, '', 'K-PERM-1..4 unamended versus D-GOV-43 user policy (PRD FR-027 at docs/PRD.md:632)'), (C, '', 'R4-Q6 (K-PERM-1); R4-Q1: hard-deny precedence only in LEGACY permission-overlay.ts')),
 'S2-058': ((C, '', 'A ten-step CI review is a manual review record; absence only, so UNKNOWN'), (C, '', HDN_NO)),
 'S2-059': ((D, '', 'Reading A: K-DOMAIN-2 hook enforcement exists only in legacy while D-GOV-43 removed Chirality hooks, AUTHORITY_CONFLICT. Reading B: the text is a trade-off for a future implementation; the live path exposes no domain operations, so nothing diverges today (ALIGNED or DOCUMENTED_UNIMPLEMENTED for the future item)'),
            (C, '', 'R4-Q1 by evidence: only LEGACY chirality-hooks.ts meets it')),
 'S2-060': ((C, '', 'Row names the conflict itself: K-ENGINE-4 unamended versus amended K-EVENT-1/K-EVENT-6'), (C, '', 'R4-Q5 exactly')),
 'S2-061': ((C, '', 'Same basis as S2-036 (K-NET-1 / DIRECTIVE s.4.2 versus shared ~/.codex plugins and MCP)'), (C, '', 'R4-Q6')),
 'S2-062': ((C, '', 'A copy-review method and review evidence are human steps; no completed template found, absence only, so UNKNOWN'), (C, '', HDN_NO)),
 'S2-063': ((C, '', 'Met by LIVE api-key-settings.tsx:237 and api-key-storage.ts:79; binding of the Anthropic key UI is R4-Q6 (as S2-006)'), (C, '', 'R4-Q6')),
 'S2-064': ((C, '', MIG), (C, '', HDN_NO)),
 'S2-065': ((C, '', 'DIRECTIVE s.2.10, SPEC s.10.3 unamended versus amended event texts'), (C, '', 'R4-Q5; R4-Q6')),
}

rows = []
for r in load():
    sid = r['SampleID']
    if sid.startswith('S3') and sid in S3:
        v, p, e = S3[sid]
        rows.append(dict(SampleID=sid, ClaimKey=r['ClaimKey'], CheckField=r['CheckField'],
                         CheckedValue=r['RemappedValue'], Verdict=v, ProposedValue=p, Evidence=e))
    elif sid in S2:
        (dv, dp, de), (hv, hp, he) = S2[sid]
        rows.append(dict(SampleID=sid, ClaimKey=r['ClaimKey'], CheckField='Disposition',
                         CheckedValue=r['Disposition'], Verdict=dv, ProposedValue=dp, Evidence=de))
        rows.append(dict(SampleID=sid, ClaimKey=r['ClaimKey'], CheckField='HumanDecisionNeeded',
                         CheckedValue=r['HumanDecisionNeeded'], Verdict=hv, ProposedValue=hp, Evidence=he))
missing = [k for k in list(S3) + list(S2) if k not in {x['SampleID'] for x in rows}]
assert not missing, missing
for x in rows:
    assert '/Users/' not in x['Evidence'] and '/private/' not in x['Evidence']
out = os.path.join(os.path.dirname(__file__), '..', 'T8C_VERDICTS.csv')
write_csv(out, ['SampleID', 'ClaimKey', 'CheckField', 'CheckedValue', 'Verdict', 'ProposedValue', 'Evidence'], rows)
from collections import Counter
print(len(rows), Counter((x['SampleID'][:2], x['CheckField'] if x['SampleID'].startswith('S2') else 'S3', x['Verdict']) for x in rows))
