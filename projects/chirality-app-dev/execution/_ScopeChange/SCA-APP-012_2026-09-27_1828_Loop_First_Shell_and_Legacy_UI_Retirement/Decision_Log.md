# SCA-APP-012 Decision Log

Every checkpoint decision for SCA-APP-012. Each accepted checkpoint also has
an immutable decision snapshot under
`execution/_ScopeChange/checkpoint_snapshots/`, which is the authority for
that checkpoint. This log only indexes it.

| ID | Date | Checkpoint | Act (verbatim) | Recorded interpretation | Snapshot |
|---|---|---|---|---|---|
| DIR-1 | 2026-09-27 | Owner direction (pre-intake) | "You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary." | Initiates SCA-APP-012 on the coordinating session's proposal (`Brief.md`) | — |
| DIR-2 | 2026-09-27 | Owner direction (pre-intake) | "Scaffolding through the agent is enough." | Authority for the Runtime scaffold-API retirement (PR #1012) and for set S (`Brief.md`) | — |
| G1-ACCEPT | 2026-09-27 | Checkpoint group 1 | "Accept SCA-APP-012 group 1: R-b, W-b, P-keep (keeping the two pages, as recommended), defaults." | BASE + S + R-b + W-b + P-keep; defaults L-lib, S-tool, E; KG-033 acknowledgment unchanged; 24 register rows at group 2. P-keep departs from the approved proposal; the owner had the "One departure from what you approved" section and, as the coordinating session reports, its explanation of each recommendation | `checkpoint_snapshots/SCA-APP-012_GROUP-1_2026-09-27/` |

## Notes on accepted records (not owner acts)

Accepted decision snapshots are immutable. These notes record corrections
found after acceptance; they do not change the snapshot, and each correction
of substance goes to the owner in the next checkpoint package.

| ID | Date | Concerns | Note | Snapshot change |
|---|---|---|---|---|
| G1B-01 | 2026-09-27 | G1-ACCEPT, basis | Basis refresh. Group 2 is prepared at `830913331` (PRs #1015, #1016), not the package basis `adc8bdae1`. All 57 inputs hashed in the accepted `Brief.md` are byte-identical. Main changed the DEL-02-01 dependency register (DEP-02-01-006 `DOWNSTREAM`/`HANDOVER` → `UPSTREAM`/`INTERFACE`, target DEL-08-02 unchanged; DEP-02-01-012 resolved to DEL-05-03) outside every SCA-APP-012 edit. A rerun of the accepted builder differs only in `governed_inputs_identical_to_basis`, DEP-02-01-006's `Direction`/`Type` and the closure edge count (103 → 104); no accepted finding depends on them (`Handoff_State.md`) | None |
| G1-NOTE-1 | 2026-09-27 | G1-ACCEPT, `DECISION.md` lines 12-13 and 92, `ACCEPTED_MANIFEST.csv` (Impact Assessment row), `Handoff_State.md` line 37 | Commit identifiers and basis after a rebase. The branch was rebased onto `origin/main` `974bf7da4` (PR #1014, PEC files only; no App file, no edited file and no hashed input moved). Two commit identifiers the snapshot cites are therefore not ancestors of the branch head: `4f2d79ec9710a13f6a86c7dce82592406618ff2a` (the commit the owner was sent) and `47a62467481a9b853f90ec6285ade4605dde92fe` (its first rebase). The same revision-4 bytes are now commit `530ad4d10d44dfcd31a786a7f975e138246dcd70`; `git diff 4f2d79ec9 530ad4d10` over the package folder is empty. The acceptance binds content by SHA-256 in `ACCEPTED_MANIFEST.csv`, and those hashes are unchanged, so the accepted identity holds. The snapshot text naming `830913331` as the group-2 basis stays true for the package; the branch head is `974bf7da4` plus this package. Method.md makes decision snapshots immutable and gives no pre-merge exception, so the snapshot is not rewritten; commit identifiers in it are informational until merge, and further rebases are recorded here | None (snapshot immutable) |
