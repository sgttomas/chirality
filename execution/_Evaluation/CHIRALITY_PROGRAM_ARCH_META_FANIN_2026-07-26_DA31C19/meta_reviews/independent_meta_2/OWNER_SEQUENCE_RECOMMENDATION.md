# Owner Sequence Recommendation — Program-Level Decision Slate

Derived from the comparative meta-review of the three completed tandem reviews (see
`COMPARATIVE_META_REVIEW.md`, crosswalk IDs X-*). Non-governing. Nothing below creates a
requirement; every item routes through its owning instrument and remains the owner's call.
Where the three source packages differ, the difference is stated, not averaged; my
recommendation is marked **REC**.

## The smallest decision-ready owner slate (seven decisions)

### OD-1 — Runtime boundary and route (the load-bearing ruling)
*Sources: codex DQ-01/DQ-02; Root-managed slate 1(a)-(c); PEC-managed D1/D2/D10. Crosswalk X-01, X-02, X-41, X-45.*

1. **Rule the boundary:** Root owns generic runtime semantics; App (and PEC) are clients —
   or rule the opposite by amending D-GOV-20. **REC:** rule Root-owner/App-client; the App
   PRD §17, D-T0-23, and the shipped facade already say it; only the App decomposition §13
   sentence says otherwise.
2. **Choose the Root-side route:**
   - (a) Root PRD amendment adding one minimal operative runtime-ownership/conformance
     commitment, then Root SCOPE_CHANGE (decomposition extension or SOW-027 split with
     `runtime/` as declared write locus — shape is yours); or
   - (b) recorded deferral (OI-013/§12.1 pattern).
   **REC:** (a). If (b), make it *explicitly interim*, name the interim carrier for the
   D-GOV-20 security review and cross-client conformance duties, and set a trigger
   condition — a silent terminal deferral leaves ruled obligations unowned while the
   runtime keeps changing through consumer loops.
3. **Optionally settle the severity convention** that produced every BLOCK-vs-REVIEW
   divergence: adopt the bounded-claim reading (BLOCK attaches to a named reliance claim,
   not to the product). **REC:** adopt; it dissolves the recurring divergence at zero cost.
4. Attach the bounded read-only check all three packages missed (X-44): a daemon-consumption
   census, so the F3/self-authorization question is settled by fact rather than carried.

### OD-2 — App boundary SCOPE_CHANGE (after or coordinated with OD-1)
*Sources: codex DQ-02/DQ-04; RM slate 1(a)/2; PEC D2 + FI-03/FI-05. Crosswalk X-02..X-06, X-19.*

One App SCOPE_CHANGE + D-APP tranche: correct the §13 sentence (deliverable accountability
vs runtime semantic ownership); rescope-or-defer SOW-037/DEL-03-01 and affected runtime
SOWs to client/adapter/presentation/compatibility/acceptance duties; disposition D-APP-48
(retire, supersede, or repin) **resolving the ee290e22/55a066fd source-identity conflict in
the same act**, with a consumer inventory before any semantic-compatibility claim and a
declared validator observation boundary; run the first actual D-APP-49 audit; route notices
to Tier-0 and PEC. Decide whether downstream loops must pin the Root doctrine surfaces they
inherit (X-19) — **REC:** yes, it is what makes the claimed deterministic backstop real.

### OD-3 — App basis-integrity tranche (deterministic start is sequence-independent)
*Sources: RM slate 5; PEC D3/D5; codex DQ-03. Crosswalk X-07..X-12, X-13, X-14, X-16(defer), X-17, X-23(App half).*

- **Now, no dependency:** re-pin the six `decomposition_basis` fields citing the
  nonexistent `416b29033…` object (deterministic defect, no scope change).
- At SCA-APP-004 implementation closeout: re-pin all contracts to one current basis
  (single-pin pattern per Root/PEC); refresh REF-006; fold in stale folder labels.
- One provenance ruling binding the exact accepted decomposition bytes + SCA chain (or
  exact-byte re-acceptance).
- Create-or-defer `contract_invariant_coverage_register.csv` (include §1.13 families if
  created) before any App REVIEW closure.
- SOW-064 coverage-or-deferral; reconcile the seven §8/§9 rows; declare the authoritative
  surface; rule the PKG-00 control-overlay status (retirement available).
- Assign App ResponsibleParty (D-GOV-27 pattern); adopt-or-mark the draft AGENTS overlay.

### OD-4 — Root record and supersession-propagation tranche (mechanical; parallel-safe)
*Sources: codex DQ-05; RM slate 6; PEC D6. Crosswalk X-20..X-23, X-25..X-28.*

Backfill D-GOV-27 EffectiveSHA, then repin the four amended SOWs; fix the decomposition
header SHA-role label; amend DEL-02-01 to cite SPEC §0.2.1 + D-GOV-26/27; add CLAUDE.md to
the §9/_CONTEXT/write-locus enumerations; complete C-4 in README with a correcting receipt;
close OI-011 and refresh the 82 stale ResponsibleParty surfaces; record the O-1 clause gap
(or split SOW-026); repoint CURRENT_WORKPLAN and publish the minimal initialization handoff.
Optional: commission the clause-granularity sweep over the remaining ~100 scope items
(X-27's mechanism, found twice independently).

### OD-5 — Tier-0 and cross-loop coordination tranche
*Sources: RM slate 2/3/9; PEC D4/D7; codex FAN-015/019. Crosswalk X-29..X-38.*

- Ship the overdue D-GOV notice tranche to PEC, Piping, and the domain packs (D-GOV-18/20/
  22/25/26/27 as applicable) — **can start now**; content referencing the runtime ruling
  waits for OD-1.
- Tier-0: residual row recording D-T0-23's partial supersession by PEC PRD v2.1; coupling
  row for event-contract home / daemon event feed / auth-token reuse (D-T0-19 precedent);
  D-T0-07 ruling on the flow-a contract version identity (bump-and-repin or recorded
  carry-forward).
- pec.yaml interim demotion (demote grant-bearing fields or SUPERSEDED_PENDING_V2), with
  the challenge-narrowed urgency in view; full supersession remains deferred to v2 shape.
- Notice the stale RB-PEC-ADAPTER row to PEC; PEC open-issue annotation naming the external
  owner of PEC-K-03/K-11 consumer-side obligations; notice Piping on D-30; each derivative
  source manifest reconciled or explicitly suspended by its own loop.

### OD-6 — Method-layer tranche (deliberately separate and later)
*Sources: RM slate 4/7/8; PEC D8/D9; codex FAN-012 smallest-action. Crosswalk X-15, X-16, X-24, X-40.*

Decide as one D-GOV-16/M2 package, **after** the architecture tranches land: optional
`interfaces:`/`consumers:` SOW element (the structural fix behind the runtime cluster;
in-corpus shape precedent: the D-APP-48 `boundaries` object); machine-readable
`acceptance_status:`/`claim_status:` field; validator observation-boundary declaration
convention; whether a forward-coverage register becomes a required decomposition output
(then App builds its FR/NFR companion register: 8 unowned FRs, 43 multi-owned, 23 untraced
NFRs → coverage-or-deferral each). Separately judge App's acceptance-criteria posture
(conversion-fidelity pattern; 0/53 in-contract human gates): deliberate rebaseline
consequence or defect — noting the method-era UNKNOWN. **REC:** treat as reform, not repair;
none of it blocks OD-1..OD-5.

### OD-7 — Evidence retention and meta hygiene (immediate; no judgment content)
*Sources: all three handoffs; meta-review §11. Crosswalk X-33, X-42, X-43, X-44.*

Adopt the retention list (three complete packages + both meta-analyses, byte-exact with
hashes); **relocate the two at-risk packages** (Root-managed out of session scratchpad;
codex out of the prunable worktree) into the durable evaluation area when assembling the
program-level package; record the corrected disclosures (X-33's one-active-pin fact; X-19's
deepened notice defect) so future review manifests do not re-propagate them; record the
shared-blind-spot register as explicit non-coverage.

## Sequencing

```
now (parallel, no judgment dependency):
  OD-7 retention/relocation ..... OD-3 six-pin repair ..... OD-4 mechanical Root repairs
  OD-5 overdue-notice shipment (content-independent part)

gate 1:  OD-1 runtime boundary + route (+ severity convention, + consumption census)
           |
gate 2:  OD-2 App boundary SCOPE_CHANGE (repin/rescope targets now determinate)
           |               \
           |                OD-5 remainder (Tier-0 rows, ruling-dependent notices)
           |
closeout: OD-3 remainder (single-pin at SCA-APP-004 closeout; provenance ruling;
          register create-or-defer)
           |
later:   OD-6 method tranche (separate instrument)
           |
then:    resume App UI/API semantic-parity planning ONLY against the corrected
         boundary, via its own future instrument (none exists today)
```

**Rerun posture** (all three packages agree; adopt as-is): preserve the frozen packages;
after each accepted change, update the manifest to the new accepted bytes and rerun only the
affected trace/boundary rows — never the whole review by default.

## What must NOT ride these tranches

Semantic parity, application environment profiles, the reusable work surface, and resource
governance stay outside accepted scope (all three reviews and this meta-review concur);
PEC and resource governance remain optional; no severity is averaged; no candidate enters
through SOW or decomposition prose. The held-open questions (work-surface ownership, PEC
availability thresholds, bundling-vs-composition + degraded mode, resource-governance
contract) remain owner-held with alternatives preserved in the source reports.
