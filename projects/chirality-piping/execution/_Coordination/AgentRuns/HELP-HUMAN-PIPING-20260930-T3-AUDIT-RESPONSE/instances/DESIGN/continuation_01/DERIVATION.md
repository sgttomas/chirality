# A0 continuation derivation and competing exclusions

Status: DESIGN's hand derivation against source base
`3bddc2b05f6106e969c7cf43373b230845c7cc66`. No numeric script, source probe,
build or model has been run. This proposes discriminating sources; it does not
prove that the complete implementation selects them. Independent checking and
an unmutated public-API witness remain prerequisites to a solver-defect claim.
Aliases and fixture definitions are in `A0_BRIEF.md` and `CASE_MATRIX.md`.

## What V0 establishes, and what it leaves stipulated

V0 (`Run/instances/AUDIT-REVIEW/REVIEW.md`, SHA256
`13a0dc689fc47ec26af93e3b4624f281a4c88345209c2653f79161b593f1befc`)
confirms the proof defect and qualifies reachability. It independently checks
the 20% scale loss, the abstract 9/8 claim ratio, both coupling directions,
the A1 boundary and the magnitude-row extra charge. It does not realize the
source-derived residual, t1/t3, W-plus, theta/g, force/moment estimate/charge,
refinement, positive-definiteness and encoding conditions together.

In particular, exact verification truth does **not** imply the implementation
returns W-plus=0. The following construction aims to leave quantitative slack
for a positive W-plus; its amount must be checked rather than stipulated away.

## Exact source equations

The C family has one straight member, two free axial translations, one axial
spring to ground and one independent free tip torsion. The remaining DOFs are
zero constrained. `assemble.rs:281–295` forms a=EA/L and torsion GJ/L=4.
Writing q=0 initially and g=0, the axial equations are

    (a+k)u0 - a u1 = F+t
         -a u0 + a u1 = -F.

Their sum gives ku0=t. Thus `u0=t/k`, `u1=t/k-F/a`; the independent torsion
is `r=5h/4`. The symmetric axial block is positive definite since a,k>0 and
its determinant is ak. Its energy is `a(u0-u1)^2 + k u0^2`. No nonzero
prescription creates the tiny free rotation, so it is not input-derived.

For C17: a=2^76, k=2^-33, F=2^-900, t=9h. Let B=F/a=2^-976 and
d=t/k=9·2^-1041=(9/8)2^-1038. The exact state is `(d,d-B,5h/4)`.
The proposed p=128 state is `(0,-B,5h/4)`, while P=256 can retain the full
dyadic exact solution. These state predictions are derived below and remain
subject to runtime verification.

## Ledger, order and factor: why the proposed loss is specific

The exact ledger retains every authored term (`ledger.rs:1–13,91–125`).
`reduced_rhs` (`assemble.rs:818–850`) adds that ledger exactly and rounds once
at the current p. For C17, the 9h tail is much smaller than half an ulp of F
at p=128, but F+9h fits at P=256. This is a loss at the prescribed RHS
projection, not a false claim that the exact ledger itself discarded the tail.

Ordering is consequential. `Structure::new` inserts the member's full 12×12
structural block (`assemble.rs:545–569`), including numerical zeros.
The three free DOFs have global indices `[0,6,9]`; their structural adjacency
is a clique. The current deterministic RCM (`factor.rs:224–397`) starts at
free index 0, visits 1 then 2, and reverses to `[2,1,0]`: tip Rx, ungrounded
Ux, grounded Ux. The first torsional row decouples arithmetically. The axial
elimination therefore pivots on a before a+k. Moving the ground to node 1 in
C21 deliberately reverses this advantage without changing the physical
two-by-two equations under their (grounded, ungrounded) labels.

Radix scaling for C17 is 2^-38 at each axial DOF and 2^-1 at Rx
(`factor.rs:519–528`; `wide.rs:341–345` defines the leading-bit exponent).
The scaled axial block is `[[1+κ,-1],[-1,1]]`, κ=k/a=2^-109, in original
axial order. With the ungrounded row first its pivots are 1 and κ and its
off-diagonal factor is -1. All are exactly representable at p=128, as is
1+κ. The scaled loads +F and -F can therefore cancel exactly in the final
forward-substitution row, giving candidate u0=0. At P=256 the retained tail
survives that subtraction and yields d. The solve loops are `factor.rs:630–675`.

The p=128 last-pivot screen has m=6 under this full profile, cancellation
scale 2+κ and pivot κ. Its inequality is

    κ(2^128-6) > 384(2+κ),

whose left side is almost 2^19 while the right is approximately 768. This
particular pivot screen does not exclude the proposed state. The true scaled
inverse has norm 2/κ+1 and matrix norm 2+κ, giving true 1-norm condition
approximately 2^111, below the screen's 2^127 boundary. The implementation
uses its own finite-precision condition estimate, not this substituted exact
norm; its recorded screen result must still be checked (`factor.rs:700–811`).

## Why refinement need not repair the tail

`residual_rows` uses the exact ledger and the re-formed operator. It checks
`|r|(2^p-m) <= 64m D`, where D is the coalesced absolute denominator
(`adaptive.rs:1413–1484`). For the proposed C17 candidate, the grounded row
has residual t=9h and denominator 2F+t; only one nonzero Kij uj term enters
its count, so m=4. Hence the candidate gate compares

    9h(2^128-4) <= 256(2·2^-900+9h).

There is a large margin: the tail is roughly 2^-171 of F. The other axial
row and torsion have exact-zero residuals under the derived state. The loop
exits before computing a correction when every row passes
(`adaptive.rs:1755–1758`); corrections are not unconditional. If the runtime
instead records correction/refusal, the derived state or gate calculation
must be revised. The bounded fallback is reached only after failed gate and
stalled/exhausted corrections; it is not assumed active for this case.

## The publication claim that would be tested

If the derived p/P pair survives every other gate, the rotation remains a
publishable h while the raw axial maximum is below the rotation coupling.
The verification translation scale is `(5/4)2^-974=5B`; publication gives
`S_pub=2^-974=4B`. Candidate node 0 Ux and its displacement magnitude are
exact zero and publish zero with plain b=2^-1038. The exact error is 9b/8,
which exceeds the accepted b(1+2^-22) factor at p=128.

The retained difference d consumes 9/10 of `2^-64 S_v`. The remaining room
is 2^-1041, and must contain the **actual positive W-plus** and, for the
magnitude row, `2^(1-P)|q_P|`. V0 already shows the abstract magnitude term
alone is small; it does not bound the full source-derived W-plus here.

C18 puts the exact error at b; C20 removes the tail entirely. C19 puts the
disagreement exactly at `2^-64 S_v`; any positive W-plus or magnitude term
then rejects p=128 under the derived states. Escalation is an admissible
observed result, not a test failure to suppress.

## Verification conditions still to discharge

`verify.rs:831–858` recomputes the residual from exact ledger and q_W=448
contributions for P=256, and solves for its correction. Even if that residual
and correction are exactly zero, `:1113–1179` includes t1 in W-plus:

    N_u = ||S A_bar |u0||| + 2 B_c ||S A_bar S|| ||S r||
    t1 = 2^(7-q_W) B_c N_u
    t3 = 3 B_c ||S r2||
    W_plus_i = |delta_i| + s_i(t1+t3).

Nonzero displacement means the first term of N_u need not vanish. A2 must
form an available certified B_c; the true inverse norm cannot substitute
for the implementation's possibly larger certificate. The actual theta is
`2^(7-P) B_c ||S A_bar S||` and must be <=1/2. Axis alignment suggests g=1,
but geometry and the recorded g-validity result remain checks.

Force/moment rows also need their V, verification estimate and charge tests.
Here large opposing axial loads create force-scale and reaction data even
though target u0 is tiny. Receipt E values and their coupled hats must remain
encodable. `adaptive.rs:2105–2250` applies these checks to the entire layout,
including rows that the publication filter omits. No row may be ignored to
make a target-only argument pass. Do not assume B, E, W-plus or charge equal
a hand estimate simply because the one-dimensional exact solve is simple.

The public API exposes selection, row/bound bits, attempt reasons, correction
counts, residual summaries, B/theta/g summaries and E/estimate/charge summaries.
It deliberately does not expose PrecisionState or per-row W-plus/t1/t3
(`structural.rs:5–35`, `adaptive.rs:2326–2374,2713–2736`). A selected
unmutated result plus an independent exact truth can prove a false claim
without a private-state dump. A claimed internal mechanism beyond those
observables remains a derivation until separately instrumented with authority.

## Zero-scale and relative-threshold extensions

C22 uses L=2^-100, a=2^276 and k=2^167, retaining κ=2^-109 and the same
loads. Then B=2^-1176 and d=9·2^-1241. The nonzero candidate ungrounded
translation rounds to zero as **unpublishable** and is excluded from scale
maxima. The target candidate remains exact zero and publishable; its retained
truth is nonzero. The rotation coupling gives positive S_v but zero S_pub.
This would test a b=0 false claim if selection and the proposed candidate
are observed. It must not be replaced by a binary64-zero oracle.

C23 uses F=2^-920, a=2^56, k=2^-33 and q=2^-1008, with a separate kq load
of 2^-1041 and the same 9h tail. F+kq fits in 128 significant bits; adding
9h is below its half-ulp and is lost there, but retained at P=256. The
predicted candidate target is q, exactly the published relative threshold;
truth is q+d. The raw maximum remains below the torsional coupled scale.
The error ratios are exactly

    d/q = 9/(8·2^30) > 10^-9,
    d/(q+d) = 9/(8·2^30+9) > 10^-9.

This is a proposed source realizing the earlier synthetic relative example,
not a realized result. The same full gates and positive W-plus requirement
apply. C24 removes the tail and supplies an honest threshold control. The
protected 2^-34 threshold and 1e-9 criterion remain unchanged.

No repair is selected. A failed construction narrows reachability only; the
confirmed universal proof gap remains open until a complete transfer proof,
enforced exclusion or independently selected amendment closes it.
