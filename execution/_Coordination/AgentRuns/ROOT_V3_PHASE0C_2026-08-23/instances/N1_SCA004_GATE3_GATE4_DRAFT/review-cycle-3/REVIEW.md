# Fresh Review — N1 SCA-004 Gate 3 / Gate 4 drafts, cycle 3

Verdict: `FAIL — ONE ACTIONABLE FINDING`

Review basis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`

Review posture: fresh independent, read-only, non-delegating Agent-2 review.
No N1 output was repaired or modified.

This review does not approve Gate 3, approve Gate 4, open Gate 5, amend live
decomposition truth, materialize a deliverable, lift a hold, or confer
implementation, pointer, App-loop, publication, release, commit, or merge
authority.

## Actionable finding

### N1-R3-F1 — MEDIUM — The exact working-surface candidate leaves OI-011 at the superseded 46-deliverable responsibility count

The Gate-3 candidate adds seven deliverables and correctly projects 53 total,
with all seven new register rows assigning `ResponsibleParty=Ryan Tufts`.
However, the candidate working surface retains this current-state row in §12:

```text
| OI-011 | ... | all 46 deliverables | `ResponsibleParty` is assigned to Ryan
Tufts across the accepted register and the SCA-001 carrier. | D-GOV-27 assigned
responsibility across the original 45 deliverables; SCA-001 carries that
existing assignment to DEL-02-06 ... |
```

That row is no longer concordant with the exact candidate it is part of. This
is not merely untouched historical evidence: SCA-001 deliberately advanced
OI-011 from the original 45-deliverable assignment to `all 46 deliverables`
and recorded DEL-02-06's carriage. The same live-working-surface convention
therefore requires this candidate to account for all 53 rows and the seven
SCA-004 additions. The current 89-check validator checks total topology and
new-row completeness but does not check the OI-011 affected count or
responsibility disposition, so its PASS does not close the inconsistency.

Bounded repair: update only the deterministic builder's OI-011 candidate edit
so the affected set is all 53 deliverables and the description/disposition
records that the seven SCA-004 candidate rows carry the existing Ryan Tufts
assignment. Add a semantic validator assertion for the 53-row responsibility
concordance, then regenerate the candidate working surface, exact diff,
preview/hash tables, validation JSON/check count, decision/handoff/return
claims, and every affected identity. Do not alter live decomposition truth,
the other six candidate surfaces except where deterministic identity evidence
requires it, or any Gate-4 substantive allocation.

## Prior-cycle findings — closure check

- `N1-R1-F1` remains closed. An independent all-row derivation found exact
  inverse consistency across all 6 package and 53 deliverable reverse rows,
  including the repaired OBJ-3/OBJ-4 omissions and PKG-04's E-2 consequence.
- `N1-R1-F2` remains closed. The exact candidate rows carry full G0 A3, A4,
  and A7 semantics, including role parity, labelled Agent-2/TASK fallback,
  instruction+config assertion, hard containment, the three command-network
  postures, explicit-user-act `acceptForSession`, grouping caveat, separately
  enumerated OpenAI service endpoints, exact-pin empirical proof, conditional
  `thread/resume`, fresh-thread fallback, and no in-flight re-attach claim.
- `N1-R1-F3` remains closed. `DerivativePackageState=INCOMPLETE` uses the
  fixed-state vocabulary.
- `N1-R2-F1` is closed. `Amendment_Actions.csv` exactly matches the current
  SCA-002/normative nine-column schema and supplies 8/8 evidence-supported
  `SupersessionBindingPresent=NO` dispositions for structural/allocation
  actions that supersede no admitted-authority fact.

## Independent checks that passed

- Every bound live decomposition/register/trace/telemetry SHA-256 and
  `execution/_ScopeChange/_LATEST.md` reproduces the Phase-0c basis.
- `Brief.md`, `Gate_1_Validation.md`, `Parsed_Actions.csv`,
  `WORK_GRAPH.json`, `DAG.md`, `Impact_Assessment.md`, and the Gate-1
  AUDIT_DECOMP coverage summary remain byte-identical to their protected
  bases.
- A fresh isolated deterministic build reproduced all seven candidate
  SHA-256 identities and `Gate_3_Exact_Amendment.diff` byte-for-byte.
- Applying the exact diff with `--unidiff-zero` to isolated bound-input copies
  reproduced every candidate byte exactly.
- An isolated execution of `validate_gate3_candidate.py` reproduced
  `PASS: 89 checks, 0 failures`, and the regenerated JSON was byte-identical
  to `Gate_3_Validation.json`.
- Independent full-register checks found 53 unique deliverables, 104 unique
  scope items, 7 supported objectives, 85 forward rows, 59 exact reverse
  units, zero unmapped IN rows, and zero dangling or asymmetric scope,
  objective, forward, or reverse relationships.
- Projected topology is correct: PKG-02=12, PKG-04=11, all other package
  counts unchanged, six packages total, and Context Envelopes S=14, M=38,
  L=1.
- The seven candidate IDs are collision-free and unmaterialized. Every new
  row has the prescribed parent, bounded artifact-kind type, M envelope,
  complete description/artifact/mapping fields, and non-authorizing write
  locus.
- DEL-02-06 retains SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, the
  standing integration/release-assurance role, and the unchanged accepted
  compatibility object containing exactly ten `HELD_UNAVAILABLE` bindings
  with null identities.
- DEL-04-11 is a PKG-04 `TEST_SUITE` mapped exactly to SOW-041, SOW-053, and
  OBJ-003 under the recorded cross-package coverage rule.
- R2-A is byte-verbatim in `Decision_Log.md`; Gate 3 and Gate 4 remain
  separately `PENDING_OWNER_APPROVAL`.
- The Gate-3 and Gate-4 questions are separate. The propagation plan includes
  all seven four-file PREPARATION INITs, the DEL-02-06 context edit list,
  dependency/estimate/schedule advisories, graph and audit reruns, a separate
  closure-validation lane, pointer quarantine, and stop rules.
- Candidate whitespace, `git diff --check`, literal diff apply-check,
  protected-byte fences, `_STATUS.md` protection, candidate-folder absence,
  and Gate-5 fences all pass.
- No live decomposition, companion register, pointer, `_STATUS.md`, package
  folder, SOW, dependency, estimate, schedule, runtime, tool, App, hold, pin,
  or Gate-5 surface changed. Concurrent N2 governance-harness work was outside
  this review and was not touched.

## Disposition

N1 is not ready for HELP_HUMAN fan-in because the exact candidate working
surface is internally stale at OI-011. Repair only N1-R3-F1, refresh the
affected deterministic evidence and identity claims, and submit the complete
package to a fresh independent review.
