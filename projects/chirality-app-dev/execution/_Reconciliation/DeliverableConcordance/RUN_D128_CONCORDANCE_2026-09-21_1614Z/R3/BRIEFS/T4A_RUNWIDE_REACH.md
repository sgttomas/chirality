# T4A — Run-wide consistency calls (a), (b), (g): reach and stale basis flags

Read `_COMMON.md` first. Also read CONVENTIONS §2.3 (ImplementationEvidence reachability; the
REACH definitions), §9 row 2 (`REACHABILITY.csv` method) and RUN_BASIS Addendum 1 item 4
(unreached code takes `REACH=LEGACY_ONLY` with `UNREACHED` in Notes).

Decide each call **from code and records in the evidence roots only**. A call is a consistency
call for this run's rows, not a ruling. Where the code genuinely supports both readings, say so
and state the reading R3 applies for consistency, with the reason.

**(a) Reach of the domain contract modules.** The evidence pack
(`<RUN>/R2/_shared/EVIDENCE_PACK/REACHABILITY.csv`) says LIVE; the RTCONTRACT capability file
(`<RUN>/R2/SURFACES/RTCONTRACT_capabilities.csv` and `RTCONTRACT_notes.md`) says TEST_ONLY.
Identify exactly which modules are in dispute (under
`projects/chirality-runtime/packages/contracts/src/**` and any App re-export), trace the static
import chain from a product entry point (`frontend/src/app/api/**` routes, `frontend/src/app/**`
pages, `frontend/electron/main.ts`, or the runtime-service entry the App packages), and
distinguish "module is imported" from "the symbol the claim relies on is used on the live path".

**(b) Reach of build and validation scripts** (`frontend/scripts/**`, `package.json` script
entries, `proof:*`, `validate:*`, `harness:validate:*`, `controlled-ci-runtime.ts`,
`run-packaged-security-proof.mjs`, `run-network-policy-proof.mjs`, `scan-secret-evidence.mjs`).
The R1b BUILD capability file tags validation and `proof:*` scripts TEST_ONLY; PKG-09 workers
and grading key "4b" tagged scripts invoked by release `package.json` entries LIVE; some rows
say LEGACY_ONLY with UNREACHED. See `<RUN>/R2/PKG-09/VERIFICATION.md` §5.3 and the rows it lists,
`<RUN>/R2/SURFACES/BUILD_capabilities.csv` and `BUILD_notes.md`. Fix one reading per script class
(for example: packaging/build scripts invoked by `desktop:dist`; release-validation scripts;
proof scripts; CI-only runners) grounded in how the code is actually invoked.

**(g) RUN_BASIS §5 flags found stale.** RUN_BASIS §5 lists D-APP-104, 107, 121, 122, 123, 125 and
126 as "GOVERNING, flagged" (effect pending, held or unapplied). EXT found the effects of D-APP-104,
107, 122 and 123 did land (`R2/EXT/R3_OBSERVATIONS.md`; `DEC:REGISTER-1`, `-2` in
`EXTENSION_CONCORDANCE.csv`). Confirm or refute per decision from the register
(`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` and the ruling
records) and code. This is recorded as a finding; RUN_BASIS is HELP_HUMAN's and is not edited.
List the concordance rows that relied on a stale flag (search `CLAIM_CONCORDANCE.csv` and
`EXTENSION_CONCORDANCE.csv` for those decision IDs); do not re-map them unless the row's
Disposition rests on the flag alone, and then say so.

**Affected rows.** For (a) and (b), find every concordance row whose `ImplementationEvidence`
tags the disputed paths with a REACH value that differs from the call (script search over both
concordance files). Each re-mapping is a literal substring replacement inside the cell.

**Output 1.** `<RUN>/R3/_work/T4A_REMAPS.csv`:
`ClaimKey,Field,Find,Replace,Call,Evidence` — `Field` is normally `ImplementationEvidence`;
`Find` is the exact substring in the current cell (e.g. `run-network-policy-proof.mjs REACH=LEGACY_ONLY`)
and `Replace` the replacement. `Find` must occur exactly once in the cell. `Call` is `a`, `b` or `g`.
Only list rows whose tag actually changes.

**Output 2.** `<RUN>/R3/_work/T4A_RUNWIDE.md`: one section per call (a), (b), (g): **Evidence**
(paths and import chains), **Call** (the reading applied), **Affected rows** (count and keys; say
which rows' Dispositions might be affected by the tag change, without re-dispositioning them),
and **Limits**. ≤ 150 lines.
