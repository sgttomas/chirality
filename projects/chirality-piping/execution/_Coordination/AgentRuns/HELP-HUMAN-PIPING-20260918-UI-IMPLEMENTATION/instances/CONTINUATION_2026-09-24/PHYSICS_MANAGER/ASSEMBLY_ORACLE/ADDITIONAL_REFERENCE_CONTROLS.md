# Additional case/material controls before observation

These additional independent expectations are selected before their first public test run. They preserve the original reference freeze rather than overwrite it. Issuer /root/physics_manager relayed ROOT's prospective interface allocation: region identity is (load_case_id,region_id), duplicate region IDs within one case block, exact-pressure rows use load_case basis_ref and region evidence binds their actual row IDs. Same region ID in distinct cases is permitted. Exact maximum displacement selects across all case solves; ties use lexicographically smallest case ID then location.

The previously frozen annulus remains ri=.05, ro=.06, L=6 m, with J=3.355e-6*pi m^4. A +1 N*m end torque on the root-fixed pipe gives theta_x=6/(G*J), independently of the linear pressure strain. Adding this torsion makes the material G authority observable.

- Selected point E=100 GPa, nu=.1 gives G=(500/11) GPa and pressure extension 3/13750 m.
- At the strict-interior midpoint between (T=0 degC,E=100 GPa,nu=.1) and (T=100 degC,E=300 GPa,nu=.4), the common interpolated pair is E=200 GPa,nu=.25, hence G=80 GPa and pressure extension 3/44000 m. Interpolating endpoint G values instead gives about 76.30 GPa and must fail the torque reference.
- A thermal case selecting a complete point E=100 GPa,nu=.2,alpha=20e-6/degC and DeltaT=100 degC gives extension .012+9/55000 m. Missing unused base alpha must not invalidate that selected complete point; missing actual selected alpha must block.
- Missing G is permitted in exact mode with complete E/nu, but missing G remains a legacy input error. A nonempty request material list replaces the model list; missing used material or missing override nu cannot be repaired by merging base entries.
- Two otherwise identical cases with p=+2 MPa and p=-4 MPa give extensions +3/55000 and -6/55000 m. The second has the larger displacement magnitude regardless of case order. With p=+/-2 MPa the magnitudes tie and the agreed case-ID tie rule applies. Pressure Nw=p*.0025*pi and all Lamé/axial quantities remain case-qualified.

All nonzero quantity comparisons remain relative 1e-9. The original fixture-zero scale rule is unchanged. These formulas come from the previously frozen pressure compliance and circular torsion relations, not observed production results. They establish neither shear/Bourdon/prestress behavior nor native/consumer qualification.

The manager's separately owned X1 caller-control statics were also checked in chat: with A=1e6*Z, w_z=8A, tip Fz=-4A, Fy=-A and Mz=A at L=1, right-segment equilibrium gives My=4A*x*(1-x), Mz=A*x. The stress magnitude squared divided by 1e12 is x²(16(1-x)²+1), whose derivative is 2x(32x²-48x+17). The maximum is at (6-sqrt(2))/8 and equals 1e6*sqrt(71+8sqrt(2))/8 Pa, exceeding the endpoint 1e6 Pa. This pressure test owner does not duplicate or qualify the manager's separate X1 implementation test.
