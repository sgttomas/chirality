# D-PEC-37 - PROPOSAL: User-defined reports

**Status:** RULED 2026-07-09 (O-A; execution gated on D-PEC-36).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-37
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded user-defined reporting tranche under the adopted
> reporting-first PEC workplan. Source execution remains prohibited unless and
> until the owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner asked for novel user-defined reports in addition to standard reports.
D-PEC-37 lets the agent compose a report from a user prompt using the bounded
read-act surface and the standard-report conventions from D-PEC-36. It keeps
the factual-or-absent rule: if records do not support a requested figure, the
agent says so instead of synthesizing it.

## Dependencies

D-PEC-37 depends on D-PEC-36 being ruled and executed first, because D-PEC-36
establishes report basis pointers, output shape, standard report tests, and
the sidecar report-read convention. It also relies on D-PEC-21's agentic turn
loop and the existing bounded read-act profile. If a ruling authorizes D-PEC-37
before D-PEC-36 lands, execution must still wait for D-PEC-36.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| The sidecar SDK engine already has a bounded tool set with read acts and report reads. | `agent-sidecar/src/engine/sdk.ts:172-267` |
| Unknown report names are refused rather than guessed. | `agent-sidecar/src/acts.ts:357-374`; tests in `agent-sidecar/test/access-basis.test.ts` |
| Boundary pins refuse forbidden human acts and force import paths before server calls. | `agent-sidecar/src/pec-client.ts:110-196` |
| REPORT_BASIS requires an answer about project state to cite records, views, or report bases and to say when the record set does not support a claim. | `execution/_Coordination/REPORT_BASIS.md:55-56` |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-37:

1. Add a user-defined report mode to the agent turn surface: the human supplies
   a report request, the agent plans required read acts, reads only through the
   bounded PEC client, then returns an exported report artifact/payload.
2. Reuse D-PEC-36 report conventions: basis pointers, contributing refs where
   available, factual-or-absent statements, visibility/redaction preserved, and
   explicit unsupported-request notes.
3. Add guardrails for prompt-driven reporting: refuse professional opinions,
   go-live/issuance claims, unsupported forecasts, hidden data requests,
   direct mutations, and export formats outside the ruled egress basis.
4. Add tests for prompt-to-report routing, unsupported claim refusal, basis
   citation, unknown/unsupported data requests, no mutation, and multi-turn
   follow-up behavior.
5. Keep in-app report editing/viewing out under O-A; the report is generated
   by the sidecar/report lane and can be displayed or saved by the existing
   app surfaces only where already supported.

**Not in scope:** new server mutations; direct database queries by the agent;
new data visibility; report approval/workflow; in-app report editor under O-A;
new export-egress route unless explicitly ruled; new dependencies; replacing
standard reports.

## Fence (exact; STOP outside it)

O-A:

- `projects/pec/agent-sidecar/**`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`

O-B may additionally open only if the ruling explicitly selects an in-app
viewing/export surface:

- named files under `projects/pec/web/src/**`
- named read-only report route files under `projects/pec/server/src/**`

No `core/**`, no database schema/files, no import templates, no root manifests
or dependencies, no profile, and no decision/register file edits during
execution except the post-run receipt.

## Options

- **O-A (recommended):** sidecar user-defined report mode over bounded reads,
  D-PEC-36 conventions, no new web/editor surface.
- **O-B:** O-A plus a named in-app generated-report viewer/export surface.
- **O-C:** guardrail/runbook design only; no source change.
- **O-D:** defer D-PEC-37.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Sidecar tests for report prompt routing, read-act planning, basis citation,
  unsupported claim refusal, unknown data request handling, no mutations, and
  multi-turn follow-up.
- If O-B adds web/server surfaces: visual pass at desktop and narrow viewports,
  keyboard operability, no overflow, and server tests for read-only report
  retrieval.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: no unsupported project status claim, no professional
  opinion/issuance/go-live claim, no data visibility expansion, no mutation.

## Rollback

Single revert of the source/report-basis tranche commit(s). No schema, data,
dependency, or runtime rollback is needed.

## Human ruling

O-A affirmed 2026-07-09.

Execution remains gated on D-PEC-36, as the packet already states. D-PEC-37
must reuse the D-PEC-36 conventions after they land.

O-B is rejected for now. Do not add an in-app viewer/export surface: under the
PE/PD operating model, reports are drafted by the sidecar, vetted by the PE,
then edited and issued outside the app. A viewer may return as its own later
packet.
