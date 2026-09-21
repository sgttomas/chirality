# DEL-05-05: reverse-pass notes (R2, PKG-05)

Capability files, answered in this order: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL.
Together they hold 370 rows.

The sealed ledger's SHA-256 is unchanged: `858bd152506b5ea0220f796244e6b49542684552e7f610e8e3e9d18c77c0d152`.

## Responses

- **Totals:** 1 CLAIMED_BY, 10 PARTIAL, 359 NOT_MINE.
- **CLAIMED_BY:** CAP-HARNESS-048 (the legacy tool-result artifact store) → CLM-005.
- **PARTIAL:** these capabilities each have another primary owner. DEL-05-05 covers only its tool-result or artifact slice:
  - CAP-HARNESS-032 → CLM-010.2 (mapper call to persist artifacts)
  - CAP-HARNESS-038 → CLM-012.6 (legacy JSONL log used by the replay fixtures)
  - CAP-HARNESS-027 → CLM-010.6 (redaction)
  - CAP-RTCONTRACT-042 → CLM-010.12 (resultBudget thresholds)
  - CAP-RTCONTRACT-021 → CLM-010.5 (artifact-link projection)
  - CAP-RTCONTRACT-020 → CLM-010.8 (malformed-tail replay)
  - CAP-RTCORE-017 → CLM-010.9 (append ordering)
  - CAP-RTCORE-025 → CLM-010.4 (live truncation mechanism)
  - CAP-SETTINGS-042 → CLM-026 (deprecated tool-descriptor facade)
  - CAP-SHELL-040 → STATE-1 (ToolStreamView artifact semantics, per D-APP-70)

## Errata (4 rows; no Disposition changes)

1. **CLM-003 ImplementationEvidence.** The facade `frontend/packages/harness-contract/src/tool-descriptor.ts` should be
   tagged `REACH=TEST_ONLY`, not `REACH=LEGACY_ONLY`. CAP-SETTINGS-042 shows its only importer is
   `harness-contract-rollback.test.ts`. The sealed Notes word "UNREACHED" for this facade is therefore also inaccurate.
2. **CLM-010.12 ImplementationEvidence.** The runtime threshold constants in `tool-descriptor.ts:183-199` should be
   `REACH=LEGACY_ONLY`, not `REACH=LIVE`. CAP-RTCONTRACT-042 shows `resultBudget` is consumed only by legacy
   `lib/harness` files; under the symbol rule in the brief, a symbol no live entry calls is not live. The facade tag
   changes to TEST_ONLY as in erratum 1.
3. **CLM-026 ImplementationEvidence.** Same two corrections as erratum 2.
4. **CLM-026 HumanDecisionNeeded.** `NO` becomes `R4-Q1`. After erratum 3, the only code that meets the claim is
   LEGACY_ONLY (Addendum 6, rule 3).

## Census, sealed vs errata-applied

Dispositions are identical in both, because no erratum changes a Disposition:

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 14 |
| STALE_VERIFICATION | 12 |
| PARTIALLY_IMPLEMENTED | 9 |
| DOCUMENTED_UNIMPLEMENTED | 8 |
| ALIGNED | 7 |
| NOT_AUDITABLE | 7 |
| IMPLEMENTED_DIFFERENTLY | 2 |
| REMAINING_STATE_MISMATCH | 1 |

HumanDecisionNeeded changes after the errata:

| Value | Sealed | Errata-applied |
|---|---:|---:|
| NO | 26 | 25 |
| Rows citing R4-Q1 | 33 | 34 |

## Coverage gaps (for the manager; not expressible as errata)

- **No live producer of tool-result artifacts.** No capability row in any of the eight files describes one. RTCORE-017
  and RTCORE-025 persist Codex tool events without budgeting, artifact storage or redaction. The requirement still stands
  under CONTRACT K-EVENT-7 and SPEC 9.2. After SCA-APP-005, the owner of that requirement is Runtime/Root, and DEL-05-05
  owns only the App consumption and conformance side. No forward row owns the missing producer as work to do; it is
  recorded as a coverage gap in the pass-1 notes.
- **No redaction before persistence on the live path.** Amended K-EVENT-6 requires structural redaction before
  persistence. No capability provides it: ELECTRON-035 and RTCORE-004/013 redact e-mail addresses in diagnostics only.
  This gap is shared with DEL-05-02 and DEL-05-03; DEL-05-05 covers it only on CLM-010.6 and CLM-010.7.
- **Mis-anchored ToolStreamView ownership.** D-APP-70 assigns DEL-05-05 the artifact semantics of the
  `ToolStreamView` in CAP-SHELL-040. The SoW has no unit for it, so it is anchored on STATE-1 as PARTIAL.
