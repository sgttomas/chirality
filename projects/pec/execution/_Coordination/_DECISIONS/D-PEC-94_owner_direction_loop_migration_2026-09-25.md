# D-PEC-94 — owner direction: PEC adopts the shared development loop; remaining work is organized by work graph

Owner: Ryan Tufts. Date: 2026-09-25 (session date). HELP_HUMAN recorded this (run `HELP-HUMAN-PEC-20260923-SCA005`, node M1) as a faithful transcription under K-AUTH-1.

## Exact owner direction (verbatim)

> You can continue with all the open work you identified.  Start with the loop migration, then use the loops for organizing the remaining work into a work graph to help plan and orchestrate the implementation.  You are now HELP_HUMAN in the Agent 0 role.  Read your instructions if you need a refresher and carry on.

HELP_HUMAN's preceding message listed the open work after the D-PEC-93 closeout (PR #915):
- stale pointer and handoff text;
- context and reference re-pinning;
- the 19 stale dependency evidence quotes;
- SOW currency and the first SOWs for DEL-02-08/09;
- the `projects/pec/AGENTS.md` instruction update;
- the D-PEC-90 reliance amendment;
- PEC's loop migration.

Status: **DIRECTION OF RECORD / EFFECTIVE ON SHARED-MAIN PUBLICATION**.

## HELP_HUMAN interpretation (interpretation, not owner text)

| Item | Effect |
|---|---|
| Loop migration | This exercises `D-PEC-86` §3 I-7, whose deferral condition (SCA-005 closing) was met on 2026-09-25. PEC adopts the shared development-loop method that App and Piping run. That means an evergreen `loop/LOOP_INIT.md`, steering-selected undertakings, work graphs at `execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md`, PR-sized slices, one bounded closeout, one central `AgentRuns/<RunID>/RECEIPT.md` and terse deliverable `MEMORY.md` entries. The change is carried as an instruction tranche with its own manifest and notices, as Root `AGENTS.md` requires. It also carries the pending `projects/pec/AGENTS.md` fixes: PRD v2.3 references, and the D-GOV-43 A2 Runtime boundary. `loop/LOOP_RECEIPTS.md` is frozen as a historical ledger after its final receipt. `D-PEC-80` is superseded only as the dispositions table below states (item B's generic instruction surface and selection, item C's per-iteration receipt and one-PR boundary, and item D's Remaining-only selection); its loop home `projects/pec/loop/` (item A) and item D's workplan retirement and owner-intent record stand. |
| Organizing the remaining work | After the migration merges, HELP_HUMAN constructs one work graph for the remaining open work with `construct-local-work-graph`. The graph plans and orchestrates it through PRs, and each node that writes outside PEC's default surfaces still needs its own owner-ruled D-PEC packet. The graph itself grants no scope. |
| "Continue with all the open work" | This authorizes HELP_HUMAN to prepare and carry the listed work forward within existing authority. Writes that `projects/pec/AGENTS.md` fences (decomposition, registers, `_STATUS.md`, `docs/PRD.md`, `v2/**`) still come to the owner as exact packets, prepared ready to decide. |

## The adoption tranche (the packet this record opens)

The migration is the tranche `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml` (SHA-256 `0ccddebe999f1ee3a35ff0672069fce20302ab9ae56517836e825c68a3beb783`), prepared by HELPS_HUMANS (run-record node M1) and independently verified. This record opens exactly its paths, acts, checks and rollback:
- `projects/pec/loop/LOOP_INIT.md` (rewritten as PEC's instance of the shared method), `projects/pec/AGENTS.md` (loop, record and check sections; PRD v2.3; D-GOV-43 A2 Runtime boundary), and `projects/pec/loop/LOOP_RECEIPTS.md` (append-only closing Receipt 197; frozen thereafter);
- the four non-binding adoption notices (Root, App, Piping, Runtime);
- in addition, `projects/pec/init/taskmgmt-init-prompt.md`, whose lines saying the pointer does not adopt the App/Piping loop become false, is opened for that correction.

`docs/STATUS.md` and `README.md` are refreshed under `D-PEC-88`. Rollback: a revert PR of the whole adoption PR, restoring the preimages the manifest lists and, with them, this record's dependent `init/taskmgmt-init-prompt.md`, `docs/STATUS.md` and `README.md` text. The accepted `D-PEC-80` ruling text is not edited.

## Dispositions of the tranche's open points (HELP_HUMAN interpretation, not owner text; the owner may revise any of them)

| Point | Disposition | Basis |
|---|---|---|
| `D-PEC-88` item 6: does the standing STATUS/README duty carry into the migrated loop? | Yes, as HELP_HUMAN's interpretation put to the owner for confirmation (D-PEC-88 says this is decided at the migration). It stays standing until the owner revokes it; its trace clause is met through each undertaking's work graph and central receipt, as the new `AGENTS.md` states. | `D-PEC-88` is standing until revoked, and the owner's direction continues the work without revoking it. |
| MEMORY rows (the method's Step 5) under PEC's fence | Unchanged: a deliverable `MEMORY.md` row needs the path grant of the undertaking's governing `D-PEC` packet, which names those paths, as the new `AGENTS.md` states. This record grants no standing MEMORY write. | A standing grant would widen write authority beyond what the owner stated. The owner may add a standing clause for terse run-index rows if the per-packet naming proves burdensome. |
| `## Remaining` | The sections stay as deliverable-local records. They no longer select work and receive no new entries; retiring them is a separate owner-directed undertaking. | Tranche design; nothing is deleted. |
| `D-PEC-80` | Not edited. Item A (loop home) stands; item B's generic instruction surface and selection and item C's per-iteration receipt and one-PR boundary are replaced by the shared method; item D's workplan retirement and owner-intent record stand, its Remaining-only selection is replaced. | The owner's adoption direction; the tranche's reading. |
| Launcher alignment | `projects/pec/init/dev-loop-init-prompt.md` stays byte-bound to Root `init/dev-loop-init-prompt.md` §4 (checked by `validate_instruction_entrypoints.py`); aligning its wording with App/Piping needs a Root change and is out of scope. | Root owns that file. |

## Limits

No CHECKING, ISSUED, artifact acceptance or release. No product, decomposition or lifecycle change is made by this record. D-PEC-88's standing STATUS/README duty continues; its "trace in receipts" now means the undertaking's central receipt and work graph.
