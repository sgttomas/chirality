# SCA-APP-009 / SCA-APP-010 Mechanical Comparison

Date: 2026-09-22
Purpose: compare accepted SCA action, manifest, supersession, handoff, and current decomposition records against current App files. This note records mechanical counts and exact byte identities; it gives no SCA closure, acceptance, or release verdict.

## Execution record

This was a delegated Type 2 TASK under parent /root, using the collaboration child-task mechanism; no further delegation occurred. Engine: Codex. Model/effort: gpt-6-luna / xhigh. Provider label was not exposed in the task handoff.

Supplied basis: the parent task naming SCA-APP-009 and SCA-APP-010, the two expected current file hashes, the output/write boundary, and the requirement to run APP-HOLD-1. Instructions read: repository AGENTS.md SHA-256 1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57; agents/AGENT_TASK.md 1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7; App AGENTS.md abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f; chirality-change skill at .agents/skills/chirality-change/SKILL.md 2b490e172436417896c1cd25dbcd543c676e3473aa58b7663985d75785ff7dba. The skill informed evidence and Git-scope hygiene; no Git operation was performed.

Observed repository HEAD for the final full preflight: 0fb42b36df5c93c34c02e209670f3cede937ce84. The current decomposition, companion register, DEL-02-05 ScopeOfWork.md, and DEL-04-01 ScopeOfWork.md were already modified in the worktree. I read them as assigned inputs and did not edit them. The only output of this task is this evidence file. No result from a prior temporary scanner was used.

## APP-HOLD-1 preflight

I enumerated directories matching projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-* and extracted unique DEL-NN-NN identifiers. There are 54 physical folders and 54 unique IDs. The 16 direct SCA deliverable targets are a subset of those 54.

From the App working root, the final command was:

python3 execution/_Scripts/app_hold.py check --operation reliance --entry-path execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md --target DEL-00-01 --target DEL-00-02 --target DEL-01-01 --target DEL-01-02 --target DEL-01-03 --target DEL-01-04 --target DEL-02-01 --target DEL-02-02 --target DEL-02-03 --target DEL-02-04 --target DEL-02-05 --target DEL-03-01 --target DEL-03-02 --target DEL-03-03 --target DEL-03-04 --target DEL-04-01 --target DEL-04-02 --target DEL-04-03 --target DEL-04-04 --target DEL-04-05 --target DEL-05-01 --target DEL-05-02 --target DEL-05-03 --target DEL-05-04 --target DEL-05-05 --target DEL-06-01 --target DEL-06-02 --target DEL-06-03 --target DEL-06-04 --target DEL-06-05 --target DEL-06-06 --target DEL-07-01 --target DEL-07-02 --target DEL-07-03 --target DEL-07-04 --target DEL-07-05 --target DEL-07-06 --target DEL-08-01 --target DEL-08-02 --target DEL-08-03 --target DEL-08-04 --target DEL-08-05 --target DEL-09-01 --target DEL-09-02 --target DEL-09-03 --target DEL-09-04 --target DEL-09-05 --target DEL-09-06 --target DEL-09-07 --target DEL-10-01 --target DEL-10-02 --target DEL-10-03 --target DEL-10-04 --target DEL-10-05

Observed exit 0, empty stderr, top-level ALLOW, and 54 result rows all CLEAR / NOT_HELD / ALLOW. active_hold_deliverables, scan_held_deliverables, and structural_bootstrap_deliverables were all empty. The output reports repo_head 0fb42b36df5c93c34c02e209670f3cede937ce84, register SHA-256 d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c, and scan fingerprint e4197287316e62db84950ccbc46de95bcd9866afb36894023b400e0fe4fa7be1. The checker source hash was 92e6dd4c001e8715450e61f91073b49da6788de41f43606c812457c02e07c5bc3.

Physical inventory comparison: 52 current decomposition deliverable IDs all have physical folders; two physical closure units are outside the decomposition inventory: DEL-00-01 and DEL-00-02. The direct affected set is DEL-02-01, DEL-02-02, DEL-02-04, DEL-02-05, DEL-03-02, DEL-04-01, DEL-04-04, DEL-05-01, DEL-05-02, DEL-06-03, DEL-07-01, DEL-07-03, DEL-08-01, DEL-08-03, DEL-08-04, and DEL-09-07. All 16 also appear in the current decomposition and physical directory census.

## Accepted SCA package counts and row parity

| Record | Amendment action rows | DELIVERABLE rows | Supersession delta / binding-YES rows | Cumulative map rows | Manifest entries matching |
|---|---:|---:|---:|---:|---:|
| SCA-APP-009 | 16 | 4 | 4 / 4 | 34 | 41 / 41 |
| SCA-APP-010 | 30 | 13 | 11 / 11 | 45 | 59 / 59 |
| SCA-APP-010 DEL-02-05 propagation addendum | — | 1 carrier | — | — | 13 / 13 |

For SCA-APP-009, the four delta decisions D-001, D-003, D-005, and D-007 are all present as full rows in the 34-row cumulative map. For SCA-APP-010, all 11 delta rows (D-015, D-002 through D-006, D-009 through D-012, and D-017) are present in the 45-row map. Each delta count equals the corresponding action-ledger SupersessionBindingPresent=YES count. The four and 13 direct deliverable action IDs were all found in the current decomposition; none were absent from the 54-folder census.

The SCA-APP-010 stage artifact PARSED_ACTIONS.csv has 29 rows, while final Amendment_Actions.csv has 30. At sequence 29, the parser-stage entity is OI-008 and the final ledger entity is COVERAGE-TELEMETRY; final sequence 30 adds the DEL-08-03 retired-presentation note, absent from PARSED_ACTIONS.csv. The current decomposition contains both OI-008 and DEL-08-03. This is an observed difference between a parser-stage artifact and the final action ledger; it is not treated here as a failed manifest or an omitted current identifier.

Key package identities:
- SCA-APP-009: MANIFEST.sha256 file  ffcfa82baf3b9c7f915641033af585d4d7f2261b1f9f5472bb4b3d647c6d74ea; Amendment_Actions.csv 46273d39b991551326688fac9d5f4f8381b181503bdf38aced4a94d46223c2b6; Supersession_Delta.csv 7c3b1899825ac3a208c6e0ca8fc5afacafdd02e1355ed8393bab042b949d9233; Supersession_Map.csv 5f7f0176ac161ac14f1f4e70f02e7810df211a24ad0dbf4b240b17efbce3403b.
- SCA-APP-010: MANIFEST.sha256 file 2ccd2b29da4e9fae79af83730f6917237f03075e147584f8f8196a8ca8d298a6; Amendment_Actions.csv 8b579266d3a4f7b73c093467691f2f9d7fe140bf8a0cb6f5d7c6c1ac2ef0a109; PARSED_ACTIONS.csv f39f9f75d0cbab0f883c6811a895bae9c6e0dc0af5b541f84ea12002f973ecc0; Supersession_Delta.csv c610f49478e314aeda673ec67befcc3369a50d559f98a18ddf5484a9b8449562; Supersession_Map.csv 2045684e8d2d1aff5a46663016f07c16f0c60462c8c8d729ea3c3c1a64f8dbb6.
- DEL-02-05 propagation addendum: MANIFEST.sha256 file 694baaa9b7f102e855df1e428ea5b729b0d5749c15e38515706371ee49bf907f.

## Current decomposition and derivative bytes

The current SOFTWARE decomposition SHA-256 is 9261ce30f933a0b72364a5af09c8aeed9208372774959864ff24a805126ea8a6 (136,687 bytes), matching the supplied current identity. The companion register is 918e475a48899d18755139027e61db200d23a531e48ed9f969c526dd842fa944 (99,496 bytes), also matching the supplied current identity.

Current declared/observed counts agree: 84 unique SOW IDs (SOW-001 through SOW-084), 10 package IDs, 52 deliverable rows, 10 objective IDs, and context-envelope counts S=9 / M=41 / L=2 / XL=0. Parsing the 52 deliverable rows independently produced the same envelope census. The 52 rows include retired DEL-09-07, classified M; excluding that retired row leaves 51 active deliverables and an active-row size census of S=9 / M=40 / L=2 / XL=0. SOW-080 is retained as OUT. The current note explicitly says these retained IDs remain in counts and DEL-09-07 has no selectable work.

The two current hashes differ from the earlier SCA Gate-5 pins. SCA-APP-009 Handoff_State.md records decomposition e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97 and register e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70. SCA-APP-010 Handoff_State.md records decomposition c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61 and register 63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca. Current derivatives are the 2026-09-22 worktree bytes above. The decomposition records the later D-GOV-43 item 11 / D-APP-127 application, and D-APP-108 Q15/Q16 wording remains in SOW-081. D-APP-131 applies the current R5/R6 carrier reconciliation. D-APP-131 P-18 says not to automatically re-pin merely because a carrier lagged.

The register still has 83 data rows and the same 83 invariant IDs as HEAD. Exactly three rows changed current application annotations: K-CONTROL-1, K-STORE-2, and K-VALIDATE-1; changed fields are AppDeliverableIDs, EnforcementSurfaces, ValidationSurfaces, RationaleEvidenceAnchor, and AppDecompositionBasis. All 83 candidate-sha256 references remain at the original SCA-APP-010 identity c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61. Per D-APP-131 P-18 and the existing retirement backcheck, this records preserved source identity; this note makes no repin recommendation.

The current DEL-02-05 ScopeOfWork.md is SHA-256 32f725b3c2892ce19fe43579cc5dad2a1f51f2cddc625db986f30cfdbf449c15 (27,939 bytes). The immutable SCA-APP-010 propagation addendum pins its earlier reviewed postimage at 0c40921347b4478d3d200daf4a766a5652239a2c9ab4b60ad0646017c5c70c29 (35,562 bytes). The current carrier contains D-APP-131 applicability text and is linked to the DEL-02-05 R5/R6 record (SHA-256 9aa09a764279861aa729afc3e23ea91fcccb3a50f417e9faf11989d9c8643c96). This is a later claim-repair application; the addendum remains historical and its handoff still says OPEN_APPLIED_AUDIT_PENDING.

The current DEL-04-01 ScopeOfWork.md includes SOW-079 and is mapped to it by the decomposition. Its current _STATUS.md remains IN_PROGRESS and carries a named SOW-079 observation/adoption-evidence item. The current DEL-09-07 ScopeOfWork.md remains present as history; its _STATUS.md says retired by D-APP-127 and no Remaining item. These match the later D-APP-127/D-APP-131 records; the earlier SCA-APP-009 pre-pointer handoff describes its earlier scaffold-only state.

## Handoff states and open consequences recorded

The current execution/_ScopeChange/_LATEST.md points to SCA-APP-010 and names the DEL-02-05 carrier addendum. SCA-APP-009 Handoff_State.md remains a dated Gate-5 pre-pointer handoff with OPEN_PENDING_DERIVATIVE_CLOSURE / ReadyForNextPhase NO. SCA-APP-010 Handoff_State.md records ACTIVE_OPEN_PENDING_DERIVATIVE_CLOSURE / ReadyForNextPhase NO; it says its own AUDIT_SCOPE_CLOSURE run was not dispatched and SCA-APP-009 derivative closure remains open. The carrier-propagation addendum says OPEN_APPLIED_AUDIT_PENDING and calls for an independent poststate audit. Thus the later pointer movement does not remove those recorded consequences.

A separate existing retirement backcheck is at projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/RETIREMENT_APPLICATION.md (current SHA-256 5feb56605d7f113ae09c0e064054d1ae94b126ff1c8a81004ac5054499cff363). It is referenced as existing parent-run evidence; none of its results are claimed as work performed by this TASK.

## Limits

This comparison checked exact file hashes, listed manifest entries, CSV row and ID counts, current table counters, current physical DEL folder IDs, and the APP-HOLD output. It did not perform semantic scope re-adjudication, product checks, delivery acceptance, or SCA closure review. No broader unsourced discrepancy was asserted from this bounded mechanical pass.
