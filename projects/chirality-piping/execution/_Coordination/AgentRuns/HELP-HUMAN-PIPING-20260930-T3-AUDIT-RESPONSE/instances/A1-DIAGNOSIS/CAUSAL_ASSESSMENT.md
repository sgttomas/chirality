# A1 preparation causal assessment

The matrix is unchanged. These are source inspection and exact-arithmetic
findings, not selected-solver observations. The universal transfer proof gap
confirmed by V0 remains open; no repair is selected.

The independent oracle derives the scalar and two-by-two equilibria directly
from the sealed matrix. `matrix.json` preserves all 24 sources, separate load
IDs/bits, 880 exact truth rows, and nearest-binary64 truth bits. Truth is stored
as the exact signed integer `n` times `2^e`. These are mathematical expected
values, not assertions that the candidate or verification equals truth. All
optional collections are empty; zero load contributions are omitted, while
every prescribed displacement is explicit positive zero.

The B sources have scalar free stiffness 4. Both node displacement magnitudes,
all twelve end-action components and every restrained reaction are included.
B15/B16 have a nonzero exact driver `h/2`, whose nearest binary64 value is zero:
the oracle calls this underflow, never a published-zero witness. B09/B10's
coupled zero scale alone makes no false-truth claim.

For C, the determinant is `ak > 0`, the energy is
`a(u_g-u_j)^2+k*u_g^2`, and truth is
`u_g=q+t/k`, `u_j=q+t/k-F/a`, `r_1x=5h/4`.
Exact equilibrium checks cover every free DOF. The spring action is `-k*u_g`;
member end actions follow the node-on-element sign convention; constrained
reactions include the root torsional reaction. Magnitudes are absolute axial
translations, so their oracle values require no irrational approximation.

The pure projection checks independently confirm that C17–C24's grounded
ledger rounds at p=128 to `F+kq`, and at P=256 to `F+kq+t`.
This is a projection fact only. The exact ledger has not lost its tail.
For C22 the ground truth is `9*2^-1241 > 0`, retained exactly in the oracle.
C23's two exact relative ratios exceed `1/10^9` as the derivation states.

The full 12-by-12 member structural block makes the C free pattern a clique
on global indices `[0,6,9]`, even though the torsion is numerically decoupled.
The deterministic degree/index choices give traversal `[0,1,2]`, reversed to
`[2,1,0]`. Thus the derived elimination order is global `[9,6,0]`.
Ground placement C21 changes which axial diagonal goes first; it does not
change the structural order. The public RCM helper in the inert probe can
later observe the order on this independently constructed pattern. It is not
a private-factor observation.

For C17–C20 the derived radix factors are `2^-38` on axial DOFs and `2^-1`
on Rx. With `kappa=2^-109`, the favorable order has exact pivots `1,kappa`.
The exact proposed last-pivot inequality
`kappa*(2^128-6) > 384*(2+kappa)` passes. The proposed zero grounded candidate
also satisfies the coalesced residual inequality
`9h*(2^128-4) <= 256*(2*2^-900+9h)`.
The source exits refinement when all coalesced rows pass, so unconditional
correction cannot be assumed. These checks support the causal hypothesis;
they do not run or duplicate the solver, condition estimator or refinement.
C21's different arithmetic order and any correction/escalation remain open.

Full selection remains the controlling uncertainty. An exact P-state does
not imply zero W-plus. Source `verify.rs:1113–1179` includes positive t1 from
the bounded operator applied to nonzero displacement, even if delta and both
residuals vanish. The source's certified B, bounded norms, upward arithmetic,
theta and g validity cannot be replaced by the exact two-by-two inverse norm.
Force/moment estimate and charge, all layout rows, E/hat encoding, O9 eligibility
and any p=512 floor must also pass. C19's hypothesized disagreement consumes
the full allowance before the positive W-plus and magnitude charge; rejection
at p=128 is an expected competing outcome, not a failed experiment to suppress.
C17/C18/C22/C23 require actual remaining room, not an assumption that t1 is zero.

No correction to the sealed matrix is currently warranted by this preparation.
The strongest live alternatives are source/geometry refusal, condition or
pivot escalation, a different candidate/refinement path, W-plus disagreement
rejection, force/moment charge or estimate rejection, and receipt encoding.
Any one can invalidate a proposed C mechanism without repairing the universal
proof gap. The public evidence exposes reasons/summaries and opaque encodings;
per-row W-plus/t1/t3 and both full retained states remain unavailable through
ordinary public accessors. A selected false claim could still be established
by complete public output plus independent exact truth.

The downstream inventory retains stop (a), charge (d), floors, absolute and
relative classification, D2 G5b/G5c and receipt checks. Per ROOT's message
through DESIGN, R7 §6.3 lines 839–840 also relies on the converted published
translation scale being relatively within `2^-50` of the retained scale to
derive G5a's lower bound. This is a shared proof dependency, not evidence that
the lower-bound check itself has failed. No D2/F2a reliance or repair is granted.

B01–B16 remain the first future tranche. Return their source/API limitations,
full results and derivation reassessment before any C17–C24 admission. A realized
false claim stops the activated tranche immediately; unrun cases stay unrun.
