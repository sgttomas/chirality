# DEL-09-04 — reverse pass notes (merged P1 + P2 ledger)

- **Ledger answered for:** the merged `DEL-09-04_claims.csv` (76 rows, SHA-256 `be6f865c…4d9374`, unchanged).
- **P1 part ledger:** SHA-256 `8f24ab0c…5ad0f4`, unchanged.
- **Capability files, in order:** BUILD, ELECTRON, HARNESS, RTCORE, WORKSPACE (225 rows in total).

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 9 |
| PARTIAL | 17 |
| NOT_MINE | 199 |

- **BUILD** carries most of the ownership: 7 CLAIMED_BY and 12 PARTIAL. The packaging chain, Codex staging and pin, afterPack, the signing hook, version identity and the icon are covered.
- **ELECTRON** has 4 PARTIAL:
  - Codex path hand-off;
  - service instruction root;
  - renderer egress;
  - working-root picker.
- **RTCORE** has 2 PARTIAL:
  - the service-side Codex version gate;
  - the sandbox network mapping.
- **WORKSPACE** has 1 PARTIAL: the folder picker, via procedure step 9.
- **HARNESS** (the legacy in-process harness) is entirely NOT_MINE. The live packaging path uses none of it. The legacy packaged SDK probes are scripts, answered under BUILD.

## Errata (2 rows, no Disposition change)

1. **CLM-004.4 Notes: blame correction flagged in pass 1.** Line 109 of `codex-supervisor.ts` blames to `1cb09c09d`, not `95364569a`. PostReleaseBasis stays NO.
2. **CLM-009.8 ImplementationEvidence: missing live evidence added.** `app-owned-composition.ts:117-124` refuses to start the Codex app-server unless the packaged `codex --version` equals the pin. I found this through CAP-RTCORE-002.
   - The Runtime service does execute the packaged Codex on the live path.
   - The row stays PARTIALLY_IMPLEMENTED: there is still no packaged run record and no secret or network assertion.
   - Cited lines 117-124 are outside the TOUCHED_PATHS ranges for that file.

**Census, sealed and errata-applied side by side:**

| Disposition | Sealed | Errata-applied |
|---|---:|---:|
| All dispositions | as sealed | identical |

Both errata change evidence and Notes only, so no verdict field changes.

## REACH and STATE comparison with the capability files

Where the files and the ledger agree:

- **Signing hook** (`sign-electron-runtime-v2.mjs`): CAP-BUILD-016/017 give REACH=LIVE, STATE=DISABLED. The ledger gives REACH=LIVE with `DISABLED_BY_DEFAULT`.
- **`verify-version-identity.mjs`**: CAP-BUILD-018 gives LIVE, a standalone script not in `desktop:dist`. The ledger says the same.
- **`generate-macos-icon.mjs`**: both give LEGACY_ONLY/UNREACHED.

One difference:

- **`run-network-policy-proof.mjs`.** CAP-BUILD-029 tags it TEST_ONLY (a manual proof npm script). P2's CLM-017 tags it `REACH=LEGACY_ONLY`.
- I side with the ledger, and wrote no erratum:
  - No packaging entry invokes the script, so under the brief's reach rule it is not LIVE.
  - It is not reached only by a test either: `proof:network-policy` is an npm script.
  - Its allowlist targets only the retained Anthropic path (`run-network-policy-proof.mjs:20`), which is what LEGACY_ONLY denotes.
  - Under the A0 rule (UNREACHED takes LEGACY_ONLY) the ledger tag is the defensible one.
- **R3 should check one thing.** If CLM-017 relies on this script for the network item, R4-Q1 applies only if no LIVE code meets that item. The live `codex-supervisor.ts` sandbox mapping arguably does, so R4-Q1 should not follow automatically.

## Coverage gaps (not expressible as errata)

- **CAP-BUILD-001/002 (Next and Electron production build).** `desktop:dist` requires these outputs but does not run the build; `desktop:prepare` does. No DEL-09-04 row owns "the build before packaging". CLM-016 (procedure) touches it only indirectly.
- **CAP-BUILD-010 (Electron fuses).** Hardening that ships in the DMG. DEL-09-04 claims it only through the asar trade-off (CLM-023.2). The owner is likely the security deliverable (DEL-09-06).
- **OUT-001 (SoW L22) and the SoW frontmatter.** Carried over from the P1 notes: still unindexed.
