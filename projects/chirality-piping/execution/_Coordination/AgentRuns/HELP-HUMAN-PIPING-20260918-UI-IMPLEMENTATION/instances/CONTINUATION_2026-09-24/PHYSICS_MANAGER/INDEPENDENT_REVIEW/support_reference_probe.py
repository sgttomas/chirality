"""Independent exact force/moment balance and parallel-spring reference checks."""
from fractions import Fraction as F
from pathlib import Path
import json
R=[[F(x,3) for x in row] for row in [[2,-2,1],[1,2,2],[-2,-1,2]]]
rot=lambda v:[sum(R[i][j]*v[j] for j in range(3)) for i in range(3)]
cross=lambda a,b:[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
det=R[0][0]*(R[1][1]*R[2][2]-R[1][2]*R[2][1])-R[0][1]*(R[1][0]*R[2][2]-R[1][2]*R[2][0])+R[0][2]*(R[1][0]*R[2][1]-R[1][1]*R[2][0])
assert det==1
assert all(sum(R[k][i]*R[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
f=[F(1000),F(2000),F(-3000)];m=[F(400),F(-500),F(600)];r=[F(1),F(0),F(0)]
rf=[-x for x in f];rm=[-a-b for a,b in zip(m,cross(r,f))]
assert rm==[-400,-2500,-2600]
assert [-x for x in rot(f)]==rot(rf)
assert [-a-b for a,b in zip(rot(m),cross(rot(r),rot(f)))]==rot(rm)
# Divide all three parallel stiffnesses by k=EA/L; u*k=F/(1+1+2).
loads=[F(-1000,4),F(-1000,4),F(-1000,2)];assert sum(loads)==-1000
result={"method":"Exact Fraction orthogonality/determinant, root moment balance -(M+r cross F), transformed vector balance and normalized parallel stiffness fractions. No product import.","rotation_proper":True,"root_force_N":list(map(str,rf)),"root_moment_Nm":list(map(str,rm)),"rotated_root_force_N":list(map(str,rot(rf))),"rotated_root_moment_Nm":list(map(str,rot(rm))),"root_spring1_spring2_force_N":list(map(str,loads)),"pass":True,"timing":"Independent check during review, after public tests were authored; not a prior ASSEMBLY_ORACLE freeze claim"}
(Path(__file__).parent/"support_reference_probe.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"rotation_and_balance":True,"spring_partition":True}))
