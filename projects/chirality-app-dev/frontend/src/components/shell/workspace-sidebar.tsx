'use client';

import { useRef, type KeyboardEvent } from 'react';
import { FileTreePanel } from './file-tree-panel';
import { OperatorToolkitPanel } from './operator-toolkit-panel';
import { SubagentStreamView } from './subagent-stream-view';
import { ToolStreamView } from './tool-stream-view';

export type SidebarTabId =
  | 'files'
  | 'tools'
  | 'subagents'
  | 'document'
  | 'workflow'
  | 'toolkit';

type SidebarTab = {
  id: SidebarTabId;
  label: string;
};

const SIDEBAR_TABS: readonly SidebarTab[] = [
  { id: 'files', label: 'Files' },
  { id: 'tools', label: 'Tools' },
  { id: 'subagents', label: 'Subagents' },
  { id: 'document', label: 'Document' },
  { id: 'workflow', label: 'Workflow' },
  { id: 'toolkit', label: 'Tool Kit' }
];

const TAB_PANEL_ID = 'workspace-sidebar-panel';

function tabButtonId(id: SidebarTabId): string {
  return `workspace-sidebar-tab-${id}`;
}

function SidebarPlaceholder({ title, note }: { title: string; note: string }): JSX.Element {
  return (
    <aside className="panel panel--stream panel--placeholder">
      <header className="panel-header">
        <h2>{title}</h2>
      </header>
      <div className="panel-body">
        <p className="panel-empty">{note}</p>
      </div>
    </aside>
  );
}

type WorkspaceSidebarProps = {
  activeTab: SidebarTabId;
  onTabChange: (tab: SidebarTabId) => void;
};

/**
 * The collapsible multi-view sidebar (DESIGN §3.2). One tabbed pane is the
 * normal modality for reaching the workspace views: the live file tree, the
 * bridge-fed Tools and Subagents streams, and (seeded) Document/Workflow peeks,
 * plus the local Tool Kit folded in from its former dedicated pane.
 *
 * Active-tab state is lifted to the parent shell so it survives the pane being
 * unmounted on collapse. Implements the WAI-ARIA tabs pattern: roving tabindex,
 * arrow/Home/End navigation, and a labelled tabpanel.
 */
export function WorkspaceSidebar({ activeTab, onTabChange }: WorkspaceSidebarProps): JSX.Element {
  const tabRefs = useRef<Partial<Record<SidebarTabId, HTMLButtonElement | null>>>({});

  function focusTab(id: SidebarTabId): void {
    onTabChange(id);
    tabRefs.current[id]?.focus();
  }

  function handleTabKeyDown(event: KeyboardEvent<HTMLButtonElement>): void {
    const index = SIDEBAR_TABS.findIndex((tab) => tab.id === activeTab);
    if (index < 0) {
      return;
    }

    if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
      event.preventDefault();
      focusTab(SIDEBAR_TABS[(index + 1) % SIDEBAR_TABS.length].id);
      return;
    }

    if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
      event.preventDefault();
      focusTab(SIDEBAR_TABS[(index - 1 + SIDEBAR_TABS.length) % SIDEBAR_TABS.length].id);
      return;
    }

    if (event.key === 'Home') {
      event.preventDefault();
      focusTab(SIDEBAR_TABS[0].id);
      return;
    }

    if (event.key === 'End') {
      event.preventDefault();
      focusTab(SIDEBAR_TABS[SIDEBAR_TABS.length - 1].id);
    }
  }

  return (
    <div className="workspace-sidebar">
      <div className="workspace-sidebar-tabs" role="tablist" aria-label="Workspace views">
        {SIDEBAR_TABS.map((tab) => {
          const isActive = tab.id === activeTab;
          return (
            <button
              key={tab.id}
              ref={(node) => {
                tabRefs.current[tab.id] = node;
              }}
              type="button"
              role="tab"
              id={tabButtonId(tab.id)}
              aria-selected={isActive}
              aria-controls={TAB_PANEL_ID}
              tabIndex={isActive ? 0 : -1}
              className={
                isActive
                  ? 'workspace-sidebar-tab workspace-sidebar-tab--active'
                  : 'workspace-sidebar-tab'
              }
              onClick={() => {
                onTabChange(tab.id);
              }}
              onKeyDown={handleTabKeyDown}
            >
              {tab.label}
            </button>
          );
        })}
      </div>

      <div
        className="workspace-sidebar-body"
        role="tabpanel"
        id={TAB_PANEL_ID}
        aria-labelledby={tabButtonId(activeTab)}
        tabIndex={0}
      >
        {activeTab === 'files' ? <FileTreePanel /> : null}
        {activeTab === 'tools' ? <ToolStreamView /> : null}
        {activeTab === 'subagents' ? <SubagentStreamView /> : null}
        {activeTab === 'document' ? (
          <SidebarPlaceholder
            title="Document"
            note="Document preview lands with the content API (Phase 4)."
          />
        ) : null}
        {activeTab === 'workflow' ? (
          <SidebarPlaceholder
            title="Workflow"
            note="Workflow design is a thin peek now; the full surface is the deferred secondary phase."
          />
        ) : null}
        {activeTab === 'toolkit' ? <OperatorToolkitPanel /> : null}
      </div>
    </div>
  );
}
