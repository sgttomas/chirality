# D-GOV-47 — Decomposition rulings: Package home for IN items only; combined review for a small, reversible undertaking

Status: OWNER-DIRECTED 2026-09-26 — application carried in the same pull
request as this record, for merge under the standing Git authorization of
2026-09-12

Date: 2026-09-26 (America/Edmonton)

FramedBy: Claude Code session on `claude/brave-goodall-wj3hok` (workflow-library
review, wave 2b items 3 and 4), after tranche
`ROOT-WORKFLOW-WAVE2A-FORMATION-20260926`, whose scope limits left both rulings
open

AcceptedBasis: main@971ca68a15a562f6df33cf4c78d27948ad07f822 (merge of PR #935)

PriorRevisions (git blob SHAs at AcceptedBasis, preserved by history):
`docs/TYPES.md` `d341b1e2…`;
`docs/DECOMPOSITION_STANDARD.md` `00b6062e…`;
`workflows/software-decomp/WORKFLOW.md` `f27baa22…`;
`workflows/software-decomp/resources/contract.md` `67e04e8d…`;
`workflows/software-decomp/resources/method.md` `d35a93d4…`;
`workflows/project-decomp/WORKFLOW.md` `78e9dfd5…`;
`workflows/project-decomp/resources/contract.md` `b5461c63…`;
`workflows/project-decomp/resources/method.md` `fdc843de…`;
`tools/validation/validate_decomposition_registers.py` `96c059e2…`

PublicationSHA: the merge commit of the pull request that introduces this
file; recorded in `_REGISTER.md` by the next Root change that touches the
register (K-AUTH-2)

EffectiveSHA: same as PublicationSHA for decompositions that begin after it;
in-flight decompositions adopt by their own ruling (see item 4)

## Owner direction (verbatim)

Owner Ryan Tufts (repository owner sgttomas), 2026-09-26, in the Claude Code
conversation, on the wave 2b items presented to him:

> yes, go ahead with wave 2b #1 and 2, and on #3 and 4 as recommended.

The two recommendations that direction accepted, as presented to the owner:

> #3 Package home: "does every scope item need a Package, or only in-scope
> items? software-decomp's contract and TYPES.md say every item. Its method
> and the decomposition standard say only in-scope items. My recommendation is
> only in-scope items. Out-of-scope and TBD items stay in the ledger with their
> source reference, but don't get a Package. This matches the standard, and the
> new 'material outside the accepted basis' rule needs it."

> #4 Combined review for small undertakings: "the management manual allows
> presenting basis, structure and final package together for a small,
> reversible undertaking. The decomposition workflows require three separate
> checkpoints. My recommendation is to allow one sitting in which all three are
> presented, with the independent audit still done first and the three
> snapshots still written in order."

This record carries items 3 and 4. Items 1 and 2 of the same direction are
outside this record.

## Decision

1. **Package home is required for IN items only (PROJECT and SOFTWARE).**
   Every IN scope item belongs to exactly one Package and maps to its
   Deliverables. OUT and TBD items remain in the Scope Ledger with their
   `SourceRef` and have no Package; their `PackageID` is blank (the
   convention the standard already used for OUT and that the PEC registers
   follow). `UnassignedScopeItems` counts IN items without a Package. This
   aligns `docs/TYPES.md` §1.1 and §8.1, both decomposition contracts
   (invariant, Validity tables, Scope Ledger column and hard rule, telemetry)
   and both methods with the standard's I4, and lets group 1 record material
   outside the accepted basis as `TBD` without inventing a Package for it.
   The standard's ledger column now reads "blank for OUT and TBD" and its
   glossary and extension-contract text say the same. DOMAIN is unchanged:
   `domain-decomp` already requires a Category for IN Handbook Units only.
2. **Register validator.** `tools/validation/validate_decomposition_registers.py`
   adds `XRG-011` (ERROR: IN ledger item with no `PackageID`) and `XRG-012`
   (WARNING: OUT or TBD ledger item carrying a `PackageID`). Both apply only
   when the ledger has a `PackageID` column. `XRG-012` is a warning because a
   decomposition adopted before this ruling may have given an excluded item a
   traceability home. Tests cover both, the conforming blank case, and a
   ledger without the column. The PEC registers report no findings.
3. **Combined review sitting (PROJECT and SOFTWARE only).** For a small,
   reversible undertaking, the human may choose to decide all three
   checkpoint groups in one sitting: the basis, normalized scope, vocabulary
   and objectives; the proposed Packages and Deliverables with coverage
   findings and exceptions; and the audited final decomposition. Conditions:
   - groups 2 and 3 are each prepared on the preceding group's proposed
     state, and the independent audit of the final package is completed
     before the decision;
   - the decision records which groups it covers, and the audit and decision
     record the hashes of the presented package;
   - the group-1, group-2 and group-3 snapshots and pointers are still
     written in that order after the decision, and must match the recorded
     hashes (a difference reopens the affected groups and every later group);
   - a material change found during the sitting reopens the groups it
     affects and every later group; only earlier, unaffected groups may
     still be decided in the sitting.

   The standard's I1 and PROTOCOL, both methods, both contracts and both
   `WORKFLOW.md` entrypoints carry this. DOMAIN does not use the allowance.
   This matches the management manual (v7, chapter 3: "For a small,
   reversible undertaking, the basis, structure, and final package may be
   presented together."). The agent manual (v3, §6) does not require separate
   sittings and is unchanged.
4. **Adoption.** In-flight decompositions keep the rule and edition they
   adopted; nothing is retrofitted. A project loop adopts this change by its
   own ruling. `software-decomp`'s edition note names this amendment. The
   standard's prospective status and its ratified D-GOV-14 edition are
   unchanged.
5. **Not changed.** Dependency schema and `docs/SPEC.md` §5,
   `workflows/review`, `write_status.sh`, the `semantic-lens` and
   `engineering-extraction` workflows, `domain-decomp`, `scope-change` and
   `audit-decomp` are not changed. The management manual, the field book and the
   thesis are not edited by this record (see Known residue).

## Known residue

- The management manual v7 (`docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v7.md`,
  chapter 3) still says every SSOW Scope Item has exactly one Package home,
  including excluded and unresolved items, and that every Scope Item must
  have a Package allocation before acceptance. It now differs from item 1
  and needs its own authorized revision.
- `docs/thesis/04_architecture.md` §4.3 and `docs/thesis/glossary.md`
  (Package, Scope ledger) restate the earlier every-item wording.
- The field book (`docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Field_Book_v1.md`)
  says to give each scope item one accountable package home.

## Application and assurance

- Application paths are listed in the tranche manifest
  `docs/governance_harness/tranche_manifests/ROOT-DECOMP-RULINGS-D-GOV-47-20260926.yaml`.
- Notices are routed to the App, Runtime, Piping and PEC loops. The App authority
  corpus pins `software-decomp` hashes, so it will report drift against these
  bytes. Each loop decides its own adoption. No release is made.
