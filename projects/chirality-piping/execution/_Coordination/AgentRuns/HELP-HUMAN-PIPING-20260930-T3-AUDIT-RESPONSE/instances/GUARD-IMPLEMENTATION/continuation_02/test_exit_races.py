"""Deterministic fake-native membership/exit races; no live process capability."""
import ctypes as C
import errno
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from harness import original, v3 as guard


class Scenario:
    def __init__(self, case, frames, known=True, failure=('info',101,1), error=errno.ESRCH,
                 returned=None, native=False, global_frames=None):
        self.case=case; self.frames=frames; self.failure=failure; self.error=error
        self.returned=returned; self.native=native; self.global_frames=global_frames
        self.table_count=0;self.all_count=0;self.calls=[];self.counts={};self.events=[]
        self.clock=100.0;self.advance={};self.mutate={};self.zombies=set()
        self.values={100:(100,80),101:(400,300),102:(700,500),103:(900,600)}
        self.extra_failures=set();self.global_return=None
        self.p=object.__new__(guard.MacProvider)
        self.p.known={100:case.leader,**({101:case.worker} if known else {})}
        self.p.trace=lambda kind,**data:self.events.append((kind,data))
        self.p.table=self.table
        self.p.lib=SimpleNamespace(proc_pidinfo=self.info,proc_pid_rusage=self.usage,proc_listpids=self.listpids)
        case.enterContext(patch('os.getsid',side_effect=self.sid))
        case.enterContext(patch('time.monotonic',side_effect=lambda:self.clock))
        case.enterContext(patch('time.time_ns',return_value=100000000000))

    def row(self,pid):
        if isinstance(pid,guard.Row): return pid
        return guard.Row(pid,2 if pid in (100,900) else 100,900 if pid==900 else 100,501,False)

    def frame(self):
        return self.frames[min(self.table_count-1,len(self.frames)-1)]

    def table(self,deadline):
        self.table_count+=1
        self.clock+=self.advance.get(('table',self.table_count),0)
        frame=self.frame()
        if isinstance(frame,Exception): raise frame
        return {self.row(pid).pid:self.row(pid) for pid in frame}

    def hit(self,kind,pid):
        key=(kind,pid);self.counts[key]=self.counts.get(key,0)+1
        point=(*key,self.counts[key]);self.calls.append(point)
        self.clock+=self.advance.get(point,0)
        return point,point==self.failure or point in self.extra_failures

    def info(self,pid,flavor,arg,raw,size):
        point,failed=self.hit('info',pid)
        if failed:
            C.set_errno(self.error)
            return self.returned if self.returned is not None else 0
        obj=C.cast(raw,C.POINTER(guard.BSDInfo)).contents
        obj.pid=pid;obj.ppid=2 if pid==100 else 100;obj.uid=obj.ruid=501
        obj.pgid=100;obj.start_sec=12000;obj.start_usec=50 if pid==100 else 60+(pid-101)
        obj.status=5 if pid in self.zombies else 2
        for key,value in self.mutate.get(point,{}).items(): setattr(obj,key,value)
        return size

    def sid(self,pid):
        point,failed=self.hit('sid',pid)
        if failed: raise OSError(self.error,'fake native failure')
        return self.mutate.get(point,{}).get('sid',100)

    def usage(self,pid,flavor,raw):
        point,failed=self.hit('rusage',pid)
        if failed:
            C.set_errno(self.error)
            return self.returned if self.returned is not None else -1
        obj=C.cast(raw,C.POINTER(guard.RUsageV0)).contents
        obj.proc_start_abstime=1
        obj.resident_size,obj.phys_footprint=self.values[pid]
        for key,value in self.mutate.get(point,{}).items():setattr(obj,key,value)
        return 0

    def listpids(self,flavor,value,buffer,size):
        if flavor==2:
            self.table_count+=1;self.clock+=self.advance.get(('table',self.table_count),0)
            frame=self.frame()
            if isinstance(frame,Exception): raise frame
            pids=[self.row(x).pid for x in frame if self.row(x).pgid==100]
        else:
            self.case.assertEqual((flavor,value),(1,0))
            self.all_count+=1
            self.clock+=self.advance.get(('all',self.all_count),0)
            if self.global_return is not None:
                C.set_errno(self.error);return self.global_return if self.global_return!='full' else size
            pids=self.global_frames[min(self.all_count-1,len(self.global_frames)-1)] if self.global_frames else [self.row(x).pid for x in self.frame()]
        for index,pid in enumerate(pids):buffer[index]=pid
        return len(pids)*4

    def collect(self,deadline=101.5):
        return self.p.live_group(self.case.leader) if self.native else self.p.group(self.case.leader,deadline)


class ExitRaces(original.PureCase):
    def test_known_exits_at_every_identity_and_rusage_boundary(self):
        points=[('info',101,n) for n in (1,2,3,4)]+[('sid',101,n) for n in (1,2,3,4)]+[('rusage',101,1)]
        for point in points:
            with self.subTest(point=point):
                scenario=Scenario(self,[[100,101,900],[100,900]],failure=point)
                rss,footprint,live,ids=scenario.collect()
                self.assertEqual((rss,footprint,live,set(ids)),(100,80,[],{100}))
                record=scenario.p.group_exits[0]
                self.assertEqual(record['pid'],101)
                self.assertEqual(record['identity']['start_sec'],12000)
                self.assertEqual(record['native_failure']['errno'],3)
                self.assertEqual(record['measurement_state'],'exited-unmeasured')
                self.assertIsNone(record['resource_observation'])
                self.assertTrue(record['complete_global_absence'])
                self.assertEqual(scenario.table_count,3)
                self.assertNotIn(900,{call[1] for call in scenario.calls})

    def test_B02_zombie_snapshot_then_ESRCH_needs_fresh_absence(self):
        z=guard.Row(101,100,100,501,True)
        scenario=Scenario(self,[[100,z,900],[100,900]],known=False)
        self.assertEqual(scenario.collect()[:3],(100,80,[]))
        record=scenario.p.group_exits[0]
        self.assertTrue(record['last_membership_row']['zombie'])
        self.assertIsNone(record['identity'])
        self.assertIsNone(record['resource_observation'])
        self.assertEqual(record['measurement_state'],'exited-unmeasured')
        self.assertEqual(record['native_failure']['operation'],'proc-pidinfo-denied-missing-short/0')

    def test_Z_alone_never_bypasses_identity_error(self):
        z=guard.Row(101,100,100,501,True)
        scenario=Scenario(self,[[100,z]],error=errno.EPERM)
        with self.assertRaises(guard.NativeReadFailure):scenario.collect()
        self.assertEqual(scenario.table_count,1)

    def test_ESRCH_still_present_reused_or_escaped_is_not_absence(self):
        for row in [101,guard.Row(101,1,777,501,False),guard.Row(101,100,100,502,False)]:
            with self.subTest(row=row):
                scenario=Scenario(self,[[100,101,900],[100,row,900]])
                with self.assertRaises(guard.Refusal):scenario.collect()
                self.assertEqual(scenario.p.group_exits,[])

    def test_leader_exit_never_allowed(self):
        for frames in ([[101,900]],[[100,101,900],[101,900]]):
            scenario=Scenario(self,frames,failure=('info',100,1))
            with self.assertRaises(guard.Refusal):scenario.collect()
            self.assertEqual(scenario.p.group_exits,[])

    def test_leader_zombie_refuses(self):
        scenario=Scenario(self,[[100,101]],failure=None);scenario.zombies={100}
        with self.assertRaisesRegex(guard.Refusal,'leader-zombie'):scenario.collect()

    def test_EPERM_EIO_unknown_and_short_reads_never_retry(self):
        cases=[('info',errno.EPERM,0),('info',errno.EIO,0),('info',0,0),
               ('info',errno.ESRCH,135),('info',errno.ESRCH,-1),
               ('rusage',errno.EPERM,-1),('rusage',0,-1),('rusage',errno.ESRCH,1),
               ('sid',errno.EPERM,None),('sid',errno.EINVAL,None)]
        for kind,error,returned in cases:
            with self.subTest(kind=kind,error=error,returned=returned):
                scenario=Scenario(self,[[100,101],[100]],failure=(kind,101,1),error=error,returned=returned)
                with self.assertRaises(guard.NativeReadFailure) as raised:scenario.collect()
                self.assertEqual(raised.exception.details['pid'],101)
                self.assertEqual(raised.exception.details['errno'],error)
                self.assertFalse(raised.exception.esrch_candidate)
                self.assertEqual(scenario.table_count,1)

    def test_partial_native_identity_is_preserved(self):
        scenario=Scenario(self,[[100,101],[100]],known=False,failure=('info',101,2))
        scenario.collect();details=scenario.p.group_exits[0]['native_failure']
        self.assertEqual(details['partial_identity']['start_usec'],60)
        self.assertEqual(details['partial_identity']['uid'],501)

    def test_matching_zombie_identity_has_explicit_unmeasured_provenance(self):
        scenario=Scenario(self,[[100,101]],failure=None);scenario.zombies={101}
        self.assertEqual(scenario.collect()[:3],(100,80,[]))
        self.assertFalse(any(c[0]=='rusage' and c[1]==101 for c in scenario.calls))
        record=next(data for kind,data in scenario.events if kind=='group-collection')
        self.assertEqual(record['zombie_present_unmeasured'],[101])

    def test_known_missing_before_first_read_requires_two_fresh_tables(self):
        scenario=Scenario(self,[[100,900]],failure=None)
        self.assertEqual(scenario.collect()[:3],(100,80,[]))
        self.assertEqual(scenario.table_count,3)
        self.assertIsNone(scenario.p.group_exits[0]['native_failure'])
        self.assertEqual(scenario.p.group_exits[0]['measurement_state'],'exited-unmeasured')

    def test_missing_known_but_fresh_global_presence_refuses(self):
        scenario=Scenario(self,[[100,900],[100,guard.Row(101,1,777,501,False),900]],failure=None)
        with self.assertRaises(guard.Refusal):scenario.collect()

    def test_new_member_during_retry_is_measured(self):
        scenario=Scenario(self,[[100,101,900],[100,102,900]])
        rss,footprint,live,ids=scenario.collect()
        self.assertEqual((rss,footprint,live,set(ids)),(800,580,[102],{100,102}))
        self.assertTrue(any(c[0]=='rusage' and c[1]==102 for c in scenario.calls))
        self.assertNotIn(900,{call[1] for call in scenario.calls})

    def test_new_member_at_end_of_successful_pass_is_not_silently_dropped(self):
        scenario=Scenario(self,[[100,101,900],[100,101,102,900]],failure=None)
        self.assertEqual(scenario.collect()[:3],(1200,880,[101,102]))
        self.assertEqual(scenario.table_count,4)

    def test_valid_large_partial_read_retained_after_member_exits(self):
        scenario=Scenario(self,[[100,101],[100]],failure=None)
        scenario.values[101]=(10000,8000)
        self.assertEqual(scenario.collect()[:3],(10100,8080,[]))
        self.assertEqual(scenario.p.group_exits[0]['measurement_state'],'measured-in-this-acquisition-before-exit')
        self.assertEqual(scenario.p.group_exits[0]['resource_observation']['rss_bytes'],10000)

    def test_reappeared_retired_pid_refuses_even_outside_group(self):
        scenario=Scenario(self,[[100,101],[100],[100,guard.Row(101,1,777,501,False)]])
        with self.assertRaises(guard.Refusal):scenario.collect()

    def test_deadline_never_resets_on_ESRCH_or_refresh(self):
        for point in [('info',101,1),('table',2)]:
            scenario=Scenario(self,[[100,101],[100]])
            scenario.advance[point]=1.51
            with self.assertRaisesRegex(guard.Refusal,'timeout'):scenario.collect()

    def test_stale_full_collection_is_rejected(self):
        scenario=Scenario(self,[[100,101],[100]])
        scenario.advance[('table',2)]=2.01
        with self.assertRaisesRegex(guard.Refusal,'timeout'):scenario.collect(deadline=110)

    def test_repeated_churn_is_bounded(self):
        scenario=Scenario(self,[[100,101],[100,102],[100,103],[100]])
        scenario.extra_failures={('info',102,1),('info',103,1)}
        with self.assertRaisesRegex(guard.Refusal,'churn-limit'):scenario.collect()
        self.assertEqual(scenario.table_count,3)

    def test_second_disappearance_is_recorded_within_same_budget(self):
        scenario=Scenario(self,[[100,101],[100,102],[100]])
        scenario.extra_failures={('info',102,1)}
        self.assertEqual(scenario.collect()[:3],(100,80,[]))
        self.assertEqual([e['pid'] for e in scenario.p.group_exits],[101,102])

    def test_malformed_or_denied_refresh_table_refuses(self):
        for error in [PermissionError('fake denial'),guard.Refusal('malformed-process-table')]:
            scenario=Scenario(self,[[100,101],error])
            with self.assertRaises((guard.Refusal,PermissionError)):scenario.collect()

    def test_start_UID_session_and_rusage_identity_changes_refuse(self):
        mutations=[(('info',101,2),{'start_usec':61}),(('info',101,1),{'uid':502}),
                   (('sid',101,2),{'sid':101}),(('info',101,3),{'start_sec':12001}),
                   (('rusage',101,1),{'proc_start_abstime':0}),
                   (('rusage',101,1),{'proc_exit_abstime':10})]
        for point,change in mutations:
            scenario=Scenario(self,[[100,101],[100]],failure=None);scenario.mutate[point]=change
            with self.assertRaises(guard.Refusal):scenario.collect()
            self.assertEqual(scenario.table_count,1)

    def test_native_completion_exit_uses_global_absence_and_no_ps(self):
        scenario=Scenario(self,[[100,101,900],[100,900]],native=True)
        scenario.p.table=lambda *_:self.fail('supervisor may not spawn ps')
        self.assertEqual(scenario.collect(),[])
        self.assertEqual(scenario.all_count,2)
        self.assertEqual(scenario.p.group_exits[0]['measurement_state'],'exited-unmeasured')

    def test_native_completion_new_member_is_retained(self):
        scenario=Scenario(self,[[100,101,900],[100,102,900]],native=True)
        self.assertEqual(scenario.collect(),[102])

    def test_native_completion_present_or_escaped_candidate_refuses(self):
        scenario=Scenario(self,[[100,101],[100]],native=True,global_frames=[[100,101,900]])
        with self.assertRaises(guard.Refusal):scenario.collect()

    def test_native_completion_global_enumeration_must_be_complete(self):
        for returned in (0,-1,2,'full'):
            scenario=Scenario(self,[[100,101],[100]],native=True)
            scenario.global_return=returned
            with self.assertRaisesRegex(guard.Refusal,'enumeration'):scenario.collect()
            self.assertEqual(scenario.p.group_exits,[])

    def test_native_completion_original_deadline(self):
        scenario=Scenario(self,[[100,101],[100]],native=True)
        scenario.advance[('all',1)]=.51
        with self.assertRaisesRegex(guard.Refusal,'timeout'):scenario.collect()

    def test_partial_contradiction_before_ESRCH_never_recovers(self):
        for phase in (1,3):  # initial identity and the post-rusage identity
            for field,value in [('start_sec',12001),('start_usec',61),('uid',502),
                                ('ruid',502),('pgid',777),('pid',999)]:
                with self.subTest(phase=phase,field=field):
                    sid_call=1 if phase==1 else 3
                    scenario=Scenario(self,[[100,101],[100]],failure=('sid',101,sid_call))
                    scenario.mutate[('info',101,phase)]={field:value}
                    with self.assertRaisesRegex(guard.Refusal,'partial-'):scenario.collect()
                    self.assertEqual(scenario.table_count,1)
                    self.assertEqual(scenario.p.group_exits,[])

    def test_partial_contradiction_for_new_worker_also_refuses(self):
        for field,value in [('uid',502),('ruid',502),('pgid',777),('pid',999)]:
            scenario=Scenario(self,[[100,101],[100]],known=False,failure=('info',101,2))
            scenario.mutate[('info',101,1)]={field:value}
            with self.assertRaisesRegex(guard.Refusal,'partial-'):scenario.collect()
            self.assertEqual(scenario.table_count,1)

    def test_observed_session_mismatch_then_ESRCH_is_preserved(self):
        scenario=Scenario(self,[[100,101],[100]],failure=('info',101,2))
        scenario.mutate[('sid',101,1)]={'sid':777}
        with self.assertRaisesRegex(guard.Refusal,'partial-'):scenario.collect()
        details=next(data for kind,data in scenario.events if kind=='native-read-failure')
        self.assertEqual(details['partial_identity']['sid'],777)
        self.assertEqual(scenario.table_count,1)

    def test_missing_partial_fields_remain_unknown(self):
        guard.MacProvider._validate_partial({'uid':501},101,None,self.leader)
        guard.MacProvider._validate_partial(None,101,self.worker,self.leader)
        with self.assertRaises(guard.Refusal):
            guard.MacProvider._validate_partial({'uid':502},101,None,self.leader)

    def test_malformed_native_failure_return_never_allows_absence(self):
        for returned in (False,0.0):
            scenario=Scenario(self,[[100,101],[100]],returned=returned)
            with self.assertRaises(guard.NativeReadFailure) as raised:scenario.collect()
            self.assertFalse(raised.exception.esrch_candidate)
            self.assertEqual(scenario.table_count,1)

    def test_final_snapshot_leader_zombie_refuses(self):
        scenario=Scenario(self,[[100,101],[guard.Row(100,2,100,501,True),101]],failure=None)
        with self.assertRaisesRegex(guard.Refusal,'leader-zombie'):scenario.collect()

    def test_monitor_recovered_exit_sends_heartbeat_not_false_stop(self):
        scenario=Scenario(self,[[100,101],[100]])
        controls=[]
        def sample():
            rss,footprint,_,_=scenario.collect()
            return guard.Sample(**{**guard.asdict(self.base),'rss_bytes':rss,'footprint_bytes':footprint})
        decision=guard.MonitorState().step(sample,lambda *args:controls.append(args),self.base,self.limits,100)
        self.assertIsNone(decision)
        self.assertEqual(controls,[('HEARTBEAT','')])
        self.assertEqual(scenario.p.group_exits[0]['measurement_state'],'exited-unmeasured')

    def test_monitor_still_stops_on_valid_partial_cap_crossing(self):
        scenario=Scenario(self,[[100,101],[100]],failure=None)
        scenario.values[101]=(self.limits.cap_bytes,8000)
        controls=[]
        def sample():
            rss,footprint,_,_=scenario.collect()
            return guard.Sample(**{**guard.asdict(self.base),'rss_bytes':rss,'footprint_bytes':footprint})
        decision=guard.MonitorState().step(sample,lambda *args:controls.append(args),self.base,self.limits,100)
        self.assertEqual(decision,'rss-cap')
        self.assertEqual(controls,[('STOP','rss-cap')])

    def test_cross_acquisition_reappearance_is_never_new(self):
        for row in [101,guard.Row(101,1,777,501,False)]:
            scenario=Scenario(self,[[100,101,900],[100,900]])
            self.assertEqual(scenario.collect()[:3],(100,80,[]))
            self.assertIn(101,scenario.p.departed)
            before=list(scenario.calls)
            scenario.frames=[[100,row,900]];scenario.table_count=0
            with self.assertRaises(guard.Refusal):scenario.collect()
            self.assertEqual(scenario.calls,before)  # no read/signal aimed at reused PID
            self.assertIn(101,scenario.p.departed)

    def test_cross_acquisition_native_completion_reappearance_refuses(self):
        for members in ([100,101,900],[100,900]):
            scenario=Scenario(self,[[100,101,900],[100,900]],native=True)
            self.assertEqual(scenario.collect(),[])
            before=list(scenario.calls)
            scenario.frames=[members];scenario.table_count=0;scenario.all_count=0
            scenario.global_frames=[[100,101,900]]
            with self.assertRaises(guard.Refusal):scenario.collect()
            self.assertEqual(scenario.calls,before)
            self.assertEqual(scenario.all_count,1)

    def test_departed_history_persists_without_reemitting_zero_metrics(self):
        scenario=Scenario(self,[[100,101,900],[100,900]])
        scenario.collect();first=dict(scenario.p.departed[101])
        scenario.frames=[[100,900]];scenario.table_count=0
        self.assertEqual(scenario.collect()[:3],(100,80,[]))
        self.assertEqual(scenario.p.departed[101],first)
        self.assertEqual(scenario.p.group_exits,[])
        self.assertIsNone(first['resource_observation'])

    def test_job_lifetime_seen_history_is_bounded_without_eviction(self):
        scenario=Scenario(self,[[100,700,900]],known=False,failure=None)
        scenario.p.seen={pid:None for pid in range(100,100+guard.MAX_MEMBERS)}
        scenario.p.seen[100]=self.leader
        scenario.p.departed={pid:{'pid':pid} for pid in range(101,100+guard.MAX_MEMBERS)}
        with self.assertRaisesRegex(guard.Refusal,'job-seen-pid-limit'):scenario.collect()
        self.assertEqual(len(scenario.p.seen),guard.MAX_MEMBERS)
        self.assertEqual(len(scenario.p.departed),guard.MAX_MEMBERS-1)
        self.assertNotIn(700,scenario.p.seen)

    def test_monitor_and_DONE_group_paths_share_repair(self):
        for deadline in (101.5,101.0):
            scenario=Scenario(self,[[100,101],[100]])
            self.assertEqual(scenario.collect(deadline)[:3],(100,80,[]))


if __name__=='__main__':unittest.main(verbosity=2)
