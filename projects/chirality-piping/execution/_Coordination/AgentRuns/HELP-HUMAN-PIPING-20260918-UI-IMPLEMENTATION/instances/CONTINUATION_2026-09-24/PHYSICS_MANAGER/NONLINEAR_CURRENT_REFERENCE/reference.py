#!/usr/bin/env python3
"""Independent energy-assembled, Decimal arithmetic frame/Coulomb reference.
No product imports, binary execution, solver-output inputs, or adaptive tolerances.
All writes are restricted to this script's evidence directory.
"""
import copy, hashlib, json, platform, sys
from decimal import Decimal as D, getcontext
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'projects/chirality-piping/fixtures/product_preview/invented_preview_model.json').is_file())
PIP = ROOT/'projects/chirality-piping'
getcontext().prec = int(sys.argv[1]) if len(sys.argv)>1 else 60
PI = D('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
ZERO = D(0)
TINY = D('1e-40')  # reference branch/equilibrium classification only, not product acceptance

def read(path): return json.loads(path.read_text(), parse_float=D, parse_int=D)
def enc(v):
    if isinstance(v,D): return str(v)
    raise TypeError(type(v))
def dump(path, data): path.write_text(json.dumps(data,indent=2,default=enc)+'\n')
def dot(a,b): return sum((x*y for x,y in zip(a,b)),ZERO)
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def norm(a): return dot(a,a).sqrt()
def unit(a): return [x/norm(a) for x in a]
def vec(): return [ZERO]*30
def outer_add(K,a,b,c):
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: K[i][j]+=c*x*y

def projection(node,axis,rotation=False):
    a=vec(); a[6*node+(3 if rotation else 0):6*node+(6 if rotation else 3)]=axis; return a

def difference(a,b): return [x-y for x,y in zip(a,b)]

def gauss(A,b):
    A=[r[:]+[x] for r,x in zip(A,b)]; n=len(b)
    for i in range(n):
        p=max(range(i,n),key=lambda j:abs(A[j][i])); assert A[p][i]
        A[i],A[p]=A[p],A[i]
        for j in range(i+1,n):
            c=A[j][i]/A[i][i]
            for k in range(i+1,n+1): A[j][k]-=c*A[i][k]
            A[j][i]=ZERO
    x=[ZERO]*n
    for i in reversed(range(n)): x[i]=(A[i][n]-dot(A[i][i+1:n],x[i+1:]))/A[i][i]
    return x

m=read(HERE/'fixture_pressure_free_nodalized.json')
node_ids=[n['id'] for n in m['nodes']]
positions=[[n['position'][x] for x in 'xyz'] for n in m['nodes']]
pipes={p['id']:p for p in m['pipe_segments']}
material=m['materials'][0]; E=material['elastic_modulus']['value']; G=material['shear_modulus']['value']; alpha=material['thermal_expansion_coefficient']['value']
K=[[ZERO]*30 for _ in range(30)]
sections={}; orientation={}
for p in m['pipe_segments']:
    ni=node_ids.index(p['from']); nj=node_ids.index(p['to']); edge=difference(positions[nj],positions[ni]); L=norm(edge); x=unit(edge)
    yr=[p['y_reference'][s] for s in 'xyz']; y=unit(difference(yr,[dot(yr,x)*v for v in x])); z=cross(x,y)
    orientation[p['id']]=(ni,nj,L,x,y,z)
    od=p['section']['outside_diameter']['value']; wall=p['section']['wall_thickness']['value']; inner=od-2*wall
    area=PI*(od**2-inner**2)/4; I=PI*(od**4-inner**4)/64; J=2*I; sections[p['id']]=(area,I,J)
    # Axial and torsional strain energies: 1/2 EA/L (delta u.x)^2, 1/2 GJ/L (delta theta.x)^2.
    a=difference(projection(nj,x),projection(ni,x)); outer_add(K,a,a,E*area/L)
    a=difference(projection(nj,x,True),projection(ni,x,True)); outer_add(K,a,a,G*J/L)
    # For each bending plane, integrate EI/2 * (v''(s))^2 over 0<=s<=L.
    # Cubic Hermite curvature coefficients are linear in xi=s/L.
    # v''= [-6+12xi, L*(-4+6xi), 6-12xi, L*(-2+6xi)] / L^2 times [vi,theta_i,vj,theta_j].
    for transverse in [y,z]:
        b=cross(x,transverse)
        a=[projection(ni,transverse),projection(ni,b,True),projection(nj,transverse),projection(nj,b,True)]
        c=[(-D(6),D(12)),(-4*L,6*L),(D(6),-D(12)),(-2*L,6*L)]
        for i in range(4):
            for j in range(4):
                integral=c[i][0]*c[j][0]+(c[i][0]*c[j][1]+c[i][1]*c[j][0])/2+c[i][1]*c[j][1]/3
                outer_add(K,a[i],a[j],E*I*integral/L**3)
# Actual fixture EJ contract is six relative DOF springs in parallel with P-130 beam.
ej=next(c for c in m['components'] if c['kind']=='expansion_joint')
ni,nj,L,x,y,z=orientation[ej['geometry']['expansion_joint_pipe_ref']]; mods=ej['modifiers']
for axis,rotation,name in [(x,False,'axial'),(y,False,'lateral'),(z,False,'lateral'),(x,True,'torsional'),(y,True,'angular'),(z,True,'angular')]:
    a=difference(projection(nj,axis,rotation),projection(ni,axis,rotation)); outer_add(K,a,a,mods[name+'_stiffness_user_value']['value'])
fixed=set()
for s in m['supports']:
    if 'nonlinear' not in s:
        for dof in s['restraints']: fixed.add(6*node_ids.index(s['node'])+['UX','UY','UZ','RX','RY','RZ'].index(dof))
normal_dof=19; friction_dof=20; stop_dof=25; mu=D('0.01')

def linear(F,boundary):
    free=[i for i in range(30) if i not in boundary]; u=vec()
    for i,x in zip(free,gauss([[K[i][j] for j in free] for i in free],[F[i] for i in free])): u[i]=x
    r=[dot(row,u)-f for row,f in zip(K,F)]
    return u,r,free

def load_vector(case,variant):
    F=vec()
    for load in case['primitive_loads']:
        value=load['magnitude']['value']
        if variant=='reverse_z' and load['id'].split(':historical')[0] in ['load:L-100-Z','load:L-200-Z']: value=-value
        if variant=='reverse_all': value=-value
        if load['dimension']=='force':
            idx=6*node_ids.index(load['target']['node'])+['global_x','global_y','global_z'].index(load['direction']); F[idx]+=value
        elif load['category']=='thermal':
            pid=load['target']['pipe']; ni,nj,_,x,_,_=orientation[pid]; thrust=E*sections[pid][0]*alpha*value
            for i in range(3): F[6*ni+i]-=thrust*x[i]; F[6*nj+i]+=thrust*x[i]
        else: assert load['category']=='pressure' and not value
    return F

def explore(F):
    answers=[]; trials=[]
    for active in [True,False]:
        boundary=fixed|({stop_dof} if active else set())
        u0,r0,free=linear(F,boundary)
        unit_force=vec(); unit_force[friction_dof]=D(1); hu,hr,_=linear(unit_force,boundary)
        # A sticking branch additionally fixes the friction DOF.
        us,rs,_=linear(F,boundary|{friction_dof})
        admissible_stop = rs[stop_dof] < 0 if active else us[stop_dof] <= TINY
        if admissible_stop and abs(rs[friction_dof])<=mu*abs(rs[normal_dof]):
            answers.append(record(F,us,rs,active,'sticking',None,r0[normal_dof],hr[normal_dof]))
        for motion in [-D(1),D(1)]:
            for normal_sign in [-D(1),D(1)]:
                c=-motion*mu*normal_sign
                p=c*r0[normal_dof]/(1-c*hr[normal_dof])
                u=[a+p*b for a,b in zip(u0,hu)]
                # Reactions are against the original force vector, so friction reaction is p.
                r=[dot(row,u)-f for row,f in zip(K,F)]
                admissible_stop = r[stop_dof] < 0 if active else u[stop_dof] <= TINY
                admissible_normal=normal_sign*r[normal_dof]>0
                admissible_motion=motion*u[friction_dof]>0
                if admissible_stop and admissible_normal and admissible_motion:
                    assert abs(r[friction_dof]-p)<TINY
                    assert abs(abs(p)-mu*abs(r[normal_dof]))<TINY
                    answers.append(record(F,u,r,active,'sliding',p,r0[normal_dof],hr[normal_dof]))
        trials.append({'stop_active':active,'friction_free_u_z_m':u0[friction_dof],'source_reaction_without_friction_N':r0[normal_dof],'stop_reaction_without_friction_N':r0[stop_dof],'stop_displacement_without_friction_m':u0[stop_dof],'friction_unit_force_influence_on_source':hr[normal_dof],'sticking_trial_tangential_N':rs[friction_dof],'sticking_trial_source_N':rs[normal_dof]})
    assert len(answers)==1,(len(answers),answers)
    return {'unique_admissible_equilibrium':answers[0],'branch_trials':trials}

def record(F,u,r,active,state,p,a,b):
    allowed=fixed|({stop_dof} if active else set())|{friction_dof}
    residual=max(abs(r[i]) for i in range(30) if i not in allowed)
    assert residual<TINY
    assert r[friction_dof]*u[friction_dof] <= TINY
    return {'one_way_state':'active' if active else 'inactive','friction_state':state,'source_UY_reaction_N':r[normal_dof],'normal_magnitude_N':abs(r[normal_dof]),'friction_UZ_reaction_N':r[friction_dof],'friction_UZ_displacement_m':u[friction_dof],'stop_UY_reaction_N':r[stop_dof],'stop_UY_displacement_m':u[stop_dof],'source_affine_intercept_N':a,'source_affine_friction_influence':b,'free_equilibrium_residual_N_or_Nm':residual,'displacement_vector_m_rad':u,'reaction_vector_N_Nm':r,'applied_vector_N_Nm':F}

out={'method':'Independent Decimal cubic-Hermite strain-energy frame assembly and exhaustive admissible contact/Coulomb branch enumeration; no product execution','decimal_precision':getcontext().prec,'python':platform.python_version(),'units':'m, N, rad; 30-DOF ordering node fixture order x UX UY UZ RX RY RZ','sections':sections,'cases':{}}
for case in m['load_cases']:
    out['cases'][case['id']]={v:explore(load_vector(case,v)) for v in ['original','reverse_z','reverse_all']}
dump(HERE/f'reference_values_precision_{getcontext().prec}.json',out)
for case,variants in out['cases'].items():
    for variant,value in variants.items():
        r=value['unique_admissible_equilibrium']; print(case,variant,json.dumps({k:str(v) for k,v in r.items() if not isinstance(v,list)}))
