# SCOPE_CHANGE return — SCA-004 Gate 3 preview

Status: `COMPLETE — AWAITING OWNER GATE 3 APPROVAL`  
Manager: `SCOPE_CHANGE`  
RunID: `PEC-DPEC77-78-20260802`  
InstanceID: `scope-change-sca004-gate3`  
AmendmentID: `SCA-004`

## Result

The exact SCA-004 Gate 3 content postimage is prepared and validated against
the accepted revision 1.3 bytes. It is a preview only. Gate 4 is not open, no
propagation plan has been prepared, and no live decomposition, pointer,
metadata, downstream, source, lifecycle, register, or foreign-loop byte was
changed.

Gate 3 preview:
`projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Amendment_Preview.md`

## Preview evidence hashes

| File | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f` |
| `Gate3_Preview_Validation.md` | `62487b68e72d6fcaea03fd0dfa490d9c5fa2c488407f2dedb14370523be47a13` |
| `Gate3_Handoff.md` | `5cc5689b41fae6ab130a6930a17d15dd2f95a6c9116bc8518a70158eb6699faa` |
| `Decision_Log.md` | `2974a2ec92baca61e96559931f2ca69af204fe64842b6df7112a5c12dc5f4ed8` |

Accepted Gate 2 impact assessment SHA-256:
`df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661`.

## Exact action postures

### A001 — SOW-077

- `InOutStatus`: `TBD` → `IN`.
- `ScopeItemStatement`:
  `Home and shape of the loop registry (which loops PEC serves; today five)`
  → `Maintain the PEC-owned long-term service registry naming the loop
  locators PEC serves through the strict version-1 JSON/schema paths and
  core-owned typed LoopRegistry port`.
- `SourceRef`: `§16.3` → `§16.3, D-PEC-78`.
- `PackageID / DeliverableIDs / ObjectiveIDs`:
  blank → `PKG-01 / DEL-01-06 / OBJ-004`.
- `DecisionRef`: blank → `D-PEC-78`.
- `OpenIssue`: `TRUE` → `FALSE`.
- `Notes` becomes:
  `D-PEC-78 O-A: PEC owns only its configured service set; each listed loop
  remains authoritative for its own entrypoint and truth; later row changes
  are owner-gated PEC configuration changes; no governed act depends on PEC
  or the registry`.
- The markdown row moves from §2.3 TBD to §2.1 IN. PKG-01 and OBJ-004 summary
  views gain SOW-077.

### A002 — SOW-094

Status, statement, source, package, deliverable, objective, and open-issue flag
remain unchanged. `DecisionRef` becomes `D-PEC-78`; `Notes` becomes:

`Local JSON configuration is the implementation basis for the long-term
PEC-owned service registry confirmed by D-PEC-78; the core port keeps
filesystem and JSON details replaceable`.

### A003 — DEL-01-06

- `CoversScopeItems`: `SOW-094` → `SOW-077;SOW-094`.
- `Description` becomes:
  `PEC-owned local configuration naming the loop locators PEC serves: one loop
  at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration
  changes. The strict version-1 JSON/schema paths and core-owned typed port are
  the long-term home and shape under D-PEC-78; each listed loop remains
  authoritative for its own entrypoint and truth, and no governed act depends
  on PEC or the registry.`
- ID, name, path, package, type, responsible party, artifacts, objective,
  envelope, envelope note, and phase remain unchanged.

### A004 — OI-003

The row is preserved and becomes:

`RESOLVED by D-PEC-78 O-A: the existing PEC-owned JSON/schema paths and
core-owned typed port are the long-term registry home and shape. PEC owns only
its configured service set; each listed loop retains authority over its
entrypoint and governed truth; no governed act depends on PEC or the registry.`

Its owner action becomes `Closed`. Telemetry changes from
`71 IN / 14 OUT / 9 TBD` to `72 IN / 14 OUT / 8 TBD`, and from
`11 open / 2 resolved` to `10 open / 3 resolved`.

### A005 — amendment traceability

- Successor revision: `1.3` → `1.4`.
- Successor revision date: `2026-08-03`, or the actual later Gate 5 acceptance
  date if Gate 5 is not confirmed on 2026-08-03.
- Add exact `DL-19` recording the Ryan Tufts / D-PEC-78 O-A amendment,
  preserved DEL-01-06 identity, and unchanged source bytes.
- Add exact revision-history row `1.4 / SCA-004`.
- Update the §7 revision telemetry row to revision 1.4.
- Acceptance/session-authority metadata changes only at the later accepted
  Gate 5 state. Pointer text and measured hashes remain Gate 4/Gate 5 work.

The full exact markdown and CSV rows are in `Amendment_Preview.md`; this return
does not abbreviate the approval unit.

## Reciprocal mapping and telemetry proof

An in-memory simulation over the accepted CSV schemas passed:

| Check | Result |
|---|---|
| Status counts | `72 IN / 14 OUT / 8 TBD` |
| SOW-077 lineage | `PKG-01 / DEL-01-06 / OBJ-004` |
| DEL-01-06 reverse coverage | `SOW-077;SOW-094` |
| Reciprocal SOW/deliverable mapping | `PASS` |
| PKG-01 scope count | `8` |
| OBJ-004 scope count | `11` |
| IN without package / deliverable | `0 / 0` |
| IN without objective | `11`, unchanged |
| Packages / deliverables / objectives | `11 / 64 / 6`, unchanged |
| Context Envelopes | `S 28 / M 34 / L 2 / XL 0`, unchanged |
| Execution edges / SCCs | `119 / 0`, unchanged |

Semantic bindings passed for Change Register, Unit Ledger, Packages,
Deliverables, Objectives, Coverage/Telemetry, and Open Issues. Stable-ID,
package-discipline, artifact-kind granularity, and no-supersession checks pass.

## Derivative boundary

Gate 3 approval would not approve any derivative write. The expected
DEL-01-06 `_CONTEXT.md` mirror delta, the other 63 context provenance re-pins,
all 64 reference re-pins, one SOW-077 non-gating requirement anchor, four
ScopeOfWork currency repairs, the accepted SPEC repair, snapshot/pointer
materialization, and post-change audit remain separately owned and gated.
Source, lifecycle, Task Management, decisions, receipts, and foreign-loop
surfaces remain `NO_CHANGE`.

## Synchronization and boundary checks

- Worktree HEAD and observed `origin/main` both resolve to
  `7249281e1f84ba5abee3c31c2fea3736b22000d3`; the branch contains
  `origin/main`.
- All five governed decomposition preimage hashes remain byte-identical to
  the accepted Gate 2 basis.
- `git diff --check` passes.
- The only SCA-004 writes in this run are the interim package evidence and
  this instance return/status.

## Exact owner Gate 3 question

**Do you approve these exact SCA-004 amendments to the PEC SOFTWARE
decomposition and authorize SCOPE_CHANGE to prepare the Gate 4 propagation
plan only?**
