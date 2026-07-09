# D-PEC-36 - PROPOSAL: Standard report set

**Status:** RULED 2026-07-09 (O-A with rider).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-36
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded standard-report source tranche under the adopted
> reporting-first PEC workplan. Source execution remains prohibited unless and
> until the owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner asked for standard reports and novel user-defined reports, both
drill-backed and based only on recorded facts. D-PEC-36 is the standard-report
lane: weekly project status, package issue summary, and deliverable
completeness/MDL status. It names bases by pointer and composes exported
documents from server-computed data; it does not invent status or become a
planning/scheduling platform.

## Dependencies

D-PEC-36 depends on the drill spine and reporting foundation (D-PEC-25,
D-PEC-27, D-PEC-29, D-PEC-38). D-PEC-35 is not a hard dependency. D-PEC-37
depends on D-PEC-36 because user-defined reports should reuse the conventions
and guardrails established here.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| Server report endpoints currently include sponsor brief and package pack. | `server/src/api.ts:365-370`; `server/src/reports/` |
| The agent sidecar can read reports named `sponsor-brief` and `package-pack`. | `agent-sidecar/src/acts.ts:357-374`; `agent-sidecar/src/pec-client.ts:367-372` |
| REPORT_BASIS requires reported figures to name their server-computed basis by pointer and says absent record support must be stated as absent. | `execution/_Coordination/REPORT_BASIS.md:1-56` |
| The D-PEC-38 branch makes package issue mix and log summary data closer to Explain-shaped report inputs. | `server/src/services/views.ts:252-713` |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-36:

1. Define and implement a standard report set:
   - weekly project status, based on `overviewView`, Log summary, and package
     rollups, with payload support for grouping by discipline as well as by
     package;
   - package issue summary, based on `packageDetailView.issues[]`,
     `packagesView.issueMix`, and `logSummaryView`;
   - deliverable completeness / MDL status, based on `deliverablesView`,
     deliverable detail facts/open items, and package context.
2. Each report payload and exported document names its basis by pointer:
   route/view/function, rule id where applicable, and contributing refs where
   available. Unsupported figures are omitted and called out as absent.
3. Add sidecar read/report support for the new standard report names, with
   refusal for unknown report names and no mutation.
4. Preserve data-residency/egress basis: generated report contents must stay
   inside the ruled OPEN_ENUMERATED profile basis and contain no committed
   real-row evidence beyond permitted summary/export behavior.
5. Add tests for report shape, basis pointers, unknown report refusal,
   factual-or-absent behavior, and no mutation.

**Not in scope:** user-defined prompt reports (D-PEC-37); in-app report editor;
new charting/PDF/docx dependencies; importing/uploading; professional
certification; claims not supported by server records; `.docx` generation;
percent-complete ingestion; reporting period/snapshot semantics.

## Fence (exact; STOP outside it)

- `projects/pec/server/src/reports/**`
- `projects/pec/server/src/api.ts`
- `projects/pec/server/src/services/views.ts` only for read-only report payload
  helpers required by the standard reports
- `projects/pec/agent-sidecar/**`
- tests under `projects/pec/server/test/**` and `projects/pec/agent-sidecar/test/**`
- `projects/pec/execution/_Coordination/REPORT_BASIS.md`

No `core/**` unless a ruled implementation proves an existing type export is
strictly necessary; no database schema/files; no web pages under O-A; no root
manifests or dependencies; no profile; no decision/register file edits during
execution except the post-run receipt.

## Options

- **O-A (recommended):** server JSON/Markdown-style standard report payloads
  plus sidecar read support; no new dependencies and no web editor.
- **O-B:** O-A plus a small web Reports index that links/downloads the standard
  report outputs. This explicitly opens the named web files in the ruling.
- **O-C:** report-basis/runbook design only; no source change.
- **O-D:** defer D-PEC-36.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server tests for each standard report: payload shape, basis pointers, no
  invented values, unsupported/absent figures called out, redaction/visibility
  preserved.
- Sidecar tests for new report names, unknown report refusal, broad/enumerated
  read-basis behavior, and no mutation.
- Browser visual pass only if O-B adds web report surfaces; otherwise report
  payload and sidecar tests are the primary verification.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: every report figure has a basis pointer or is absent;
  no professional/go-live/forecast claim is invented.

## Rollback

Single revert of the source/report-basis tranche commit(s). No schema, data,
dependency, or runtime rollback is needed.

## Human ruling

O-A affirmed 2026-07-09, with rider.

Build the standard report machinery and the three named reports. The weekly
project status report payload must support grouping by discipline as well as by
package. Rationale: the owner's actual recurring weekly report is
discipline-oriented, the deliverable discipline field already exists, and
supporting this grouping now prevents the report foundation from hardening
around package as the only axis.

O-B is rejected for now. Do not add a web Reports index or in-app report
viewer/editor: under the PE/PD operating model, reports are drafted by the
sidecar, vetted by the PE, then edited and issued outside the app. In-app
storage is a convenience at most, and a viewer may return as its own later
packet.

Explicit exclusions for this packet, even though related to reporting: `.docx`
generation/template conformance, percent-complete ingestion, reporting
period/snapshot semantics, first-class discipline view, interfaces import
contract, MDL-to-RAIL consistency checks in intake/triage, and internal/client
typing of needs. These await a workplan amendment and the owner's revised MDL
and RAIL templates; do not pre-build them and do not build against them.
