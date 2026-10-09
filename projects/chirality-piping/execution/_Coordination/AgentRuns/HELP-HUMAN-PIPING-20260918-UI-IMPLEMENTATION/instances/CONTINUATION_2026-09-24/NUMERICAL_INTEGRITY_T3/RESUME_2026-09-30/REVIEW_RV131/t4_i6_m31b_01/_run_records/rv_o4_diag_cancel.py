"""RV131 O4 diagnostic: which flexibility part carries the closed form's u/phi^3 loss (decimal 38 digits against 110, T4-I6's curved_ref in DIR, labelled).
usage: python -I rv_o4_diag_cancel.py T4I6_RUN_RECORDS_DIR"""
import sys, math
sys.path.insert(0, sys.argv[1])
from decimal import Decimal as D, getcontext, localcontext
import curved_ref as C
E,G,A,I,J = 2e11,8e10,0.005969026041820614,2.700984283923829e-05,5.401968567847658e-05
g30=2.0**-30
def gr(v): return round(v/g30)*g30
d=[gr(0.3*math.cos(math.pi/6)), gr(0.3*math.sin(math.pi/6)), 0.0]
for phi in (1e-6,1e-8,1e-9):
    with localcontext() as c:
        c.prec=60
        L=C.norm([C.dec(v) for v in d]); R=float(L/(2*C.sin(C.dec(phi)/2)))
    res={}
    for p in (38,110):
        getcontext().prec=p
        geo=C.geometry([C.dec(0.0)]*3,[C.dec(v) for v in d],R,[D(0),D(1),D(0)])
        parts=C.flexibility_parts(geo,C.dec(E),C.dec(G),C.dec(A),C.dec(I),C.dec(J))
        F=C.flexibility(geo,C.dec(E),C.dec(G),C.dec(A),C.dec(I),C.dec(J),D(1),D(1))
        res[p]=(geo,parts,F)
    getcontext().prec=110
    g38,p38,F38=res[38]; g110,p110,F110=res[110]
    print("phi",phi,"phi err",C.sci((g38['phi']-g110['phi'])/g110['phi'],3),"cosp err",C.sci(g38['cosp']-g110['cosp'],3), "1-cosp rel", C.sci(((1-g38['cosp'])-(1-g110['cosp']))/(1-g110['cosp']),3))
    for key in ("Mip","Mop","T","N"):
        worst=(D(0),None)
        for a in range(6):
            for b in range(6):
                den=(abs(F110[a][a]*F110[b][b])).sqrt()
                e=abs(p38[key][a][b]-p110[key][a][b])/den
                if e>worst[0]: worst=(e,(a,b))
        print("  part",key,"worst diag-scaled err",C.sci(worst[0],3),"at",worst[1])
