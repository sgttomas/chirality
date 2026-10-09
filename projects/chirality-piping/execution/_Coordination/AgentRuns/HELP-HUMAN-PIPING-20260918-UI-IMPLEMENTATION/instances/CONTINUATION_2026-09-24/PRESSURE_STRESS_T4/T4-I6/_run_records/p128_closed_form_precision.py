"""T4-I6: accuracy of the closed-form flexibility evaluated at about 128-bit (decimal 34/38) and 50-digit precision at small angles, against 110 digits (for K-D5's p = 128 re-formation)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext, localcontext
import curved_ref as C
E,G,A,I,J = 2e11,8e10,0.005969026041820614,2.700984283923829e-05,5.401968567847658e-05
g30=2.0**-30
def gr(v): return round(v/g30)*g30
d=[gr(0.3*math.cos(math.pi/6)), gr(0.3*math.sin(math.pi/6)), 0.0]
for phi in (1e-2,1e-4,1e-6,1e-8,1e-9):
    with localcontext() as c:
        c.prec=60
        L=C.norm([C.dec(v) for v in d]); R=float(L/(2*C.sin(C.dec(phi)/2)))
    res={}
    for p in (34,38,50,110):
        getcontext().prec=p
        el=C.curved_element([0.0,0,0],d,R,[0.0,1.0,0.0],E,G,A,I,J,1.0,1.0)
        res[p]=el
    getcontext().prec=110
    ref=res[110]["K"]; sc=C.max_abs(ref)
    out=[]
    for p in (34,38,50):
        dk=max(abs(res[p]["K"][i][j]-ref[i][j]) for i in range(12) for j in range(12))/sc
        df=max(abs(res[p]["F"][i][j]-res[110]["F"][i][j])/abs(res[110]["F"][i][i]*res[110]["F"][j][j]).sqrt() for i in range(6) for j in range(6))
        out.append("p%d: K %s F %s"%(p,C.sci(dk,2),C.sci(df,2)))
    print("phi",phi," ; ".join(out))
