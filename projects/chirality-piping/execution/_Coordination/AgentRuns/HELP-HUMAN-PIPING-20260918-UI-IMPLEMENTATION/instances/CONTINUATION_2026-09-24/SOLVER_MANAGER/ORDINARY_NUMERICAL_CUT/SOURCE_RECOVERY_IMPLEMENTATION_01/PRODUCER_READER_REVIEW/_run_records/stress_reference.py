#!/usr/bin/env python3
"""Independent source-scalar counterexample; no product execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from decimal import Decimal,localcontext
from fractions import Fraction as Q
import json,math
root=next(p for p in Path(__file__).resolve().parents if (p/'agents/AGENT_TASK.md').is_file())
sys.path.insert(0,str(root/'projects/chirality-piping'))
from core.analysis_runs.source_blocks import _derived

def decimal(q):
    with localcontext() as c:
        c.prec=100
        return str(Decimal(q.numerator)/Decimal(q.denominator))

F=1e-306
A=math.pi*(2000.**2-1800.**2)/4
I=math.pi*(2000.**4-1800.**4)/64
pa=F/A; mpa=pa/1e6
exact_pa=Q(F)/Q(A); exact_mpa=exact_pa/10**6
relative_pa=abs(Q(pa)-exact_pa)/exact_pa
relative_mpa=abs(Q(mpa)-exact_mpa)/exact_mpa
assert relative_mpa>Q(1,10**9)
force={'kind':'element_local_axial_force','unit':'N','value':F,'entity_ref':'pipe'}
stress={'kind':'element_local_axial_normal_stress','unit':'MPa','value':mpa,'entity_ref':'pipe','metadata':{'component':'axial_normal_stress'}}
summary={'kind':'open_formula_stress_summary','unit':'MPa','value':mpa,'entity_ref':'pipe'}
# These calls check existing scalar recipe predicates only. They do not create
# an authenticated source-block receipt or prove full product reachability.
_derived('straight_open_stress_v1',stress,[force])
_derived('reviewed_stress_summary_v1',summary,[stress])
print(json.dumps({'scope':'source-scalar transcription and actual Python scalar recipe predicates; no product solve',
 'source_basis':'actual represented binary64 force and section-area formula; source area independently transcribed, not runtime-captured; no primitive-pi accuracy claim',
 'force_hex':F.hex(),'area_hex':A.hex(),'area':A,
 'axial_stiffness':1e-6*A/2,'torsional_stiffness':1e-5*(2*I)/2,
 'axial_displacement':F/(1e-6*A/2),'mm_displacement':F/(1e-6*A/2)*1000,
 'stress_pa':pa,'stress_mpa':mpa,
 'exact_pa_fraction':str(exact_pa),'exact_mpa_fraction':str(exact_mpa),
 'exact_pa_decimal100':decimal(exact_pa),'exact_mpa_decimal100':decimal(exact_mpa),
 'pa_relative_error':decimal(relative_pa),'mpa_relative_error':decimal(relative_mpa),
 'mpa_fails_1e-9':True,'existing_python_scalar_stress_and_summary_predicates_accept':True},indent=2))
