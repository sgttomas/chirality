"""Line parity: legacy four documents at <commit>^ vs ScopeOfWork.md at frozen HEAD. Read-only git show."""
import subprocess,sys,os,glob
F=os.environ['FROZEN']; delid=sys.argv[1]; commit=sys.argv[2]
d=os.path.relpath(glob.glob(f"{F}/projects/chirality-app-dev/execution/PKG-*/1_Working/{delid}_*")[0],F)
def show(rev,p):
    r=subprocess.run(['git','-C',F,'show',f'{rev}:{p}'],capture_output=True,text=True)
    return r.stdout if r.returncode==0 else None
sow=open(os.path.join(F,d,'ScopeOfWork.md')).read()
norm=lambda s:' '.join(s.replace('>','').split())
sown=norm(sow)
tot=miss=0; ex=[]
for doc in ['Datasheet.md','Specification.md','Guidance.md','Procedure.md']:
    t=show(commit+'^',f'{d}/{doc}')
    if t is None: print('absent',doc); continue
    for ln in t.split('\n'):
        s=norm(ln)
        if not s or set(s)<=set('-|: '): continue
        tot+=1
        if s not in sown: miss+=1; ex.append((doc,s[:140]))
print(delid,'lines',tot,'missing',miss)
for e in ex[:8]: print(' ',e)
