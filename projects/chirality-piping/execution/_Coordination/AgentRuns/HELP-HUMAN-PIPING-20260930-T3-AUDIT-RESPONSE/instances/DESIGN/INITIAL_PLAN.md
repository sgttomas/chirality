# DESIGN initial checkpoint — AUD-T3-01

Status: proposed diagnosis route, 2026-09-30. No experiment, repair, design
amendment or acceptance is reported. ROOT's separate AUDIT-REVIEW may confirm,
narrow or refute the audit. This packet is an ad hoc execution plan, not a
reusable workflow.

Aliases: `P = projects/chirality-piping`; `FK = P/core/solver/frame_kernel`;
`Run = P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`;
`T3 = P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3`.
Paths are relative to the Git-derived repository root.

## Question and current evidence

For a source accepted by `PrimitiveSource`, which passes the full retained
selection procedure at p, does every published row satisfy its selected
accuracy claim when the claim uses the scale reconstructed from the published
binary64 rows? In particular, can the verification-to-publication transfer be
proved for both L and 1/L coupling when an included raw row is subnormal,
including a coupled published scale of zero and the 2^-988 A1 boundary?

The distinct objects must stay explicit:

1. `q_p`, `q_P`, P = 2p, and independent model truth `q*`;
2. raw maxima over the same eligible rows at P and after candidate publication;
3. the P-bit coupled verification scale `S_v`, and the binary64 coupled and
   possibly floored publication scale `S_pub`;
4. the row class, its exact published bound bits, and its allowed qualification.

Source inspection agrees with the audit's causal trace: `adaptive.rs:1904–1949`
forms `S_v` from verification values, excluding input-derived rows and rows
whose candidate cannot publish; `:2051–2060` establishes that candidate mask.
`:2598–2658` instead takes maxima of already published candidate rows, then
uses `coupled_scales` (`:296`). `row_bound` (`:380`) adds the A1 terms only for
0 < S_pub < 2^-988 and returns zero at S_pub = 0. A1's direct row-rounding
allowance does not, by itself, account for rounding a different raw row before
L multiplication or division.

For an eligible row set and exact positive L, write raw maxima as a and b and
their approximations as a_hat and b_hat. The elementary stability obligations
include

    |max(a,L b) - max(a_hat,L b_hat)| <= max(|a-a_hat|, L|b-b_hat|)
    |max(b,a/L) - max(b_hat,a_hat/L)| <= max(|b-b_hat|, |a-a_hat|/L).

The full proof must additionally charge candidate/verification disagreement,
P-bit coupling, binary64 coupling, max-branch changes and any shared ceiling
floor. An absolute raw rounding allowance therefore has the raw quantity's
unit before L or 1/L conversion. A unitless common half-subnormal allowance
cannot simply be copied across all kinds. These inequalities identify proof
obligations; they are not a selected bound formula or a completed proof.

R7 §5.2 asserts the relative scale-transfer premise; RV19's D.4 adds one
half-subnormal absolute term. The audit's r = (5/4)2^-1074 with L = 2^100
algebraically contradicts that general assertion. This checkpoint has read
that derivation, but has neither independently executed it nor established
that a selected source realizes a wrong row claim. AUDIT-REVIEW owns the fresh
independent judgment on the audit.

ROOT additionally requested an explicit trace of relative classification and
the downstream 1e-9 assurance. That path is implicated at the proof level as
well: classification uses `|q_pub| >= fl(2^-34 S_pub)` when S_pub >= 2^-988,
whereas the retained allowance can use S_v. At the threshold, the leading
relative bound is `2^-30 (S_v/S_pub)`, before the existing rounding/charge
terms. A 5/4 scale ratio exceeds the roughly 7% margin for which the pinned
2^-34 threshold was chosen (`DESIGN_NUMERICS/DESIGN.md:424–446`).

A concrete abstract check for the future independent oracle is to keep the
audit's rotation and L=2^100, set candidate translation q=2^-1008, and set
verification/truth to q+d with d=(9/8)2^-1038 and zero verification error.
Then S_pub=2^-974 and S_v=(5/4)2^-974 remain dominated by the rotation coupling;
q is exactly the published relative threshold. The abstract disagreement
d < 2^-64 S_v passes, while d/q = 9/(8·2^30) > 10^-9, and also
d/(q+d) = 9/(8·2^30+9) > 10^-9. This is a hand-derived logical counterexample
to transferring that allowance, not an executed arithmetic test or a source
whose candidate and verification states have been realized. It requires
independent checking and does not establish a new reachable relative failure.
The diagnosis must therefore retain absolute-bound, class-transition and
relative-assurance questions separately.

## Strongest competing explanations

The strongest defense is an enforced source/selection invariant, or a direct
per-row argument, that excludes harmful scale-transfer states from the actual
guaranteed domain. The audit's independently assigned candidate and truth need
not be jointly realizable by the unmutated formation, solve and verification
steps. A selected real model may have exact candidate values or enough unused
error allowance that its published claims remain honest despite a large scale
ratio error. Thus a reachable scale gap alone is not a solver defect.

Check specifically whether another same-kind row dominates the raw maximum,
input-derived exclusion removes the proposed driver, O9 makes the candidate
unpublishable, verification rejects the source, or a force/moment ceiling floor
dominates both scales. A proof of one of these facts for one fixture narrows
that fixture only. A universal exclusion must cover every admitted source and
both coupling directions, not just the current controls.

The existing product's capture range is another possible domain exclusion,
but cannot alone discharge a retained-kernel guarantee: `PrimitiveSource::new`
accepts finite coordinates without that numeric limit, and F2a is a future
integration gate. Source reach, current product reach and intended F2a reach
must be reported separately. A newly imposed range guard is a proposed domain
change, not evidence of a pre-existing exclusion. Likewise, the audit's zero
scale example proves a scale effect; it does not prove nonzero truth behind a
published zero.

## Bounded route

1. Incorporate V0's independent disposition before sealing A1-DIAGNOSIS. If V0
   refutes the finding, assess its exact scope before commissioning probes.
   If it narrows it, reduce the brief accordingly. Preserve disagreements for
   DESIGN-VERIFY rather than assuming either author is correct.
2. Use hand-derived exact rational one-member controls to target the scale
   premise. A straight axis-aligned member with exactly one free torsional or
   axial DOF gives a one-by-one free stiffness and an independent oracle.
   The draft brief gives concrete starting constructions and their limits.
3. After E0 and ROOT's separate heavy-slot grant, execute these through the
   unmutated public retained API. Classify validation refusal, selection
   refusal, reachable scale gap and wrong published claim separately. Keep
   the first matrix under 24 cases, at one to three members; no scale search.
4. Only if needed, design a tiny two-free-DOF or two-member cancellation case
   whose exact solution tests an absolute row near the accepted disagreement
   limit. A seeded or substituted internal state is an algebra diagnostic,
   never a realized-source witness. Stop and return rather than widening into
   a large-model search when these bounded cases do not settle the question.
5. DESIGN develops closure from the returned evidence: a complete enforced
   exclusion/direct proof, or a proposed change to scale transfer, bound,
   encoding or guard. No option is selected now. Freeze the proposal for
   independent DESIGN-VERIFY, then ROOT's D1 decision and any human-reserved
   consequence. DELIVERY owns any separately briefed implementation.

The outcome taxonomy is: audit premise refuted/narrowed; proof gap confirmed
without realized scale witness; selected source with scale gap but honest rows;
selected source with wrong claim (BLOCKING); or bounded investigation remains
inconclusive. Failure to find a bad case does not establish a universal proof.

## D2, F2a and K6c consequences

| Surface | Required consequence assessment before closure |
|---|---|
| D2 G5b | It currently recomputes S* bit for bit from raw publication and section terms. An outward verification-scale receipt would require a precisely specified new evidence relation and reader checks; it cannot silently replace this equality. |
| D2 G5c | Exact class/list equality and bound-bit checks must adopt A1 and any further selected formula, including the zero-scale and 2^-988 cases. Retain input-derived and unpublishable distinctions. |
| Relative row reliance | A smaller S_pub can lower the 2^-34 threshold and label a row relative_verified. Trace the full 1e-9 argument and covered derived-stress propagation before treating a bound-only change as sufficient; preserve the pinned threshold and protected criterion unless their owner changes them. |
| D2 G5a / receipt | Any extra coupling allowance, scale evidence, refusal or calculation work needs a closed field/encoding/check specification and parity in Rust, Python and TS. A receipt of a larger number alone is not evidence that the number is trustworthy. |
| D2 S-I | Reconcile the row-bound meaning, R7's factors (1 + 2^-22, or 1 + 2^-21 at p=512), endpoint rounding, unit conversion and the b=0 exact-point rule. State the precise assurance inherited by interval binding. Do not silently describe the nominal [q-b,q+b] interval as an exact forward-error enclosure beyond the accepted qualification. |
| D2 historical design text | Its plain-b and operational-convergence descriptions predate the routed A1/R7 consequences. Prepare an additive consequence account; do not rewrite hash-bound DESIGN.md or treat its older wording as superseding later rulings. |
| F2a / S-G1 | Keep their assurance gate open pending independently verified closure and W1 limits. Product capture restrictions, receipt failures and row standing require explicit mapping; no F2a implementation is in this response. |
| K6c | Any retained scale/bound implementation delta must disclose new allocations, work counters, cached state and refusal paths. DELIVERY must cover the final A1 behavior in the phase model or obtain a checked no-impact argument before final measurements. |

Force/moment coupling has the same raw-rounding question as translation/rotation;
stress scales add A/Z and unit/factor operations. Diagnosis can start with the
one-DOF displacement witnesses, but a closure proof must inventory all dependent
kind/scale uses before claiming completeness. A2 remains a separate certified-
bound availability argument; this plan neither reopens it without evidence nor
uses it to discharge A1.

## Decision ownership and next condition

ROOT owns V0 disposition, source/brief sealing, slots and host admission,
integration, and routine in-scope execution choices. DESIGN owns proposal
coherence; it cannot approve its own proof. DESIGN-VERIFY independently checks
the frozen proposal. The human decides any narrowing of the guaranteed domain,
change of published contract/standing or protected criterion, scope expansion,
or unresolved ownership consequence. Those decisions need a concrete verified
proposal; no such decision is requested at this checkpoint.

To launch the draft child, ROOT must supply the V0 result and exact launch basis,
grant a TASK slot, and state its permitted scratch/target locations. Rust runs
additionally need the E0 host/protection record and a heavy-slot grant. This
checkpoint ends with the draft ready for that sealing step.
