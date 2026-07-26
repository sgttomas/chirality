# TASK_RUN 2026-07-25 — D-PEC-65 register evidence repair (DEL-01-02)

- **Packet:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25, §3.1 repair method)
- **Actor:** sealed ephemeral Agent 2 (file-tool-only; no Bash, no git, no scripts), model `opus-5`
- **Write scope exercised:** `Dependencies.csv` (EXECUTION-row evidence cells only) + this run record
- **Rows in file:** 3 (2 ANCHOR read-only, 1 EXECUTION)

## Row dispositions

| DependencyID | Class | Defect class found | Disposition |
|---|---|---|---|
| DEP-01-02-001 | ANCHOR | n/a (read-only) | untouched |
| DEP-01-02-002 | ANCHOR | n/a (read-only) | untouched |
| DEP-01-02-003 | EXECUTION | EVQ-003 + EVQ-004 empty-evidence row (`EvidenceQuote` blank, `SourceRef` = `location TBD`) | **REPAIRED** (not waived — real quotable evidence found) |

## DEP-01-02-003 — cells changed

Edge `E-P17`: DEL-01-03 (Store bootstrap & content-minimal guard) → DEL-01-02
(Presence-tier schema & entity model). The D-PEC-62 exhibit row carried an empty
`BasisCitation`, which is why the seeder emitted the placeholder; the exhibit was
read as provenance only and is not cited.

- `EvidenceFile`
  - before: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` (the D-PEC-62 frozen exhibit — history only per D-PEC-62 §3.3)
  - after: `execution/_Decomposition/SOFTWARE_DECOMP.md` (rev 1.2 `current_basis`)
- `SourceRef`
  - before: `location TBD` (placeholder — the EVQ-004 defect)
  - after: `SOFTWARE_DECOMP.md section 2.1 IN-scope items - SOW-010 row`
  - Quote-free: contains no paired double-quote span, so the EVQ-002 `QUOTE_SPAN` test cannot fire.
- `EvidenceQuote`
  - before: empty (the EVQ-003 defect)
  - after: `store gitignored and safe to delete; presence tier expected lost on rebuild`
  - Verbatim, contiguous, character-for-character from the `SOW-010` row of the
    §2.1 IN-scope table in `SOFTWARE_DECOMP.md`. No reflow, no ellipsis, no
    paraphrase.

### Locus aptness

The claim in `Statement` is that the presence-tier schema is hosted by the same
store lifecycle that DEL-01-03 provides. SOW-010 states the store is gitignored
and safe to delete and that the presence tier is expected lost on rebuild —
i.e. presence-tier state resides in that same deletable store, whose gitignored
path management and safe-delete semantics are exactly DEL-01-03's scope
(SOW-056; `Deliverables.csv` DEL-01-03). The quote therefore warrants the
dependency of DEL-01-02 on DEL-01-03 without invention.

## Statement edits

**None.** The seeded `Statement` ("Presence-tier schema is hosted by the same
store lifecycle") states the dependency claim correctly and was left untouched.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` was created: real quotable
source text exists in accepted decomposition truth, so a waiver would have been
the dishonest option here.

## Untouched

All other cells (IDs, classes, targets, maturities, `SatisfactionStatus`,
`Confidence`, `Origin`, `FirstSeen`/`LastSeen`, `Status`, `Notes`). No rows
added, deleted, or reordered; 29 columns preserved (re-read and verified after
the edit).
