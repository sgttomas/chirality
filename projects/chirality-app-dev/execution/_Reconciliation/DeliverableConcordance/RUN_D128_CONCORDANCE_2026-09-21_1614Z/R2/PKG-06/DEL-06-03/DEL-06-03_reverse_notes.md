# DEL-06-03 reverse-pass notes (pass 2)

This pass checked `DEL-06-03_reverse.csv` against eight capability files, in this order: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS and WORKSPACE. They hold 364 capabilities in total.

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 1 |
| PARTIAL | 13 |
| NOT_MINE | 350 |

- **CLAIMED_BY:** CAP-HARNESS-050 (the read MCP tools), owned by SEC-1.
- **PARTIAL:** each capability below maps to the forward row that covers the part DEL-06-03 owns.

| Capability | Forward row |
|---|---|
| CAP-HARNESS-031 | CLM-035.2 |
| CAP-HARNESS-052 | CLM-010.3 |
| CAP-HARNESS-056 | CLM-035.1 |
| CAP-HARNESS-057 | CLM-035.1 |
| CAP-RTCONTRACT-042 | CLM-010.4 |
| CAP-RTCONTRACT-044 | CLM-003 |
| CAP-BUILD-027 | CLM-012 |
| CAP-ROUTES-029 | CLM-010.13 |
| CAP-ROUTES-031 | CLM-010.11 |
| CAP-ROUTES-033 | CLM-010.12 |
| CAP-WORKSPACE-018 | CLM-010.13 |
| CAP-WORKSPACE-020 | CLM-010.11 |
| CAP-WORKSPACE-023 | CLM-010.15 |

All eight validator runs returned `RESULT PASS errors=0 warnings=0`.

## Errata

There is no errata file, so the sealed and errata-applied census figures are identical.

The sealed claims file is unchanged. Its SHA-256 is `144c7df45b57a4f1c3f70045feac1ccf14a8067df4ee5163b468f715d02bc569`.

## Observations for the manager and verifier (no errata filed)

### 1. Symbol-level reach of the runtime-contracts modules

- **What the capability files say.** CAP-RTCONTRACT-042 and CAP-RTCONTRACT-044 record `REACH=LEGACY_ONLY; STATE=DISABLED`. They reason that the only consumers of the descriptor registry and the tool-name vocabulary are legacy `lib/harness` modules. The evidence pack shows these modules as LIVE only because of the contracts barrel import.
- **What my ledger does.** It follows the pack's module-level map, as CONVENTIONS §2.3 [INTEG] requires. It tags `tool-names.ts` and `tool-descriptor.ts` as `REACH=LIVE` in these rows:
  - CLM-003;
  - CLM-010.1, .4 and .9;
  - CLM-014, CLM-020 and CLM-030;
  - CLM-035.1 and CLM-035.2;
  - SEC-1 and SEC-2.3.
- **Why no errata.** The tags comply with the rule. The ledger's findings already treat the tool surface as absent on the live path.
- **What would change under symbol-level reach.** Two rows would read slightly differently, and the verifier may choose that reading:
  - CLM-010.1 and CLM-010.4 could move from PARTIALLY_IMPLEMENTED to DOCUMENTED_UNIMPLEMENTED;
  - SEC-2.3 (the catalog-validation boundary, ALIGNED) would still hold at module level.

### 2. Scaffold preview

CAP-HARNESS-052 independently confirms the point in my ledger at CLM-010.3: `scaffold.ts` looks LIVE in the pack only because the scaffold route imports a type from it.

### 3. Dependency register read

- **What the capability file says.** CAP-WORKSPACE-023 notes that the live dependency route is served, but it has no live UI caller, because its client callers are retired and unmounted.
- **Why CLM-010.15 is unaffected.** It stays ALIGNED. REQ-06-03-015 concerns the read behaviour, and that behaviour is live and reachable through the route.

### 4. Live mechanism for Chirality tools

- **What exists.** CAP-RTCONTRACT-034, the application-owned dynamic tools contract, is the live mechanism through which Chirality tools could reach Codex. It is enabled, but no App code registers any tools through it.
- **Why no forward row covers it.** No DEL-06-03 claim covers it.
- **How it bears on the ledger.** It supports the alternative reading recorded for the AUTHORITY_CONFLICT rows in `DEL-06-03_notes.md` §2: the SDK-specific clauses could still be met on the Codex path, which would make those rows DOCUMENTED_UNIMPLEMENTED. Either reading still routes to R4-Q1.

### 5. Coverage gaps

None found. No capability that DEL-06-03 plausibly owns lacks a forward row.
