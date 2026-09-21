# RETURN: EXT worker W_DOC_REL (item 4, release documents)

- **Worker:** TASK (Type 2).
- **Run:** RUN_D128_CONCORDANCE_2026-09-21_1614Z, R2 extension, wave 5.
- **Delegation:** none.
- **Basis:** frozen tree `00115c719`.

## Ledgers (sealed)

### DOC-BUILDREL (`docs/BUILD_AND_RELEASE.md`)

- **Rows:** 48 rows over 15 units.
- **Top dispositions:** ALIGNED 32, STALE_SPECIFICATION 13, NOT_AUDITABLE 2, UNKNOWN 1.
- **Confidence:** 1 LOW row (`#9.5`).
- **Validator:** `RESULT PASS errors=0 warnings=0`
- **SHA-256:** `114fc8140e0b62e2248872d04e01d222801b872736b472b5541b8a806bf4470f`

### DOC-RQGATES (`docs/RELEASE_QUALITY_GATES.md`)

- **Rows:** 23 rows over 14 units.
- **Top dispositions:** ALIGNED 14, STALE_SPECIFICATION 6, PARTIALLY_IMPLEMENTED 1, AUTHORITY_CONFLICT 1 (R4-Q5),
  NOT_AUDITABLE 1.
- **Validator:** `RESULT PASS errors=0 warnings=0`
- **SHA-256:** `114304029c9d01300c1a1a52fa1ee6a76fa4fc77cf88cba33959459ffa1dc6c2`

### DOC-RQRUN (`docs/RELEASE_QUALITY_RUNBOOK.md`)

- **Rows:** 7 rows over 7 units.
- **Top dispositions:** ALIGNED 6, STALE_SPECIFICATION 1.
- **Validator:** `RESULT PASS errors=0 warnings=0`
- **SHA-256:** `b5dbe9c69261ca7f2ebaae2f7eeb597f28e315346c8495a6e9e6a86e2bfa8996`

**Notes files:** `DOC-BUILDREL_notes.md`, `DOC-RQGATES_notes.md` and `DOC-RQRUN_notes.md`. No errata.

## For the manager's summary

### RELEASE_PROCESS_NOT_RUN rows (7)

- **BUILDREL#4.7 and #7.4, packaged Agent SDK proof.** It cannot pass on an A2 package, and no v3 build record
  runs it.
- **BUILDREL#9.3, notarization of v3.0.1.** `package.json` is at 3.0.1 (`cf4653526`), and I found no 3.0.1
  notarization or publication record.
- **BUILDREL#9.5, packaged S-6/S-8.** Neither check is recorded on the published v3.0.0 App. The row is UNKNOWN
  and LOW.
- **BUILDREL#11, hosted release job and attestation.** `desktop-release-template.yml` hard-fails at its S0 block
  step, so the hosted release job cannot run.
- **BUILDREL#12 and RQGATES#12, attestation and a wider release matrix.** No evidence shows either ran.

### Processes that did run (these rows are not flagged)

- Developer ID signing.
- Manual notarization and stapling.
- GitHub publication of v3.0.0 on 2026-09-13, per `PUBLIC_RELEASE_20260913.md`.

Several sections still describe these processes as "future" or "open", or name v2.0.0 as the current release.
Those sections are marked STALE_SPECIFICATION: BUILDREL#1, #12, #14 and RQGATES#12.

## Items for the manager to resolve

1. **New CauseTag.** `OTHER:DUPLICATE_TEST_RETIREMENT` is used on RQRUN#2 and needs reporting.
2. **R4 citations.**
   - R4-Q1: BUILDREL#4.6, #4.7, #4.16 and RQGATES#2.3, #6.
   - R4-Q5: RQGATES#5. This is an AUTHORITY_CONFLICT between the §5 restatement of K-ENGINE-4 and §7 of the
     same document.
3. **Undocumented commands.** Twelve shipped npm commands are missing from the BUILDREL §4 command map. They are
   listed in the BUILDREL notes §4. The split rule gives such omissions no row type.
4. **CI premerge evidence.** Section 8 runs in CI against the legacy stub engine (`controlled-ci-runtime.ts`), so
   the release-quality evidence does not exercise the Codex path. This is relevant to R4-Q1 and R4-Q2.
