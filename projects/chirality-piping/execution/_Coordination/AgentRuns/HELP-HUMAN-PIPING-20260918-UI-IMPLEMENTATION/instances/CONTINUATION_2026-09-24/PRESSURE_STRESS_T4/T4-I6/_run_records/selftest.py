"""T4-I6 cross-check: the element against CB's quarter-circle longhand (curved_bend/src/lib.rs:1093-1175@ed012c7ccf, a labelled cross-check) and against an independent Gauss-Legendre quadrature; symmetry and rigid modes."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import curved_ref as C
getcontext().prec = 110
t0=time.time()
# CB toy quarter circle: centre origin, i=(2,0,0), j=(0,2,0); y_ref = bow (1,1,0)
E,G,A,I,J = 100.0,40.0,3.0,5.0,7.0
for kin,kout in ((1.0,1.0),(2.5,1.75)):
    el = C.curved_element([2.0,0,0],[0,2.0,0],2.0,[1.0,1.0,0.0],E,G,A,I,J,kin,kout)
    g = el["geo"]
    print("phi-pi/2", C.sci(g["phi"]-C.pi()/2,5), "axes", [[C.sig(v,6) for v in a] for a in g["axes"]])
    F = el["F"]; pi = C.pi(); r=D(2)
    EI=D(E)*D(I); EA=D(E)*D(A); GJ=D(G)*D(J)
    fxx = D(kin)*r**3*(D(3)*pi/4-2)/EI + r*(pi/4)/EA
    fxy = D(kin)*r**3*D("0.5")/EI - r*D("0.5")/EA
    fxm = D(kin)*r*r*(1-pi/2)/EI
    fyy = D(kin)*r**3*(pi/4)/EI + r*(pi/4)/EA
    fym = -D(kin)*r*r/EI
    fmm = D(kin)*r*(pi/2)/EI
    c1=pi/4; c2=D(3)*pi/4-2
    fzz = r**3*(D(kout)*c1/EI + c2/GJ)
    fzx = r*r*(D(kout)*c1/EI + (pi/4-1)/GJ)
    fzy = r*r*(D(kout)*D("0.5")/EI + D("0.5")/GJ)
    fxx2 = r*(D(kout)*c1/EI + c1/GJ); fxy2 = r*(D(kout)*D("0.5")/EI - D("0.5")/GJ); fyy2 = r*(D(kout)*c1/EI + c1/GJ)
    exp = {(0,0):fxx,(0,1):fxy,(0,5):fxm,(1,1):fyy,(1,5):fym,(5,5):fmm,(2,2):fzz,(2,3):fzx,(2,4):fzy,(3,3):fxx2,(3,4):fxy2,(4,4):fyy2,
           (0,2):D(0),(0,3):D(0),(0,4):D(0),(1,2):D(0),(1,3):D(0),(1,4):D(0),(2,5):D(0),(3,5):D(0),(4,5):D(0)}
    worst = max(abs(F[a][b]-v) for (a,b),v in exp.items())
    print("k",kin,kout,"max |F - longhand| =", C.sci(worst,3), " max|F|", C.sci(C.max_abs(F),5))
    Fq = C.flexibility_by_quadrature(2.0, g["phi"], E,G,A,I,J,kin,kout, n=40)
    print("   quadrature vs closed form max diff", C.sci(max(abs(F[a][b]-Fq[a][b]) for a in range(6) for b in range(6)),3))
    K = el["K"]
    sym = max(abs(K[i][j]-K[j][i]) for i in range(12) for j in range(12))
    res = max(max(abs(v) for v in C.matvec(K,m)) for _,m in C.rigid_modes([2.0,0,0],[0,2.0,0]))
    print("   sym", C.sci(sym,3), "rigid residual", C.sci(res,3), "max|K|", C.sci(C.max_abs(K),6))
