## 8. Cross-package observations for R3 (hand-written by the PKG-07 manager; evidence, not rulings)

1. **Live scaffolding is not wired (DEL-07-02; both blind workers found it independently).**
   `POST /api/harness/scaffold` is served, but `RuntimeService.scaffold` returns 501
   `ENGINE_UNAVAILABLE` because the App-owned composition passes `scaffoldPort = undefined`
   (`app-owned-composition.ts:226`). The only adapter left with the in-process host (`2f825f180`,
   deleted in `39c0bb6ab`, the D-GOV-43 A2 change). No ruling or CONTEXT record says scaffolding was
   dropped. Worker B also reads the heading regex (`scaffold.ts:273`) as rejecting every package
   heading of the accepted v3.2 decomposition (from code reading, not a run). Relevant to the A2
   topology cluster (PKG-03/05) and to SOW rows for scaffolding.
2. **Path-containment guarantees exist only on the legacy path (DEL-07-01, 07-04, 07-05).**
   Working-root validation runs LIVE (App validate route, Runtime project registry). Instruction-root
   write protection, symlink rejection, fail-closed hooks, the status/dependency MCP tools and their
   permission checks exist only in retained Claude-SDK code; the live Codex runtime registers no
   Chirality MCP server (`runtime-service.ts:580` `mcpServers: []`). 52 rows cite R4-Q1; DEL-07-01
   holds six AUTHORITY_CONFLICT rows (unamended K-ROOT-2, K-PATH-2/3, K-HOOK-1, DIRECTIVE §2.9 against
   D-GOV-43 items 4 and 10). Same cluster as R0 §8 item 1 and PKG-04/06/08.
3. **R4-Q3 is concrete in DEL-07-04.** Actor and approval SHA are caller-supplied free strings on both
   the POST route and the legacy MCP tool (SHA checked for format only); REQ-013 is AUTHORITY_CONFLICT
   (D-APP-13 vs unamended K-AUTH-1 / K-GATE-1). The code also lags SPEC §4.3 (human actor missing on
   two forward transitions; the 2026-07-11 human reversal transitions are rejected), and every
   transition rewrites `_STATUS.md` from parsed fields, dropping `## Remaining` and free-form history.
   Codex agents change `_STATUS.md` by direct file edit and bypass the transition validator entirely.
4. **Routes served but never called from the rendered UI.** The status, dependency and scaffold API
   routes are LIVE handlers, but their only UI callers sit in unmounted Pipeline / Workbench /
   LoopShell surfaces. The pack's REACHABILITY map tags those surfaces LIVE. R3 should treat
   "served route, no rendered caller" consistently across packages (PKG-02 shell findings).
5. **Carrier propagation is total in PKG-07.** No PKG-07 carrier — not even `_STATUS.md` — cites
   D-APP-127 or D-GOV-43 (pack item 5: 30/30 `NO`), unlike R0 packages where `_STATUS.md` was revised.
6. **Reference-hash drift is post-v3 and invisible to the product.** All 18 `_REFERENCES.md` MATCH
   hashes fail; the recorded values equal authority corpus v23, and the three docs were edited on
   2026-09-12 without the D-APP-38 corpus bump (DEL-07-06). The App's scanner only greps for the
   literal `HASH_MISMATCH` and never recomputes, so the App cannot show the drift. Tagging of this
   drift differs across ledgers (DOC_HYGIENE vs PRE_V3_DRIFT; `GOV:D-GOV-43` vs `NONE_FOUND`) — see
   VERIFICATION.md pattern 1 and CORRECTIONS.csv. Supports R0 §8 item 7 (one corpus-wide repair).
7. **Deleted four-document kit still cited.** `Dependencies.csv` rows in DEL-07-02, 07-05 and 07-06
   (25 ACTIVE rows in DEL-07-05 alone) cite `Datasheet.md` / `Specification.md` / `Procedure.md`,
   deleted 2026-07-13 (`8cb9cdaf0`); DEL-07-04 DEP-07-04-008 is SATISFIED at two module paths that
   never existed in git.
8. **Coverage gaps (no forward row can own them):**
   - SoW `## Purpose and Objective Traceability` (OUT-001) and `## Output and Evaluation Matrix` are
     not indexed units in DEL-07-01, 07-02 and 07-06; the matrices point OUT-001 at a non-requirement
     unit (CLM-007/CLM-008).
   - DEL-07-03: the live scanner's ScopeOfWork.md production-format resolver and migration-dual code
     (`filesystem.ts:186-203, 657-861`; CAP-WORKSPACE-014/015) has no SoW unit — an
     IMPLEMENTED_UNDOCUMENTED candidate; valid SOW_V1 folders still get four
     `missing_document_kit_file` warnings.
   - DEL-07-04: no SoW unit states that transitions must preserve `## Remaining` and history.
   - DEL-07-06: the App execution-tree governance scripts (`references_hash_tool.py`,
     `validate_dependencies.py`, `reconcile_authority_corpus.py`) implement K-REF-1 but belong to no
     capability area.
   - `_SEMANTIC*.md` files are not indexed and embed machine-specific absolute paths (DEL-07-01, 07-04, 07-06).
9. **Cross-deliverable:** DEL-07-03's governed-workflow file contract (`governed-workflow.ts`, PR #733)
   is TEST_ONLY; the live Workflows panel lists Runtime WORKFLOW.md packages (CAP-WOVEN-030). No record
   retires the SOW-081 governed-file contract — for DEL-02-02 / PKG-02. DEL-07-01's Remaining item
   cites D-APP-98 (Electron version) where D-APP-100 appears intended, and names the deleted
   `electron/daemon-instruction-root.ts`; three DEL-07-01 rows carry `D-APP-119` (AWAITING_RULING).
10. **Double-blind reading (details in `DOUBLE_BLIND_DEL-07-02.md` §9–§10):** Disposition exact
    agreement 19/31 (61%), ALIGNED-vs-not 23/23 on unsplit keys; no pure STALE_SPECIFICATION vs
    REMAINING_STATE_MISMATCH split (Addendum 5 held); R4-Q1 agreement 19/31 — A 0 rows, B 22 rows —
    entirely from symbol-level REACH tagging in `scaffold.ts` (TEST_ONLY vs LEGACY_ONLY), not from
    subject reading. Rule 3 needs a stated reading for claims met by mixed TEST_ONLY + LEGACY_ONLY code.
