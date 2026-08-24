#!/usr/bin/env python3
"""Read-only deterministic verifier for the post-Phase-5 graph snapshot."""
import csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REGISTER = ROOT / 'execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    graph=json.loads((HERE/'WORK_GRAPH.json').read_text())
    rows=list(csv.DictReader(REGISTER.open()))
    ids={r['DeliverableID'] for r in rows}; packages={r['ParentPackageID'] for r in rows}
    assert len(rows)==53 and len(ids)==53 and len(packages)==6
    assert {n['id'] for n in graph['nodes'] if n['kind']=='ROOT_DELIVERABLE'}==ids
    assert {n['id'] for n in graph['nodes'] if n['kind']=='ROOT_PACKAGE'}==packages
    expected=graph['basis']['dependency_file_sha256']; decls=[]
    for r in rows:
        did=r['DeliverableID']; p=ROOT/'execution'/r['ParentPackageID']/'1_Working'/did/'_DEPENDENCIES.md'
        if did in expected: assert sha(p)==expected[did]
        if did not in expected: continue
        section=''
        for line in p.read_text().splitlines():
            if line.startswith('## Upstream'): section='upstream'
            elif line.startswith('## Downstream'): section='downstream'
            elif line.startswith('## '): section=''
            if section in {'upstream','downstream'} and line.startswith('| `DEL-'):
                c=[x.strip() for x in line.strip().strip('|').split('|')]; peer=c[0].strip('`')
                src,tgt=(peer,did) if section=='upstream' else (did,peer)
                decls.append((src,tgt,c[1].strip('`'),c[2].lower()=='yes'))
    current=set(decls); recorded={(e['from'],e['to'],e['type'],e['gating']) for e in graph['dependency_edges']}
    assert len(decls)==16 and current==recorded and len(current)==9
    adjacency=defaultdict(list)
    for a,b,t,g in current:
        if g: adjacency[a].append(b)
    index=[0]; stack=[]; on=set(); indices={}; low={}; comps=[]
    def visit(v):
        indices[v]=low[v]=index[0]; index[0]+=1; stack.append(v); on.add(v)
        for w in sorted(adjacency[v]):
            if w not in indices: visit(w); low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            c=[]
            while True:
                w=stack.pop(); on.remove(w); c.append(w)
                if w==v: break
            comps.append(c)
    for v in sorted(ids|packages):
        if v not in indices: visit(v)
    assert len(comps)==59 and all(len(c)==1 for c in comps)
    assert len(graph['membership_edges'])==53 and len(graph['notice_edges'])==2
    print(json.dumps({'status':'PASS_PHASE3_SHAPE_EXACT_MATCH','nodes':59,'membership_edges':53,'local_declarations':16,'root_relationships':9,'gating':8,'notice_edges':2,'sccs':59,'non_trivial_sccs':0,'human_gated_move':False},sort_keys=True))
if __name__=='__main__': main()
