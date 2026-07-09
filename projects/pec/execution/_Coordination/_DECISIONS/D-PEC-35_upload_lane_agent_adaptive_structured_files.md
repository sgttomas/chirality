# D-PEC-35 - PROPOSAL: Upload lane - agent-adaptive structured files

**Status:** RULED 2026-07-09 (O-A with rider).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-35
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded upload-lane source and runbook tranche under the
> adopted reporting-first PEC workplan. Source execution remains prohibited
> unless and until the owner rules this packet. Sources govern on any
> disagreement.

## Why this row exists

The owner redirected the phase toward an effective reporting tool that can
begin by uploading documents that allow issues and status to be updated.
The standing plan narrows the previously postponed import lane: it reactivates
only as the proposal-gated D-PEC-08/D-PEC-22 pattern where the agent maps a
structured file, files an import proposal, and the human accepts/applies.

D-PEC-35 is the first reporting-first upload lane packet. It does not authorize
direct writes, force imports, or human-act substitution.

## Dependencies

D-PEC-35 depends on the landed D-PEC-08/D-PEC-22 proposal-shaped agent path and
benefits from D-PEC-26/D-PEC-38 Admin reporting foundation. Execution should
start from a base that includes the D-PEC-38 closeout. It does not require
D-PEC-30/31.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The server already exposes direct import, CSV export, sponsor brief, package pack, and import-proposal routes. | `server/src/api.ts:352-403` |
| The agent sidecar already has bounded proposal acts and refuses accept/apply/force paths. | `agent-sidecar/src/pec-client.ts:244-287`; `agent-sidecar/src/acts.ts:125-197` |
| The SDK/stub tool surface has `propose_csv`, `refresh_proposal`, `withdraw_proposal`, and proposal status. | `agent-sidecar/src/engine/sdk.ts:172-235` |
| The sidecar HTTP attachment contract is currently CSV-only. | `agent-sidecar/src/http.ts:94` |
| FILE_DROP_RUNBOOK requires agent map -> proposed import -> user approval, and forbids guesses for unmappable rows. | `execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md:36-70` |

## Decision to rule

Whether to authorize one source/runbook tranche implementing D-PEC-35:

1. Add an agent-facing structured-file intake path that accepts CSV/TSV/plain
   tabular text attachments and maps them to the existing §16/tracker import
   contracts. Rows/columns that cannot be mapped without inventing meaning
   become explicit questions or rejects with reasons.
2. Preserve proposal-gated apply: the agent may file, refresh, or withdraw its
   own import proposals; accept/apply/force remain human acts and are still
   refused by the sidecar before any server call.
3. Produce a mapping summary in the proposal context: detected source schema,
   selected target contract, field mapping, omitted fields, rejected rows, and
   confidence/basis notes. No direct database write occurs.
4. Update FILE_DROP_RUNBOOK / mapping guidance so arbitrary structured files
   are handled by the same proposal-before-approval flow.
5. Keep zero-new-runtime-dependency posture under O-A: no binary XLSX parser is
   added. XLSX workbooks must be converted to CSV/TSV/text outside the app or
   handled by an explicitly ruled O-B dependency/server upload route.
6. Add sidecar tests for mapping/refusal behavior, unknown schemas, proposal
   filing, no accept/apply/force, and stale proposal refresh behavior.

**Not in scope:** human accept/apply automation; direct writes; `force=true`;
new import contracts; D-PEC-14/15/19 reopening; binary workbook parsing under
O-A; new reporting documents; role assignment; professional/go-live claims.

## Fence (exact; STOP outside it)

O-A:

- `projects/pec/agent-sidecar/**`
- `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/**`

O-B may additionally open only if the ruling explicitly selects it:

- `projects/pec/server/src/api.ts`
- `projects/pec/server/src/services/proposals.ts`
- root/package manifest and lockfile rows needed for an explicitly named parser

No `core/**`, no database schema files, no tracked DB files, no profile, no
web pages, no unrelated runbooks, and no decision/register file edits during
execution except the post-run receipt.

## Options

- **O-A (recommended):** CSV/TSV/plain tabular agent-adaptive mapping, no new
  runtime dependency, proposal-gated only.
- **O-B:** O-A plus a named binary workbook parsing/upload approach. This must
  name any dependency or server route explicitly in the ruling.
- **O-C:** runbook-only clarification; no source change.
- **O-D:** defer D-PEC-35.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Sidecar tests: schema detection, target-contract selection, unmappable rows,
  mapping summary, proposal creation, refusal of accept/apply/force, stale
  proposal refresh/report behavior.
- If O-B touches server/upload routes: server tests for caps, content types,
  proposal creation only, and no apply.
- Browser/Admin smoke pass only for proposal visibility if O-A changes proposal
  payloads surfaced in the current UI; otherwise sidecar/API tests are the
  primary source verification.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: no direct import/write path, no guessed mapping, no
  accept/apply/force by the agent, and no new dependency under O-A.

## Rollback

Single revert of the source/runbook tranche commit(s). No schema/data rollback
is needed. Any proposals filed during scratch verification must use scratch DBs
only and must not be committed as tracked instance data.

## Human ruling

O-A affirmed 2026-07-09, with rider.

Build the CSV/TSV/plain tabular adaptive mapping lane as specified. This is an
interim lane: the owner's real recurring source files are XLSX workbooks, and
binary workbook/XLSX parsing is expected to return as a follow-on packet once
the owner provides the revised MDL and RAIL templates.

The follow-on packet must name its parsing approach and any dependency
explicitly for its own ruling. Do not design or begin binary workbook parsing
before the revised templates exist, because those templates define the target
columns and vocabulary, including status vocabulary, PE-attested percent
complete, and coverage dates.

Explicit exclusions for this packet: reporting periods/snapshots, percent
complete ingestion, first-class discipline view, `.docx` template conformance,
interfaces import contract, MDL-to-RAIL consistency checks in intake/triage,
and internal/client typing of needs. These await a workplan amendment and the
owner's revised templates; do not pre-build them and do not build against them.
