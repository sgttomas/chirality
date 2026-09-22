"""Line parity: every non-empty legacy line (heading markers and blockquote prefix stripped) present in the SoW at a given revision."""
import subprocess, sys, re
tree, d, legacy_rev, sow_rev = sys.argv[1:5]
def show(rev, path):
    r = subprocess.run(["git","-C",tree,"show",f"{rev}:{path}"],capture_output=True,text=True)
    return r.stdout if r.returncode==0 else None
def norm(l):
    l=l.strip()
    while l.startswith(">"): l=l[1:].strip()
    l=re.sub(r"^#+\s*","",l)
    return l.strip()
sow = show(sow_rev, f"{d}/ScopeOfWork.md")
sowset = {norm(l) for l in sow.splitlines()}
tot=miss=0; misses=[]
for f in ["Datasheet.md","Specification.md","Procedure.md","Guidance.md"]:
    t=show(legacy_rev,f"{d}/{f}")
    if t is None: print("absent",f); continue
    for l in t.splitlines():
        n=norm(l)
        if not n: continue
        tot+=1
        if n not in sowset: miss+=1; misses.append((f,n[:100]))
print(f"legacy_nonempty={tot} missing={miss} sow_rev={sow_rev}")
for m in misses[:15]: print("  MISS",m)
