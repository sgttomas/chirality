"""Independent rational assembly/reference checks; never imports product code."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext
import json, hashlib, datetime, platform
out=Path(__file__).resolve().parent
reference=out.parent/"ASSEMBLY_ORACLE/FROZEN_RUNTIME_EXPECTATIONS.json"
data=json.loads(reference.read_text())

def solve_axial(lengths, areas_over_pi, moduli, nus, pressure_force_over_pi, thermal, transfer, fixed):
    # Independent 1D weak-form assembly, with every force/stiffness divided by pi.
    n=len(lengths)+1; K=[[Q(0) for _ in range(n)] for _ in range(n)]; rhs=[Q(0) for _ in range(n)]; eigen=[]
    for i,(L,A,E,nu,aT) in enumerate(zip(lengths,areas_over_pi,moduli,nus,thermal)):
        k=E*A/L; ep=E*A*aT-2*nu*pressure_force_over_pi
        K[i][i]+=k;K[i+1][i+1]+=k;K[i][i+1]-=k;K[i+1][i]-=k
        rhs[i]-=ep;rhs[i+1]+=ep;eigen.append((-ep,ep))
    rhs[0]-=pressure_force_over_pi if transfer[0] else 0
    rhs[-1]+=pressure_force_over_pi if transfer[1] else 0
    free=[i for i in range(n) if i not in fixed]; A=[[K[i][j] for j in free]+[rhs[i]] for i in free]
    for col in range(len(free)):
        pivot=next(row for row in range(col,len(free)) if A[row][col]);A[col],A[pivot]=A[pivot],A[col]
        v=A[col][col];A[col]=[x/v for x in A[col]]
        for row in range(len(free)):
            if row!=col:
                v=A[row][col];A[row]=[x-v*y for x,y in zip(A[row],A[col])]
    u=[Q(0) for _ in range(n)]
    for j,i in enumerate(free):u[i]=A[j][-1]
    reaction=[sum(K[i][j]*u[j] for j in range(n))-rhs[i] for i in range(n)]
    wall=[E*A*(u[i+1]-u[i])/L-eigen[i][1] for i,(L,A,E) in enumerate(zip(lengths,areas_over_pi,moduli))]
    assert all(reaction[i]==0 for i in free)
    return u,reaction,wall

checks=[];P=Q(5000);As=Q(11,10000);E=Q(200000000000);nu=Q(3,10)
for row in data["six_SI_states"]:
    aT=Q(row["thermal_strain"]["exact"]);fixed={0,1} if row["restrained_axially"] else {0}
    transfer=(row["both_closures_transfer"],)*2
    u,reaction,wall=solve_axial([Q(6)],[As],[E],[nu],P,[aT],transfer,fixed)
    assert u[-1]==Q(row["extension_m"]["exact"])
    assert wall[0]==Q(row["Nw_over_pi_N"]["exact"])
    assert wall[0]-P==Q(row["S_over_pi_N"]["exact"])
    assert reaction==[Q(x["exact"]) for x in row["support_pair_over_pi_N"]]
    assert wall[0]/As==Q(row["axial_membrane_Pa"]["exact"])
    checks.append({"id":row["id"],"u_m":list(map(str,u)),"reaction_over_pi_N":list(map(str,reaction)),"wall_over_pi_N":list(map(str,wall)),"pass":True})
for fixed in [False,True]:
    u,r,w=solve_axial([Q(3),Q(3)],[As,Q(69,40000)],[E,Q(100000000000)],[nu,Q(1,4)],P,[Q(0),Q(0)],(True,True),{0,2} if fixed else {0})
    prefix="fixed" if fixed else "free"; ref=data["two_span"]
    assert u[1]==Q(ref[prefix+"_mid_m"]["exact"]);assert u[2]==Q(ref[prefix+"_tip_m"]["exact"])
    assert all(x==Q(ref[prefix+"_Nw_over_pi_N"]["exact"]) for x in w)
    checks.append({"id":"two_span_"+prefix,"u_m":list(map(str,u)),"reaction_over_pi_N":list(map(str,r)),"wall_over_pi_N":list(map(str,w)),"pass":True})
for j,transfer in enumerate([(True,False),(False,True)]):
    row=data["mixed_closures"][j];u,r,w=solve_axial([Q(6)],[As],[E],[nu],P,[Q(0)],transfer,{0})
    assert u[-1]==Q(row["extension_m"]["exact"]);assert r[0]==Q(row["root_reaction_over_pi_N"]["exact"]);assert w[0]==Q(row["Nw_over_pi_N"]["exact"])
    checks.append({"id":row["id"],"u_m":list(map(str,u)),"reaction_over_pi_N":list(map(str,r)),"wall_over_pi_N":list(map(str,w)),"pass":True})
# Direct traction/compliance reductions, independent of the implementation.
ri=Q(1,20);ro=Q(3,50);p=Q(2000000);C=p*ri**2/(ro**2-ri**2);B=C*ro**2
assert [C-B/r**2 for r in [ri,ro]]==[Q(x["exact"]) for x in data["lame_radial_inner_outer_Pa"]]
assert [C+B/r**2 for r in [ri,ro]]==[Q(x["exact"]) for x in data["lame_hoop_inner_outer_Pa"]]
with localcontext() as ctx:
    ctx.prec=80;t=(D(6)-D(2).sqrt())/D(8);b=D(4)*t*(1-t);c=t
    derivative=D(2)*t*(D(32)*t*t-D(48)*t+D(17))
    value=D(1000000)*(b*b+c*c).sqrt();expected=D(1000000)*(D(71)+D(8)*D(2).sqrt()).sqrt()/D(8)
    assert abs(derivative)<D('1e-70');assert abs(value-expected)<D('1e-65')
    assert value>D(1000000)*D(325).sqrt()/D(16)
    x1={"t":str(t),"value_pa":str(value),"derivative_residual":str(derivative),"old_candidate_upper_pa":str(D(1000000)*D(325).sqrt()/D(16)),"pass":True}
result={"method":"Independent Fraction assembled axial K, eigen and cap ledgers, Gaussian elimination; direct traction algebra;80-digit Decimal X1 differentiation/evaluation. No product import or runtime invocation.","python":platform.python_version(),"recorded_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"reference_sha256":hashlib.sha256(reference.read_bytes()).hexdigest(),"assembly_cases":checks,"lame_surface_check":True,"x1":x1,"limits":"Independent reference arithmetic only; no native/product execution, no solver/coefficient error certification or engineering acceptance."}
(out/"independent_reference_probe.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"assembly_cases":len(checks),"lame_surface_check":True,"x1_pass":True}))
