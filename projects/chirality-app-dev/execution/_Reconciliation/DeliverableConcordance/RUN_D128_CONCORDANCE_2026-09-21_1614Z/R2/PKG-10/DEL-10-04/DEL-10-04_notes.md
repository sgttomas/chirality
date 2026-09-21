# DEL-10-04 — forward-pass notes (R2, PKG-10)

Ledger: `DEL-10-04_claims.csv`, 58 rows. Validator: `RESULT PASS errors=0 warnings=0`.
Applied rules: CONVENTIONS as adopted, plus RUN_BASIS Addendum 4 (R4-Q4, not needed here) and
Addendum 5 (the STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break), both received from
the manager before sealing.

## 1. Census

**Units and split rate.** There are 34 indexed units (all CLM; no REM or REMTXT, and
`## Remaining` is empty). 4 of 34 units are split (12%), giving 52 rows from indexed units plus
6 run-local rows (REGISTER-1..4, STATE-1..2):

- CLM-004 → .1–.6, table rows;
- CLM-010 → .1–.12, one per REQ-001..012;
- CLM-016 → .1 ownership amendment, .2 AC-001;
- CLM-023 → .1 P45 note, .2 VER-001.

**Disposition, all 58 rows:**

| Disposition | All rows | Non-SEE rows | SEE rows |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 30 | 17 | 13 |
| PARTIALLY_IMPLEMENTED | 9 | 7 | 2 |
| ALIGNED | 7 | 6 | 1 |
| NOT_AUDITABLE | 5 | 5 | 0 |
| REMAINING_STATE_MISMATCH | 3 | 3 | 0 |
| ACCEPTED_DIVERGENCE | 1 | 1 | 0 |
| AUTHORITY_CONFLICT | 1 | 1 | 0 |
| IMPLEMENTED_DIFFERENTLY | 1 | 1 | 0 |
| UNKNOWN | 1 | 1 | 0 |
| **Total** | **58** | **42** | **16** |

**SEE rows** (MR-4 / Addendum 5 rule 3): 16 in total.

- 9 point to `REGISTER-1`: the REF-006 "is MATCH" restatements.
- 3 point to `CLM-007`: the repeated P45 note.
- 1 points to each of `CLM-003`, `CLM-004.1`, `CLM-004.5` and `CLM-004.6`.

**By ClaimType:**

| ClaimType | Rows | Dispositions |
|---|---:|---|
| STATE_ASSERTION | 22 | STALE 20; PARTIAL 1; ALIGNED 1 |
| REQUIREMENT | 21 | PARTIAL 8; ALIGNED 5; STALE 5; ACCEPTED_DIVERGENCE 1; AUTHORITY_CONFLICT 1; IMPLEMENTED_DIFFERENTLY 1 |
| CONTEXT_CLAIM | 8 | NOT_AUDITABLE 5; STALE 3 |
| REGISTER_DEFECT | 4 | REMAINING_STATE_MISMATCH 3; STALE 1 |
| ACCEPTANCE | 2 | ALIGNED 1; UNKNOWN 1 |
| EXCLUSION | 1 | STALE 1 |

No errata file exists; this is pass 1 only.

**One measure throughout.** Behavioural claims are judged on the live Codex product path.

- Only the inert contract types and guards are LIVE (`runtime-contracts` `domain-profile.ts`
  and `operation-proposal.ts`). No product code calls them.
- The domain registry, read, proposal and headless tools and the PEC bridge client are
  LEGACY_ONLY.
- Fixture and validation files under `_DomainEngines/**` are data, not code, so they carry no
  REACH tag.
- Test files are TEST_ONLY.

## 2. Least-confident rows (with the alternative reading)

- **CLM-004.6 / CLM-010.4** (PARTIALLY_IMPLEMENTED, FR-114). The OpenPipeStress-specific
  `domain_headless_preview_run` descriptor sits in public `runtime-contracts`. It has a const
  profileId and runner environment names (`tool-descriptor.ts:817-845`,
  `tool-catalog.ts:110-128`), while the runner itself is LEGACY_ONLY.
  - Alternative 1: ACCEPTED_DIVERGENCE, because D-APP-50 ruled the headless tool.
  - Alternative 2: ALIGNED, because registry-gated descriptors are an adapter layer and not
    "core runtime".
- **CLM-028** (IMPLEMENTED_DIFFERENTLY). The SoW's trade-off text says not to put OpenPipeStress
  concepts in public core runtime contracts, and the descriptor above does exactly that.
  Alternative: ACCEPTED_DIVERGENCE under D-APP-50, though the SoW text does not acknowledge that
  ruling.
- **CLM-016.1** (AUTHORITY_CONFLICT, R4). The D-APP-56 R4-P27 ownership of
  `_DomainEngines/profiles/pec.yaml` and its validation record conflicts with D-APP-58 lines
  76–77 and 102 and with SPEC §18: "this project never writes `_DomainEngines/**`" (F-APP-3),
  and the tier-0 bridge loop owns those writes. D-APP-58 does not name R4-P27. Alternative:
  "owns" means accountability for content and evidence, not write authority, which would make
  the row ALIGNED.
- **STATE-2** (STALE_SPECIFICATION). MEMORY.md keeps the "active code implementation is
  underway" wording, which D-APP-37 ruled false for `_STATUS.md`. Alternative: MEMORY is dated
  history outside the repair's scope, and staged code did land later, so there is no defect.

## 3. Register-defect summary

- **REGISTER-1** (STALE_SPECIFICATION): `_REFERENCES.md` MATCH hashes for CONTRACT, SPEC and PRD
  do not reproduce (`HASH-RECOMPUTE@00115c719`, pack rows Match=NO).
  - Last refresh was `23b3879b3` (2026-09-12). The documents changed later that day
    (`9eaddb596`, `7f1e9f387`).
  - SoW CLM-014 carries a third PRD hash (`ac35fba4…`), different from both the register value
    and the recomputed one.
  - Nine SoW rows restate "REF-006 is MATCH" as current. They are STALE_SPECIFICATION with
    `SEE:REGISTER-1` (Addendum 5 rules 1 and 3).
- **REGISTER-2** (REMAINING_STATE_MISMATCH): the `_DEPENDENCIES.md` summary table
  (SATISFIED 4 / PENDING 4), closure text and declared lists lag `Dependencies.csv`
  (7 SATISFIED / 1 PENDING).
- **REGISTER-3** (REMAINING_STATE_MISMATCH, `ALSO:STALE_SPECIFICATION`): rows DEP-10-04-006
  and -007 in `Dependencies.csv` are SATISFIED but keep TBD placeholders in their target and
  quote fields. The DEP-005 note cites the old PRD hash as MATCH.
- **REGISTER-4** (REMAINING_STATE_MISMATCH): `_STATUS.md` shows `Last Updated 2026-07-17`
  although it has a 2026-07-20 history entry, which is placed first.
- **Related findings outside the register files.** These are folded into CLM-016.1 and
  CLM-010.3/.12 rather than given separate register rows:
  - the `pec.yaml` header still reads "Candidate only. D-T0-27 is awaiting owner ruling" although
    D-T0-27 was applied (`b1074e7a4`) and profile_status is ADOPTED;
  - `pec.validation.json` predates the `ca49b846d` byte change and binds no hash;
  - `open_pipe_stress.validation.json` carries a machine-absolute `profile_path`.

## 4. Direction and cause

**Main CauseTags:**

| CauseTag | Rows | What it covers |
|---|---:|---|
| PRE_V3_DRIFT | 26 | Legacy four-document text preserved through the 2026-07-13 SoW v1 migration; D-APP-49..59 and D-APP-70 state changes (2026-07) never transcribed into the SoW body |
| DOC_HYGIENE | 11 | Reference hash drift and its restatements; VER-001 evidence absent |
| LIFECYCLE_GATE_PENDING | 6 | Future validation behind DEP-10-04-004 / D-APP-37 |
| CODEX_SOLE_ENGINE | 3 | Staged tools legacy-only; `_CONTEXT.md` still names Claude SDK as the current path |

**Secondary causes:** `CAUSE2:CARRIER_PROPAGATION` ×16 (the P45 note claims snake_case
alignment that commit `87b3589b8` never applied to the body), `CAUSE2:DOC_HYGIENE` ×4 and
`CAUSE2:RUNTIME_EXTRACTION` ×3.

**GOVERNING records used as `GOV:`:**

- D-APP-37: the doc-only acceptance profile. It permits CLM-010.5 as ACCEPTED_DIVERGENCE.
- D-APP-49 through D-APP-53, D-APP-56, D-APP-58, D-APP-59 and D-APP-70.
- D-GOV-43 and D-APP-127.

No CONTEXT (`CTX:`) record was needed.

**Searches behind each `NONE_FOUND`:**

- REF-006 and REGISTER-1 rows: a `_DECISIONS/_REGISTER.md` grep for a reference refresh after
  2026-09-12 found nothing. RUN_BASIS §5 lists corpus drift as a known basis defect.
- CLM-021 and CLM-023.2: a register grep for "ScopeOfWork v1" and "legacy source range" found no
  App ruling. The migration method is Root `workflows/scope-of-work`, which was not read (Δ10).
- Also consulted: the register rows for D-APP-37/38/45/49–59/70 and the ruling records for
  D-APP-37, D-APP-50 and D-APP-58; SPEC §18; TYPES §11; PRD §8.17; and `docs/harness/reliance_boundary_register.md`
  (`section9.domain_profile_validation`).

**R4 citations:**

- `R4-Q1` ×5, on the legacy-only staged tools and the OpenPipeStress descriptor.
- Plain `R4` ×1, on CLM-016.1, where two rulings conflict over `_DomainEngines` ownership.

**PostReleaseBasis** is NO on every row. None of the cited files is in `TOUCHED_PATHS.csv`; the
only PKG-10-adjacent touched path is a Runtime execution artifact, which was not read.

## 5. Method friction

- **SEE across differing restatements.** MR-4 SEE assumes the same normative statement.
  - CLM-003 (the attribute table) mixes the stale camelCase field list with FR-114 and
    K-DOMAIN rows that are dispositioned elsewhere. I dispositioned it on the field list and
    named the other rows in Notes.
  - Proposal: allow `SEE:` per sub-statement, or allow splitting attribute tables.
- **The CLM-012 verification table was not split.** Each of its checks restates a REQ row that
  is already split, so splitting it would have duplicated those rows.
- **Evidence outside the App and Runtime roots.** The deterministic profile validator is a Root
  tool (`tools/validation/…`). The code-path regex forces a REACH tag on it, so it carries
  `REACH=LEGACY_ONLY` with UNREACHED noted. Proposal: add a tag or wording for
  "Root tool, not a product module".
- **Rulebook changed mid-pass.** Addendum 5 arrived mid-pass. Under the pre-Addendum reading of
  MR-8(iv), I had planned REMAINING_STATE_MISMATCH for the REF-006 restatements; I applied the
  new rule before sealing.

## 6. Effort

- **Files read:** about 30, as full files or targeted ranges.
  - The deliverable: SoW, `_STATUS`, `_CONTEXT`, MEMORY, `_DEPENDENCIES`, `Dependencies.csv`,
    `_REFERENCES`, the assessment and four run records.
  - Two runtime contract modules, the registry, parts of the descriptor and catalog, and the
    test case lists.
  - The two profile YAMLs and their validation JSONs.
  - TYPES §11, SPEC §18, PRD §8.17, the CONTRACT K-rows and DIRECTIVE §0.
  - Three ruling records and the register rows.
- **Git:** read-only `log`, `show` and `blame -L` against the frozen tree.
- `_SEMANTIC*.md` and the 2026-05 TASK run records were not read (the SoW preserves their
  substance).
- **Context budget:** adequate, not tight.
