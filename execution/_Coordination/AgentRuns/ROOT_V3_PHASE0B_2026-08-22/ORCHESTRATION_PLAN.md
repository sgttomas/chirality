# Orchestration Plan — Root v3 Phase 0b

PlanVersion: `1`
RunID: `ROOT_V3_PHASE0B_2026-08-22`
SelectionAuthority: `HUMAN`
Posture: `MIXED`
SupervisingRole: `HELP_HUMAN`
AcceptedBasis: `origin/main@b143444bd497eae1b1b638670a33e6df756d9084`
OwnerSteerSHA256: `c4b674327b78434561a42f93b8bb34e50921281459ec00ca6c8afaaa9ebb80e2`
R1RecordSHA256: `a9879a87faaeb4cd4d5f16b2b4b0364543dff117e1b51c7e17d1efdcb20f377d`

## Objective and authority

Execute exactly the three owner-selected nodes in
`plans/steers/chirality_app_v3_phase0b_steer_root_2026-08-22.md`, applying
the owner rulings in
`plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`.
The basis gate and idle-workplan Step 0 passed before this plan was written.

## Work graph

| Node | Lane | Content ownership | Dependency | Expected return | Fan-in gate |
|---|---|---|---|---|---|
| N1 | HELPS_HUMANS / CHANGE integration | Exact N1 paths in the steer | basis only | D-GOV-35 record, exact instruction application, manifest, notices, evidence | fresh independent review PASS; all N1 checks PASS |
| N2 | SCOPE_CHANGE | `execution/_ScopeChange/SCA-004_2026-08-22_1749/**` only | owner R1-C; semantic acknowledgement that D-GOV-35 is ruled | Gate-2 impact assessment and four-state handoff | fresh independent review PASS; protected bytes unchanged |
| N3 | TASK_MANAGEMENT | exact ruling/register/archive-if-required/Root-handoff paths in steer | owner R1-D; N1 decision-record path | two dispositions, reconciled register/archive/counts | fresh independent review PASS; exactly two basis rows disposed |

N1, N2, and N3 may author concurrently because their content write sets are
disjoint. Each instance owns only its own control-plane subfolder. Git commits
are serialized by CHANGE in dependency order N1, then N2, then N3. Receipt 115,
run-level final handoff, validation evidence, push, and PR creation occur only
after all three reviewed commits fan in.

## Human gates and stops

No write-set widening, sync/rebase, merge, Gate 3, hold lift, pin change,
artifact download, App implementation/adoption, lifecycle, release, export,
or reliance act is authorized. If `origin/main` advances, stop and request
owner sync authorization. Publication is one human-gated PR; self-merge is
false.

## Closure contract

Accept only validated manager returns and fresh zero-actionable-finding node
reviews. Preserve every failed review and repair cycle. Final closeout must
append Receipt 115 with the two verbatim CHAT_TRANSCRIPTION blocks, record all
hashes/commits/check outputs and reconciled counts, emit a run handoff, use
CHANGE for routine commit/push/PR closeout, and stop without merge.
