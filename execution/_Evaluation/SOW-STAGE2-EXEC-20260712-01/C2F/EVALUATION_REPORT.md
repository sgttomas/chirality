# C2F Independent Consumer Evaluation Report

Verdict: `BLOCKED`
Gate disposition: `C2G_NOT_ELIGIBLE`
Scoring: none

## Outcome

The candidate is exactly contained, fully inventoried, current-hash-bound, and
green on the recorded and targeted mechanical checks. It nevertheless fails
the mandatory content/authority gate: root and App dual-format resolvers accept
a merely syntactic, self-matching D-GOV-16 token without proving it is the
accepted ruling. The root ISSUED converter also omits the required accepted-
basis binding. These are fail-closed blockers and cannot be averaged against
the green test totals.

The root C2A return pointer is additionally incomplete: project-local C2A is
terminal PASS, while the root instance remains READY and names a missing
return. C2G must remain parked.

## Basis, method, and coverage

The basis and method are frozen in `EVALUATION_PROTOCOL.md`; exact diagnostic
results are in `reports/DIAGNOSTICS.md`. Coverage includes D-GOV-16, the
accepted Stage-2 plan/graph, P0 and P1 handoffs, all 64 exact caller rows, all
nine App callers, both source diffs and manifests, C2R/C2A returns, child and
fallback evidence, normalized test evidence, current source hashes, and
targeted independent reruns.

No subject, Git, deliverable, control, lifecycle, receipt, release, H1/H2, or
snapshot state was modified by this evaluation.

## Question results

| Question | Result | Evidence |
|---|---|---|
| 64 exact callers and nine App callers classified | PASS | P0/C2R surface sets are identical at 64; App is a 9-row subset; no unknown row |
| exact contained and disjoint source changes | PASS | 48 root + 4 App paths; intersection 0; diff gaps 0; post-hash mismatches 0; forbidden paths 0 |
| success and fail-closed behavior proven | BLOCKED | SOW-only, legacy-only, missing, partial, invalid, and ordinary ambiguous cases pass; syntactically valid but unruled authority is accepted as `MIGRATION_DUAL` |
| current required checks green | PASS_WITH_RESOLVED_SUBSTRATE_EVENTS | targeted current checks pass; expensive current-hash-bound root/App/build/self-check/practitioner/owned-server evidence is green |
| issues separated by class | PASS | schema, content/authority, preservation, and substrate are reported separately below |

## Classified outcomes

### Schema/mechanical

`BLOCKED` only for the stale/missing root C2A return pointer
(`EVAL-C2F-003`). The caller manifests, changed-path manifests, source hashes,
tests, agent/skill validators, export profile, build/typecheck, and check
schemas otherwise pass.

### Content/authority

`BLOCKED`:

1. `EVAL-C2F-001` — unauthorized dual is not fail-closed. Both lanes accept
   synthetic `D-GOV-16@0123456` when it is self-bound and the isolation/path
   flags are present. The accepted ruling is
   `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.
2. `EVAL-C2F-002` — ISSUED preparation has no accepted-basis input or emitted
   binding despite the ratified and skill contracts.

The App review's earlier `INVALID`/`valid: true` bug was a real content defect,
was repaired, and is now covered by the 70-test focused rerun. The absence of a
direct DocumentView component regression is retained as low non-blocking risk
`EVAL-C2F-004`.

### Preservation/containment

`PASS`. All 52 changed source paths are exact manifest members, root and App
are disjoint, live hashes equal their post hashes, canon is unchanged, and no
governed deliverable/control/status/lifecycle/receipt/release path is touched.

### Execution substrate

`RESOLVED_SUBSTRATE_FALLBACK`, not a content PASS substitute. Preserved events
include the root TOOL-CORE interruption, C2A implementation duration fallback,
the correction-only review rerun stall, and the first App premerge attempt
without a loopback listener. Each has later bounded evidence; the owned-server
premerge rerun passes 8/8 plus 16/16 report-only. The root initial full-suite
import collision was a candidate integration defect, not substrate; it was
repaired and the current-hash-bound full root suite passed 788 tests.

## Validated return inventory

- C2R manager return/status: terminal PASS; artifacts and 64-row manifest
  valid, but its authority claim is contradicted by direct code/test evidence.
- C2A project-local manager return/status: terminal PASS; package artifacts,
  9-row manifest, independent review, repair backcheck, and registered checks
  present, but its authority claim is contradicted by direct code/test
  evidence.
- C2A root pointer: invalid/incomplete (`READY`, missing declared return).

Producer PASS labels are preserved as produced; they are not silently repaired
or promoted through fan-in.

## Decision queue and reruns

No human authority expansion is required to correct these candidates inside
their already accepted consumer-activation objective. Route repair to
HELPS_HUMANS for root tools and App WORKING_ITEMS for runtime/tests, with one
frozen accepted-authority source shared by both implementations. WORKING_ITEMS
must also complete its root terminal return pointer.

After repair:

1. add negative tests proving a syntactically valid unruled D-GOV-16 hash is
   refused in root and App;
2. require and emit the ISSUED accepted-basis binding, with missing/wrong-basis
   negative tests;
3. rerun affected root/App focused and full checks, exports, typecheck, build,
   self-check, practitioner, and owned-server premerge evidence;
4. regenerate exact manifests/hashes and terminal returns; and
5. rerun independent C2F. C2G remains parked until all C2F lanes pass.
