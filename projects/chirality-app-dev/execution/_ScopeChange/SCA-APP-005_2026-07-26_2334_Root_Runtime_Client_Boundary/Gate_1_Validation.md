# Gate 1 Validation

**Verdict:** `WARNINGS_PENDING_OWNER_CONFIRMATION`

## Semantic section binding

Heading-text binding resolved all required SOFTWARE sections without using
section position:

| Semantic section | Resolved heading |
|---|---|
| Change Register | `Decision Log / Change Log` |
| Unit Ledger | `Scope Ledger` |
| Objectives | `Objectives` |
| Primary Partitions | `Packages` |
| Secondary Entities | `Deliverables` |
| Coverage Basis | `Coverage and Telemetry` |

## Entity validation

- `PKG-03` exists exactly once in the Packages table.
- `DEL-03-01` exists exactly once in the Deliverables table and has a
  matching folder under PKG-03.
- `SOW-037` occurs once in SSOW and once in the Scope Ledger.
- `OBJ-002`, `OI-007`, and `DEC-019` each exist exactly once in their
  respective authoritative table.
- The register contains six `MODIFY` and two `ADD` actions. Every `MODIFY`
  target exists; neither proposed addition (`DEC-021` or the SCA-APP-005
  change-log entry) exists in the accepted decomposition.
- No parent binding, package membership, ID, lifecycle state, or topology
  change is proposed.

## Governing contradiction

The accepted App decomposition currently states:

> Root `runtime/` ownership is an implementation-location change; app-dev
> deliverables retain semantic ownership and acceptance evidence through the
> SCA-APP-003 impact map.

D-GOV-20 rules the generic runtime as Root-owned, and adopted Root PRD O-11
states that App, PEC, or another client's implementation work does not
transfer ownership of generic runtime semantics away from Root. SCA-APP-005
therefore corrects the ownership claim while retaining App client duties.

## Exact-source discipline for later gates

Gate 3 must not invent seam partitions. Any exact boundary sentence that is
marked as transcribed must be copied from D-GOV-20 and pass byte-level
concordance. App-specific client duties not settled by ruled text must be
labeled as proposed and returned for owner approval.

## Baseline and limitations

A read-only AUDIT_DECOMP specialist found that the last admitted App audit is
scoped to PKG-02, PKG-05, and PKG-08 and therefore cannot serve as the
affected-scope baseline for PKG-03. No repository-provided safe write-free
AUDIT_DECOMP runner exists. The specialist instead ran deterministic
read-only parsing over the current basis and found 10/10 packages, 51/51
deliverables, 51/51 contexts, 51/51 ScopeOfWork files, 78 ledger rows, and no
duplicate decomposition IDs.

Two pre-existing reverse-coverage limitations remain warnings: PKG-00 control
folders are outside the declared topology, and a second
`PKG-03_Harness_Runtime_Core` contains ignored evidence for undeclared
DEL-03-06. Neither is a new stable-ID collision or an SCA-APP-005 topology
blocker. Gate 5 must produce a fresh immutable AUDIT_DECOMP snapshot.

Gate 2 must explicitly disposition the linked rows `DEL-01-02`,
`DEL-09-02`, `DEL-03-02` through `DEL-03-04`, and their seven directly
connected scope items. They are not silently included in Gate 1's direct
write set.

## Independent adversarial classification

A second read-only Agent 2 classified the candidate before presentation:

| Classification | IDs |
|---|---|
| `DIRECT_CONTRADICTION` | `SOW-037;DEL-03-01` |
| `NECESSARY_CONSEQUENTIAL_ALIGNMENT` | `SOW-009;SOW-010;SOW-011;SOW-012;SOW-015;SOW-038;DEL-03-02;DEL-03-04` |
| `GATE-2_OBSERVATION_ONLY` | `SOW-040;DEL-03-03` |

It also confirmed `PKG-03` and `OBJ-002` as direct MODIFY actions because
their current text explicitly claims product ownership. Its one required
register correction was applied: DEC-019 is now `NO_CHANGE`, OI-007 is its
own conditional MODIFY action, and the new decision and change-log entries
are separate ADD actions.

This baseline does not claim OD-6 contract correctness. The six APP-HOLD-1
targets, contract acceptance/basis repair, invariant-register disposition,
D-APP-48/49 evidence, consumer/version work, and population repin remain
separate.

## Gate state

- Gate 1 validation: complete
- Gate 1 human confirmation: pending
- Gate 2: not opened
- Decomposition writes: none
- `_ScopeChange/_LATEST.md` update: none
