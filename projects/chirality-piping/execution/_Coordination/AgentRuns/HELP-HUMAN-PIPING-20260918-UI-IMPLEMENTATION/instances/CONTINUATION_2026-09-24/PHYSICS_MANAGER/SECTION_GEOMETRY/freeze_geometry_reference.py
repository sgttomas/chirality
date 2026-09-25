"""Independent annulus integration and represented-radius runtime references."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import hashlib
import json
import struct

base = Path(__file__).resolve().parent
def atan_inverse(q,n):
    return sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),Q())
pi = 16*atan_inverse(5,100)-4*atan_inverse(239,30)
def value(x):
    with localcontext() as ctx:
        ctx.prec=80
        decimal=str(Decimal(x.numerator)/Decimal(x.denominator))
    try:
        rounded=float(x)
    except OverflowError:
        rounded=None
    return {"exact_rational_with_bounded_pi":str(x),"decimal":decimal,"f64":rounded,
            "binary64_representable":rounded is not None}
def bits(x):
    return f"{struct.unpack('>Q',struct.pack('>d',x))[0]:016x}"
cases=[]
for identifier, wall, pressure, transverse, torque in [
    ("ordinary",0.01,2e6,100.0,1.0),
    ("thin",1e-12,1e-6,1e-12,1e-10),
]:
    od=0.12
    ro=float(Q(od)/2)
    ri=float(Q(ro)-Q(wall))
    r,o=Q(ri),Q(ro)
    assert 0<r<o
    # Exact integrals and factorizations checked independently of product code.
    difference=o*o-r*r
    area=pi*difference
    area_factored=pi*(o-r)*(o+r)
    inertia=pi*(o**4-r**4)/4
    assert area==area_factored
    assert inertia==area*(o*o+r*r)/4
    polar=2*inertia
    modulus=inertia/o
    bore=pi*r*r
    e=Q(200e9);nu=Q(0.3);g=e/(2*(1+nu));length=Q(6)
    p=Q(pressure);fy=Q(transverse);t=Q(torque);cap=p*bore
    sigma=cap/area
    extension=(1-2*nu)*cap*length/(e*area)
    authored_ro=Q(od)/2
    authored_ri=authored_ro-Q(wall)
    authored_area=pi*(authored_ro**2-authored_ri**2)
    authored_cap=p*pi*authored_ri**2
    authored_extension=(1-2*nu)*authored_cap*length/(e*authored_area)
    cases.append({
        "id":identifier,
        "inputs":{"OD_m":od,"wall_m":wall,"p_Pa":pressure,"E_Pa":200e9,"nu":0.3,"L_m":6.0,
            "tip_Fy_N":transverse,"tip_Mx_Nm":torque},
        "normalized_geometry_semantics":"ro=round_binary64(OD_SI/2), ri=round_binary64(ro-wall_SI); all exact-profile properties and response references bind these declared radii",
        "ro_m":ro,"ri_m":ri,"ro_bits_hex":bits(ro),"ri_bits_hex":bits(ri),
        "effective_gap_m":value(o-r),
        "effective_gap_relative_to_entered_wall":value((o-r)/Q(wall)-1),
        "A_m2":value(area),"Ai_m2":value(bore),"I_m4":value(inertia),"J_m4":value(polar),"Z_m3":value(modulus),
        "P_N":value(cap),"G_Pa":value(g),
        "free_pressure_extension_m":value(extension),
        "axial_membrane_Pa":value(sigma),
        "tip_bending_y_m":value(fy*length**3/(3*e*inertia)),
        "tip_rotation_z_rad":value(fy*length**2/(2*e*inertia)),
        "tip_rotation_x_rad":value(t*length/(g*polar)),
        "torsional_surface_shear_Pa":value(t*o/polar),
        "maximum_absolute_normal_stress_Pa":value(sigma+fy*length/modulus),
        "lame_inner_radial_Pa":value(-p),"lame_outer_radial_Pa":value(Q()),
        "lame_inner_hoop_Pa":value(p*(o*o+r*r)/difference),
        "lame_outer_hoop_Pa":value(2*p*r*r/difference),
        "root_force_Fy_N":value(-fy),"root_moment_Mz_Nm":value(-fy*length),"root_moment_Mx_Nm":value(-t),
        "authored_OD_wall_exact_area_m2":value(authored_area),
        "authored_OD_wall_exact_pressure_extension_m":value(authored_extension),
        "represented_vs_authored_extension_relative":value(extension/authored_extension-1),
    })
assert cases[0]["ro_bits_hex"]=="3faeb851eb851eb8"
assert cases[0]["ri_bits_hex"]=="3fa9999999999999"
assert cases[1]["ri_bits_hex"]=="3faeb851eb82ebc5"
assert float(Q(0.12)/2-Q(1e-20))==float(Q(0.12)/2)
large_ro=float(Q(2e77)/2);large_ri=float(Q(large_ro)-Q(5e76))
large_o=Q(large_ro);large_r=Q(large_ri)
large_area=pi*(large_o**2-large_r**2)
large_i=pi*(large_o**4-large_r**4)/4
large_j=2*large_i
f64_max=Q(float.fromhex("0x1.fffffffffffffp+1023"))
assert 0<large_i<large_j<f64_max
assert large_area*(large_o**2+large_r**2)>f64_max
large_p=Q(1e-155);large_cap=large_p*pi*large_r**2
large_nu=Q(0.3)
large={
    "inputs":{"OD_m":2e77,"wall_m":5e76,"E_Pa":1e-100,"nu":0.3,"p_Pa":1e-155,"L_m":1e79},
    "boundary":"both ends fully fixed; pure pressure; geometry/range control only",
    "ro_m":large_ro,"ri_m":large_ri,"ro_bits_hex":bits(large_ro),"ri_bits_hex":bits(large_ri),
    "A_m2":value(large_area),"Ai_m2":value(pi*large_r**2),
    "I_m4":value(large_i),"J_m4":value(large_j),"Z_m3":value(large_i/large_o),
    "unscaled_A_times_radius_sum_before_division":value(large_area*(large_o**2+large_r**2)),
    "fixed_wall_force_N":value(2*large_nu*large_cap),
    "fixed_axial_membrane_Pa":value(2*large_nu*large_cap/large_area),
    "root_reaction_N":value((1-2*large_nu)*large_cap),
    "range_fact":"I and J are representable although A*(ro²+ri²) before division by4 exceeds binary64 maximum; avoid rejecting based only on that intermediate"
}
record={
    "status":"frozen_independent_before_section_source_repair",
    "actor":"/root/numerical_policy_review","actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
    "method":"Exact rational circular-section integrals and Machin pi with absolute error<3e-142; all float inputs/radius formation explicit; no product calculation import",
    "comparison":{"all_nonzero":"relative 1e-9 unchanged","exact_zero":"1e-9 times independent same-dimension input force/moment/stress/strain scale; never redefine nonzero as zero"},
    "cases":cases,
    "representable_range_control":large,
    "boundaries":[
        {"id":"radius_gap_unrepresentable","OD_m":0.12,"wall_m":1e-20,"reason":"finite positive entered wall rounds ri to ro; nonzero annulus is not represented; must block, no fabricated thickness"},
        {"id":"area_overflow","OD_m":1e200,"wall_m":1e190,"reason":"true bore area exceeds binary64 maximum; must block successful exact publication"},
        {"id":"area_underflow","OD_m":1e-200,"wall_m":1e-210,"reason":"true positive bore/wall areas are below smallest positive binary64; must block successful exact publication"},
    ],
    "limits":"Thin wall is arithmetic/contract control, not physically manufactured pipe or shell/buckling validation. Consistency with declared binary64 radii does not prove 1e-9 accuracy against authored OD/wall geometry. Original pressure14 and protected historical criteria unchanged.",
}
(base/"FROZEN_SECTION_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({"cases":[{"id":c["id"],"A":c["A_m2"]["decimal"],"I":c["I_m4"]["decimal"],"J":c["J_m4"]["decimal"],"extension":c["free_pressure_extension_m"]["decimal"],"authored_difference":c["represented_vs_authored_extension_relative"]["decimal"]} for c in cases]},indent=2))
