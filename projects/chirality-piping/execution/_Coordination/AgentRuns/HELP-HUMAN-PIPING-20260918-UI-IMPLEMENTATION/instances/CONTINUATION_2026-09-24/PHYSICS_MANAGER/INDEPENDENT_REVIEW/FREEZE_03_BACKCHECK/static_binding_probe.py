"""Read-only unified-diff inversion and hash verification; no Git or product execution."""
from pathlib import Path
import json, hashlib, re
ROOT=Path.cwd()
PM=ROOT/"projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER"
OUT=PM/"INDEPENDENT_REVIEW/FREEZE_03_BACKCHECK"
F=PM/"FREEZE_03"
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((F/"SOURCE_MANIFEST.json").read_text())
def invert(patch):
 lines=patch.read_text().splitlines(keepends=True); sections=[]; i=0
 while i<len(lines):
  if not lines[i].startswith("--- "): i+=1;continue
  old=lines[i][4:].strip(); new=lines[i+1][4:].strip(); i+=2
  path=new[2:] if new.startswith("b/") else new
  current=(F/"source"/path).read_text().splitlines(keepends=True)
  result=[]; cursor=0; hunks=0
  while i<len(lines) and not lines[i].startswith("diff --git ") and not lines[i].startswith("--- "):
   if not lines[i].startswith("@@ "): i+=1;continue
   match=re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@",lines[i]);assert match,lines[i]
   newstart=int(match[3]); newcount=int(match[4] or 1); oldcount=int(match[2] or 1)
   start=newstart-1 if newcount else newstart
   assert start>=cursor
   result.extend(current[cursor:start]); i+=1; left=[];right=[]
   while i<len(lines) and lines[i][:1] in [" ","+","-"] and not lines[i].startswith("--- "):
    mark=lines[i][0]; content=lines[i][1:]
    if mark in " -":left.append(content)
    if mark in " +":right.append(content)
    i+=1
   assert len(left)==oldcount and len(right)==newcount,(path,len(left),oldcount,len(right),newcount)
   assert current[start:start+len(right)]==right,(path,newstart,"new-side mismatch")
   result.extend(left);cursor=start+len(right);hunks+=1
  result.extend(current[cursor:]); reconstructed="".join(result).encode()
  if old=="/dev/null":assert reconstructed==b"",path
  sections.append({"path":path,"old_absent_in_patch_basis":old=="/dev/null","reconstructed_old_sha256":None if old=="/dev/null" else sha(reconstructed),"hunks":hunks})
 return sections
full=invert(F/"source.patch");delta=invert(F/"source-geometry-pressure.delta.patch")
assert {x['path'] for x in full}=={x['path'] for x in m['paths']}
fd={x['path']:x for x in full};dd={x['path']:x for x in delta}
checks=[]
for x in m['paths']:
 path=x['path']; current=sha((ROOT/path).read_bytes());snapshot=sha((F/'source'/path).read_bytes())
 assert current==snapshot==x['sha256'],path
 assert fd[path]['reconstructed_old_sha256']==x['base_sha256'],path
 if path in dd:assert dd[path]['reconstructed_old_sha256']==x['freeze_02_sha256'],path
 else:assert x['sha256']==x['freeze_02_sha256'],path
 checks.append({'path':path,'current_and_snapshot_match':True,'full_patch_base_match':True,'f02_delta_or_unchanged_match':True})
checks_out={'method':'Python file hashes and reverse unified-patch reconstruction; no Git/base checkout execution','candidate':m['candidate_content_sha256'],'files':len(checks),'checks':checks,'full_patch':full,'delta':delta,'note':'Cargo /dev/null in F02-owned delta means absent from prior owned snapshot; full base patch correctly treats the two manifests as pre-existing files.'}
(OUT/'static_binding_probe.json').write_text(json.dumps(checks_out,indent=2)+'\n')
print(json.dumps({'files':len(checks),'full_patch_sections':len(full),'delta_sections':len(delta),'all_checks_pass':True}))
