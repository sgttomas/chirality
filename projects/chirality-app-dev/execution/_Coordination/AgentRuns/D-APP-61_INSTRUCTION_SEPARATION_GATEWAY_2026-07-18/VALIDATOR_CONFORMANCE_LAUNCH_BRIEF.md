# Sealed refutation brief — D-APP-61 validator conformance correction

**Status:** SEALED before verifier dispatch
**Parent:** app-dev loop operator
**Role:** independent read-only adversarial verifier
**Base:** `main` at `d3ad7fd2326dd32093aadf24ef32f0f8a9aff24a`
**Candidate:** `codex/d-app-61-validator-conformance-fix`

## Permission and return contract

Read the base, ruled D-APP-61 packet, candidate diff, validator, tests, run
record, and remote piping PR facts needed below. Run deterministic checks as
needed. Do not write, stage, commit, push, merge, or modify the piping checkout,
branch, or PR. Return exactly `COMMIT-SAFE` if every claim survives, or `BLOCK`
with specific counterevidence. Do not rely on the run record as proof.

## Claims to refute

1. D-APP-61 Appendix V does not authorize unconditional project-AGENTS
   requirements for `one package-scoped instance`, `terminal fan-out/fan-in`,
   or `supervised many-to-many`; removing them conforms the implementation to
   M5-A rather than creating a new policy choice.
2. The validator removes only those three requirements and retains the
   case-insensitive `software_workflow_profile.md` project-contract pointer.
3. A regression proves a thin piping-shaped project `AGENTS.md` can cite
   canonical runtime instructions without repeating the three phrases, while
   a separate regression proves omission of the software-profile pointer
   still fails.
4. Every pre-existing instruction-entrypoint test passes unchanged in meaning;
   tagged-launcher parity and D-APP-61 structural checks are unmodified.
5. The validator passes the entire current `main`-based candidate, including
   current piping state, and the prospective separated piping fixture passes
   while its launcher does not select HELP_HUMAN.
6. No byte under `projects/chirality-piping/**` differs from `main`; piping PR
   #269 remains held and is not advanced by this correction.
7. Writes are confined to the validator, its focused test, this run record,
   this sealed brief, the eventual verifier return, and one append-only app-dev
   receipt. No ruled packet, register, prior receipt, prior AgentRuns record,
   authority corpus, deliverable, or runtime source changes.
8. NM-6 truthfully records the failure mode and correction without claiming
   authority or editing an earlier near-miss.
9. The staged diff equals the authorized correction exactly, and no other byte
   differs from `main`.

## Required checks

- Inspect `git diff --cached --binary main`, name/status, and piping-path diff.
- Trace every changed validator condition to D-APP-61 Appendix V.
- Run the focused validator tests, live validator, app-dev receipt validator,
  corpus status, self-check, full practitioner-harness pytest, and
  `git diff --check`.
- Verify PR #269 state and remote head read-only. An unavailable required check
  is `BLOCK`, not an assumption.
