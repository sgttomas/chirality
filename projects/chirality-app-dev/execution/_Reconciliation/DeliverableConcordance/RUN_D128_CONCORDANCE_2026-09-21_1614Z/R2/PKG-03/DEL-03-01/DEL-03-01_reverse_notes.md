# DEL-03-01 — reverse-pass notes

**Scope.** I answered 325 capability rows from seven files, in this order: BUILD, ELECTRON,
HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS. The results are 3 CLAIMED_BY, 10 PARTIAL and
312 NOT_MINE.

**Claimed rows.**
- **CAP-RTCONTRACT-036** (the engine port) is claimed by CLM-009.1.
- **CAP-RTCONTRACT-039** (the conformance suite) is claimed by CLM-005.4.
- **CAP-SETTINGS-042** (the harness-contract facade) is claimed by REM-1.

**Partial rows.** The PARTIAL rows are surfaces where DEL-03-01 owns only one aspect:
- the conformance and provider-neutrality question on the Codex adapter and its notification
  pass-through;
- the stub engine that tests still use;
- the Section 9 linkage;
- the harness-contract facade's dependency validator.

**No errata.** The capability notes support the sealed forward tags:
- CAP-RTCONTRACT-039 tags the suite TEST_ONLY, reached only through the barrel. This matches
  CLM-005.4.
- CAP-SETTINGS-042 and CAP-BUILD-022 tag the facade TEST_ONLY. This matches REM-1.
- CAP-RTCORE-003 and CAP-RTCORE-025 tag the Codex engine and its delegated adapter LIVE. This
  matches CLM-003.9 and CLM-005.6.

Sealed and errata-applied census figures are the same, because there is no errata file.

**No coverage gaps.** Every capability I would expect DEL-03-01 to own already has a forward row.
Owners of the other surfaces:
- the route and SSE proxy belongs to DEL-03-02 and DEL-03-03;
- the turn lifecycle and session lock belong to DEL-03-02;
- the Claude and Pi adapters belong to PKG-04.

**Seal.** The claims file SHA-256 is unchanged:
`a833e5b32dafc16c45dbc32a420e17f4c0122c17ae979cca09ecc446f2d6e820`.
