<!-- PACKET
id: P-16
cluster: CL-16
title: Old chat history not picked up for new projects
question: The Runtime can read old project-local chat sessions, but projects the App sets up never declare where those are, so the reader never runs; should the deliverable text say so, or should the code declare the old location?
recommended: A — correct the text; code stands
depends_on: none
decision_type: owner; engineering
tier: GOVERNING
-->
# P-16 — Old chat history not picked up for new projects

Cluster CL-16 · no named question (live-path finding) · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** The Runtime can read and lazily copy chats from the older project-local store. But the project manifest the App writes never lists the old locations, so for projects the App sets up, nothing is ever read from there. Which do you want?
- Correct the deliverable text to match this.
- Have the code declare the old location.

## What we found
- Amended CONTRACT K-EVENT-4 names the central store under the App's user data as canonical, and the project-local `.chirality/sessions` as a legacy source that is migrated lazily. SPEC §8.2 still shows the project-local layout. The DIRECTIVE §0 order puts CONTRACT above SPEC, so the rows are text out of date, not a conflict (see the Notes on `DEL-05-04#CLM-003.1`). [GOVERNING]
- D-GOV-43 item 5: daemon-era chats "are preserved unchanged in place". If the existing reader shows them without new work, they stay viewable; otherwise they are kept as an accessible archive. "No history-import feature is a release prerequisite" (`D-GOV-43.proposed.md:196-207`). [GOVERNING]
- `bootstrapProject` writes the v2 manifest with no `legacySessionRoots` field (`projects/chirality-runtime/packages/core/src/bootstrap-project.ts:43-53`). The registry accepts the field's absence (`packages/core/src/project-registry.ts:225-233`). The session store reads legacy roots only when the field is present (`packages/core/src/session-store.ts:112,170`). [code]
- No deliverable names which unit declares legacy roots. Only the App-dev repository's own manifest names one (`R3/CROSS_PACKAGE_FINDINGS.csv` XPF-045). [run finding]
- `DEL-05-01#CLM-010.3` (an ALSO member here) records this as a choice nobody recorded: bootstrap came from `2f825f180` on 2026-09-10. [run finding]

## Affected rows
<!-- COUNTS -->
**8 rows are decided in this packet** (PRIMARY); 6 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-16`.

| Package | Text out of date (`STALE_SPECIFICATION`) | Total |
|---|---:|---:|
| PKG-01 | 4 | 4 |
| PKG-05 | 4 | 4 |
| **Total** | **8** | **8** |

ALSO/CONTEXT members by Disposition: Text out of date 3, Partly built 2, Verification out of date 1.

<!-- /COUNTS -->
All 8 PRIMARY rows are "text out of date": they name the project-local store as canonical, or describe the retired eager conversion. None needs an authority ruling. The 6 ALSO rows are in DEL-05-01 and DEL-05-04 and are decided in P-09 (4) and P-11 (2). `DEL-05-01#CLM-010.3` (P-09) asks whether the unreachable migration is acceptable.

## Options
**A. Correct the text; the code stands.**
- The deliverable text names the central store as canonical and the project-local store as a legacy source that is read only when a manifest declares it.
- For App-set-up projects, older chats stay in place as an archive, as D-GOV-43 item 5 allows.
- *R5 would:* edit the 8 rows' text in DEL-01-01, DEL-01-02 and DEL-05-04, and add, in DEL-05-01, a sentence naming who may declare legacy roots.

**B. Code declares the legacy root.** A separate implementation brief makes bootstrap (or first open) add an existing `.chirality/sessions` to `legacySessionRoots`. *R5 would:* make the same text edits as A, and the migration rows wait on the brief.

**C. Retire the migration requirement.** The deliverable text drops lazy migration for App-set-up projects altogether. *R5 would:* rewrite the rows and the DEL-05-01 migration requirement.

**D. Defer.** Nothing changes.

## HELP_HUMAN recommendation (draft)
Option A:
- D-GOV-43 item 5 already says old chats are preserved in place and that no import feature is required.
- The 8 rows are plain text repairs.

Option A leaves one choice open: whether you want old chats visible in App-set-up projects. If you do, Option B is a small bounded change. It is Runtime code, so it would be the Runtime loop's brief.

## Who decides
The owner decides the direction. Option B is an engineering brief in the Runtime loop, outside this run's write scope. Nothing here is outside your App authority.

## On ruling
- The consolidated R4 ruling record (next free D-APP ID, committed by HELP_HUMAN) names the option and the key set (`PACKET_INDEX.csv` P-16 PRIMARY).
- R5 tranche managers for PKG-01 and PKG-05 edit the text of those rows. R6 backchecks each row.
- Under Option B, the separate implementation brief runs first for the migration rows.
- No lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-05-01#CLM-010.3` (PRIMARY in P-09; it cites R4 and R4-Q1) decides whether unreachable migration is an acceptable state. Its answer should match this one.
- The ALSO rows `DEL-05-04#CLM-018` and `DEL-03-02#CLM-004` also carry R4-Q1 (P-09).
- No spot-check contest touches these rows.
