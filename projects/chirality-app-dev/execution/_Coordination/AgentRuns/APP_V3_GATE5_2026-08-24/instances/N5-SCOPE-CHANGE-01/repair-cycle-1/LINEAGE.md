# N5 Repair Cycle 1 — Current-Pin Fan-In Lineage

**Repair class:** `CURRENT_PIN_REGENERATION_AFTER_RECORD_ONLY_AUDIT_CSV_NORMALIZATION`
**Semantic change:** none to the audit metrics, graph, warnings, pointer payload,
pointer transaction, notice, or authoritative truth

## Upstream controlling lineage

N4 repair cycle 1 normalized exactly six audit evidence CSVs from CRLF to LF
with parsed row/cell equality. Its controlling lineage is
`instances/N4-SCOPE-CHANGE-01/repair-cycle-1/LINEAGE.md`, SHA-256
`6d221501f2e13995d302c9b56e2e7578cb6e7546ef213a638280e53b4d871d07`.

The audit manifest changed from
`1b50536809996025f6476e08c475b242a2113932c9a8b2dbdbd9156d93ca7012`
to `7c30c9e2244beca0a9d8182e1908ce188cba48ea87b919b5da16f3a83423077d`.
All 16 post-repair manifest entries validate. The report, issue log, closure
summary, metrics, `WARNINGS` verdict, one nine-node SCC, five isolates, and one
bidirectional pair are unchanged.

## Current N5 pin lineage

| Current artifact | Pre-repair SHA-256 | Post-repair SHA-256 | Exact change |
| --- | --- | --- | --- |
| `Phase5/Handoff_State.md` | `55fc0063268293ae23bc897960a33ea665c01f4fb23f24d8b11a6855738e2e9f` | `2ba40bccd70ca3bb178e1c4eca9c0ba3096d2081ad85ce297290c3c65fa4f4d6` | replace the current audit-manifest pin and add N4 repair/review-supersession disposition |
| `instances/N5-SCOPE-CHANGE-01/RETURN.md` | `5546f832908d3031d3bff6c06985ab8431fadf98055459c3cb254927f14ea9aa` | `450cfe548f0ebf660b386aa43c2f6e263c51a76add74d95b2235dd4962824c2a` | replace the current manifest and Phase5-handoff pins and record the nine-path disposition |
| `instances/N5-SCOPE-CHANGE-01/STATUS.json` | `44f5461aaea274f20070fa4190921fd458ddb5667db45256432149f4d75aef27` | `ea18bc09158b9a13124ce48aed43672c71a358e2b5c039a9c1385c591f660e48` | update current return/handoff/manifest and N4-lineage identities and require fresh review |

## Nine-path stale-pin disposition

The three current-state files above were regenerated. These six files remain
byte-identical historical pre-repair evidence and are not current pins:

1. `instances/N4-SCOPE-CHANGE-01/N4_RESUME_RETURN.md`;
2. `instances/N4-SCOPE-CHANGE-01/children/AUDIT-DEP-CLOSURE-GATE5-01/RETURN.md`;
3. `instances/N4-SCOPE-CHANGE-01/children/AUDIT-DEP-CLOSURE-GATE5-01/STATUS.json`;
4. `instances/N5-REVIEW-01/REVIEW.md`;
5. `instances/N5-REVIEW-01/RETURN.md`;
6. `instances/N5-REVIEW-01/STATUS.json`.

Their occurrences of `1b505368...` truthfully record the manifest that existed
when those returns and REVIEW-01 were produced. They are superseded for
current-state use by the N4 repair lineage and the current pins above. REVIEW-01
is historical evidence only for the pre-normalization bytes; fresh REVIEW-02 is
required for the current candidate.

## Byte-identical N5 candidates

The N4 stale-pin inventory found no audit-manifest occurrence in these files,
so N5 preserved them byte-identical:

- `_LATEST.proposed.md`
  `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`;
- `LATEST_POINTER_CANDIDATE.md`
  `44c39e11b4de7621fe25d643d049443223ffbbcd8160855c3fb85d4a4186609a`;
- `NOTICE_TO_ROOT_READY_TO_ROUTE.md`
  `75c9d5dde1b0c405181baf9b3ee1e8431e7bd5ae920355f3861a8bc51ce8e834`.

The live `_LATEST.md` remains byte-identical at
`a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`;
the notice remains unrouted and no Root path was written.

## Sequencing

Candidate whitespace passed against basis `cc196023...` immediately before
the current-pin regeneration and after the N4 CSV/manifest repair. No Receipt,
stage, commit, push, PR, pointer write, or notice-routing act occurred.
