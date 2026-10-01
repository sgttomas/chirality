#!/usr/bin/env python3
"""Source grammar/record arithmetic only; no Rust, model or runner import."""
import hashlib
import json
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
HERE=Path(__file__).resolve().parent
P=Path('projects/chirality-piping')
FK=P/'core/solver/frame_kernel'
H=P/'core/solver/performance_harness'
VR=P/'validation/benchmarks/numerical_robustness'
K=FK/'src/structural/retained'
BASIS='3bddc2b05f6106e969c7cf43373b230845c7cc66'

def sha(x):return hashlib.sha256(x).hexdigest()
def text(p):return (ROOT/p).read_text()
def split_top(s):
    depth=0;start=0;out=[]
    for i,c in enumerate(s):
        if c in '([{<':depth+=1
        elif c in ')]}>':depth-=1
        elif c==',' and depth==0:out.append(s[start:i].strip());start=i+1
    if s[start:].strip():out.append(s[start:].strip())
    return out
def enum_source(path,name):
    s=re.sub(r'//[^\n]*','',text(path));m=re.search(r'pub enum '+name+r'\s*\{',s);assert m,name
    start=m.end();depth=1;i=start
    while depth:
        if s[i]=='{':depth+=1
        elif s[i]=='}':depth-=1
        i+=1
    return split_top(s[start:i-1])

def main():
    ledger=json.loads((HERE/'INPUTS.json').read_text())
    runtime=Path(tempfile.gettempdir())/ledger['runtime_directory_name']
    for entry in ledger['inputs']:
        origin=entry['origin']
        if origin.startswith('<RESPONSE_RUNTIME>/'):path=runtime/origin.split('/',1)[1]
        elif origin.startswith('<OWNER_CARGO_HOME>/'):path=Path.home()/'.cargo'/origin.split('/',1)[1]
        else:path=ROOT/origin
        assert sha(path.read_bytes())==entry['sha256'],'input drift: '+origin
    consulted=[K/'source.rs',K/'recover.rs',K/'adaptive.rs',K/'wide.rs',K/'ledger.rs',FK/'src/exact_sum.rs',
        FK/'src/structural.rs',FK/'src/rigid_body.rs',FK/'src/lib.rs',FK/'src/structural/sparse.rs',
        H/'src/bin/k6_observe/main.rs',H/'src/bin/k6_observe/w1.rs',H/'src/k6/w1/staged.rs',
        H/'src/k6/counts.rs',H/'src/k6/canonical.rs',H/'src/k6/w1/rows.rs',H/'observations/k6b/counts.jsonl',
        VR/'cases/rf_large.jsonl',VR/'cases/expected_unresolved.json']
    pins=[]
    for p in consulted:
        b=(ROOT/p).read_bytes();assert b==subprocess.check_output(['git','show',BASIS+':'+str(p)]),str(p)
        pins.append(dict(path=str(p),sha256=sha(b)))
    # Raw source-token lengths conservatively dominate decoded literal bytes.
    static=max(len(x.encode()) for p in [FK/'src/lib.rs',FK/'src/structural.rs',FK/'src/rigid_body.rs',K/'wide.rs',FK/'src/structural/sparse.rs']
               for x in re.findall(r'"((?:[^"\\]|\\.)*)"',text(p)))
    f64=2+1074+53+8 # sign/point + exact binary64 fractional span + significand upper + exponent syntax
    bounds={'usize':20,'u64':20,'u32':10,'u8':3,'i64':20,'bool':5,'f64':f64,"&'static str":2+6*static}
    def named(name,fields):return len(name)+5+sum(len(k)+2+bound(t) for k,t in fields)+(2*max(0,len(fields)-1))
    schema={}
    for name,path in [('Component',K/'source.rs'),('MemberProperty',K/'source.rs'),('End',K/'recover.rs'),('Kind',K/'recover.rs'),('BudgetScope',K/'adaptive.rs'),('SumError',FK/'src/exact_sum.rs'),('WideError',K/'wide.rs'),('LedgerRefusal',K/'ledger.rs'),('QuantityId',K/'recover.rs'),('SourceError',K/'source.rs'),('AttemptStop',K/'adaptive.rs'),('AttemptReason',K/'adaptive.rs'),('AttemptOutcome',K/'adaptive.rs'),('AttemptRole',K/'adaptive.rs'),('Refusal',K/'adaptive.rs'),('UnresolvedReason',K/'adaptive.rs'),('FrameKernelError',FK/'src/lib.rs')]:
        schema[name]=enum_source(path,name)
    def bound(t):
        t=t.strip()
        if t=='Dof':return named('Dof',[('node','u32'),('component','Component')])
        if t in bounds:return bounds[t]
        if t.startswith('Option<'):return max(4,6+bound(t[7:-1]))
        if t.startswith('['):
            e,n=t[1:-1].split(';');n=int(n);return 2+n*bound(e)+2*max(0,n-1)
        if t=='StructuralError':
            # geometry_first -> assess_rigid_body/Expansion: these two variants only.
            return max(len('InvalidInput')+2+bound("&'static str"),len('Range')+2+bound("&'static str"))
        assert t in schema,t
        vs=[]
        for v in schema[t]:
            m=re.fullmatch(r'(\w+)\s*(.*)',v,re.S);name,tail=m.groups()
            if not tail or tail.startswith('='):n=len(name)
            elif tail.startswith('{'):
                fields=[]
                for f in split_top(tail[1:-1]):
                    key,ty=f.split(':',1);fields.append((key.strip(),ty.strip()))
                n=named(name,fields)
            elif tail.startswith('('):
                ts=split_top(tail[1:-1]);n=len(name)+2+sum(bound(x) for x in ts)+2*max(0,len(ts)-1)
            else:raise AssertionError(v)
            vs.append(dict(variant=name,max_debug_bytes=n))
        bounds[t]=max(v['max_debug_bytes'] for v in vs)
        enum_rows[t]=vs
        return bounds[t]
    enum_rows={}
    for t in schema:bound(t)
    bounds['Dof']=bound('Dof')
    reason=max(bound('SourceError'),bound('AttemptOutcome'),bound('Refusal')+len('Refused()'),bound('UnresolvedReason')+len('Unresolved()'))
    source_files=[H/'src/bin/k6_observe/main.rs',H/'src/bin/k6_observe/w1.rs']
    occurrences=[]
    for p in source_files:
        s=text(p)
        for m in re.finditer(r'\.(n|s|b|opt_n|opt_s|null|hex|f)\(\s*"((?:[^"\\]|\\.)*)"',s):
            occurrences.append(dict(path=str(p),line=s[:m.start()].count('\n')+1,method=m[1],key=m[2],multiplicity_upper=1,key_bytes_upper=len(m[2].encode())))
        for m in re.finditer(r'\.(n|s|b|opt_n|opt_s|null|hex|f)\(\s*&format!\("([^"]+)"',s):
            key=re.sub(r'\{[^}]*\}','x'*20,m[2])
            occurrences.append(dict(path=str(p),line=s[:m.start()].count('\n')+1,method=m[1],key_template=m[2],multiplicity_upper=19,key_bytes_upper=len(key.encode())))
    # kind inserted by Line::new even though its quoted value is passed via a variable.
    occurrences.append(dict(path='Line::new',key='kind',multiplicity_upper=1,key_bytes_upper=4))
    counts=[json.loads(s) for s in text(H/'observations/k6b/counts.jsonl').splitlines() if s.strip()]
    modelid=max(len(x['model']) for x in counts)
    h_static=max(len(x.encode()) for p in source_files for x in re.findall(r'"((?:[^"\\]|\\.)*)"',text(p)))
    value=max(39,f64,reason,static,modelid,240*4)
    for x in occurrences:
        assert re.fullmatch(r'[A-Za-z0-9_]+',x.get('key',re.sub(r'\{[^}]*\}','x'*20,x.get('key_template',''))))
        method=x.get('method','s');key=x.get('key','')
        if method in ['n','opt_n']:v=39
        elif method=='b':v=5
        elif method=='null':v=4
        elif method=='hex':v=18
        elif method=='f':v=f64
        else:
            sv=reason if ('reason' in key or 'error' in key) else max(h_static,modelid,240*4)
            v=2+6*sv
        x['encoded_value_bytes_upper']=v
    # Common static-key multiset contains every reachable W1/counts Line;
    # extra occurrences in other branches only increase this envelope.
    line_bytes=3+sum(x['multiplicity_upper']*(x['key_bytes_upper']+x['encoded_value_bytes_upper']+4) for x in occurrences)
    bstr=lambda n:max(8,2*n)
    mstr=lambda n:bstr(n)+bstr(n)//2
    line_helper=mstr(reason)+mstr(min(reason,960))+mstr(max(x['key_bytes_upper'] for x in occurrences))+mstr(max(39,f64))+mstr(6)
    rows=[json.loads(s) for s in text(VR/'cases/rf_large.jsonl').splitlines() if s.strip()]
    def shape(v):
        arrays=Counter();objects=Counter();string_bytes=0;key_bytes=0;longest=0;depth_max=0
        def visit(x,depth):
            nonlocal string_bytes,key_bytes,longest,depth_max
            depth_max=max(depth_max,depth)
            if isinstance(x,str):string_bytes+=len(x.encode());longest=max(longest,len(x.encode()))
            elif isinstance(x,list):
                arrays[len(x)]+=1
                for y in x:visit(y,depth+1)
            elif isinstance(x,dict):
                objects[len(x)]+=1
                for k,y in x.items():key_bytes+=len(k.encode());longest=max(longest,len(k.encode()));visit(y,depth+1)
        visit(v,0)
        return dict(array_length_histogram=dict(sorted(arrays.items())),object_key_count_histogram=dict(sorted(objects.items())),string_payload_bytes=string_bytes,key_payload_bytes=key_bytes,longest_string_bytes=longest,maximum_depth=depth_max)
    def stats(v):
        if isinstance(v,str):return (1,len(v.encode()),0,0,len(v.encode()))
        if isinstance(v,list):
            xs=[stats(x) for x in v];return (sum(x[0] for x in xs),sum(x[1] for x in xs),1+sum(x[2] for x in xs),sum(x[3] for x in xs),max([0]+[x[4] for x in xs]))
        if isinstance(v,dict):
            xs=[stats(x) for x in v.values()];return (len(v)+sum(x[0] for x in xs),sum(len(k.encode()) for k in v)+sum(x[1] for x in xs),sum(x[2] for x in xs),1+sum(x[3] for x in xs),max([0]+[len(k.encode()) for k in v]+[x[4] for x in xs]))
        return (0,0,0,0,0)
    result=dict(kind='source_finish_symbolic_envelope_parameters_not_Emax',product_basis=BASIS,actual_coordination=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),script_sha256=sha(Path(__file__).read_bytes()),script_origin='new source_finish_01 record; not a historical script at product basis',inputs=pins,
        formatting=dict(static_literal_bytes_upper=static,f64_no_precision_text_upper=f64,type_debug_upper=bounds,variants=enum_rows,reason_upper=reason,
            line_field_occurrences=occurrences,dynamic_occurrence_multiplier=19,dynamic_placeholder_bytes_upper=20,value_bytes_upper=value,line_encoded_bytes_upper=line_bytes,line_requested_move_upper=mstr(line_bytes),helpers_requested_upper=line_helper,
            caveat='Deliberately broad source-derived common envelope; duplicate/non-W1 key occurrences retained. Applies only reachable W1 scalar/reason value types, not arbitrary Display or unrelated modes.'),
        vr_family=dict(file=str(VR/'cases/rf_large.jsonl'),bytes=len((ROOT/VR/'cases/rf_large.jsonl').read_bytes()),cases=[dict(id=r['id'],rows=len(r['rows']),controls=len(r['controls']),strings_arrays_objects_stats=stats(r),line_json_shape=shape(r)) for r in rows]),
        expected_unresolved=dict(file=str(VR/'cases/expected_unresolved.json'),bytes=len((ROOT/VR/'cases/expected_unresolved.json').read_bytes()),shape=shape(json.loads(text(VR/'cases/expected_unresolved.json')))),
        inputs_not_supplied=['future exact argv and path byte lengths','twelve large-model bytes/shapes bound by their existing hashes','L1 and consumer layout values'],runtime_execution=False)
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
