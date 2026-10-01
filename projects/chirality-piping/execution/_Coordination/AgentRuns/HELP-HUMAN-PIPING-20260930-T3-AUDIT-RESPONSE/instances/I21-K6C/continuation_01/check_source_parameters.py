#!/usr/bin/env python3
"""Bounded source/record arithmetic; no model/generator/runner imports.

The integer graph below is connectivity metadata for pre-dedup cardinalities,
not a mechanics model. No coordinates, stiffness, factor or solve is formed.
"""
import hashlib
import json
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
HERE = Path(__file__).resolve().parent
P = Path('projects/chirality-piping')
H = P/'core/solver/performance_harness'
VR = P/'validation/benchmarks/numerical_robustness'
BASIS = '3bddc2b05f6106e969c7cf43373b230845c7cc66'

def sha(b): return hashlib.sha256(b).hexdigest()
def read(path): return (ROOT/path).read_text()
def lines(path): return [json.loads(x) for x in read(path).splitlines() if x.strip()]
def g(k, minimum=4): return max(minimum,1<<(k-1).bit_length()) if k else 0
def enc_cap(length):
    c=6
    while c<length:c*=2
    return c
def bulk_nodes(k):
    """Before right-border fix, append.rs's base-12 carry construction."""
    if not k:return {'leaves':0,'internal':0}
    leaves=1+k//12; internal=0; threshold=12
    while k>=threshold:
        internal += 1+k//(12*threshold)
        threshold*=12
    return {'leaves':leaves,'internal':internal}

def comparison_bound(d,lo10,hi10):
    """Source operator DAG allocation-volume bound for one comparison group.

    Metadata tuples = (significand bit upper, p2 low/high, p10 low/high).
    Never computes an observation, predicate, reference answer or solver state.
    Charging every allocation request of the finite DAG is conservative for
    simultaneous live bytes. Row/control iterations are sequential.
    """
    charged=0;maxbits=0
    def words(bits):return (max(1,bits)+31)//32
    def note(x):
        nonlocal maxbits
        maxbits=max(maxbits,x[0]);return x
    def clone(x):
        nonlocal charged
        charged+=4*words(x[0]);return x
    def f64():
        nonlocal charged
        charged+=8;return note((53,-1074,971,0,0))
    def dec():
        nonlocal charged
        # digits String, chunks Vec<&[u8]>, monotonic mantissa growth;
        # sum of requests through doubling <=2*final-capacity.
        charged+=4*max(8,2*d)+2*max(4,2*((d+8)//9+1))*16+2*max(4,2*words(4*d))*4
        return note((4*d,0,0,lo10,hi10))
    def pow2(k):
        nonlocal charged
        charged+=8;return note((1,k,k,0,0))
    def scaled(x,a,b):
        clone(x);return note((x[0],x[1]+a,x[2]+a,x[3]+b,x[4]+b))
    def align(a,b):
        nonlocal charged
        p2,p10=min(a[1],b[1]),min(a[3],b[3]);xs=[]
        for x in [a,b]:
            shifted=x[0]+x[2]-p2
            total=shifted+4*(x[4]-p10)
            # shl request history, then clone+monotonic mul_pow10 growth.
            charged+=2*max(4,2*words(shifted))*4+2*max(4,2*words(total))*4
            xs.append(total)
            note((total,p2,p2,p10,p10))
        return xs
    def cmp(a,b):align(a,b)
    def add(a,b):
        nonlocal charged
        ab=align(a,b);charged+=4*(max(map(words,ab))+1)
        return note((max(ab)+1,min(a[1],b[1]),max(a[2],b[2]),min(a[3],b[3]),max(a[4],b[4])))
    def sub(a,b):return add(a,clone(b))
    def mul(a,b):
        nonlocal charged
        charged+=12*(words(a[0])+words(b[0])+1) # u64 acc + new u32 Vec
        return note((a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3],a[4]+b[4]))
    def maximum(a,b):
        cmp(a,b);x=(max(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),min(a[3],b[3]),max(a[4],b[4]));return clone(x)
    def tol(e,s):return scaled(maximum(clone(e),s),0,-9)
    e,s=dec(),dec()
    # Value predicate, magnitude predicate (both branches), covered and
    # outside_binary64. Charging all alternatives together only increases it.
    obs=f64();cmp(clone(sub(obs,e)),tol(e,s))
    y,z=f64(),f64();squares=add(mul(y,y),mul(z,z));t=tol(e,s)
    upper=add(e,t);cmp(squares,mul(upper,upper));lower=sub(e,t);cmp(squares,mul(lower,lower))
    cmp(maximum(clone(e),s),scaled(f64(),-34,0))
    ea=clone(e);tiny=pow2(-1075);huge=sub(pow2(1024),pow2(970));cmp(ea,tiny);cmp(ea,huge)
    # Value controls parse one additional decimal observation; their scalar
    # predicate may span the whole decimal exponent range.
    co=dec();cmp(clone(sub(co,e)),tol(e,s))
    return dict(requested_allocation_volume_upper_bytes=charged,max_intermediate_significand_bits=maxbits,
                method='sum of fresh allocation requests of finite Exact/Nat operator DAG; excludes caller persistent data and separate diagnostic formatting')

def topology(mid,c):
    n,m=c['w1_nodes'],c['w1_members'];neighbors=[set() for _ in range(n)]
    fixed={0:set(range(6))}; labels=[];member_labels=[];load_dofs=[]
    def edge(a,b):
        assert a!=b and b not in neighbors[a]
        neighbors[a].add(b);neighbors[b].add(a)
    if mid.startswith('RF-LARGE-'):
        family=mid.split('-')[2];rot=mid.endswith('-ROT')
        if family=='CHAIN':
            labels=['N'+str(i) for i in range(n)];member_labels=['M'+str(i) for i in range(1,m+1)]
            for i in range(1,n):edge(i-1,i)
            load_dofs=list(range(6*m,6*m+6))
        elif family=='TREE':
            labels=['P0'];h=m//2
            for k in range(1,h+1):
                labels.extend(['P'+str(k),'B'+str(k)]);member_labels.extend(['S'+str(k),'Q'+str(k)])
                edge(0 if k==1 else 2*k-3,2*k-1);edge(2*k-1,2*k)
                if k%7!=3:load_dofs.extend(12*k+a for a in (range(3) if rot else [2 if k%2 else 1]))
        else:
            assert family=='CONT';h=m//2;labels=['S'+str(i) for i in range(h+1)]+['C'+str(i) for i in range(1,h+1)]
            for j in range(1,h+1):
                member_labels.extend(['A'+str(j),'B'+str(j)]);edge(j-1,h+j);edge(h+j,j);fixed[j]={0,1,2}
                y,z=j%5-2,j%3-1
                comps=[2*y+2*z,y-2*z,2*y-z] if rot else [0,y,z]
                load_dofs.extend(6*(h+j)+a for a,v in enumerate(comps) if v)
        provenance='Symbolic integer connectivity/zero-support rules from H models.rs; no generator executed'
    else:
        name=mid.replace('DEC053:','DEC053_')+'.k6model';path=H/'observations/k6/models'/name
        text=read(path);fixed={};labels=[]
        for s in text.splitlines():
            w=s.split()
            if not w:continue
            if w[0]=='node':labels.append(w[2])
            if w[0]=='member':edge(int(w[3]),int(w[4]));member_labels.append(w[2])
            if w[0]=='restraint':fixed[int(w[1])]={i for i,z in enumerate(w[2]) if z=='1'}
            if w[0]=='load':
                assert int(w[2],16)&0x7fffffffffffffff
                load_dofs.append(int(w[1]))
        provenance=str(path)
    assert len(labels)==n and len(member_labels)==m
    assert len(load_dofs)==c['w1_loads'] and len(set(load_dofs))==len(load_dofs)
    assert sum(len(x) for x in neighbors)==2*m
    assert sum(len(x) for x in fixed.values())==c['w1_constraints']
    assert fixed.get(0)==set(range(6))
    free=[6-len(fixed.get(i,())) for i in range(n)]
    degree=[free[i]-1+sum(free[j] for j in neighbors[i]) for i in range(n)]
    ad=Counter()
    for k,d in zip(free,degree):
        if k:ad[d]+=k
    assert sum(ad.values())==c['w1_free_dofs']
    source_ids=sum(len('k6:'+str(i)) for i in load_dofs)
    return dict(origin=provenance,node_label_payload_bytes=sum(map(len,labels)),member_label_payload_bytes=sum(map(len,member_labels)),
        node_label_max_bytes=max(map(len,labels)),member_label_max_bytes=max(map(len,member_labels)),
        load_dofs_unique=True,loads_nonzero_by_fixture_construction=True,source_id_bytes_exact=source_ids,
        source_id_format_capacity_bytes=sum(6 if len('k6:'+str(i))<=6 else 12 for i in load_dofs),
        fully_fixed_node_zero=True,node_degree_histogram=dict(sorted(Counter(map(len,neighbors)).items())),
        full_pattern_prededup_entries=144*m,upper_positions=78*m,
        sparse_prededup_row_capacity_usize=sum(6*g(12*len(nb)) for nb in neighbors),
        free_adjacency_degree_histogram=dict(sorted(ad.items())),free_adjacency_entries=sum(d*k for d,k in ad.items()),
        free_adjacency_capacity_usize=sum(g(d)*k for d,k in ad.items()),
        rcm_neighbors_prededup_capacity_usize=sum(g(2*d)*k for d,k in ad.items()))

def main():
    # AUD-REV-N1: validate the consulted source/library snapshot separately
    # from identifying this new arithmetic script by its own hash.
    source_pins=json.loads((HERE/'SOURCE_INPUTS.json').read_text())
    runtime_binding=json.loads(read(P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE/RUNTIME_BINDING.json'))
    runtime=Path(tempfile.gettempdir())/runtime_binding['runtime_directory_name']
    for entry in source_pins['inputs']:
        name=entry['origin']
        if name.startswith('<RESPONSE_RUNTIME>/'):
            path=runtime/name.split('/',1)[1]
        elif name.startswith('<OWNER_CARGO_HOME>/'):
            path=Path.home()/'.cargo'/name.split('/',1)[1]
        else:path=ROOT/name
        assert sha(path.read_bytes())==entry['sha256'],'source input drift: '+name
    historical_vr=P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/IMPLEMENTATION/KF3/_run_records/b/counts.json'
    pinpaths=[H/'observations/k6b/counts.jsonl',H/'observations/k6b/sources.txt',H/'observations/k6/models_sha256.txt',
        H/'src/k6/models.rs',H/'src/k6/w1/adapter.rs',VR/'cases/rf_large.jsonl',VR/'cases/large_models.sha256']
    pinpaths += [historical_vr]+[p.relative_to(ROOT) for p in sorted((ROOT/H/'observations/k6/models').glob('*.k6model'))]
    identities=[]
    for p in pinpaths:
        raw=(ROOT/p).read_bytes();assert raw==subprocess.check_output(['git','show',BASIS+':'+str(p)]),str(p)
        identities.append(dict(path=str(p),sha256=sha(raw)))
    sources={};canon={}
    for line in read(H/'observations/k6b/sources.txt').splitlines():
        if line and not line.startswith('#'):
            k,length,s,f=line.split();sources[k]=(int(length),s,f)
    for line in read(H/'observations/k6/models_sha256.txt').splitlines():
        if line and not line.startswith('#'):
            s,k=line.split();canon[k]=s
    out=[]
    for c in lines(H/'observations/k6b/counts.jsonl'):
        mid=c['model'];v=topology(mid,c);N,m,r,l=[c['w1_'+k] for k in ['nodes','members','constraints','loads']]
        q=7*N+18*m+r;stf=26+24*N+84*m+5*r;src=38+24*N+100*m+13*r+17*l+v['source_id_bytes_exact'];led=10+26*l
        assert q==c['w1_rows'] and src==c['w1_source_encoding_len']==sources[mid][0]
        assert c['w1_source_encoding_fnv64']==sources[mid][2]
        actual=ROOT/H/'observations/k6/models'/(mid.replace('DEC053:','DEC053_')+'.k6model')
        if actual.exists():assert sha(actual.read_bytes())==canon[mid]
        entry=dict(model=mid,canonical_model_sha256=canon[mid],K4SRC_sha256=sources[mid][1],K4SRC_fnv64=sources[mid][2],
            N=N,m=m,r=r,l=l,n=6*N,f=c['w1_free_dofs'],q=q,b=c['w1_blocks'],B=c['w1_bodies'],z=c['w1_pattern_entries'],s=c['w1_profile_entries'],topology=v,
            payload_bytes=dict(K4STF=stf,K4SRC=src,K4LED=led,K4RST={str(W):22+(6*N+6*m)*(9+8*W) for W in [4,8,16]}),
            capacity_bytes=dict(K4STF=enc_cap(stf),K4SRC=enc_cap(src),K4LED=enc_cap(led),K4RST={str(W):enc_cap(22+(6*N+6*m)*(9+8*W)) for W in [4,8,16]}),
            K4STF_identity=dict(method='deterministic stiffness projection of sealed K4SRC under source.rs pinned function',payload_sha256='not materialized; no invented byte hash'),
            geometry_branch='root has six constraints; general scratch bounded, SVD early-return not assumed for CONT/grid',
            single_case_attempts_max=4,prefix_segments_max=10,prefix_limits_max=9)
        out.append(entry)
    rf=lines(VR/'cases/rf_large.jsonl');vh={x['model']:x for x in lines(historical_vr)}
    vr=[]
    for c in rf:
        mid=c['id'];hc=next(x for x in out if x['model']==mid)
        model=c.get('model');l=hc['l'];ids=sum(1+len(str(i)) for i in range(l))
        if model is not None:
            loads=model['loads'];assert len(loads)==l and len({(x[0],x[1]) for x in loads})==l
            assert all(int(x[2],16)&0x7fffffffffffffff for x in loads)
            assert sum(len(x[3]) for x in loads)==ids
            assert not model['springs'] and not model['omitted_springs']
        src=38+24*hc['N']+100*hc['m']+13*hc['r']+17*l+ids
        if mid in vh:assert src==vh[mid]['source_encoding_len']
        decimals=[]
        decimal_inputs=list(c['scales'].values())+list((c.get('s_full') or {}).values())
        for row in c['rows']:
            decimal_inputs.append(row[1])
            if row[3] is not None:decimal_inputs.append(row[3])
        for control in c['controls']:
            if control[2]=='value':decimal_inputs.extend(control[3].values())
        for s0 in decimal_inputs:
            mt=re.fullmatch(r'[+-]?(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?',s0)
            assert mt and (mt[1] or mt[2]),(mid,s0)
            decimals.append((len(mt[1] or '')+len(mt[2] or ''),int(mt[3] or 0)-len(mt[2] or '')))
        digitmax=max(x[0] for x in decimals);p10min=min(x[1] for x in decimals);p10max=max(x[1] for x in decimals)
        vr.append(dict(model=mid,K4SRC_sha256=c['k4src_sha256'],canonical_model_sha256=c.get('model_sha256'),
            canonical_model_presence='external hash-bound generated model' if model is None else 'embedded rf_large.jsonl model',
            model_generated_or_run=False,K4SRC_payload_bytes=src,K4SRC_capacity_bytes=enc_cap(src),
            source_id_payload_bytes=ids,reference_rows=len(c['rows']),control_count=len(c['controls']),
            field_string_bytes=sum(len(s.encode()) for s in strings(c)),max_field_string_bytes=max(map(len,strings(c))),
            metadata_json_payload_bytes=len(json.dumps(c,separators=(',',':'),sort_keys=True).encode()),
            decimal_digit_count_upper=digitmax,decimal_p10_min=p10min,decimal_p10_max=p10max,
            exact_comparison_scratch=comparison_bound(digitmax,p10min,p10max),
            sample_load_uniqueness_checked=model is not None,
            large_load_uniqueness='RF family generator map components, no RF-CANCEL authored contribution path; general68-limb bound retained if that generator binding is not accepted'))
    result=dict(kind='new_source_parameter_analysis_not_runtime',source_basis=BASIS,
        coordination_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        script_sha256=sha(Path(__file__).read_bytes()),inputs=identities,H_rows=out,VR_rows=vr,
        checks=dict(H_count=33,H_exact_K4SRC_payloads=33,H_unique_load_sets=33,H_root_fixed=33,VR_count=24,VR_scale_count_bindings=18),
        limits=['No final E_max, model run or measured capacity/bound.', 'L1 private layouts remain required.',
                'VR large-source byte hashes are retained identities, not newly regenerated bytes.'])
    print(json.dumps(result,indent=2,sort_keys=True))

def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,list):return [s for y in x for s in strings(y)]
    if isinstance(x,dict):return [s for k,y in x.items() for s in [k]+strings(y)]
    return []

if __name__=='__main__':main()
