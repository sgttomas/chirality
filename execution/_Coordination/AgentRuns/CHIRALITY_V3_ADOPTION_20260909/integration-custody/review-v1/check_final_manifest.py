"""Read-only audit. The sole write is its terminal evidence result in this directory."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path('/private/tmp/chirality-v3-adoption-20260909')
review=Path(__file__).resolve().parent
p=root/'execution/_Coordination/AgentRuns/CHIRALITY_V3_ADOPTION_20260909/integration-custody/STAGING_MANIFEST_V1.json'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
assert sha(p)==sys.argv[1], 'Manifest changed after declared freeze'
d=json.loads(p.read_text());u=json.loads((review/'UNION_CHECK_FINAL.json').read_text());union={e['path']:e for e in u['sourceUnion']}
issues=[]
for group in ['sourceFiles','evidenceFiles','effectiveSubjects']:
 for e in d[group]:
  f=root/e['path']
  if not f.is_file() or f.is_symlink():issues.append([group,e['path'],'not a regular non-symlink file']);continue
  if sha(f)!=e['sha256']:issues.append([group,e['path'],'hash mismatch'])
  if 'sizeBytes' in e and f.stat().st_size!=e['sizeBytes']:issues.append([group,e['path'],'size mismatch'])
source={e['path'] for e in d['sourceFiles']};evidence={e['path'] for e in d['evidenceFiles']}
for e in d['sourceFiles']:
 if e['path'] not in union or union[e['path']]['sha256']!=e['sha256']:issues.append(['sourceBinding',e['path'],'not exact independently reconstructed effective subject'])
changed=set(subprocess.check_output(['git','diff','--name-only',d['baseCommit']],cwd=root,text=True).splitlines())
changed.update(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
changedProduct={q for q in changed if '/AgentRuns/' not in q}
for q in sorted(changedProduct-source):issues.append(['coverage',q,'missing changed source'])
for q in sorted(source-changedProduct):issues.append(['coverage',q,'selected unexpected changed source'])
for q in sorted(source&evidence):issues.append(['classification',q,'source/evidence overlap'])
assert sha(p)==sys.argv[1], 'Manifest changed during audit'
result={'manifest':str(p.relative_to(root)),'manifestSha256':sha(p),'manifestBytes':p.stat().st_size,'base':d['baseCommit'],'branch':d['branch'],'sourceRows':len(d['sourceFiles']),'sourceBytes':sum(e['sizeBytes'] for e in d['sourceFiles']),'evidenceRows':len(d['evidenceFiles']),'evidenceBytes':sum(e['sizeBytes'] for e in d['evidenceFiles']),'subjectFileBindings':len(d['effectiveSubjects']),'independentUnionPaths':len(union),'independentUnionSha256':sha(review/'UNION_CHECK_FINAL.json'),'duplicateSourceRows':len(d['sourceFiles'])-len(source),'duplicateEvidenceRows':len(d['evidenceFiles'])-len(evidence),'missingChangedSource':sorted(changedProduct-source),'manifestReportedGaps':{k:d[k] for k in ['sourceOwnerGaps','currentPostimageBindingGaps','missingEvidence']},'issues':issues,'verdict':'PASS' if not issues else 'HOLD'}
assert result['duplicateSourceRows']==result['duplicateEvidenceRows']==0
out=review/'FINAL_MANIFEST_CHECK.json';assert not out.exists(),'Do not overwrite terminal evidence'
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
