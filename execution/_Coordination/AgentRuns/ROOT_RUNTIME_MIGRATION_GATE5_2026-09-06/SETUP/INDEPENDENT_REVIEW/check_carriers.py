from pathlib import Path
import csv,re,json,subprocess,hashlib,sys
OUT=Path(__file__).parent
rs=list(csv.DictReader(open('execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/RUNTIME_METADATA_BINDINGS.csv')))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def defs(t,prefix):
 result={}
 for m in re.finditer(r'^- \*\*('+prefix+r'-\d+)(.*?)(?=\n- \*\*|\n\s*\n|\Z)',t,re.M|re.S):result[m.group(1)]=re.sub(r'\s+',' ',m.group(2)).strip()
 return result
for r in rs:
 ident=r['DeliverableID'].split('_')[0]
 if ident not in sys.argv[1:]:continue
 folder=Path(r['Folder']);prod=folder/'ScopeOfWork.md';source=Path(r['SourceContract']);text=prod.read_text();old=source.read_text()
 status=folder/'_STATUS.md';status.read_text();memory={str(f):sha(f) for f in [folder/'_MEMORY.md',folder/'MEMORY.md'] if f.is_file() and f.read_text() is not None}
 checks={'production_sha256':sha(prod),'source_sha256':sha(source),'status_sha256':sha(status),'paired_memory':memory,'author_validation_sha256':sha(folder/'_run_records/SCA005_INIT/Validation.json'),'definitions':{},'commands':[]}
 for prefix in ['REQ','CLM','OUT','VER','AC']:
  sd,pd=defs(old,prefix),defs(text,prefix);checks['definitions'][prefix]={'source_count':len(sd),'destination_count':len(pd),'missing':list(sd.keys()-pd.keys()),'changed':{k:{'source':sd[k],'destination':pd.get(k)} for k in sd if sd[k]!=pd.get(k)}}
 for tool,args in [('validate_scope_of_work.py',['--json']),('derive_review_checklist.py',[]),('check_boundary_owner_resolution.py',['--show-not-checkable'])]:
  cmd=['python3','tools/scope_of_work/'+tool,str(folder),*args];v=subprocess.run(cmd,text=True,capture_output=True);checks['commands'].append({'argv':cmd,'exit':v.returncode,'stdout':v.stdout,'stderr':v.stderr})
 (OUT/(ident+'_CHECKS.json')).write_text(json.dumps(checks,indent=2)+'\n')
 print(ident,checks['production_sha256'],{k:(v['source_count'],v['destination_count'],len(v['changed'])) for k,v in checks['definitions'].items()},[x['exit'] for x in checks['commands']])
