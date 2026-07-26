# TASK RUN — QA item 20 per-row disposition, DEL-08-01

- **Date:** 2026-07-26
- **Authority:** `D-PEC-66` act 3 (RULED 2026-07-26 at creation), sealed Agent 2 dispatch, file-tool-only
- **Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 and `skills/scope-of-work/SKILL.md` matrix row-semantics constraint
- **Write scope:** `ScopeOfWork.md` (Output and Evaluation Matrix rows only) and this run record
- **Flagged rows expected / found:** 1 / 1 — no discrepancy

## Test applied

A matrix row is *flagged* when it carries ≥2 `AC-*` refs and ≥2 `VER-*` refs.
Checklist derivation is row-scoped, so every `VER` in a row is assigned to every
`AC` in that row. The disposition test is per-AC × per-VER: **CONFORMS** only
when every pair is a genuine verification relation; **OVER-LINKED** when any
`AC` would inherit a `VER` that does not verify it.

## Per-row dispositions

| Row | Output | ACs | VERs | Disposition |
|---|---|---|---|---|
| M-1 | OUT-001 | AC-001, AC-005 | VER-001 | not flagged (1 VER) — no disposition required; checked anyway and sound |
| M-2 | OUT-002 | AC-002, AC-003, AC-004 | VER-002, VER-003, VER-004 | **OVER-LINKED** — repaired by split |
| M-3 | OUT-003 | AC-006 | VER-005 | not flagged |
| M-4 | OUT-001 | AC-007 | HUMAN_REVIEW | not flagged |

### Row M-2 — per-pair reasoning (9 pairs)

| Pair | Genuine? | One-line reasoning |
|---|---|---|
| AC-002 × VER-002 | yes | VER-002 exercises the access path per class and then with absent, malformed, unresolvable, and invalid tokens, asserting refusal with no partial or default-scoped result — AC-002 exactly. |
| AC-002 × VER-003 | **no** | VER-003 is a static identifier scan of source, config, and fixtures; it exercises no token resolution and no refusal path. |
| AC-002 × VER-004 | **no** | VER-004 inspects the token-mechanism seam boundary and substitutes a stub; it does not establish that every served operation is preceded by a token resolution. |
| AC-003 × VER-002 | **no** | Presenting one token per class shows the three classes resolve; it does not establish that the delivered set is *exactly* those three, nor the absence of retired v1.0/prototype role identifiers, which is the whole of AC-003's negative half. |
| AC-003 × VER-003 | yes | VER-003 scans for retired role identifiers and confirms the delivered access-class set is exactly owner, harness, and admin — AC-003 exactly. |
| AC-003 × VER-004 | **no** | Seam inspection evaluates no identifier inventory. |
| AC-004 × VER-002 | **no** | Token-resolution transcripts do not show whether the mechanism is reachable only through the declared seam. |
| AC-004 × VER-003 | **no** | An identifier scan does not demonstrate stub substitutability across the seam. |
| AC-004 × VER-004 | yes | VER-004 confirms the mechanism is reached only through the declared seam and that stub substitution changes no socket-server or access-class code — AC-004 exactly. |

### Row M-1 — recorded, not flagged

M-1 carries 2 ACs but a single VER, so it does not trip the P7 warning shape and
is outside this dispatch's repair mandate. It was nonetheless checked against
item 20's second clause: VER-001 enumerates the bound listeners and confirms a
Unix-domain-socket default **and** the absence of any TCP or otherwise
network-reachable listener, which is AC-001's positive half and AC-005's
negative claim ("No loopback or other TCP listener is delivered"). Both pairs
are genuine; **no edit**.

## Repair — before / after (content-preserving)

**Before (1 row):**

```
| OUT-002 | SOW-003 OBJ-001 | REQ-002, REQ-003, REQ-004, REQ-006, CLM-004, CLM-006 | AC-002, AC-003, AC-004 | VER-002, VER-003, VER-004 | Token-resolution transcripts for each access class and for each rejection case, an identifier scan of source/config/fixtures against the retired role sets, and the seam interface signature plus the stub-substitution diff |
```

**After (3 rows, 1:1 AC↔VER):**

```
| OUT-002 | SOW-003 OBJ-001 | REQ-002 | AC-002 | VER-002 | Token-resolution transcripts for each access class and for each rejection case |
| OUT-002 | SOW-003 OBJ-001 | REQ-003, REQ-004, CLM-004 | AC-003 | VER-003 | An identifier scan of source/config/fixtures against the retired role sets |
| OUT-002 | SOW-003 OBJ-001 | REQ-006, CLM-006 | AC-004 | VER-004 | The seam interface signature plus the stub-substitution diff |
```

## Preservation record

- **AC set unchanged:** AC-001..AC-007, each still mapped; each still attached to
  the same output.
- **VER set unchanged:** VER-001..VER-005, each still referenced; the M-4
  `HUMAN_REVIEW` cell is untouched.
- **Requirement/claim refs:** union preserved exactly.
  {REQ-002, REQ-003, REQ-004, REQ-006, CLM-004, CLM-006} redistributed as
  AC-002→{REQ-002}, AC-003→{REQ-003, REQ-004, CLM-004} (the access-class set and
  the retirement rule, with CLM-004's characterization of the three classes),
  AC-004→{REQ-006, CLM-006} (the seam requirement and the OI-006 envelope note
  that motivates it). Nothing added, nothing dropped.
- **Evidence expectation:** the three clauses of the original cell were
  redistributed verbatim to the row whose method produces each. Two cosmetic
  changes, disclosed: a clause moved to the start of a cell has its first letter
  capitalized ("an identifier scan …" → "An identifier scan …"; "the seam
  interface signature …" → "The seam interface signature …") and the two
  conjunctions ", " / ", and " that joined the clauses are gone as a consequence
  of the split.
- **Untouched:** frontmatter, every heading, every definition, all prose
  including the source-chain blockquotes, matrix rows M-1, M-3, and M-4, table
  formatting, and column headers. `_STATUS.md` not touched.

## Derived-checklist effect (deriver re-run is the dispatcher's)

| AC | Methods before | Methods after |
|---|---|---|
| AC-001 | VER-001 | VER-001 |
| AC-002 | VER-002, VER-003, VER-004 | VER-002 |
| AC-003 | VER-002, VER-003, VER-004 | VER-003 |
| AC-004 | VER-002, VER-003, VER-004 | VER-004 |
| AC-005 | VER-001 | VER-001 |
| AC-006 | VER-005 | VER-005 |
| AC-007 | HUMAN_REVIEW (unchanged) | HUMAN_REVIEW (unchanged) |

No AC loses its method; no AC is orphaned; the P7 multi-AC/multi-VER warning no
longer fires on this contract.
