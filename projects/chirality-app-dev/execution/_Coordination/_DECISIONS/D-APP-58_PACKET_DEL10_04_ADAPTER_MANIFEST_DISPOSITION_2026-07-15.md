# D-APP-58 — DEL-10-04 Adapter-Manifest Requirement Disposition

**Status:** PROPOSAL — AWAITING_RULING

**Date prepared:** 2026-07-15

**Prepared by:** app-dev loop operator under the D-APP-53 deliverable-local
work-surface protocol

## Decision statement

Decide how DEL-10-04 should carry the still-unassigned deterministic
domain-engine adapter-manifest location in DEP-10-04-007. The decision must
preserve the current staged domain boundary and must not invent a manifest
path, schema, or implementation authority from partial test evidence.

This packet creates no manifest, schema, runtime behavior, domain-engine
binding, protected-path write, or lifecycle transition. It is a candidate
gateway under K-AUTH-1 and F-APP-3; only the owner may rule.

## Governing basis and evaluated evidence

- `docs/CONTRACT.md`: K-AUTH-1 keeps adoption and direction with the owner;
  K-DOMAIN-2 and K-DOMAIN-3 preserve the domain-engine write and apply gates;
  K-CLAIM-1 forbids promoting a proposal or gap into accepted truth.
- `docs/SPEC.md` §18 says future profiles must define deterministic adapter
  manifests, but it does not assign their location or schema.
- D-APP-50 authorizes only the ruled staged MCP tool surface and expressly
  excludes tier-0 authoring, apply exposure, piping writes, and live-binding
  claims.
- The app-dev standing workplan F-APP-3 stops this loop from advancing the
  domain-engine boundary beyond tier-0 bridge authority.
- DEL-10-04 `ScopeOfWork.md` records that a human-approved PKG-10 amendment or
  explicit authorization must identify the ResponsibleParty, concrete test
  path, adapter-manifest location, evidence format, and expected-failure
  fixtures before implementation work becomes executable.
- DEP-10-04-007 remains `PENDING`: four concrete app-side test paths exist,
  but no accepted source assigns a domain-engine adapter-manifest location.
  The inspected `projects/chirality-piping/_harness/adapter.yaml` is a
  practitioner-harness configuration, not the missing manifest.
- DEP-10-04-008 is already `SATISFIED` under D-APP-56 R5 P45 against accepted
  snapshot `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`; that separate
  stale status item is repaired in the packet-preparation tranche.

## Requirements and objectives

R1. Preserve the unassigned location as a gap unless an owner act supplies or
authorizes its governing basis.

R2. Do not treat existing tests, profiles, tool descriptors, or the piping
practitioner-harness adapter as a domain-engine manifest by analogy.

R3. Keep any future work inside the app-dev write fence unless a ruling grants
a specific wider scope; no `_DomainEngines/**` or piping write is implied.

R4. Preserve D-APP-50 exclusions: no apply exposure, protected-path write,
live binding, L3 claim, or professional/release claim.

Objective: make the next lawful state of DEP-10-04-007 explicit without
silently designing or activating a future domain contract.

## Options

### O-A — Defer under the existing future-amendment gate (recommended)

Keep DEP-10-04-007 `ACTIVE / PENDING`. Replace the currently ungated
deliverable-local instruction to assign a location now with an explicit gate
to a future owner-approved PKG-10 amendment or other owner authorization that
names the location and governing schema basis.

**Tradeoff:** preserves truthful uncertainty and the smallest live surface,
but the future fixture cannot claim implementation-quality manifest
validation until the owner later activates the amendment.

### O-B — Authorize a bounded app-side contract-design tranche

Authorize a design-only tranche inside `projects/chirality-app-dev/**` to
derive candidate manifest location/schema options from accepted tier-0 and
app authority, then return a separate owner gateway before any implementation
or dependency-row closure. No domain-engine or piping write is included.

**Tradeoff:** advances the design evidence while retaining the implementation
gate, but adds work before a concrete domain-engine activation need is ruled.

### O-C — Retire or replace DEP-10-04-007 for the current staged boundary

Authorize dependency reconciliation to retire the combined test-path and
manifest-location prerequisite, or replace it with a narrower prerequisite
that applies only when a future PKG-10 implementation tranche is activated.

**Tradeoff:** removes a premature current dependency, but changes the
deliverable's accepted dependency model and needs an explicit recorded basis.

## Evaluation and non-binding recommendation

The four test paths satisfy only half of the combined prerequisite. No
accepted source currently supplies a manifest location, and choosing one
would shape the future domain contract across the F-APP-3 boundary. Current
runtime readiness does not require that choice because DEL-10-04 remains a
future-boundary deliverable and its activation authority is still gated.

Recommend O-A. It accurately preserves the gap, prevents the item from being
reselected as ordinary agent work, and defers design cost until the owner
activates a concrete PKG-10 need. The recommendation is non-binding.

## Validation criteria before continuation

Any continuation is valid only when:

1. the owner selection is recorded in a D-APP-58 ruling file and the register
   row is changed to `RULED` without broader attribution;
2. DEP-10-04-007 remains pending unless the selected option supplies a cited
   accepted basis for a different status;
3. any new location or schema is traced to accepted sources and is not inferred
   from the practitioner-harness adapter or test paths alone;
4. writes remain within the ruled scope and F-APP-3/D-APP-50 exclusions pass;
5. DEL-10-04 stays `IN_PROGRESS`; and
6. dependency validation, practitioner self-check, receipt validation, and
   documentation-only closeout checks pass.

## On-ruling mechanism

- **O-A:** record the ruling, keep DEP-10-04-007 pending, replace the D-APP-58
  gate with the ruled future-amendment gate, validate, and close through a PR.
- **O-B:** record the ruling, execute only the bounded app-side design tranche,
  return its candidate choices to the owner, and make no manifest/runtime or
  dependency-satisfaction claim.
- **O-C:** record the ruling, reconcile DEP-10-04-007 and its markdown/status
  mirrors against the exact ruled replacement basis, then validate and close
  through a PR.
