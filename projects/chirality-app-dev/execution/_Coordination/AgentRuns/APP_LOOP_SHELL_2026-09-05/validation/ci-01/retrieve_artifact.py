import pathlib,subprocess,json,hashlib,datetime,zipfile,io,time
D=pathlib.Path(__file__).resolve().parent;argv=['gh','api','repos/sgttomas/chirality/actions/artifacts/9976749587/zip'];start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();p=subprocess.run(argv,capture_output=True,timeout=55)
meta={'argv':argv,'cwd':str(pathlib.Path.cwd()),'started_at':start,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'duration_seconds':time.monotonic()-t,'artifact_id':9976749587,'raw_zip_sha256':hashlib.sha256(p.stdout).hexdigest(),'published_digest':'dc93bcd5f83aa5c278261562344a951478372418dac256582363f3a69b1e6e17','raw_zip_retained':False}
(D/'artifact-download.stderr.log').write_bytes(p.stderr)
if p.returncode:raise SystemExit(p.returncode)
assert meta['raw_zip_sha256']==meta['published_digest']
rows=[]
with zipfile.ZipFile(io.BytesIO(p.stdout)) as z:
 for name in z.namelist():
  if name.endswith('/'):continue
  assert not pathlib.PurePosixPath(name).is_absolute() and '..' not in pathlib.PurePosixPath(name).parts
  assert name.endswith('.json')
  data=z.read(name);parsed=json.loads(data);path=D/'published-summaries'/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
  rows.append({'path':name,'sha256':hashlib.sha256(data).hexdigest(),'status':parsed.get('status'),'bytes':len(data)})
meta['extracted']=rows;(D/'artifact-download.command.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
