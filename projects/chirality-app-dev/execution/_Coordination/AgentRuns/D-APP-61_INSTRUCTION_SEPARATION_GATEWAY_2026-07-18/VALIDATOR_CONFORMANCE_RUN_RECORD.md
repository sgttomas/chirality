# D-APP-61 validator conformance correction

**Date:** 2026-07-18
**Operator:** Codex primary agent (runtime exposed no more-specific model
identifier)
**Base:** clean `origin/main` at PR #271 merge
`d3ad7fd2326dd32093aadf24ef32f0f8a9aff24a`
**Live direction:** “I won't need to tell the piping agent that if you just take
action accordingly and then provide them an updated response.”

## Requirement and bounded objective

D-APP-61 M5-A adopted Appendix V as the validator contract for app-dev and
piping. Appendix V retains tagged-launcher parity and replaces bare-vocabulary
requirements with structural duplication checks on HELP_HUMAN-selected loop
surfaces. It does not require project `AGENTS.md` files to repeat root runtime
doctrine.

When held piping PR #269 exercised the ruled cross-project integration, the
validator produced exactly three findings: piping's separated `AGENTS.md`
lacked `one package-scoped instance`, `terminal fan-out/fan-in`, and
`supervised many-to-many`. Those unconditional phrase requirements survived
from the pre-D-APP-61 validator even though Appendix V does not contain them.
The fourth existing project-AGENTS requirement,
`software_workflow_profile.md`, remains a valid project contract pointer and
is retained.

The authorized correction is therefore limited to:

1. remove only the three obsolete runtime-doctrine phrase requirements;
2. retain the software-workflow-profile reference requirement;
3. add regression coverage proving both properties;
4. independently refute the complete diff and stop at an owner merge gate.

No piping byte, ruled packet, register row, prior receipt, or prior AgentRuns
record may change. Piping PR #269 remains held until this correction lands.

## Predeclared validation criteria

- A thin project `AGENTS.md` that cites canonical runtime instructions and the
  software workflow profile passes without the three obsolete phrases.
- Omitting `software_workflow_profile.md` still fails.
- Every prior instruction-entrypoint regression passes.
- The validator passes the entire current repository.
- The prospective piping separated state is covered without changing piping.
- Receipt, corpus, self-check, full practitioner-harness pytest, diff hygiene,
  and CI pass.
- An independent read-only verifier returns `COMMIT-SAFE`; any `BLOCK` is
  remediated and requires a fresh verdict.

## NM-6 — Carry-forward fixture content concealed an obsolete requirement

**Near-miss:** The D-APP-61 implementation replaced vocabulary enforcement in
its ruled design, but the validator retained three unconditional project
`AGENTS.md` phrase checks. The focused tests carried those phrases in shared
fixture setup; no test independently asserted that the requirements belonged
to Appendix V. Current app-dev and pre-swap piping both passed, so the defect
became visible only when piping exercised its held separation change.

**Failed protection:** Verification established that the new structural
contract worked, but did not enumerate every surviving legacy check and trace
each one to the ruled validator contract.

**Standing correction:** For a governed validator replacement, enumerate all
surviving validations—not only newly added paths—and trace each to the ruled
contract. Shared fixture content is not evidence that a requirement remains
authorized. Cross-project prospective fixtures must represent each project's
lawful post-change shape.

This record is supersede-never-edit. If later evidence changes the analysis,
add a new near-miss record citing NM-6 rather than editing this section.

## Governance routing

- Validator and tests: deterministic enforcement derivatives of ruled
  D-APP-61 Appendix V; rerun on launcher, LOOP_INIT, newest-workplan, project
  AGENTS, or validator changes.
- This record, sealed brief, and verifier return: execution evidence, not new
  authority.
- NM-6: durable local near-miss evidence; it does not alter D-APP-60 or
  D-APP-61 authority.

## Evaluation and implementation reflection

The focused suite increased from 20 to 22 passing cases. The live validator
passes the entire current repository; the exact prospective piping separation
also passes once its ruled launcher-parity swap is applied. Receipt validation,
corpus v9 status, the unchanged self-check baseline, 266 practitioner-harness
tests, and diff hygiene pass. No piping byte changed.

The independent verifier returned `COMMIT-SAFE`; its terminal return is
persisted verbatim in `VALIDATOR_CONFORMANCE_RETURN_COMMIT_SAFE.md`. The
post-verdict recording delta is limited to that return, this outcome section,
and append-only Receipt-64. The recording-only recheck also returned
`COMMIT-SAFE`; its verbatim return is persisted in
`VALIDATOR_CONFORMANCE_RETURN_COMMIT_SAFE_2.md`. This deterministic final fill
does not alter the implementation delta.
