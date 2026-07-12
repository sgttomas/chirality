# DEL-07-06 concordance notes — Reference Hash and Snapshot Conventions (PKG-07, W3)

Type: `DOC_UPDATE`. This deliverable specifies documentation conventions (reference-hash handling, hash-bypass records, snapshot immutability, deterministic-tool continuity, CHANGE/SHA approval evidence). Conformance is documentation review of the four-document kit, cross-checked against live execution-tree tooling/snapshots and the reconciled REF-006 hash state. No frontend implementation surface is owned by this deliverable.

Source state: kit/registers inspected live in the current worktree at HEAD `74150b3a8`; the run's stated `frontend/` state is `fac46e33f`, byte-identical through `74150b3a8` per the W3 brief. Non-frontend live checks (docs/PRD.md shasum, `_Scripts/` tooling, snapshot folders) are cited `RUN-INSPECTION@74150b3a8`. No tests executed; no behavioral rows (documentary deliverable).

## Census

Total rows: 21.

By ClaimType:
- REQUIREMENT: 16 (DEL-07-06-REQ-001 .. REQ-016)
- EXCLUSION: 3 (EXC-001..003, from Specification "Out of scope" bullets, lines 16-18)
- REGISTER_DEFECT: 1 (REGISTER-1)
- REMAINING_WORK: 1 (REMAINING-1, ungated)
- ACCEPTANCE: 0 — Datasheet Attributes restate the REQ set; the only datasheet-distinct condition (the PRD hash warning) is stale and captured by REQ-014 + REGISTER-1 (MR-4 fold). Other Datasheet Conditions map to REQ-014/REGISTER-1 (PRD state), EXC-001 (retired scope), REQ-015/EXC-003 (human authority), and the human-owned `ResponsibleParty: TBD` (note only).
- IMPLEMENTED_UNMAPPED: 0 — the live tooling on this subject (`references_hash_tool.py`, `validate_dependencies.py`) is assigned to sibling deliverables DEL-08-01 / DEL-08-02 (per `_Scripts/README.md` headers and decomposition v3.2) — an accepted cross-deliverable mapping, not an unmapped surface for DEL-07-06 (W3 sibling-mapping rule).

By Disposition:
- ALIGNED: 19 (REQ-001..013, REQ-015, REQ-016; EXC-001..003; REMAINING-1)
- STALE_SPECIFICATION: 1 (REQ-014)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

Confidence: HIGH 20, MEDIUM 1 (REQ-013, self-flagged).

## Key finding — REF-006 (docs/PRD.md) reconciliation is landed but the kit + registers are stale

Identical in shape to the sibling DEL-07-04 finding. The whole kit still declares `docs/PRD.md` as `HASH_MISMATCH`: Specification REQ-014 + the pervasive "(with REF-006 hash warning)" source tags (lines 32-41), Datasheet References REF-006 (line 62 "HASH_MISMATCH source-state warning"), Guidance Considerations (line 30), Procedure step 1 (lines 13, 22), plus `Dependencies.csv` DEP-07-06-013 and `_DEPENDENCIES.md` line 29. But the deliverable's own `_REFERENCES.md` REF-006 (line 12) now records `ExpectedSHA256 == ActualSHA256 == ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`, Status **MATCH**, and a live `shasum -a 256 docs/PRD.md` this run reproduces exactly `ac35fba4...` (neither of the old mismatch pair `86cb6fb9.../fb1c73f7...` recorded in the INSP-03 Source-State Caveat). **D-APP-35** (2026-06-21, "Option A — Refresh accepted hash") accepted the current PRD as the intended basis and authorized the bounded downstream reference-refresh, which has landed in `_REFERENCES.md`. Consequences:
- REQ-014 → STALE_SPECIFICATION: its conditional warning ("until docs/PRD.md hash state is reconciled or accepted") is now discharged on both limbs (reconciled AND accepted); the kit's persisting warning language describes a superseded source state. D-APP-35 governs. HIGH.
- REGISTER-1 → REMAINING_STATE_MISMATCH: `Dependencies.csv` DEP-07-06-013 and `_DEPENDENCIES.md` line 29 contradict the same deliverable's `_REFERENCES.md` REF-006 MATCH (internal register inconsistency + metadata lag against D-APP-35). HIGH.

## REQ-012 / REQ-013 — INSP-03 PARTIAL overtaken by verified tooling

INSP-03 left REQ-012 and REQ-013 PARTIAL because tool availability was not checked in a docs-focused assessment. This run verified the accepted tooling exists, is indexed, and is locally executable: `execution/_Scripts/references_hash_tool.py` (reference-hash compute/verify/recompute + human-approved `--allow-bypass` writing `HASH_VERIFICATION_BYPASS.jsonl`) and `execution/_Scripts/validate_dependencies.py` (the "dependency linter"), both catalogued in `_Scripts/README.md`. Neither reactivates the PLAN §9 retired scope. Both are owned by DEL-08-01 / DEL-08-02, so their existence substantiates DEL-07-06's *documented convention* that the tooling remains available (REQ-012 ALIGNED HIGH) and indexed/executable when present (REQ-013 ALIGNED — self-flagged below). Also substantiates REQ-003/004/005 (out-of-folder hashing, bypass approval, bypass record surface) at the convention level. No `HASH_VERIFICATION_BYPASS.jsonl` exists in the tree because no bypass has been recorded — the MAY convention (REQ-005) is correctly documented, not violated.

## Snapshot conventions (REQ-006/007) are live

Timestamped immutable snapshot folders and mutable `_LATEST.md` pointers coexist in the live tree (e.g. `execution/_Reconciliation/DepClosure/CLOSURE_D53A_..._2026-07-11_0224Z` alongside `execution/_Reconciliation/DepClosure/_LATEST.md`; this very `RUN_D55_..._1904Z` folder). Prior accepted snapshots are not overwritten. ALIGNED HIGH.

## Least-confident rows (mandatory self-flag, with the flipping alternative)

- **REQ-013 (ALIGNED, MEDIUM).** The documented convention ("deterministic tools/scripts remain indexed and locally executable when present") is satisfied — the tools that exist are indexed in `_Scripts/README.md` and runnable. Alternative reading that flips it to **PARTIALLY_IMPLEMENTED** (INSP-03's original call): because exact registry membership for DEL-07-06 is intentionally `TBD` (REQ-016) and no owned slice has enumerated the full deterministic set, one could hold that "indexed" is only partially demonstrated. Kept ALIGNED because REQ-013 is a SHOULD-level convention about tools *when present*, and the TBD-membership aspect is REQ-016's separate (satisfied) control; the residual is captured in RemainingWork rather than as a scope gap.

Also flagged for the fan-in recheck (non-ALIGNED, already surfaced above): REQ-014 (STALE_SPECIFICATION) and REGISTER-1 (REMAINING_STATE_MISMATCH). Both rest on the same live-verified hash fact (`shasum docs/PRD.md == ac35fba4... == _REFERENCES.md MATCH`) plus RULING-RECORD(D-APP-35). The alternative that would flip both: if the `_REFERENCES.md` REF-006 refresh were somehow *not* an accepted reconciliation (e.g. an unauthorized edit), the kit's warning would still be current and REQ-014 would revert to ALIGNED/PASS with no register defect — but D-APP-35 explicitly authorized this refresh, so I judge the reconciliation accepted.

## Register-defect summary

- REGISTER-1 (HIGH): `Dependencies.csv` DEP-07-06-013 (REF-006 CONSTRAINT — Statement/Notes assert HASH_MISMATCH + "no reconciliation evidence found", SatisfactionStatus TBD) and `_DEPENDENCIES.md` Run Notes line 29 (`[WARNING] SOURCE_HASH_MISMATCH ... remains HASH_MISMATCH`) contradict the same deliverable's `_REFERENCES.md` REF-006 MATCH. Metadata lag against the D-APP-35 reconciliation. R5 repair: refresh both registers to MATCH.

Per the W3 brief rule, the bare Declared Upstream / Declared Downstream "TBD" sections in `_DEPENDENCIES.md` (lines 12-18) are human-owned declaration surfaces by design (SPEC §5.2) and are NOT emitted as register defects. Observation only: they remain TBD while the Extracted register holds 13 ACTIVE rows. Likewise `ResponsibleParty: TBD` (`_CONTEXT.md` Source Authority) is a human-owned act, not a defect. `Dependencies.csv` DEP-07-06-010 (`_STATUS.md` "target not read", satisfaction TBD) reflects the 2026-05-20 dependency-recording evidence-scope ruling, not a live-state lag — not rowed.

## Method notes / deviations

- No method deviations. 19-column header copied verbatim from the R0 exemplar (`DEL-02-01_claims.csv`); validated 21/21 data rows carry 19 columns. MR-1 (single AssessmentEvidence token OVERTAKEN/STILL CURRENT/NOT APPLICABLE on every row), MR-2 (SelectableUnderCurrentLoop=YES only on the one ungated REMAINING row; all others NO), MR-4 (Datasheet folded into REQ rows; 0 ACCEPTANCE), MR-5 (bare `REGISTER-1` ID), MR-6 (verbatim `UNGATED` on REMAINING-1), MR-7 (`D-APP-35` governs REQ-014/REGISTER-1; `D-APP-55` on the concordance REMAINING row), MR-10 (documentary rows use `documentary claim` + exact doc sections; verification vocabulary `RUN-INSPECTION@<sha>` / `RULING-RECORD(D-APP-35)`) all satisfied.
- `REQUIREMENT_INDEX.csv` listed both prefixed (`DEL-07-06-REQ-0nn`) and bare (`REQ-0nn`) IDs for this deliverable — an R1 index duplication, not a real doubling. The claim set was re-derived from `Specification.md` (16 requirements + 3 out-of-scope exclusions); no parser zero-scan gap applied here.
- `DECISION_INDEX.csv` has no DEL-07-06 row; D-APP-35 (REF-006) was found by direct search of `_Coordination/_DECISIONS/` and cross-confirmed against the sibling DEL-07-04 rows. Worth an R3 note that the decision index under-links D-APP-35 to the PRD-grounded PKG-07 deliverables.
