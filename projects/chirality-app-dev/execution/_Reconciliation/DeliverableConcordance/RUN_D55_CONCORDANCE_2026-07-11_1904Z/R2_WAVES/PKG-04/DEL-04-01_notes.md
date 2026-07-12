# DEL-04-01 R2 concordance notes — RUN_D55_CONCORDANCE_2026-07-11_1904Z

Wave: W2 (PKG-04). Source state: frontend/ at `fac46e33f` (byte-identical through
HEAD `1625b396a`, orchestrator-verified); docs/kit inspected at `1625b396a`.
Claim set re-derived from `Specification.md`: 15 requirement rows, matching the
R1 REQUIREMENT_INDEX 15-ID checklist exactly (no parser gap for this deliverable).

## Census

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 15 |
| EXCLUSION | 3 |
| ACCEPTANCE | 3 |
| IMPLEMENTED_UNMAPPED | 1 |
| REMAINING_WORK | 3 |
| REGISTER_DEFECT | 1 |
| **Total** | **26** |

| Disposition | Rows |
|---|---:|
| ALIGNED | 14 |
| PARTIALLY_IMPLEMENTED | 7 |
| STALE_SPECIFICATION | 2 |
| DOCUMENTED_UNIMPLEMENTED | 1 |
| ACCEPTED_DIVERGENCE | 1 |
| REMAINING_STATE_MISMATCH | 1 |

MR-4 note: Datasheet Conditions restatements (settings isolation, transcript
canonicality, tool restriction boundary, permission overlay, probe exposure)
are folded into REQ-005/009/006/014 rows. The three ACCEPTANCE rows are
datasheet/kit-distinct conditions: the REF-006 source-state condition
(ACC-001), the adoption-decision authority condition (ACC-002), and the
setup-era TBD wording cluster (ACC-003).

## Least-confident rows (mandatory self-flagging)

1. **DEL-04-01-REQ-001 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading:
   ALIGNED. The requirement says subprocess version "when knowable"; recording
   `BLOCKED_TBD` with the gated live-demonstration path arguably satisfies the
   clause, since the version is not knowable without the owner-gated act. I
   kept PARTIALLY_IMPLEMENTED because the deliverable's own evidence record and
   Remaining item treat it as an open residual, not a satisfied condition.
2. **DEL-04-01-REQ-010 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading:
   ACCEPTED_DIVERGENCE — the taxonomy portion is ruled (D-APP-40) and landed,
   and the only open part is the D-APP-52-gated live-behavior residual, which a
   ruling acknowledges. That reading would flip the row. I kept
   PARTIALLY_IMPLEMENTED because the requirement's "require ... events to
   persist before production default use" clause is only deterministically
   evidenced while the key-aware default is already live.
3. **DEL-04-01-REQ-011 (ALIGNED, MEDIUM).** Alternative reading:
   PARTIALLY_IMPLEMENTED — ADQ-15 proofs are scripted no-live; a live packaged
   provider turn has never been observed. I read the requirement as "test
   packaging and record residual risks", both of which are done and recorded;
   if the fan-in reads "test Electron packaging of the SDK subprocess" as
   requiring a live packaged turn, the row flips.
4. **DEL-04-01-EXC-001 (ALIGNED, MEDIUM).** Alternative reading: the exclusion
   is only documentarily respected — INSP-03 itself cites the downstream
   implementation files as this deliverable's conformance evidence, and the
   four handover rows are unconsumed, so ownership of those surfaces by
   DEL-04-02..05 is asserted by the decomposition but not evidenced end-to-end.
5. **DEL-04-01-ACC-002 (DOCUMENTED_UNIMPLEMENTED, MEDIUM).** Alternative
   reading: ALIGNED-as-declared — the kit's own threshold rule says the
   approver field "remains TBD" until assigned, so TBD is the documented
   expected state, not a defect. I kept DOCUMENTED_UNIMPLEMENTED because the
   acceptance condition (a named approver before any adoption verdict is
   accepted) is objectively unmet and human-owned; `NEW-PACKET` recorded.
6. **UNMAPPED-1 (ACCEPTED_DIVERGENCE, MEDIUM).** Alternative reading:
   IMPLEMENTED_UNDOCUMENTED — the key-aware default is arguably DEL-04-05 /
   PKG-03 surface, and the divergence framed here (ruled default cutover ahead
   of this deliverable's adoption record) could instead be scored as a missing
   deliverable-local mapping. D-APP-18 is an explicit human ruling permitting
   the bounded cutover, which is why ACCEPTED_DIVERGENCE was chosen (MR-8).

The fan-in verifier should also recheck all non-ALIGNED rows per the brief;
the two STALE_SPECIFICATION rows (ACC-001, ACC-003) are high-confidence —
every asserted-stale wording location was re-read this run and the REF-006
hash was recomputed live (`shasum -a 256 docs/PRD.md` reproduces
`ac35fba4...c30bfd`, matching `_REFERENCES.md` REF-006 MATCH).

## Register-defect summary

One defect (REGISTER-1): `_DEPENDENCIES.md` "Declared Upstream" / "Declared
Downstream" narrative sections still assert "TBD - no accepted dependency
edges have been extracted yet" while the same file records the 13-row
extracted register and the 2026-05-20 extraction run. The D-APP-53 (DRQ-04)
sync corrected the summary/metric tables but left these two sections stale.
`Dependencies.csv` itself is internally consistent with `_DEPENDENCIES.md`'s
tables (ACTIVE 12 / RETIRED 1; SATISFIED 7 / TBD 5 / NOT_APPLICABLE 1) and the
D53A evidence record; validation PASS (13 rows, 0 errors) is recorded in that
evidence file. No defect found in `_REFERENCES.md` (all seven rows MATCH;
REF-006 re-verified by live hash recomputation).

## Remaining-item handling

Three `## Remaining` items, three REMAINING_WORK rows (per dispatch note):

- REMAINING-1 (handover consumption, UNGATED) — SelectableUnderCurrentLoop YES.
- REMAINING-2 (CODEV-001 live-environment residuals) — gate suffix carried
  verbatim: `(gated: D-APP-52 owner act — live-LLM demonstration)`. Gate
  unsatisfied at the source state (no live-LLM demonstration evidence in this
  project's surfaces), so NO per MR-6. Own-project gate; no cross-project
  UNKNOWN needed.
- REMAINING-3 (concordance bootstrap, UNGATED) — YES; this run is its
  in-progress execution.

REQ-001/003/008/010 carry Remaining item 2's verbatim text in
RecordedRemaining because that recorded residual covers those claims' open
portions.

## Method deviations

None. Line anchors for the largest test suites (sdk-options-builder permission
block 255-562; harness-anthropic redaction 572-935; claude-agent-sdk-manager
interrupt 262-332) are attributed to INSP-03's citations with the suites'
presence and line counts re-verified at fac46e33f; anchors I re-derived
directly this run are stated without attribution. No tests executed; no
dependencies installed; no files outside the two wave artifacts written.
