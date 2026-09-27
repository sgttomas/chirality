import json,subprocess,sys
P='projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/'
R='projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/premise/'
for key,f in (('DEL-00-03_SPEC','artifacts/v2/SPEC.md'),('DEL-00-03_SOW','ScopeOfWork.md')):
    pre=subprocess.run(['git','show','7c250e370^:'+P+f],capture_output=True,text=True).stdout
    cur=open(P+f).read()
    led=json.load(open(R+key+'.json'))
    hunks=led['hunks'] if isinstance(led,dict) and 'hunks' in led else led
    print(key,'ledger type',type(led).__name__, 'keys', list(led.keys()) if isinstance(led,dict) else '', 'hunks',len(hunks))
    t=pre; ok=0
    for h in hunks:
        p=h['pre']; q=h['post']
        n=t.count(p)
        if n!=1: print('  hunk',h.get('id'),'pre occurrences',n)
        t=t.replace(p,q,1); ok+=1
    print('  applied',ok,'; rendering equals current bytes:',t==cur)
    print('  hunk ids/causes:')
    for h in hunks: print('   ',h.get('id'),'|',h.get('locus','')[:60],'|',str(h.get('cause',''))[:90])
