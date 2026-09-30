# A1 closure alternatives — conditional design draft

Status: reviewable alternatives and proof obligations only. ROOT authorized
lightweight drafting while the guard is repaired. No alternative is selected,
no new case is proposed or run, and no source, protected constant, criterion,
old ruling or sealed packet is changed. Remaining A0 evidence, independent
design verification and the owning decision still precede implementation.

Aliases: `P=projects/chirality-piping`; `FK=P/core/solver/frame_kernel`;
`Run=P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`;
`T3=P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3`;
`R7=T3/DESIGN_NUMERICS/REV_5A3_CANDIDATE/D1_REV_5A3_SSTAR_RESOLUTION_R7.md`.
All source loci below are at numerical basis
`3bddc2b05f6106e969c7cf43373b230845c7cc66`, unchanged in the inspected checkout.

## Evidence and question

V0 confirms the general scale-transfer proof defect. B01 is a clean selected
source with exact scalar rotation 5h/4 published as h and coupled translation
scale 2^-974, with all 37 row claims honest. Exact mechanics predicts the
5/4 retained-to-published scale ratio; the public API does not separately
expose that retained scale. B02's complete output has 37 honest forensic rows
and p128 rejection at a force-row stop check before p256 selection, but its
guard failed. It remains guard-failed. B03–B16 and all C cases are unrun at
this draft's basis. There is no realized false-claim witness yet.

The question is whether the publication guarantee can be derived directly
from the acceptance allowance, without asserting relative closeness of a
retained coupled scale to one made from rounded rows. The proposal space is
to give each covered row an acceptance budget X bounded by the **same finite
scale S used for that row's eventual publication**, and use X consistently
where the p512 formation charge depends on the acceptance magnitude.

## Definitions and unchanged instruments

Here "covered row" means a quantity in the retained kernel layout. Covered
derived product rows require the separate propagation check in
`PROOF_OBLIGATIONS.md` §5. For a non-input-derived kernel row with a finite
binary64 publication:

- x=q_p is the retained candidate, v=q_P is verification, P=2p, and y is the
  actual published binary64 value. All quantities/scales must share canonical
  units. A nonzero x rounding to zero is unpublishable, not y=0.
- S0 is the existing scale reconstructed from candidate publication values:
  eligible raw maxima, then the pinned binary64 L or 1/L coupling order,
  then the existing shared force/moment Phi floor only at p=512.
- Sv is today's verification scale, including that same Phi where applicable;
  M0_i=max(|v_i|,Sv_kind) is today's row magnitude.
- epsilon=2^-64; R=2^-34; u=2^-53; h=2^-1074; Q=2^-988.
  The existing b rule and A1 per-row small-scale bound remain unchanged in
  the alternatives below except where a changed *scale definition* is itself
  explicitly proposed as a contract alternative.

Retain the existing numerator D_i=|x_i-v_i|+V_i, including W-plus for free
displacements/rotations and the magnitude-row extra charge. Retain all of
R7's estimate, certified-bound, theta, g and formation-error premises, with
the `(1+2^-P)` term intact. Retain lambda, all charge constants, p schedule,
Phi exponent, branch thresholds, publication factors and the 1e-9 criterion.
There is no KF3-B1 lambda split or dense-screen decision in this draft.

## Alternatives

| Alternative | Covered-row stopping/charge budget | Published scale | Distinguishing consequence |
|---|---|---|---|
| P — candidate publication scale | X_i=S0_kind | S=S0, existing bits/formula | Direct proof, no private/public scale transfer. S0 can exceed Sv after upward rounding, so the acceptance set is not proved to be a subset of today's set. |
| C — conservative cap on the old budget | X_i=min(M0_i,S0_kind), comparing lifted values exactly | S=S0, existing bits/formula | Direct proof plus a candidate-by-candidate subset argument for (a) and p512 (d). Requires both scale paths and may escalate or refuse additional cases. |
| U — one shared outward scale | X_i=Scommon_kind, with both decision and publication using those exact bits | S=Scommon, newly specified | Direct proof can hold, but publication-scale identity/class/bound behavior and D2's recomputation contract change. A private-derived common scale needs explicit evidence/reader policy. |

For P and C, change (a)'s right side to epsilon X_i and at p512 change (d)'s
allowance to 2^-86 X_i. Keep p128/256 (d) at 60·2^-P·e_hat, (b) unchanged,
and (c) unchanged. In C, X_i<=M0_i makes these two tests no looser for fixed
candidate/verification states. This does **not** prove unchanged precision,
work, downstream classes, retirement-gate coverage or usable availability.

For the covered eligibility set, `scales_at` includes |v_i| in its raw maximum,
so M0_i=Sv_kind. C can therefore use the body/kind common cap
`min(Sv_kind,S0_kind)` **after** each scale's coupling and shared floor, with
no per-row budget array. Both floored force/moment operands are at least Phi,
so their minimum preserves that lower floor. Reintroducing `max(|v_i|,cap)`
after taking this minimum would undo its intended publication cap.

C is also expressible as retaining today's (a)/(d) checks and adding a second
publication-cap check to each. That permits consideration of preserving the
old receipt summaries with their **old denominator meanings**, while the
additional selection guard is verified by producer/replay. Replacing the
summary denominators by X is a different contract choice. The selected design
must say which it does; two different meanings cannot silently share a field.

U needs a concrete scale rule before it is an implementable proposal. One
candidate rule is `Scommon=up64(max(Sv,S0))`, after applying the same Phi to
both operands. Its finite bits would be used identically in (a), ceiling (d),
classification, b and the receipt. It eliminates scale transfer by identity;
it does not establish that its magnitude is independently reconstructible
from public rows. Overflow/unencodability must have a named conservative
outcome. A public-only outward rule is a different U variant and must be
specified separately; adding a half-subnormal after coupling does not define
a correct pre-coupling error enclosure.

No ranking here selects an alternative. P trades the old retained scale for
the publication scale. C retains an additional old-acceptance restriction.
U changes what the public scale means. Their proof, availability, receipt and
resource consequences differ and must be compared on the selected design basis.

## Required edge behavior

1. **Both coupling directions and both kind pairs.** Form tr/ro and fo/mo
   in exactly the existing order from actual candidate-publication bits.
   The proof below needs X<=S, not a closeness estimate after multiplying or
   dividing a raw subnormal by L. Preserve the actual `extent==0` branch;
   do not silently replace it with a different geometric-domain rule.
2. **O9 and input-derived rows.** Only finite-valued, non-input-derived rows
   supply S0. Keep unpublishable rows in the existing numerical tests under
   their current M0 unless a separately proved change is selected; they
   do not gain a publication claim. Preserve input-derived custody and range
   behavior. Do not coerce an underflow/overflow outcome to a numeric zero.
3. **Zero S.** The covered-row budget is zero. An accepted row must then
   have the exact-zero candidate/truth consequences proved in
   `PROOF_OBLIGATIONS.md`; b=0 cannot be inferred merely from rounded coupling.
4. **Small S and relative rows.** Preserve Q, R and the current row-bound
   formula. The proof treats 0<S<Q separately and uses the published-value
   denominator for the relative claim. No larger comparison tolerance is added.
5. **Ceiling.** Compute the existing Phi from the same reported E/e_hat bits
   as today. Apply it to S before the covered-row acceptance budget is formed,
   and use that budget in ceiling charge (d). Changing only (a) is insufficient.
6. **Finite representation.** An infinite/NaN publication scale cannot be
   treated as an unlimited acceptance allowance. Preserve existing extent,
   E/hat, arithmetic and encoding refusals; identify any newly needed named
   scale-encoding path before claiming domain equivalence. Do not accidentally
   remove an implicit finite-extent check by eliminating `scales_at`.
7. **Publication identity.** An early tentative projection must produce the
   same eligible value, scale and Phi bits as final publication. Input-derived
   prescribed overrides are formed from exact sums in finalization and remain
   a separate obligation, especially for D2's lower bound. No hidden second
   rounding or final-unit conversion may change the value/scale being proved.

## Traps that do not constitute closure

- Increasing only b leaves the relative threshold and 1e-9 guarantee unresolved.
- Taking the minimum of raw scales **before** L/1/L coupling is not the stated
  cap on the final row magnitude; max/coupling/floor ordering must be explicit.
- Replacing Sv by S0 but retaining `max(|v|,S0)` does not establish X<=S0.
  It requires a separate self-consistency proof; at zero S0, relying on |v|
  can leave a positive budget. It is not interchangeable with P or C.
- Keeping p512 charge based on old M0 while tightening only stop (a) leaves
  the corollary's extra 2^-22 term on the wrong scale.
- A public scale field larger than a reconstructed minimum is not itself a
  certificate of an unpublished verification quantity.
- A passing finite case list, including B01, is not a universal proof. Failed
  C reproduction would not repair the already refuted general premise.

The direct kernel-row argument is in `PROOF_OBLIGATIONS.md`. D2/F2a, exact
source loci, work/allocation questions and decision ownership are in
`IMPACT_AND_DECISIONS.md`. None of these draft files activates implementation.
