# Brief — R2 PKG-02 verifier shard (TASK, Type 2, evidence-only)

**Role.** Fresh TASK (Type 2). Do not delegate. Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2,
package PKG-02. You check selected ledger items against evidence. **You never edit any ledger, notes,
reverse or errata file.** Your verdicts are evidence for the manager, not rulings.

**Placeholders** (values in your dispatch prompt; never write the values into outputs): `<SHARD>`
(e.g. `SHARD-01`), `<UNIT>` (the deliverable, e.g. `DEL-02-03`), `<FROZEN_TREE>`, `<RUN>`,
`<PKG>` = `<RUN>/R2/PKG-02`.

## Inputs

- `<PKG>/_verify/<SHARD>.csv`: your items (`Unit,Class,ClaimKey,CapabilityID,ErrataField,Reason`).
- `<PKG>/<UNIT>/`: `<UNIT>_claims.csv`, `_notes.md`, `_reverse.csv`, `_reverse_notes.md`,
  `_errata.csv` (if present), `REVERSE_AREAS.md`, `REVERSE_INPUT_capabilities.csv`.
  Read CSVs with scripts (e.g. `python3 -c` with the `csv` module), pulling only your items' rows.
- `<RUN>/CONVENTIONS.md` in full (the rulebook you grade against); `<RUN>/RUN_BASIS.md` §3, §5 and
  addenda.
- Evidence pack `<PKG>/EVIDENCE_PACK/` (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES, DECISION_HITS,
  D-APP-127 map).
- `<RUN>/R2/SURFACES/<AREA>_capabilities.csv` for class-c items.
- The frozen tree `<FROZEN_TREE>`: deliverable files, code, tests, decision register and rulings,
  governing docs.
- You may consult `<RUN>/R0_CALIBRATION/VERIFICATION.md` §4 for R0 patterns. Do not read R0 ledgers or
  any other package's R2 folder.

## Reading discipline

Frozen tree only for deliverables and code; never the working repository's deliverable folders; never
read, list or grep `projects/chirality-runtime/execution/**` (exclude it explicitly; scope greps to `packages/` and `tests/`). Do not read other
units' folders under `<PKG>` or other packages' folders. Git: only read-only
`git -C <FROZEN_TREE> log|show|blame -L`. No installs, no tests. No absolute paths in outputs. Write
only your two shard files.

## Shared grading key (applies identically across all PKG-02 shards)

For each item, open the cited evidence and give exactly one verdict:

- `CONFIRMED`: the row's Disposition, CauseTag, evidence citations and other checked fields hold (for
  class c: the capability-to-claim response holds; for class e: the ProposedValue is right).
- `REFUTED`: something does not hold. **A wrong citation, gloss, tag or token whose Disposition holds is
  REFUTED on that field** (Field ≠ Disposition). Give the correct reading and evidence.
- `CONTESTED`: reasonable either way under the conventions; give both readings.

Checks, in order:
1. **Disposition** against evidence and §2.6, including the `STALE_SPECIFICATION` / `REMAINING_STATE_MISMATCH` tie-break (RUN_BASIS Addendum 5; `ALSO:<verdict>` when both fit) (MR-8: ACCEPTED_DIVERGENCE needs text acknowledging the
   gate **and** a GOVERNING ruling; RETIRED_BY_RULING needs a governing ruling naming the item;
   snapshot-true claims are REGISTER rows).
2. **Reachability (§2.3):** code evidence carries `REACH=` matching `REACHABILITY.csv`; a requirement
   met only on a LEGACY_ONLY path is judged on the live path. Treat a reach tag contradicting the pack
   as REFUTED on ImplementationEvidence unless the row gives a code-verified reason. The pack is
   import-based and module-level: a module LIVE by static import whose relied-on symbol is never
   rendered/called/constructed on the product path (e.g. retired Pipeline/Workbench/Portal
   presentation) must be judged on what the product actually does; if the worker treated such a
   symbol as live behaviour and that changes the Disposition, REFUTE the Disposition; otherwise
   record it as a field-level point.
3. **MR-11 / AUTHORITY_CONFLICT (§1):** MR-11 only where the ruling explicitly addresses the clause or
   deliverable; DIRECTIVE §0 order resolves where it can; otherwise AUTHORITY_CONFLICT with R4/R4-Qn.
   **Legacy-versus-live subject test (CONVENTIONS §2.4, RUN_BASIS Addendum 6)** is graded as written:
   subject decided from the claim text (product behaviour unless the claim names one code unit and
   only its own contract; ties → product behaviour, judged on the live path); `R4-Q1` is required on
   every row whose only meeting code is `REACH=LEGACY_ONLY` and must not be cited for that reason on
   rows met by LIVE code or with no code evidence; product-behaviour rows met only by legacy code need
   `ALSO_MODULE:<verdict>` in Notes. Q2 = K-ENGINE-2 conformance, Q3 = status_transition actor,
   `R4-Q4` = v3 four-role adoption versus SPEC §7/§13 and the persona/matrix contracts (Addendum 4); `R4-Q5` = Codex event payloads stored as received vs translated (Addendum 7). Ledgers sealed before Addendum 7 may carry plain `R4` there; that is not a refutation.
   The App DIRECTIVE §2.8 was never amended for D-GOV-43: check that the worker applied DIRECTIVE §0's
   order rather than assuming the Codex-only preambles win.
4. **DirectionEvidence:** `CTX:`/`GOV:` prefix correctness (CONTEXT vs GOVERNING per RUN_BASIS §5);
   `NONE_FOUND` only after a named register + CONTEXT search; spot-check that search yourself
   (`_REGISTER.md`). UNRECORDED_JUDGMENT requires DirectionEvidence NONE_FOUND.
5. **CauseTag:** §4 vocabulary and precedence (mechanism > PRE_V3_DRIFT > UNRECORDED_JUDGMENT).
6. **AuthorityTier:** highest source restated; NOT_APPLICABLE rules.
7. **PostReleaseBasis:** for cited files in TOUCHED_PATHS, blame the lines.
8. **MechanicallyUnblocked / gates** (§2.5, MR-6 App-surface rule; `MOOT:` for retired premises).
9. **AssessmentEvidence** token (MR-1).
10. **Line anchors:** checked at the frozen tree; drift of ≤ 6 lines with the right symbol is not a
    refutation (note it in ConventionIssue).
Many items share evidence: open it once, but give each item its own verdict line.

**Verdict fields (RUN_BASIS Addendum 3).** Only `Disposition` (ledger or errata row) and the reverse
`Response` (including the claim it names) are verdict fields. Name the exact field in `Field` (one
field per line; if a row is wrong on both the Disposition and another field, use `Disposition` and
mention the other in CorrectReading). For a class-c item refuted on the named claim, use
`Response`.

## Outputs (under `<PKG>/_verify/`)

1. `V-<SHARD>.csv`, header exactly
   `Unit,Class,ClaimKey,CapabilityID,Verdict,Field,RowValue,CorrectReading,Evidence,ConventionIssue`,
   one line per SHARD item in the same order, then a final line `#END`. `Field` = the field at issue
   for REFUTED/CONTESTED (`-` when CONFIRMED); `RowValue` = the ledger's value (for class e: the
   ProposedValue); `CorrectReading` (both readings separated by ` || ` for CONTESTED; `-` when
   CONFIRMED); `Evidence` = repo-relative `path:line`; `ConventionIssue` = rule misapplied or
   ambiguous, else `-`. Quote fields with commas properly (use the csv module to write).
2. `V-<SHARD>_notes.md`: (i) counts by verdict and class; (ii) systematic patterns with example keys;
   (iii) effort.

## Return (≤ 5 lines)

Counts by verdict; disposition-level REFUTED keys; top 3 patterns; SHA-256 of `V-<SHARD>.csv`.
