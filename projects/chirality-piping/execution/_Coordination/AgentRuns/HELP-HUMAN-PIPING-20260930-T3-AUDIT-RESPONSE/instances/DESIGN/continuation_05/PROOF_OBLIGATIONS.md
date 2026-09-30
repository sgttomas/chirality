# Direct publication-budget argument and remaining proof obligations

This is DESIGN's hand derivation for review, not an independently verified or
accepted amendment. No arithmetic experiment or model run was performed for
this draft. Symbols and alternatives are defined in `A1_CLOSURE_OPTIONS.md`.
R7's standing formation, inverse-bound, theta/g, exact-ledger and recovery
premises remain assumptions of this argument; they are not reproved here.

## 1. A sufficient covered-row invariant

For each covered non-input-derived row that will publish a finite binary64
value y, establish a finite nonnegative acceptance budget X_i and publication
scale S such that

    X_i <= S,    |y| <= S,
    |x-v| + V_i <= epsilon X_i.

Keep the verification estimate and certified-bound conditions unchanged. For
force/moment rows retain the current charge allowance at p128/256, and use
`C_i <= 2^-86 X_i` at p512. The same X_i must feed both ceiling tests.

R7's theorem at lines 563–574 bounds the verification error independently of
the particular acceptance scale. Repeating its corollary with X_i substituted
for M_q gives:

- At p128/256, for force/moment:

      |x-q*| <= epsilon X_i
          - [256-69-64(1+2^-P)-60] 2^-P e_hat
        < epsilon X_i - 62·2^-P e_hat <= epsilon S.

- At p512, the unused positive resolution margin and the ceiling charge give

      |x-q*| <= epsilon X_i (1+2^-22) <= epsilon S (1+2^-22).

- Free translation/rotation use the existing certified W-plus in (a):
  `|x-q*| <= epsilon X_i <= epsilon S`. For displacement magnitudes retain
  the existing component-bound construction and the extra
  `2^(1-P)|q_P|` term in the numerator; their verification-bound premise must
  remain separately valid, rather than treating a magnitude as a free scalar.

Thus write `|x-q*| <= alpha epsilon S`, where alpha=1 except for the
force/moment ceiling case, for which alpha=1+2^-22. This does not compare S
with Sv and does not cancel a rounded pre-coupling error. It retains the
`(1+2^-P)` multiplier and does not choose a new lambda/residual split.

P and C satisfy X_i<=S by definition, with S=S0. U does so by using one
identical Scommon in both places, provided that scale is finite and includes
every eligible raw published magnitude. These are sufficient conditions;
they do not prove the algorithms' availability or final-publication identity.

## 2. Direct binary64 publication error

For round-to-nearest binary64 publication, a conservative bound stated using
the published value is

    |y-x| <= u |y| + h/2.

For a normal result the sharper `|y-x| <= u|y|` applies, including the normal
boundary. Preserve the nonzero-rounds-to-zero `Unpublishable` outcome rather
than pretending it is an exact-zero publication. The source implementation
normalizes an exact zero to +0 and otherwise keeps that conversion outcome.

### S=0

The raw-max invariant gives y=0. A finite published zero in the present
non-input-derived path comes from x=0; a nonzero x rounding to zero would be
unpublishable. X_i=0 then makes the accepted numerator zero. With the unchanged
verification theorem and ceiling charge condition, the candidate-error bound
is zero, so q*=0. Consequently b=0 is honest. Positive verification scale
caused by coupling cannot create a positive budget on this path.

This proof requires the **new** zero budget and current outcome semantics.
It does not follow from equality of rounded scales or from a presumed unloaded
body. Data-free-block and input-derived premises are still their own premises.

### 0<S<Q

All such rows stay absolute. The unchanged A1 formula is

    b_row = up64(up64(epsilon S) + up64(u |y|) + h).

It satisfies `b_row >= epsilon S + u|y| + h`. Therefore

    |y-q*| <= alpha epsilon S + u|y| + h/2 <= alpha b_row.

This fits the existing publication qualification factors: 1+2^-22 at
p128/256 and 1+2^-21 at p512. No amplified-operand rounding estimate is used;
the actual final S supplies the retained-error budget, and the row's own
publication rounding is charged separately.

### S>=Q, absolute row

The threshold `R S` is exactly representable, since S>=2^-988 and R=2^-34.
Classification gives `|y|<R S`. Hence

    u|y| < 2^-87 S = 2^-23 epsilon S,
    h/2 <= 2^-87 S = 2^-23 epsilon S.

Their sum is at most `2^-22 epsilon S`. With `b=up64(epsilon S)`, the
published error is bounded by b(1+2^-22) at p128/256 and by b(1+2^-21) at
p512. These are the current factors; neither b nor the oracle is widened.

### Relative row

S>=Q and `|y|>=R S` imply a nonzero normal y. Using the normal rounding bound:

    |y-q*|/|y| <= alpha 2^-30 + 2^-53
               <= (2^23+3)/2^53 < 1/10^9.

The last inequality is the exact integer comparison
`8,388,611,000,000,000 < 9,007,199,254,740,992`. It uses the worst ceiling
alpha and preserves the published-value denominator in D1's argument.
The distinct R1 class-scale benchmark is not substituted for this assurance.

This establishes a sufficient **kernel-row** publication argument under the
listed premises. It does not automatically prove transformed product rows,
unit-roundtrip behavior or the D2 lower-bound availability claim.

## 3. Publication identity and exceptional rows

The proof requires y and S to be the bits ultimately published, not an earlier
approximation that finalization changes. `finish_selected` currently calls
`selected.published()`, applies `publish_prescribed`, then recomputes the
classification scales. A prospective early scale helper must either share
that operation or prove exact equality for every eligible row and floor.
Prescribed rows are excluded from S, but they still enter D2's displacement
sums and may be republished from exact combination terms.

For unpublishable and input-derived rows, P/C propose leaving today's M0
numerical checks intact. This avoids silently weakening other checks while
providing the direct X_i argument only for rows that actually carry it.
O9 must use the candidate's actual outcome at every attempted p, not the
verification's outcome or a coerced zero. If a later precision makes a row
publishable, recompute its eligibility, S and X for that pair.

Nonfinite coupled scales and conversions require an explicit existing or
selected refusal/encoding path. Infinity cannot satisfy a finite proof
budget. An implementation that drops `scales_at` must preserve the finite
extent checks it formerly supplied. The current zero-extent behavior remains
distinct from an assumed geometric single-node test.

## 4. R7 section 6.3 G5a: a separate unresolved obligation

R7 lines 839–840 derive a published-data lower bound using relative 2^-50
closeness between the converted publication scale and Sv. The direct row
argument above removes the need for that premise in the **error guarantee**;
it does not make that old G5a derivation true.

For a canonical-unit free component with no intervening unit transform, the
new stop rule instead supplies the absolute relation

    |v-y| <= epsilon S + u|y| + h/2.

Summing six component relations gives an explicit publication-quantization
allowance as well as six epsilon S terms. The original lower-bound deduction
subtracts 2^-60 S (=16 epsilon S) and charges relative summation/conversion
rounding. For normal-enough scales, the absolute h terms can be bounded
relative to epsilon S; for small or zero scales that inference is unavailable.
It must be derived case by case, not restored by calling S0 and Sv close.

Input-derived components need their own bound. For one case they publish the
binary64 prescription unchanged. For combinations, `prescribed_at` rounds the
exact prescription sum to P while `publish_prescribed` rounds that exact sum
once to binary64. Their difference is bounded from the common exact sum,
not by applying a new covered-row cap that excludes them.

For unit conversion, track each operation in its own unit and multiply its
rounding error by every following conversion factor. In a simple one-step
description, if x,v,y are in one unit and Y=RN64(c y), then

    |Y-c v| <= |Y-c y| + |c|(|y-x|+|x-v|).

The half-subnormal term from the raw unit is multiplied by |c|; a fresh
half-subnormal term belongs to the destination-unit rounding. Actual facade
roundtrips must be composed explicitly. If the kernel's decision scale is
canonical SI but D2 reconstructs from product-unit rows, equality of those
canonical bits must be proved or supplied by one shared projection contract.

Three concrete proof/implementation directions remain for G5a assessment,
without selecting or changing its protected check here:

1. Derive sufficient conditions under which the existing 2^-59 branch,
   2^-60 subtraction and 1+2^-40 comparison margin remain valid with the
   explicit publication and conversion error terms. Prove coverage of the
   actual admitted domain, including small scales and prescribed components.
2. Retain the existing reader criterion and, if necessary, check it exactly
   at production before claiming a readable selected receipt. This can enforce
   operability of a particular receipt but does not prove that every honest E
   passes; any availability consequence or new refusal must be stated.
3. If neither closes the intended domain, prepare a separately governed reader
   contract proposal based on outward quantization intervals and their unit
   conversions. It could derive a rigorous lower bound directly from public
   operands, but changes the current G5a criterion and is **not authorized or
   selected here**. Do not quietly relax the existing check to obtain a pass.

No G5a failure has been demonstrated by B01/B02, and no new probe was created
to decide these directions. The need for this proof is established by the
source dependency and ROOT's explicit consequence instruction.

## 5. Covered derived rows and relative reliance

D1 `DESIGN.md:424–429` derives stress guarantees from published actions and
asserts relative rounding terms in the product formulas. A repair to the
kernel's coupled stopping scale cannot automatically discharge every such
formula. For example, a raw action's absolute quantization term propagates
through 1/A, 1/Z, a span length or an intensification factor with that
multiplier; it does not become a universal unamplified h/2 at the destination.

The selected closure must either prove the current covered formula's entire
published-denominator 1e-9 argument with these terms, or identify an already
enforced invariant that makes them negligible. Normal-result rounding at a
later step does not erase earlier subnormal information loss. Existing
pressure/not-covered distinctions and all propagation factors stay unchanged.
This is a downstream proof obligation, not a new realized product-defect claim
or permission to add cases, change coverage or implement F2a.

## 6. Independent verification before selection

The verifier should check the X_i substitution against every M_q consumer;
the exact publication and eligibility identity; the three S regimes above;
both kind-pair coupling directions; shared Phi and p512 charge; exceptional
rows and finite encoding; G5a after unit conversion; and covered derived-row
propagation. It must distinguish a correct sufficient lemma from a complete
implementation/contract proposal. Remaining A0 output may sharpen the failure
mechanism or show additional exclusions; it cannot be presumed by this draft.
