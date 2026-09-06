import pathlib,json,csv,hashlib
P=pathlib.Path(__file__).parent
rows=[]
for d,rev in [('DEL-10-10','REVISION_V001'),('DEL-10-03','REVISION_V002')]:
 w=P/'WORKERS'/d;q=w/rev;mp=json.loads((q/'CHANGE_MAP.json').read_text());actual=[]
 for f,key in [('CLAIMS.csv','ClaimID'),('RESIDUALS.csv','ResidualID')]:
  old=list(csv.DictReader((w/f).open()));new=list(csv.DictReader((q/f).open()));assert [x[key] for x in old]==[x[key] for x in new]
  for a,b in zip(old,new):
   for k in a:
    if a[k]!=b[k]:actual.append({'file':f,'row_id':a[key],'column':k,'old':a[k],'new':b[k]})
 mapped=mp.get('changed_cells',mp.get('changes',[]));normalized=[{**{k:r[k] for k in ['file','column','old','new']},'row_id':r.get('row_id',r.get('id'))} for r in mapped]
 assert sorted(actual,key=lambda x:(x["file"],x["row_id"],x["column"]))==sorted(normalized,key=lambda x:(x["file"],x["row_id"],x["column"])),(d,'change map mismatch')
 rows.append({'deliverable':d,'revision':rev,'mapped_cells':len(actual),'exact_map':True,'unaffected_cells_equal':True})
(P/'MANAGER_CORRECTION_BACKCHECK.json').write_text(json.dumps({'result':'PASS','checks':rows,'source_mutation':False},indent=2)+'\n');print(json.dumps(rows,indent=2))
