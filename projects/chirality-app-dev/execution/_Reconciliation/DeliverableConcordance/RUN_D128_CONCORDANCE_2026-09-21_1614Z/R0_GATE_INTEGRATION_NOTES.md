# R0 gate integration notes — RUN_D128_CONCORDANCE_2026-09-21_1614Z

> **From:** R0 gate integration TASK (Type 2), dispatched by HELP_HUMAN.
> **Basis:** the owner's R0 gate ruling of 2026-09-21 (being transcribed as D-APP-129),
> items A–D, as stated in `BRIEFS/R0_GATE_INTEGRATION_TASK.md`.
> **Status:** integration work product. Items marked `[INTEG]` in `CONVENTIONS.md` are this
> TASK's integration details, not rulings.
> No R0 output, `CONVENTIONS_CANDIDATE.md` or `_scripts/claim_index.py` was modified.
> No git, install or network was used.

## 1. Outputs

| File | Role |
|---|---|
| `CONVENTIONS.md` | Adopted, self-contained R2 rulebook (§1–§7 integrated; §8 scope extension; §9 evidence pack; §10 R2 operating rules) |
| `_scripts/validate_ledger.py` | Validator v2 (edited in place) |
| `_scripts/test_validate_ledger.py` | pytest fixture suite for v2 |
| `_scripts/extension_index.py` | Deterministic extension-unit indexer |
| `R1_INVENTORY/EXTENSION_INDEX.csv` | Extension coverage checklist (221 units) |
| `R0_GATE_INTEGRATION_NOTES.md` | This file |

## 2. Mapping: §7 verdict → CONVENTIONS.md → validator rule

Validator rule IDs are the bracketed IDs printed by v2 (`ERROR [ID]` / `WARN [ID]`).

### 2.1 R0 report §7.1

| §7 row | Verdict | Landed in `CONVENTIONS.md` | Validator |
|---|---|---|---|
| MR-1 | REVISE | §2.3 `AssessmentEvidence`; §2.6 `STALE_ASSESSMENT` | `MR-1` (exactly one token; no other token's phrase; `STALE_ASSESSMENT` ⇒ `OVERTAKEN`). "NOT APPLICABLE only when no conclusion" and "non-reproducing MATCH ⇒ OVERTAKEN": prose only |
| MR-2 | ADOPT | §2.5 | `MR-2` (v1 rule kept) |
| MR-3 (replacement) | ADOPT | §2.3 `VerificationEvidence` | `MR-10` checks the `GATE-TRANSCRIPT(APP\|RUNTIME@sha)` form; "plus test file and case": prose only |
| MR-4 | REVISE | §2.2 "Repeated statements"; §3 census | `MR-4` (`SEE:<ClaimKey>` target exists in the ledger and has the same Disposition). "Earliest indexed unit": prose only |
| MR-5 | REVISE | §2.7 | `MR-5` (REGISTER_DEFECT ⇒ `REMAINING_STATE_MISMATCH` or `STALE_SPECIFICATION`). One-row-per-stale-hash: prose only (supported by §9 `REFERENCE_HASHES.csv`) |
| MR-6 | REVISE | §2.5 | `MR-6` (`MOOT:` must name `D-APP-nn`/`D-GOV-nn`; a MOOT row needs `MechanicallyUnblocked = NO`). App-surface rule: prose only |
| MR-7 | REVISE | §2.3 `LatestDecision` | `MR-7` (pattern `D-APP-nn`/`D-GOV-nn` [+ ` (context)`] or `NONE_FOUND`) |
| MR-8 | REVISE | §2.6 (i)–(iv) | `V-VOCAB` (`RETIRED_BY_RULING` added); `MR-8` (`RETIRED_BY_RULING` needs a governing `LatestDecision`). (i), (ii), (iv): prose only |
| MR-9 | ADOPT | §2.3 `AssessmentEvidence` | prose only |
| MR-10 | REVISE | §2.4 VerificationEvidence tokens | `MR-10` (at least one recognised token or `NONE_FOUND`; malformed `HASH-RECOMPUTE`, `REACHABILITY`, `GATE-TRANSCRIPT`, `RUN-INSPECTION` rejected) |
| MR-11 | REVISE | §1 "Authority handling" | `MR-11` (`AUTHORITY_CONFLICT` ⇒ `HumanDecisionNeeded` contains `R4` or `R4-Qn`). Explicit-address test and DIRECTIVE §0 order: prose only |

### 2.2 R0 report §7.2

| §7 row | Verdict | Landed in `CONVENTIONS.md` | Validator |
|---|---|---|---|
| 25-column schema, `#END`, repo-relative paths | ADOPT | §2.1 | `V-SCHEMA`, `V-ABS`, `V-KEY`, `V-DUP`, `V-CLAIMID`, `V-DELID`, `V-COVERAGE`, `V-EMPTY` (v1 rules kept) |
| `CONTEXT_CLAIM` | REVISE | §2.3 `ClaimType` | `CTXCLAIM-DISP` (CONTEXT_CLAIM ⇒ `STALE_SPECIFICATION` or `NOT_AUDITABLE`); `W-NOTAUD` warning |
| `STATE_ASSERTION` | ADOPT | §2.3 `ClaimType` | `V-VOCAB` |
| AuthorityTier | REVISE | §2.3 `AuthorityTier` | `TIER-CONTEXT` (ruled); `TIER-NA` [INTEG]. "PRD only when highest source": prose only |
| `MechanicallyUnblocked` rename | ADOPT | §2.5 | `V-VOCAB`, `MR-2` |
| DirectionEvidence | REVISE | §2.3 `DirectionEvidence` | `DIR-PREFIX`; `W-DIR-SEARCH` (NONE_FOUND without a named search); `W-DIR-ALIGNED` |
| PostReleaseBasis | REVISE | §2.3 `PostReleaseBasis`; §7; §9 item 1 | `V-VOCAB` only (YES/NO); the blame procedure is prose only |
| CauseTag vocabulary | REVISE | §4 | `V-CAUSE` (`LIFECYCLE_GATE_PENDING` added), `V-CAUSE-NONE`, `CAUSE-UNRECORDED` [INTEG consequence], `CAUSE2`. Precedence: prose only |
| NOT_AUDITABLE | ADOPT | §2.6 | `V-VOCAB`; `V-CAUSE-NONE` exempts it |
| ImplementationEvidence reachability | REVISE | §2.3 `ImplementationEvidence` | `REACH` (code path cited ⇒ `REACH=LIVE\|LEGACY_ONLY\|TEST_ONLY`; bad values rejected). Live-path judging: prose only |
| ClaimKey splitting and run-local keys | REVISE | §2.2 | `V-KEY` (split suffix and run-local forms). Split criteria: prose only |
| Reverse pass | REVISE | §5.1 | `errata` mode: `ERR-FILENAME`, `ERR-LEDGER`, `ERR-KEY`, `ERR-FIELD`, `ERR-DUP`, `ERR-SEALED`, `ERR-PROPOSED`, `ERR-EVIDENCE`, and every row rule re-run on the errata-applied row; `REV-*` (v1 reverse rules kept) |
| Capability file | REVISE | §5.2 | `CAP-REACH`, `CAP-STATE` (tokens in Notes [INTEG]); `CAP-ID`, `CAP-POST`. Granularity: prose only |
| Double-blind check | ADOPT (1 per wave) | §10 | prose only |
| Validator (§6) | REVISE | §6 | CSV-record parsing (`V-SCHEMA`), `TIER-CONTEXT`, `DIR-PREFIX`, `errata` mode |
| `OTHER:<TOKEN>` | ADOPT | §4 | `V-CAUSE` |

### 2.3 Rulings B, C, D

| Item | Landed in `CONVENTIONS.md` | Validator |
|---|---|---|
| B (done-declaration CONTEXT only; Q-01..Q-13 to R4) | §1 item 3; §2.4; §10 | `HDN` rejects `Q-nn` as a HumanDecisionNeeded token |
| C (managers, evidence pack, wave order, double-blind, R4-Q1..Q3) | §2.4; §9; §10 | `HDN` (accepts `R4-Q1..R4-Q3`), `MR-11` |
| D (scope extension items 3–7) | §8 | `EXT-FILENAME`, `EXT-KEY`, `EXT-PKG`, `EXT-DEL`, `EXT-COVERAGE`, `W-AUDIT-ONLY` |

## 3. §7 text not integrated mechanically, and interpretations

1. **Errata cannot add a missing row.** The Reverse pass REVISE defines errata as field
   corrections (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`). A coverage gap found
   in pass 2 (R0 example: DEL-04-05's D-APP-72 oMLX work has no row) has no errata form;
   `CONVENTIONS.md` §5.1 routes it to reverse_notes. An owner or HELP_HUMAN choice is needed
   if gaps should be carried in errata (e.g. a `NEW_ROW` field).
2. **CONTEXT_CLAIM read literally.** The REVISE text allows `STALE_SPECIFICATION` or
   `NOT_AUDITABLE` only, so a checkable and still-true CONTEXT_CLAIM is `NOT_AUDITABLE`,
   not `ALIGNED`. The validator enforces the literal reading (`CTXCLAIM-DISP`); 9 of the 15
   R0 hits are ALIGNED CONTEXT_CLAIM rows; the other 6 carry divergent Dispositions. If the intended reading admits ALIGNED, delete
   one rule line.
3. **DirectionEvidence on NOT_AUDITABLE rows.** The brief says the `CTX:`/`GOV:` prefix
   applies to non-ALIGNED rows. The validator also exempts `NOT_AUDITABLE`, which records
   no divergence (the candidate gives such rows `NOT_APPLICABLE`). Stated as [INTEG] in §2.3.
4. **REACH has no "unreached" value.** The ruled vocabulary is `LIVE`, `LEGACY_ONLY`,
   `TEST_ONLY`. The §9 reachability map also records `UNREACHED` modules. §2.3 does not
   assign a tag for citing one; managers should report any such case as method friction.
5. **Index-side requests not actioned.** MR-9's optional old-ID → new-ID column and the
   splitting row's "R1 should emit REQ, AC and VER bullets as index units" both require
   changing `CLAIM_INDEX.csv` or `_scripts/claim_index.py`, which this brief forbids. The
   interim split rule in §2.2 covers the gap.
6. **Judgment rules stay prose.** The PostReleaseBasis blame procedure, the AuthorityTier
   "highest source" rule, the CauseTag precedence, MR-6 App-surface gates, MR-11's
   explicit-address test and the live-path judging of LEGACY_ONLY evidence cannot be
   checked without reading evidence. The verifier's shared grading key (§10) should cover
   them.
7. **`W-DIR-SEARCH` is a heuristic.** It looks for "search" or "grep" in Notes. It is a
   warning, not an error.
8. **Git permission versus RUN_BASIS.** `RUN_BASIS.md` §4 says children never run git. The
   adopted PostReleaseBasis REVISE requires read-only `git -C <frozen> blame -L`, and §9
   item 1 needs `git show`/`blame` from managers. `CONVENTIONS.md` §7 carries the ruled
   exception. `RUN_BASIS.md` is not this TASK's to edit, so HELP_HUMAN may want to note the
   exception there.
9. **Manager span superseded.** Report §9 proposed up to 10 forward workers per manager;
   Ruling C sets 4 concurrent children per manager and at most 3 concurrent managers.
   `CONVENTIONS.md` §10 follows Ruling C.
10. **Extension index unit choices** ([INTEG], §8): `RULED` means a State cell beginning
    `RULED`, giving 38 DEC units and excluding D-APP-116..119. A `#0` preamble unit is
    indexed for 9 of the 11 documents; `RELIANCE` and `TRACEABILITY` have no preamble
    text. `README` is the DOCID of `frontend/docs/harness/README.md` (uppercase stem, as
    ruled).

## 4. Extension index

`python3 _scripts/extension_index.py --frozen <FROZEN_TREE> --out R1_INVENTORY/EXTENSION_INDEX.csv`.
Two runs gave byte-identical output.

| Item | Units | Detail |
|---|---:|---|
| 3 `DEC` | 38 | D-APP-86..115 and D-APP-120..127 |
| 4 `DOC` | 58 | BUILDREL 15, RQGATES 14, VALSTRAT 9, RQRUN 7, RELIANCE 13 |
| 5 `SOW` | 84 | SOW-001..SOW-084 |
| 6 `DOC:PRODAGENTS` | 9 | |
| 7 `DOC` | 32 | README 7, TRACEABILITY 2, ADDING_A_TOOL 8, RUNTIME_ENGINE_CONTRACT 11, TOOL_CATALOG 4 |
| **Total** | **221** | |

## 5. pytest

`python3 -m pytest -p no:cacheprovider -q _scripts/test_validate_ledger.py` gave
**74 passed, 0 failed.** Each rule has at least one passing and one failing fixture.
`-p no:cacheprovider` and `PYTHONDONTWRITEBYTECODE=1` were used so that no cache files were
left in the run folder.

## 6. Validator v2 over the R0 calibration outputs (counts only; R0 outputs not edited)

**Ledgers.** `ledger` mode over the 9 sealed `*_claims.csv` files (579 rows):
**FAIL, 530 errors and 129 warnings.**

| Rule | Errors |
|---|---:|
| `REACH` (code cited without a REACH tag) | 308 |
| `DIR-PREFIX` (no `CTX:`/`GOV:` prefix on a divergent row) | 199 |
| `CTXCLAIM-DISP` (CONTEXT_CLAIM not STALE_SPEC/NOT_AUDITABLE) | 15 |
| `TIER-CONTEXT` (CONTEXT_CLAIM tier not NOT_APPLICABLE) | 7 |
| `MR-5` (REGISTER_DEFECT disposition) | 1 |
| All other rules (v1 rules, MR-1/2/4/6/7/8/10/11, HDN, CAUSE2, CAUSE-UNRECORDED, TIER-NA) | 0 |

Warnings: `W-DIR-SEARCH` 129.

| Ledger | Errors | Warnings |
|---|---:|---:|
| DEL-01-01 | 25 | 8 |
| DEL-02-05 | 71 | 12 |
| DEL-03-01_A | 58 | 20 |
| DEL-03-01_B | 79 | 10 |
| DEL-04-05 | 76 | 20 |
| DEL-06-04 | 66 | 19 |
| DEL-08-04 | 76 | 22 |
| DEL-09-07 | 32 | 0 |
| DEL-10-01 | 47 | 18 |

**Reverse files** (9, against `HARNESS_capabilities.csv`): PASS, 0 errors.
**Capability file** (`HARNESS_capabilities.csv`, 60 rows): FAIL, 120 errors (`CAP-REACH` 60,
`CAP-STATE` 60). The file records legacy status as free text (`LEGACY-IN-PROCESS:` on 31
rows), not as the new tokens.
**Errata:** R0 has no `_errata.csv` files, so there was nothing to validate.

These failures are expected. They are the new rules applied to ledgers written under the
candidate conventions, and they are not findings against the R0 workers.
