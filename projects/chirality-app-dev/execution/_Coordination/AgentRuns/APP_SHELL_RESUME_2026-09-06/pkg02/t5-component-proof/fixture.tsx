import React, {useEffect} from 'react';
import {createRoot} from 'react-dom/client';
import {ActivityView} from '../../../../../../frontend/src/components/woven-dialogue/activity-shelf';
import {HarnessEventsProvider,useHarnessEventActions} from '../../../../../../frontend/src/components/workspace/harness-events-provider';
const event=(eventId:string,type:string,data:Record<string,unknown>,timestamp='2026-09-06T12:00:00Z',sessionId='fixture-main')=>({schemaVersion:1,eventId,sessionId,turnId:'fixture-turn',timestamp,type,data});
const fixtures=[
 event('read-start','tool.started',{toolUseId:'read',toolName:'read_file',inputMetadata:{pathFields:{path:'execution/DEL-02-01/_STATUS.md'}}}),
 event('read-done','tool.completed',{toolUseId:'read'},'2026-09-06T12:00:02Z'),
 event('write','tool.started',{toolUseId:'write',toolName:'write_file',inputMetadata:{pathFields:{path:'reviews/current-review.md'}}},'2026-09-06T12:00:03Z'),
 event('mystery','tool.failed',{toolUseId:'mystery',toolName:'custom_pipeline_probe'},'not-a-time'),
 event('task','subagent.started',{taskId:'review-task',agentName:'WORKING_ITEMS',description:'Check the recorded review scope.'}),
 event('task-complete','subagent.completed',{taskId:'review-task',summary:'The selected scope was reviewed.'},'2026-09-06T12:00:05Z'),
 event('task2','subagent.failed',{taskId:'read-task',agentName:'RESEARCH',description:'Inspect the fixture source.'},'2026-09-06T12:00:06Z')
];
function Fixture(){const{hydrateEvents,appendEvent}=useHarnessEventActions();useEffect(()=>{hydrateEvents(fixtures as never);},[hydrateEvents]);return <><p className="proof-note">Component-only Activity view · synthetic recorded events · no live runtime</p><div className="proof-layout"><main><h1>Activity view presentation</h1><p>Actual ActivityView and HarnessEventsProvider; adjacent controls belong to this fixture.</p><button onClick={()=>{document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'light':'dark'}}>Toggle fixture theme</button><button onClick={()=>appendEvent(event('write-end','tool.completed',{toolUseId:'write'},'2026-09-06T12:00:10Z') as never)}>Complete fixture write</button><button onClick={()=>hydrateEvents(fixtures as never)}>Reset fixture events</button></main><aside className="woven-coordination"><section className="woven-right-panel"><div id="right-view-content"><ActivityView/></div></section></aside></div></>}
createRoot(document.getElementById('fixture')!).render(<HarnessEventsProvider><Fixture/></HarnessEventsProvider>);
