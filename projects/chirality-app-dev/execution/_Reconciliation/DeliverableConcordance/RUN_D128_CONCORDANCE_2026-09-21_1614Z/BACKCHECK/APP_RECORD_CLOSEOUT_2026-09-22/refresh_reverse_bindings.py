# One-time prepublication binding utility; after publication use --check only.
from pathlib import Path
import csv,io,re,json,hashlib,collections,argparse
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--check',action='store_true');args=ap.parse_args();assert not (args.write and args.check)
root=Path('projects/chirality-app-dev/execution');run=root/'_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z';home=run/'BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22';p=home/'REVERSE_OWNERSHIP.csv'
rows=list(csv.DictReader(p.open()));fields=list(rows[0]);source=list(csv.DictReader((run/'R3/UNMAPPED_IMPLEMENTATION.csv').open()));source=[r for r in source if r.get('CapabilityID','')!='#END']
h=lambda b:hashlib.sha256(b).hexdigest()
assert h((run/'R3/UNMAPPED_IMPLEMENTATION.csv').read_bytes())=='be3af4989fb9fb6f06593122a2c715d25f1bc2fcf8838c48aa76ce872c18a833','Frozen reverse discovery source changed'
assert len(rows)==107 and len({r['CapabilityID'] for r in rows})==107
orig={r['CapabilityID']:r for r in source};assert set(orig)=={r['CapabilityID'] for r in rows}
lookup={}
for f in (run/'R2').rglob('*claims.csv'):
 for r in csv.DictReader(f.open()):lookup[r['ClaimKey']]=r
updaters={'CAP-ELECTRON-030','CAP-SHELL-014','CAP-SHELL-015'};citations=0;changed_hashes=set()
for r in rows:
 assert r['OriginalRowSHA256']==h(json.dumps(orig[r['CapabilityID']],sort_keys=True,separators=(',',':')).encode())
 for copied,original in [('OriginalCapability','Capability'),('OriginalReach','Reach'),('OriginalState','State'),('EvidencePaths','Paths')]:
  assert r[copied]==orig[r['CapabilityID']][original],(r['CapabilityID'],'Original source field mismatch',copied)
 if r['CapabilityID'] in updaters:
  r['AppClaimKeys']=r['AppClaimKeys'].replace('DEL-02-01#SEC-3','DEL-02-01#CLM-009')
  r['RemainingTask']='Accepted carrier propagation is applied in DEL-09-05 CLM-005 and DEL-02-01 CLM-009. Preserve the current verification hooks for manual/startup/six-hour fixed-source checks, truthful states and explicit browser handoff; this record pass supplies no new runtime/native result and grants no automatic install, restart or publication.'
  r['DecisionInterfaceVerification']='Decision: prior owner continuation accepted checker and later scheduling. Interface: update availability and explicit download, now carried by DEL-09-05 CLM-005 and DEL-02-01 CLM-009. Verification: named maintained update tests and candidate-bound native startup/cadence/browser evidence; no new execution result asserted.'
 old_citations=r['CurrentSourceCitation'].split(';');new=[]
 for key in r['AppClaimKeys'].split(';'):
  if key=='NONE':continue
  assert key in lookup,key
  did,claim=key.split('#');paths=list(root.glob('PKG-*/1_Working/'+did+'*/ScopeOfWork.md'));assert len(paths)==1,(key,paths)
  path=paths[0];lines=path.read_text().splitlines()
  if claim.startswith('CLM-'):
   base=claim.split('.')[0];matches=[i for i,l in enumerate(lines,1) if re.match(r'^#{2,3}\s+'+re.escape(base)+r'\b',l)]
   assert len(matches)==1,(key,matches)
   ln=matches[0]
  else:
   assert claim.startswith('SEC-'),key
   needle='### Current acceptance obligations' if key=='DEL-02-04#SEC-4' else '### Current responsibility'
   matches=[i for i,l in enumerate(lines,1) if l==needle];assert matches,key
   ln=matches[-1] if did in {'DEL-02-01','DEL-02-02','DEL-02-04'} else matches[0]
  new.append(str(path)+':'+str(ln));citations+=1
 for c in old_citations:
  if c!='NONE' and '/ScopeOfWork.md:' not in c and c not in new:new.append(c)
 r['CurrentSourceCitation']=';'.join(dict.fromkeys(new)) if new else 'NONE'
 hashes=json.loads(r['SourceHashes'])
 required={s.strip().split('#')[0] for col in ['EvidencePaths','GoverningSources'] for s in r[col].split(';') if s.strip() and s!='NONE'}
 required.update(re.sub(r':\d+$','',s.strip()) for s in r['CurrentSourceCitation'].split(';') if s.strip()!='NONE')
 required.add(str(run/'R3/UNMAPPED_IMPLEMENTATION.csv'))
 assert required<=set(hashes),(r['CapabilityID'],'Missing cited source binding',sorted(required-set(hashes)))
 for fp,old in hashes.items():
  now=h(Path(fp).read_bytes())
  if now!=old:changed_hashes.add(fp)
  hashes[fp]=now
 r['SourceHashes']=json.dumps(hashes,sort_keys=True,separators=(',',':'))
f=io.StringIO(newline='');w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows);data=f.getvalue().encode()
if args.check:assert p.read_bytes()==data,'Reverse-map current citations, applied-task wording or source hashes differ; refresh before publication and independently backcheck'
if args.write:p.write_bytes(data)
print(json.dumps({'mode':'APPLIED' if args.write else ('CHECKED' if args.check else 'PREVIEW'),'rows':len(rows),'current_claim_citations':citations,'hashes_to_refresh':len(changed_hashes),'changed_hash_paths':sorted(changed_hashes),'result_sha256':h(data),'counts':dict(collections.Counter(r['Disposition'] for r in rows))},indent=2))
