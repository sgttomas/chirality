import pathlib,csv,json,hashlib,subprocess,runpy,collections
P=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=P,text=True).strip())
V=runpy.run_path(str(P/'validate_package.py'))
paths=[P/'CORRECTIONS/C01'/f'DEL-06-{i:02}' if i<3 else P/'CORRECTIONS/C02_DEPENDS'/f'DEL-06-{i:02}' if i>4 else P/'WORKERS'/f'DEL-06-{i:02}' for i in range(1,7)]
result,claims,residuals=V['validate'](paths)
assert result['passed'],result
assert len(result['members'])==6
for x in ['VERIFICATION/RETURN.md','VERIFICATION/VERIFICATION.md','VERIFICATION/OUTPUT_MANIFEST.json','CORRECTIONS/C01/RETURN.md']:
 assert (P/x).is_file(),x

def write_csv(name,fields,rows):
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
write_csv('PACKAGE_CLAIMS.csv',V['C'],claims)
write_csv('PACKAGE_RESIDUALS.csv',V['R'],residuals)
summary=[]
for info,path in zip(result['members'],paths):
 d=info['DeliverableID']; summary.append({'DeliverableID':d,'PackageID':'PKG-06','ClaimCount':info['Claims'],'UnknownClaimCount':info['Unknown'],'ResidualCount':info['Residuals'],'SummaryDisposition':'ASSESSED_UNKNOWN' if info['Unknown'] else 'ASSESSED_WITH_RESIDUALS' if info['Residuals'] else 'ASSESSED_ALIGNED','WarrantedNone':'FALSE' if info['Unknown'] or info['Residuals'] else 'REQUIRES_SEMANTIC_WARRANT','SelectedClaims':str((path/'CLAIMS.csv').relative_to(ROOT)),'SelectedResiduals':str((path/'RESIDUALS.csv').relative_to(ROOT)),'SelectedReadManifest':str((path/'READ_MANIFEST.json').relative_to(ROOT)),'Notes':'ALIGNED rows are class-qualified documentary/lifecycle assertions, not verified product behavior; no executable Remaining changed.'})
write_csv('PACKAGE_SUMMARY.csv',list(summary[0]),summary)
selection=[]
for path in paths:
 selection.append({'DeliverableID':path.name,'path':str(path.relative_to(ROOT)),'hashes':{f:hashlib.sha256((path/f).read_bytes()).hexdigest() for f in ['CLAIMS.csv','RESIDUALS.csv','READ_MANIFEST.json','COVERAGE.md','RETURN.md']}})
(P/'SELECTED_OUTPUTS.json').write_text(json.dumps(selection,indent=2)+'\n')
print(json.dumps(result,indent=2))
