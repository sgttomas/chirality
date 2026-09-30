# A0 finite source-case matrix — sealed draft

This specifies at most 24 distinct sources. Nothing here has been executed.
All predicted outcomes are hypotheses for the unmutated public API and exact
oracle, not acceptance results. The first tranche is B01–B16. C17–C24 require
the separate extension checkpoint in `A0_BRIEF.md`; they occupy the remaining
eight slots, not eight additions to 24. No unspecified sweep or random search.

## Shared conventions

Let h=2^-1074. Every input is an exact binary64 value; future probe code must
construct the specified powers of two and h multiples from their exact bits,
not decimal approximations. Coordinates are m; E and G are Pa; A is m²;
Iy, Iz and J are m⁴; axial stiffness is N/m; torsional stiffness is N·m/rad;
loads are N or N·m as appropriate. Radians are the rotation unit.

Every source has two nodes, `(0,0,0)` and `(L,0,0)`, one straight member id 1
from node 0 to node 1, y-reference `(0,1,0)`, and zero constraints on all DOFs
except the explicitly free ones. No prescribed nonzero motion, stations,
directional springs, support groups, combination, seed or mutation is used.
Empty optional lists remain empty. Use stable unique source IDs for separate
load contributions; never pre-round their sum into one binary64 load.

These are mathematical kernel sources. They do not claim realistic piping
properties, present product-capture admission or engineering acceptance.
Actual `PrimitiveSource::new` and full solve admission must be observed.

## One-free-DOF sources

T(L,M): only node 1 Rx is free; E=G=A=Iy=Iz=1, J=4L; one tip Mx=M.
The independent scalar oracle is r=M/4; all translations are exactly zero.

A(L,F): only node 1 Ux is free; E=G=Iy=Iz=J=1, A=4L; one tip Fx=F.
The independent scalar oracle is u=F/4; all rotations are exactly zero.

| ID | Family | L | Nonzero load | Purpose and predicted scale fact, conditional on selection |
|---|---|---|---|---|
| B01 | T | 2^100 | 5h | Raw r=5h/4 publishes h; tr S_v/S_pub=5/4. |
| B02 | A | 2^-100 | 5h | Mirror through 1/L: ro S_v/S_pub=5/4. |
| B03 | T | 1 | 5h | Unamplified raw-rounding control. |
| B04 | A | 1 | 5h | Unamplified inverse-coupling control. |
| B05 | T | 2^85 | 5h | Coupled published tr scale 2^-989, below A1 boundary. |
| B06 | T | 2^86 | 5h | Coupled published tr scale 2^-988, on plain-b branch. |
| B07 | A | 2^-85 | 5h | Coupled published ro scale 2^-989. |
| B08 | A | 2^-86 | 5h | Coupled published ro scale 2^-988. |
| B09 | T | 2^-100 | 5h | Positive retained tr coupling rounds to zero publication scale. |
| B10 | A | 2^100 | 5h | Positive retained ro coupling rounds to zero publication scale. |
| B11 | T | 2^100 | 4h | Raw result exactly h; remove the pre-coupling rounding loss. |
| B12 | A | 2^-100 | 4h | Mirror exact-subnormal control. |
| B13 | T | 2^100 | 2^-1020 | Raw result exactly 2^-1022, normal-boundary control. |
| B14 | A | 2^-100 | 2^-1020 | Mirror normal-boundary control. |
| B15 | T | 2^100 | 2h | Raw result h/2 ties to zero; O9 should exclude the unpublishable nonzero driver. |
| B16 | A | 2^-100 | 2h | Mirror tie/underflow exclusion. |

In B09/B10 the zero-scale rows are not claimed to have nonzero truth. In
B15/B16 a nonzero retained value rounding to zero is **unpublishable**, not a
published-zero witness. Every family includes the layout's displacement
magnitudes; the oracle and evidence must account for them.

## Three-free-DOF cancellation sources

Define C(L,a,k,F,t,q,g), with free node 0 Ux, node 1 Ux and node 1 Rx. Set
E=G=Iy=Iz=1, A=aL, J=4L. Add one global-axis Ux spring id 1 of stiffness k at
grounded node g (0 or 1). The other axial node is j=1-g. Apply to g separate
contributions `+F`, `+kq` when nonzero, and `+t` when nonzero; apply `-F` to j.
Apply `5h` as Mx at node 1. All three contributions are individually binary64
inputs in this matrix. Omit zero loads, recording the omission convention.

Exact oracle:

    u_g = q + t/k;  u_j = q + t/k - F/a;  r_1x = 5h/4.

The two-by-two axial stiffness is `[[a+k,-a],[-a,a]]` in (g,j) order;
its determinant ak is positive. The torsional DOF is independent with stiffness
4. This is not an assertion that a particular finite-precision schedule selects.

| ID | L | a | k | F | t | q | g | Purpose |
|---|---|---|---|---|---|---|---|---|
| C17 | 2^100 | 2^76 | 2^-33 | 2^-900 | 9h | 0 | 0 | Main absolute-claim candidate: exact u_g=(9/8)2^-1038. |
| C18 | 2^100 | 2^76 | 2^-33 | 2^-900 | 8h | 0 | 0 | Bound control: exact u_g=2^-1038. |
| C19 | 2^100 | 2^76 | 2^-33 | 2^-900 | 10h | 0 | 0 | Full retained-disagreement boundary; positive W-plus/magnitude charge can reject p=128. |
| C20 | 2^100 | 2^76 | 2^-33 | 2^-900 | 0 | 0 | 0 | Exact-zero truth control. |
| C21 | 2^100 | 2^76 | 2^-33 | 2^-900 | 9h | 0 | 1 | Ground/load placement reverses the favorable axial elimination order; test the competing explanation. |
| C22 | 2^-100 | 2^276 | 2^167 | 2^-900 | 9h | 0 | 0 | Zero published tr-scale candidate; exact u_g=9·2^-1241 remains nonzero below binary64. |
| C23 | 2^100 | 2^56 | 2^-33 | 2^-920 | 9h | 2^-1008 | 0 | Relative-threshold candidate: exact error increment d=(9/8)2^-1038. |
| C24 | 2^100 | 2^56 | 2^-33 | 2^-920 | 0 | 2^-1008 | 0 | Exact relative-threshold baseline control. |

For C17–C21, A=2^176 and J=2^102. For C22, A=2^176 and J=2^-98.
For C23/C24, A=2^156 and J=2^102; the separate `kq` load is 2^-1041.
All primitives are finite, strictly positive and normal. The spring is weak
relative to a even where its absolute stiffness is large. These dimensional
checks do not replace actual validation, geometry checks or receipt encoding.

Stop the activated tranche on a realized false claim and return its complete
packet immediately. Unrun cases remain named and unrun; do not continue merely
to fill the matrix. A named refusal is evidence about that case, never a pass.
