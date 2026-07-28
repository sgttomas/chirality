---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-07
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-044, SOW-074]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-04-07

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-04-07`, Public
Export Boundary Conformance, a `SECURITY_CONTROL` deliverable of
`PKG-04_Developmental_Machinery_and_Change_Control`. It serves project scope
items SOW-044 and SOW-074 and package objective OBJ-001.

SOW-044 states that the public-export boundary is an explicit allowlist profile
that copies allowlisted content, sanitizes private absolute paths, writes a
manifest and report, and fails on forbidden paths or leaks, and that the
profile is the boundary contract and is incorporated by reference. Its
SourceRef is PRD §5.3 D-10, labelled TRANSCRIBED.

SOW-074 is an `OUT`-status boundary item: no change to the public-export
boundary. Its SourceRef is PRD §8.1, a transcribed non-goal, with DecisionRef
DEC-007. It is contracted here as a constraint on this deliverable, not as work
to be produced.

OBJ-001 is coherent and discoverable normative authority — a reader can
determine what governs, from the repository alone. The boundary contract is
discoverable only if the profile itself governs and no narrative restatement
competes with it, which is what the incorporation-by-reference clause protects.

The register records ContextEnvelope `S` with the note that this is one profile
with existing failure modes. This Scope of Work contracts conformance evidence
against those existing modes; it does not add modes.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in the register and `_CONTEXT.md` are an
export run manifest/report, a boundary conformance note, and leak-check
evidence. They are expressed here as three outputs.

- **OUT-001** — An export run manifest and report produced by the profile
  itself for the declared run, recording the copied allowlisted content, the
  sanitization count, and any boundary findings.
- **OUT-002** — A boundary conformance note that states, against the profile as
  it stands, that the run exhibited each behaviour SOW-044 requires and that the
  boundary was unchanged by the deliverable.
- **OUT-003** — Leak-check evidence recording that the staged tree contained no
  forbidden path and no private absolute path surviving sanitization.

- **CLM-001** — The profile `exports/chirality-app/export_public.py` is the
  boundary contract. PRD §5.3 D-10 incorporates it by reference and states that
  membership is not restated; PRD §5 registry discipline cites the profile as a
  live registry and provides that where live registry and narrative disagree,
  the live registry governs and the discrepancy is surfaced.
- **CLM-002** — PRD §10.2 preserves the discovery record for C-4. PR #345
  (merge `ba2b80bf2`, Receipt 44) added `runtime/` to the `README.md`
  public-export description and closed C-4 while preserving the live profile
  as the boundary contract. This deliverable performs a standing re-check and
  does not carry C-4 as open.
- **CLM-003** — Restating allowlist membership inside this deliverable would
  create exactly the drifting parallel registry that the incorporation-by-
  reference clause exists to prevent. The outputs therefore cite the profile
  and its generated artifacts rather than enumerating members.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The outputs shall evidence, for the declared export run, each
  behaviour SOW-044 states: allowlisted content copied, private absolute paths
  sanitized, a manifest and a report written, and failure on forbidden paths or
  leaks (PRD §5.3 D-10 [TRANSCRIBED]).
- **REQ-002** — The outputs shall not restate or redefine allowlist membership,
  and shall cite the profile as the boundary contract wherever membership is at
  issue.
- **REQ-003** — The deliverable shall leave the boundary unchanged. Producing
  conformance evidence is within scope; altering the profile is excluded by
  SOW-074 (PRD §8.1 [TRANSCRIBED non-goal]; DEC-007).

- **AC-001** — For the declared run, the manifest and report exist, the report
  records the manifest row count and sanitization count, and the run's exit
  status is consistent with the findings the report records: a clean report
  accompanies a success exit and a findings report accompanies a failure exit.
- **AC-002** — The leak-check evidence shows an empty forbidden-path finding
  set for the staged tree, or, where findings exist, lists each one rather than
  summarizing it away.
- **AC-003** — The conformance note cites the profile path as the boundary
  contract, enumerates no allowlist members of its own, and records that no
  change to the profile was made under this deliverable.

## Production and Verification Method — Praxeology

Production runs the existing profile and reads its generated artifacts. It does
not reimplement the boundary scan, because a second implementation would become
a competing boundary statement.

- **VER-001** — Execute the profile with
  `python3 exports/chirality-app/export_public.py --stage-dir <path>` and record
  its exit status together with the generated
  `exports/chirality-app/export-manifest.csv` and
  `exports/chirality-app/export-report.md`. A nonzero boundary-scan exit is
  itself a conformant observation of the fail-on-findings behaviour and is
  recorded, not suppressed.
- **VER-002** — Confirm the profile is unmodified by this deliverable by
  inspecting `git status --porcelain exports/` and the diff of
  `exports/chirality-app/export_public.py` against the run's base commit,
  expecting no change to the profile.

Whether the conformance note faithfully reads the profile as the boundary
contract, and whether it preserves C-4's recorded closure while surfacing any
new disagreement, are semantic judgments routed to human review in the matrix
below.

## Governing Values and Decisions — Axiology

- **AX-001** — The live registry governs over narrative. PRD §5 states that
  where live registry and narrative disagree, the live registry governs and the
  discrepancy is surfaced. This deliverable surfaces; it does not reconcile by
  editing either side.
- **AX-002** — Conflicts are surfaced with pointers and never silently
  resolved, per the epistemic discipline PRD §5.1 N-4 transcribes. C-4 is closed
  by PR #345 and Receipt 44; a new disagreement would be surfaced as new
  evidence rather than silently resolved or treated as a reopening.
- **AX-003** — The register records `AnticipatedWriteLocus: execution-tree;
  exports/ (M2) if the profile must change`. That is a planning note, not
  authorization. This Scope of Work grants no act on the instruction surface —
  `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`,
  `.github/workflows/` — and no change to the export profile; any such act
  requires an independently authorized M2 tranche, which this document does not
  supply.
- **AX-004** — Every `AC-*` and `VER-*` defined here is a candidate. This
  document claims no acceptance, no approval, and no lifecycle state. The accepted decomposition states no per-deliverable acceptance criteria; nothing is inferred to fill that gap. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register
  (K-INVENT-1).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-044 OBJ-001 | REQ-001 CLM-001 | AC-001 | VER-001 | Generated manifest and report for the declared run, with the recorded exit status and counts |
| OUT-002 | SOW-074 OBJ-001 | REQ-002 REQ-003 CLM-003 | AC-003 | VER-002 | Conformance note citing the profile path, plus a clean profile diff against the base commit |
| OUT-003 | SOW-044 OBJ-001 | REQ-001 CLM-002 | AC-002 | HUMAN_REVIEW: owner reading of the leak-check findings and the closed C-4 trace against `exports/chirality-app/export_public.py` as the governing profile | Enumerated forbidden-path and sanitization findings for the staged tree, with C-4's closure preserved and any new disagreement surfaced |
