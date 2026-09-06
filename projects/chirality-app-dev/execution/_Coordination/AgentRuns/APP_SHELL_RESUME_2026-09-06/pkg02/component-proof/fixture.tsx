import React from 'react';
import {createRoot} from 'react-dom/client';
import {Navigator} from '../../../../../../frontend/src/components/woven-dialogue/navigator';
const selected: string[]=[];
const sessions = [
 {sessionId:'reveal-alpha',projectRoot:'/tmp/chirality-proof-alpha',persona:'WORKING_ITEMS',createdAt:'2026-09-06T12:00:00Z',updatedAt:'2026-09-06T12:00:00Z'},
 {sessionId:'reveal-beta',projectRoot:'/tmp/chirality-proof-beta',persona:'HELP_HUMAN',createdAt:'2026-09-05T12:00:00Z',updatedAt:'2026-09-05T12:00:00Z'},
 {sessionId:'missing-root',persona:'RESEARCH',createdAt:'2026-09-04T12:00:00Z',updatedAt:'2026-09-04T12:00:00Z'}
];
createRoot(document.getElementById('fixture')!).render(<><p className="proof-note">Component-only proof · synthetic recorded chats · no native bridge or runtime</p><div className="proof-layout"><aside><Navigator activeSurface="dialogue" legacyHref="#legacy" onOpenSurface={()=>{}} onNewChat={()=>{}} sessions={sessions} onSelectSession={id=>{selected.push(id);document.getElementById('selection')!.textContent=selected.join(',');}} /></aside><main><h1>Recorded-chat Reveal</h1><label>Continuity draft<textarea aria-label="Continuity draft" defaultValue="Unsaved fixture draft"/></label><p>Selection: <span id="selection">none</span></p><button onClick={()=>{document.documentElement.dataset.theme=document.documentElement.dataset.theme==='dark'?'light':'dark';}}>Toggle fixture theme</button></main></div></>);
