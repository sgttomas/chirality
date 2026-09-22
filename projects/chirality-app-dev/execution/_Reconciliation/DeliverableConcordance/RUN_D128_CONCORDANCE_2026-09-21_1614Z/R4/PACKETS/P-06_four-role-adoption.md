<!-- PACKET
id: P-06
cluster: CL-06
title: Does the App adopt the 2026-09-09 four-role model?
question: Should the App loop adopt the 2026-09-09 four-role model that the code already ships, by amending its own governing texts, or do the unamended App texts still bind?
recommended: A — adopt for the App; amend texts
depends_on: P-09, P-22, P-23
decision_type: owner; external authority (Root / HELPS_HUMANS for role files and D-GOV-42); engineering (only under option B)
tier: GOVERNING
-->
# P-06 — Does the App adopt the 2026-09-09 four-role model?

Cluster CL-06 · named question R4-Q4 · draft by TASK D4 for HELP_HUMAN review; not a ruling.

**Question.** The 2026-09-09 commit `9b005c23a` gave the App four roles (HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS, TASK) with HELP_HUMAN as the default. It kept only the `HELP` and `AGENTS` aliases, dropped the agent matrix and Pipeline surface, and brought in Root role files without the old header. The App's PRD, SPEC, TYPES and CONTRACT were never amended to match. Does the owner adopt that model for the App, so the governing texts and deliverables change and the code stands? Or do the unamended texts still bind?

## What we found
- `9b005c23a` (2026-09-09) changed App code and tests and Root docs (Root `docs/SPEC.md`, `docs/TYPES.md`, `AGENTS.md`, the `agents/` files). It changed no file under `projects/chirality-app-dev/docs/`. [code]
- The App SPEC §13.1 fallback table still says the persona defaults to a "hardcoded `WORKING_ITEMS` default when empty or missing" (`docs/SPEC.md` §13.1). [GOVERNING]
- The live resolver sets `DEFAULT_PERSONA = 'HELP_HUMAN'` and maps only `HELP` and `AGENTS` (`frontend/src/lib/shell/persona-resolution.ts:3-9`). The retained legacy harness still defaults to `WORKING_ITEMS` (`frontend/src/lib/harness/session-manager.ts:9`). [code]
- App TYPES §3.4 and PRD FR-026 still list `ORCHESTRATE -> PROJECT_SETUP` and `DEPENDENCIES -> EVALUATION`, which the code no longer maps. [GOVERNING]
- App SPEC §7 requires every agent file to carry a `[[DOC:AGENT_INSTRUCTIONS]]` header, an `AGENT_TYPE` line and an Agent Type table. CONTRACT K-WRITE-1 requires every agent file to declare its write scope. The shipped Root role files (`agents/AGENT_HELP_HUMAN.md` and the other three) have none of these; they open with `## PROTOCOL`. [GOVERNING]
- App DIRECTIVE §0 ranks App SPEC and CONTRACT above `agents/AGENT_*.md` (rank 7), so under the App's own authority order the unamended texts prevail. [GOVERNING]
- D-APP-108 Q3 retires only the `/workbench` and `/pipeline` routes (reachable by URL, unlisted). No App ruling adopts the four-role model, and the App register has no D-GOV-42 row. [GOVERNING]
- The Root register row D-GOV-42 describes the 2026-09-09 work as an "owner-directed candidate implementation", with "exact reviewed-byte acceptance" still pending. It states that it covers no receiving-loop adoption. This is a Root record and is not on this run's GOVERNING list. [run finding]
- The adoption run `CHIRALITY_V3_APP_ADOPTION_20260909` (UI source freeze v7) explains the change, and R2 found it across four packages (XPF-015). [CONTEXT]

## Affected rows
<!-- COUNTS -->
**102 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-06`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Old assessment overtaken (`STALE_ASSESSMENT`) | Verification out of date (`STALE_VERIFICATION`) | Retired by a ruling (`RETIRED_BY_RULING`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT |  | 2 | 2 |  |  |  |  | 4 |
| PKG-02 | 13 | 16 | 18 | 2 |  | 5 | 3 | 57 |
| PKG-04 |  | 1 |  | 1 |  |  |  | 2 |
| PKG-08 | 8 | 10 | 17 | 1 | 1 |  |  | 37 |
| PKG-10 |  |  |  | 2 |  |  |  | 2 |
| **Total** | **21** | **29** | **37** | **6** | **1** | **5** | **3** | **102** |

<!-- /COUNTS -->
Most rows are in DEL-02-01, 02-02 and 02-03 (the shell, matrix and Pipeline surfaces) and DEL-08-01 and 08-02 (role-file packaging, aliases and matrix routing). Each one reads the old persona, matrix or file-format contract against code that follows the four-role model. 14 rows also turn on the legacy agent-file validator (R4-Q1, P-09). 4 rows also carry a plain owner question on release scope (R4).

## Options
**A. Adopt the four-role model for the App (code stands).** The ruling records the App loop's own adoption of the model the code ships: HELP_HUMAN default, `HELP` and `AGENTS` aliases only, matrix and Pipeline retired from the shell, and Root role-file format. It orders the App governing amendment of SPEC §7 and §13.1, TYPES §3.4 and §4, PRD FR-026 and CONTRACT K-WRITE-1. It also covers FR-001, FR-007, FR-023 and DIRECTIVE §4.1, which XPF-015 lists; the amendment tranche confirms each of these. SPEC §7 would defer the file format to Root. *R5 would:* after that amendment lands, change the deliverable text of the listed rows to the adopted model, package by package (PKG-02, PKG-08, then PKG-04, PKG-10 and the extension rows).
**B. The unamended texts bind (change the code).** Restore the WORKING_ITEMS default, the four aliases, the matrix and the header conformance on the live path. A separate `software-bounded-implementation` brief does this, and the Root role files would need the header, which is a Root matter. *R5 would:* hold every row until the code lands, then re-check.
**C. Accept the difference without amending.** *R5 would:* record the acceptance in deliverable text, so the rows become "difference already permitted". SPEC, TYPES and PRD would still contradict the code.
**D. Defer until Root accepts D-GOV-42.** The rows stay held and reopen on Root acceptance.

## HELP_HUMAN recommendation (draft)
Option A. The four-role model is what shipped in v3.0.0 and v3.0.1. The Root D-GOV-42 row records it as owner-directed, and the adoption run shows it was deliberate. Option B would reverse a released product decision to satisfy text nobody amended. Receiving-loop adoption is the App loop's own decision (Root `AGENTS.md`: each receiving loop decides its adoption), so the owner can make it here without waiting for Root. A leaves two things open: (1) Root's acceptance of D-GOV-42 and the role-file bytes, which stays with Root; (2) whether the legacy agent-file validator is kept, which P-09 decides.

## Who decides
The owner decides App adoption and the App governing amendment. The role files, `agents/registry.json`, Root SPEC and TYPES, and the D-GOV-42 acceptance are Root-owned (agent instructions and workflows are never changed by an App repair; run packet rule Δ10) and route to Root / HELPS_HUMANS; this packet asks nothing of them. Under B, engineering decides the implementation through a bounded brief.

## On ruling
1. HELP_HUMAN commits the consolidated R4 ruling record, under the next free D-APP ID with its register row. It carries the P-06 clause, which names the adopted model and the listed clauses.
2. A separate governed amendment tranche edits App SPEC, TYPES, PRD, DIRECTIVE and CONTRACT as listed. It follows the established procedure: the D-APP-38 corpus version bump and re-pin, as used under D-APP-56. An independent review covers the diff.
3. Then an R5 tranche manager per package edits the ScopeOfWork, `_STATUS`, `_REFERENCES` and register text of the `PACKET_INDEX.csv` P-06 PRIMARY rows. The 14 R4-Q1 co-cited rows wait for the P-09 ruling.
4. R6 backchecks every listed row. HELP_HUMAN sends a notice to Root recording the App adoption, for Root's own use. No lifecycle transition.

## Risks, contested rows and dependencies
- No contested or spot-refuted rows in this cluster.
- 66 of these rows are ALSO in P-22, 26 in P-23, 14 in P-09 and 4 in P-11. P-22's text repair presumes this answer.
- Before any amendment, the owner should confirm that K-WRITE-1 (declared write scope) may move from each file to the Root role registry. Otherwise the write-scope guarantee would lose its carrier.
