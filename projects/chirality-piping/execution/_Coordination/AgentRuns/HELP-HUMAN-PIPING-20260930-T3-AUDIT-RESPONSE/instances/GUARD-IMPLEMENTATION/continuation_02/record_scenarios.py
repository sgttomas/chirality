"""Bounded fake-native traces for backcheck; no signals/provider activation."""
import json
from harness import v3 as guard
from test_exit_races import ExitRaces,Scenario

results=[]
for mode in ('B02-zombie-reaped','new-member-on-retry','validated-partial-peak',
             'partial-reuse-then-ESRCH','completion-native-absence'):
    case=ExitRaces('test_B02_zombie_snapshot_then_ESRCH_needs_fresh_absence');case.setUp()
    try:
        frames=[[100,101,900],[100,900]]
        if mode=='B02-zombie-reaped':frames[0]=[100,guard.Row(101,100,100,501,True),900]
        if mode=='new-member-on-retry':frames[1]=[100,102,900]
        failure=None if mode=='validated-partial-peak' else ('info',101,1)
        if mode=='partial-reuse-then-ESRCH':failure=('sid',101,1)
        scenario=Scenario(case,frames,known=mode!='B02-zombie-reaped',failure=failure,
                          native=mode=='completion-native-absence')
        if mode=='validated-partial-peak':scenario.values[101]=(10000,8000)
        if mode=='partial-reuse-then-ESRCH':scenario.mutate[('info',101,1)]={'start_sec':12001}
        try:
            output=scenario.collect()
            if not scenario.native:
                rss,footprint,live,identities=output
                output={'rss_bytes':rss,'footprint_bytes':footprint,'live':live,
                        'identities':{str(p):guard.asdict(i) for p,i in identities.items()}}
            result={'outcome':'collected','output':output}
        except guard.Refusal as exc:
            result={'outcome':'refused','reason':str(exc)}
        results.append({'case':mode,'fake_native_only':True,**result,
                        'table_calls':scenario.table_count,'complete_native_pid_lists':scenario.all_count,
                        'native_calls':scenario.calls,'events':scenario.events})
    finally:case.doCleanups()
print(json.dumps({'claims':'deterministic fake-native observations, not live measurements',
                  'cases':results},indent=2))
