# Fresh Review — N1 SCA-004 Gate 3 / Gate 4 drafts, cycle 1

Verdict: `FAIL — THREE ACTIONABLE FINDINGS`

Review basis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`

Review posture: fresh independent, read-only, non-delegating Agent-2 review.
No N1 output was repaired or modified.

This review does not approve Gate 3, approve Gate 4, open Gate 5, amend live
decomposition truth, materialize a deliverable, lift a hold, or confer
implementation, pointer, App-loop, publication, release, or merge authority.

## Actionable findings

### N1-R1-F1 — HIGH — The candidate reverse trace is not consistent with the candidate objective/forward registers

The Gate-3 contract requires recomputed forward and reverse trace files and
requires the two directions to be consistent with the candidate registers.
The candidate telemetry also says that reverse trace resolves through both
scope items and `SupportsObjectives` and that both directions are computed,
not asserted.

An independent full-register inverse comparison found four candidate
deliverable rows whose `PRDItems` omit an objective carried by the candidate
deliverable/objective/forward truth:

| Candidate reverse row | Required objective PRD item that is absent |
|---|---|
| `DEL-01-04_Human_Authority_and_Three_Judgment_Gate_Model` | `OBJ-3` |
| `DEL-03-01_Path_Model_and_ScopePath_Containment_Conformance` | `OBJ-4` |
| `DEL-03-06_Root_Materialization_Readiness_and_Deliverable_Stream` | `OBJ-4` |
| `DEL-06-04_Downward_Variant_Service_and_Non_Weakening` | `OBJ-4` |

For example, candidate forward rows `OBJ-3` and `OBJ-4` name those
deliverables, while candidate reverse lines 11, 22, 27, and 49 omit the
corresponding objective item. These omissions existed in the bound reverse
register, but the reverse file is classified as `RECOMPUTE`; carrying the
stale omissions into the exact candidate does not satisfy the required
candidate consistency check.

The validator masks the defect: it affirmatively requires all existing
reverse rows to remain unchanged (`existing_reverse_rows_unchanged`) and then
checks exact PRD/scope content only for the seven new rows. It never compares
every candidate deliverable reverse row to the candidate scope and objective
registers / forward trace. Consequently, `Gate_3_Validation.json` cannot
truthfully remain `PASS`, 76 checks, 0 failures.

Bounded repair: deterministically recompute every deliverable reverse row
from the candidate scope and objective/forward truth; repair the four omitted
objective items; replace the validator's unchanged-existing-row assertion
with a full candidate inverse-consistency check; then regenerate the exact
candidate, full diff, preview, validation JSON, hashes, return, and handoff.
No new SCA action or live write is needed because reverse trace is already a
declared `RECOMPUTE` derivative in this exact candidate.

### N1-R1-F2 — HIGH — The exact candidate does not fully carry the accepted G0 A3/A7 semantics it claims are explicit

R2-A accepts Gate 2 including G0 A3/A4/A7 carriage. The accepted
`Impact_Assessment.md` makes those amendments controlling inputs to every
later exact carrier and specifically assigns A3 to DEL-02-07/09/10/12 and A7
to DEL-02-08/09/10/12. `Handoff_State.md` then claims that G0 A3/A4/A7 are
"explicit in the candidate rows."

A4 is explicit and complete in DEL-02-11. A3 and A7 are not:

- The new candidate rows contain no exact A3 parity rule that Agent 0/1/2
  role entry is always offered, no explicit Agent 2/TASK fallback labelled
  `role not mechanically enforced`, and no statement that delegated-harness-
  native K-SUBAGENT non-delegation is instruction+config asserted rather than
  mechanism-proven. DEL-02-12 contains only the more general phrase
  `instruction-asserted versus mechanism-proven evidence labels`.
- The A7 fragments cover enumerated service endpoints, three posture labels,
  prompt routing, and a generic grouping caveat, but the exact candidate rows
  omit `acceptForSession` being allowed only by explicit user act. They also
  do not bind the complete no-command-network default / visible host and
  protocol / same-destination queued-request caveat / exact-pin empirical
  proof set across the named A7 carriers.

The accepted Gate-2 prose remains evidence, but it is not one of the seven
candidate live surfaces. Approving the present Gate-3 bytes would therefore
not make the claimed complete A3/A7 carrier semantics part of the exact
decomposition candidate.

Bounded repair: add the controlling A3 and A7 semantics to the appropriate
new deliverable descriptions, anticipated artifacts, and/or Context Envelope
notes in the deterministic builder and candidate register; add semantic
validator checks for the exact required controls; correct any overclaim in
the preview/handoff; then regenerate all candidate identities, the full diff,
validation JSON, return, and handoff. Preserve A4, the hard-containment
boundary, all ten holds, and the no-live-write posture.

### N1-R1-F3 — MEDIUM — `DerivativePackageState` uses a value forbidden by the SCOPE_CHANGE fixed-state schema

`AGENT_SCOPE_CHANGE.md` declares the only allowed `DerivativePackageState`
values as `INCOMPLETE` or `COMPLETE`. `Handoff_State.md` instead records
`CURRENT_CANDIDATE_FOR_BOUND_REVISION_1_2` in that fixed field. The descriptive
four-state table may use richer prose, but the fixed state field must use its
closed vocabulary.

Bounded repair: set the fixed `DerivativePackageState` to `INCOMPLETE` while
owner Gate-3/Gate-4 approval is pending, retaining
`CURRENT_CANDIDATE_FOR_BOUND_REVISION_1_2` as explanatory prose if useful.
Recompute the handoff and return hashes.

## Independent checks that passed

- Every bound live decomposition/register/trace/telemetry SHA-256 and
  `execution/_ScopeChange/_LATEST.md` reproduces the Phase-0c basis.
- `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`,
  `WORK_GRAPH.json`, `DAG.md`, `Impact_Assessment.md`, and the Gate-1
  AUDIT_DECOMP coverage summary remain byte-identical to basis.
- A fresh deterministic build in an isolated temporary root reproduced all
  seven candidate SHA-256 identities and the exact-diff SHA byte-for-byte.
- Applying `Gate_3_Exact_Amendment.diff` with `--unidiff-zero` to an isolated
  copy of the seven live basis files reproduced every candidate byte exactly.
- The seven new IDs are collision-free and unmaterialized. All are parented
  to PKG-02 or PKG-04, have complete row fields, `M` Context Envelopes,
  bounded artifact-kind types, and declared anticipated write loci.
- Projected topology is internally correct: 53 deliverables; PKG-02=12;
  PKG-04=11; six packages; 104 scope items; seven objectives; S=14, M=38,
  L=1; zero unmapped IN scope rows; zero unsupported objectives.
- DEL-02-06 retains SOW-104, OBJ-001/002/004/007, REQ-027, its standing
  integration/release-assurance role, and the ten-binding hold boundary.
- DEL-04-11 is a PKG-04 `TEST_SUITE` mapped exactly to SOW-041, SOW-053, and
  OBJ-003; DEC-010 supports the cross-package SOW-053 coverage mapping.
- Candidate scope and objective mappings are bidirectionally symmetric with
  their authoritative registers; all new forward/reverse rows are present;
  candidate telemetry counts match the candidate registers.
- R2-A is reproduced verbatim in `Decision_Log.md`, and Gate 3 / Gate 4 are
  separately `PENDING_OWNER_APPROVAL`.
- The Gate-3 question and separate Gate-4 question are present. The
  propagation plan includes the seven folder paths and four-file
  PREPARATION posture, DEL-02-06 context edit list, dependency/estimate/
  schedule advisories, graph and audit reruns, a separate closure-validation
  lane, pointer quarantine, and stop rules.
- No live decomposition, pointer, `_STATUS.md`, package/deliverable folder,
  runtime, tool, App, hold, pin, or Gate-5 surface changed. Concurrent N2
  governance-harness work was outside this review and was not touched.

## Disposition

N1 is not ready for HELP_HUMAN fan-in. Repair only the bounded findings
above, regenerate every derived candidate identity and evidence claim, and
submit the complete repaired N1 package to a fresh independent review.
