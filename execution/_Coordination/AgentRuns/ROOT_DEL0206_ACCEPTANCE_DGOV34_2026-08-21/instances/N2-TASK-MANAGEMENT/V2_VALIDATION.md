# N2 validation evidence — Dependent Objective V2

Result: `PASS`

## Corrected predecessor identity

The initially relayed SHA
`8e704f2b63ebac92ee4195e070411913629622c5` did not resolve. N2 failed
closed before any V2 register mutation. HELP_HUMAN corrected and explicitly
confirmed N3 commit
`8e704f2b63302c8568c48f8fee7c4681e3ec4262`, parent
`275b524bc61139ebad96144b1811297b09a99e94`, in the V2 amendment. The
corrected commit resolves as a Git commit and is current `HEAD` for the V2
work.

Verified evidence pins:

- D-GOV-34 SHA-256:
  `99180dc091ab4b425b9bd8ccf15d7bbaf7527d33aec90ffa41153abb7048faf1`;
- `agents/AGENT_CHANGE.md` SHA-256:
  `bb2922c5761395687caf120097276806769ec38f4fee8935d9e6c7bbb8506a06`;
- G4 manifest SHA-256:
  `df058c953422b4de55903774181355c463bd1861fb1c645baf36ebedbf91513b`;
- N3 return SHA-256:
  `ccc90129ef616ee8cd72fc4479331dcf620ffa96f956f0eb76c41b0f5ca98e9d`.

## Exact register result

`TM-ROOT-124` is `CLOSED`, `Disposition=RESOLVED_WITH_CHANGE`, with empty
Trigger, `LastReviewed=2026-08-21`, and `Closed=2026-08-21`. Its authority
pointer and evidence fields cite D-GOV-34, the landed instruction bytes, G4
manifest, and N3 return with exact matching hashes. The archive helper moved
exactly this one owner-closed row.

Keyed comparison against the N3 commit proves:

- live removed: exactly `TM-ROOT-124`;
- archive added: exactly `TM-ROOT-124`;
- no added live ID, removed archive ID, changed common live row, or changed
  common archive row.

## Checks

- V2 mandatory preflight federation: `COMPLETE`.
- Live register validation: PASS, 21 rows.
- Closed archive validation: PASS, 106 rows.
- Archive dry-run: exactly one row eligible.
- Archive application: exactly one row moved.
- `python3 -m pytest -q tools/taskmgmt`: 49 passed.
- Final federation: `COMPLETE`, four registers, 79 findings, zero writes.
- Closure evidence SHA currentness: PASS.
- Foreign register preservation: PASS.

No D-GOV, agent, notice, receipt, foreign register, commit, push, PR, or merge
write occurred in V2.
