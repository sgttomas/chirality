"""T4-I12 binary64 plausibility probe for U3-SYS-DEMO-CONNECTOR-001 (informational, not a reference).

The same model is rebuilt here separately in binary64 and solved by partial-pivot Gaussian
elimination with no equilibration; the result is compared with the frozen reference under
the case's own criterion (relative 1e-9 with the zero-scale floors). It shows the criterion
is attainable by an ordinary binary64 solve with margin, and gives a second, independently
written assembly of the system.

Usage: python -I probe_binary64.py <u3_reference_cases.json>
"""
import json, sys, math
ref = json.load(open(sys.argv[1]))
E=2e11; nu=0.3; G=E/(2*(1+nu)); a=1.2e-5; OD=0.168; t=0.007
ro=OD/2; ri=ro-t; As=math.pi*t*(OD-t); I=As*(ro*ro+ri*ri)/4; J=2*I
N={'N-100':(0,0,0),'N-110':(3.2,0,0),'N-120':(3.2,2.4,0),'N-130':(7.6,2.4,0),'N-140':(7.6,2.4,2.2)}
ids=list(N)
P={'P-100':('N-100','N-110',(0,0,1)),'P-110':('N-110','N-120',(0,0,1)),'P-120':('N-120','N-130',(0,0,1))}
def sub(u,v): return [x-y for x,y in zip(u,v)]
def dot(u,v): return sum(x*y for x,y in zip(u,v))
def cr(u,v): return [u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
def nrm(u): l=math.sqrt(dot(u,u)); return [x/l for x in u]
def kloc(L):
    k=[[0.0]*12 for _ in range(12)]
    def s(i,j,v): k[i][j]=v; k[j][i]=v
    A_=E*As/L; T_=G*J/L
    s(0,0,A_);s(6,6,A_);s(0,6,-A_);s(3,3,T_);s(9,9,T_);s(3,9,-T_)
    z12,z6,z4,z2=12*E*I/L**3,6*E*I/L**2,4*E*I/L,2*E*I/L
    s(1,1,z12);s(1,5,z6);s(1,7,-z12);s(1,11,z6);s(5,5,z4);s(5,7,-z6);s(5,11,z2);s(7,7,z12);s(7,11,-z6);s(11,11,z4)
    s(2,2,z12);s(2,4,-z6);s(2,8,-z12);s(2,10,-z6);s(4,4,z4);s(4,8,z6);s(4,10,z2);s(8,8,z12);s(8,10,z6);s(10,10,z4)
    return k
def axes(xi,xj,yr):
    d=sub(xj,xi); L=math.sqrt(dot(d,d)); x=nrm(d); yc=sub(yr,[dot(yr,x)*c for c in x]); y=nrm(yc); z=cr(x,y); return L,[x,y,z]
def T12(R):
    T=[[0.0]*12 for _ in range(12)]
    for b in range(4):
        for i in range(3):
            for j in range(3): T[3*b+i][3*b+j]=R[i][j]
    return T
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(r) for r in zip(*A)]
K=[[0.0]*30 for _ in range(30)]; f=[0.0]*30
def dofs(n): b=6*ids.index(n); return list(range(b,b+6))
for p,(i,j,yr) in P.items():
    L,R=axes(N[i],N[j],yr); T=T12(R); kg=mm(mm(tr(T),kloc(L)),T); idx=dofs(i)+dofs(j)
    for a_,ia in enumerate(idx):
        for b_,ib in enumerate(idx): K[ia][ib]+=kg[a_][b_]
Q=[[0,0,-1],[0,1,0],[1,0,0]]; r=[0,0,2.2]
def S(v): return [[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]]
QT=tr(Q); I3=[[1,0,0],[0,1,0],[0,0,1]]; Z=[[0]*3 for _ in range(3)]
hr=[x/2 for x in r]
def hc(*bs): return [sum((list(b[i]) for b in bs),[]) for i in range(3)]
neg=lambda M:[[-x for x in r_] for r_ in M]
B=mm(QT,hc(neg(I3),S(hr),I3,S(hr)))+mm(QT,hc(Z,neg(I3),Z,I3))
Kc=[3.2e6,9e5,9e5,6.2e5,4.8e5,4.8e5]
Ke=[[sum(B[k][i]*Kc[k]*B[k][j] for k in range(6)) for j in range(12)] for i in range(12)]
idx=dofs('N-130')+dofs('N-140')
for a_,ia in enumerate(idx):
    for b_,ib in enumerate(idx): K[ia][ib]+=Ke[a_][b_]
sd=dofs('N-140')[2]; K[sd][sd]+=42000.0
def run(w,Fy,dT,Fx=0.0,My=0.0,Mz=0.0):
    f=[0.0]*30
    L,R=axes(N['N-120'],N['N-130'],(0,0,1)); wl=[dot(R[k],[0,0,w]) for k in range(3)]
    fl=[0.0]*12; fl[1]=fl[7]=wl[1]*L/2; fl[5]=wl[1]*L*L/12; fl[11]=-wl[1]*L*L/12
    fg=[sum(T12(R)[k][i]*fl[k] for k in range(12)) for i in range(12)]
    for a_,ia in enumerate(dofs('N-120')+dofs('N-130')): f[ia]+=fg[a_]
    f[dofs('N-140')[1]]+=Fy; f[dofs('N-140')[0]]+=Fx; f[dofs('N-140')[4]]+=My; f[dofs('N-140')[5]]+=Mz
    NT=E*As*a*dT
    for k in range(3): f[dofs('N-120')[k]]-=NT*R[0][k]; f[dofs('N-130')[k]]+=NT*R[0][k]
    rest=sorted(dofs('N-100')+[dofs('N-120')[0],dofs('N-120')[2],dofs('N-130')[1]])
    fr=[i for i in range(30) if i not in rest]
    A=[[K[i][j] for j in fr]+[f[i]] for i in fr]; n=len(fr)
    for c in range(n):
        p=max(range(c,n),key=lambda i:abs(A[i][c])); A[c],A[p]=A[p],A[c]
        for i in range(c+1,n):
            m=A[i][c]/A[c][c]
            if m: A[i]=[x-m*y for x,y in zip(A[i],A[c])]
    x=[0.0]*n
    for i in reversed(range(n)): x[i]=(A[i][n]-sum(A[i][j]*x[j] for j in range(i+1,n)))/A[i][i]
    d=[0.0]*30
    for k,v in zip(fr,x): d[k]=v
    dc=[d[i] for i in idx]; q=[sum(B[k][j]*dc[j] for j in range(12)) for k in range(6)]; g=[Kc[k]*q[k] for k in range(6)]
    R_=[sum(K[i][j]*d[j] for j in range(30))-f[i] for i in range(30)]
    return d,q,g,R_
worst=0.0
for case,args in {'load:L-100':(-190.0,350.0,12.5),'load:L-200':(-95.0,125.0,0.0),'load:L-300':(0.0,0.0,0.0,200.0,-80.0,150.0)}.items():
    d,q,g,R_=run(*args); e=ref['cases']['U3-SYS-DEMO-CONNECTOR-001']['expected'][case]
    qe=[float(s) for s in e['connector']['q_local']]; ge=[float(s) for s in e['connector']['g_local']]
    fl=e['zero_scale_floors']
    print(case,'q rel err (vs max(|exp|, max|q_t|)):',['%.1e'%(abs(a_-b_)/max(abs(b_),float(fl['q_translation_m']) if k<3 else float(fl['q_rotation_rad']))) for k,(a_,b_) in enumerate(zip(q,qe))])
    print(case,'g rel err (vs max(|exp|, floor)):',['%.1e'%(abs(a_-b_)/max(abs(b_),float(fl['g_force_N']) if k<3 else float(fl['g_moment_N_m']))) for k,(a_,b_) in enumerate(zip(g,ge))])
    du=[]
    for n in ids:
        for k in range(3):
            ex_=float(e['displacements']['node:'+n]['u_m'][k]); du.append(abs(d[dofs(n)[k]]-ex_)/max(abs(ex_),float(fl['translation_m'])))
    print(case,'max displacement rel err', '%.1e'%max(du))
    rr=[]
    for sid,(n,ks) in {'support:S-100':('N-100',range(6)),'support:S-120':('N-120',[0,2]),'support:S-130':('N-130',[1])}.items():
        for k in ks:
            ex_=float(e['reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz'][sid][k]); fam=float(fl['force_N']) if k<3 else float(fl['moment_N_m'])
            rr.append(abs(R_[dofs(n)[k]]-ex_)/max(abs(ex_),fam))
    print(case,'max reaction rel err','%.1e'%max(rr))
    worst=max(worst,max(rr),max(du))
print('worst normalized error over displacements and reactions: %.1e (criterion 1e-9)'%worst)
print('PASS' if worst<=1e-9 else 'FAIL')
