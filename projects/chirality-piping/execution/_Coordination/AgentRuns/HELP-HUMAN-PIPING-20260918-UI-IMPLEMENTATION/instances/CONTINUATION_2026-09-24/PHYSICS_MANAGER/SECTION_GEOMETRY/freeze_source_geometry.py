"""Source OD/effective-wall successor; preserves earlier radii comparison freeze."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import json

base=Path(__file__).resolve().parent
earlier=json.loads((base/"FROZEN_SECTION_EXPECTATIONS.json").read_text())
def atan(q,n):
    return sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),Q())
pi=16*atan(5,100)-4*atan(239,30)
def val(x):
    with localcontext() as ctx:
        ctx.prec=80
        d=str(Decimal(x.numerator)/Decimal(x.denominator))
    try:
        f=float(x)
    except OverflowError:
        f=None
    return {"exact_rational_with_bounded_pi":str(x),"decimal":d,"f64":f}
def source_properties(inputs):
    diameter=Q(inputs["OD_m"]);t=Q(inputs["wall_m"])
    ro=diameter/2;ri=ro-t
    assert 0<ri<ro
    area=pi*t*(diameter-t)
    bore=pi*ri**2
    inertia=pi*(ro**4-ri**4)/4
    assert area==pi*(ro**2-ri**2)
    assert inertia==area*(ro**2+ri**2)/4
    return ro,ri,area,bore,inertia,2*inertia,inertia/ro
cases=[]
for old in earlier["cases"]:
    inputs=old["inputs"]
    ro,ri,a,ai,i,j,z=source_properties(inputs)
    e=Q(inputs["E_Pa"]);nu=Q(inputs["nu"]);length=Q(inputs["L_m"])
    g=e/(2*(1+nu));p=Q(inputs["p_Pa"]);cap=p*ai
    f=Q(inputs["tip_Fy_N"]);t=Q(inputs["tip_Mx_Nm"])
    cases.append({
        "id":old["id"],"inputs":inputs,
        "geometry_basis":"source normalized OD and effective wall; radii are rounded derived observations, not the property basis",
        "ro_bits_hex":old["ro_bits_hex"],"ri_bits_hex":old["ri_bits_hex"],
        "A_m2":val(a),"Ai_m2":val(ai),"I_m4":val(i),"J_m4":val(j),"Z_m3":val(z),
        "P_N":val(cap),"G_Pa":val(g),
        "free_pressure_extension_m":val((1-2*nu)*cap*length/(e*a)),
        "tip_bending_y_m":val(f*length**3/(3*e*i)),
        "tip_rotation_z_rad":val(f*length**2/(2*e*i)),
        "tip_rotation_x_rad":val(t*length/(g*j)),
        "axial_membrane_Pa":val(cap/a),
        "maximum_absolute_normal_stress_Pa":val(cap/a+f*length/z),
        "torsional_surface_shear_Pa":val(t*ro/j),
        "lame_inner_radial_Pa":val(-p),"lame_outer_radial_Pa":val(Q()),
        "lame_outer_hoop_Pa":val(2*p*ai/a),"lame_inner_hoop_Pa":val(2*p*ai/a+p),
        "root_force_Fy_N":val(-f),"root_moment_Mz_Nm":val(-f*length),"root_moment_Mx_Nm":val(-t),
        "earlier_declared_radius_comparison":{
            "A_m2":old["A_m2"],"I_m4":old["I_m4"],"J_m4":old["J_m4"],"Z_m3":old["Z_m3"],
            "free_pressure_extension_m":old["free_pressure_extension_m"],
            "relative_extension_difference":old["represented_vs_authored_extension_relative"]},
    })
large_input=earlier["representable_range_control"]["inputs"]
ro,ri,a,ai,i,j,z=source_properties(large_input)
large_p=Q(large_input["p_Pa"]);large_nu=Q(large_input["nu"]);cap=large_p*ai
limit=Q(float.fromhex("0x1.fffffffffffffp+1023"))
assert i<j<limit and a*(ro*ro+ri*ri)>limit
record={
    "status":"frozen_source_faithful_successor_before_production_repair",
    "actor":"/root/numerical_policy_review","actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
    "authority":"ROOT selected source OD/effective-wall geometry, preserving radii-only scalar kernel and earlier comparison history",
    "method":"Independent exact Fraction source-input integrals, Machin pi absolute error<3e-142; no product import or observed output as oracle",
    "source_semantics":"Inputs are exact normalized binary64 OD and effective wall. Exact mathematical ro=OD/2, ri=ro-wall define properties; rounded reported radii may differ. Cases here have no mill tolerance, so effective wall equals entered normalized wall.",
    "cases":cases,
    "representable_range_control":{
        "inputs":large_input,"boundary":"fully fixed both ends; pure pressure",
        "ro_bits_hex":earlier["representable_range_control"]["ro_bits_hex"],
        "ri_bits_hex":earlier["representable_range_control"]["ri_bits_hex"],
        "A_m2":val(a),"Ai_m2":val(ai),"I_m4":val(i),"J_m4":val(j),"Z_m3":val(z),
        "unrepresentable_intermediate":val(a*(ro*ro+ri*ri)),
        "fixed_wall_force_N":val(2*large_nu*cap),
        "fixed_axial_membrane_Pa":val(2*large_nu*cap/a),
        "root_reaction_N":val((1-2*large_nu)*cap),
    },
    "blocked_boundaries":earlier["boundaries"],
    "comparison":"Unchanged nonzero relative 1e-9; zero comparisons use independently specified same-unit load/strain scale. No source/represented tolerance substitution.",
    "limits":"Source-faithful arithmetic control; thin/extreme geometry is not manufactured-pipe, shell, collapse, local-end or engineering fitness evidence. Below-ULP rounded-ri collapse remains blocked per selected runtime contract.",
}
(base/"SOURCE_ODWALL_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({c["id"]:{k:c[k]["decimal"] for k in ["A_m2","Ai_m2","I_m4","J_m4","Z_m3","free_pressure_extension_m","tip_bending_y_m","tip_rotation_x_rad","axial_membrane_Pa","maximum_absolute_normal_stress_Pa"]} for c in cases},indent=2))
