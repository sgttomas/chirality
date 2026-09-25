"""Independent near-incompressible load-cancellation controls, no product import."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal,localcontext
import struct,json
base=Path(__file__).resolve().parent
def atan(q,n):
    return sum((Q((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),Q())
pi=16*atan(5,100)-4*atan(239,30)
def val(x):
    with localcontext() as c:
        c.prec=90
        d=str(Decimal(x.numerator)/Decimal(x.denominator))
    return {"decimal":d,"f64":float(x),"exact_rational_with_bounded_pi":str(x)}
def bits(x):return f"{struct.unpack('>Q',struct.pack('>d',x))[0]:016x}"
d=Q(0.12);t=Q(0.01);r=d/2
a=pi*t*(d-t);ai=pi*(r-t)**2;p=Q(2e6);e=Q(200e9);length=Q(6);cap=p*ai
last=struct.unpack('>d',bytes.fromhex("3fdfffffffffffff"))[0]
cases=[]
for label,nu in [("near",0.499999),("nearer",0.4999999999),("last_valid",last)]:
    n=Q(nu); net=(1-2*n)*cap
    assert 0<n<Q(1,2) and net>0
    cases.append({"id":label,"nu":nu,"nu_bits_hex":bits(nu),"one_minus_two_nu":val(1-2*n),
        "source_pressure_cap_N":val(cap),"source_pressure_eigen_magnitude_N":val(2*n*cap),
        "source_net_axial_rhs_N":val(net),"extension_m":val(net*length/(e*a)),
        "wall_force_N":val(cap),"axial_membrane_Pa":val(cap/a)})
assert Q(last)==Q(1,2)-Q(1,2**54)
record={"actor":"/root/numerical_policy_review","actual_harness_parent":"/root","issuer_integrator":"/root/physics_manager",
    "status":"independent_near_incompressible_expectations_frozen_before_source_repair",
    "inputs":{"OD_m":0.12,"wall_m":0.01,"E_Pa":200e9,"p_Pa":2e6,"L_m":6.0},
    "cases":cases,
    "ledger":"Physical cap and eigen contributions remain separately identified; assembled net load must retain their small mathematical difference. A tiny assembled-system residual does not prove original-source load accuracy.",
    "criterion":"Nonzero extension and source netload use unchanged relative1e-9; do not replace them with zero or use a force-scale floor.",
    "invalid_neighbor":{"nu":0.5,"expected":"material range rejection unchanged"},
    "limits":"Numerical source-cancellation control for admissible isotropic inputs, not real-material incompressibility validation or forward-error guarantee for arbitrary models."}
(base/"NEAR_INCOMPRESSIBLE_EXPECTATIONS.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({c["id"]:{"nu_bits":c["nu_bits_hex"],"net_N":c["source_net_axial_rhs_N"]["decimal"],"extension_m":c["extension_m"]["decimal"]} for c in cases},indent=2))
