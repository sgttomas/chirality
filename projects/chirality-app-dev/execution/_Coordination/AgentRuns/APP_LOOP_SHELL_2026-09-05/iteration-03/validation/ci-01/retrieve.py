import sys,pathlib,subprocess,json,hashlib,datetime,re,time
D=pathlib.Path(__file__).resolve().parent
kind,name=sys.argv[1:]
commands={'metadata':['gh','run','view','33994563156','--repo','sgttomas/chirality','--json','databaseId,workflowName,event,headSha,headBranch,status,conclusion,jobs,url,createdAt,updatedAt'],'artifacts':['gh','api','repos/sgttomas/chirality/actions/runs/33994563156/artifacts'],'logs':['gh','run','view','33994563156','--repo','sgttomas/chirality','--log']}
argv=commands[kind];start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();p=subprocess.run(argv,capture_output=True,text=True,timeout=55)
def redact(s):
 s=re.sub(r'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-ant-[A-Za-z0-9_-]{20,})\b','[REDACTED_TOKEN]',s)
 return re.sub(r'(?i)(authorization:\s*(?:bearer|token)\s+)\S+',r'\1[REDACTED]',s)
out=redact(p.stdout);err=redact(p.stderr)
(D/(name+'.output.json')).write_text(json.dumps({'stdout':out,'stderr':err},indent=2)+'\n')
if kind!='logs' and p.returncode==0:(D/(name+'.stdout.json')).write_text(out)
meta={'argv':argv,'cwd':str(pathlib.Path.cwd()),'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':time.monotonic()-t,'exit_code':p.returncode,'environment':'existing gh authentication; no credential values captured','redaction_applied':out!=p.stdout or err!=p.stderr,'stdout_sha256':hashlib.sha256(out.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(err.encode()).hexdigest()}
(D/(name+'.command.json')).write_text(json.dumps(meta,indent=2)+'\n')
if kind=='metadata' and p.returncode==0:
 d=json.loads(out);assert d['headSha']=='239c8f2a53397f88f16e3d56ecbba9af83829246' and d['event']=='workflow_dispatch';print(json.dumps({'status':d['status'],'conclusion':d['conclusion'],'jobs':[{'name':j['name'],'conclusion':j['conclusion'],'steps':[{'name':s['name'],'conclusion':s['conclusion'],'status':s['status']} for s in j['steps'] if s['status']!='pending']} for j in d['jobs']]}))
else: print(json.dumps(meta))
raise SystemExit(p.returncode)
