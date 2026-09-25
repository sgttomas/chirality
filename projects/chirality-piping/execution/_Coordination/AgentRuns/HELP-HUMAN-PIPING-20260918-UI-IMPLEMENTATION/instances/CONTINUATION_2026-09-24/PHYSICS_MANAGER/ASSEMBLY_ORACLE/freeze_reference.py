"""Independent algebraic runtime-pressure expectations, before new source inspection."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
import json

base = Path(__file__).resolve().parent
def atan_inverse(q, n):
    return sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(n)), F())
pi = 16*atan_inverse(5,100)-4*atan_inverse(239,30)
def decimal(x):
    with localcontext() as ctx:
        ctx.prec = 70
        return str(D(x.numerator)/D(x.denominator))
def value(x):
    return {"exact":str(x),"decimal":decimal(x),"f64":float(x)}

As = F(11,10000)
Ai = F(1,400)
E = F(200000000000)
EA = E*As
nu = F(3,10)
P = F(2000000)*Ai
L = F(6)
assert EA == 220000000 and P == 5000
states = []
for name, restrained, transfer, thermal in [
    ("SI_FREE_TRANSFER",False,True,F()),
    ("SI_FIXED_TRANSFER",True,True,F()),
    ("SI_FREE_SEPARATE",False,False,F()),
    ("SI_FIXED_SEPARATE",True,False,F()),
    ("SI_FREE_TRANSFER_THERMAL",False,True,F(3,2500)),
    ("SI_FIXED_TRANSFER_THERMAL",True,True,F(3,2500)),
]:
    wall = -EA*thermal+2*nu*P if restrained else (P if transfer else F())
    strain = thermal+(wall-2*nu*P)/EA
    assert not restrained or strain == 0
    cap = P if transfer else F()
    reactions = [-wall+cap,wall-cap] if restrained else [F(),F()]
    states.append({
        "id":name,"restrained_axially":restrained,"both_closures_transfer":transfer,
        "thermal_strain":value(thermal),"extension_m":value(L*strain),
        "Nw_over_pi_N":value(wall),"S_over_pi_N":value(wall-P),
        "wall_actions_over_pi_N":[value(-wall),value(wall)],
        "axial_membrane_Pa":value(wall/As),
        "support_pair_over_pi_N":[value(q) for q in reactions],
        "eigen_pair_over_pi_N":[value(-EA*thermal+2*nu*P),value(EA*thermal-2*nu*P)],
    })
assert states[0]["extension_m"]["exact"]=="3/55000"
assert states[2]["extension_m"]["exact"]=="-9/110000"
assert states[4]["extension_m"]["exact"]=="399/55000"
assert states[5]["Nw_over_pi_N"]["exact"]=="-261000"

# Independent compatibility/equilibrium for equal-bore unequal wall/E members.
l1=l2=F(3); ea1=EA; ea2=F(100000000000)*F(69,40000)
nu1=nu; nu2=F(1,4)
nw=(l1*2*nu1*P/ea1+l2*2*nu2*P/ea2)/(l1/ea1+l2/ea2)
middle=l1*(nw-2*nu1*P)/ea1
assert nw==F(427000,157) and middle==F(-3,785000)
tip_free=l1*(P-2*nu1*P)/ea1+l2*(P-2*nu2*P)/ea2
assert tip_free==F(179,2530000)

summary = {
 "status":"frozen_independent_analytical_reference_before_new_pressure_source_read",
 "actor":"/root/numerical_policy_review","issuer":"/root/physics_manager","actual_harness_parent":"/root",
 "arithmetic":"Exact rational coefficients and Machin pi; no production helper/import/output used",
 "comparison_policy":{"nonzero":"absolute difference <=1e-9*abs(independent expected); no larger floor","zero":"absolute difference <=1e-9*independent same-dimension characteristic scale; zero scale requires exact zero","force_scale":"max(abs(P), abs(EA*thermal_strain), abs(total mechanical force))","moment_scale":"force_scale*component_length","stress_scale":"force_scale/wall_area","translation_scale":"component_length*max(abs(thermal_strain),abs(P/EA),abs(total_mechanical_force/EA))","rotation_scale":"translation_scale/component_length","scope":"New independent fixture comparisons only; not solver, contact, stability or protected old-reference tolerance changes"},
 "pi_approximation_absolute_error_less_than":"3e-142",
 "geometry_SI":{"L_m":6,"ri_m":0.05,"ro_m":0.06,"E_Pa":200000000000,"nu":0.3,"p_Pa":2000000},
 "area_over_pi_m2":value(As),"bore_area_over_pi_m2":value(Ai),"EA_over_pi_N":value(EA),"P_over_pi_N":value(P),
 "lame_radial_inner_outer_Pa":[value(F(-2000000)),value(F())],
 "lame_hoop_inner_outer_Pa":[value(F(122000000,11)),value(F(100000000,11))],
 "six_SI_states":states,
 "two_span":{"L1_m":3,"L2_m":3,"ro2_m":0.065,"E2_Pa":100000000000,"nu2":0.25,"ri_both_m":0.05,
   "free_mid_m":value(F(3,110000)),"free_tip_m":value(tip_free),
   "free_Nw_over_pi_N":value(P),"free_S_over_pi_N":value(F()),
   "fixed_Nw_over_pi_N":value(nw),"fixed_S_over_pi_N":value(nw-P),
   "fixed_mid_m":value(middle),"fixed_tip_m":value(F()),
   "fixed_support_pair_over_pi_N":[value(P-nw),value(nw-P)],
   "fixed_strains":[value((nw-2*nu1*P)/ea1),value((nw-2*nu2*P)/ea2)],
   "orientation_invariance":"Reverse either authored member or terminal order; physical vectors and tension-positive Nw/S remain unchanged. Local wall endpoint pair stays [-Nw,+Nw]."},
 "mixed_closures":[
   {"id":"LEFT_TRANSFER_RIGHT_SEPARATE_ROOT_ANCHOR","Nw_over_pi_N":value(F()),"S_over_pi_N":value(-P),"extension_m":value(F(-9,110000)),"root_reaction_over_pi_N":value(P)},
   {"id":"LEFT_SEPARATE_RIGHT_TRANSFER_ROOT_ANCHOR","Nw_over_pi_N":value(P),"S_over_pi_N":value(F()),"extension_m":value(F(3,55000)),"root_reaction_over_pi_N":value(-P)}],
 "distributed_axial":{"w_N_per_m":100,"L_m":6,"Nw_at_station":"5000*pi + 100*(6-x) N","S_at_station":"100*(6-x) N","wall_endpoint_actions_N":["-(5000*pi+600)","5000*pi"],
   "tip_extension_m":value(F(3,55000)+F(1800)/(EA*pi)),"root_reaction_N":-600,"station_x_m":[0,1.5,3,4.5,6],
   "wall_force_N":[value(P*pi+F(100)*(6-x)) for x in [F(),F(3,2),F(3),F(9,2),F(6)]],
   "membrane_Pa":[value((P*pi+F(100)*(6-x))/(As*pi)) for x in [F(),F(3,2),F(3),F(9,2),F(6)]]},
 "rotation":{"proper_basis_columns":[["1/3","2/3","2/3"],["-2/sqrt(5)","1/sqrt(5)","0"],["-2/(3*sqrt(5))","-4/(3*sqrt(5))","sqrt(5)/3"]],
   "rule":"All axial displacement/reaction vectors multiply t=(1,2,2)/3; local pressure scalars unchanged; pure-pressure global couples zero."},
 "limits":"Long straight homogeneous isotropic small-strain annulus, reference-geometry uniform internal pressure increment and zero exterior increment. Not curved, shell/end/interface stress, follower/prestress stability, flow momentum, nonlinear-contact or professional acceptance.",
}
(base/"FROZEN_RUNTIME_EXPECTATIONS.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps({"states":len(states),"two_span_fixed_wall_over_pi":str(nw),"two_span_fixed_middle":str(middle),"free_tip":str(tip_free),"output":str(base/"FROZEN_RUNTIME_EXPECTATIONS.json")},indent=2))
