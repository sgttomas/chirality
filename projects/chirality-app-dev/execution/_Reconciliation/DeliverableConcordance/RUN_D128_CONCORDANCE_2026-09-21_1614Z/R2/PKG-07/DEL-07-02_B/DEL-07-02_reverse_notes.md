# DEL-07-02 — reverse-pass notes (worker B, pass 2)

## Inputs, results and seal

- **Capability files**, answered in this order: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS and WORKSPACE `_capabilities.csv`. That is 364 capability rows.
- **Responses:** CLAIMED_BY 3, PARTIAL 4, NOT_MINE 357.
- **CLAIMED_BY:**
  - CAP-HARNESS-052 → CLM-005.
  - CAP-ROUTES-021 → CLM-009.9.
  - CAP-SETTINGS-035 → CLM-009.11.
- **PARTIAL:**
  - CAP-HARNESS-022 → CLM-009.9.
  - CAP-RTCORE-023 → CLM-003.
  - CAP-RTCONTRACT-049 → CLM-009.9.
  - CAP-RTCONTRACT-023 → CLM-010.
- **Errata:** none, so there is no errata file. The sealed and errata-applied census figures are therefore identical; see the forward notes, §1.
- **Seal:** the claims SHA-256 is unchanged at `ddea31e03f538b77d5e1f28b482a02507c3104010cc2971b84d19e139d9da0b1`.

## REACH and STATE disagreements with the ledger or the pack

- **CAP-ROUTES-021 (`STATE=ENABLED (endpoint)`):** the endpoint is served, but on the live path the operation behind it fails. CAP-RTCORE-023 is `STATE=DISABLED`: its `RuntimeService.scaffold` returns 501 because `app-owned-composition.ts:226` passes no scaffold port. My ledger records this as CLM-009.9 PARTIALLY_IMPLEMENTED, with the live-gap rows DOCUMENTED_UNIMPLEMENTED. The two capability files are consistent with each other only when they are read together.
- **CAP-RTCONTRACT-049 (`STATE=ENABLED`):** this is true on the client side only. The server side is disabled, as for CAP-RTCORE-023.
- **CAP-HARNESS-052 (`REACH=LEGACY_ONLY`):** this agrees with the ledger, and both disagree with the pack's `REACHABILITY.csv`, which tags `scaffold.ts` LIVE through the type-only import.
  - One difference in detail: the capability says the "execution code [is] reached only through legacy mcp/read-tools.ts".
  - That holds only for `previewScaffoldExecutionRoot`.
  - `scaffoldExecutionRoot`, the writer, has no caller outside tests, even from `read-tools.ts`. The ledger's UNREACHED note is the narrower statement for the writer.
- **CAP-HARNESS-022 (`REACH=LIVE`, `STATE=DISABLED`):** this agrees with the ledger. The client function is live-imported, but its only renderer caller, PipelineSurface, is unmounted.
- **CAP-SETTINGS-035 and CAP-SETTINGS-029:**
  - CAP-SETTINGS-035 notes that containment is checked against any bound project, although the error text names the app-dev project.
  - CAP-SETTINGS-029 describes a multi-folder routing port that routes by execution root.
  - The ledger (CLM-004.1, CLM-009.11) cites the containment check in `runtime-daemon-harness-port.ts` against the configured or bound project's `canonicalRoot`, and that citation still holds. The test name quoted in the ledger ('fixed app-dev project') reflects the older single-project wording.
  - Neither point changes a verdict, so I raised no erratum.
- **CAP-WORKSPACE-031 (`STATE=DISABLED`, RETIRED-UNMOUNTED):** this agrees with the ledger's note that no rendered UI calls the route.

## Coverage gaps

- **Forward rows owning a capability:** every capability I judged to belong to DEL-07-02 has an owning forward row. No capability exposed a DEL-07-02 behaviour without one.
- **Capability that owns nothing:** no capability describes the accepted-v3.2 parser boundary. HARNESS-052 folds the parser into the scaffold module and does not record that the parser rejects the accepted decomposition. That finding lives only in the ledger (CLM-005, CLM-009.13, CLM-014.1).
