# Agent-Index Re-disposition Handoff State

Status: `AGENT-INDEX-REDISPOSITION_PR0_DRAFTED_AWAITING_OWNER_RULING`
Run: `AGENT-INDEX-REDISPOSITION-20260721`

## Current status

PR-0 is drafted. The D-GOV-18 decision record exists as
`docs/governance_harness/_DECISIONS/D-GOV-18_agent_index_redisposition.md` with
Status `PROPOSED — AWAITING OWNER RULING`; the register carries one PROPOSED
row; the disposition matrix ORCHESTRATOR and EVALUATION rows are annotated as
superseded-on-ruling and the CHANGE row notes the D-GOV-18 slim tranche. No
role file, validator, skill, or lifecycle state has changed. No owner ruling,
approval, or SHA-binding has been recorded or fabricated.

## Accepted upstream state

- `main@0c066652cd527eb1559f715e914262d2bda42602` (synchronized integration
  basis at run start).
- Framing record D-GOV-11 (runtime role ownership; Agent-2 construction forms).

## Derivative-package status

This run produces the D-GOV-18 governance record (authoritative-on-ruling) plus
navigational annotations (register row, matrix annotations). The register and
matrix annotations are derivative navigational surfaces citing the D-GOV-18
record; on any disagreement the decision record governs.

## Closure verdict

PR-0 is not closed. Files were written, but closure requires the owner's
verbatim ruling and its SHA-binding. Until then the record is PROPOSED and no
downstream PR (PR-1..PR-4) may execute.

## Blockers

- **Owner ruling of D-GOV-18** (primary blocker). No item has operative effect
  before it. The owner supplies a signable sentence of the form
  "I APPROVE D-GOV-18 items 1–8 at commit <SHA-TBD>." Ruling SHA: TBD.
- **PR-2 additionally blocked** by closure of the App Dev in-flight EVALUATION
  fan-in.

## Coordination handoff notice (to the App Dev project loop)

Per D-GOV-18 Item 6, the App Dev couplings to the ORCHESTRATOR name are
deferred to the App Dev project loop by owner consent:
`projects/chirality-app-dev/frontend/src/lib/shell/persona-resolution.ts:36`
(`ORCHESTRATE → 'ORCHESTRATOR'`), its Jest expectation at
`projects/chirality-app-dev/frontend/src/__tests__/lib/persona-resolution.test.ts:24`,
and App Dev `AGENTS.md` wording. Verified no root-PR CI breakage under the PR-3
rename: the root rename touches no app-dev source, and app-dev tests run under
the app-dev loop. The App Dev loop owns whether and when to carry the rename
through its own instruments.

## Rerun requirements

- If the accepted basis (`main@0c066652cd…`) changes before the owner rules,
  re-derive the D-GOV-18 `AcceptedBasis` line and re-verify the cited file/line
  references before publishing the ruling.
- On ruling, CHANGE publishes and SHA-binds; the Ruling SHA backfills into the
  D-GOV-18 record, the register row, and this handoff.
- Any validator or evidence surface whose basis changes before PR-1..PR-4
  executes must be rerun.

## Recorded follow-on candidates (not in this run)

- AUDIT_DECOMP undeclared-caller hygiene (REVIEW / SCOPE_CHANGE frontmatter).
- `tools/decomp/propose_gate4_kty.py` old-name (`ORCHESTRATOR`) seeds.
- Optional one-line historical note in `agents/AGENT_REVIEW.md` on the
  legacy `_Reconciliation/Reviews/` piping.
