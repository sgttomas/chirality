<!-- PACKET
id: P-EX
cluster: CL-EX
title: Three rows that fit no other packet
question: For each of three unrelated rows, what should R5 do?
recommended: EX-1 record; EX-2 route; EX-3 fix text
depends_on: none
decision_type: owner; HELPS_HUMANS (workflow, for EX-2)
tier: mixed
-->
# P-EX — Three rows that fit no other packet

Cluster CL-EX · no named question · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** Three rows from the extension audit (decision register, decomposition scope ledger and release documents) fit no other cluster. Each gets its own short question.

- **P-EX.a (EX-1)** — `DEC:D-APP-99`. Four committed evidence files exceed D-APP-99's size guideline, and no reason is recorded. What should happen?
- **P-EX.b (EX-2)** — `SOW:SOW-033.2`. Is "immutable snapshots" (PRD FR-062) App product scope, or a workflow convention?
- **P-EX.c (EX-3)** — `DOC:RQRUN#2`. Should the release-quality runbook be corrected to what the wrapper actually runs?

## What we found
- **EX-1.** D-APP-99 (C3, 2026-08-17, prospective) says committed evidence is compact and commit-bound. "a committed evidence file over ~2,000 lines needs a stated reason in the run record" (ruling record, line 18). [GOVERNING]
- **EX-1.** Four DEL-09-06 secret-scan summaries written after that ruling run from 7,515 to 9,922 lines. `Evidence/Node_N_CSP_Nonce_2026-09-04/secret-scan-summary.json` is 9,922 lines, and the three `Packaged_Security_Proof_2026-08-20` copies run 7,515–7,578. The Node N run record cites its file without giving a size reason. Other evidence adopted the compact shape. The row is graded **partly built**, cause "unrecorded judgment", MEDIUM confidence, because the ruling calls the threshold a guideline. [run finding]
- **EX-2.** The decomposition scope ledger row SOW-033 ("Immutable snapshots", PRD §8.10, owned by DEL-07-06) is in scope. PRD FR-062 says snapshot-producing workflows write immutable timestamped folders and mutable `_LATEST.md` pointers (`docs/PRD.md:697`). [GOVERNING]
- **EX-2.** No App or Runtime code produces snapshots, and no ruling defers it. DEL-07-06 is a documentation deliverable. The row is graded **agent-instruction matter**, cause "workflow convention", LOW confidence. The worker recorded two other readings: a pure documentation convention ("matches"), or product scope ("written, not built"). [run finding]
- **EX-3.** `docs/RELEASE_QUALITY_RUNBOOK.md` §2 says the wrapper runs the full test suite, typecheck, a standalone `npm run harness:validate:section9`, and premerge. [run finding]
- **EX-3.** The wrapper first runs `harness:validate:contract-deps` (`frontend/package.json:29`). It then runs Section 9 and premerge in-process, reusing the full test run (`frontend/scripts/validate-release-quality-evidence.mjs:430-446`). This changed in commit `718b0d47a` (2026-09-09, "reuse release test results"). The row is graded **text out of date**. The output path and the rest of the command set are correct. [code]

## Affected rows
<!-- COUNTS -->
**3 rows are decided in this packet** (PRIMARY); 0 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-EX`.

| Package | Partly built (`PARTIALLY_IMPLEMENTED`) | Text out of date (`STALE_SPECIFICATION`) | Agent-instruction matter (`DEFERRED_AGENT_WORKFLOW`) | Total |
|---|---:|---:|---:|---:|
| EXT | 1 | 1 | 1 | 3 |
| **Total** | **1** | **1** | **1** | **3** |

<!-- /COUNTS -->
Three unrelated rows, one per sub-question. No sub-question file is needed, because each row is its own question.

## Options
**EX-1 (`DEC:D-APP-99`):**
- **A. Record the reason.** A note in the DEL-09-06 record states why the per-file path lists were kept, or states that no reason was given. *R5 would:* add that note to DEL-09-06 `_STATUS.md` History, citing the four files.
- **B. Replace the files** with compact, hash-referenced summaries. This is a separate bounded task that re-derives the summaries. *R5 would:* repair the text after the task lands.
- **C. Accept the divergence.** The ruling names the four files as a permitted guideline exception. *R5 would:* record the acceptance.

**EX-2 (`SOW:SOW-033.2`):**
- **A. Workflow convention.** FR-062 describes what snapshot-producing *workflows* do, so it routes to HELPS_HUMANS for workflow and instruction guidance. *R5 would:* at most add one clarifying sentence to DEL-07-06.
- **B. Product scope.** The App should produce snapshots. *R5 would:* change nothing, and a separate implementation brief would follow.
- **C. Documentation convention already met.** *R5 would:* change nothing, and the ruling records the row as "matches".

**EX-3 (`DOC:RQRUN#2`):**
- **A. Change the text.** *R5 would:* describe Section 9 and premerge as in-process steps that reuse the full test run, and add the contract-deps pre-step.
- **B. Defer.**

## HELP_HUMAN recommendation (draft)
- **EX-1: A.** The ruling asks only for a stated reason. Rewriting committed evidence is heavier than the guideline warrants, and those files are part of the release-proof history.
- **EX-2: A.** Nothing in the App's code or the decomposition makes the App itself the snapshot producer. The confidence is low, so you may prefer C.
- **EX-3: A.** A plain correction.
- Left open: whether the D-APP-99 guideline should become a checked limit. That is a future engineering choice.

## Who decides
- **Owner:** all three.
- **HELPS_HUMANS:** EX-2 under option A. It owns workflow and instruction method, and would decide how snapshot conventions are expressed in workflows.
- **Engineering:** EX-1 option B would need a bounded task.
- Nothing here is outside your App authority.

## On ruling
- **Ruling record.** The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN before any repair) carries one clause per row, keyed by `PACKET_INDEX.csv` P-EX.
- **R5.** The EXT tranche manager handles EX-3 (`docs/RELEASE_QUALITY_RUNBOOK.md` §2) and the EX-1 note, which lands in the PKG-09 DEL-09-06 folder, so the PKG-09 tranche writes it. Under option A, EX-2 is a HELPS_HUMANS handoff, plus any DEL-07-06 sentence.
- **Checks.** R6 backchecks all three rows. No code change and no lifecycle transition.

## Risks, contested rows and dependencies
- EX-2 is the least confident row here (LOW), and its alternative readings are recorded on the row.
- EX-1 under option B would rewrite committed packaged-security evidence. Check first for rows elsewhere that cite those files.
- No dependencies on other packets.
