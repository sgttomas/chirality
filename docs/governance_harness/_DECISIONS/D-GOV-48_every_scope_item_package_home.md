# D-GOV-48 — Every scope item has one Package home (supersedes D-GOV-47 item 1)

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record, for merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session, workflow-library review wave 3, after the
owner questioned the D-GOV-47 Package-home ruling; prepared on local branch
`wave3-package-home`

AcceptedBasis: main@8f9bd314c5f2499e6faf5bf4bdce917927e8185e (merge of PR #939)

Supersedes: D-GOV-47 Decision item 1 (Package home for IN items only) and
the part of its item 2 that added `XRG-012`. D-GOV-47's other ruling, the
combined review sitting (its Decision item 3), and its `XRG-011` check stand.
The D-GOV-47 record is not edited (supersede-never-edit).

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/TYPES.md` `882ac9d7…`;
`docs/DECOMPOSITION_STANDARD.md` `501cf29e…`;
`workflows/software-decomp/WORKFLOW.md` `31ba50c4…`;
`workflows/software-decomp/resources/contract.md` `2f6c5ae6…`;
`workflows/software-decomp/resources/method.md` `723e62d3…`;
`workflows/project-decomp/resources/contract.md` `4e27b73d…`;
`workflows/project-decomp/resources/method.md` `1dcd8902…`;
`tools/validation/validate_decomposition_registers.py` `27b9fa20…`;
`tools/validation/test_validate_decomposition_registers.py` `dbd3ac5b…`;
`tools/validation/test_workflow_catalog.py` `780d718a…`;
`docs/governance_harness/_DECISIONS/_REGISTER.md` `33afe541…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA for decompositions that begin after it;
in-flight decompositions adopt by their own ruling (see Adoption)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation, after D-GOV-47 had merged, quoting the agent's phrase "old
wording" for the every-item text:

> "Old wording" ?  Why does every scope item NOT get a package, such that you think the docs need to be updated?

The agent answered that the IN-only ruling was its own framing error and
proposed a reversal: restore the every-item rule; IN items also map to
Deliverables; OUT and TBD items keep a Package home for traceability with no
production mapping; the register validator warns, rather than errors, on an
OUT or TBD item without a Package. The owner replied:

> yes go ahead, but PEC is being redeveloped right now so I'm deferring taking action on any findings until the dust settles.

## The error found

D-GOV-47 item 1 made the Package home required for IN scope items only. The
agent presented that choice to the owner as a conflict between two Root
surfaces: `docs/TYPES.md` and the decomposition contracts (every item has a
Package) against the decomposition standard and the methods (IN items only).
It recommended IN-only and did not show the owner the management manual, which
already states the rule deliberately:

- Management manual v7
  (`docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v7.md`,
  "Allocate each Scope Item once"): "Every SSOW Scope Item has exactly one
  Package home. The Scope Ledger preserves this allocation for included,
  excluded, and unresolved items. This single home establishes responsibility
  for accounting for the whole obligation."
- The same manual, reading the coverage summary: "An excluded item retains a
  Package home for traceability while requiring no production mapping."
- Field Book v1
  (`docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Field_Book_v1.md`,
  line 104): "Give each scope item one accountable package home."

The standard's IN-only text was the outlier against the manual, not the
other way round. D-GOV-47 then listed the manual, the Field Book and the
thesis as "Known residue" needing revision. That was wrong: they already
state the owner's rule, and nothing in them needs updating for it.

The owner's direction on D-GOV-47 ("as recommended") accepted a recommendation
whose framing left out the governing source. This record restores the rule
the owner had already set.

## Decision

1. **Every scope item has exactly one Package home (PROJECT and SOFTWARE).**
   Every Scope Item, whether `IN`, `OUT` or `TBD`, belongs to exactly one
   Package. The home is an accountability and traceability allocation: it
   says where responsibility for accounting for the item sits. Only IN items
   map to Deliverables; an OUT or TBD item keeps its Package home and
   `SourceRef` and needs no production mapping. The Scope Ledger's
   `PackageID` holds exactly one Package for every item, and
   `UnassignedScopeItems` counts every item without a Package, whatever its
   status, and must be 0 for acceptance.
2. **Group timing.** Group 1 comes before Packages exist. Material recorded
   as `TBD` at group 1 (including material outside a software basis's
   accepted portions) receives its Package home at group 2, along with every
   other Scope Item.
3. **Surfaces restored.** `docs/TYPES.md` §1.1 and §8.1; the decomposition
   standard's status note, I4, glossary (Decomposition Ledger), Stage B,
   completeness and consistency tables, ledger column, hard rule,
   extension-contract text and telemetry note; both `project-decomp` and
   `software-decomp` contracts (invariant, glossary, Validity tables, Scope
   Ledger `PackageID` and `DeliverableID(s)` columns, hard rule, telemetry)
   and methods (group 2 assignment; `software-decomp` group 1 note); and the
   `software-decomp` edition note in `WORKFLOW.md`. The standard keeps DOMAIN
   distinct: `domain-decomp` requires a Category for IN Handbook Units only,
   and is unchanged.
4. **Register validator.**
   `tools/validation/validate_decomposition_registers.py` keeps `XRG-011`
   (ERROR: IN ledger item with no `PackageID`). `XRG-012` (D-GOV-47: WARNING
   when an OUT or TBD item carried a `PackageID`) is retired and not reused;
   an OUT or TBD item with a `PackageID` now conforms. New `XRG-013` is a
   WARNING for an OUT or TBD item with no `PackageID`. It is a warning, not
   an error, because decompositions adopted under D-GOV-47 or earlier left
   those items blank. Both checks apply only when the ledger has a
   `PackageID` column. `XRG-007` (ERROR: non-IN item carrying
   `DeliverableIDs`) is unchanged and carries the "no production mapping"
   half of the rule.

## Adoption

In-flight decompositions keep the rule and edition they adopted; nothing is
retrofitted. A project loop adopts this change by its own ruling.

PEC: run against `projects/pec/execution` with `--families XRG`, the
validator reports 26 `XRG-013` warnings (18 OUT and 8 TBD items with a blank
`PackageID`), no errors, and exit 0 (exit 1 only under `--strict`). PEC is
being redeveloped, and the owner is deferring action on any findings until
that settles. The warnings are informational until then. This record does not
edit PEC's registers.

The App, Runtime and Piping loops have no `ScopeLedger.csv`, so the XRG
family skips them.

## Unchanged

- D-GOV-47 Decision item 3, the combined review sitting for a small, reversible
  PROJECT or SOFTWARE undertaking, in the standard, both methods, both
  contracts and both `WORKFLOW.md` entrypoints.
- `domain-decomp` and its Category rule; DOMAIN telemetry
  (`UnassignedINUnits`).
- The management manual, the Field Book and the thesis. They already state
  this rule.
- Dependency schema and `docs/SPEC.md` §5, `workflows/review`,
  `scope-change`, `audit-decomp` and `project-setup`.
- The standard's prospective status and its ratified D-GOV-14 edition.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-PACKAGE-HOME-D-GOV-48-20260926.yaml`.
- `tools/validation/test_validate_decomposition_registers.py` covers the
  conforming case (OUT and TBD items with a Package home), `XRG-011` on an
  IN item, `XRG-013` on OUT and TBD items, and the retirement of `XRG-012`.
  `tools/validation/test_workflow_catalog.py` checks the every-item text in
  TYPES, the standard and both decomposition packages, that the combined
  review text stands, and that DOMAIN keeps its IN-only Category rule.
- The register fills D-GOV-47's publication SHA
  (`6c2bddddb626f862a880e87ee1ed9d21f862acb0`, merge of PR #938) and notes
  that its Package-home ruling is superseded here.
- Notices are routed to the App, Runtime, Piping and PEC loops. The App
  authority corpus pins `software-decomp` hashes, so it will report drift
  against these bytes. Each loop decides its own adoption. No release is made.
