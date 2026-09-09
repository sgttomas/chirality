"""Independent candidate-pointer behavior probes; no source writes."""
from pathlib import Path
import dataclasses
import hashlib
import json
import sys
import tempfile
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[5]
sys.path.insert(0,str(ROOT/'tools/validation'))
import validate_domain_decomposition_integrity as v
results=[]
with tempfile.TemporaryDirectory(dir=OUT) as tmp:
    workspace=Path(tmp)/'workspace';change=workspace/'execution/_ScopeChange';change.mkdir(parents=True)
    previous=change/'SCA-001'; previous.mkdir();candidate=change/'SCA-001-candidate';candidate.mkdir()
    for name in v.REQUIRED_SNAPSHOT_ARTIFACTS:
        (candidate/name).write_text('Column\n' if name.endswith('.csv') else 'Candidate evidence\n')
    latest=change/'_LATEST.md'
    def run(case,text,expected_pass,**kwargs):
        if text is None:
            latest.unlink(missing_ok=True)
        else:latest.write_text(text)
        try:
            findings=v.validate_snapshot(candidate,mode='candidate',**kwargs)
            passed=not findings
            results.append({'case':case,'pass':passed==expected_pass,'expectedValid':expected_pass,'findings':[dataclasses.asdict(x) for x in findings]})
        except Exception as exc:results.append({'case':case,'pass':False,'error':str(exc)})
    run('first-amendment-absent-pointer',None,True,expected_no_active_snapshot=True)
    run('first-amendment-premature-pointer','Latest: SCA-001-candidate\n',False,expected_no_active_snapshot=True)
    for case,text in [
        ('current-field','Latest: SCA-001\n'),
        ('legacy-snapshot-field','Latest snapshot: `SCA-001/`\n'),
        ('legacy-bold-field','- **Latest snapshot:** `SCA-001/`\n'),
        ('legacy-table-path','|Snapshot|`execution/_ScopeChange/SCA-001/`|\n'),
        ('legacy-raw-name','SCA-001\n'),
    ]:run(case,text,True,expected_active_snapshot=previous)
    run('candidate-prefix-collision','Latest: SCA-001-candidate\n',False,expected_active_snapshot=previous)
    run('historical-mention-is-not-target','Latest: SCA-001-candidate\nPrevious: SCA-001\n',False,expected_active_snapshot=previous)
    run('foreign-same-basename','Latest: /another-root/SCA-001\n',False,expected_active_snapshot=previous)
    latest.write_text('Latest: SCA-001-candidate\n')
    findings=v.validate_snapshot(candidate)
    results.append({'case':'accepted-active-mode','pass':not findings,'findings':[dataclasses.asdict(x) for x in findings]})
report={'sourceSHA256':hashlib.sha256((ROOT/'tools/validation/validate_domain_decomposition_integrity.py').read_bytes()).hexdigest(),'results':results,'pass':all(x['pass'] for x in results)}
print(json.dumps(report,indent=2));raise SystemExit(0 if report['pass'] else 1)
