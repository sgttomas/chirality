# D-PEC-07 - PROPOSAL: embedded upload-agent pathway (file upload → agent-mapped update)

**Status:** AWAITING_RULING.
**Date prepared:** 2026-07-05
**Decision ID:** D-PEC-07
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1; D-GOV-04).

## Owner direction of record (verbatim, 2026-07-05, in-session, Ryan Tufts)

> Will do. In order to do so I want the embedded agent to accept a file upload
> from me and take action accordingly to update things. That's one end goal.

Said of the remaining owner-side data work (risk-log population, schedule
CSV/XER export) after the D-PEC-01 evidence-01..03 rehearsals.

## Decision to rule

What pathway realizes "upload a file → agent takes action to update things",
and in what order. Constraints in force: D-T0-13 O-A staging (L3 is the
destination, per-operation risk-graded), D-PEC-05 O-B (L3 deferred **until
after D-PEC-01 pilot evidence** — that evidence now exists: evidence-01..03),
F-PEC-1 (no pec source writes without a tranche authorization), profile
`operation_proposal_contract` (proposal lifecycle draft → ready_for_review →
accepted → applied), `requires_human_confirmation` flags, `force=true` off.

## Verified facts

| Fact | Source |
|---|---|
| The import seam is proven end-to-end on real data: MDL 457/457 + idempotent; RAIL 254/272 as intake; decisions 52/62; row-level rejects for data gaps. | `_DomainEngines/pec/PEC_2026-07-05_DPEC01-pilot-evidence-0{2,3}/MANIFEST.md` |
| Mapping from the owner's workbook shapes to §16 is documented and ratified, with templates. | `../IMPORT_TEMPLATES/IMPORT_MAPPING.md` |
| The API accepts CSV via `POST /api/projects/:pid/import/:contract` behind `config.manage`; there is no file-upload UI or agent surface in the app today. | `server/src/api.ts:316` |
| L3/proposal-shaped apply needs a pec proposal-shaped API that does not exist yet. | `_DomainEngines/profiles/pec.yaml` open issues; D-PEC-05 packet |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | **Loop-agent pathway now (zero code):** owner drops a file in `pilot-scratch/input/` (or hands it in-session); the standing loop agent maps it per `IMPORT_MAPPING.md`, shows the proposed import (counts + sample + new mappings) and imports on the owner's in-session confirmation; evidence snapshot per run. | Available immediately; exactly the proven evidence-01..03 mechanics, formalized. Human confirmation stays in-session per act. |
| O-B | **L3 design brief (design only):** authorize a CANDIDATE design brief for the embedded in-app agent — upload endpoint, proposal lifecycle records (draft/review/accept/apply per the profile contract), RBAC'd confirm-in-app, audit history. No implementation until the brief is adopted and a tranche is authorized. | Moves the true end goal forward inside the D-T0-13 L3 rung without opening the pec source fence yet. |
| O-C | O-A + O-B together (staged). | The working pathway today plus the designed destination; implementation still gated on brief adoption + tranche authorization. |
| O-D | Defer both. | End goal parked; owner-side data work proceeds manually via templates. |

## Recommendation (non-binding)

**O-C.** O-A is already proven mechanics and costs nothing; O-B is the lawful
next step toward the stated end goal now that D-PEC-05's pilot-evidence
precondition is met. Implementation authority is deliberately NOT requested
here — the brief comes back as a rulable artifact first.

## On ruling

- O-A/O-C: the loop treats an owner file-drop + in-session direction as the
  trigger; each run lands as a dated evidence snapshot with per-act
  confirmation recorded.
- O-B/O-C: next iteration produces the CANDIDATE design brief
  (`_DomainEngines/proposals/pec/`), terminating in its own adoption gate.

## Human ruling

_(open — owner's act)_
