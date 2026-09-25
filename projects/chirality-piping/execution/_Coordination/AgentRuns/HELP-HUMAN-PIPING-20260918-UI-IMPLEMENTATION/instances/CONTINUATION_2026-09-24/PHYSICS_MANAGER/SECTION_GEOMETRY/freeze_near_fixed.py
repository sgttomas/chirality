"""Independent restrained near-limit wall/effective/reaction reference."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal,localcontext
import json
base=Path(__file__).resolve().parent
near=json.loads((base/"NEAR_INCOMPRESSIBLE_EXPECTATIONS.json").read_text())
def val(q):
    with localcontext() as c:
        c.prec=90
        d=str(Decimal(q.numerator)/Decimal(q.denominator))
    return {"decimal":d,"f64":float(q),"exact_rational_with_bounded_pi":str(q)}
cases=[]
for old in near["cases"]:
    cap=Q(old["source_pressure_cap_N"]["exact_rational_with_bounded_pi"])
    net=Q(old["source_net_axial_rhs_N"]["exact_rational_with_bounded_pi"])
    cases.append({"id":old["id"],"nu_bits_hex":old["nu_bits_hex"],
        "wall_force_N":val(cap-net),"effective_force_N":val(-net),
        "left_support_Fx_N":val(net),"right_support_Fx_N":val(-net),
        "extension_m":val(Q())})
record={"status":"independent_fixed_near_reference_before_recovery_repair","actor":"/root/numerical_policy_review",
 "actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
 "inputs":near["inputs"],"cases":cases,
 "derivation":"Both ends fixed, no thermal/mechanical load: epsilon=0; Nw=2nuP; S=(2nu−1)P; R_left=(1−2nu)P and R_right=−R_left. Reference S is formed exactly, not by subtracting rounded wall and cap floats.",
 "criterion":"Nonzero wall, effective force and each signed support reaction keep relative1e-9; exact zero displacement is separate.",
 "limits":"Arithmetic/control interpretation only; source grouping and constitutive recovery must be verified at real public entrypoint. Prior free/geometry references remain unchanged."}
(base/"NEAR_FIXED_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({c["id"]:{"S":c["effective_force_N"]["decimal"],"left_R":c["left_support_Fx_N"]["decimal"]} for c in cases},indent=2))
