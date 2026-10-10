---
name: bounded-reconciliation
description: Compare affected deliverable commitments, design and dependency conditions with a concrete result and make warranted source edits.
---
# Bounded reconciliation

Use this method when a change may leave its current deliverable documents out of
step with the result. It is a bounded comparison, not a mandatory final stage or
a whole-corpus audit. Perform warranted edits in the PR doing the work.

Identify the affected deliverables, actual candidate, relevant consumers and
permitted scope from the assignment and diff. Read their ScopeOfWork, Design
and dependency conditions. Follow only the sources needed to establish the
meaning of the affected commitment or interface. During migration, existing
CSV dependencies remain source inputs until their replacement is available.

Compare the documents with implementation and meaningful verification. Separate
missing behaviour from stale description and missing evidence. Keep future
requirements when the implementation falls short. A passing rerun alone does
not explain how a known defect was repaired.

Correct ordinary factual descriptions and dependency conditions within the
assignment. Decisions edit the current text they govern. Preserve commitments,
acceptance criteria, explicit holds and product boundaries; bring any reserved
change to the owner as a concrete choice and consequence. Do not turn incidental
implementation detail into another continuing documentation obligation.

Check the changed documents together with affected consumers. Where a comparison
finds no warranted edit, report that result without creating a record. Where it
finds unfinished required work, repair it within authority or report the specific
obstruction; moving it to another list does not complete it.

Return the changed locations, checks, findings and open decisions. The PR is the
change record. Do not add receipt files, MEMORY entries, claim ledgers or routine
handoff documents. Keep a replaceable current-state note only when recovery
requires it. This comparison does not itself declare acceptance or release.
