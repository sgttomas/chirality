# DEL-01-04 reverse-pass notes (R2, PKG-01)

The sealed ledger's SHA-256 is unchanged: `bcc4a3d16ca575af7801c5d5acdc95c34dd5910cff36bfc3a36809455fa0b27b`.

## Responses

- **Scope of the reverse file:** one row per capability, 365 in all. The files were concatenated in the order given: BUILD 41, ELECTRON 35, HARNESS 60, RTCONTRACT 53, RTCORE 50, SETTINGS 42, SHELL 45, WORKSPACE 39.
- **Counts:** CLAIMED_BY 0, PARTIAL 43, NOT_MINE 322.
- **Why there is no CLAIMED_BY:** DEL-01-04 is a DOC_UPDATE boundary register. It owns boundary statements, not code capabilities. Every capability that bears on a boundary row is therefore PARTIAL, and the implementation belongs to DEL-04, DEL-05, DEL-09, DEL-10 or a Runtime deliverable.
- **PARTIAL rows grouped by ledger key:**

| Ledger key | Boundary | Capabilities |
|---|---|---|
| CLM-003.4 | Remote MCP/plugins | RTCORE-004, RTCORE-005, RTCORE-030, SHELL-038, SETTINGS-016 |
| CLM-003.5 | Shipped bypass | RTCONTRACT-019, RTCORE-028, SETTINGS-030, SHELL-025, HARNESS-031 |
| CLM-003.7 | Packaging | BUILD-008, BUILD-009, BUILD-016 |
| CLM-003.8 | Domain contracts | RTCONTRACT-040, RTCONTRACT-041 |
| CLM-006.1 | Application-owned tools | RTCONTRACT-034, RTCONTRACT-035, RTCORE-033 |
| CLM-006.5 | Domain carve-in | HARNESS-053, HARNESS-054, HARNESS-055, BUILD-039, BUILD-040 |
| CLM-006.6 | Pi/provider/residency | 14 capabilities |
| CLM-010.6 | Event log | HARNESS-038 |
| STATE-2 | Claude "current path" remnants | HARNESS-028, HARNESS-033, RTCONTRACT-053, RTCORE-003, RTCORE-048, SETTINGS-009 |

## Errata (2 rows, both ImplementationEvidence; no Disposition change)

- **CLM-003.8.** I tagged `contracts/src/harness/domain-profile.ts` REACH=LIVE. CAP-RTCONTRACT-040 shows it is LIVE only through the contracts barrel and has no non-test consumer, so the tag should be REACH=TEST_ONLY. I had not confirmed the symbol-level reach in pass 1. The row stays ALIGNED, because the exclusion holds by absence on the live path.
- **CLM-006.6.** I described the Pi packages as `dependencies`. At the frozen basis they are `devDependencies`, and so are `@chirality/engine-pi-omlx` and the Claude SDK packages. The row stays STALE_SPECIFICATION, because the Pi adapter code and packages still exist, contrary to BR-006.

**Census, sealed versus errata-applied:** identical. There are 67 rows and the Disposition, CauseTag and HumanDecisionNeeded counts are unchanged. For example, the Disposition counts are ALIGNED 22, STALE_SPECIFICATION 15, NOT_AUDITABLE 13, AUTHORITY_CONFLICT 12, PARTIALLY_IMPLEMENTED 4 and REMAINING_STATE_MISMATCH 1, both sealed and after errata.

## Reach and state disagreements (no erratum needed)

- **CAP-BUILD-016 (signing).** Signing is DISABLED by default, and no notarization step exists anywhere in the BUILD area. My CLM-003.7 Notes attribute "the consolidated candidate is signed and notarized" to the CONTRACT/PRD preambles and to BUILD_AND_RELEASE line 43. That attribution is accurate as a documentary claim. The code only supports optional signing, so the docs' "signed and notarized candidate" has no notarization code behind it. This is a finding for the release deliverables (PKG-09), not a DEL-01-04 erratum. CLM-003.7 stays ALIGNED, because ordinary unsigned/unnotarized output is exactly the K-RELEASE-1 target.
- **CAP-SHELL-025.** The Permissions selector, including "Full access", renders only in the woven presentation, which is the live one. The default operator mode is `workspaceWrite`, which maps to approval `never` plus `workspace-write`. That differs from the new-project default D-GOV-43 item 4 recommends (`on-request` with `workspace-write`). It is additional evidence for the CLM-003.5 conflict cluster (policy posture) and does not change a sealed field.
- **REACHABILITY.csv versus the capability files.** CAP-RTCORE-048 is UNREACHED and CAP-RTCONTRACT-040/041 are TEST_ONLY, while the pack marks all three LIVE because of barrel re-exports. The capability files are right. My ledger cites RTCORE-048 nowhere, and cites RTCONTRACT-040 only on CLM-003.8 (erratum above).
- **Consistent with my tags:** CAP-RTCONTRACT-053 (engine-claude LEGACY_ONLY UNREACHED), CAP-HARNESS-031, 034 and 055 (LEGACY_ONLY, DISABLED), and CAP-RTCORE-005, CAP-RTCONTRACT-019 and CAP-RTCORE-028 (LIVE, ENABLED).
- **CAP-BUILD-015.** The packaged dependency boundary forbids the Claude SDK, Pi and engine packages from the shipped bundle. This supports the LEGACY_ONLY and TEST_ONLY tags on STATE-2 and CLM-006.6.

## Coverage gaps (no forward row owns them; not errata)

- **Application-owned dynamic tools:** CAP-RTCORE-033 and CAP-RTCONTRACT-034/035, added post-release in `da95ec194` and `cb08dbe2f`.
  - The capability is LIVE and ENABLED in the App-owned Runtime composition. It is limited to the owning-application client, and no App code registers tools.
  - It is a tool-extension point relevant to SOW-065 / FR-105 ("plugin-like extension points") and to BR-005 (domain-engine integration; SWBPIPE is the first intended consumer).
  - I answered PARTIAL against CLM-006.1 for the boundary aspect only. No DEL-01-04 row states whether this surface is inside or outside current scope, so the boundary register needs a row or an owner decision.
- **The user's shared Codex configuration** (D-GOV-43 item 3, CAP-RTCORE-005). This is the Codex-era counterpart of the SOW-076 "ambient settings" boundary. The register has no row for it (as noted in the pass-1 notes).
- **CAP-SHELL-025's default operator mode.** No DEL-01-04 row covers the default approval/sandbox posture. It sits under the CLM-003.5 conflict but deserves its own boundary statement once the R4 ruling lands.
