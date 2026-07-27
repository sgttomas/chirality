# App Receiving Disposition — D-GOV-26 detector-claim correction

Status: `NO_LOCAL_CORPUS_CHANGE`
Date: 2026-07-27
Receiving loop: Chirality App Dev
Upstream notice:
`NOTICE_D-GOV-26_DETECTOR_CLAIM_CORRECTION_2026-07-27.md`
Artifact class: coordination disposition; not authority

## Disposition

The App loop acknowledges the Root correction and withdraws reliance only on
the historical D-GOV-26 notice's claim that App's authority corpus pins and
detects changes to Root `docs/SPEC.md` and `docs/CONTRACT.md`, and on its
consequent instruction to re-pin those Root files.

The historical notice remains unchanged. Its factual description of the
D-GOV-26 Root changes and its K-WRITE-2 interpretation are not withdrawn.

At `main@fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`, App's resolver selects
the App-local `projects/chirality-app-dev/docs/SPEC.md` and
`projects/chirality-app-dev/docs/CONTRACT.md`. The eight-member App authority
corpus reports `MATCH` for all members and no drift.

## Local effect

`NO_LOCAL_CORPUS_CHANGE`:

- no member is added or removed;
- no resolver behavior changes;
- no hash or deliverable reference is repinned;
- no universal pinning or detector design is adopted;
- no App scope or authority changes; and
- no SCOPE_CHANGE, product, runtime, lifecycle, release, or
  professional-reliance effect occurs.

Any future cross-loop detector or corpus-membership design requires its own
governed act. Rerun this disposition only if App corpus membership, resolver
behavior, or the corrected detector claim changes.

Acknowledgement is tracked coordination and is not a Root closure gate.
