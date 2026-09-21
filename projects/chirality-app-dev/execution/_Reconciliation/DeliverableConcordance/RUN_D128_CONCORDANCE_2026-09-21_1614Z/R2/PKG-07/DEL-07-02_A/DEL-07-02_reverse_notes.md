# DEL-07-02 — reverse-pass notes (worker A)

The sealed ledger `DEL-07-02_claims.csv` is unchanged. Its SHA-256 is still
`a085ae8197e01bc1fef106a0ce21c23964f2675c65e22c0e095310caf68b7b3e`.

## Responses

- **Capabilities answered:** 364, across 8 files in this order: BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCONTRACT 53, RTCORE 50, SETTINGS 42, WORKSPACE 39.
- **CLAIMED_BY (4):**
  - CAP-HARNESS-052 → CLM-005
  - CAP-ROUTES-021 → CLM-009.9
  - CAP-RTCORE-023 → CLM-009.9
  - CAP-SETTINGS-035 → CLM-009.11
- **PARTIAL (4):**
  - CAP-HARNESS-022 → CLM-009.9
  - CAP-RTCONTRACT-004 → CLM-009.9
  - CAP-RTCONTRACT-049 → CLM-009.9
  - CAP-RTCONTRACT-023 → CLM-010
- **NOT_MINE:** 356. Four of these carry a named reason:
  - CAP-HARNESS-050: the `scaffold_preview` MCP tool belongs to DEL-06-03.
  - CAP-WORKSPACE-031: the pipeline scaffold form is UI presentation.
  - CAP-SETTINGS-024: `_STATUS.md` parsing belongs to DEL-07-04.
  - CAP-SETTINGS-029: the routing port is runtime-client plumbing.
- **Errata:** none. No errata file was written.

## REACH/STATE disagreements with the ledger or the pack

1. **CAP-HARNESS-052 tags `scaffold.ts` `REACH=LEGACY_ONLY`.**
   - Its reasoning is that execution code is reached only through the legacy `mcp/read-tools.ts`.
   - That holds at module level and for `previewScaffoldExecutionRoot`.
   - The ledger tags the write symbol `scaffoldExecutionRoot` as `REACH=TEST_ONLY`. Only tests and `__tests__/api/harness/fake-daemon-harness-port.ts:262` call it. `read-tools.ts` imports only the preview function, and `scripts/run-dapp52-live-llm-demo.ts` reaches only `read-tools`.
   - Both readings reject the pack's LIVE tag.
   - Consequence for R3: if the verifier takes the capability's module-level LEGACY_ONLY tag, Addendum 6 rule 3 would add `R4-Q1` to the CLM-009.x product-behaviour rows and to CLM-003, 005, 018, 029 and 014.2. I kept `NO` because rule 3 applies to the symbol that actually meets the claim. The forward notes (§2, §5) record this as the least-confident reading. It is not an erratum.
2. **CAP-SETTINGS-024 says the `lib/harness/scaffold.ts` execution path is `REACH=LEGACY_ONLY`.** The ledger's symbol-level reading is TEST_ONLY (see 1).
3. **CAP-ROUTES-021 is `STATE=ENABLED` (endpoint) and CAP-RTCORE-023 is `STATE=DISABLED`.** This agrees with the ledger: the route is served, but the Runtime has no scaffold adapter and returns 501.
4. **CAP-HARNESS-022 and CAP-WORKSPACE-031 are `STATE=DISABLED`.** This agrees with the ledger (the pipeline surface is not rendered, because `woven-dialogue-route.tsx:18` discards the `legacy` prop).
5. **CAP-RTCONTRACT-004 and CAP-RTCONTRACT-049 mark the scaffold route and client `STATE=ENABLED`.** That is true at the contract and client layer. Behind it, the composed service throws, so the end-to-end state is the disabled state recorded on CAP-RTCORE-023.
6. **CAP-SETTINGS-035 notes that the error text names the app-dev project even though any bound project is checked.** This does not change CLM-009.11.

## Coverage gaps

No capability showed a missing forward row. The forward coverage gaps in the notes (OUT-001 and the Output and Evaluation Matrix) stand.
