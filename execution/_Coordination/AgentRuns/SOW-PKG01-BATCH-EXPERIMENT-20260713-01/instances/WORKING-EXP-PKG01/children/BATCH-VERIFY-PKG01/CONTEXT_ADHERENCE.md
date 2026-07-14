# BATCH-VERIFY-PKG01 Context and Task Adherence

Verdict: `PASS_WITH_ONE_CONTAINED_SUBSTRATE_RESTART`

The verifier processed exactly `DEL-01-02`, `DEL-01-03`, and `DEL-01-04` in
numeric order inside this one verifier session. It did not delegate, contact
the author, read the excluded author child folder, repair a candidate, touch a
project file, or perform Git/network/lifecycle/integration work.

## Observable completeness

| Member | Evidence files | Mappings | Source lines | Mechanical result | Restarts |
|---|---:|---:|---:|---|---:|
| DEL-01-02 | 103 | 26 | 204 | PASS_UNCHANGED | 1 |
| DEL-01-03 | 103 | 34 | 290 | PASS_UNCHANGED | 0 |
| DEL-01-04 | 103 | 28 | 233 | PASS_UNCHANGED | 0 |
| Total | 309 | 88 | 727 | 3/3 PASS_UNCHANGED | 1 |

Each member has the same required evidence classes: frozen row and pre/post
hashes; two disjoint converter workspaces; standalone and authorized-dual
validations; repeated claim maps, parity, checklists, and HTML; four
fail-closed negative cases; explicit determinism; immutable-literal/semantic
review; four verdicts; and terminal checks summary. Byte volume varies with
source size, not evidence truncation.

## Error and drift assessment

`DEL-01-02` had one verifier-local harness restart. A malformed shell quote in
the later HTML scan was encountered after Bash had already executed through
the preservation checkpoint, leaving five partial progress rows. The exact
cause, stderr, fresh-workspace restart, and containment are recorded in
`EVIDENCE_CORRECTION-001.md`. This is classified as a script/orchestration
error and efficiency cost—not task drift, context loss, candidate failure, or
evidence contamination.

`DEL-01-03` and `DEL-01-04` each completed their full member sequence on the
first attempt. The final member has all 103 member evidence files, complete
28/28 mappings and 233/233 lines, all deterministic pairs, all four negative
cases, semantic review, and terminal hash checks. No member-1 or member-2
path, hash, candidate, scope refs, or objective refs were reused for a later
member. This supplies no observed sign of late-batch degradation, forgotten
instructions, evidence abbreviation, or cross-member contamination.

All three members deliberately rechecked the sealed brief/frozen-input
requirements at their preflight checkpoint. There were no semantic retries,
candidate repairs, waivers, blockers, unknowns, or wrong-reference/hash
detections.

## Measurement limit

Native token counts and exact context-window occupancy were not supplied by
the runtime and are therefore unavailable. The experiment can assess context
adherence only through durable sequence, equal evidence-class coverage,
member-specific references/hashes, error/retry telemetry, and terminal
artifact completeness. Those proxies pass; they do not prove behavior for
larger packages or longer source corpora.

