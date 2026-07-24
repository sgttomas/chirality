# D-PEC-58 — RULED: adopt PRD v2.0 (coordination plane) and supersede PRD v1.0

**Status:** RULED 2026-07-24 — owner adoption act; documentation-only fence, owner-amended same day to include the prototype-docs archive cleanup
**Decision ID:** D-PEC-58
**FramedBy:** agent (Claude Fable 5), under the ruled `D-PEC-57` O-A path
**Structure precedent:** `D-PEC-55_prd_v1_adoption.md` (adoption act, exact fence, verification/rollback)

## Context

`D-PEC-57` (RULED O-A, 2026-07-24) adopted the coordination-plane product
direction and routed the candidate PRD to this adoption gate. The owner's
"proceed to D-PEC-58" direction authorizes framing and staging this packet;
per D-PEC-57's own ruling text and the K-AUTH-1 gate, **adoption of the PRD
text is the distinct owner act recorded on this row**.

Candidate under review:
`projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md`
(authored at commit `e3d696423`).

Staged companion (activated only by this row's ruling):
`projects/pec/execution/_Coordination/WORKPLAN_CANDIDATE_2026-07-24_pec_coordination_plane.md`
— the replacement standing plan, deliberately staged **outside**
`_DomainEngines/pec/` because LOOP_INIT selects the newest `WORKPLAN_*.md`
in that directory and the candidate must not become live protocol before
this ruling.

## Ruled behavior (proposed; effective upon adoption)

1. PRD v2.0 (coordination plane) is **adopted** as the product definition of
   record for PEC: the candidate text is promoted to `projects/pec/docs/PRD.md`
   with header status flipped to Adopted (date of ruling, `D-PEC-58`).
2. PRD v1.0 (team information hub) is **superseded**. Its full text remains
   preserved in Git at the last commit carrying it as
   `projects/pec/docs/PRD.md`; that SHA is recorded in this packet at
   execution time, per the D-PEC-55 convention of citing the commit that
   last carried the superseded text (recorded at execution:
   **`c31be74c2:projects/pec/docs/PRD.md`**; the text is additionally
   archived at `projects/pec/docs/.archive/PRD_v1.0_2026-07-09_team_information_hub.md`). The carry-forward clause
   is PRD v2 §14. The v0.4 catalogue remains preserved at
   `7e8312172:projects/pec/docs/PRD.md`.
3. `SPEC.md` and `TRACEABILITY.md` remain the implemented v0.4 prototype
   baseline documentation. Their historical-basis notices are updated to name
   v2.0 as the adopted product and the governed-pipeline greenfield build as
   the delivery path (replacing the now-void "T0 rebaseline" pointer).
   `STATUS.md` and `README.md` product-direction notes are updated likewise.
4. The standing plan
   `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md` is
   **superseded**: the staged candidate workplan is moved to
   `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`
   (becoming the live protocol per LOOP_INIT), and the 2026-07-09 plan
   receives a gate-state supersession note only.
5. `D-PEC-49` (week-over-week deliverable progress, AWAITING_RULING since
   2026-07-09) is **closed as moot**: its subject matter belongs to the
   retired reporting product. Closure is recorded by a dated note in its
   packet and a register-row state change to `RULED` with ruling cell
   "Closed as moot by D-PEC-58" (per the register's row-state vocabulary).
   Nothing in this closure prevents a future packet from reviving the idea
   against v2 entities under its own new row (residual-work convention).
6. The old application (`core/`, `server/`, `web/`, `agent-sidecar/`,
   `tools/`, fixtures, demo tooling) is recorded as a **frozen reference
   corpus** per PRD v2 §13: read/cite only; no further feature work; archive
   from the working tree is a future packet after Phase 2 utility.
7. The next owner gate after this row is **decomposition**: a SOFTWARE_DECOMP
   session over PRD v2 with the owner at Gates 1–7. Decomposition acceptance
   and all scaffolding/implementation writes require their own packets.
   No requirement in PRD v2 becomes an implementation mandate by this
   adoption alone; PRD v2 §16 open decisions remain open and must not be
   guessed.
8. `D-PEC-56` is **partially superseded**: its ruled behavior 1 (retain
   PEC's deterministic acts, RBAC, reporting, and domain tools as a project
   adapter service) does not survive the product retirement (PRD v2
   §8/§13); its no-dual-loop boundary (behavior 4) and human-only-act
   restrictions (behavior 7) survive unchanged.
9. In ruling this row the owner also answers, or defers with awareness, the
   question PRD v2 §15 reserves: whether PEC's persistent presence service
   falls within `D-GOV-01` Option A's "no coordinator process" clause. The
   record tier is Option A's sanctioned projection either way.
10. Follow-ons noted, not executed here: `_DomainEngines/profiles/pec.yaml`
   supersession (domain-engine framing and the L3 import lane belong to the
   retired product) and the `projects/pec/AGENTS.md` overlay rewrite are
   named as the first candidate packets of the new workplan.

## Exact fence (upon ruling)

- `projects/pec/docs/PRD.md` (replaced with the adopted v2.0 text)
- `projects/pec/docs/SPEC.md`, `projects/pec/docs/TRACEABILITY.md` (basis notices only)
- `projects/pec/docs/STATUS.md`, `projects/pec/README.md` (product-direction notes only)
- `projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md` (header note: adopted and promoted; file retained as authoring record)
- `projects/pec/execution/_Coordination/WORKPLAN_CANDIDATE_2026-07-24_pec_coordination_plane.md` (moved to `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md`)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-49_week_over_week_deliverable_progress.md` (closure note only)
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md` (supersession gate-state note only)
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

No runtime source, dependency, database, demo input, report, profile, or
external system change is authorized by this row. PRD v2 requirement content
is not modified at promotion beyond header/status fields.

## Verification and rollback

- Verify `docs/PRD.md` reads v2.0 Adopted and no `docs/`/`README.md` surface
  still names the team information hub as the target product.
- Verify preservation objects resolve: the execution-time-recorded v1.0 SHA
  and `7e8312172:projects/pec/docs/PRD.md` (v0.4).
- Verify `_DomainEngines/pec/` contains exactly one newest workplan dated
  2026-07-24 and LOOP_INIT resolves to it.
- Verify the D-PEC-49 row reads `RULED` / "Closed as moot by D-PEC-58" and
  its packet carries the dated closure note.
- Run `git diff --check`; append the loop receipt.
- Roll back by reverting the documentation/coordination commit(s); no data
  rollback exists.

## Human ruling

**RULED (adoption), 2026-07-24.** Owner direction of record (Ryan Tufts,
in-session, 2026-07-24), verbatim:

> "you should also clean up the current PEC project folder removing all
> obsolete files along with the current PRD.  You can just move them into the
> nearest `.archive` folder or something if you want.  You do what's best,
> but it seems prudent?  Otherwise, you have approve to proceed with the PRD
> v2 candidate to promote it and proceed from there accordingly.  Then open
> the PR once that's complete and you can self-merge on this approval given
> now, for the remainder of this session only.  Continue executing with
> `opus-5` subagents where it's effective."

PRD v2.0 is adopted; ruled behavior items 1–10 execute under this row.

**Owner-directed fence amendment (2026-07-24, quoted above):** this row's
fence additionally covers the prototype-docs cleanup — moves of
`projects/pec/docs/{SPEC,TRACEABILITY,PILOT}.md` and `docs/adr/**` into
`projects/pec/docs/.archive/**`; archival of the superseded PRD v1.0 and
prototype `STATUS.md`/`README.md` texts; a replacement `docs/STATUS.md` and
rewritten `projects/pec/README.md`; and removal of the committed demo
database `projects/pec/pec-demo.db` (preserved in Git history). The frozen
reference corpus (`core/`, `server/`, `web/`, `agent-sidecar/`, `tools/`,
`fixtures/`, workspace manifests) and the live loop launcher
(`init/init-prompt.md`) are deliberately NOT touched; source-tree archival
remains a future packet per PRD v2 §13. Ruled behavior 3 is superseded by
this amendment: `SPEC.md`/`TRACEABILITY.md` are archived rather than
re-noticed, and their v1.0/T0-rebaseline notices are accepted as permanently
stale historical text, indexed by `docs/.archive/README.md`. A `.gitignore`
guard against `pec-demo.db` reappearing (the path is not currently ignored
and old runbooks still name it) is outside this fence and is noted for the
follow-on packet.

**Coordination notice (agent-index change-notice rule):**
`_DomainEngines/profiles/pec.yaml` `chirality_readable_artifacts` still
enumerates pre-archive paths for `SPEC.md`, `TRACEABILITY.md`, `PILOT.md`,
and `adr/ADR.md` (the file's header comment names the same pre-archive
paths); that enumeration is stale as of this row's execution and
is not edited here (profile edits are outside this fence). Resolution
belongs to the named profile-supersession follow-on (item 10).

Additionally (recorded at execution, 2026-07-24): historical decision
records — at minimum `D-T0-12..15`, which cite `projects/pec/docs/SPEC.md` —
now carry archive-induced unresolved-reference findings in the practitioner
harness (K-PROV-1 WARN, non-gating; observed 2026-07-24 via
`python3 tools/practitioner_harness/harness.py self-check` — WARN never
gates per D-GOV-02). Historical records are not edited to
match reality; the references were true when written and the cited content
is retained at `projects/pec/docs/.archive/`. This staleness is accepted as
permanent on those records.
