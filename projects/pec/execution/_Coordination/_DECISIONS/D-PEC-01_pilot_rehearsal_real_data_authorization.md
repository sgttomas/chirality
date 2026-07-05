# D-PEC-01 - PROPOSAL: pilot rehearsal and real-data authorization

**Status:** RULED / O-A affirmed by owner; exact rehearsal basis still pending owner supply.
**Date prepared:** 2026-07-04
**Decision ID:** D-PEC-01
**Prepared by:** PEC work loop agent under the standing PEC loop. The ruling act is the owner's (K-AUTH-1; D-GOV-04).
**Ruling SHA:** `3e4ba7543` - the commit publishing this ruling record (backfilled same-branch per the D-T0-10 / D-T0-17 precedent).

## Decision to rule

Decide whether, when, and under what data-residency basis agents may help with
the real PEC pilot rehearsal: real MDL/RAIL/decision/risk spreadsheet shakedown,
real pilot import, and the real-pilot restore rehearsal required before go-live.

Until this decision is ruled, D-T0-14's CLOSED default remains in force: agents
may use committed fixtures and scratch/demo databases, but not real PEC
instance content.

## Verified facts

| Fact | Source |
|---|---|
| D-T0-14 kept PEC data residency CLOSED and said the real MDL/RAIL moment belongs in D-PEC-01 with a concrete data case, not a pre-authorized abstract egress rule. | `_DomainEngines/_DECISIONS/D-T0-14_pec_data_residency.md:47-56` |
| PEC STATUS says pilot-readiness tooling is done but the human rehearsal remains: import real MDL/RAIL, run a real weekly triage, rehearse one restore against the real pilot DB, and use feedback to drive later scope. | `projects/pec/docs/STATUS.md:54-63`, `projects/pec/docs/STATUS.md:90-95` |
| The pilot runbook says `tools/pilot-drill.ts` rehearses imports, row-level reject reporting, triage, derived-view rendering, and backup-restore on scratch DBs; real spreadsheets can be shaken down with `--mdl/--rail/--decisions/--risks`. | `projects/pec/docs/PILOT.md:7-29` |
| The pilot runbook requires one tested restore of real pilot data before go-live, rehearsed by restoring a real backup to a scratch path and spot-checking through a temporary server. | `projects/pec/docs/PILOT.md:93-113` |
| PEC import/export routes expose project data, use per-row reports, and make `force=true` a deliberate override path. | `projects/pec/docs/SPEC.md:351-372`, `projects/pec/docs/SPEC.md:376-388` |
| Import cannot advance an existing revision lifecycle through the issue gate; issue-affecting transitions remain gated workflow acts. | `projects/pec/docs/SPEC.md:456-459` |
| The profile marks `import.csv`, `backup.restore`, and `seed.demo` as domain-controlled writes requiring human confirmation; `force=true` is never agent-set without a ruling. | `_DomainEngines/profiles/pec.yaml:107-125` |

## Options

| ID | Option | Consequence |
|---|---|---|
| O-A | Authorize a narrow D-T0-14/O-B real-data case for the pilot rehearsal only: owner supplies the exact real spreadsheet paths or exports, actor/visibility basis, and scratch DB/backup locations; agents may run the named rehearsal commands, capture immutable manifests/check summaries, and avoid committing raw real spreadsheets, real DB copies, or unredacted instance exports unless separately enumerated. `force=true` remains off unless separately ruled. | Advances the real pilot gate while keeping egress bounded and auditable. |
| O-B | Keep agents out of real data. The pilot team runs the real spreadsheet shakedown, import, triage, and restore rehearsal; agents may only record a cited owner result summary and pointers supplied by the owner. | Lowest data exposure, but less reproducible agent-side evidence. |
| O-C | Open PEC instance-content residency for this pilot phase, allowing agents to inspect/capture real exports, reports, logs, and DB-derived artifacts under a named actor. | Broadest help, but highest privacy/egress exposure; supersedes the current CLOSED default for this scope. |
| O-D | Defer. Keep D-T0-14 CLOSED with no real-data pilot authorization. | Preserves current fence; real pilot execution remains blocked for agent participation. |

## Recommendation

Recommend **O-A**.

O-A is the smallest ruling that moves the pilot gate: it lets the owner put a
concrete real-data basis in front of the loop, while keeping the capture rule
manifest-first and no-raw-data-by-default. It also keeps PEC's reserved human
acts intact: agents can run rehearsals and report row-level outcomes, but they
do not approve imports, accept checks, issue revisions, record engineering
judgments, or claim pilot/go-live readiness.

## If O-A is ruled

The next lawful tranche should be a branch-first evidence run that records:

- owner-provided input basis: paths, hashes if permitted, actor/visibility
  basis, and whether raw file contents may be viewed or only command outputs;
- commands and environment: `node tools/pilot-drill.ts --mdl ... --rail ...
  --decisions ... --risks ...` against owner-provided files, plus the restore
  rehearsal against a scratch `PEC_DB`;
- capture limits: no raw real spreadsheets, real DB files, or unredacted
  exports committed unless the ruling names them; manifests may record
  filenames, hashes, counts, timings, and reject summaries permitted by the
  ruling;
- gate limits: no `force=true` unless separately ruled; no Gate 2 adoption; no
  L3/proposal-shaped apply path; no pilot-readiness or go-live claim.

## Human ruling

**Ruling:** O-A affirmed by owner (Ryan Tufts), 2026-07-05, in-session.

Owner ruling of record:

> D-PEC-01: O-A. Authorize the narrow pilot-only real-data rehearsal as scoped in the packet. Two riders: (1) SHA-256 hashes of the real input files are permitted in manifests -- resolve the packet's "hashes if permitted" clause as permitted; this anchors the evidence chain without content egress, same convention as the L1 manifests. (2) The exact spreadsheet/export paths, actor/visibility basis, scratch DB/backup locations, and capture limits will be supplied by me before the evidence run begins -- do not start the rehearsal until I provide them. `force=true` remains off; it requires a separate ruling.

This ruling authorizes only the narrow pilot-only real-data rehearsal described
in O-A. It does not itself supply the real spreadsheet/export paths,
actor/visibility basis, scratch database or backup locations, or capture
limits. Agents must not begin the real-data evidence run until the owner
provides those inputs. `force=true` remains prohibited absent a separate owner
ruling.
