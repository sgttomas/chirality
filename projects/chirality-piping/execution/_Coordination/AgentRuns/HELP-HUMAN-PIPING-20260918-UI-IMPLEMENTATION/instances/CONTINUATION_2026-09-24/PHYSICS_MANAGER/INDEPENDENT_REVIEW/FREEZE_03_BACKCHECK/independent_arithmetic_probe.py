"""Independent exact-rational source identity/physics checks; Python only, no product execution."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import struct,math,random,json
OUT=Path(__file__).resolve().parent
PM=OUT.parent.parent
SG=PM/'SECTION_GEOMETRY'
q=lambda x:Q.from_float(x)
bits=lambda x:struct.pack('>d',x).hex()
def key(od,t):
 a=od*.5;x=a-t;bv=a-x;av=x+bv;y=(a-av)+(bv-t)
 return x,0.0 if y==0.0 else y
random.seed(314159)
count=0;keymap={}
for _ in range(6000):
 od=math.ldexp(random.uniform(1,2),random.randint(-240,240))
 t=od*random.uniform(2**-51,.49)
 hi,lo=key(od,t)
 assert q(hi)+q(lo)==q(od)/2-q(t)
 k=(bits(hi),bits(lo));exact=q(od)/2-q(t)
 assert k not in keymap or keymap[k]==exact
 keymap[k]=exact;count+=1
# Distinct authored sources with the same exact bore must share one pressure factor.
assert key(.15625,.015625)==key(.1875,.03125)
# Equal rounded radii need not share an exact authored bore.
a=(.12,1e-12);b=(.12,math.nextafter(1e-12,math.inf))
assert key(*a)[0]==key(*b)[0] and key(*a)[1]!=key(*b)[1]
# Independently derive serial free span equilibrium and isotropic compatibility.
two=json.loads((SG/'NEAR_TWO_SPAN_EXPECTATIONS.json').read_text())
I=two['inputs']; nu1=q(struct.unpack('>d',bytes.fromhex(I['nu1_bits_hex']))[0]);nu2=q(struct.unpack('>d',bytes.fromhex(I['nu2_bits_hex']))[0])
p=q(I['p_Pa']);ri=q(I['ri_m']);a1=q(I['OD1_m'])/2;a2=q(I['OD2_m'])/2
# Pi cancels in displacement; the force reference contains its separately bounded rational pi.
d1=(1-2*nu1)*p*ri**2*q(I['L1_m'])/(q(I['E1_Pa'])*(a1*a1-ri*ri))
d2=(1-2*nu2)*p*ri**2*q(I['L2_m'])/(q(I['E2_Pa'])*(a2*a2-ri*ri))
assert d1==Q(two['span1_extension_m']['exact_rational_with_bounded_pi'])
assert d2==Q(two['span2_extension_m']['exact_rational_with_bounded_pi'])
P=Q(two['wall_force_N']['exact_rational_with_bounded_pi'])
rhs=[-(1-2*nu1)*P,2*(nu2-nu1)*P,(1-2*nu2)*P]
assert sum(rhs)==0
assert rhs==[Q(v['exact_rational_with_bounded_pi']) for v in two['source_global_axial_rhs_N']]
fixed=json.loads((SG/'NEAR_FIXED_EXPECTATIONS.json').read_text());near=json.loads((SG/'NEAR_INCOMPRESSIBLE_EXPECTATIONS.json').read_text())
for c,n in zip(fixed['cases'],near['cases']):
 nu=q(struct.unpack('>d',bytes.fromhex(c['nu_bits_hex']))[0]);P=Q(n['source_pressure_cap_N']['exact_rational_with_bounded_pi'])
 assert Q(c['wall_force_N']['exact_rational_with_bounded_pi'])==2*nu*P
 assert Q(c['effective_force_N']['exact_rational_with_bounded_pi'])==(2*nu-1)*P
 assert Q(c['left_support_Fx_N']['exact_rational_with_bounded_pi'])==(1-2*nu)*P
 assert Q(c['right_support_Fx_N']['exact_rational_with_bounded_pi'])==-(1-2*nu)*P
# Orthogonal, determinant-positive coordinate basis using a scaled y/z pair; exact dot and cross.
x=[Q(1,3),Q(2,3),Q(2,3)];y=[Q(-2),Q(1),Q()];z=[Q(-2,3),Q(-4,3),Q(5,3)]
dot=lambda a,b:sum((u*v for u,v in zip(a,b)),Q())
cross=lambda a,b:[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
assert dot(x,x)==1 and dot(y,y)==dot(z,z)==5 and dot(x,y)==dot(x,z)==dot(y,z)==0 and cross(x,y)==z
# Independent arithmetic counterexample for dividing a published subnormal wall force.
# This diagnoses a caller expression, not actual public-model reachability.
od=q(4e-77);t=q(1e-77);pressure=q(4.7e-170);nu=q(.1);pi=q(math.pi)
area=pi*t*(od-t);bore=pi*(od/2-t)**2;wall=2*nu*pressure*bore
membrane=float(wall/area);published_wall=float(wall);redivided=published_wall/float(area)
assert membrane!=0 and abs(redivided/membrane-1)>0.1
record={'actor':'/root/c4_resume/startup_full_review','actual_parent':'/root/c4_resume','assignment_integrator':'/root','method':'Independent Python Fraction algebra, IEEE binary64 via Python float, deterministic source-key arithmetic; no Rust/public product run','source_bore_identity_cases':count,'same_exact_bore_grouping':True,'same_rounded_bore_distinct_source_keys':True,'two_span_reference_exact_agreement':True,'fixed_reference_exact_agreement':True,'proper_rotation_exact_agreement':True,'membrane_publication_arithmetic':{'scope':'Expression-level counterexample only; public path unverified by this reviewer','OD_m':float(od),'wall_m':float(t),'p_Pa':float(pressure),'nu':float(nu),'wall_published_N':published_wall,'stable_membrane_Pa':membrane,'redivided_membrane_Pa':redivided,'relative_error':redivided/membrane-1},'limits':['Source-key arithmetic agreement does not qualify rounded pressure products or solver conditioning.','The 32epsilon normwise cancellation screen is an admission screen, not a universal per-component or subnormal forward-error proof.','No source/test edits and no model execution.']}
(OUT/'independent_arithmetic_probe.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
