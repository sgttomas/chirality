# A2-PKG09-R19-REPAIR-01 sealed brief

Status: `FROZEN`

## Objective

Repair exactly findings R19-REV-01 and R19-REV-02 from the immutable fresh
review. Use the original executor context because only it retains the complete
pack command's execution-tool transcript. Do not delegate.

## Allowed writes

- `instances/WI-PKG09-R19-STAGING-01/executor/desktop-pack.full.log`
- new `instances/WI-PKG09-R19-STAGING-01/repair-cycle-1/executor/` lineage,
  checks, and return files
- R19 record only, limited to restored-log hash/completeness pointers and
  top-level/directly dependent claim calibration

Do not modify `_STATUS.md`, original executor return/evidence other than the
one pack log, original review, source/tests/package files, or shared plan bytes.

## Exact repair

1. Freeze the current log at SHA-256
   `a15031aa4ae1dc640075409858eb0c8e7602858fa0f49c5115b0ac244162bec6`
   with exact byte count and deterministic preimage copy/hash.
2. Recover the exact omitted raw `duplicate dependency references` field from
   the original `npm run desktop:pack` execution-tool transcript. Restore it
   byte-for-byte at the line-83 suppression marker and preserve every byte
   before and after the marker. Do not regenerate, approximate, reconstruct
   from a later command, or rerun packaging. If the complete field is not
   recoverable from retained actual output, fail closed.
3. Freeze recovered-field bytes/hash, restored full-log bytes/hash, and exact
   prefix/suffix identity. Prove the suppression marker is absent, the exact
   custom electronDist line and all terminal embedded gates remain, and the
   no-download/GitHub/release-assets scan still passes.
4. Change R19's top-level result to distinguish passed build/package/
   empirical/procedure-staging subscope from retained non-PASS validation.
   Calibrate only directly dependent wording and log hash/completeness claims.
   Preserve the cure as not PASS and the fresh review's 504 classification;
   make no product/proof/lifecycle/release claim.
5. Run only read-only hash, prefix/suffix, marker, whitespace, JSON, diff,
   containment, inventory, and empty-index checks. No pack/build/test/
   precheck/preflight/network/provider/proof command.
6. Write `repair-cycle-1/executor/RETURN.md` with exact before/field/after
   hashes and paths. Preserve original executor return and review untouched.

Terminal outcome is `REPAIR_PASS_PENDING_FRESH_REVIEW` or exact blocker.
