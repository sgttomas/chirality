---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-03
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-054]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-03

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-05-03`
(SHA Role Register) in service of project scope reference SOW-054 and package
objective reference OBJ-003.

DEL-05-03 is a `REGISTER` in `PKG-05` (Evidence, Provenance, and Audit). Its
work is to keep three SHA roles distinct and recorded distinctly, so that a
reader can tell which commit an owner approved, which commit carries the durable
ruling record, and which commit reflects applied state. Conflating the three is
the failure this deliverable exists to prevent.

Every definition below is grounded only in the deliverable register row for
DEL-05-03, its `_CONTEXT.md`, the scope-ledger statement for SOW-054, and the
adopted `docs/PRD_ROOT.md`. Nothing else is imported (K-INVENT-1). All
acceptance and verification definitions are **candidate**: they claim no
acceptance, no lifecycle transition, and no owner ruling.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in `_CONTEXT.md ## Anticipated Artifacts`
and in the register `AnticipatedArtifacts` field are two, and they are the two
outputs of this deliverable.

- **OUT-001** — SHA role register: the register that names each of the three SHA
  roles, states what each one identifies, and records where each is written.
- **OUT-002** — Record-header conformance check: the check that a governed record
  header carries the three roles in distinct fields rather than a single
  undifferentiated commit reference.

- **CLM-001** — The three roles. `docs/PRD_ROOT.md` §5.4 E-3 [TRANSCRIBED] names
  them: the **owner act binds approved content to its candidate SHA**; the
  **publication SHA identifies the durable ruling record**; the **EffectiveSHA
  identifies applied state**. The PRD records the source of E-3 as K-AUTH-2 and
  the D-GOV-21 record header. The scope-ledger statement for SOW-054 restates the
  same three roles.
- **CLM-002** — Decomposition identity. The register records DEL-05-03 as
  `Type: REGISTER`, `ContextEnvelope: S` ("Three fields across one record
  family"), `AnticipatedWriteLocus: execution-tree`, and
  `ResponsibleParty: Ryan Tufts`. `ResponsibleParty` is transcribed here from D-GOV-27 and the current deliverable register and is not assigned by this contract. The `S` envelope is why this deliverable is
  scoped to one record family and three fields, not to a general provenance model.
- **CLM-003** — Objective linkage. `docs/PRD_ROOT.md` §3 OBJ-3 requires that every
  accepted change carry a retrievable linkage from files alone between the
  evidence that informed it, the ruling that accepted it, and the state it
  changed. The three SHA roles are the commit-level form of exactly that
  three-part linkage; collapsing them collapses the linkage OBJ-003 measures.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The register shall record the three SHA roles as three distinct
  entries, each stating what that SHA identifies. Source: SOW-054 (SourceRef
  `PRD §5.4 E-3 [TRANSCRIBED]`).
- **REQ-002** — The register shall preserve the asymmetry among the roles: the
  candidate SHA is what an owner act binds approved content to, the publication
  SHA is what identifies the durable ruling record, and the effective SHA is what
  identifies applied state. No role may be described as a synonym of another.
  Source: SOW-054 (SourceRef `PRD §5.4 E-3 [TRANSCRIBED]`).
- **REQ-003** — The conformance check shall inspect a record header and report
  whether the three roles appear in distinct fields, treating a single
  undifferentiated commit reference as a finding. Source: SOW-054 (SourceRef
  `PRD §5.4 E-3 [TRANSCRIBED]`).

- **AC-001** — OUT-001 contains exactly three role entries, one per SOW-054 role,
  each with the role name, what it identifies, and the record surface where it is
  written; no fourth role is introduced and none is omitted.
- **AC-002** — Every SHA value recorded in OUT-001 resolves to an object in this
  repository, and the three recorded values are reported pairwise as equal or
  distinct rather than assumed distinct.
- **AC-003** — OUT-002 states the field-distinctness condition, names the record
  family it inspects, and reports a per-record finding — conforming, or the
  specific role that is missing or merged.

## Production and Verification Method — Praxeology

Production is document work under the deliverable folder. Outputs are drafted
from the four grounding sources, cross-checked against SOW-054 and
`docs/PRD_ROOT.md` §5.4 E-3 and §3 OBJ-3, and left in `OPEN` source state.

- **VER-001** — Production-contract conformance. From the repository root run
  `python3 tools/scope_of_work/validate_scope_of_work.py execution/PKG-05_Evidence_Provenance_and_Audit/1_Working/DEL-05-03_SHA_Role_Register`;
  the method passes when it exits 0 and prints a `PASS format=SOW_V1` line. This
  verifies that every output, criterion, and objective reference in this contract
  is declared, resolved, and bound in the matrix. It does not verify the
  substantive content of either output.
- **VER-002** — SHA resolution and distinctness probe. For each SHA value recorded
  in the register run `git cat-file -e <sha>^{commit}`; the method passes when
  every invocation exits 0, evidencing that the recorded value names a real commit
  in this repository rather than a transcription error. The three values are then
  compared pairwise as strings and the equal/distinct result is recorded. The
  probe uses git only. It evidences resolvability and string distinctness; it makes
  no judgment about whether the right commit was recorded for a role.

- **CLM-004** — Instruction-surface fence. The register and `_CONTEXT.md` record
  `AnticipatedWriteLocus: execution-tree`. Should any act under this deliverable
  need to touch the instruction surface (`AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, `.github/workflows/`), that act requires an
  independently authorized M2 tranche. **This Scope of Work grants no such
  authorization.** The methods in VER-001 and VER-002 are read-only invocations
  and are not writes to that surface.

Where no deterministic surface exists at this basis, the matrix records
`HUMAN_REVIEW: <named method>` rather than naming a command that does not exist.
No field-name-level record-header validator exists at this basis, and this
contract does not fix field names beyond the role names carried by SOW-054 and
`docs/PRD_ROOT.md` §5.4 E-3.

## Governing Values and Decisions — Axiology

- **AX-001** — No invention. Only the deliverable register row, `_CONTEXT.md`, the
  SOW-054 scope-ledger statement, and `docs/PRD_ROOT.md` ground content here
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records that the accepted
  decomposition states no per-deliverable acceptance criteria; the criteria above
  are therefore candidate definitions authored under this contract.
- **AX-002** — Distinctness is the point. The register's value is that three roles
  stay three. A register that records one commit under three labels satisfies the
  form and defeats the purpose.
- **AX-003** — Approval binds to content. An owner act binds approved content to a
  candidate SHA; a recorded SHA is therefore an assertion about specific content,
  not a decoration on a record.
- **AX-004** — A resolving SHA is not an approval. VER-002 evidences that a value
  names a real commit. It does not evidence that an owner approved that commit,
  and no passing probe is an owner ruling.
- **AX-005** — Lifecycle neutrality. This contract makes no lifecycle transition
  and asserts no approval. Lifecycle state is `INITIALIZED` at the current basis and is read from
  `_STATUS.md`, which this contract does not modify.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-054 OBJ-003 | REQ-001 REQ-002 CLM-001 | AC-001 AC-002 | VER-001 VER-002 | Register with three role entries and their record surfaces; validator output line; per-SHA `git cat-file` exit status and the pairwise distinctness result |
| OUT-002 | SOW-054 OBJ-003 | REQ-003 CLM-002 CLM-003 | AC-003 | HUMAN_REVIEW: role-by-role read-back of one record header against the three SOW-054 roles, recording per-record whether each role appears in its own field | Conformance check naming the record family, its per-record findings, and any role found missing or merged |
