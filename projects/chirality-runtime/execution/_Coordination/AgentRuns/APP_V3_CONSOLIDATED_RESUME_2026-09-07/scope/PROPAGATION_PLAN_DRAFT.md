# Runtime account-authority propagation plan — draft for Gate 4

Status: DRAFT / UNACCEPTED. This plan authorizes no write by itself.

## Direct SCOPE_CHANGE application subject

After applicable Gate 2, Gate 3 and Gate 4 owner confirmations, apply exactly `author-v2/CANDIDATE.patch` SHA256 `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395` to the synchronized Runtime basis `e8cdc460cffccfe9e58ab4e5b9bbc05350c09327`. It changes exactly:

1. new authoritative companion supplement `_Decomposition/ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`;
2. append-only amendment record in `_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`;
3. SOW-104 `DecisionRef` and `Notes` only in `_Decomposition/RUNTIME_SCOPE_LEDGER.csv`.

Application must create a new immutable Runtime SCA snapshot using the next identifier discovered at application time and must update an active pointer only under its owning act. This draft does not allocate that identifier or move a pointer.

## No-change direct surfaces

All seven deliverable `_CONTEXT.md` and `_STATUS.md` files, `Dependencies.csv`, existing `CUSTODY_DISPOSITION_D36.md`, source requirements and pins, authority maps, objective/deliverable registers, hold maps, historical snapshots, accepted evidence, estimates and schedules receive no direct edit in this amendment. No package/deliverable/objective/requirement identity, scope allocation, topology or lifecycle changes.

## Downstream handoffs after accepted canonical commit

- DEL-02-06: later full ScopeOfWork postimage may amend CLM-003 and REQ-010 only as required by the accepted canonical amendment.
- DEL-02-09: later full ScopeOfWork postimage may amend REQ-001 and REQ-002 only as required by the accepted canonical amendment.
- Those complete SOW postimages must use the actual accepted Runtime decomposition commit as their basis. Historical basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48` remains current until that commit exists.
- A separate author and independent reviewer prepare the two exact SOW subjects. Their owning propagation acceptance/application is not supplied by this Gate 4 draft.
- Root later records required successor adoption for the accepted Runtime transition and later SOW transition through its own instrument.
- App/CLI/client coordination notices remain drafts until they can cite accepted identities; receiving loops own adoption.

## Derivative disposition

Historical migration, audit, estimate, schedule, trace and coverage artifacts remain historical and are not overwritten. At canonical application, the SCA handoff must identify which downstream derivative packages are current, stale-rebuild-required or explicitly deferred. Full wire/recipient, durable lifecycle, successor-recovery, source/synthetic, supplier, paired-consumer, protected-fixture and release evidence remain open and cannot be closed by documentary application.

## Validation and closure

At Gate 5, verify actual patch scope, postimage hashes, CSV parse/field conservation, 1 SOW/7 carriers/4 objectives/66 inherited requirements/9 holds plus R16-B, historical basis, `root-runtime-1` epoch 1, no activation and the Root published identity. Independently audit the actual poststate before owner Gate 5 acceptance. CHANGE publication and fetched-main backcheck follow only after accepted canonical state.

