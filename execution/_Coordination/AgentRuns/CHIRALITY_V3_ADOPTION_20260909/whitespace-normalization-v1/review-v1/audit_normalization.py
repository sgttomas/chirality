import csv, hashlib, io, json, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
HERE=Path(__file__).resolve().parent
NORM=HERE.parent
PREDECESSOR="9b005c23a76fc2619780d27f5fabb70e3221cf02"
BASE="c16812685831a1cae3d44bf478d08b033c605c3a"
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*args): return subprocess.check_output(["git",*args],cwd=ROOT)
def record(p):
 b=(ROOT/p).read_bytes(); return {"path":p,"sizeBytes":len(b),"sha256":sha(b)}
pre=json.loads((NORM/"PREIMAGE_MANIFEST.json").read_text())
over=json.loads((NORM/"NORMALIZATION_OVERLAY.json").read_text())
assert pre["fileCount"]==over["fileCount"]==len(pre["files"])==len(over["files"])==27
assert pre["committedCandidate"]==over["predecessorCommit"]==PREDECESSOR
assert pre["baseCommit"]==over["baseCommit"]==BASE
assert [r["path"] for r in pre["files"]]==[r["path"] for r in over["files"]]
results=[]
for old,row in zip(pre["files"],over["files"]):
 p=row["path"]; original=git("show",f"{PREDECESSOR}:{p}"); saved=(NORM/"preimages"/p).read_bytes(); current=(ROOT/p).read_bytes()
 assert original==saved,p
 assert len(original)==old["sizeBytes"]==row["sizeBytes"] and sha(original)==old["sha256"]==row["sha256"],p
 assert len(current)==row["newSizeBytes"] and sha(current)==row["newSha256"],p
 assert old["issues"]==row["issues"],p
 lines=original.splitlines(keepends=True)
 actual=[]
 for i,line in enumerate(lines,1):
  if line.rstrip(b"\r\n").endswith((b" ",b"\t")): actual.append({"line":i,"issue":"trailing whitespace."})
 eof=len(lines)
 while eof>0 and lines[eof-1].strip(b" \t\r\n")==b"": eof-=1
 actual += [{"line":i,"issue":"new blank line at EOF."} for i in range(eof+1,len(lines)+1)]
 assert actual==row["issues"],(p,actual,row["issues"])
 expected=re.sub(rb"[ \t]+(?=\r?$)",b"",original,flags=re.M)
 expected=expected.rstrip(b"\n")+b"\n"
 assert current==expected,p
 assert re.findall(rb"\S+",original)==re.findall(rb"\S+",current),p
 results.append({**record(p),"preimageSha256":sha(saved),"preimageSizeBytes":len(saved),"preimageMatchesGit":True,"reportedIssuesExact":True,"onlyReportedWhitespaceRemoved":True,"tokensUnchanged":True,"removedBytes":len(saved)-len(current)})
manifest_path="exports/chirality-app/export-manifest.csv"
prior=list(csv.DictReader(io.StringIO(git("show",f"{PREDECESSOR}:{manifest_path}").decode())))
current=list(csv.DictReader(io.StringIO((ROOT/manifest_path).read_text())))
assert [r["path"] for r in prior]==[r["path"] for r in current]
changed=[]
normalized={r["path"] for r in results}
for a,b in zip(prior,current):
 if a!=b:
  assert a["path"] in normalized,a["path"]
  live=record(b["path"])
  assert b["size_bytes"]==str(live["sizeBytes"]) and b["sha256"]==live["sha256"]
  changed.append(b["path"])
assert set(changed)==normalized&{r["path"] for r in current}
index="workflows/index.json"
assert git("show",f"{PREDECESSOR}:{index}")==(ROOT/index).read_bytes()
changed_tracked=git("diff","--name-only",PREDECESSOR).decode().splitlines()
others=[p for p in changed_tracked if p not in normalized and p!=manifest_path]
assert others==[".github/workflows/harness-premerge.yml"],others
# Every previously committed file outside the enumerated normalization and separate CI/export paths is Git-identical.
subject={"schema":"chirality-whitespace-independent-subject/v1","baseCommit":BASE,"predecessorCommit":PREDECESSOR,"files":[record(r["path"]) for r in results],"bindings":[record(str((NORM/f).relative_to(ROOT))) for f in ("PREIMAGE_MANIFEST.json","NORMALIZATION_OVERLAY.json")]+[record(manifest_path),record(index)],"exclusions":["Independent CI concurrency change in .github/workflows/harness-premerge.yml", "Untracked historical scratch artifacts outside the candidate; preserved preimages intentionally retain defects"]}
subject_bytes=(json.dumps(subject,indent=2)+"\n").encode()
(HERE/"SUBJECT_INTERIM.json").write_bytes(subject_bytes)
result={"status":"PASS_INTERIM_PENDING_DISTRIBUTION_FREEZE","subjectSha256":sha(subject_bytes),"fileCount":27,"issueCount":sum(len(r["issues"]) for r in pre["files"]),"removedBytes":sum(r["removedBytes"] for r in results),"files":results,"exportChangedRows":changed,"rootWorkflowIndexUnchanged":True,"unchangedHistoricalEvidenceOutsideOverlay":True,"separateExcludedChanges":others}
(HERE/"BYTE_AUDIT_INTERIM.json").write_text(json.dumps(result,indent=2)+"\n")
for label,cmd in [("CANDIDATE_WHITESPACE",[sys.executable,"tools/validation/validate_candidate_whitespace.py","--repo-root",str(ROOT),"--paths",*[r["path"] for r in results],manifest_path,index]),("PROSPECTIVE_DIFF_CHECK",["git","diff","--check",BASE,"--",*[r["path"] for r in results],manifest_path,index]),("WORKFLOW_INDEX",[sys.executable,"tools/validation/build_workflow_index.py","--check"])]:
 r=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (HERE/(label+"_INTERIM.log")).write_bytes(r.stdout)
 assert r.returncode==0,(label,r.stdout)
print(json.dumps({k:v for k,v in result.items() if k not in ("files","exportChangedRows")},indent=2))
