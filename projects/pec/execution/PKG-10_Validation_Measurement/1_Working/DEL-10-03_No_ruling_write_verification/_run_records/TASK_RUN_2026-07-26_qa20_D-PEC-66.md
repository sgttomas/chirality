# TASK RUN — QA item 20 per-row disposition, DEL-10-03

- **Date:** 2026-07-26
- **Authority:** `D-PEC-66` act 3 (RULED 2026-07-26 at creation), sealed Agent 2 dispatch, file-tool-only
- **Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 and `skills/scope-of-work/SKILL.md` matrix row-semantics constraint
- **Write scope:** `ScopeOfWork.md` (Output and Evaluation Matrix rows only) and this run record
- **Flagged rows expected / found:** 3 / 3 — no discrepancy

## Test applied

A matrix row is *flagged* when it carries ≥2 `AC-*` refs and ≥2 `VER-*` refs.
Checklist derivation is row-scoped, so every `VER` in a row is assigned to every
`AC` in that row. The disposition test is per-AC × per-VER: **CONFORMS** only
when every pair is a genuine verification relation; **OVER-LINKED** when any
`AC` would inherit a `VER` that does not verify it.

### The standing-assertion framing does not change the test

This contract is written under a brief-directed **standing** framing (§Purpose,
CLM-007, CON-001, AX-003): the verification has no completion state, every
method is re-run on every evaluated state, and a passing run is evidence for the
state it evaluated and no later state. That framing was read before judging, and
it is *temporal*, not *relational*. It says each method re-runs continuously; it
does not say every method bears on every criterion. Grouping AC-001 with AC-002
because both are continuing obligations would license exactly the inheritance
item 20 forbids — a checklist entry for AC-001 naming VER-002, a definition
audit that does not evaluate AC-001's pass/fail-with-location behaviour. The
split below preserves the standing character intact: each `VER` remains standing
by its own text and by the Praxeology preamble, which is untouched.

The `C-08` `STANDING_NODES` classification (arithmetic exclusion settled at
`D-PEC-62` §1(4); release-gating force unresolved and routed at AC-009) is
likewise untouched by this repair. The AC-007/VER-007 pair and the AC-009
`HUMAN_REVIEW` row keep their exact wording and their CON-001 references.

## Per-row dispositions

| Row | Output | ACs | VERs | Disposition |
|---|---|---|---|---|
| M-1 | OUT-001 | AC-001, AC-002 | VER-001, VER-002 | **OVER-LINKED** — repaired by split |
| M-2 | OUT-001 | AC-003, AC-004 | VER-003, VER-004 | **OVER-LINKED** — repaired by split |
| M-3 | OUT-001 | AC-005 | VER-005 | not flagged |
| M-4 | OUT-001 | AC-006, AC-007 | VER-006, VER-007 | **OVER-LINKED** — repaired by split |
| M-5 | OUT-001 | AC-008 | VER-008 | not flagged |
| M-6 | OUT-001 | AC-009 | HUMAN_REVIEW | not flagged |
| M-7 | OUT-001 | AC-010 | HUMAN_REVIEW | not flagged |

### Row M-1 — per-pair reasoning (4 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-001 × VER-001 | yes | VER-001 runs the suite against a conforming fixture and two violating fixtures and asserts pass/failure naming the offending operation and its schema element or route — AC-001 exactly. |
| AC-001 × VER-002 | **no** | VER-002 audits the recorded operative definition and traces classifications back to it; it asserts nothing about whether a violating state produces a located failure. |
| AC-002 × VER-001 | **no** | Fixture execution produces classifications but does not establish that the operative definition is recorded, cites `PEC-GAT-004` and §4.2, or that no outcome rests on an unrecorded reading of TBD-002. |
| AC-002 × VER-002 | yes | VER-002 is the definition inspection and classification trace AC-002 states. |

### Row M-2 — per-pair reasoning (4 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-003 × VER-003 | yes | VER-003 compares the evaluated operation set against schema and listener, seeds an unevaluated addition, and presents an unresolvable schema — AC-003's three clauses exactly. |
| AC-003 × VER-004 | **no** | Probe execution per access class evaluates refusal behaviour, not how the operation set was enumerated. |
| AC-004 × VER-003 | **no** | An enumeration audit issues no adoption-, ruling-, or direction-shaped probe and checks no persistence or class asymmetry. |
| AC-004 × VER-004 | yes | VER-004 issues the probes per access class, asserts refusal and non-persistence, and asserts a reported failure on a class-asymmetric seeded state — AC-004 exactly. |

### Row M-4 — per-pair reasoning (4 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-006 × VER-006 | yes | VER-006 presents a sequence of states, asserts a state-bound execution per state with no reuse, and invokes the binding interface against an unevaluated state — AC-006 exactly. |
| AC-006 × VER-007 | **no** | VER-007 asserts that a blocking verdict is returned; it does not assert state-bound executions, non-reuse, or the missing-evaluation report. The two methods meet at the withheld-check case but assert different properties of it — verdict character (AC-007) versus missing-evaluation reporting (AC-006). |
| AC-007 × VER-006 | **no** | VER-006 presents a release-candidate fixture but asserts execution binding, not that the mechanism returns an explicit blocking verdict. |
| AC-007 × VER-007 | yes | VER-007 submits a violating candidate and a withheld check and asserts an explicit blocking verdict in both — AC-007 exactly. |

## Repair — before / after (content-preserving)

**Before (rows M-1, M-2):**

```
| OUT-001 | SOW-025 OBJ-005 | REQ-001, REQ-002, REQ-011, CLM-001, CLM-002, TBD-002 | AC-001, AC-002 | VER-001, VER-002 | Fixture set with expected verdicts, suite output naming each offending operation and the schema element or route through which it is reachable, and the recorded operative definition read against the PEC-GAT-004 and §4.2 wording with its permitted-write enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-003, REQ-004, REQ-005, REQ-006, CLM-008, CLM-009, TBD-004, TBD-005 | AC-003, AC-004 | VER-003, VER-004 | Enumeration audit comparing the evaluated operation set against the obliged schema's declared shapes and the obliged listener's served operations, with reported failures for a seeded unevaluated addition and an unresolvable enumeration; plus probe transcripts per access class showing refusal, no persisted record, and a reported failure on a seeded class-asymmetric state |
```

**After (4 rows, 1:1 AC↔VER):**

```
| OUT-001 | SOW-025 OBJ-005 | REQ-001, REQ-011, CLM-001, CLM-002 | AC-001 | VER-001 | Fixture set with expected verdicts, suite output naming each offending operation and the schema element or route through which it is reachable |
| OUT-001 | SOW-025 OBJ-005 | REQ-002, TBD-002 | AC-002 | VER-002 | The recorded operative definition read against the PEC-GAT-004 and §4.2 wording with its permitted-write enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-003, REQ-004, CLM-009, TBD-004, TBD-005 | AC-003 | VER-003 | Enumeration audit comparing the evaluated operation set against the obliged schema's declared shapes and the obliged listener's served operations, with reported failures for a seeded unevaluated addition and an unresolvable enumeration |
| OUT-001 | SOW-025 OBJ-005 | REQ-005, REQ-006, CLM-008 | AC-004 | VER-004 | Probe transcripts per access class showing refusal, no persisted record, and a reported failure on a seeded class-asymmetric state |
```

**Before (row M-4):**

```
| OUT-001 | SOW-025 OBJ-005 | REQ-007, REQ-008, CLM-007, AX-003, CON-001 | AC-006, AC-007 | VER-006, VER-007 | Execution records binding each presented state — API-surface changes, an additional schema version, and a release-candidate fixture — to the run that evaluated it; a scratch-caller invocation of the suite's binding interface against an unevaluated state showing the missing evaluation reported rather than passed or silently skipped; and blocking-verdict demonstrations for a violating candidate and for a withheld check |
```

**After (2 rows, 1:1 AC↔VER):**

```
| OUT-001 | SOW-025 OBJ-005 | REQ-007, AX-003 | AC-006 | VER-006 | Execution records binding each presented state — API-surface changes, an additional schema version, and a release-candidate fixture — to the run that evaluated it; a scratch-caller invocation of the suite's binding interface against an unevaluated state showing the missing evaluation reported rather than passed or silently skipped |
| OUT-001 | SOW-025 OBJ-005 | REQ-008, CLM-007, CON-001 | AC-007 | VER-007 | Blocking-verdict demonstrations for a violating candidate and for a withheld check |
```

## Preservation record

- **AC set unchanged:** AC-001..AC-010, each still mapped to OUT-001 (the single
  output). Derived `output_refs` are unchanged for every criterion.
- **VER set unchanged:** VER-001..VER-008, each still referenced; both
  `HUMAN_REVIEW` cells (M-6, M-7) are byte-identical.
- **Requirement/claim refs:** union preserved exactly per split.
  M-1's {REQ-001, REQ-002, REQ-011, CLM-001, CLM-002, TBD-002} →
  AC-001{REQ-001, REQ-011, CLM-001, CLM-002}, AC-002{REQ-002, TBD-002}.
  M-2's {REQ-003, REQ-004, REQ-005, REQ-006, CLM-008, CLM-009, TBD-004, TBD-005} →
  AC-003{REQ-003, REQ-004, CLM-009, TBD-004, TBD-005},
  AC-004{REQ-005, REQ-006, CLM-008}.
  M-4's {REQ-007, REQ-008, CLM-007, AX-003, CON-001} →
  AC-006{REQ-007, AX-003}, AC-007{REQ-008, CLM-007, CON-001}.
  Nothing added, nothing dropped. REQ-004 and REQ-011 continue to appear in
  M-3 as before; REQ-008, CLM-007, CON-001, and AX-003 continue to appear in
  M-6 as before.
- **Evidence expectation:** each clause redistributed verbatim to the row whose
  method produces it. Cosmetic changes, disclosed: a clause moved to the start of
  a cell is capitalized ("the recorded operative definition …" → "The recorded
  …"; "probe transcripts …" → "Probe transcripts …"; "blocking-verdict
  demonstrations …" → "Blocking-verdict demonstrations …") and the joining
  ", and " / "; plus " / "; and " conjunctions are gone as a consequence of the
  split. No wording was authored, reordered within a clause, or deleted.
- **Untouched:** frontmatter, every heading, every definition, all prose
  including the `D-PEC-63` brief quotation and the SCA-002 Q1.7 quotations, the
  Praxeology standing preamble, matrix rows M-3, M-5, M-6, M-7, table
  formatting, and column headers. `_STATUS.md` not touched.

## Derived-checklist effect (deriver re-run is the dispatcher's)

| AC | Methods before | Methods after |
|---|---|---|
| AC-001 | VER-001, VER-002 | VER-001 |
| AC-002 | VER-001, VER-002 | VER-002 |
| AC-003 | VER-003, VER-004 | VER-003 |
| AC-004 | VER-003, VER-004 | VER-004 |
| AC-005 | VER-005 | VER-005 |
| AC-006 | VER-006, VER-007 | VER-006 |
| AC-007 | VER-006, VER-007 | VER-007 |
| AC-008 | VER-008 | VER-008 |
| AC-009 | HUMAN_REVIEW (unchanged) | HUMAN_REVIEW (unchanged) |
| AC-010 | HUMAN_REVIEW (unchanged) | HUMAN_REVIEW (unchanged) |

No AC loses its method; no AC is orphaned; the P7 multi-AC/multi-VER warning no
longer fires on this contract.
