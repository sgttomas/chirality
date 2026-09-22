<!-- PACKET
id: P-01
cluster: CL-01
title: Two DEL-06-02 rows where the two workers disagreed
question: For DEL-06-02#CLM-005 and #CLM-032, which of the two workers' verdicts stands, or a third reading?
recommended: C — both "built differently", follow P-09
depends_on: P-09
decision_type: owner
tier: GOVERNING
-->
# P-01 — Two DEL-06-02 rows where the two workers disagreed

Cluster CL-01 · no named question · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** DEL-06-02 (the SDK read-tool surface and tool-name validation) was audited twice, independently. On two rows the workers reached opposite verdicts, and you reserved both for yourself (RUN_BASIS Addendum 5). Which verdict stands for each row?

## What we found
- The run recorded both verdicts and resolved neither, as you directed: worker A's ledger (`R2/PKG-06/DEL-06-02_A`) is the ledger of record and worker B's (`R2/PKG-06/DEL-06-02_B`) is carried alongside in the concordance column `AltReading` (RUN_BASIS Addendum 5; R3_SUMMARY §8). [run finding]
- **CLM-005 (the "Construction" table).** The deliverable text lists a tool registry, a resolver, name validation, deterministic ordering, read-first filtering, a hand-off to the permission layer, and tests. It marks the registry path, interface shape and test paths as TBD (DEL-06-02 `ScopeOfWork.md` CLM-005). [run finding]
- CLM-005, worker A: **text out of date** (`STALE_SPECIFICATION`), cause pre-v3 drift, HIGH confidence. Reasoning: the "TBD" paths are now false because the code exists. A also notes the deterministic-ordering item is not built: the resolver keeps request order. [run finding]
- CLM-005, worker B: **built differently** (`IMPLEMENTED_DIFFERENTLY`), cause "Codex is the only engine", MEDIUM confidence. Reasoning: the construction exists only in the legacy harness (the retained in-process Claude SDK code that the live Codex path does not reach). The live Codex path uses Runtime admission and the Codex sandbox instead. The TBD paths are also stale. [run finding]
- **CLM-032 (the "Examples" table).** Five scenarios: registered names accepted; an unknown name rejected before reaching the SDK; `Write` excluded in read-only mode; `allowedTools` cannot bypass policy; a new `domain_*` tool name treated as unsupported until amended. [run finding]
- CLM-032, worker A: **built differently**, cause "Codex is the only engine", MEDIUM. Reasoning: examples 1–4 hold only in the legacy harness, and example 5 is overtaken. [run finding]
- CLM-032, worker B: **text out of date**, cause pre-v3 drift, MEDIUM. Reasoning: a ruling explicitly overtook example 5, and examples 1–4 follow other rows that are legacy-only. [run finding]
- The code both workers relied on: the legacy resolver `resolveHarnessToolPool` de-duplicates the request and keeps its order, with no canonical sort (`frontend/src/lib/harness/tool-pool.ts:36-111`). On the live path, the Runtime filters requested tools by read-only pattern, role and method, with no registry lookup (`chirality-runtime/packages/core/src/runtime-method-service.ts:507-519`). The Codex adapter starts the turn with an empty tool list (`packages/core/src/delegated-engine-adapter.ts:231`). [code]
- The five `domain_*` tool names are registered (`chirality-runtime/packages/contracts/src/harness/mcp/tool-names.ts:16-22`). [code]
- D-APP-56 (R4-P27) explicitly reconciles the former "unsupported/TBD" domain-tool wording and gives the domain roster to PKG-10. DEL-06-02's own ScopeOfWork records this at CLM-034, but the CLM-032 example 5 was never changed. [GOVERNING]
- D-GOV-43 makes Codex the sole engine. Its App application, D-APP-127, does not name DEL-06-02 or CONTRACT K-TOOL-1 (the tool-registry invariant). [GOVERNING]
- Since this split happened, you adopted the "legacy-versus-live subject test" (RUN_BASIS Addendum 6; CONVENTIONS §2.4). A claim that states an outcome or a guarantee is product behaviour and is judged on the live Codex path. Where only legacy code meets it, the row waits on R4-Q1: is the retained legacy harness history, compatibility or an obligation? Both rows carry R4-Q1 in the final concordance (R3 re-derived CLM-005's). [run finding]

## Affected rows
<!-- COUNTS -->
**2 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-01`.

| Package | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|---:|
| PKG-06 | 1 | 1 | 2 |
| **Total** | **1** | **1** | **2** |

<!-- /COUNTS -->
Two rows in one deliverable (DEL-06-02). Both describe the legacy tool resolver, and both now wait on R4-Q1 (P-09). Worker A's verdicts are the current values.

## Options
**A. Worker A stands** (CLM-005 text out of date; CLM-032 built differently). *R5 would:* for CLM-005, replace the TBD paths with the real locations and say which path they serve. For CLM-032, restate the examples for the Codex path, or mark them as legacy, once P-09 is ruled.

**B. Worker B stands** (CLM-005 built differently; CLM-032 text out of date). *R5 would:* for CLM-032, replace example 5 now, since D-APP-56 already decided it. CLM-005 would wait on P-09.

**C. Both "built differently", each waiting on P-09, applying the subject test you adopted later.** Both tables state outcomes and guarantees (accept, reject, exclude, deny, "no bypass"), so the subject test treats them as product behaviour. On the live Codex path, no registry lookup, ordering or unknown-name rejection happens. The stale parts (the TBD paths in CLM-005; example 5 in CLM-032) are recorded as secondary "text out of date" findings on the same rows. *R5 would:* fix the TBD paths and example 5 now, because those repairs need no R4-Q1 answer. The rest of each row follows the P-09 ruling: either mark the tables as legacy history, or restate them for the live path.

**D. Defer.** Both rows stay held with their current values until P-09 is ruled, and you decide then.

## HELP_HUMAN recommendation (draft)
Option C. It applies the rule you adopted to settle exactly this kind of split (Addendum 6, rules 1–2), and it treats these rows the same way as the rest of the R4-Q1 population. It also lets the two uncontested text repairs, which D-APP-56 and the existing code already settle, go ahead without waiting for P-09. The deterministic-ordering gap (the resolver does not sort) is left open. Whether it is owed at all depends on P-09: it is real only if the legacy harness remains an obligation.

## Who decides
Owner (you reserved these keys). Nothing here is outside your App authority.

## On ruling
The consolidated R4 ruling record (the next free D-APP ID in `execution/_Coordination/_DECISIONS/_REGISTER.md`, with its register row, committed by HELP_HUMAN before any repair) names both keys and the Disposition chosen for each. The PKG-06 R5 tranche manager then edits DEL-06-02 `ScopeOfWork.md` CLM-005 and CLM-032 (`PACKET_INDEX.csv` rows P-01), limited to the parts the ruling releases. Under option C, those are the TBD paths and example 5. The remainder waits for the P-09 clause. R6 backchecks both rows against the ruling. No code change and no lifecycle transition.

## Risks, contested rows and dependencies
- Both rows are contested by design (the two workers' readings are in `AltReading`). Neither is touched by the spot check or the owner check.
- Depends on P-09 (R4-Q1): under every option, the substantive repair of both rows follows that ruling.
- CLM-005 is also a member of P-19 (pre-v3 drift), and CLM-032 of P-20 (Codex sole engine). Those packets do not decide these rows.
