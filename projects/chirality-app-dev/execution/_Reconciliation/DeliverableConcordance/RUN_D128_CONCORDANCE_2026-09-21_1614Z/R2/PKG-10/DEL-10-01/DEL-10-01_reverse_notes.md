# DEL-10-01 — reverse-pass notes

- **Capability files answered (in order):** BUILD (41), ELECTRON (35), HARNESS (60), RTCONTRACT (53) and SETTINGS
  (42). That is 231 rows.
- **Responses:** 1 CLAIMED_BY, 3 PARTIAL, 227 NOT_MINE.
  - **CLAIMED_BY:** CAP-RTCONTRACT-040 (domain-profile contract) → CLM-016.1.
  - **PARTIAL:**
    - CAP-RTCONTRACT-041 → CLM-012.9. Only the profile's `operation_proposal_contract` block belongs here; the
      record contract belongs to DEL-10-03.
    - CAP-HARNESS-053 → CLM-016.1. The registry mechanism belongs here; the read tools are ruled D-APP-50/51
      surfaces.
    - CAP-SETTINGS-042 → CLM-016.1. Only the facade's domain-profile subpath relates here; the facade itself
      belongs to DEL-03-01.
- **Left NOT_MINE despite a domain link:**
  - CAP-HARNESS-054 (headless preview) and CAP-HARNESS-055 (pec proposal tools). The sibling PKG-10
    tool/fixture deliverables own these. DEL-10-01 cites them only as reach evidence in CLM-004.1.
  - CAP-RTCONTRACT-042/043/044 (tool descriptors, catalog and names).
  - CAP-BUILD-022 and CAP-BUILD-038..040 (facade purity; pec scratch, rehearsal and demo scripts).
- **Errata:** none. The reverse pass did not refute any sealed forward row.
- **Coverage gaps:** none found. Every capability that DEL-10-01's claims describe maps to an existing forward row.
- **Seal:** the claims SHA-256 is unchanged
  (`1162da3169b34110888ee1d0920e2a273ed2883a948c0dc0dbbd110ef8f8915a`).
