import re,sys,glob
E="projects/pec/execution/"
rows=[("DEL-01-01","REQ-003",["DEL-04-03"],["CLM-012"]),("DEL-01-01","REQ-004",["DEL-03-02","DEL-03-03"],["CLM-012"]),("DEL-01-01","REQ-005",["DEL-03-01"],["CLM-012"]),("DEL-01-01","REQ-007",["DEL-01-03"],["CLM-012"]),("DEL-01-01","REQ-015",["DEL-04-05"],["CLM-012"]),("DEL-01-01","REQ-016",["DEL-01-06"],["CLM-012"]),
("DEL-02-06","REQ-004",["DEL-04-01"],["CLM-011","CLM-012"]),("DEL-02-06","REQ-006",["DEL-04-03"],["CLM-011"]),("DEL-02-06","REQ-009",["DEL-01-03"],["CLM-011"]),("DEL-02-06","REQ-010",["DEL-03-01"],["CLM-011"]),
("DEL-02-07","REQ-004",["DEL-04-05"],["CLM-014"]),("DEL-02-07","REQ-006",["DEL-01-03"],["CLM-014"])]
def block(text,id_):
    # the paragraph/list item/table row that defines id_
    lines=text.splitlines(); out=[]
    for i,l in enumerate(lines):
        if re.match(r'^\s*(?:[-*]\s+|\|\s*|#+\s+)?\**`?%s`?\**[\s:|.—-]'%re.escape(id_), l):
            out.append(l); j=i+1
            while j<len(lines) and lines[j].strip() and not re.match(r'^\s*(?:[-*]\s+|\|\s*|#+\s+)?\**`?[A-Z]{2,4}-\d{3}`?\**[\s:|.—-]',lines[j]):
                out.append(lines[j]); j+=1
            break
    return "\n".join(out)
fail=0
for d,req,owners,clms in rows:
    p=glob.glob(E+f"PKG-*/1_Working/{d}_*/ScopeOfWork.md")[0]; t=open(p).read()
    rb=block(t,req); cb=" ".join(block(t,c) for c in clms)
    for o in owners:
        inreq=o in rb; inclm=o in cb
        ok=inreq and inclm; fail|= not ok
        print(("PASS" if ok else "FAIL"),d,req,"->",o,"| owner in REQ text:",inreq,"| owner in cited",",".join(clms)+":",inclm,"| REQ block chars",len(rb),"CLM block chars",len(cb))
print("RESULT","FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
