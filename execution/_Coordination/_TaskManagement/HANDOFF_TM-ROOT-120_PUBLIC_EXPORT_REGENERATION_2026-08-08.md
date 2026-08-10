# Routed handoff — TM-ROOT-120 public-export regeneration

Status: **ROUTED THROUGH ROOT CLOSEOUT — NOT ACTIVATED**

From: Root `TASK_MANAGEMENT`
To: Root `WORKING_ITEMS`, package
`PKG-04_Developmental_Machinery_and_Change_Control`, deliverable
`DEL-04-07_Public_Export_Boundary_Conformance`
Related row: `TM-ROOT-120`
Routing authority: `RULING_2026-08-08_ROOT_DEFERRAL_REVIEW.md`

This handoff is a Root-local ordinary intake record. Routing does not activate
the deliverable, authorize an export, publish or release any target, or permit
a write outside a later sealed `WORKING_ITEMS` activation.

## Objective

Regenerate the tracked Chirality App public-export derivatives against the
accepted current Root PRD bytes without changing the governed export profile
or applying to an external target.

## Accepted input basis

- `docs/PRD_ROOT.md`, SHA-256
  `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`.
- `execution/_ScopeChange/SCA-003_2026-08-02_2212/PRD_Application_Export_Disposition_2026-08-03.md`,
  SHA-256
  `a5de5ae0ef0cd3a1d17b9c9527eebdeacd6e68fe7b981e2b632b84c20d07ead6`.
- Current stale `exports/chirality-app/export-manifest.csv`, SHA-256
  `079736ce89ab4e3143b91486974eff76336879d8297a04aedd229ceb680b4249`.
- Governed profile: `exports/chirality-app/export_public.py` and its existing
  allowlist/failure behavior, incorporated by Root PRD D-10.

## Bounded work requested through the owning instrument

1. Activate only `DEL-04-07_Public_Export_Boundary_Conformance` through the
   ordinary `WORKING_ITEMS` lane and its lifecycle gates.
2. Run the existing export profile against accepted committed Root state.
3. Regenerate the tracked staging tree, manifest, and export report only.
4. Do not use `--apply-target`; do not write an external repository.
5. Do not modify the profile, allowlist, sanitization rules, or boundary
   semantics. Any such need stops and returns for a separately governed act.
6. Verify that the new manifest binds `docs/PRD_ROOT.md` at SHA-256
   `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`.
7. Run forbidden-path, private-path leak, manifest-integrity, report, and
   ordinary diff/whitespace checks.

## Required return

- exact activation and accepted-basis references;
- command, exit status, copied-file count, sanitization count, and leak-check
  result;
- exact SHA-256 identities for the regenerated manifest and report;
- confirmation that the allowlist/profile bytes did not change;
- confirmation that no external target was written;
- closure recommendation for `TM-ROOT-120`, with exact evidence paths and
  hashes; and
- explicit statement that regeneration alone creates no target publication,
  lifecycle, release, reliance, or acceptance effect.
