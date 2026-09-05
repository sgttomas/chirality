# PEC L2 evidence — `seed.demo` 01 — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** Per-operation L2
> evidence under the D-T0-13 O-A staging and D-T0-17 L1 acceptance. Captured
> outputs are derivative; pec's tests and source govern. Immutable after
> publication — corrections go in a new dated snapshot.

## Authority for this act

`seed.demo` is profile-flagged `requires_human_confirmation: true`. Owner
confirmation of record (2026-07-05, in-session, Ryan Tufts): "For the Optional
demo-basis L2 rungs, I approve they can run on scratch/demo basis
independently of D-PEC-01." Guard repair authority: D-PEC-06 O-A (executed
PR #68, Receipt 14).

## What this proves

The repaired `seed.demo` operation at L2 on a scratch/demo basis: it requires
an explicit `PEC_DB`, seeds the full demo project through the real service
layer on a scratch/demo target, and refuses a non-scratch/non-demo target
without creating or deleting anything.

## Source refs

- Tree: branch `codex/pec-dpec01-pilot-evidence` at base `59d1e4c7c`
  (`origin/main`); pec sources unmodified.
- Positive run: `PEC_DB=projects/pec/pilot-scratch/db/pec-scratch-demo-seed.db
  node tools/seed.ts` → exit 0; full Aurora demo project seeded (registers,
  history 163 entries, notifications 28; see `seed-demo.log`). Seeded DB
  SHA-256
  `eafc3b3f49be5f490df870e0e7cec769ae3329e66ee78507aed6ed59001aecc8`;
  scratch DB deleted after capture with its `-wal`/`-shm`.
- Refusal run: `PEC_DB=$HOME/pec-guard-refusal-test.db node tools/seed.ts` →
  exit 1, `Error: Refusing to seed non-scratch/non-demo database target`; no
  file was created at the target (`seed-guard-refusal.log`).

## Limitations

- Demo seed content only (committed `tools/seed.ts` fiction); no real project
  content involved; D-T0-14 posture unaffected.
- Not a pilot-readiness, correctness, or adoption claim (F-PEC-2); Gate 2
  remains DRAFT/open (D-PEC-04 O-B); L3 remains deferred (D-PEC-05 O-B).
- With this rung, remaining per-operation L2 coverage: `import.csv` at
  real-data basis rides the D-PEC-01 evidence line (evidence-01 captured its
  contract-gate seam; row-level import awaits contract-shaped exports);
  `backup.create`/`backup.restore` were proven in
  `PEC_2026-07-04_L2-backup-create-01` / `…restore-01`.
