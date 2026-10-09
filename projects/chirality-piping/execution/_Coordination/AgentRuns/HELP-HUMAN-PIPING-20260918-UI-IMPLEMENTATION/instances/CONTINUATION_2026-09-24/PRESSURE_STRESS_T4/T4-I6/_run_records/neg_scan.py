"""T4-I6 Part A: every committed JSON with pressure_regions, scanned for a negative or signed-zero region pressure. usage (from NUM4): python -I neg_scan.py <commit>"""
import json, subprocess, sys
C = sys.argv[1]
files = subprocess.run(["git","grep","-l","pressure_regions",C,"--","projects/chirality-piping"],capture_output=True,text=True).stdout.split()
hits=[]; nfiles=0
def walk(o, path, f):
    if isinstance(o, dict):
        if "pressure_regions" in o and isinstance(o["pressure_regions"], list):
            for r in o["pressure_regions"]:
                if isinstance(r, dict) and isinstance(r.get("pressure"), dict):
                    v = r["pressure"].get("value")
                    if isinstance(v,(int,float)) and (v < 0 or (v == 0 and str(v).startswith("-"))):
                        hits.append((f, path, v))
        for k,v in o.items(): walk(v, path+"/"+k, f)
    elif isinstance(o, list):
        for i,v in enumerate(o): walk(v, path+f"[{i}]", f)
for spec in files:
    f = spec.split(":",1)[1]
    if not f.endswith(".json"): continue
    nfiles+=1
    txt = subprocess.run(["git","show",spec],capture_output=True,text=True).stdout
    try: d=json.loads(txt)
    except Exception as e: continue
    walk(d,"",f)
print("json files with pressure_regions:", nfiles)
print("negative-pressure regions:", len(hits))
for h in hits[:20]: print(h)
