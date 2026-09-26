---
doc_id: PEC-SCA006-CP3-AGENTS-MD-AMENDMENT1-DIFF
doc_kind: scope_change.instruction_amendment_hunk
amendment: SCA-006
checkpoint_group: 3 (preparation)
prepared: 2026-09-26
prepared_by: WORKING_ITEMS manager, brief B6, HELP_HUMAN undertaking HELP-HUMAN-PEC-20260925-POST-SCA005, work-graph node R3; roles instruction-asserted, not mechanically enforced
status: applied_owner_hunk_approved (2026-09-26)
authority: checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md (SHA-256 15720eb1d25ade4e7cb5d62765824634318e0e956129a6e6c3ad30cdaf74777e)
candidate: CP2_CANDIDATE/AGENTS.candidate.md
candidate_sha256: 49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d
candidate_slot_filled_sha256: 6f6f2ed1c0ed6e009323beaa004a79b72b717b4cd9431199eb2f9b990cf264e6
applied_postimage: projects/pec/AGENTS.md
applied_postimage_sha256: 4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c
live_preimage_sha256: c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a
---

# SCA-006 group-2 amendment 1 — the `AGENTS.md` Remaining-sections hunk

This file records the one correction that SCA-006 checkpoint group 2
amendment 1 adds to the accepted `projects/pec/AGENTS.md` candidate. It was
drafted during checkpoint-3 preparation within the bounds amendment 1 sets.
**The owner must explicitly approve the exact hunk text below before the
checkpoint-3 application PR merges. Display alone is not enough.** When this
file was first written, no approval had been given. **Update, 2026-09-26: the
owner approved the exact hunk below, verbatim "approve hunk"**, after
HELP_HUMAN presented this paragraph, the dropped clause (§2) and the audit's
COV-083 observation. HELP_HUMAN transcribed the act under K-AUTH-1; it is
recorded in `Decision_Log.md` row SCA006-G2-A1. The approved postimage is
`projects/pec/AGENTS.md` `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`.

## 1. Owner's words (verbatim, 2026-09-26)

> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned.

HELP_HUMAN's interpretation of these words is in amendment 1's `DECISION.md`.
This hunk implements its row "`AGENTS.md` Remaining correction".

## 2. Bounds applied

| Amendment-1 bound | How the hunk meets it |
|---|---|
| Replace exactly the paragraph at candidate L261–270, and no other line | The replaced span is candidate L261–270 (live preimage L241–250). Candidate L1–260 and L271–454 are byte-identical in the applied file, apart from the application-date slot at L6 (§4) |
| State that PEC adds no new `## Remaining` sections or entries | Sentence 1 |
| State that no PEC feed profile reads them, so the coordination plane does not scan them | Sentence 2. Checked against the live tree: no `projects/pec/v2/**` file names a `remaining-loop` or `remaining-items` profile, and PRD v2.4 §7.1 (Package / Deliverable row) makes remaining items a per-loop optional field read only where a loop's feed profile declares it. **Conflicting design text in the same poststate:** revision 1.6 keeps, unchanged from 1.5, the statement that PEC's own `pec` row "declares the `remaining-loop` profile now". It appears in `SOFTWARE_DECOMP.md` L259 (SOW-094), `ScopeLedger.csv` L72 (SOW-094), `Deliverables.csv` L10 (DEL-01-06) and `SOFTWARE_DECOMP.md` L652 (§9 "feed profile" examples); audit finding COV-083 in `COV_SCA006_POSTCHANGE_2026-09-26_0051` records it. Under SCA-005 (Q8 (a)) `remaining-loop` is the profile that would read these sections. `D-PEC-96` has since been ruled (2026-09-26, `_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md`, SHA-256 `852057f0…399e`, on `origin/main` through PR #946): PEC's row is migrated and carries no `remaining-loop` profile. That ruling leaves the decomposition sentences to a later PEC scope change, which SCA-006 cannot perform without enlarging its accepted amendment (`RUN_SUMMARY.md` Q-CP3-1). HELP_HUMAN presented this observation to the owner before the hunk was approved |
| New open scope goes to the work graph and its governing records | Sentence 3 |
| Keep the status quo for the existing sections until any retirement ruling: they stay in place | Sentence 4 |
| Each item's gate markers still bind that item | Sentence 5, unchanged from the candidate |
| They are updated only under a packet that opens that `_STATUS.md` | Sentences 6 and 7, carrying the candidate's "without that grant, record the consequence in the graph and bring it to the owner" |
| Keep the statement that retiring them, as App and Piping did, is a separate owner-directed undertaking | Last sentence, unchanged in wording |
| Minimal and factual; do not decide the retirement | The paragraph grows from 10 to 12 lines. It retires nothing and names no retirement outcome |

One clause of the candidate paragraph is not carried: "its graph accounts for
the Remaining items it touches". The owner's words say there is "no need to
scan for them", and that clause implies that each undertaking's graph looks
for Remaining items. The duty that still applies when an undertaking does
touch an item is kept in part in sentences 6 and 7. Disclosure (verifier verdict
01, finding 2): the clause concerned only items an undertaking already
touches, so dropping it is a judgment. The candidate's positive duty ("When an
undertaking completes or changes an item, update it under the packet…")
becomes a restriction ("Update an item only under the packet…"), and "changes"
becomes "affects". An undertaking holding a grant therefore has no explicit
duty left to update an item it completes; without a grant, the duty to record
the consequence in the graph and bring it to the owner remains. The owner
approved these bytes after seeing the dropped clause. The verifier is asked to confirm
this reading (brief B6 §"Independent verification").

## 3. The hunk (exact text)

Before — `CP2_CANDIDATE/AGENTS.candidate.md` L261–270:

```text
PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). They are no longer a work-selection surface: steering
selects the undertaking and its graph accounts for the Remaining items it
touches. A Remaining item's own gate markers still bind that item. When an
undertaking completes or changes an item, update it under the packet that
opens that `_STATUS.md`; without that grant, record the consequence in the
graph and bring it to the owner. Record new open scope in the graph and its
governing records rather than as a new Remaining entry. Retiring the sections,
as App and Piping did, is a separate owner-directed undertaking.
```

After — applied `projects/pec/AGENTS.md` L261–272:

```text
PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries
(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2
amendment 1). No PEC feed profile reads them, so the coordination plane does
not scan them, and they are not a work-selection surface. Steering selects the
undertaking; record new open scope in its work graph and governing records.
Until any retirement ruling, the existing sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). A Remaining item's own gate markers still bind that item.
Update an item only under the packet that opens that `_STATUS.md`. If an
undertaking completes or affects an item without such a grant, record the
consequence in the graph and bring it to the owner. Retiring the sections, as
App and Piping did, is a separate owner-directed undertaking.
```

Unified diff, zero context, slot-filled candidate against the applied file.
`difflib` splits the one replaced paragraph into two regions because the line
"deliverable-local records of open scope under their owning decisions (for"
occurs unchanged in both. Both regions lie inside candidate L261–270.

```diff
--- AGENTS.candidate.md (slot-filled)
+++ projects/pec/AGENTS.md (applied)
@@ -261 +261,6 @@
-PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as
+PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries
+(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2
+amendment 1). No PEC feed profile reads them, so the coordination plane does
+not scan them, and they are not a work-selection surface. Steering selects the
+undertaking; record new open scope in its work graph and governing records.
+Until any retirement ruling, the existing sections stay in place as
@@ -263,8 +268,5 @@
-example `D-PEC-83`). They are no longer a work-selection surface: steering
-selects the undertaking and its graph accounts for the Remaining items it
-touches. A Remaining item's own gate markers still bind that item. When an
-undertaking completes or changes an item, update it under the packet that
-opens that `_STATUS.md`; without that grant, record the consequence in the
-graph and bring it to the owner. Record new open scope in the graph and its
-governing records rather than as a new Remaining entry. Retiring the sections,
-as App and Piping did, is a separate owner-directed undertaking.
+example `D-PEC-83`). A Remaining item's own gate markers still bind that item.
+Update an item only under the packet that opens that `_STATUS.md`. If an
+undertaking completes or affects an item without such a grant, record the
+consequence in the graph and bring it to the owner. Retiring the sections, as
+App and Piping did, is a separate owner-directed undertaking.
```

## 4. Slots and the verification rule

Amendment 1 §"Verification rule": the applied file equals
`49ce993a…070d` with its application-date slots filled per
`AGENTS_MD_CANDIDATE_DIFF.md` §9, except for this one hunk.

| Slot (`AGENTS_MD_CANDIDATE_DIFF.md` §9) | Default | Applied | Basis |
|---|---|---|---|
| L6 front-matter `amended:`, first token | `2026-09-25` | `2026-09-26` | application-date slot; the tranche is applied on 2026-09-26 (local date, America/Edmonton) |
| L209 Governance Pointers group-2 folder token | `SCA-006_GROUP-2_2026-09-25` | `SCA-006_GROUP-2_2026-09-25` (unchanged) | the actual group-2 folder name; act-date value |

| Measure | SHA-256 |
|---|---|
| Live preimage `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| Accepted candidate (slots at default) | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` |
| Accepted candidate with the L6 slot filled | `6f6f2ed1c0ed6e009323beaa004a79b72b717b4cd9431199eb2f9b990cf264e6` |
| Applied postimage (slot filled plus this hunk) | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |

Proof, run by `CP3_EVIDENCE/apply_a4_agents.py` (Python 3.13.7). To rerun any `CP3_EVIDENCE` script elsewhere, set its `R` constant to the value of `git rev-parse --show-toplevel`:
1. It asserts the preimage and candidate hashes.
2. It fills the L6 slot, and asserts that L209 carries the act-date token.
3. It asserts that the replaced span is exactly candidate L261–270, bounded by
   the blank lines at L260 and L271.
4. It asserts that every differing region lies inside that span, and that the
   prefix L1–260 and the suffix from L271 are identical.
5. It puts the "before" text back and asserts the result equals `6f6f2ed1…`.
6. It restores the slot default and asserts the result equals `49ce993a…`.
7. It checks that no added line exceeds 79 characters or carries trailing
   whitespace or a tab.

Every step passed, and the script exited 0.

## 5. What this does not do

- It retires, deletes or edits no `## Remaining` section. The existing
  sections are unchanged.
- It writes no `_STATUS.md` and changes no lifecycle.
- It changes no other line of `projects/pec/AGENTS.md`.
- It is not itself the owner's approval. That approval is the owner's act of
  2026-09-26, recorded in `Decision_Log.md` row SCA006-G2-A1.
- It makes no CHECKING, ISSUED or acceptance claim.
