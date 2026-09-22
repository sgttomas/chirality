# T7 — Cross-package findings and coverage gaps

Read `_COMMON.md` first. Then read every `<RUN>/R2/PKG-*/PACKAGE_SUMMARY.md` (hand-written
sections: cross-package observations, coverage gaps, method friction), `<RUN>/R2/EXT/EXT_SUMMARY.md`
§§5–6, `<RUN>/R2/EXT/R3_OBSERVATIONS.md`, and grep the `*_reverse_notes.md` of the ledgers of
record (listed in `<RUN>/R3/INPUT_MANIFEST.md`) for "gap", "no forward row", "no row", "unowned",
"not indexed", "missing".

**Output 1 — `<RUN>/R3/COVERAGE_GAPS.csv`.** Every coverage gap a manager or worker reported:
work items or SoW scope with no forward row, records with no index unit (for example PKG-00's
control records), capabilities no deliverable owns that a manager called out, and indexed scope a
worker could not own. Header:
`GapID,PackageID,DeliverableID,GapType,Description,SourceRecord,RelatedKeys`
- `GapID`: `GAP-001`…; `GapType`: `NO_FORWARD_ROW|NO_INDEX_UNIT|UNOWNED_CAPABILITY|UNOWNED_WORK_ITEM|OTHER`.
- `SourceRecord`: run-relative path and section of the report you took it from.
- `RelatedKeys`: `;`-separated ClaimKeys or CapabilityIDs, or empty.
De-duplicate gaps reported twice; keep both sources in SourceRecord.

**Output 2 — `<RUN>/R3/CROSS_PACKAGE_FINDINGS.csv`.** Header:
`FindingID,Category,Summary,Packages,ClaimKeys,Evidence,SourceRecords`
- `FindingID`: `XPF-001`…
- `Category`: `DUPLICATE_OWNERSHIP|INCOMPATIBLE_OWNERSHIP|SHARED_SURFACE|INCONSISTENT_DECISION|INCONSISTENT_TERMINOLOGY|RULED_NOT_APPLIED|STALE_VERIFICATION|LIFECYCLE_REMAINING_DEFECT|REGISTER_DEFECT|LIVE_PATH_RECURRING`.
- Cover at least: duplicate or incompatible ownership of the same capability across packages
  (compute from `<RUN>/R3/REVERSE_CONCORDANCE.csv`: capabilities with CLAIMED_BY from deliverables
  in two or more packages; report the notable ones as findings and the full list as
  `<RUN>/R3/_work/T7_SHARED_CAPS.csv`); inconsistent decisions or terminology across packages;
  RULED-but-not-applied decisions (D-APP-127 carriers — use
  `<RUN>/R2/_shared/EVIDENCE_PACK/D-APP-127_APPLICATION_MAP.csv`; D-APP-99, 101, 121, 125.1 from the
  `DEC:` rows in `EXTENSION_CONCORDANCE.csv`); stale verification (validation that exercises only the
  legacy harness; tests expecting behaviour contrary to amended SPEC); lifecycle and Remaining-state
  defects that recur; register defects (the `_REFERENCES.md` hash mismatches in
  `REFERENCE_HASHES.csv`, the multiple `decomposition_basis` pins, D-APP-112 item B's unregistered
  basis, the DepClosure pointer note in RUN_BASIS §5); and live-path findings that recur across
  packages (unredacted event storage K-EVENT-6, unenforced protected paths K-DOMAIN-2 with PKG-06's
  path and hook rows, the human gate and status transition R4-Q3, scaffolding returning 501, the
  legacy-session migration).
- `ClaimKeys`: find the affected rows by script in `CLAIM_CONCORDANCE.csv` /
  `EXTENSION_CONCORDANCE.csv`; list them all (`;`-separated) — these keys are used to build clusters.
- `Evidence`: short, with repo- or run-relative paths. No options or recommendations.

**Output 3 — `<RUN>/R3/_work/T7_NOTES.md`** (≤ 60 lines): counts by category and GapType, and the
search terms used for each live-path finding's key list.
