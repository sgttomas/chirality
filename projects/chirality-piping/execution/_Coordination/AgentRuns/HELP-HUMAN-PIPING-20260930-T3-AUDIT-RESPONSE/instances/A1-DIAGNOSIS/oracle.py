#!/usr/bin/env python3
"""Independent exact oracle for the sealed A1 24-case matrix.

Only Python standard-library integer/Fraction arithmetic supplies truth. No
solver, Wide helper, GEN/audit/reviewer oracle or scientific package is imported.
The generated Rust fixture is input data, never a substitute retained state.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import struct

def power(e):
    return Q(1 << e) if e >= 0 else Q(1, 1 << -e)

H = power(-1074)
COMP = ('Ux', 'Uy', 'Uz', 'Rx', 'Ry', 'Rz')
KINDS = ('Translation', 'Rotation', 'Force', 'Moment')

def exponent(x):
    assert x > 0
    n, d = x.numerator, x.denominator
    e = n.bit_length() - d.bit_length()
    return e - (x < power(e))

def nearest_integer(x):
    assert x >= 0
    n, rem = divmod(x.numerator, x.denominator)
    return n + (2 * rem > x.denominator or (2 * rem == x.denominator and n % 2))

def rounded(x, p):
    if not x:
        return Q(0)
    unit = power(exponent(abs(x)) - p + 1)
    return (-1 if x < 0 else 1) * nearest_integer(abs(x) / unit) * unit

def bits(x):
    """Correctly rounded binary64 bits, RN ties-even, including signed underflow."""
    if not x:
        return 0
    sign = (1 << 63) if x < 0 else 0
    x = abs(x)
    e = exponent(x)
    if e < -1022:
        return sign | nearest_integer(x / H)
    unit = power(e - 52)
    sig = nearest_integer(x / unit)
    if sig == 1 << 53:
        e += 1
        sig >>= 1
    if e > 1023:
        return sign | 0x7ff0000000000000
    return sign | ((e + 1023) << 52) | (sig - (1 << 52))

def from_bits(b):
    sign = -1 if b >> 63 else 1
    ef = (b >> 52) & 2047
    sig = b & ((1 << 52) - 1)
    if ef == 2047:
        raise ValueError('Nonfinite binary64 has no Fraction')
    return sign * (sig * H if ef == 0 else ((1 << 52) + sig) * power(ef - 1075))

def up(x):
    assert x >= 0
    b = bits(x)
    if b == 0x7ff0000000000000:
        raise OverflowError('upward result is not finite')
    return from_bits(b + (from_bits(b) < x))

def exact(x):
    """Normalized dyadic value n*2^e; never replace tiny nonzero truth by zero."""
    if not x:
        return {'n': '0', 'e': 0}
    assert x.denominator & (x.denominator - 1) == 0
    n, e = x.numerator, -(x.denominator.bit_length() - 1)
    while n % 2 == 0:
        n //= 2
        e += 1
    return {'n': str(n), 'e': e}

def read_exact(v):
    return int(v['n']) * power(v['e'])

def hex_bits(x):
    return f'{bits(x):016x}'

def source_cases():
    b = [('T',100,5*H),('A',-100,5*H),('T',0,5*H),('A',0,5*H),
         ('T',85,5*H),('T',86,5*H),('A',-85,5*H),('A',-86,5*H),
         ('T',-100,5*H),('A',100,5*H),('T',100,4*H),('A',-100,4*H),
         ('T',100,power(-1020)),('A',-100,power(-1020)),
         ('T',100,2*H),('A',-100,2*H)]
    for i,(family,le,load) in enumerate(b,1):
        yield dict(id=f'B{i:02}',family=family,L=power(le),load=load)
    c = [(100,76,-33,-900,9,0,0),(100,76,-33,-900,8,0,0),
         (100,76,-33,-900,10,0,0),(100,76,-33,-900,0,0,0),
         (100,76,-33,-900,9,0,1),(-100,276,167,-900,9,0,0),
         (100,56,-33,-920,9,-1008,0),(100,56,-33,-920,0,-1008,0)]
    for i,(le,ae,ke,fe,th,qe,g) in enumerate(c,17):
        yield dict(id=f'C{i}',family='C',L=power(le),a=power(ae),k=power(ke),
                   F=power(fe),t=th*H,q=power(qe) if qe else Q(0),g=g)

def materialize(c):
    family,L = c['family'],c['L']
    area = 4*L if family == 'A' else c['a']*L if family == 'C' else Q(1)
    torsion = Q(1) if family == 'A' else 4*L
    free = [6] if family == 'A' else [9] if family == 'T' else [0,6,9]
    u = [Q(0) for _ in range(12)]
    loads = []
    def load(g,x,label):
        if x:
            assert from_bits(bits(x)) == x
            loads.append(dict(global_dof=g,value_bits=hex_bits(x),source_id=c['id']+':'+label))
    if family == 'C':
        g,j = c['g'],1-c['g']
        u[6*g] = c['q']+c['t']/c['k']
        u[6*j] = u[6*g]-c['F']/c['a']
        u[9] = 5*H/4
        load(6*g,c['F'],'axial-F-ground')
        load(6*g,c['k']*c['q'],'axial-kq-ground')
        load(6*g,c['t'],'axial-tail-ground')
        load(6*j,-c['F'],'axial-minus-F-other')
        load(9,5*H,'tip-Mx')
        assert (c['a']+c['k'])*u[6*g]-c['a']*u[6*j] == c['F']+c['k']*c['q']+c['t']
        assert -c['a']*u[6*g]+c['a']*u[6*j] == -c['F']
    else:
        u[free[0]] = c['load']/4
        load(free[0],c['load'],'tip-Mx' if family=='T' else 'tip-Fx')
    constraints = [g for g in range(12) if g not in free]
    springs = [] if family != 'C' else [dict(id=1,global_dof=6*c['g'],stiffness_bits=hex_bits(c['k']))]
    member = dict(id=1,node_i=0,node_j=1,elastic_modulus_bits=hex_bits(Q(1)),
                  shear_modulus_bits=hex_bits(Q(1)),area_bits=hex_bits(area),
                  second_moment_y_bits=hex_bits(Q(1)),second_moment_z_bits=hex_bits(Q(1)),
                  torsion_constant_bits=hex_bits(torsion),y_reference_bits=[hex_bits(Q(0)),hex_bits(Q(1)),hex_bits(Q(0))])
    for key in ('elastic_modulus_bits','shear_modulus_bits','area_bits','second_moment_y_bits','second_moment_z_bits','torsion_constant_bits'):
        v=int(member[key],16)
        assert 0 < ((v>>52)&2047) < 2047 and not v>>63
    primitive = dict(nodes_bits=[[hex_bits(Q(0))]*3,[hex_bits(L),hex_bits(Q(0)),hex_bits(Q(0))]],
                     members=[member],springs=springs,directional_springs=[],
                     constraints=[dict(global_dof=g,value_bits=hex_bits(Q(0))) for g in constraints],
                     loads=loads,stations=[],supports=[])
    # Independent exact axial/torsional mechanics. Node-on-element convention:
    # N = EA/L*(u1-u0), T = GJ/L*(r1-r0); end I = -(N,T), end J = +(N,T).
    n = area/L*(u[6]-u[0]); m = torsion/L*(u[9]-u[3])
    nodal = [Q(0)]*12
    nodal[0],nodal[6],nodal[3],nodal[9] = -n,n,-m,m
    if family == 'C':
        nodal[6*c['g']] += c['k']*u[6*c['g']]
    applied = [Q(0)]*12
    for item in loads:
        applied[item['global_dof']] += from_bits(int(item['value_bits'],16))
    assert all(nodal[g] == applied[g] for g in free)
    rows=[]
    def row(key,kind,value,input_derived=False):
        b=bits(value)
        outcome='Overflow' if b&0x7fffffffffffffff == 0x7ff0000000000000 else 'Underflow' if value and not b&0x7fffffffffffffff else 'Value'
        rows.append(dict(key=key,kind=kind,input_derived=input_derived,truth=exact(value),
                         correctly_rounded_truth_bits=f'{b:016x}',truth_rounding_outcome=outcome))
    for g,v in enumerate(u): row(f'D:{g}',KINDS[g%6>=3],v,g in constraints)
    for node in range(2): row(f'M:{node}','Translation',abs(u[6*node]))
    for end,sign in [('I',-1),('J',1)]:
        for k in range(6): row(f'E:1:{end}:{k}','Force' if k<3 else 'Moment',sign*(n if k==0 else m if k==3 else Q(0)))
    if family=='C': row('S:1:0','Force',-c['k']*u[6*c['g']])
    for g in constraints: row(f'R:{g}','Force' if g%6<3 else 'Moment',nodal[g]-applied[g])
    source_bytes=json.dumps(primitive,sort_keys=True,separators=(',',':')).encode()
    return dict(id=c['id'],family=family,parameters={k:exact(v) for k,v in c.items() if isinstance(v,Q)},
                grounded_node=c.get('g'),primitive=primitive,input_json_sha256=hashlib.sha256(source_bytes).hexdigest(),
                free_dofs=free,expected_rows=rows,runtime_status='UNRUN',
                note='Exact mathematical truth and nearest truth bits; not predicted or observed selected values.')

def selfcheck():
    checks=0
    known=[(Q(0),0),(H/2,0),(3*H/2,2),(5*H/4,1),(5*H/2,2),
           (-H/2,1<<63),(power(-1022)-H/2,0x0010000000000000),
           (Q(1)+power(-53),0x3ff0000000000000),(Q(1)+3*power(-53),0x3ff0000000000002),
           ((2-power(-52))*power(1023),0x7fefffffffffffff),
           ((2-power(-53))*power(1023),0x7ff0000000000000)]
    for x,b in known: assert bits(x)==b; checks+=1
    for e in [-1074,-1073,-1022,-1021,-100,-1,0,1,100,1023]:
        base=bits(power(e))
        for off in range(-8,9):
            b=base+off
            if 0<=b<0x7ff0000000000000:
                for sign in [0,1<<63]:
                    bb=b|sign
                    assert bits(from_bits(bb)) == (bb if b else 0)
                    if b:
                        for quarter in [Q(-1,4),Q(1,4),Q(1,2),Q(3,4)]:
                            x=from_bits(bb)+quarter*power(max(-1074,e-52))
                            expected=int.from_bytes(struct.pack('>d',float(x)),'big')
                            assert bits(x)==expected
                            checks+=1
                    checks+=1
    sources=[materialize(c) for c in source_cases()]
    assert len(sources)==24
    assert [len(c['expected_rows']) for c in sources]==[37]*16+[36]*8
    c22=sources[21]
    target=next(r for r in c22['expected_rows'] if r['key']=='D:0')
    assert read_exact(target['truth'])==9*power(-1241)>0
    assert target['truth_rounding_outcome']=='Underflow'
    # Check exact projected ledger at p=128 and P=256, not a solver emulation.
    projection=[]
    for c in source_cases():
        if c['family']!='C': continue
        net=c['F']+c['k']*c['q']+c['t']
        assert rounded(net,128)==c['F']+c['k']*c['q']
        assert rounded(net,256)==net
        projection.append(dict(id=c['id'],net=exact(net),p128=exact(rounded(net,128)),P256=exact(rounded(net,256))))
    d=9*power(-1041); q=power(-1008)
    assert d/q>Q(1,10**9) and d/(q+d)>Q(1,10**9)
    kappa=power(-109)
    assert kappa*(2**128-6)>384*(2+kappa)
    assert 9*H*(2**128-4)<=256*(2*power(-900)+9*H)
    # Synthetic serialization/comparator checks only. These are fabricated
    # records for testing the oracle, never presented as solver observations.
    synthetic=synthetic_log(sources[2])
    assert not compare(sources,synthetic)['violations']
    for bad in [synthetic.replace('SELECTED\t128\t256','SELECTED\t128\t512'),
                synthetic+'SCALE\tForce\t0000000000000000\n',
                synthetic_log(sources[2],p=512).replace('FLOOR\tMoment\t0000000000000000\n',''),
                synthetic_log(sources[2],p=512)+'FLOOR\tForce\t0000000000000000\n']:
        try: compare(sources,bad)
        except AssertionError: pass
        else: raise AssertionError('malformed synthetic record was accepted')
    unexpected=synthetic.replace('ROW\tD:9\tRotation\tValue\t0000000000000001\tAbsoluteVerified',
                                'ROW\tD:9\tRotation\tUnderflow\tnone\tUnpublishable')
    assert 'range:D:9' in compare(sources,unexpected)['violations']
    for index,override in [(16,{'D:0':Q(0),'M:0':Q(0)}),
                           (21,{'D:0':Q(0),'M:0':Q(0)}),
                           (22,{'D:0':power(-1008),'M:0':power(-1008)})]:
        result=compare(sources,synthetic_log(sources[index],override=override))
        assert 'claim:D:0' in result['violations']
        if index==22:
            target=next(r for r in result['comparisons'] if r['key']=='D:0')
            assert not target['relative_claim_published_passes'] and not target['relative_truth_passes']
    return dict(status='PASS',binary64_checks=checks,cases=24,truth_rows=sum(len(c['expected_rows']) for c in sources),
                exact_equilibrium='PASS for all free DOFs of all 24 sources',
                synthetic_comparator_checks='PASS: honest scalar, p/P mismatch, duplicate scale/floor, missing p512 floor, unexpected range, false absolute/zero-bound/relative claims',
                projection_checks=projection,scope='Pure integer/Fraction and scalar binary64 self-checks only; no solver execution.')

def rust_data(cases):
    out=['// Generated inert input data by oracle.py; exact bits, no arithmetic oracle.','const CASES: &[Spec] = &[']
    for c in cases:
        p=c['primitive']; m=p['members'][0]
        loads=', '.join(f'({v["global_dof"]}, 0x{v["value_bits"]}, "{v["source_id"]}")' for v in p['loads'])
        k=p['springs'][0]['stiffness_bits'] if p['springs'] else '0000000000000000'
        g=p['springs'][0]['global_dof'] if p['springs'] else 0
        out.append(f'    Spec {{ id: "{c["id"]}", length: 0x{p["nodes_bits"][1][0]}, area: 0x{m["area_bits"]}, torsion: 0x{m["torsion_constant_bits"]}, spring: ({g}, 0x{k}), free: &{c["free_dofs"]}, loads: &[{loads}] }},')
    return '\n'.join(out+ ['];',''])

def row_bound(q,s):
    b=up(s*power(-64))
    return up(b+up(abs(q)*power(-53))+H) if 0<s<power(-988) else b

def synthetic_log(c, p=128, override=None):
    """Pure comparator fixture, not a constructed/observed retained state."""
    values={r['key']:read_exact(r['truth']) for r in c['expected_rows']}
    values.update(override or {})
    raw={k:Q(0) for k in KINDS}
    for r in c['expected_rows']:
        x=values[r['key']]; b=bits(x)
        if not r['input_derived'] and (not x or b&0x7fffffffffffffff):
            raw[r['kind']]=max(raw[r['kind']],abs(from_bits(b)))
    L=from_bits(int(c['primitive']['nodes_bits'][1][0],16)); rn=lambda x:from_bits(bits(x))
    scales=dict(Translation=max(raw['Translation'],rn(L*raw['Rotation'])),
                Rotation=max(raw['Rotation'],rn(raw['Translation']/L)),
                Force=max(raw['Force'],rn(raw['Moment']/L)),Moment=max(raw['Moment'],rn(L*raw['Force'])))
    lines=[f'CASE\t{c["id"]}', 'STATUS\tSelected',f'SELECTED\t{p}\t{2*p}']
    lines += [f'SCALE\t{k}\t{bits(v):016x}' for k,v in scales.items()]
    if p==512: lines += ['FLOOR\tForce\t0000000000000000','FLOOR\tMoment\t0000000000000000']
    for r in c['expected_rows']:
        x=values[r['key']]; b=bits(x); q=from_bits(b); s=scales[r['kind']]
        if x and not b&0x7fffffffffffffff:
            outcome,bitstring,cls,bound='Underflow','none','Unpublishable','none'
        else:
            outcome,bitstring='Value',f'{b:016x}'
            cls='InputDerived' if r['input_derived'] else 'AbsoluteVerified' if s<power(-988) or abs(q)<rn(s*power(-34)) else 'RelativeVerified'
            bound=hex_bits(row_bound(q,s)) if cls=='AbsoluteVerified' else 'none'
        lines.append(f'ROW\t{r["key"]}\t{r["kind"]}\t{outcome}\t{bitstring}\t{cls}\t{bound}')
    return '\n'.join(lines)+'\n'

def compare(cases, log):
    """Read the probe's TSV subset; every claimed row gets exact truth comparison."""
    rows={}; scales={}; floor={}; cid=None; p=None; P=None; status=None
    for line in log.splitlines():
        v=line.split('\t')
        if v[0]=='CASE': cid=v[1]
        elif v[0]=='STATUS': status=v[1]
        elif v[0]=='SELECTED':
            assert p is None, 'duplicate selection'
            p,P=int(v[1]),int(v[2])
        elif v[0]=='ROW':
            assert v[1] not in rows, 'duplicate output row'
            rows[v[1]]=v
        elif v[0]=='SCALE':
            assert v[1] not in scales, 'duplicate scale'
            scales[v[1]]=from_bits(int(v[2],16))
        elif v[0]=='FLOOR':
            assert v[1] not in floor, 'duplicate floor'
            floor[v[1]]=from_bits(int(v[2],16))
    source=next(c for c in cases if c['id']==cid)
    result=dict(id=cid,status=status,selected_precision=p,verification_precision=P,comparisons=[],violations=[],limits=[],
                relative_claim_basis='D1 DESIGN_NUMERICS/DESIGN.md section 4.1.6 lines 424-446: error/abs(published q); exact truth ratio separately preserved. Not the distinct R1 class-scale benchmark predicate.')
    if status!='Selected':
        result['disposition']='source_or_solve_refusal_or_incomplete; never a pass'
        return result
    assert p in [128,256,512]
    assert P==2*p, 'verification precision must be twice selected precision'
    assert set(floor)==({'Force','Moment'} if p==512 else set()), 'floor inventory inconsistent with selected precision'
    assert all(v>=0 for v in list(scales.values())+list(floor.values()))
    assert set(rows)=={r['key'] for r in source['expected_rows']}, 'missing/extra row'
    assert set(scales)==set(KINDS), 'missing scale'
    raw={k:Q(0) for k in KINDS}
    for r in source['expected_rows']:
        v=rows[r['key']]
        assert v[2]==r['kind']
        if v[3]=='Value' and not r['input_derived']:
            raw[r['kind']]=max(raw[r['kind']],abs(from_bits(int(v[4],16))))
    L=from_bits(int(source['primitive']['nodes_bits'][1][0],16))
    rn=lambda x:from_bits(bits(x))
    calculated=dict(Translation=max(raw['Translation'],rn(L*raw['Rotation'])),
                    Rotation=max(raw['Rotation'],rn(raw['Translation']/L)),
                    Force=max(raw['Force'],rn(raw['Moment']/L)),
                    Moment=max(raw['Moment'],rn(L*raw['Force'])))
    for kind in KINDS:
        if p==512 and kind in ('Force','Moment'):
            calculated[kind]=max(calculated[kind],floor[kind])
        if calculated[kind]!=scales[kind]: result['violations'].append('scale:'+kind)
    for r in source['expected_rows']:
        v=rows[r['key']]; truth=read_exact(r['truth']); item=dict(key=r['key'],truth=r['truth'],outcome=v[3],row_class=v[5])
        if v[3]!='Value':
            item['disposition']='unpublishable; no published-zero claim'
            item['truth_rounding_outcome']=r['truth_rounding_outcome']
            item['range_agrees_with_exact_truth']=v[3]==r['truth_rounding_outcome']
            result['limits'].append('unpublishable:'+r['key'])
            if not item['range_agrees_with_exact_truth']: result['violations'].append('range:'+r['key'])
            if v[5]!='Unpublishable': result['violations'].append('unpublishable-class:'+r['key'])
        else:
            q=from_bits(int(v[4],16)); err=abs(q-truth); s=scales[r['kind']]
            cls='InputDerived' if r['input_derived'] else 'AbsoluteVerified' if s<power(-988) or abs(q)<rn(s*power(-34)) else 'RelativeVerified'
            if cls!=v[5]: result['violations'].append('class:'+r['key'])
            item.update(published=exact(q),absolute_error=exact(err))
            if cls=='InputDerived': ok=q==truth
            elif cls=='AbsoluteVerified':
                b=from_bits(int(v[6],16)); expected=row_bound(q,s)
                if b!=expected: result['violations'].append('bound-bits:'+r['key'])
                ok=err<=b*(1+power(-21 if p==512 else -22))
                item['bound']=exact(b)
            else:
                # D1's assurance proof uses the published denominator. Keep
                # true-relative error explicit; never silently choose between
                # conventions if a case distinguishes them.
                ok=bool(q) and err<=abs(q)/10**9
                truth_ok=bool(truth) and err<=abs(truth)/10**9
                item['relative_claim_published_passes']=ok
                item['relative_truth_passes']=truth_ok
                if ok!=truth_ok: result['violations'].append('relative_denominator_disagreement:'+r['key'])
                item['relative_error_truth']=str(err/abs(truth)) if truth else None
                item['relative_error_publication']=str(err/abs(q)) if q else None
            item['claim_passes']=ok
            if not ok: result['violations'].append('claim:'+r['key'])
        result['comparisons'].append(item)
    result['disposition']='STOP_AND_RETURN' if result['violations'] else 'finite_published_claims_pass_with_unpublishable_limits; not universal proof closure' if result['limits'] else 'finite_selected_claims_pass; not universal proof closure'
    return result

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('self-check')
    sub.add_parser('generate')
    p=sub.add_parser('compare'); p.add_argument('stdout_path')
    args=ap.parse_args(); here=Path(__file__).resolve().parent
    if args.command=='self-check': print(json.dumps(selfcheck(),indent=2))
    elif args.command=='generate':
        cases=[materialize(c) for c in source_cases()]
        (here/'matrix.json').write_text(json.dumps(dict(format='a1-exact-matrix-v1',zero_loads='omitted; no pre-summed loads',cases=cases),indent=2)+'\n')
        (here/'src').mkdir(exist_ok=True)
        (here/'src/cases.rs').write_text(rust_data(cases))
        print(json.dumps(dict(status='generated',cases=len(cases),truth_rows=sum(len(c['expected_rows']) for c in cases))))
    else:
        cases=json.loads((here/'matrix.json').read_text())['cases']
        print(json.dumps(compare(cases,Path(args.stdout_path).read_text()),indent=2))

if __name__=='__main__': main()
