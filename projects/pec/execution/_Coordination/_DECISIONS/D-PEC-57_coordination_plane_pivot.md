# D-PEC-57 — RULED: pivot PEC to the Chirality coordination plane

**Status:** RULED 2026-07-24 (O-A) — owner direction act; documentation-only fence
**Decision ID:** D-PEC-57
**FramedBy:** agent (Claude Fable 5), from owner-directed brainstorm, session 2026-07-24
**Structure precedent:** `D-PEC-54`/`D-PEC-55` (direction → candidate → adoption two-step); options form per `D-PEC-49`

## Context and owner direction under framing

Owner direction from the 2026-07-24 session, recorded in summary by the
framing agent — NOT A VERBATIM TRANSCRIPT (EVIDENCE, NOT RULING; the only
verbatim owner quotation in this packet is in the Human ruling section):

> PEC should morph into the core agentic workflow coordination substrate for
> Chirality — deterministic tooling, data arriving from workflow/agent events,
> the existing pages repurposed as dashboards/analytics. As a human-used
> project-management tool it has no interest. It should embody Step 0 and the
> deterministic parts of Step 1 of the canonical loop; polling is determined
> by the harness, not agent behaviour; ruling capture remains file-native; it
> does not subsume the practitioner harness; it is "the coordination plane
> that doesn't need to exist." Old PEC is superseded wholesale; v2 is a
> greenfield build through the governed pipeline with old PEC as a cited
> reference corpus.

The candidate product definition embodying this direction is
`projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md`.

Honest supersession rationale, for the register: PRD v1.0 (`D-PEC-55`,
2026-07-10) was adopted but never piloted; none of its §20 open decisions was
answered. The understood user changed — from a multidiscipline human team to
the owner plus an agent fleet across concurrent sessions. This packet
supersedes an untested adoption, not validated learning.

## Decision to make

Whether to (1) adopt the coordination-plane product direction, retiring the
team-information-hub framing; (2) route PRD v2 through candidate review to a
`D-PEC-58` adoption act; (3) replace the standing workplan upon adoption; and
(4) close legacy row `D-PEC-49` as moot.

## Options

- **O-A (recommended):** Adopt the direction as framed. PRD v2 candidate
  proceeds to owner review; adoption itself is a separate `D-PEC-58` act
  (two-step, per the D-PEC-54/55 precedent). Upon D-PEC-58:
  the standing plan `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md`
  is superseded by a new date-stamped workplan; `D-PEC-49` is closed as moot
  (its subject matter belongs to the retired product); the v2 build proceeds
  greenfield through SOFTWARE_DECOMP → PROJECT_SETUP → WORKING_ITEMS under
  per-tranche packets; old PEC is frozen as a cited reference corpus per the
  PRD's §13 disposition.
- **O-B:** Adopt the direction but amend PRD v1.0 rather than supersede it.
  Not recommended: the §2/§14 analysis shows the information contract,
  capture surfaces, roles, integrations, metrics, and release strategy of
  v1.0 do not survive — that is past an amendment.
- **O-C:** Defer; keep the T0 rebaseline against PRD v1.0 as next gate.
- **O-D:** Reject the pivot; PEC continues as the team information hub.

## Recommendation (non-binding)

O-A. Compliance posture is designed in rather than sought by exception: the
record tier is `D-GOV-01` Option A's rebuildable projection, and Option A's
adjacent constraints ("no coordinator process, no leases, no database-owned
status") are addressed head-on in PRD v2 §15, with the presence-tier
"coordinator process" question expressly reserved for the owner at D-PEC-58;
no second execution loop is created (`D-GOV-20`; D-PEC-56's no-dual-loop
boundary and human-only-act restrictions survive, while its adapter-retention
behavior is partially superseded at D-PEC-58, declared there); rulings remain
file-native (K-AUTH-1). The practitioner harness's cache half remains closed
by its own record (query-pain precondition measured unmet 2026-07-02); this
row directs the PEC product, not the harness.

## Exact fence (this packet, if ruled O-A)

- `projects/pec/execution/_Coordination/PRD_V2_CANDIDATE_2026-07-24_coordination_plane.md` (authored under this row; thereafter status fields and review-outcome corrections only)
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-57_coordination_plane_pivot.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md` (packet preparation only; unruled)
- `projects/pec/execution/_Coordination/WORKPLAN_CANDIDATE_2026-07-24_pec_coordination_plane.md` (candidate only; does not replace the standing plan)
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

No runtime source, dependency, database, demo input, report, `docs/**`
surface, the standing workplan
(`_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md`),
profile, or external system change is authorized by this row. PRD v2 adoption, workplan replacement, `docs/PRD.md` replacement,
decomposition, and all implementation writes require their own packets
(`D-PEC-58` onward).

## Verification and rollback

- Verify the candidate PRD file exists at the path above and its header still
  reads CANDIDATE (this row does not adopt it).
- Verify `D-GOV-01`, `D-GOV-20`, `D-PEC-55`, `D-PEC-56` are cited accurately
  (compliance-by-design claims in PRD §15).
- Reversal is an owner act on a new successor row (residual-work convention,
  `_REGISTER.md`); a ruled row is not reopened or annotated. The candidate
  PRD remains on disk as an unadopted artifact with no force until D-PEC-58.

## Human ruling

**RULED O-A (2026-07-24).** Owner direction of record (Ryan Tufts, in-session,
2026-07-24):

> "I rule D-PEC-57 O-A, commit and proceed to D-PEC-58 using subagents where
> effective and using the `opus-5` model when doing so."

The coordination-plane direction is adopted as framed. The PRD v2 candidate
proceeds to the `D-PEC-58` adoption gate; adoption of the PRD text itself
remains a distinct owner act on that row. Preparation of the D-PEC-58 packet
and its staged execution artifacts (candidate replacement workplan, document
notices) is authorized within this row's documentation-only posture; no
D-PEC-58-fenced surface is written until D-PEC-58 is ruled.
