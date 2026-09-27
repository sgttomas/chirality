# SCA-APP-011 Decision Log

Every checkpoint decision for SCA-APP-011. Each accepted checkpoint also has
an immutable decision snapshot under
`execution/_ScopeChange/checkpoint_snapshots/`, which is the authority for
that checkpoint. This log only indexes it.

| ID | Date | Checkpoint | Act (verbatim) | Recorded interpretation | Snapshot |
|---|---|---|---|---|---|
| DIR-1 | 2026-09-27 | Owner direction (pre-intake) | "We don't need to carry the Workbench or Pipeline forms any longer. They are obsolete." Route option "Remove the routes (Recommended)"; scope option "Scope-change amendment (Recommended)" | Initiates SCA-APP-011 (`Brief.md`) | — |
| SEL-1 | 2026-09-27 | Group-1 choices (AskUserQuestion) | A "Rescope it (Recommended)"; B "Exclude it (Recommended)"; D "Restate them (Recommended)"; S "Remove the route too" | Stated selections, not a checkpoint acceptance (`Brief.md`) | — |
| G1-ACCEPT | 2026-09-27 | Checkpoint group 1 | "I accept SCA-APP-011 checkpoint group 1" | BASE + DQ-R + S-c; D restate; L excluded; E no change; M-a; scaffold library kept | `checkpoint_snapshots/SCA-APP-011_GROUP-1_2026-09-27/` |
| G2 | — | Checkpoint group 2 | Awaiting owner: the candidate is revision 2 of `Propagation_Plan.md` (presentation at top, with the G1-NOTE-1 correction and the DEL-07-01 addition), `Amendment_Preview.md`, `Amendment_Actions.csv`, `Supersession_Delta.csv`; open choices W and Q | — | — |
| G3 | — | Checkpoint group 3 | Awaiting owner | — | — |

## Notes on accepted records (not owner acts)

Accepted decision snapshots are immutable. These notes record corrections
found after acceptance; they do not change the snapshot, and each correction
of substance goes to the owner in the next checkpoint package.

| ID | Date | Concerns | Note | Snapshot change |
|---|---|---|---|---|
| G1-NOTE-1 | 2026-09-27 | G1-ACCEPT, M-a row | Truth correction. The accepted M-a wording ("state that live Codex exposure is DEL-06-03's open work") names DEL-06-03 for all four tool contracts. DEL-06-03 is "Initial Chirality MCP Read Tools" and owns only the reads. The group-2 exact text says instead: live exposure of the read tools (`status_read`, `deps_read`, scaffold preview) is DEL-06-03's open work; `status_transition` and `deps_write` remain retained, governed operations with no live registration, and any live registration of them is governed by DEL-06-04-REQ-010. The substance of M-a (the library is the interface; this amendment adds no live tool exposure; the Root tools are today's agent path) is unchanged. Flagged in the group-2 presentation for the owner's group-2 act. | None |
| G1-NOTE-2 | 2026-09-27 | G1-ACCEPT, `DECISION.md` line 12-13 | Wording nit. `DECISION.md` calls "Please accept, correct or return group 1" the top section of Impact Assessment revision 2. It is a subsection (line 89) under the top section "Checkpoint group 1 — revision 2: final acceptance requested" (line 31). The accepted content and the owner's act are unaffected. | None (snapshot immutable) |
