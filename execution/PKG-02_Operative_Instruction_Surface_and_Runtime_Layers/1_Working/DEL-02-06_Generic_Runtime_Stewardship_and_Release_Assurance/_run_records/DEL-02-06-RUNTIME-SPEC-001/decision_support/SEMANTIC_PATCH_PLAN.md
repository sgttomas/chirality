# DEL-02-06 deterministic future semantic patch plan

- Status: `DERIVATIVE PLAN — NO CURRENT BYTE MAY BE EDITED`
- Upstream handoff: `handoff/OWNER_GATE_HANDOFF.md` @ `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`
- Scope of Work: `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
- Option coverage: exactly `54/54` mappings for the matrix's `27/27` rows.

## Future package root and patch discipline

Every mapping below targets a future package rooted at:

`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/decision_candidates/OWNER_SELECTION_V1/`

The literal `OWNER_SELECTION_V1` is the first proposed version. A later sealed
brief must prove the path is unused and authorize its exact membership. If it
cannot do so, it must allocate a new version such as `OWNER_SELECTION_V2`; it
must never overwrite or repair existing bytes. Each selected option replaces
only its named placeholder ID in the named future file and heading. Unselected
option text is omitted but remains preserved in this derivative plan.

Proposed future package files are:

1. `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md`
2. `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md`
3. `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md`
4. `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md`
5. `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md`
6. `OWNER_DECISION_RECORD_CANDIDATE_V1.md`

Those files do not exist through this plan and are not authorized here.

## Exact pre-assembly census-tuple gate

Before any placeholder substitution or future output byte is assembled, parse
the selections as the ordered tuple `(TBD-005, TBD-011, TBD-013, CENSUS)`.
The only allowed tuples are exactly:

1. `(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)`
2. `(TBD-005-A, TBD-011-B, TBD-013-A, CENSUS-A)`
3. `(TBD-005-B, TBD-011-A, TBD-013-B, CENSUS-B)`
4. `(TBD-005-B, TBD-011-B, TBD-013-B, CENSUS-B)`

`TBD-011-A` preserves PEC `UNRESOLVED` and routes a PEC-owned
exact-operation/no-effect ruling now. `TBD-011-B` preserves PEC `UNRESOLVED`
and defers that route. Neither option classifies PEC, infers PEC work,
dependency, or veto, prescribes the PEC-owned outcome, or has current effect.

Any other tuple is contradictory, invalid, and explicit no-effect. Reject it
before package-hash or signer/date acceptance, perform no placeholder
substitution, emit no future semantic candidate bytes, and return for a new
versioned response. Future assembly and every fresh refutation must apply this
same four-item allowed set; no precedence or silent normalization is permitted.

## Exact 54-option mapping

| Row / option | Deterministic future path, heading, and placeholder | Inserted semantic disposition | Dependencies | Required validation, refutation, and rerun | No-effect fence |
|---|---|---|---|---|---|
| `D1-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Recovery terminal policy` / `<SEL-D1>` | Distinct recovery terminal plus explicit session-status mapping; preserve all four observed terminal forms. | D3,D4,D7,TBD-006,TBD-016 | Re-run N1 vocabulary inventory, terminal-cardinality design, N4 integration, fresh read-only semantic refutation, and handoff assembly. | No edit to current integration, handoff, contracts, runtime, or client bytes. |
| `D1-B` | same file / heading / `<SEL-D1>` | Reuse `turn.interrupted` with a mandatory recovery reason and explicit consumer-preservation rule. | D3,D4,D7,TBD-006,TBD-016 | Same reruns; additionally prove reason preservation through session summary, Root CLI, and App-owned presentation. | No current event or status vocabulary changes. |
| `D2-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Retry replay and resume` / `<SEL-D2>` | No retry or resume of indeterminate work; any later owner act is a new independent turn. | D1,D3,D4,TBD-006,TBD-008,TBD-016 | Re-run N3 RR-02/03/05/07/13/14 design coverage, N4 integration, fresh refutation, and handoff. | No resend, replay, retry command, or runtime/client change. |
| `D2-B` | same file / heading / `<SEL-D2>` | Operator-only retry after reconciliation, new turn identity, `supersedes_turn_id`, explicit authorization and proof. | D1,D3,D4,TBD-006,TBD-008,TBD-016 | Same reruns plus new authorization, lineage, duplicate-work, and affected-client proof design before adoption. | No operator command or retry behavior is implemented. |
| `D3-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Recovery audit and redaction` / `<SEL-D3>` | Append-only structured recovery record and immutable checkout manifest with exact fields and redaction policy. | D1,D4,D7,D8,TBD-008,TBD-014,TBD-016 | Re-run N3-R08/R09/R10/R15, manifest reproducibility design, N4 integration, fresh refutation, and handoff. | No audit, manifest, secret handling, or authority record changes. |
| `D3-B` | same file / heading / `<SEL-D3>` | Daemon-local structured log with later manual export and explicit non-authoritative status. | D1,D4,D7,D8,TBD-008,TBD-014,TBD-016 | Same reruns plus prove export completeness, ordering, redaction, and checkout reconstruction before adoption. | No daemon log or export mechanism is created. |
| `D4-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Transaction durability and writer ownership` / `<SEL-D4>` | One corpus writer, per-turn atomic compare-and-append, durable summary, final batch manifest, closed readiness until complete. | D1,D3,D7,D9,TBD-006,TBD-016 | Re-run N3-R02/R07/R10/R12 and RR-04/05/08/09/18 design, N4, fresh refutation, handoff. | No store, lock, event, or session byte changes. |
| `D4-B` | same file / heading / `<SEL-D4>` | Whole-corpus all-or-nothing recovery transaction. | D1,D3,D7,D9,TBD-006,TBD-016 | Same reruns plus exact storage-feasibility and crash-boundary proof design; return if Context Envelope M is exceeded. | No transaction primitive or runtime write is authorized. |
| `D5-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Drain reconstruction` / `<SEL-D5>` | Treat every unresolved accepted turn as a local drain contribution until disproved. | D6,D8,TBD-016 | Re-run N1 residency inventory, N3 DA-01..06/RR-10..12, N4, fresh refutation, handoff. | No drain counter, model, residency, activation, or attribution change. |
| `D5-B` | same file / heading / `<SEL-D5>` | Count only proven-local turns; ambiguous attribution is a separate activation blocker. | D6,D8,TBD-016 | Same reruns and prove numeric ledger plus blocker ledger are complete and non-overlapping. | No model/residency action or invented attribution. |
| `D6-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md` / `## Recovery readiness and retained functions` / `<SEL-D6>` | Retain truthful non-mutating health/status, byte-stable replay, and list/get diagnostics; block all consequential/mutating surfaces. | D3,D5,D7,D8,TBD-009,TBD-016,CENSUS | Re-run complete route/direct-entry census, N3-R03/R13 and RR-17, affected-client matrices, N4, fresh refutation, handoff. | No route, direct entry, client surface, or foreign function changes. |
| `D6-B` | same file / heading / `<SEL-D6>` | Retain only minimal recovery-not-ready health; block every other daemon surface. | D3,D5,D7,D8,TBD-009,TBD-016,CENSUS | Same reruns plus diagnostic sufficiency and evidence-access review. | No endpoint availability or daemon behavior changes. |
| `D7-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Malformed and contradictory evidence` / `<SEL-D7>` | Preserve/quarantine exact affected unit, allow safe diagnostics, hold global consequential readiness pending authorized disposition. | D1,D3,D4,D6,TBD-008,TBD-016 | Re-run N3-R08/R10 and RR-04/06/15/16, repair-authority design, N4, fresh refutation, handoff. | No corpus inspection, quarantine, repair, or runtime mutation. |
| `D7-B` | same file / heading / `<SEL-D7>` | Block and quarantine entire registered corpus on first malformed or contradictory item. | D1,D3,D4,D6,TBD-008,TBD-016 | Same reruns plus blast-radius and diagnostic-continuity review. | No corpus-wide block or quarantine is activated. |
| `D8-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Acceptance-time attribution` / `<SEL-D8>` | Persist provider, engine, model, locality, and residency epoch with acceptance and bind recovery to those facts. | D3,D5,D6,TBD-016 | Re-run source/schema inventory, N3-R06/R09/R15 and DA cases, N4, fresh refutation, handoff. | No event schema, provider/model field, or runtime state change. |
| `D8-B` | same file / heading / `<SEL-D8>` | Derive recovery attribution from current session selection and residency record. | D3,D5,D6,TBD-016 | Same reruns plus stale-selection, missing-epoch, and ambiguity refutation; return on invented attribution. | No current attribution or model state is relied upon or changed. |
| `D9-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md` / `## Cutover rollback and irreversible boundary` / `<SEL-D9>` | Roll back source only before first recovery mutation; afterward require proven old-reader compatibility or separately approved forward repair. | D1,D4,TBD-006,TBD-014,COMPAT-DELTA | Re-run N3 CO-01..07/RR-18, compatibility analysis, N4, fresh refutation, handoff; later CHANGE/deployment remain separate. | No cutover, corpus mutation, rollback, Git, deployment, lifecycle, or release act. |
| `D9-B` | same file / heading / `<SEL-D9>` | Restore exact old runtime at any failed cutover point while preserving corpus and audit bytes. | D1,D4,TBD-006,TBD-014,COMPAT-DELTA | Same reruns plus exact proof old bytes interpret every possible post-mutation corpus; return if not proven. | No restore or Git/deployment authority. |
| `TBD-001-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Identity grammar` / `<SEL-TBD-001>` | Grammar `root-runtime-<positive-decimal-epoch>`; exact initial epoch remains an owner-supplied value in the future package. | TBD-015,COMPAT-DELTA | Re-run compatibility candidate validation, collision/reserved-value review, N4, fresh refutation, handoff. | No identity value, contract, repin, or release effect. |
| `TBD-001-B` | same file / heading / `<SEL-TBD-001>` | Opaque UUID/hash identity with exact canonical encoding and comparison. | TBD-015,COMPAT-DELTA | Same reruns plus canonicalization and provenance-binding review. | No current identity is minted. |
| `TBD-002-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Declaration and comparison` / `<SEL-TBD-002>` | Two-sided per-operation preflight and request-bound exact equality before consequential work. | TBD-001,TBD-003,TBD-004,COMPAT-DELTA | Re-run protocol/client inventory, mismatch negative cases, affected-client proof design, N4, fresh refutation, handoff. | No route, request field, comparison, or client behavior changes. |
| `TBD-002-B` | same file / heading / `<SEL-TBD-002>` | Exact equality only at daemon or session start. | TBD-001,TBD-003,TBD-004,COMPAT-DELTA | Same reruns plus stale-binding and mid-session-change refutation. | No startup/session behavior changes. |
| `TBD-003-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Mismatch envelope` / `<SEL-TBD-003>` | Distinct `RUNTIME_COMPATIBILITY_MISMATCH` class and exact envelope preserved through Root and separately owned App presentation. | TBD-001,TBD-002,TBD-007,TBD-009,CENSUS | Re-run ten-condition matrix, Root CLI matrix, App-owned matrix planning, N4, fresh refutation, handoff. | No error constant, adapter, CLI, or App byte changes. |
| `TBD-003-B` | same file / heading / `<SEL-TBD-003>` | Generic `RUNTIME_UNAVAILABLE` class with compatibility detail. | TBD-001,TBD-002,TBD-007,TBD-009,CENSUS | Same reruns plus prove machine-readable mismatch survives simplification; return if class is erased. | No current error/presentation change. |
| `TBD-004-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Compatibility binding record` / `<SEL-TBD-004>` | One immutable complete binding manifest for contract, source, release, clients, evidence, and disposition. | TBD-001,TBD-005,TBD-014,TBD-015,CENSUS,COMPAT-DELTA | Re-run manifest determinism/completeness twice, N4, fresh refutation, handoff. | No present source/release/client/evidence binding or release act. |
| `TBD-004-B` | same file / heading / `<SEL-TBD-004>` | Multiple immutable linked records joined by the exact compatibility identity. | TBD-001,TBD-005,TBD-014,TBD-015,CENSUS,COMPAT-DELTA | Same reruns plus dangling-link and partial-fan-in adversarial checks. | No binding record is created. |
| `TBD-005-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` / `## Accepted census disposition` / `<SEL-TBD-005>` | Root CLI/App affected; Piping/Tier-0 not affected; PEC unresolved, exactly as N2. | TBD-009,TBD-011,TBD-013,CENSUS,COMPAT-DELTA; only with TBD-013-A/CENSUS-A, either TBD-011 | Before assembly, require an allowed A-posture tuple; then re-run source-hash and obligation checks, N2 census, N4, fresh refutation, handoff; route foreign gates separately. | A disallowed tuple is rejected and no-effect; no client work, PEC ruling, dependency, veto, or foreign write. |
| `TBD-005-B` | same file / heading / `<SEL-TBD-005>` | Defer the whole census; retain all N2 classifications as unaccepted planning evidence. | TBD-009,TBD-011,TBD-013,CENSUS,COMPAT-DELTA; only with TBD-013-B/CENSUS-B, either TBD-011 | Before assembly, require an allowed B-posture tuple; re-run census on source drift before later decision; N4/refutation/handoff remain held. | A disallowed tuple is rejected and no-effect; no client classification is accepted. |
| `TBD-006-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md` / `## Recovery cutover replay and indeterminate completion` / `<SEL-TBD-006>` | Staged no-replay policy preserving partial output and an irreversible rollback boundary, populated from selected D1/D2/D4/D9. | D1,D2,D4,D9,TBD-016 | Re-run N3 RR/CO matrices, N4 synthesis, fresh refutation, handoff. | No migration, replay, cutover, rollback, or runtime effect. |
| `TBD-006-B` | same file / heading / `<SEL-TBD-006>` | Retain unresolved; no composite recovery/cutover clause. | D1,D2,D4,D9,TBD-016 | Keep semantic integration and implementation held; rerun after later exact ruling. | No present effect. |
| `TBD-007-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md` / `## Ten-condition identifiers and envelopes` / `<SEL-TBD-007>` | One distinct stable machine identifier and exact envelope per ten-condition row. | D1,D7,TBD-003,TBD-008,TBD-016 | Re-run exact ten-row/nine-column preservation, identifier uniqueness, presentation preservation, N4, fresh refutation, handoff. | No runtime constants, adapters, or client bytes change. |
| `TBD-007-B` | same file / heading / `<SEL-TBD-007>` | Coarse boundary identifiers with exact condition subtype fields. | D1,D7,TBD-003,TBD-008,TBD-016 | Same reruns plus prove subtype cannot be erased at every presentation boundary. | No current error taxonomy changes. |
| `TBD-008-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md` / `## Precedence retry and evidence fields` / `<SEL-TBD-008>` | Ordered first-blocking response, complete redacted audit, retry false unless D2 separately allows it. | D2,D3,D7,TBD-007,TBD-016 | Re-run precedence permutations, redaction/adversarial review, N4, fresh refutation, handoff. | No retry timing, redaction, evidence, or response behavior changes. |
| `TBD-008-B` | same file / heading / `<SEL-TBD-008>` | Unordered multi-error response with all safe fields. | D2,D3,D7,TBD-007,TBD-016 | Same reruns plus deterministic ordering/canonicalization and leakage review. | No current response change. |
| `TBD-009-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` / `## Client conformance package partition` / `<SEL-TBD-009>` | Separate Root CLI and App matrices; PEC matrix only after a PEC-owned exact obligation. | D6,TBD-005,TBD-011,CENSUS | Re-run N2, N3 retained-function matrix, Root proof design, route App/PEC to their owners, N4, fresh refutation, handoff. | No client implementation/conformance or foreign-loop write. |
| `TBD-009-B` | same file / heading / `<SEL-TBD-009>` | One generic client matrix for every classified client. | D6,TBD-005,TBD-011,CENSUS | Same reruns plus authority-partition refutation; return if it transfers client ownership. | No generic matrix is adopted. |
| `TBD-010-A` | `OWNER_DECISION_RECORD_CANDIDATE_V1.md` / `## Tier-0 relationship routing` / `<SEL-TBD-010>` | Prepare and route a continue-separate Tier-0 relationship candidate; Root semantics unchanged. | TBD-001,TBD-004,COMPAT-DELTA | Re-run exact identity citations and no-transfer review; send only under a separately authorized coordination act; record Tier-0 response before release fan-in. | No Tier-0 decision, record, Root identity, or foreign write occurs now. |
| `TBD-010-B` | same file / heading / `<SEL-TBD-010>` | Defer Tier-0 routing. | TBD-001,TBD-004,COMPAT-DELTA | Keep Tier-0 relationship fan-in unresolved; rerun before release if relationship is affected. | No coordination act. |
| `TBD-011-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` / `## PEC v2 disposition` / `<SEL-TBD-011>` | Preserve `UNRESOLVED`; route a PEC-owned exact-operation/no-effect ruling now, only under PEC authority. | TBD-005,TBD-009,TBD-013,CENSUS; allowed with either coherent census posture | Before assembly, require one of the two allowed tuples containing TBD-011-A; re-run PEC source currency only under an authorized census refresh; route without prescribing outcome; fresh refutation and handoff. | A disallowed tuple is rejected and no-effect; no PEC work, dependency, classification, veto, prescribed outcome, or write. |
| `TBD-011-B` | same file / heading / `<SEL-TBD-011>` | Preserve PEC `UNRESOLVED`; defer the PEC-owned exact-operation/no-effect ruling route with no current PEC effect. | TBD-005,TBD-009,TBD-013,CENSUS; allowed with either coherent census posture | Before assembly, require one of the two allowed tuples containing TBD-011-B; refute any PEC classification, inferred work/dependency/veto, or prescribed PEC outcome; keep the route deferred and handoff unresolved. | A disallowed tuple is rejected and no-effect; no PEC route, work, dependency, classification, veto, prescribed outcome, or write. |
| `TBD-012-A` | `OWNER_DECISION_RECORD_CANDIDATE_V1.md` / `## Uncovered ownership seams` / `<SEL-TBD-012>` | Record no additional seam currently proven and require source-cited owner routing for any later seam. | CENSUS | Re-run census/source review on drift, N4, fresh refutation, handoff. | No owner, client, dependency, or work package is invented. |
| `TBD-012-B` | same file / heading / `<SEL-TBD-012>` | Create an omnibus Root seam owner. | CENSUS | Mandatory governance/authority refutation; return on conflict with named foreign ownership. | No omnibus ownership is created. |
| `TBD-013-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` / `## Piping disposition` / `<SEL-TBD-013>` | Piping `NOT_AFFECTED` on current evidence; reopen only on a later accepted Piping-owned obligation. | TBD-005,CENSUS; only with TBD-005-A/CENSUS-A | Before assembly, require an allowed A-posture tuple; re-run Piping obligation check on source drift, N2, N4, fresh refutation, handoff. | A disallowed tuple is rejected and no-effect; no Piping work, dependency, or foreign write. |
| `TBD-013-B` | same file / heading / `<SEL-TBD-013>` | Retain Piping unresolved. | TBD-005,CENSUS; only with TBD-005-B/CENSUS-B | Before assembly, require an allowed B-posture tuple; keep census incomplete and implementation/release fan-in held; rerun after a source-cited ruling. | A disallowed tuple is rejected and no-effect; no Piping classification or work. |
| `TBD-014-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md` / `## Semantic conformance and regression matrix` / `<SEL-TBD-014>` | Accept N3 as complete required design only; every matrix remains pending execution under later exact authority. | D1,D2,D3,D4,D5,D6,D7,D8,D9,TBD-009 | Revalidate 16 recovery requirements, 18 RR, 6 DA, 8 terminal, 7 CO, 8 retained-function cases; N4, fresh refutation, handoff. | No executable check, pass result, implementation, closure, or reliance evidence. |
| `TBD-014-B` | same file / heading / `<SEL-TBD-014>` | Replace N3 with a reduced evidence matrix. | D1,D2,D3,D4,D5,D6,D7,D8,D9,TBD-009 | Mandatory coverage comparison and refutation; return on any weakened positive/negative/adversarial obligation. | No evidence plan is changed now. |
| `TBD-015-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Epoch-change criteria` / `<SEL-TBD-015>` | New epoch for adopted consequential client-visible semantics; no change for evidence-only/internal non-observable changes. | TBD-001,TBD-004,COMPAT-DELTA | Re-run compatibility impact analysis, affected-client census, binding completeness, N4, fresh refutation, handoff. | No epoch, repin, client work, release, or Git effect. |
| `TBD-015-B` | same file / heading / `<SEL-TBD-015>` | Case-by-case epoch choice without a standing criterion. | TBD-001,TBD-004,COMPAT-DELTA | Re-run impact analysis for every tranche; fresh refutation must test consistency and hidden defaults. | No current epoch ruling. |
| `TBD-016-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` / `## Daemon recovery state machine` / `<SEL-TBD-016>` | Explicit `RECOVERY_REQUIRED`, `RECOVERY_SCANNING`, `RECOVERY_BLOCKED`, and `READY` states plus distinct corpus classes and transitions. | D1,D2,D3,D4,D5,D6,D7,D8,TBD-006,TBD-007,TBD-008 | Re-run state/precedence matrix, readiness races, Agent 1 parity, N4, fresh refutation, handoff. | No daemon state, readiness, admission, or runtime behavior changes. |
| `TBD-016-B` | same file / heading / `<SEL-TBD-016>` | Boolean readiness flag with error detail outside the state model. | D1,D2,D3,D4,D5,D6,D7,D8,TBD-006,TBD-007,TBD-008 | Same reruns plus prove cause, precedence, resumability, and indeterminate completion remain machine-readable. | No Boolean flag or runtime behavior is introduced. |
| `CENSUS-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` / `## Accountable-human census ruling` / `<SEL-CENSUS>` | Accept exact N2 five-row census; foreign implementation/conformance gates remain separate and PEC remains unresolved. | TBD-005,TBD-009,TBD-011,TBD-013,COMPAT-DELTA; only with TBD-005-A/TBD-013-A, either TBD-011 | Before assembly, require an allowed A-posture tuple; re-run N2 hash/obligation checks and any drifted sources, N4 integration, fresh refutation, handoff. | A disallowed tuple is rejected and no-effect; no client work, migration, conformance, dependency, veto, release, or foreign effect. |
| `CENSUS-B` | same file / heading / `<SEL-CENSUS>` | Defer census acceptance; retain N2 only as planning evidence. | TBD-005,TBD-009,TBD-011,TBD-013,COMPAT-DELTA; only with TBD-005-B/TBD-013-B, either TBD-011 | Before assembly, require an allowed B-posture tuple; hold semantic adoption and implementation; rerun census before later decision. | A disallowed tuple is rejected and no-effect; no classification is accepted. |
| `COMPAT-DELTA-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` / `## Recovery compatibility disposition` / `<SEL-COMPAT-DELTA>` | `DELTA` if recovery semantics are adopted; require new exact identity and complete binding before implementation. | D1,D6,TBD-001,TBD-002,TBD-003,TBD-004,TBD-005,TBD-015,CENSUS | Re-run compatibility analysis, census, binding validation, N4, fresh read-only refutation, handoff. | No delta, identity, contract, repin, client work, implementation, or release effect. |
| `COMPAT-DELTA-B` | same file / heading / `<SEL-COMPAT-DELTA>` | `NO_CHANGE` only if recovery is not adopted or exact later proof shows no consequential client-visible change. | D1,D6,TBD-001,TBD-002,TBD-003,TBD-004,TBD-005,TBD-015,CENSUS | Require explicit no-change evidence and adversarial refutation; return if recovery-before-readiness or machine behavior changes remain. | No current no-change ruling or compatibility effect. |

## Package-wide checks after a future selection

The later author must verify one and only one option for every row, then apply
the exact census-tuple gate before package-hash or signer/date acceptance and
before any placeholder substitution. It must also verify exact
response-token/package-hash binding, 27/27 row and 54-option source
traceability, dependency closure without silently ordering a cycle, exact
accepted-base hashes, UTF-8/text hygiene, immutable manifest reproducibility,
and no owner token embedded in candidate files. A disallowed tuple is invalid
and no-effect: emit no future semantic candidate bytes and return for a new
versioned response. The later author must rerun basis and census checks on
drift, regenerate integration candidates only after tuple acceptance, dispatch
a genuinely fresh read-only refuter that independently reapplies the identical
four-tuple set, and assemble a new immutable handoff only after that refutation
passes. A material finding returns to the owning author or human gate; the
verifier does not repair.

## Global no-effect fence

A disallowed census tuple never authorizes assembly and has no effect. This
plan never directs an edit to `accepted_inputs/`, `basis/`, `inventory/`,
`clients/`, `evidence/`, `integration/`, `handoff/`, `ScopeOfWork.md`, any
current candidate or acceptance record, `runtime/**`, any client/project,
profile/check, dependency, SCA/decomposition/PRD, Task Management, lifecycle,
release, publication, issuance, reliance, Git, PR, merge, or foreign-loop
surface. Only a later sealed brief and exact accountable-human decision may
create a new versioned candidate package.
