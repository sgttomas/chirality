# TASK RUN — QA item 20 per-row disposition, DEL-01-06

- **Date:** 2026-07-26
- **Authority:** `D-PEC-66` act 3 (RULED 2026-07-26 at creation), sealed Agent 2 dispatch, file-tool-only
- **Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 and `skills/scope-of-work/SKILL.md` matrix row-semantics constraint
- **Write scope:** `ScopeOfWork.md` (Output and Evaluation Matrix rows only) and this run record
- **Flagged rows expected / found:** 2 / 2 — no discrepancy

## Test applied

A matrix row is *flagged* when it carries ≥2 `AC-*` refs and ≥2 `VER-*` refs
(the `derive_review_checklist.py` P7 warning shape). Because checklist
derivation is row-scoped, every `VER` in a row is assigned to every `AC` in that
row. The disposition test is therefore per-AC × per-VER: **CONFORMS** only when
every pair is a genuine verification relation; **OVER-LINKED** when any `AC`
would inherit a `VER` that does not verify it.

## Per-row dispositions

| Row | Output | ACs | VERs | Disposition |
|---|---|---|---|---|
| M-1 | OUT-001 | AC-001, AC-002, AC-005 | VER-001, VER-002, VER-005 | **OVER-LINKED** — repaired by split |
| M-2 | OUT-002 | AC-003, AC-004, AC-005 | VER-003, VER-004, VER-005 | **OVER-LINKED** — repaired by split |

### Row M-1 — per-pair reasoning (9 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-001 × VER-001 | yes | VER-001 validates the documented format against the default instance and the malformed-fixture set — exactly AC-001's accept/reject property. |
| AC-001 × VER-002 | **no** | VER-002 asserts registered-loop count/identity and additive extensibility; AC-001 claims nothing about instance content or extensibility. |
| AC-001 × VER-005 | **no** | VER-005 inspects the dependency manifest and import graph; it evaluates no format documentation or validation behaviour. |
| AC-002 × VER-001 | **no** | VER-001 checks schema conformance of the instance, not that exactly one loop is registered at P1 nor that no unnamed loop appears. |
| AC-002 × VER-002 | yes | VER-002 asserts one registered loop at P1 identified as PEC v2's own build and confirms additive-only extension — AC-002 verbatim. |
| AC-002 × VER-005 | **no** | Dependency and network inspection says nothing about registered-loop content or staging. |
| AC-005 × VER-001 | **no** | Format validation cannot establish the absence of a third-party runtime dependency or a network call. |
| AC-005 × VER-002 | **no** | Instance inspection cannot establish zero-dependency or locality. |
| AC-005 × VER-005 | yes | VER-005 is the dependency-manifest and import-graph inspection AC-005 states. |

### Row M-2 — per-pair reasoning (9 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-003 × VER-003 | yes | VER-003 runs the loader against invalid, unreadable, and absent fixtures and asserts an explicit located failure with no fallback — AC-003 exactly. |
| AC-003 × VER-004 | **no** | VER-004 exercises the consumer-facing interface on a valid configuration; it tests no rejection path. |
| AC-003 × VER-005 | **no** | Dependency and network inspection evaluates no loader failure behaviour. |
| AC-004 × VER-003 | **no** | Failure-path fixtures do not inspect the interface signature for path or serialization leakage. |
| AC-004 × VER-004 | yes | VER-004 exercises the interface and inspects its signature for configuration-path or serialization leakage — AC-004 exactly. |
| AC-004 × VER-005 | **no** | Dependency and network inspection says nothing about interface shape. |
| AC-005 × VER-003 | **no** | Loader rejection fixtures do not establish zero-dependency or locality. |
| AC-005 × VER-004 | **no** | Interface exercise does not establish zero-dependency or locality. |
| AC-005 × VER-005 | yes | As above. |

## Repair — before / after (content-preserving)

**Before (2 rows):**

```
| OUT-001 | SOW-094 OBJ-004 | REQ-001, REQ-002, REQ-006, CLM-004, CLM-005 | AC-001, AC-002, AC-005 | VER-001, VER-002, VER-005 | Format documentation, the checked-in default instance, the malformed-fixture set, and validation output showing accept/reject per fixture |
| OUT-002 | SOW-094 OBJ-004 | REQ-003, REQ-004, REQ-005, REQ-006, CLM-006 | AC-003, AC-004, AC-005 | VER-003, VER-004, VER-005 | Loader failure-path transcripts, the consumer-facing interface signature, and dependency-manifest plus import-graph inspection records |
```

**After (6 rows, 1:1 AC↔VER):**

```
| OUT-001 | SOW-094 OBJ-004 | REQ-001, CLM-004 | AC-001 | VER-001 | Format documentation, the checked-in default instance, the malformed-fixture set, and validation output showing accept/reject per fixture |
| OUT-001 | SOW-094 OBJ-004 | REQ-002, CLM-005 | AC-002 | VER-002 | The checked-in default instance |
| OUT-001 | SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
| OUT-002 | SOW-094 OBJ-004 | REQ-003 | AC-003 | VER-003 | Loader failure-path transcripts |
| OUT-002 | SOW-094 OBJ-004 | REQ-004, REQ-005, CLM-006 | AC-004 | VER-004 | The consumer-facing interface signature |
| OUT-002 | SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
```

## Preservation record

- **AC set unchanged:** AC-001..AC-006, each still mapped. AC-005 remains
  attached to **both** OUT-001 and OUT-002, exactly as before, so its derived
  `output_refs` are unchanged.
- **VER set unchanged:** VER-001..VER-006, each still referenced.
- **Requirement/claim refs:** union preserved exactly. M-1's
  {REQ-001, REQ-002, REQ-006, CLM-004, CLM-005} redistributed as
  AC-001→{REQ-001, CLM-004}, AC-002→{REQ-002, CLM-005}, AC-005→{REQ-006}.
  M-2's {REQ-003, REQ-004, REQ-005, REQ-006, CLM-006} redistributed as
  AC-003→{REQ-003}, AC-004→{REQ-004, REQ-005, CLM-006}, AC-005→{REQ-006}.
  REQ-006 appears twice, as it did before.
- **Evidence expectation:** cell text redistributed verbatim to the row whose
  method produces it. Two cosmetic changes, disclosed: a fragment moved to the
  start of a cell has its first letter capitalized to match cell convention
  ("the checked-in default instance" → "The checked-in default instance";
  "dependency-manifest plus import-graph inspection records" →
  "Dependency-manifest plus …"). The AC-005/VER-005 evidence phrase, which
  existed only in M-2's cell, now appears in both AC-005 rows because AC-005
  was already carried in both rows; no new wording was authored.
- **Untouched:** frontmatter, every heading, every OUT/CLM/REQ/AC/VER/CON/TBD/AX
  definition, all prose, the OUT-003 matrix row, table formatting, and column
  headers. `_STATUS.md` not touched.

## Derived-checklist effect (deriver re-run is the dispatcher's)

| AC | Methods before | Methods after |
|---|---|---|
| AC-001 | VER-001, VER-002, VER-005 | VER-001 |
| AC-002 | VER-001, VER-002, VER-005 | VER-002 |
| AC-003 | VER-003, VER-004, VER-005 | VER-003 |
| AC-004 | VER-003, VER-004, VER-005 | VER-004 |
| AC-005 | VER-001, VER-002, VER-003, VER-004, VER-005 | VER-005 |
| AC-006 | VER-006 | VER-006 |

No AC loses its method; no AC is orphaned; the P7 multi-AC/multi-VER warning no
longer fires on this contract.
