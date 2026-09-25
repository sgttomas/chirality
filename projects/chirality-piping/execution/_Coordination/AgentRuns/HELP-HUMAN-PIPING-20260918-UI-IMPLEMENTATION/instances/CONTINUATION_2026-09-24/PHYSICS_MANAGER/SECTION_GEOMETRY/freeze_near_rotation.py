"""Independent proper-rotation extension companion, before observation."""
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
    extension=Q(old["extension_m"]["exact_rational_with_bounded_pi"])
    cases.append({"id":old["id"],"nu_bits_hex":old["nu_bits_hex"],
        "scalar_extension_m":old["extension_m"],
        "global_displacement_m":[val(extension*q) for q in [Q(1,3),Q(2,3),Q(2,3)]]})
record={"actor":"/root/numerical_policy_review","actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
 "status":"independent_proper_rotation_append_before_observation","inputs":near["inputs"],
 "proper_rotation_columns":[["1/3","2/3","2/3"],["-2/sqrt(5)","1/sqrt(5)","0"],
   ["-2/(3sqrt(5))","-4/(3sqrt(5))","sqrt(5)/3"]],
 "transformed_tip_m":[2,4,4],"cases":cases,
 "derivation":"Original displacement is extension*e_x; R is proper orthogonal, so physical displacement is extension*(1,2,2)/3. Root full anchor is invariant as a constrained subspace; rotate y_reference by R as well.",
 "criterion":"Every nonzero global displacement component retains1e-9 relative; scalar norm also compared. No old8 predicates altered.",
 "discriminator":"Correctly summing already-rounded t and -2nu*t can still lose the tiny source force. Group source coefficients before multiplying common pressure and direction magnitude.",
 "limits":"Bounded linear-isotropic source/rotation control, not a universal forward-error or geometric-input condition guarantee."}
(base/"NEAR_ROTATION_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({"last_valid_vector":[q["decimal"] for q in cases[-1]["global_displacement_m"]]},indent=2))
