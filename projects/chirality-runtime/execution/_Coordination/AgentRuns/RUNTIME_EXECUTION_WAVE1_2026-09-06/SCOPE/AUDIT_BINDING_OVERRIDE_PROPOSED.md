# Proposed one-run AUDIT_DECOMP input binding

Status: PROPOSED METHOD OVERRIDE; not granted or executed. This is an explicit exception to AUDIT_DECOMP v2.1 normative input-binding instructions, not a routine supported input parameter. The accountable owner must authorize it; a permanent shared-role repair instead belongs to Root. Route through App Agent0 to owner. This changes only the next bounded audit's input-reading method, not accepted decomposition, shared agent instructions, IDs, scope or acceptance conditions. Prior audit remains FAILED_INPUTS; do not relabel it.

Suggested exact grant:

> For one fresh D36 pre-change AUDIT_DECOMP run on Runtime PKG-02, permit the following explicit input binding in place of the generic SOFTWARE heading/bare-ID assumptions. Keep all twelve checks and all other role constraints. Do not edit any live input or silently relax a finding. Record this override in the new audit Decision_Log.

Execution root: projects/chirality-runtime/execution. Main decomposition: _Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md. All paths below are relative to that execution root.

| Required semantic field | Exact accepted binding |
|---|---|
| Partitions | Main document `SSOW and package partition` table: PackageID, Name, Work domain / inclusions, Exclusions. Preserve PKG-02_Runtime_Product exactly. |
| Production units | Main `Objectives, deliverables and artifacts` explicit reference to `_Decomposition/RUNTIME_DELIVERABLE_REGISTER.csv`: DeliverableID, ParentPackageID, Name, Type, ResponsibleParty, AnticipatedArtifacts, CoversScopeItems, SupportsObjectives, ContextEnvelope. |
| Ledger | Main `SSOW and package partition` explicit reference to `_Decomposition/RUNTIME_SCOPE_LEDGER.csv`: ScopeItemID, InOutStatus, PackageID, DeliverableIDs, ObjectiveIDs. Split semicolon lists without changing member identity. |
| Objectives | Check7 membership derives from ledger ObjectiveIDs; supporting units derive from register SupportsObjectives. `_Decomposition/RUNTIME_OBJECTIVE_REGISTER.csv` ObjectiveID, Statement, MappedDeliverables and MappedScopeItems supply crosscheck evidence, not replacement mapping authority. |
| IDs and filesystem | Full DeliverableID slug matches the identical folder basename under the full ParentPackageID directory /1_Working/. Full package slug likewise matches its directory basename. Numeric prefixes may be displayed as aliases but never replace keys. QualifiedIdentity identifies runtime ownership; historical Root identity is separate. No renaming, suffix removal or rewritten register rows. |
| Requirements and inherited facts | `_Decomposition/INHERITED_REQUIREMENT_TRACE.csv`, admitted source pins/full contracts and live SOWs conserve66 inherited IDs; D36 affected facts remain DEL06 REQ041 and DEL09 REQ001/002. Do not treat candidate amendment postimages as accepted live input. |

Authority status: preserve frozen candidate-era labels and interpret them through MIGRATION_ACCEPTANCE_2026-09-06.md and cited actual owner acts. D36/D126 are on main e1dee34315ff4ca448b0fbc14e5542b6bad9fac2. This does not restart migration or silently accept amendment bytes.

Audit scope remains one package/seven carriers. Resolve contract representation by the current SOW resolver; preserve role-prescribed absent-artifact severity by actual lifecycle. All twelve checks retain PASS/WARNING/BLOCKER/INCOMPLETE/SKIPPED reasoning and exact evidence. A new parser/schema ambiguity fails visibly rather than widening this override.

Writes remain a new immutable COV snapshot under Runtime _Evaluation/DecompCoverage and its tool-owned _LATEST only as specifically authorized; no SCA/accepted-pointer, source, live SOW or decomposition changes. This method grant alone authorizes neither canonical application, commits, SOW propagation, supplier/credential operations nor release. Separate exact canonical application remains pending the completed audit and named postimages in APPLICATION_SUBJECT.json.

Historical SCA005_MIGRATION_POST/Decision_Log.md used semantic fields/full slugs; this informs the proposed mapping but supplies no new audit result or authorization by analogy.

Exact instruction conflict: agents/AGENT_AUDIT_DECOMP.md v2.1 Variant Section Binding requires heading matching and stop when unresolved (line121); SOFTWARE IDs table says no suffix/direct comparison (line146), and missing/unparseable sections prescribe FAILED_INPUTS (line159). Main decomposition lines21/27/31/33 instead explicitly delegate truth to companion registers and preserve full slugs. Input hashes are in INPUTS.json and audit INPUT_HASHES. The corrected audit must precede canonical application. Conditional future application direction cannot preaccept unknown audit findings.
