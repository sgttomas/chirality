# Independent exact annulus section reference

Date: 2026-09-24. TASK /root/numerical_policy_review, actual harness parent /root, issuer/integrator /root/physics_manager. Full TASK role was read from ORACLE_BRIEF.md; prior Root/Piping/LOOP and pressure-reference instructions remain active. No delegation or new production geometry edit/read occurred before this freeze.

**PASS for independent A/Ai/I/J/Z and response reference qualification.** The exact-only repair may consistently reuse a scaled, factored annulus property calculation on the already declared normalized binary64 radii. It must not silently substitute the originally entered wall thickness for the represented gap while continuing to claim the same radii. This is reference readiness, not a runtime pass or authored-source accuracy claim.

## Integrals, dimensions and stable identities

Area integration over ri <= r <= ro gives A=pi*(ro²-ri²) and fluid bore Ai=pi*ri². Integrating y² or z² over the section gives I_y=I_z=pi*(ro⁴-ri⁴)/4. Polar integration gives J=I_y+I_z=2I. The circular outer-fibre section modulus is Z=I/ro. A/Ai have m² units, I/J m⁴ and Z m³.

Equivalent factorizations are:

    A = pi*(ro-ri)*(ro+ri)
    I = A*(ro²+ri²)/4
    J = A*(ro²+ri²)/2
    Z = I/ro.

These are algebraic identities, checked as exact rational expressions in freeze_geometry_reference.py. Near-equal fourth/squared powers should not be subtracted in ordinary arithmetic when the factored form can retain the represented gap. Range handling is still necessary: a literal A*(ro²+ri²) can overflow even when its quotient by four is representable. Reuse the existing scaled-number machinery; final positive finite property checks remain necessary, and a nonrepresentable final property must block rather than be clamped.

## What geometry the oracle means

For the SI inputs in this freeze, normalized OD and wall are their exact represented binary64 values. Radius formation is declared explicitly:

    ro = round_binary64(OD_SI/2)
    ri = round_binary64(ro-wall_SI).

The runtime property and response expectations then integrate the exact annulus defined by those two declared floating-point radii, with mathematical pi. Expected radius bits are frozen, not read back from product geometry and reused as an oracle. The script separately evaluates the annulus defined by the exact normalized OD/wall pair before radius subtraction rounds; both interpretations remain in the JSON.

| Case | Declared ro bits | Declared ri bits | Effective gap m | Gap relative to entered wall |
|---|---|---|---:|---:|
| OD=.12, wall=.01 m | 3faeb851eb851eb8 | 3fa9999999999999 | .010000000000000002 | +1.73472e-16 |
| OD=.12, wall=1e-12 m | 3faeb851eb851eb8 | 3faeb851eb82ebc5 | 9.999986949615902e-13 | -1.3050384e-6 |

The thin case's represented-geometry free extension is +1.3050401129e-6 relative to the exact normalized OD/wall interpretation. Fixing frame/pressure consistency does not remove that radius-formation effect and must not be labelled 1e-9 accuracy against the entered wall geometry. A future geometry representation that preserves the original wall separately would be a declared contract change with its own evidence, not an invisible implementation substitute.

For the ordinary case the difference is far below the unchanged relative 1e-9 criterion, so the earlier ordinary SI oracles remain applicable.

## Frozen responses

FROZEN_SECTION_EXPECTATIONS.json is independently generated using Fraction and Machin pi (absolute pi error below 3e-142), with no product calculation imports. Inputs E=200 GPa, nu=.3 and L=6 m are explicit. The ordinary case uses p=2 MPa, tip Fy=100 N and tip Mx=1 N*m. The thin case uses p=1e-6 Pa, tip Fy=1e-12 N and tip Mx=1e-10 N*m, keeping the response small while exercising the arithmetic.

| Quantity | Ordinary represented annulus | Thin represented annulus |
|---|---:|---:|
| A, m² | .00345575191894877303 | 3.76990626439743891e-13 |
| I, m⁴ | 5.27002167639687829e-6 | 6.78583127580229250e-16 |
| J, m⁴ | 1.05400433527937566e-5 | 1.35716625516045850e-15 |
| Free pressure extension, m | 5.45454545454545320e-5 | 3.60000469805440638e-7 |

The complete Ai/Z/traction/displacement/stress/torsion values are frozen in JSON. Their independent formulas are:

    P=p*Ai; G=E/[2(1+nu)]
    ux=(1-2nu)*P*L/(E*A)
    uy=Fy*L³/(3E*I); rz=Fy*L²/(2E*I)
    rx=Mx*L/(G*J)
    sigma_axial=P/A
    tau_outer=Mx*ro/J
    max_absolute_normal_stress=P/A+Fy*L/Z.

The last expression applies to this positive uniform axial wall tension plus monotonic cantilever bending, with its maximum at the root. Torsion remains a separate stress component. Supports must carry -Fy, -Fy*L and -Mx in the corresponding global reaction components; the transferred-cap pair contributes no net root axial reaction in the free-extension case.

## Range and boundary controls

- Entered OD=.12 m and wall=1e-20 m form ri=ro in binary64. That is an unresolved/nonrepresentable nonzero annulus, not a valid zero-thickness pipe. Block without a thickness floor.
- OD=1e200, wall=1e190 have a bore area beyond binary64 range; OD=1e-200, wall=1e-210 have positive bore/wall areas below its smallest positive value. Successful exact publication must block in each case. These are arithmetic boundaries, not physical design limits.
- A positive range control uses declared ro≈1e77, ri≈5e76. Exact I≈7.36e307 and J≈1.47e308 are representable, although A*(ro²+ri²) before division by four exceeds binary64 maximum. The frozen public model uses E=1e-100 Pa, p=1e-155 Pa, L=1e79 m and fully fixed ends so material/stiffness products remain finite. It is an arithmetic/range control only. Test actual geometry publication once the carrier allocation is confirmed; do not require a numerical solve for a free system whose scaling has not been qualified.

All nonzero comparisons retain relative 1e-9. No legacy section method, existing pressure14 source, protected threshold or historical evidence is changed by this reference. Tiny wall and extreme range examples are not manufactured-pipe or shell/buckling validation.

## Source suitability and next step

The current straight-annulus pressure qualification and the primary pressure/elasticity source review remain applicable. This task independently rederived the circular integrals and exact identities; no OCR equation, proprietary code rule or external-solver result was used. The material law is small-strain homogeneous isotropic elasticity on declared reference geometry. Local end/interface stresses, ovalization, collapse, pressure stiffness and engineering fitness remain outside these arithmetic controls.

ROOT's current expert-correctness authority covers this exact-only consistency repair. Parent owns source implementation and legacy preservation. Next, author only tests/pressure_section_geometry.rs and this evidence directory; inspect normalized radii/A/Ai plus physical I/J/Z observables through the real public entrypoint. New direct I/J/Z carrier assertions wait for ROOT allocation. No Cargo until parent releases the shared build slot.
