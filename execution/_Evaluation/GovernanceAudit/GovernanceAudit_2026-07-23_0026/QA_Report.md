# QA Report — Governance Audit

**Run:** GovernanceAudit_2026-07-23_0026
**Date:** 2026-07-23
**Result:** VALID

## Coverage

| Pass | Status | Files Scanned | Notes |
|---|---|---|---|
| 1 — Count Integrity | COMPLETE (revision-focused) | CONTRACT, AGENTS, agents directory, tool registry, explicit subjects | Canonical counts checked; unrelated stale-count expansion limited. |
| 2 — Cross-Reference | COMPLETE (revision-focused) | All explicit subjects | Changed references, citation keys, Chapter 3, glossary, README, and D.1–D.8 checked. |
| 3 — Invariant ID | COMPLETE (revision-focused) | Explicit subjects plus all `agents/AGENT_*.md` | Canonical K/R/I sets checked; unrelated semantic-orphan expansion limited. |
| 4 — Terminology | COMPLETE | Framework, thesis subjects, TYPES, SPEC | Operational terms, lifecycle, authentication, and gap distinction checked. |
| 5 — Agent Inventory | COMPLETE with limitation | AGENTS, agents directory, DBM | Filesystem and AGENTS agree at 33; DBM has no exhaustive current inventory table. |
| 6 — Hierarchy | COMPLETE | DIRECTIVE, CONTRACT, SPEC, TYPES, AGENTS, DBM, agents, skills, tools, professional standard | Protected-surface diff is empty; targeted coherence checks passed. |
| 6b — Claim Strength | COMPLETE | Framework, D-GOV-19, all explicit thesis subjects | Prohibited assertions and Appendix analogy boundaries checked. |

## Output validation

- Required files present: 5/5.
- Issue-log columns match the required schema.
- Issue rows: 0.
- Summary `total_issues`: 0.
- Severity counts sum to 0.
- Severity vocabulary: valid.
- Pass list accounts for 1, 2, 3, 4, 5, 6, and 6b.
- Snapshot is newly created and immutable by contract.
- `_LATEST.md` is the only mutable pointer written.
- Subject files were not edited.

## Known Limitations

- The audit was deliberately focused on the D-GOV-19 revision and its preservation boundary.
- It did not expand into unrelated pre-existing corpus-wide count, orphan, or legacy-reference remediation.
- The current DBM no longer carries an exhaustive §5.1 agent inventory; its hierarchy and live-role decisions were checked instead.
- Citation keys and bibliography metadata were checked locally; external DOI pages were not independently retrieved in this specialist run.
- Markdown references were statically and selectively reviewed, not rendered through a publication engine.

## Assumptions

- Commit `deab7a961c1a5c9fde771039497e50343b681d46` is the frozen subject tree.
- Existing unstaged changes to public-export derivative files belong to another workflow and are outside this audit's subject and write scope.
- The approved D-GOV-19 candidate and its ruled record are valid accepted inputs to this evaluation.

## Rerun Requirements

- Rerun after any source change beyond audited HEAD `deab7a961c1a5c9fde771039497e50343b681d46`.
- Rerun if a protected operational document, agent package, skill, tool, schema, enum, or lifecycle mechanic changes.
- No rerun is required from this PASS result alone.
