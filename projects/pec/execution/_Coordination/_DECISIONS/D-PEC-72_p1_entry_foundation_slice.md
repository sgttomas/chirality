# D-PEC-72 — P1-entry foundation slice

**Status:** RULED — O-B — EXECUTION AUTHORIZED

**DecisionID:** D-PEC-72

**Date presented:** 2026-08-01

**Owner:** Ryan Tufts

**Owning loop:** PEC

**Presentation basis:** `main@3c2e816f1072295de15fdcdf924c19b4b66497bc`; accepted decomposition revision 1.3

**Source selection:** `projects/pec/execution/_Coordination/PEC_NEXT_WORK_SLATE_2026-07-29.md`

**Structural precedent:** the owner-gated, exact-fence, separate-execution-and-acceptance
convention in
`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-63_pec_phase_2_2_scope_of_work_initialization_wave.md`;
this packet narrows that pattern to two package activations and three existing
production contracts.

## Owner selection that opened packet drafting

Owner return recorded verbatim (2026-08-01, in-session, Ryan Tufts):

```text
Here my response:

D-PEC-73: O-A.
D-PEC-72: select for packet drafting.
```

The D-PEC-72 line authorizes this packet's drafting only. It does not rule an
option below and grants no production or source-work authority.

## Live-state finding that fixes the first slice

The accepted deliverable-local dependency basis carries constraint `C-05`
`PRE_P1_OBLIGATION`: all three pre-P1 deliverables must complete before any P1
node starts. All three contracts are `INITIALIZED`, advisory-unblocked, and
passed the active-reliance-hold `candidate-validation` preflight on 2026-08-01:

| Package activation | Deliverable | Output class |
|---|---|---|
| PKG-00 Architecture Runway & Contracts | `DEL-00-01` v2 first ADRs | Core-isolation ADR plus carried-posture ADR content |
| PKG-00 Architecture Runway & Contracts | `DEL-00-03` v2 SPEC seed | Seed SPEC derived from accepted revision 1.3 |
| PKG-10 Validation & Measurement | `DEL-10-01` Step-0 cost baseline | Repeatable method plus pre-P1 baseline report |

WORKING_ITEMS owns one package per instance. Execution would therefore use two
separate package activations under the same owner-ruled tranche, with disjoint
writes and validated fan-in. No P1 deliverable is activated by this packet.

## Question

Should PEC authorize this exact three-deliverable pre-P1 production tranche,
including the owner architecture choice required by `DEL-00-01`?

## Options

### O-A — Authorize the pre-P1 foundation tranche (recommended)

Authorize the two bounded WORKING_ITEMS package activations and the exact
outputs/fences below. Within `DEL-00-01`, select **functional core / imperative
shell** for OI-012, while keeping the entity-schema/core versus
store-persistence/adapter seam explicit. This is the lighter of the two styles
recorded at decomposition Gate 4 and retains every invariant the gate found
forced under either style.

For `DEL-10-01`, the method shall report both distinct observations rather
than silently substitute one for the other:

- the PRD §11 metric — LLM tokens per PEC loop-iteration orientation; and
- the practitioner-harness precondition's original command-latency measure.

The sample is PEC-loop-only and creates no duty for another loop. The method
must name its sample count, exact Git SHA, observation window, model/runtime,
and input/output/cached-token boundary. If the runtime does not expose exact
token usage by the declared classes, the run records that limitation and
returns `DEL-10-01` unaccepted; it may not estimate, backsolve, or fabricate a
token count, and `C-05` remains open.

### O-B — Authorize with hexagonal / ports-and-adapters core isolation

Authorize the identical paths, measurement posture, checks, and fences, but
select ports-and-adapters / hexagonal isolation for OI-012. The ADR must still
state the entity-schema/core versus store-persistence/adapter seam and may not
restore the retired v0.4 PEC-project-adapter allocation.

### O-C — Amend

Authorize only after the owner states an amended deliverable set, artifact
path, architecture choice, measurement sampling design, or check condition.
Any amendment that adds a P1 node, shared project profile, source tree, runtime
dependency, cross-package write, or acceptance criterion requires a revised
packet before execution.

### O-D — Defer or decline

Leave all three deliverables `INITIALIZED`. `C-05` remains open and every P1
node remains blocked by the pre-P1 obligation. No source path is opened.

## Exact O-A/O-B production fence

### PKG-00 activation

Selected deliverables: `DEL-00-01`, `DEL-00-03`.

Allowed production targets:

- future target: projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md
- future target: projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md
- each selected deliverable's `_run_records/D-PEC-72_*.md`

The ADR output decides only OI-012 in the style selected by this ruling,
re-cites ADR-002 as the sole live carried posture, treats ADR-014 as historical
lineage, carries the accepted Root-runtime / optional-client / no-second-loop /
human-only-act boundary, and decides none of OI-001..009 or OI-013.

The SPEC seed derives only from PRD v2.2 and accepted decomposition revision
1.3. It is a seed other packages may cite; it is not an implementation,
acceptance, or release claim.

### PKG-10 activation

Selected deliverable: `DEL-10-01`.

Allowed production targets:

- future target: projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/artifacts/STEP0_COST_BASELINE_METHOD.md
- future target: projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/artifacts/STEP0_COST_BASELINE.md
- its `_run_records/D-PEC-72_*.md`

The baseline is measurement evidence only. It neither directs the practitioner
harness nor opens its cache half, specifies another package's behavior,
asserts an after-P1 value, nor evaluates the PRD falsification clause.

### Shared coordination and closeout targets

- this decision record and the PEC decision register;
- `_DomainEngines/pec/LOOP_RECEIPTS.md`;
- one future D-PEC-72 execution handoff under
  projects/pec/execution/_Coordination/D-PEC-72_P1_ENTRY_FOUNDATION_2026-08-01/;
- `projects/pec/docs/STATUS.md` only for a post-acceptance pointer update, and
  only after the owner accepts all three deliverables.

No other path is opened. In particular this packet does not authorize any
edit under the frozen v0.4 source corpus, any new v2 source tree, the absent
future profile target projects/pec/software-workflow.json, root `runtime/`, dependency registers,
decomposition truth, ScopeOfWork contracts, PRD text, or another package.

## Work graph and gates after ruling

1. Run the active-reliance-hold preflight with operation
   `dispatch-for-production` against all three contracts; any match fails
   closed.
2. Freeze two activation briefs: PKG-00 (`DEL-00-01`, `DEL-00-03`) and PKG-10
   (`DEL-10-01`), each with the exact targets above. ResponsibleParty remains
   `TBD` unless the owner names a human; no agent is recorded as accountable.
3. The two package activations may proceed independently because their writes
   are disjoint. Each retains one integration owner within its package.
4. Validate every output against its contract's `OUT-*`, `REQ-*`, `AC-*`, and
   `VER-*` mappings. Missing exact token telemetry blocks `DEL-10-01`
   acceptance but does not invalidate completed PKG-00 outputs.
5. Route the outputs to REVIEW and then to the owner. Writing files does not
   complete a deliverable.
6. Only the owner may accept the selected core-isolation ADR, the SPEC seed,
   and the baseline as fit evidence. Only after all three acceptances are
   recorded may `_STATUS.md` lifecycle changes and `C-05` closure be proposed.
7. The first actual P1 source slice requires a successor D-PEC packet. That
   successor must name the new v2 source tree and the project-local
   `software-workflow.json`; neither exists or is selected here.

## Verification

- Contract-specific semantic inspection for all mapped `AC-*`/`VER-*` rows.
- Exact path containment: PKG-00 writes only inside PKG-00 targets; PKG-10
  writes only inside PKG-10 targets; coordination closeout only at the named
  shared paths.
- Citation resolution and full SHA-256 manifest for produced artifacts and
  cited accepted bases.
- Strict decomposition-register validation and dependency-closure invariants:
  64 registers, 254 rows, 119 edges, zero SCCs, zero strict findings unless a
  later live run records and explains a different accepted basis.
- Practitioner-harness `self-check`; `coord-check` over the committed range;
  `git diff --check`.
- No dependency or manifest change; no frozen-corpus modification; no runtime
  service, database, external network, release, or professional-reliance act.

## Rollback and failure isolation

Before publication, rollback deletes only newly produced targets and restores
the packet/register/receipt pointer edits. After publication, corrections use
a successor record; ruled bytes are never silently rewritten.

A failure in one package holds only its own outputs and the `C-05` fan-in.
Validated outputs in the other package remain candidate work but cannot open
P1 until all three deliverables are owner-accepted.

## Recommendation history

The packet as presented recommended **O-A** because it was the decomposition's
lighter recorded style for a deterministic-derivation service. During owner
review, the owner clarified the intended system property: App, Root, PEC, Task
Management, and domain-specific applications are to remain individually
interchangeable and communicate through typed contracts. The resulting
in-session recommendation changed to **O-B** for explicit application-boundary
ports and adapters, while retaining functional-core / imperative-shell as a
compatible internal implementation technique within each bounded application.

That broader architectural intent is recorded here as the reason for the
selection. This PEC-owned decision binds only the PEC v2 core-isolation ADR;
it creates no implementation duty, contract, or architecture ruling for App,
Root, Task Management, Piping, or any other receiving loop.

## Owner ruling

**Ruled O-B on 2026-08-01.**

Owner architecture intent recorded verbatim during the option discussion:

```text
Each of App, Root, PEC, TM, and domain specific applications like Piping, should all be individually interchangeable and each communicate through typed contracts.

I think that's what I want but I'm open to discussion here.
```

Owner ruling recorded verbatim after the recommendation was updated to O-B:

```text
I agree with this proposal for D-PEC-72 and approve action as you recommend.
```

The referenced proposal recommended O-B: hexagonal boundaries between bounded
applications, capability-shaped typed contracts at the boundaries, and
functional-core / imperative-shell permitted within an application. The ruling
therefore selects O-B and opens only the exact production fence in this packet.
It is not advance acceptance of artifacts that did not yet exist.
