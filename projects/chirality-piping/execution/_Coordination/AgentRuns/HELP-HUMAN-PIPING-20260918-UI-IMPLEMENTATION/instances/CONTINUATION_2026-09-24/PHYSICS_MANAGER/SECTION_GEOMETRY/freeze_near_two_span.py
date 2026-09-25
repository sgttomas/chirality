"""Independent equal-bore, distinct near-limit nu chain reference."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal,localcontext
import struct,json
base=Path(__file__).resolve().parent
def atan(q,n):return sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),Q())
pi=16*atan(5,100)-4*atan(239,30)
def val(q):
    with localcontext() as ctx:
        ctx.prec=90
        d=str(Decimal(q.numerator)/Decimal(q.denominator))
    return {"decimal":d,"f64":float(q),"exact_rational_with_bounded_pi":str(q)}
def number(bits):return struct.unpack(">d",bytes.fromhex(bits))[0]
nu1=Q(number("3fdfffffffffffff"));nu2=Q(number("3fdffffffffffffe"))
assert 1-2*nu1==Q(1,2**53) and 1-2*nu2==Q(1,2**52)
ri=Q(1,16);ro1=Q(5,64);ro2=Q(3,32)
a1=pi*(ro1**2-ri**2);a2=pi*(ro2**2-ri**2)
e1=Q(200000000000);e2=Q(100000000000);l1=l2=Q(3);p=Q(2000000)
cap=p*pi*ri**2
d1=(1-2*nu1)*cap*l1/(e1*a1);d2=(1-2*nu2)*cap*l2/(e2*a2)
assert d1==Q(1,2**53*18750)
assert d2==Q(3,2**52*62500)
assert d2/d1==Q(9,5)
record={"actor":"/root/numerical_policy_review","actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
 "status":"independent_append_before_grouped_repair_tests",
 "inputs":{"ri_m":0.0625,"OD1_m":0.15625,"wall1_m":0.015625,"OD2_m":0.1875,"wall2_m":0.03125,
  "E1_Pa":200000000000.0,"E2_Pa":100000000000.0,"L1_m":3.0,"L2_m":3.0,"p_Pa":2000000.0,
  "nu1_bits_hex":"3fdfffffffffffff","nu2_bits_hex":"3fdffffffffffffe"},
 "wall_force_N":val(cap),"effective_force_N":val(Q()),
 "span1_extension_m":val(d1),"span2_extension_m":val(d2),"tip_displacement_m":val(d1+d2),
 "middle_displacement_m":val(d1),"span_extension_ratio":val(d2/d1),
 "source_global_axial_rhs_N":[val(-(1-2*nu1)*cap),val(2*(nu2-nu1)*cap),val((1-2*nu2)*cap)],
 "wall_stress1_Pa":val(cap/a1),"wall_stress2_Pa":val(cap/a2),
 "reference_derivation":"Each transferred free span carries common P. Compatibility sums Li*(1−2nu_i)*P/(EiAsi); bore/OD/wall are exact dyadic rationals, so no radius-formation ambiguity. Internal RHS is2*(nu2−nu1)*P.",
 "mutation_discriminators":["Retaining only stable terminal cancellation but losing the interior near-equal Poisson difference changes the middle displacement.","Using one global nu changes at least one span extension.","Authored member or region-terminal reversal cannot change physical displacements or tension-positive wall/effective forces."],
 "limits":"Two span increments differ only by factor1.8; subtracting nodal displacements is benign here. No claim that an increment1e-20 can be recovered accurately by subtracting positions/displacements of scale1e-10. Nonzero1e-9 remains unchanged."}
(base/"NEAR_TWO_SPAN_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:record[k]["decimal"] for k in ["span1_extension_m","span2_extension_m","tip_displacement_m","span_extension_ratio"]},indent=2))
