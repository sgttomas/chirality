#!/usr/bin/env python3
"""Independent exact/Decimal examples; no imports from the implementation."""
import json
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path

def encoded(v):
    if isinstance(v,F): return {'rational':str(v),'decimal':str(Decimal(v.numerator)/Decimal(v.denominator))}
    if isinstance(v,dict): return {k:encoded(x) for k,x in v.items()}
    if isinstance(v,list): return [encoded(x) for x in v]
    return v

out={}
k1,k2=F(200000000),F(100000000); g=F(1,10000)
u=k1*g/(k1+k2); ri=k1*(g-u); rj=-k2*u
assert u==F(1,15000) and ri==F(20000,3) and ri+rj==0
assert (k1+k2)*F(0)-k1*g != 0
out['prescribed_axial']={'u_mid_m':u,'support_root_N':ri,'support_end_N':rj,'omitted_coupling_residual_N':-k1*g}
EI,L,theta=F(2000),F(2),F(1,1000)
rot=[6*EI/L**2*theta,4*EI/L*theta,-6*EI/L**2*theta,2*EI/L*theta]
assert rot==[3,4,-3,2] and rot[0]+rot[2]==0 and rot[1]+rot[3]+L*rot[2]==0
out['prescribed_rotation']={'reactions_Fy_Mz_Fy_Mz':rot,'rigid_free_tip_UY_m':L*theta}
u=F(100000000)*F(1,1000)/F(300000000)
nh=F(100000000)*(u-F(1,1000)); nc=F(200000000)*u
assert u==F(1,3000) and nh==-F(200000,3) and nc+nh==0
out['per_element_shared_material']={'u_m':u,'hot_force_N':nh,'cold_force_N':nc}
l0=1+F(12,1000000)*30;l1=1+F(16,1000000)*130
eth=l1/l0-1
assert eth==F(43,25009) and eth!=F(16,1000000)*100
out['thermal_datum']={'free_strain':eth,'wrong_endpoint_alpha_deltaT':F(16,1000000)*100,'constant_alpha_interval':F(1,100000)*80}
integ=(F(10,1000000)+F(20,1000000))/2*100
assert integ==F(3,2000)
with localcontext() as c:
    c.prec=70
    logstrain=(Decimal(integ.numerator)/Decimal(integ.denominator)).exp()-1
    assert logstrain>Decimal('0.0015') and logstrain<Decimal('0.001502')
    out['coefficient_definition']={'datum_length_dilation':integ,'current_length_log_strain_decimal':str(logstrain),'wrong_endpoint':F(20,1000000)*100}
L=F(10);fit=-F(2,1000); lamfit=1+fit/L; thermal=1+F(1,100000)*80
cold=F(200000000)*(1-lamfit);eps=lamfit*thermal-1;hot=-F(150000000)*eps
assert cold==40000 and hot==-89976 and eps==F(3749,6250000)
out['cold_spring']={'cold_tension_N':cold,'hot_strain':eps,'hot_tension_N':hot,'released_cold_displacement_m':fit,'double_count_wrong_cold_N':2*cold}
metal=F(7000)*F(9,10000);fluid=F(900)*F(16,10000);q=-10*(metal+fluid)
assert q==-F(774,10) and -q*2==F(1548,10)
out['hydrotest_symbolic_pi']={'mass_per_length_kg_m_coefficient_of_pi':metal+fluid,'q_N_m_coefficient_of_pi':q,'root_Fy_N_coefficient_of_pi':-q*2,'root_Mz_Nm_coefficient_of_pi':-q*2,'wall_N_coefficient_of_pi':F(2000000)*F(16,10000),'changed_fluid_q_coefficient_of_pi':-10*(metal+F(100)*F(16,10000))}
k,ks,f0,f=F(1000),F(500),F(100),F(-1000);u=(f+f0)/(k+ks);fh=f0-ks*u;fr=-k*u
assert u==F(-3,5) and fh==400 and fr==600 and fh+fr+f==0
out['lock_replacement']={'active_u_m':u,'active_hanger_N':fh,'structure_support_N':fr,'locked_u_m':F(0),'locked_total_support_reaction_N':-f,'pin_force_if_internal_spring_retains_preload_N':-f-f0}
correct=F(-1000+200+100,1000);wrong=F(-1000+100,1000)+F(200+100,1000)
assert correct==F(-7,10) and wrong==F(-3,5)
out['persistent_preload']={'physical_combined_u_m':correct,'incorrect_sum_of_total_states_u_m':wrong}
slip=F(0);history=[]
for g in [F(0),F(3,1000),F(0)]:
    trial=1000*(g-slip)
    force=max(F(-1),min(F(1),trial))
    slip=g-force/1000
    history.append({'g_m':g,'force_N':force,'slip_m':slip})
assert history[1]['slip_m']==F(2,1000) and history[2]['slip_m']==F(1,1000) and history[2]['force_N']==-1
out['history_counterexample']={'path':history,'virgin_final_force_N':F(0)}
H,rho,g,A,p0=F(10),F(1000),F(10),F(1,100),F(200000)
pb=p0+rho*g*H;W=rho*g*A*H;z=[F(0),H/2,H]
pressure=[pb-rho*g*x for x in z]
wall=[pb*A for x in z];eff=[wall[i]-pressure[i]*A for i in range(3)]
doublewall=[pb*A+rho*g*A*x for x in z]
uniformwall=[p0*A+rho*g*A*x for x in z]
pavg=(p0+pb)/2
uniformavgwall=[pavg*A+rho*g*A*x for x in z]
assert wall==[3000,3000,3000] and eff==[0,500,1000] and W==1000
assert doublewall==[3000,3500,4000] and uniformwall==[2000,2500,3000]
EA,nu=F(200000000),F(3,10)
extension=(pb*A-2*nu*A*(pb+p0)/2)*H/EA
uniform_extension=((uniformwall[0]+uniformwall[2])/2-2*nu*p0*A)*H/EA
uniform_average_extension=((uniformavgwall[0]+uniformavgwall[2])/2-2*nu*pavg*A)*H/EA
assert extension==F(75,1000000) and uniform_extension==F(65,1000000)
assert uniformavgwall==[2500,3000,3500] and uniform_average_extension==extension
out['hydrostatic_column']={'z_m':z,'pressure_Pa':pressure,'wall_force_N':wall,'effective_force_N':eff,'support_N':W,'double_count_wall_N':doublewall,'double_count_support_N':2*W,'uniform_pressure_wall_N':uniformwall,'uniform_pressure_support_N':W,'correct_extension_m':extension,'wrong_uniform_extension_m':uniform_extension,'uniform_average_wall_force_N':uniformavgwall,'uniform_average_pressure_Pa':pavg,'uniform_average_extension_m':uniform_average_extension}
packet={'status':'PASS','claim':'Independent proposed-contract calculations only; no product execution','groups':len(out),'examples':encoded(out)}
path=Path(__file__).parent/'_run_records'/'analytical_examples.json'
path.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'status':packet['status'],'groups':packet['groups'],'output':str(path)}))
