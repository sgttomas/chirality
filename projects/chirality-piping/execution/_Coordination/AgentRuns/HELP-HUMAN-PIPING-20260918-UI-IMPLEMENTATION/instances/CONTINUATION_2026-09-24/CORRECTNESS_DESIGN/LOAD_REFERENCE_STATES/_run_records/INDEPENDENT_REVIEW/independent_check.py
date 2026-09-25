#!/usr/bin/env python3
"""Reviewer-owned analytical checks, without product or author-oracle imports."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
findings = {}

def solve(matrix, rhs):
    """Small exact elimination, independent of the product linear algebra."""
    aug = [[Q(x) for x in row] + [Q(b)] for row, b in zip(matrix, rhs)]
    for col in range(len(rhs)):
        row = next(r for r in range(col, len(rhs)) if aug[r][col])
        aug[row], aug[col] = aug[col], aug[row]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(len(rhs)):
            if row != col:
                scale = aug[row][col]
                aug[row] = [x - scale*y for x,y in zip(aug[row], aug[col])]
    return [r[-1] for r in aug]

def product(matrix, vector):
    return [sum(a*b for a,b in zip(row,vector)) for row in matrix]

# 1: Assemble both bar energies, eliminate the prescribed coordinates.
k1, k2 = Q(200_000_000), Q(100_000_000)
K = [[k1,-k1,0],[-k1,k1+k2,-k2],[0,-k2,k2]]
g = Q(1,10_000)
u = [g, solve([[K[1][1]]],[-K[1][0]*g])[0], Q(0)]
reaction = product(K,u)
assert u[1] == Q(1,15_000)
assert reaction == [Q(20_000,3),0,-Q(20_000,3)]
assert product(K,[g,0,0])[1] == -20_000
findings['axial_boundary'] = {'u':u,'support_actions':reaction}

# 2: Obtain beam reactions from the interpolating cubic and its derivatives,
# rather than taking the author's stiffness-row formula as the oracle.
L, EI, theta = Q(2),Q(2000),Q(1,1000)
a,b,c,d = solve([[1,0,0,0],[0,1,0,0],
                  [1,L,L**2,L**3],[0,1,2*L,3*L**2]], [0,theta,0,0])
actions = [EI*6*d,-EI*2*c,-EI*6*d,EI*(2*c+6*d*L)]
assert actions == [3,4,-3,2]
assert actions[0]+actions[2] == 0
assert actions[1]+actions[3]+L*actions[2] == 0
free_coefficients = solve([[1,0,0,0],[0,1,0,0],
                           [0,0,2,6*L],[0,0,0,6]],[0,theta,0,0])
assert free_coefficients == [0,theta,0,0]
findings['rotation'] = {'cubic_coefficients':[a,b,c,d],
                       'support_actions':actions,'free_tip_m':theta*L}

# 3: Compatibility and equilibrium for two parallel rods with unequal state E.
cold_k,hot_k,hot_free_extension = Q(200_000_000),Q(100_000_000),Q(1,1000)
u,Nc,Nh = solve([[cold_k,-1,0],[hot_k,0,-1],[0,1,1]],
                [0,hot_k*hot_free_extension,0])
assert [u,Nc,Nh] == [Q(1,3000),Q(200_000,3),-Q(200_000,3)]
findings['element_material_states'] = {'u':u,'cold_N':Nc,'hot_N':Nh}

# 4: Starting with independently chosen physical lengths at each temperature
# also verifies invariance under a change of coefficient datum.
datum_length = Q(10)
installation_length = datum_length*(1+Q(12,1_000_000)*30)
operating_length = datum_length*(1+Q(16,1_000_000)*130)
extension_ratio = (operating_length-installation_length)/installation_length
assert extension_ratio == Q(43,25009)
arbitrary_new_datum_length = Q(9)
assert (operating_length/arbitrary_new_datum_length)/(
    installation_length/arbitrary_new_datum_length)-1 == extension_ratio
assert extension_ratio != Q(16,1_000_000)*100
findings['coefficient_datum'] = {'engineering_strain':extension_ratio}

# 5: Integrate a_ref or a_log as declared. Split/reverse interval identities.
def coefficient_integral(start,end):
    # alpha(t) = 1e-5 + t*1e-7 for t in [0,100].
    return Q(1,100_000)*(end-start)+Q(1,20_000_000)*(end**2-start**2)
total = coefficient_integral(Q(0),Q(100))
left,right = coefficient_integral(Q(0),Q(30)),coefficient_integral(Q(30),Q(100))
assert total == Q(3,2000) and left+right == total
assert coefficient_integral(Q(100),Q(0)) == -total
with localcontext() as ctx:
    ctx.prec = 80
    dec = lambda q: Decimal(q.numerator)/Decimal(q.denominator)
    stretch = dec(total).exp()
    error = abs(dec(left).exp()*dec(right).exp()-stretch)
    assert error < Decimal('1e-78')
    assert stretch-1 > dec(total)
    log_engineering = str(stretch-1)
findings['differential_meaning'] = {'datum_length_strain':total,
    'log_length_engineering_strain_decimal':log_engineering}

# 6: Natural-length mismatch composed with free thermal length, then the
# expressly chosen small-strain assembly-reference constitutive law.
assembly_length = Q(10)
natural_cold_length = Q(9998,1000)
natural_hot_length = natural_cold_length*(1+Q(8,10_000))
epsilon_hot = (natural_hot_length-assembly_length)/assembly_length
cold_N = Q(200_000_000)*(assembly_length-natural_cold_length)/assembly_length
hot_N = Q(150_000_000)*(assembly_length-natural_hot_length)/assembly_length
assert cold_N == 40_000 and hot_N == -89_976
assert epsilon_hot == Q(3749,6_250_000)
released_u = natural_cold_length-assembly_length
assert released_u == -Q(2,1000)
# A natural-length denominator is a different constitutive approximation;
# do not claim that the first-order law is an exact finite-length rod law.
natural_reference_cold_N = Q(200_000_000)*(
    assembly_length-natural_cold_length)/natural_cold_length
assert natural_reference_cold_N != cold_N
findings['fit'] = {'cold_N':cold_N,'hot_N':hot_N,'released_u':released_u,
    'different_natural_reference_cold_N':natural_reference_cold_N}

# 7: Cross-sectional area integrals and whole-cantilever balance; pi symbolic.
ro,ri = Q(1,20),Q(1,25)
metal_area_over_pi,fluid_area_over_pi = ro**2-ri**2,ri**2
mass_over_pi = 7000*metal_area_over_pi+900*fluid_area_over_pi
weight_over_pi = -10*mass_over_pi
root_F_over_pi,root_M_over_pi = -weight_over_pi*2,-weight_over_pi*2**2/2
assert [mass_over_pi,weight_over_pi,root_F_over_pi,root_M_over_pi] == [
    Q(774,100),-Q(774,10),Q(1548,10),Q(1548,10)]
wall_pressure_over_pi = 2_000_000*fluid_area_over_pi
assert wall_pressure_over_pi == 3200
changed_q_over_pi = -10*(7000*metal_area_over_pi+100*fluid_area_over_pi)
assert changed_q_over_pi == -Q(646,10)
findings['hydrotest'] = {'q_over_pi':weight_over_pi,'root_F_over_pi':root_F_over_pi,
    'root_M_over_pi':root_M_over_pi,'wall_pressure_N_over_pi':wall_pressure_over_pi,
    'changed_q_over_pi':changed_q_over_pi}

# 8: The rigid replacement returns assembly action. An explicit internal
# spring-plus-lock model can partition it, but their sum cannot be applied twice.
k,ks,preload,load = Q(1000),Q(500),Q(100),Q(-1000)
u,structure,hanger = solve([[k,1,0],[ks,0,1],[0,1,1]],
                          [0,preload,-load])
assert [u,structure,hanger] == [-Q(3,5),600,400]
lock_position = Q(0)
locked_assembly = -load+k*lock_position
retained_spring = preload-ks*lock_position
pin_only = locked_assembly-retained_spring
assert [locked_assembly,retained_spring,pin_only] == [1000,100,900]
# Locking at the active predecessor needs no additional pin force initially.
predecessor_locked_assembly = -load+k*u
predecessor_retained_spring = preload-ks*u
assert predecessor_locked_assembly == predecessor_retained_spring == 400
findings['lock_attribution'] = {'active_u':u,'total_locked_action':locked_assembly,
    'retained_spring_if_modeled':retained_spring,'pin_if_modeled':pin_only,
    'at_predecessor_pin_if_modeled':predecessor_locked_assembly-predecessor_retained_spring}

# 9: Affine loading requires the persistent source exactly once.
physical = (Q(-1000)+200+100)/1000
sum_of_totals = (Q(-1000)+100)/1000+(Q(200)+100)/1000
assert physical == -Q(7,10) and sum_of_totals == -Q(3,5)
findings['source_participation'] = {'physical_u':physical,'wrong_sum_u':sum_of_totals}

# 10: Solve each slider equilibrium with explicit stick/slip branch checks.
slip = Q(0)
path=[]
for g in [Q(0),Q(3,1000),Q(0)]:
    trial = 1000*(g-slip)
    if trial > 1:
        force,slip = Q(1),g-Q(1,1000)
    elif trial < -1:
        force,slip = Q(-1),g+Q(1,1000)
    else:
        force = trial
    assert force == 1000*(g-slip) and abs(force) <= 1
    path.append({'position':g,'slip':slip,'force':force})
assert path[-1] == {'position':Q(0),'slip':Q(1,1000),'force':Q(-1)}
findings['history'] = path

# 11: Root-supplied hydrostatic counterexample, independently reconstructed
# from cap tractions and differential balance. z is upward from the bottom.
H, A, rho, gravity, ptop = Q(10),Q(1,100),Q(1000),Q(10),Q(100_000)
pbottom = ptop+rho*gravity*H
weight = rho*gravity*A*H
bottom_cap, top_cap = -pbottom*A,ptop*A
root_action = -(bottom_cap+top_cap)
assert weight == root_action == 1000
wall_N = pbottom*A  # no axial traction on frictionless vertical sidewalls
samples = []
for z in [Q(0),H/2,H]:
    pressure = pbottom-rho*gravity*z
    effective_N = rho*gravity*A*z
    recovered_wall_N = effective_N+pressure*A
    wrong_uniform_wall_N = effective_N+ptop*A
    assert recovered_wall_N == wall_N == 2000
    samples.append({'z':z,'pressure':pressure,'effective_N':effective_N,
                    'wall_N':recovered_wall_N,'wrong_uniform_wall_N':wrong_uniform_wall_N})
assert [s['wrong_uniform_wall_N'] for s in samples] == [1000,1500,2000]
# Applying full axial contents weight to a true wall-force/cap model doubles
# the external imbalance; the effective-force model represents it once.
double_counted_root = -(bottom_cap+top_cap-weight)
assert double_counted_root == 2000 == 2*root_action
findings['hydrostatic_wall_effective_distinction'] = {
    'root_action_N':root_action,'wrong_double_counted_root_N':double_counted_root,
    'true_wall_force_N':wall_N,'samples':samples}

# Shift p_top to the final design's 200 kPa and integrate strain coefficients.
# Averaging pressure can accidentally reproduce end extension while station
# wall forces remain wrong. Keep the previous 100 kPa witness as a second case.
ptop = Q(200_000)
pbottom = ptop+rho*gravity*H
paverage = (ptop+pbottom)/2
EA,nu = Q(200_000_000),Q(3,10)
def integrated_strain(wall_intercept,wall_slope,pressure_intercept,pressure_slope):
    strain_intercept = (wall_intercept-2*nu*A*pressure_intercept)/EA
    strain_slope = (wall_slope-2*nu*A*pressure_slope)/EA
    return strain_intercept*H+strain_slope*H**2/2
true_extension = integrated_strain(pbottom*A,0,pbottom,-rho*gravity)
uniform_top_extension = integrated_strain(ptop*A,rho*gravity*A,ptop,0)
uniform_average_extension = integrated_strain(paverage*A,rho*gravity*A,paverage,0)
true_station_N = [pbottom*A for z in [0,H/2,H]]
average_station_N = [paverage*A+rho*gravity*A*z for z in [0,H/2,H]]
assert true_station_N == [3000,3000,3000]
assert average_station_N == [2500,3000,3500]
assert true_extension == uniform_average_extension == Q(75,1_000_000)
assert uniform_top_extension == Q(65,1_000_000)
findings['hydrostatic_wall_effective_distinction']['average_pressure_counterexample'] = {
    'top_pressure_Pa':ptop,'average_pressure_Pa':paverage,
    'true_station_wall_N':true_station_N,'wrong_average_pressure_station_wall_N':average_station_N,
    'true_extension_m':true_extension,'wrong_top_pressure_extension_m':uniform_top_extension,
    'coincident_average_pressure_extension_m':uniform_average_extension}

def encode(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,list): return [encode(v) for v in x]
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    return x

packet={'status':'PASS','groups':len(findings),'scope':'independent design calculations only',
        'product_execution':False,'results':encode(findings),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'NUMERICAL_REVIEW.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'status':packet['status'],'groups':packet['groups'],'product_execution':False}))
