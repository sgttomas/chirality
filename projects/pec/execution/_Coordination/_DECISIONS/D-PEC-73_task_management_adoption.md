# D-PEC-73 — PEC Task Management adoption

**Status:** PROPOSAL — AWAITING OWNER RULING

**DecisionID:** D-PEC-73

**Date presented:** 2026-08-01

**Owner:** Ryan Tufts

**Owning loop:** PEC

**Presentation basis:** `main@3c2e816f1072295de15fdcdf924c19b4b66497bc`

**Subject:** `projects/pec/execution/_Coordination/TM_ADOPTION_PACKET_2026-07-31.md`
**Record convention:** supersede-never-edit after ruling

## Identity correction

The routed Stage-B packet called this ruling `D-PEC-72` indicatively. That
identity is not used: the PEC loop's 2026-07-29 next-work slate already
reserved `D-PEC-72` for the P1 build-slice packet. The PEC register therefore
records the P1 reservation as `D-PEC-72` and mints this adoption question as
the next ordered identity, `D-PEC-73`. This correction changes no substantive
option in the routed packet.

## Live basis

- `D-GOV-32` is RULED and adopts the Task Management PRD Revision 2, subject
  SHA-256
  `97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`.
- K-TM-1..6 are ratified at `docs/CONTRACT.md` §1.14.
- `execution/_Coordination/_TaskManagement/REGISTER.csv` row `TM-ROOT-100`
  records PEC adoption as open Stage-B work. The root loop cannot decide this
  PEC-local question.
- `projects/pec/execution/_Coordination/NOTICE_D-GOV-32_TASK_MANAGEMENT_ADOPTION.md`
  records that D-GOV-32 decides PEC PRD §16 decision 1 only for the Action
  Item register class. Decision registers and every other register class are
  unchanged.
- PEC's accepted product and decomposition bases remain PRD v2.2 and
  `SOFTWARE_DECOMP` revision 1.3. This adoption changes neither.

## Question

Should the PEC loop adopt Task Management and mint its own structured Action
Item register? If yes, which invocation binding should PEC use?

## Options

### O-A — Adopt with on-demand or owner-scheduled TASK_MANAGEMENT invocation (recommended)

Mint the PEC register, but do not bind it to session entry. The owner or loop
invokes `TASK_MANAGEMENT` (`agents/AGENT_TASK_MANAGEMENT.md`) on demand or on
an owner-scheduled routine. Existing PEC entry and receipt behavior remains
unchanged; `_DomainEngines/pec/LOOP_INIT.md` is not amended.

This matches the root loop's owner-ruled operating pattern and keeps Task
Management available without turning register reading into an implicit loop
cadence or gate.

### O-B — Adopt with LOOP_INIT reader binding

Mint the same PEC register and amend `_DomainEngines/pec/LOOP_INIT.md` so:

1. Step 0 reads rows whose `Status` is not `CLOSED`, treating them as
   attention residue rather than a work-discovery queue or directive; and
2. session close records any owner-ruled dispositions in the register, or
   records still-unresolved residue in `LOOP_RECEIPTS.md`.

The register remains non-gating, and a session may still proceed when it is
absent or has no applicable row. The exact amendment is confined to this
behavior and may not convert candidates into assignments or agent authority.

### O-C — Amend

Adopt a modified local binding or register condition stated by the owner in
the ruling. Any amendment that changes scope, authority, schema, or write
ownership must be recorded exactly before application.

### O-D — Decline

Do not mint a PEC Task Management register and do not amend `LOOP_INIT.md`.
Route the decline to the root loop so `TM-ROOT-100` can close with the PEC
decision as evidence. D-GOV-32 and K-TM-1..6 remain applicable standards, but
they create no PEC-local register without PEC adoption.

### O-E — Defer

Leave PEC unbound and `TM-ROOT-100` open. Silence and deferral create no duty.

## Common application if O-A or O-B is ruled

1. Record the owner ruling verbatim here and bring the D-PEC-73 register row
   to `RULED`.
2. Mint the future target
   _DomainEngines/pec/_TaskManagement/REGISTER.csv as a header-only
   schema-1.0 CSV with IDs `TM-PEC-<seq>` and these exact 25 columns:

   ```text
   RegisterSchemaVersion,ActionItemID,Title,Concern,SourceRef,SourceSha,CandidateRef,DomainLenses,AssociatedWith,NoticeRef,ScaRef,Assignment,Priority,PriorityBasis,Status,Trigger,ElevatedTo,Disposition,EvidenceRef,EvidenceSha,EvidenceQuote,Opened,LastReviewed,Closed,Notes
   ```

3. Migrate no root rows. Live inspection finds no root row deferred against
   this adoption; `TM-ROOT-100` is the adoption-tracking row, not a migration
   candidate.
4. Route an ordinary notice to the root loop at the future target
   execution/_Coordination/NOTICE_D-PEC-73_PEC_TASK_MANAGEMENT_ADOPTION.md.
   The notice supplies evidence for the root loop to close `TM-ROOT-100`; the
   PEC loop does not write the root register.
5. Preserve K-TM-1..6 in full: the register is a session-residue disposition
   ledger, never a work-discovery queue, resolution surface, authority source,
   or gate; no agent is the accountable `A`; only this loop writes its
   register; scanner projections remain gitignored and rebuildable.
6. Do not migrate or promote any row during minting. A later first harvest may
   write a candidate-only proposal surface using the emphasis form
   `TM-CANDIDATE: <concern> | <evidence-ref>`. Only the owner may promote
   candidates into `REGISTER.csv`.

For O-A, step 4 is followed with no `LOOP_INIT.md` change. For O-B, the exact
reader-binding amendment described under O-B is also applied. Neither option
opens P1, source implementation, WORKING_ITEMS activation, or any receiving
loop duty.

## Change fence after an adopt ruling

- Existing proposal record:
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-73_task_management_adoption.md`
- Existing PEC decision register:
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- Future register target: _DomainEngines/pec/_TaskManagement/REGISTER.csv
- Future root-notice target:
  execution/_Coordination/NOTICE_D-PEC-73_PEC_TASK_MANAGEMENT_ADOPTION.md
- Existing receipt ledger: `_DomainEngines/pec/LOOP_RECEIPTS.md`
- O-B only, existing entry contract: `_DomainEngines/pec/LOOP_INIT.md`
- Optional future first-harvest proposal, without register writes:
  _DomainEngines/pec/_TaskManagement/HARVEST_CANDIDATES_2026-08-01.md

## Verification and rollback

- Validate the CSV header has exactly 25 columns, schema version is `1.0` for
  every future row, IDs match `TM-PEC-<seq>`, and `Status`/`Disposition` are
  present.
- Confirm no data row exists immediately after minting.
- Run practitioner-harness `self-check`, coordination `coord-check` on the
  branch diff, and `git diff --check`.
- Rollback before publication is deletion of the new header-only register and
  notice plus reversion of this packet/register-row application edits (and,
  for O-B, the one `LOOP_INIT.md` amendment). After publication, supersede by
  a new PEC decision; do not silently rewrite the ruled record.

## Recommendation

Rule **O-A**. It provides the adopted Task Management capability and clear
loop-local ownership while preserving PEC's current Step-0 protocol and the
owner-controlled invocation cadence. O-B is lawful and materially stronger:
it makes register review part of every PEC entry/close cycle.

## Owner ruling

Awaiting owner. Record the return verbatim and identify O-A, O-B, O-C, O-D,
or O-E. No option is inferred from preference or silence.
