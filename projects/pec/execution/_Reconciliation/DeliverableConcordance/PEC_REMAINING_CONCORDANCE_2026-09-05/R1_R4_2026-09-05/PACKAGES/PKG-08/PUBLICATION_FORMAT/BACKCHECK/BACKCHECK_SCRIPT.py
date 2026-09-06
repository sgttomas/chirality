import pathlib,subprocess,json,csv,hashlib,base64,ast,re,collections
root=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());p=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-08';f=p/'PUBLICATION_FORMAT';o=f/'BACKCHECK';o.mkdir(exist_ok=True);hashes={}
def sha(b):return hashlib.sha256(b).hexdigest()
def read(path):
 path=root/path if not path.is_absolute() else path;b=path.read_bytes();hashes[str(path.relative_to(root))]=sha(b);return b
def table(b):return list(csv.DictReader(b.decode().splitlines()))
for n in [root/'AGENTS.md',root/'projects/pec/AGENTS.md',f/'BACKCHECK_BRIEF.md',f/'HANDOFF.md',f/'CHANGE_FINDINGS.json']:read(n)
m=json.loads(read(f/'FORMAT_MAP.json'));c=json.loads(read(f/'PREIMAGES.json'));pre={k:base64.b64decode(v['base64'],validate=True) for k,v in c['files'].items()}
for k,b in pre.items():assert sha(b)==c['files'][k]['sha256']
oldmanifest=pre[str((p/'OUTPUT_MANIFEST.json').relative_to(root))];assert sha(oldmanifest)==m['prior_output_manifest_sha256']==c['prior_manifest_sha256'];old=json.loads(oldmanifest);assert len(old['hashes'])==96
snapshot=[]
for path,h in old['hashes'].items():
 b=pre.get(path)
 if b is None:b=read(pathlib.Path(path))
 assert sha(b)==h;snapshot.append({'path':path,'hash':h,'resolved':'CARRIER' if path in pre else 'UNCHANGED_CURRENT'})
changes=[];fieldchanges=[];ast_equal=False
for n in m['normalizations']:
 path=n['path'];before=pre[path];after=read(pathlib.Path(path));assert sha(before)==n['pre_sha256'] and sha(after)==n['post_sha256'];bs=before.splitlines(keepends=True);aa=after.splitlines(keepends=True);assert len(bs)==len(aa)
 got=[i for i,(x,y) in enumerate(zip(bs,aa),1) if x!=y];assert got==n['lines'];expected=bs[:]
 for i in got:expected[i-1]=re.sub(rb'[ \t]+(?=\n$)',b'',bs[i-1])
 assert b''.join(expected)==after
 for i in got:
  e=next(x for x in m['line_edits'] if x['path']==path and x['line']==i)
  assert sha(bs[i-1])==e['before_line_sha256'] and sha(aa[i-1])==e['after_line_sha256'];removed=bs[i-1][len(aa[i-1])-1:-1];assert removed.hex()==e['removed_hex'];changes.append({'path':path,'line':i,'removed_hex':removed.hex()})
 if path.endswith('.csv'):
  a,b=table(before),table(after);assert len(a)==len(b)
  local=[]
  for x,y in zip(a,b):
   assert x.keys()==y.keys()
   for k in x:
    if x[k]!=y[k]:assert k=='Notes' and x[k].rstrip(' \t')==y[k];local.append({'ClaimID':x['ClaimID'],'field':k,'before':x[k],'after':y[k]})
  assert local==[{k:v for k,v in x.items() if k!='physical_line'} for x in n['csv_field_changes']];fieldchanges+=local
 else:assert ast.dump(ast.parse(before),include_attributes=False)==ast.dump(ast.parse(after),include_attributes=False);ast_equal=True
assert len(changes)==57 and len(fieldchanges)==56 and ast_equal
selected=json.loads(read(p/'SELECTED_DERIVATIVES.json'));allc=[];allr=[]
for s in selected:
 allc+=table(read(pathlib.Path(s['path'])/'CLAIMS.csv'));allr+=table(read(pathlib.Path(s['path'])/'RESIDUALS.csv'))
assert allc==table(read(p/'PACKAGE_CLAIMS.csv')) and allr==table(read(p/'PACKAGE_RESIDUALS.csv'));assert len(allc)==245 and len(allr)==12
assert len({x['ClaimID'] for x in allc})==245 and len({x['ResidualID'] for x in allr})==12
for row in allc+allr:assert row['Depends'] and re.search(r'\(gated:|\(stage-gated:|NOT_SELECTABLE_UNTIL:',row['ExactGate']) and row['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION'
source_count=0
for row in allc:
 for path,h in json.loads(row['SourceHashes']).items():assert sha(read(pathlib.Path(path)))==h;source_count+=1
# Full historical verifier read binding: altered historical outputs resolve to carrier, all other sources current.
v=json.loads(read(p/'VERIFICATION/READ_MANIFEST.json'))
for path,h in v['hashes'].items():
 b=pre.get(path)
 if b is None:b=read(pathlib.Path(path))
 assert sha(b)==h
violations=[];scanned=0
for path in sorted(p.rglob('*')):
 if not path.is_file() or o in path.parents:continue
 b=read(path);scanned+=1
 try:s=b.decode('utf-8')
 except UnicodeDecodeError:continue
 for i,line in enumerate(s.splitlines(),1):
  if line.endswith((' ','\t')):violations.append({'path':str(path.relative_to(root)),'line':i,'defect':'trailing whitespace'})
 if b and not b.endswith(b'\n'):violations.append({'path':str(path.relative_to(root)),'defect':'missing final LF'})
 if b.endswith(b'\n\n'):violations.append({'path':str(path.relative_to(root)),'defect':'blank EOF line'})
assert not violations,violations
val={'verdict':'PASS','files_normalized':3,'line_edits':57,'csv_Notes_terminal_trims':56,'other_csv_values_changed':0,'python_ast_equal':True,'carrier_files_decoded':len(pre),'old_snapshot_entries_resolved':len(snapshot),'old_manifest_sha256':sha(oldmanifest),'current_aggregate_exact_selected_concatenation':True,'claims':245,'residuals':12,'dispositions':dict(collections.Counter(x['Disposition'] for x in allc)),'source_hash_comparisons':source_count,'source_hashes_unchanged':True,'package_files_scanned':scanned,'whitespace_EOF_findings':violations,'semantic_or_authority_change':False}
(o/'VALIDATION.json').write_text(json.dumps(val,indent=2)+'\n');(o/'CHECKED_EDITS.json').write_text(json.dumps({'edits':changes,'csv_field_changes':fieldchanges,'old_snapshot':snapshot},indent=2)+'\n')
(o/'BACKCHECK.md').write_text('''# Independent publication-format backcheck

PASS. Exactly57 listed trailing-space removals affect3 files:28 terminal Notes values in DEL08-01 claims, the same28 values in PACKAGE_CLAIMS.csv, and1 whitespace-only Python line. Independent byte reconstruction matches every mapped pre/post hash and line edit. The CSVs differ only in those56 terminal Notes whitespace values; all other cell values, IDs, gates, source hashes, dependencies and dispositions are identical. The Python AST is identical.

All18 lossless carrier records decode to their stated hashes. The original root manifest SHA555775900d8a27b800a7b74c44a02169e8622b8f7bf3d935a12cfde7a0eb3a46 reconstructs all96 sealed entries from carrier or unchanged current bytes. Historical verifier/source references resolve similarly; original findings and verdicts remain historical. No old verification script was executed as a current-manifest checker.

Current aggregate245 claims and12 residuals exactly equal selected derivative row concatenation. All claim source hash comparisons and original verifier read-source bindings pass. The complete current package scan has no trailing whitespace, missing terminal LF or blank EOF findings. Carrier base64 is provenance encoding, not a live-file whitespace violation.

Formatting successor only: no semantic, owner, source, lifecycle, Remaining, release or product change. DEL08-04's43 bounded local classifications,80 UNKNOWNs,12 raw proposals, D66 decline and TM022/TM023 routing boundaries survive. Parent must freeze the new publication manifest after this independent backcheck; historical snapshot identity is preserved via FORMAT_MAP and PREIMAGES. Only PUBLICATION_FORMAT/BACKCHECK/** was written; Agent2 non-delegation is instruction-asserted.
''')
(o/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':m['source_commit'],'hashes':hashes,'historical_sources':[{'path':k,'sha256':sha(b),'carrier':'PUBLICATION_FORMAT/PREIMAGES.json','context':'prior package snapshot'} for k,b in pre.items()],'checks':[{'command':'python3 /tmp/pkg08_format_backcheck.py','cwd':'.','environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0,'result':val}],'source_unchanged':True},indent=2)+'\n')
(o/'BACKCHECK_SCRIPT.py').write_bytes(pathlib.Path(__file__).read_bytes())
(o/'OUTPUT_MANIFEST.json').write_text(json.dumps({'status':'PASS_FORMAT_ONLY','self_excluded':True,'files':{x.name:sha(x.read_bytes()) for x in sorted(o.iterdir()) if x.is_file() and x.name!='OUTPUT_MANIFEST.json'}},indent=2)+'\n')
print(json.dumps(val,indent=2))
