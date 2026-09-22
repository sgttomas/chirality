from rvlib import load
for f in ['R3/CLAIM_CONCORDANCE.csv','R3/EXTENSION_CONCORDANCE.csv','R4/PACKET_INDEX.csv','R4/PACKET_SUBQUESTIONS.csv']:
    r=load(f); 
    rows=r[1] if isinstance(r,tuple) else r
    print(f, type(r), len(rows)); print(list(rows[0].keys()) if hasattr(rows[0],'keys') else rows[0])
