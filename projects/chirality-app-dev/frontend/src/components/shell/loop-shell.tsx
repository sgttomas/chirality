'use client';

import { Suspense } from 'react';
import { CHAT_SECTION } from '../../lib/shell/loop-first';
import { ChatPanel } from './chat-panel';
import { PersonaPicker } from './persona-picker';
import { ShellFrame } from './shell-frame';
import { SidebarRightLoopLayout } from './sidebar-right-loop-layout';

/**
 * The loop-first / direct-chat surface (`/chat`, D-APP-23 hybrid). The live loop
 * (ChatPanel) is the primary pane and the multi-view sidebar sits on the
 * **right** — the mirror of the route surfaces, where it is on the left. The
 * sidebar collapses without unmounting the chat, so an in-flight turn survives
 * the relayout (D-APP-23 constraint). The persona picker (Type-0/Type-1,
 * D-APP-24) drives the loop via `?agent=`.
 */
export function LoopShell(): JSX.Element {
  return (
    <ShellFrame
      section={CHAT_SECTION}
      title="Direct Chat"
      subtitle="Run a live session with a Type-0/Type-1 persona; the multi-view sidebar is on the right."
    >
      <SidebarRightLoopLayout defaultSidebarTab="tools">
        <div className="loop-persona-bar">
          <PersonaPicker />
        </div>
        <div className="loop-chat-host">
          <Suspense
            fallback={
              <aside className="panel panel--chat">
                <header className="panel-header">
                  <h2>Chat Panel</h2>
                </header>
                <div className="panel-body chat-transcript">
                  <p className="panel-empty">Loading chat panel...</p>
                </div>
              </aside>
            }
          >
            <ChatPanel />
          </Suspense>
        </div>
      </SidebarRightLoopLayout>
    </ShellFrame>
  );
}
