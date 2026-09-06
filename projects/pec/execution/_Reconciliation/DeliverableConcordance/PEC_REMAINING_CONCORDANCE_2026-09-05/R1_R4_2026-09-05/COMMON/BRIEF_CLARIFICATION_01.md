# Brief clarification 01 — residual identifiers and mechanical fields

**Status:** Existing D81 rule clarified; no new scope or semantic convention.
**Authority:** D81 as incorporated by effective D82; Agent0 relay on 2026-09-05.
**Applies to:** all package managers, their specialists/verifiers and synthesis.

D81 `D-PEC-81_remaining_concordance_activation_2026-09-05.md`, “R0 sample and
proposed convention set”, stable-ID bullet, states:

> Residual proposals use `<DeliverableID>-REM-001` sequence, with many-to-many
> claim links where justified and no collision with a later existing item.

The exact pinned proposal SHA-256 is
`97b8bc73995ca415a530cbbec4a5e02111131e25faba2b3611aeac510c0e7626`.
Its repository path is
`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-81_remaining_concordance_activation_2026-09-05.md`.
D82 incorporates D81’s schema and the accepted calibration conventions;
R0 did not supersede this identifier syntax.

The sealed package briefs declare residual columns but omit an explicit pattern.
Their silence does not replace the controlling rule. Future worker residual IDs
must use their exact deliverable ID, literal `-REM-`, and a zero-padded sequential
three-digit suffix starting at001: e.g. `DEL-01-05-REM-001`, then
`DEL-01-05-REM-002`. For the current corpus the lexical check is
`^DEL-[0-9]{2}-[0-9]{2}-REM-[0-9]{3}$`; additionally require the exact owning
DeliverableID prefix, unique sequence and no collision with existing item IDs.
Apply identical IDs to all claim backlinks, residual rows, selected manifests
and summaries. Do not change stable production requirement/claim identifiers.

The same D81 section specifies `Depends: <exact target IDs or NONE>` and an
exact owner gate using `(gated: ...)`, `(stage-gated: ...)`, or
`NOT_SELECTABLE_UNTIL:`. Accordingly:

- Populate the CSV `Depends` field with `NONE` when there is no named target;
  otherwise retain only the exact justified target IDs. Empty text is not NONE.
- Populate `ExactGate` with the literal `(gated: ...)` or
  `NOT_SELECTABLE_UNTIL:` marker and its actual condition. D81 also expressly
  permits the `(stage-gated: ...)` marker. Plain prose without a governed marker
  is not a conforming gate field. Adding the marker changes representation only,
  not the existing owner condition, source grant or selectability.

Use the full adopted claim schema from D81, as echoed in sealed package briefs:
`ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,
CurrentState,ImplementationEvidence,VerificationEvidence,
ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,
ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,
Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes`.
The residual ledger contract remains the sealed brief's
`ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,
AuthorityNeeded,Selectability,Notes`. No field or semantic distinction is removed.

Before future worker handoff, pass deterministic checks for exact column order,
unique owner-prefixed sequential residual IDs, claim/residual reciprocal links,
nonempty Depends with explicit NONE when appropriate, literal gate markers,
unchanged source-bound conditions, source commit/hashes and LF CSV bytes.
A structural pass is not semantic acceptance or execution authority.

Agent0 relay received by the common integration node: package workers in PKG01
and PKG10 used noncanonical residual syntax; initial managers were notified
directly. HELP_HUMAN directed this append-only clarification for later managers.
Agent0 subsequently identified the same mechanical Depends/gate-field issues
in initial PKG01/PKG02 originals and confirmed their managers are preparing fresh
mapped corrections. This is attributed coordination evidence, not a new owner ruling.

Preserve sealed briefs and completed original outputs. A completed naming or mechanical-field defect
is corrected by a fresh bounded specialist into a separate mapped derivative,
with exact old/new ID, backlink, Depends/gate-field accounting plus independent
backcheck. Existing condition text and meaning are preserved.
No semantic rerun, new findings, source change or scope reinterpretation is
needed solely for naming. Synthesis selects the verified corrected derivative
while retaining original provenance. Package managers own their corrections;
this common integration node writes no package artifact and dispatches nobody.

This clarification appends to COMMON; COMMON_FROZEN_MANIFEST and prior sealed
essentials remain unchanged. HELP_HUMAN supplies this file to later managers.
