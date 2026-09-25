# Hydrostatic column — formulation ownership control

ROOT raised this counterexample during design review. This is an independently derived one-dimensional free body, not a vendor benchmark. It sharpens the bounded hydrotest design; it does not implement a varying-pressure adapter.

Take a straight vertical, constant-bore closed pipe from z=0 at its bottom to z=H at its top, positive z upward. The pipe is supported axially only at the top. Ignore pipe/cap weight and external pressure; the contained static fluid has density rho, gravitational acceleration magnitude g, and bore area A. Pressure at the top is p0. Use cross-section-average pressure and the existing long-annulus/small-strain approximation, without local cap or junction stress. Fluid-wall shear is zero for this static vertical column.

`p(z)=p0+rho*g*(H-z)` and `p_bottom=p0+rho*g*H`.

The fluid pushes upward on the top closure by p0*A and downward on the bottom closure by p_bottom*A. Their net force is `-rho*g*A*H=-W`. There is no axial pressure traction on the straight vertical side wall. A top support action +W balances the two physical cap actions. At any interior wall cut, the lower-part free body contains the bottom cap force but no distributed axial fluid-on-wall traction, so

`N_wall(z)=p_bottom*A` (constant tension).

The effective axial force is `S(z)=N_wall(z)-p(z)*A=rho*g*A*z`. Its derivative equals +rho*g*A, so an equivalent effective-force equation can carry downward distributed contents weight. It must transform the boundary actions and recover `N_wall=S+pA` consistently. That body term must not be added a second time to the wall-force equation already carrying the physical cap imbalance. A useful source ledger names the owned formulation and the transformation explicitly.

Invented decisive values: H=10m, rho=1000kg/m³, g=10m/s², A=0.01m², p0=200000Pa. Then W=1000N and p_bottom=300000Pa. At z=[0,5,10]m:

| Model | Wall force N | Effective force N | Top support N |
|---|---|---|---|
| Correct physical cap / wall-force balance | [3000,3000,3000] | [0,500,1000] | 1000 |
| Equivalent consistently transformed effective-force balance | [3000,3000,3000] after adding actual p(z)A | [0,500,1000] | 1000 |
| Actual cap forces plus full axial distributed contents weight again | [3000,3500,4000] | [0,1000,2000] | 2000 |
| Uniform p=p0 plus distributed contents weight in a wall-force model | [2000,2500,3000] | [0,500,1000] using the incorrect uniform p | 1000 |
| Uniform p=p_average plus distributed contents weight in a wall-force model | [2500,3000,3500] | [0,500,1000] using the incorrect uniform p | 1000 |

Both uniform rows pass total reaction and even the effective-force distribution while reporting wrong actual wall tension over most of the member. A global-force-only test cannot validate pressure/body-force bookkeeping. A uniform maximum p=p_bottom gives a different error; it is not universally conservative for all stress/displacement/support responses.

For an explicit user material E=200GPa, nu=0.3 and wall area A_s=0.001m², the existing long-annulus axial constitutive relation gives

`epsilon(z)=[N_wall(z)-2*nu*p(z)*A]/(E*A_s)`.

Integrating over H gives extension 0.000075m for the correct state. The uniform p0 approximation gives 0.000065m, despite the right total top reaction. More strongly, uniform p_average=250000Pa gives the same mean wall force, mean pressure contribution and total extension 0.000075m as the correct state. Its station wall forces [2500,3000,3500]N are still wrong. Therefore reaction, mean strain, end displacement and an apparently correct effective-force distribution together are insufficient without the actual pressure and wall-force distributions. This is an additional independent discriminator within the selected linear model; top-anchored bottom displacement is the negative of this positive extension. The geometry needed for those positive annular areas exists; no real material library data is implied.

The first uniform-pressure/full-fluid hydrotest slice therefore admits only members with zero axial gravity projection in the current cross-section-averaged beam approximation. For nonzero projection, implement the pressure-head field with pressure eigenstrain, actual physical boundary transfer and wall/effective recovery owned by one adapter, or explicitly withhold that requested physical capability. Small transverse head across a horizontal cross-section is part of the declared one-dimensional averaging approximation; this design does not claim a three-dimensional exact hydrostatic shell stress field. Gravity/mass alone cannot silently select this pressure field, and pressure alone cannot create or duplicate a fluid mass input. Drained, separately supported closures and other topology require their own explicit free bodies.

An independent TASK reviewer is checking this derivation as well as the main design. `verify_reference_states.py` supplies exact rational numbers for the table and extension. Neither script nor design is an observed solver test; eventual production verification must interrogate actual published member/pressure/support results and preserve the protected criteria.
