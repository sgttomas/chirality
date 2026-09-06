from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent;ROOT=Path.cwd();results=[]
for mf in sorted((P/'WORKERS').glob('DEL-*/OUTPUT_MANIFEST.json')):
 obj=json.loads(mf.read_text()); entries=obj.get('hashes',obj.get('outputs',obj)); errors=[]; seen=set()
 for s,h in entries.items():
  if not isinstance(h,str) or not re.fullmatch('[0-9a-f]{64}',h):continue
  f=ROOT/s if s.startswith('projects/') else mf.parent/s
  if Path(s).is_absolute() or '..' in Path(s).parts:errors.append('nonportable '+s)
  if not f.is_relative_to(mf.parent):errors.append('out of worker scope '+s)
  if f==mf:errors.append('self inclusion')
  if f in seen:errors.append('duplicate path '+s)
  seen.add(f)
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:errors.append('hash '+s)
 required={mf.parent/x for x in ('CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','READ_MANIFEST.json','RETURN.md')}
 if required-seen:errors.append('missing required '+str(sorted(str(x) for x in required-seen)))
 results.append({'manifest':str(mf.relative_to(ROOT)),'sha256':hashlib.sha256(mf.read_bytes()).hexdigest(),'entries':len(seen),'errors':errors,'pass':not errors})
print(json.dumps(results,indent=2));raise SystemExit(0 if all(x['pass'] for x in results) else 1)
