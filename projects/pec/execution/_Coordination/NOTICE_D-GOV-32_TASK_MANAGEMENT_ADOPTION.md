# Routed Change Notice — D-GOV-32 Task Management adoption decides PEC PRD §16 open decision 1 for the Action Item register class

Routed by: Root loop, HELP_HUMAN (Agent 0), 2026-07-31, under D-GOV-32
Effect 3 (Task Management Stage A, workplan step 5).

This notice is coordination, never authority. The PEC loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence.

## What changed

D-GOV-32 (ruled 2026-07-31; record effective at PR #424 merge
`1c80a2bc1b2631039149b0fb75dffa3550c583aa`) adopted the Chirality Task
Management PRD, Revision 2
(`plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md`, subject
SHA-256 `97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`),
as the accepted product basis for Chirality Task Management. Its invariants
K-TM-1..6 entered the ratified catalog at `docs/CONTRACT.md` §1.14 (PR #428,
effective `c8c2a6146b8e36103756c37ca78f8fd3b013c31e`).

Per D-GOV-32 Effect 3, this adoption decides PEC PRD §16 open decision 1
("whether decision registers gain light structure at source or remain prose
parsed best-effort") **for the Action Item register class specifically**:
Action Item registers are structured, closure-capable, git-tracked CSV at
source (`Status` and `Disposition` mandatory in every schema version,
K-TM-6), living inside the owning loop's coordination surface (K-TM-2).

Decision registers themselves are untouched: they remain prose, federated by
citation (the adopted PRD §12.5 keeps the ruled residual-row convention),
and PEC PRD §16 decision 1 remains open for every other register class.

## What did not change

No PEC PRD text, decomposition, ScopeOfWork, lifecycle state, contract pin,
hold, reliance state, or SCOPE_CHANGE gate is changed by this notice or by
Root adoption alone. Per D-GOV-32 Effect 4 the PEC loop is not bound by Task
Management: a PEC register exists only after the PEC loop's own ruling under
its own instruments (D-PEC packet), which arrives as Stage-B work with its
own routed packet. Reading any Task Management register creates no duty for
this loop (K-TM-3/K-TM-4).

## Follow-on for this loop

None required by this notice. The root program register carries a row
(`TM-ROOT-100`) tracking the PEC adoption decision as pending Stage-B work;
the Stage-B packet, when routed, is the instrument for the loop's
adopt/amend/decline ruling. Until the loop acts, nothing here binds it.
