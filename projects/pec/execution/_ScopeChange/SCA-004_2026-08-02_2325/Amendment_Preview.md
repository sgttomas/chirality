---
amendment_id: SCA-004
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-08-03
status: awaiting_gate_3_approval
accepted_gate_2_impact_sha256: df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661
---

# SCA-004 — Gate 3 exact amendment preview

## Approval unit and boundary

This document is the exact content postimage proposed for SCA-004. It is a
preview only. The accepted basis remains SOFTWARE_DECOMP revision 1.3 / SCA-003,
and no live file or pointer has changed.

The Gate 3 approval unit is limited to:

- `execution/_Decomposition/SOFTWARE_DECOMP.md`;
- `execution/_Decomposition/ScopeLedger.csv` rows `SOW-077` and `SOW-094`;
- `execution/_Decomposition/Deliverables.csv` row `DEL-01-06`.

`ContextBudgetQA.csv` and `Companion_Inventory.csv` remain byte-identical.
Snapshot pointers, `_CONTEXT.md`, `_REFERENCES.md`, dependencies, contracts,
SPEC, source, lifecycle, Task Management, decisions, receipts, and foreign-loop
surfaces are not part of this Gate 3 approval unit. Their future disposition is
fenced in §Derivative and propagation boundary below.

## Accepted byte preconditions

| Surface | Required preimage SHA-256 |
|---|---|
| `SOFTWARE_DECOMP.md` | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| `Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| `ContextBudgetQA.csv` — no change | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` |
| `Companion_Inventory.csv` — no change | `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` |

Any mismatch before Gate 5 invalidates this preview and requires a refreshed
Gate 3 presentation.

## A001 — SOW-077

### A001.1 — SSOW placement and exact row

Remove this row from §2.3 `TBD items`:

```diff
-| SOW-077 | TBD | Home and shape of the loop registry (which loops PEC serves; today five) | §16.3 | Assessed (not PRD-stated): P1 can proceed on a local config default |
```

Add this row to §2.1 `IN-scope items`, after `SOW-064` and before `SOW-084`:

```diff
+| SOW-077 | IN | Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict version-1 JSON/schema paths and core-owned typed LoopRegistry port | §16.3, D-PEC-78 | D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry |
```

### A001.2 — authoritative Scope Ledger row

```diff
-SOW-077,TBD,Home and shape of the loop registry (which loops PEC serves; today five),§16.3,,,,,TRUE,OI-003. Assessed (not PRD-stated): P1 can proceed on a local config default
+SOW-077,IN,Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict version-1 JSON/schema paths and core-owned typed LoopRegistry port,"§16.3, D-PEC-78",PKG-01,DEL-01-06,OBJ-004,D-PEC-78,FALSE,D-PEC-78 O-A: PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; no governed act depends on PEC or the registry
```

This is one in-place CSV row replacement. Physical CSV row order is preserved;
the markdown SSOW row moves between its semantic status tables.

### A001.3 — objective-side mapping view

Replace the §3 `OBJ-004` row:

```diff
-| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-024, SOW-045..051, SOW-094; instrument: SOW-085 | DEL-01-06, DEL-05-02, DEL-09-01..07, DEL-10-05 |
+| OBJ-004 | The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where | §3.4 | SOW-024, SOW-045..051, SOW-077, SOW-094; instrument: SOW-085 | DEL-01-06, DEL-05-02, DEL-09-01..07, DEL-10-05 |
```

The mapped-deliverable set is unchanged.

### A001.4 — package-side mapping view

Replace the §4 `PKG-01` row:

```diff
-| PKG-01 | Service Core & Store | The zero-dependency service foundation: record- and presence-tier entity schemas, the gitignored store with ingest-boundary content-minimal enforcement, locality/no-egress posture, self-observability logging, loop-registration config | SOW-001, 002, 052, 053, 056, 057, 094 (7) | Parsing, derivation, serving — other packages |
+| PKG-01 | Service Core & Store | The zero-dependency service foundation: record- and presence-tier entity schemas, the gitignored store with ingest-boundary content-minimal enforcement, locality/no-egress posture, self-observability logging, loop-registration config | SOW-001, 002, 052, 053, 056, 057, 077, 094 (8) | Parsing, derivation, serving — other packages |
```

## A002 — SOW-094

The statement, status, source, package, deliverable, objective, and open-issue
flag remain unchanged. Replace only its unresolved-long-term note in the §2.1
SSOW table:

```diff
-| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves (local config default) | §12 P2, PEC-DSH-002 | Long-term registry home/shape stays open as SOW-077 (OI-003); local default per its resolved note (DL-14) |
+| SOW-094 | IN | Maintain the loop-registration configuration naming the loops PEC serves (local config default) | §12 P2, PEC-DSH-002 | Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable |
```

Replace the authoritative Scope Ledger row:

```diff
-SOW-094,IN,Maintain the loop-registration configuration naming the loops PEC serves (local config default),"§12 P2, PEC-DSH-002",PKG-01,DEL-01-06,OBJ-004,,FALSE,Long-term registry home/shape stays open as SOW-077 (OI-003); local default per its resolved note (DL-14)
+SOW-094,IN,Maintain the loop-registration configuration naming the loops PEC serves (local config default),"§12 P2, PEC-DSH-002",PKG-01,DEL-01-06,OBJ-004,D-PEC-78,FALSE,Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable
```

## A003 — DEL-01-06

### A003.1 — compact deliverable view

Replace the §5 row:

```diff
-| DEL-01-06 | Loop registry (local config default) | BACKEND_FEATURE_SLICE | S | P1 | SOW-094 |
+| DEL-01-06 | Loop registry (local config default) | BACKEND_FEATURE_SLICE | S | P1 | SOW-077, SOW-094 |
```

### A003.2 — authoritative Deliverables register row

```diff
-DEL-01-06,PKG-01,Loop registry (local config default),"Local configuration naming the loops PEC serves: one loop at P1 (PEC's own build, OI-010), extended to all five registered loops at P2. Long-term home/shape stays open (OI-003).",BACKEND_FEATURE_SLICE,TBD,Config format + loader + tests,SOW-094,OBJ-004,S,,P1
+DEL-01-06,PKG-01,Loop registry (local config default),"PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict version-1 JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry.",BACKEND_FEATURE_SLICE,TBD,Config format + loader + tests,SOW-077;SOW-094,OBJ-004,S,,P1
```

Every field except `Description` and `CoversScopeItems` is byte-identical.
The stable ID, name, path, package, type, responsible party, artifacts,
objective, envelope, envelope note, and phase are preserved.

## A004 — OI-003 and telemetry

### A004.1 — preserved resolved issue row

Replace the §10 Open Issues row non-destructively:

```diff
-| OI-003 | SOW-077 | §16.3 loop-registry home/shape undecided | §16 ruling |
+| OI-003 | SOW-077 | **RESOLVED by D-PEC-78 O-A:** the existing PEC-owned JSON/schema paths and core-owned typed port are the long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its entrypoint and governed truth; no governed act depends on PEC or the registry | Closed |
```

### A004.2 — exact coverage and telemetry replacements

```diff
-| ScopeItemCount | 94 (71 IN / 14 OUT / 9 TBD) |
+| ScopeItemCount | 94 (72 IN / 14 OUT / 8 TBD) |
```

```diff
-| OpenIssuesByType | 11 open (9 §16 owner decisions: OI-001..009; 1 architecture ADR: OI-012; 1 tooling follow-on: OI-013) / 2 resolved (OI-010, OI-011 at Gate 2) |
+| OpenIssuesByType | 10 open (8 unresolved §16 owner decisions: OI-001, OI-002, OI-004..009; 1 architecture ADR: OI-012; 1 tooling follow-on: OI-013) / 3 resolved (OI-003 by D-PEC-78 O-A; OI-010 and OI-011 at Gate 2) |
```

The other telemetry rows remain unchanged: 11 packages, 64 deliverables, six
objectives, zero unassigned IN items, zero IN items without deliverable
mapping, zero unmapped objectives, 11 IN items without objective mapping, and
Context Envelopes `S 28 / M 34 / L 2 / XL 0`.

## A005 — amendment traceability

### A005.1 — front matter revision identity

These exact successor identity values apply only if Gate 5 later executes and
the owner accepts the post-change state:

```diff
-revision: "1.3"
-date: 2026-07-28
+revision: "1.4"
+date: 2026-08-03
```

Replace the `accepted` field only at that later accepted Gate 5 state:

```diff
-accepted: 2026-07-28 (original Gate 7 owner ruling under D-PEC-60; revision 1.3 successor accepted through SCA-003 under the owner's standing completion approval)
+accepted: 2026-08-03 (original Gate 7 owner ruling under D-PEC-60; revision 1.4 successor accepted through SCA-004 under the owner's Gate 5 post-change confirmation)
```

Replace the `session_authorization` field only at that later accepted state:

```diff
-session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61, by SCA-002 under D-PEC-64, then by SCA-003 under the owner's 2026-07-28 standing completion approval
+session_authorization: D-PEC-60; amended by SCA-001 under D-PEC-61, by SCA-002 under D-PEC-64, by SCA-003 under the owner's 2026-07-28 standing completion approval, then by SCA-004 under D-PEC-78 and the owner's 2026-08-03 Gate 5 post-change confirmation
```

If Gate 5 is confirmed on a later date, the two date tokens above are
measurement-bound slots and must use that actual date without changing any
approved semantic text. No acceptance metadata may be written before Gate 5.

### A005.2 — Decision Log addition

Add after `DL-18`:

```diff
+| DL-19 | 2026-08-03 | SCA-004, requested by owner Ryan Tufts through D-PEC-78 O-A, promotes SOW-077 from TBD to IN, maps it to PKG-01 → DEL-01-06 → OBJ-004, adds SOW-077 to DEL-01-06 coverage, and records OI-003 resolved; DEL-01-06's stable name/path and all source bytes remain unchanged | The existing PEC-owned strict-version-1 JSON/schema paths and core-owned typed port are the selected long-term registry home and shape. PEC owns only its configured service set; each listed loop retains authority over its own entrypoint and truth; later row changes remain owner-gated PEC configuration acts; graceful absence and the no-governed-dependency boundary remain intact |
```

If Gate 5 is confirmed on a later date, only the row's date token changes to
the actual acceptance date.

### A005.3 — Revision History addition and telemetry revision row

Add after revision `1.3`:

```diff
+| 1.4 | SCA-004 | D-PEC-78 O-A loop-registry disposition: SOW-077 TBD→IN and mapped to PKG-01 / DEL-01-06 / OBJ-004; SOW-094 implementation basis reconciled; DEL-01-06 coverage and description updated in place; OI-003 resolved; stable IDs, topology, source, dependency edges, envelope, phase, name, and path unchanged |
```

Replace the §7 revision telemetry row:

```diff
-| Revision | 1.3, 2026-07-28 (SCA-003) |
+| Revision | 1.4, 2026-08-03 (SCA-004) |
```

The actual Gate 5 date rule above applies to this telemetry row as well.

## Reciprocal-mapping proof

The postimage establishes the same relationship in all authoritative and
summary directions:

| Direction | Exact postimage |
|---|---|
| SOW → package | `SOW-077 → PKG-01` |
| SOW → deliverable | `SOW-077 → DEL-01-06` |
| SOW → objective | `SOW-077 → OBJ-004` |
| Package → SOW | `PKG-01` assigned list gains `SOW-077`; count `7 → 8` |
| Deliverable → SOW | `DEL-01-06 CoversScopeItems = SOW-077;SOW-094` |
| Objective → SOW | `OBJ-004` mapped-scope view gains `SOW-077` |

No new package, deliverable, objective, source artifact, or execution edge is
created.

## Derivative and propagation boundary

The following are impact findings, not Gate 3 amendments:

| Surface | Gate 3 posture | Earliest owning act |
|---|---|---|
| DEL-01-06 `_CONTEXT.md` | No write. Expected mirror delta is `CoversScopeItems: SOW-094 → SOW-077;SOW-094`, the exact accepted register description above, and successor-basis provenance | Gate 4 propagation-plan approval, then Gate 5 SCOPE_CHANGE execution |
| Remaining 63 `_CONTEXT.md` files | No write; semantic fields remain unchanged | Later PROJECT_SETUP provenance re-pin |
| All 64 `_REFERENCES.md` files | No write | Later PROJECT_SETUP/reference-owner re-pin |
| DEL-01-06 `Dependencies.csv` | No write; one non-gating `ANCHOR/TRACES_TO_REQUIREMENT` row for SOW-077 will be owed | Later dependency-extract / PROJECT_SETUP act |
| Four ScopeOfWork contracts | No write; remain current historical bytes until their owner repairs and re-accepts successors | Later WORKING_ITEMS/artifact gates |
| DEL-00-03 accepted SPEC | No write; accepted bytes remain historical | Later DEL-00-03 artifact-amendment gate |
| Source and tests | `NO_CHANGE` | None; D-PEC-78 confirms current implementation shape |
| Lifecycle, Task Management, decisions, receipts, foreign loops | `NO_CHANGE` | No SCA-004 act |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md`, post-change audit and SCA snapshot | No write and no previewed hash | Gate 4 plan and Gate 5 measurement/acceptance only |

No downstream package becomes current through approval of this preview.

## Gate 3 recommendation and owner question

**Recommendation:** approve the exact amendment content above. It is the
smallest postimage faithful to D-PEC-78 O-A, preserves all stable structure,
and makes the new SOW-to-deliverable mapping reciprocal. Gate 4 would prepare
only the propagation plan; it would still authorize no live edit.

**Do you approve these exact SCA-004 amendments to the PEC SOFTWARE
decomposition and authorize SCOPE_CHANGE to prepare the Gate 4 propagation
plan only?**
