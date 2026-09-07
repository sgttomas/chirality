'use client';

import { usePathname, useSearchParams } from 'next/navigation';
import {
  default as React,
  Suspense,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
  type PointerEvent
} from 'react';
import type { SessionRecord } from '@chirality/runtime-contracts/types';
import { listHarnessSessions, harnessApiErrorMessage } from '../../lib/harness/client';
import type { SelectedSessionReplayState } from '../../lib/woven-dialogue/contracts';
import { buildRecordedAgentHierarchy } from '../../lib/woven-dialogue/recorded-agent-hierarchy';
import { guardRecordedSessionSelection } from '../../lib/woven-dialogue/guarded-session-selection';
import {
  createSelectedSessionReplayLoader,
  type SelectedSessionReplayLoader
} from '../../lib/woven-dialogue/selected-session-replay';
import {
  clearProjectScopedWovenWorkspaceState,
  createDefaultWovenWorkspaceState,
  readWovenWorkspaceStateFromStorage,
  recordWovenSessionSurface,
  writeWovenWorkspaceStateToStorage,
  type WovenWorkspaceState
} from '../../lib/woven-dialogue/woven-workspace-state';
import { useHarnessStreaming, useHarnessEvents } from '../workspace/harness-events-provider';
import { useWorkspace } from '../workspace/workspace-provider';
import { ChatPanel } from '../shell/chat-panel';
import { useRuntimeEpoch } from '../shell/runtime-connectivity-provider';
import { ShellFrame } from '../shell/shell-frame';
import { ActivityStrip } from './activity-shelf';
import { CoordinationPanel } from './coordination-panel';
import { RightPanel } from './right-panel';
import { DialogueViewport } from './dialogue-viewport';
import { Navigator, type WovenSurface } from './navigator';
import { SelectedSessionReplayLens } from './selected-session-replay-lens';

type WovenDialogueShellProps = {
  defaultSurface: WovenSurface;
};

type ResizeTarget = 'navigator' | 'coordination';

function selectedReplayId(state: SelectedSessionReplayState): string | undefined {
  if (state.status === 'READY') {
    return state.projection.selectedSessionId;
  }
  if (state.status === 'LOADING' || state.status === 'UNAVAILABLE') {
    return state.selectedSessionId;
  }
  return undefined;
}

function clamp(value: number, minimum: number, maximum: number): number {
  return Math.max(minimum, Math.min(maximum, value));
}

export function WovenDialogueShell(_props: WovenDialogueShellProps): JSX.Element {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const { projectRoot } = useWorkspace();
  const streaming = useHarnessStreaming();
  const { events } = useHarnessEvents();
  const [binding, setBinding] = useState<{ root: string | null; locked: boolean }>({ root: null, locked: false });
  const [folderSelectionPending, setFolderSelectionPending] = useState(false);
  const [newChatRequest, setNewChatRequest] = useState(0);
  const runtimeEpoch = useRuntimeEpoch();
  const [primarySessionId, setPrimarySessionId] = useState<string>();
  const [workspaceState, setWorkspaceState] = useState<WovenWorkspaceState>(
    createDefaultWovenWorkspaceState
  );
  const [availableWidth, setAvailableWidth] = useState(1440);
  const workspaceRef = useRef<HTMLElement | null>(null);
  const [coordinationView, setCoordinationView] = useState<'session' | 'agents'>('agents');
  const rightView = workspaceState.rightPanelView === 'workflows' || workspaceState.rightPanelView === 'agents' || workspaceState.rightPanelView === 'activity' || workspaceState.rightPanelView === 'settings' ? workspaceState.rightPanelView : 'files';
  const widthKey = rightView === 'files' && workspaceState.openDocumentPath ? 'document' : rightView === 'agents' && coordinationView === 'session' ? 'session' : rightView;
  const rightWidth = workspaceState.rightPanelWidths?.[widthKey] ?? (widthKey === 'files' ? 300 : widthKey === 'agents' ? 360 : 480);
  const maximumRightWidth = Math.max(280, Math.min(Math.round(availableWidth * 0.6 / 8) * 8, availableWidth - (workspaceState.navigatorCollapsed ? 56 : clamp(workspaceState.navigatorWidth, 220, 360)) - 444));
  const [stateHydrated, setStateHydrated] = useState(false);
  useEffect(() => {
    if (!projectRoot || !stateHydrated) return;
    setWorkspaceState(current => ({ ...current, knownRoots: [
      { path: projectRoot, lastUsedAt: new Date().toISOString() },
      ...(current.knownRoots ?? []).filter(root => root.path !== projectRoot)
    ].slice(0, 50) }));
  }, [projectRoot, stateHydrated]);
  const [sessions, setSessions] = useState<SessionRecord[]>([]);
  const [sessionsLoading, setSessionsLoading] = useState(false);
  const [sessionsError, setSessionsError] = useState<string | null>(null);
  const [sessionRefreshToken, setSessionRefreshToken] = useState(0);
  const replayLoaderRef = useRef<SelectedSessionReplayLoader>();
  const previousProjectRootRef = useRef(projectRoot);
  const [replayState, setReplayState] = useState<SelectedSessionReplayState>({
    status: 'IDLE'
  });
  const dialogueInputRef = useRef<HTMLInputElement | HTMLTextAreaElement | null>(null);
  const resizeRef = useRef<{
    target: ResizeTarget;
    startX: number;
    startY: number;
    startValue: number;
  } | null>(null);

  if (!replayLoaderRef.current) {
    replayLoaderRef.current = createSelectedSessionReplayLoader();
  }

  useEffect(() => {
    const loader = replayLoaderRef.current as SelectedSessionReplayLoader;
    const unsubscribe = loader.subscribe(setReplayState);
    return () => {
      unsubscribe();
      loader.dispose();
    };
  }, []);

  useEffect(() => {
    if (typeof window === 'undefined') {
      return;
    }
    const stored = readWovenWorkspaceStateFromStorage(window.localStorage);
    setWorkspaceState(stored);
    // Retired Work preferences fall back to the recorded Agents projection.
    setCoordinationView('agents');
    setStateHydrated(true);
  }, []);

  useEffect(() => {
    if (!stateHydrated || typeof window === 'undefined') {
      return;
    }
    writeWovenWorkspaceStateToStorage(window.localStorage, workspaceState);
  }, [stateHydrated, workspaceState]);

  useEffect(() => {
    const element = workspaceRef.current;
    if (!element || typeof ResizeObserver === 'undefined') return;
    const observer = new ResizeObserver(entries => {
      const width = entries[0]?.contentRect.width;
      if (width) setAvailableWidth(width);
    });
    observer.observe(element);
    return () => observer.disconnect();
  }, []);

  // The recorded session list carries no surface field, so the shell tags the
  // dialogue surface when a session is first observed. Local
  // annotation only (no project truth); first attribution wins, so this is a
  // no-op — same state reference — for every session already tagged.
  useEffect(() => {
    if (!stateHydrated || !primarySessionId) {
      return;
    }
    setWorkspaceState((current) =>
      recordWovenSessionSurface(current, primarySessionId, 'dialogue')
    );
  }, [primarySessionId, stateHydrated]);

  useEffect(() => {
    replayLoaderRef.current?.cancel();
    setSessions([]);
    setSessionsError(null);
    if (
      previousProjectRootRef.current &&
      previousProjectRootRef.current !== projectRoot
    ) {
      setWorkspaceState(clearProjectScopedWovenWorkspaceState);
    }
    previousProjectRootRef.current = projectRoot;
  }, [projectRoot]);

  useEffect(() => {
    if (primarySessionId) {
      setSessionRefreshToken((token) => token + 1);
    }
  }, [primarySessionId, streaming]);

  useEffect(() => {
    if (!projectRoot) {
      setSessions([]);
      setSessionsLoading(false);
      return;
    }

    let cancelled = false;
    setSessionsLoading(true);
    setSessionsError(null);
    listHarnessSessions(projectRoot)
      .then((records) => {
        if (!cancelled) {
          setSessions(records);
        }
      })
      .catch((error) => {
        if (!cancelled) {
          setSessionsError(harnessApiErrorMessage(error));
        }
      })
      .finally(() => {
        if (!cancelled) {
          setSessionsLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
    // `runtimeEpoch` re-lists after a reconnect. The Navigator's flat list and
    // the Coordination panel's hierarchy are both projections of `sessions`, so
    // one re-list repairs all three surfaces at once.
  }, [projectRoot, sessionRefreshToken, runtimeEpoch]);

  // Read at reconnect time only, so the recovery effect below can depend on the
  // epoch alone: depending on the replay state itself would re-arm the effect
  // with every load it performs.
  const replayStateRef = useRef(replayState);
  replayStateRef.current = replayState;
  const sessionsRef = useRef(sessions);
  sessionsRef.current = sessions;

  // A replay lens left showing UNAVAILABLE is the same stale-error class as the
  // panes above, and it is still on screen — the lens is only hidden when the
  // state is IDLE. Reload it once, straight through the loader: the selection
  // guard is for operator clicks, and it answers UNCHANGED for a re-request of
  // the session already selected.
  useEffect(() => {
    if (runtimeEpoch === 0) {
      return;
    }
    const current = replayStateRef.current;
    if (current.status !== 'UNAVAILABLE') {
      return;
    }
    void replayLoaderRef.current?.load(current.selectedSessionId, {
      observedAt: new Date().toISOString(),
      availableSessionIds: new Set(
        sessionsRef.current.map((session) => session.sessionId)
      )
    });
  }, [runtimeEpoch]);

  const hierarchy = useMemo(() => {
    const observedAt = new Date().toISOString();
    return buildRecordedAgentHierarchy(
      sessions.map((session) => {
        const source = session as SessionRecord & Record<string, unknown>;
        return {
          ...source,
          sourceReference: `session:${session.sessionId}`,
          observedAt,
          currency: 'UNKNOWN',
          status: source.status,
          role: source.role
        };
      })
    );
  }, [sessions]);

  const legacyHref = useMemo(() => {
    const params = new URLSearchParams(searchParams.toString());
    params.set('legacy', '1');
    return `${pathname}?${params.toString()}`;
  }, [pathname, searchParams]);

  const updateWorkspaceState = useCallback(
    (patch: Partial<WovenWorkspaceState>): void => {
      setWorkspaceState((current) => ({ ...current, ...patch }));
    },
    []
  );

  const restoreExpanded = useCallback(() => {
    setWorkspaceState(current => {
      if (!current.rightPanelExpanded) return current;
      const previous = current.preExpandState;
      return { ...current, rightPanelExpanded: false, preExpandState: null,
        navigatorCollapsed: previous?.leftCollapsed ?? current.navigatorCollapsed,
        rightPanelWidths: { ...current.rightPanelWidths, [widthKey]: previous?.rightWidth ?? rightWidth }
      };
    });
  }, [widthKey, rightWidth]);

  const returnToPrimaryDialogue = useCallback((): void => {
    replayLoaderRef.current?.cancel();
    updateWorkspaceState({ selectedReplaySessionId: null });
    window.requestAnimationFrame(() => {
      const input = document.querySelector<HTMLInputElement | HTMLTextAreaElement>('[data-chat-input="primary"]');
      dialogueInputRef.current = input;
      input?.focus();
    });
  }, [updateWorkspaceState]);

  const loadReplay = useCallback(
    (sessionId: string): void => {
      const decision = guardRecordedSessionSelection({
        currentState: replayState,
        requestedSessionId: sessionId,
        primarySessionId,
        recordedSessionIds: sessions.map((session) => session.sessionId),
        liveTurnActive: streaming,
        replayIsolationAvailable: true
      });
      if (decision.outcome === 'RETURN_TO_PRIMARY') {
        returnToPrimaryDialogue();
        return;
      }
      if (decision.outcome === 'UNCHANGED') {
        restoreExpanded();
        updateWorkspaceState({ coordinationCollapsed: false, rightPanelView: 'agents' });
        setCoordinationView('session');
        return;
      }
      if (decision.outcome !== 'SELECT_REPLAY') {
        return;
      }

      restoreExpanded();
      updateWorkspaceState({
        selectedReplaySessionId: sessionId,
        rightPanelView: 'agents',
        coordinationCollapsed: false
      });
      setCoordinationView('session');
      void replayLoaderRef.current?.load(sessionId, {
        observedAt: new Date().toISOString(),
        availableSessionIds: new Set(sessions.map((session) => session.sessionId))
      });
    },
    [
      primarySessionId,
      replayState,
      returnToPrimaryDialogue,
      restoreExpanded,
      sessions,
      streaming,
      updateWorkspaceState
    ]
  );

  const beginResize = useCallback(
    (event: PointerEvent<HTMLDivElement>, target: ResizeTarget): void => {
      if (event.button !== 0) {
        return;
      }
      event.preventDefault();
      if (target === 'coordination') restoreExpanded();
      const startValue =
        target === 'navigator'
          ? clamp(workspaceState.navigatorWidth, 220, 360)
          : rightWidth;
      resizeRef.current = {
        target,
        startX: event.clientX,
        startY: event.clientY,
        startValue
      };
    },
    [workspaceState, rightWidth, restoreExpanded]
  );

  useEffect(() => {
    const handleMove = (event: globalThis.PointerEvent): void => {
      const resize = resizeRef.current;
      if (!resize) {
        return;
      }
      if (resize.target === 'navigator') {
        updateWorkspaceState({
          navigatorWidth: clamp(resize.startValue + event.clientX - resize.startX, 220, 360),
          navigatorCollapsed: false
        });
      } else if (resize.target === 'coordination') {
        const width = clamp(resize.startValue - event.clientX + resize.startX, 280, maximumRightWidth);
        setWorkspaceState(current => ({ ...current,
          rightPanelWidths: { ...current.rightPanelWidths, [widthKey]: width },
          coordinationWidth: width, coordinationCollapsed: false
        }));

      }
    };
    const handleUp = (): void => {
      resizeRef.current = null;
    };
    window.addEventListener('pointermove', handleMove);
    window.addEventListener('pointerup', handleUp);
    window.addEventListener('pointercancel', handleUp);
    return () => {
      window.removeEventListener('pointermove', handleMove);
      window.removeEventListener('pointerup', handleUp);
      window.removeEventListener('pointercancel', handleUp);
    };
  }, [updateWorkspaceState, widthKey, maximumRightWidth]);

  const resizeByKeyboard = useCallback(
    (target: ResizeTarget, key: string, shift: boolean): void => {
      if (target === 'coordination') restoreExpanded();
      const step = shift ? 40 : 16;
      if (target === 'navigator') {
        const value =
          key === 'Home'
            ? 220
            : key === 'End'
              ? 360
              : clamp(workspaceState.navigatorWidth, 220, 360) + (key === 'ArrowRight' ? step : -step);
        updateWorkspaceState({
          navigatorWidth: clamp(value, 220, 360),
          navigatorCollapsed: key === 'Home'
        });
      } else if (target === 'coordination') {
        const value =
          key === 'Home'
            ? 280
            : key === 'End'
              ? maximumRightWidth
              : rightWidth + (key === 'ArrowLeft' ? step : -step);
        updateWorkspaceState({
          rightPanelWidths: { ...workspaceState.rightPanelWidths, [widthKey]: clamp(value, 280, maximumRightWidth) },
          coordinationWidth: clamp(value, 280, maximumRightWidth),
          coordinationCollapsed: key === 'Home'
        });

      }
    },
    [updateWorkspaceState, workspaceState, rightWidth, widthKey, restoreExpanded, maximumRightWidth]
  );

  const toggleExpanded = () => {
    if (workspaceState.rightPanelExpanded) { restoreExpanded(); return; }
    updateWorkspaceState({ rightPanelExpanded: true,
      preExpandState: { rightWidth, leftCollapsed: workspaceState.navigatorCollapsed },
      navigatorCollapsed: true, coordinationCollapsed: false });
  };
  const stacked = availableWidth < 960;
  const leftWidth = workspaceState.navigatorCollapsed ? 56 : Math.min(clamp(workspaceState.navigatorWidth, 220, 360), Math.max(220, availableWidth - 724));
  const visibleRightWidth = workspaceState.coordinationCollapsed ? 56 : Math.max(280, Math.min(
    workspaceState.rightPanelExpanded ? Math.round(availableWidth * 0.6 / 8) * 8 : rightWidth,
    availableWidth - leftWidth - 444
  ));
  const style = {
    ...(!stacked ? { gridTemplateColumns: `${leftWidth}px 12px minmax(420px, 1fr) 12px ${visibleRightWidth}px` } : {}),
    '--woven-activity-height': '32px'
  } as CSSProperties;
  const replayVisible = replayState.status !== 'IDLE';

  return (
    <ShellFrame
      section="CHAT"
      title="Woven Dialogue"
      subtitle="A shared professional workspace where dialogue produces inspectable artifacts and governed work."
      variant="workspace"
      folderLocked={binding.locked || streaming || folderSelectionPending}
      onFolderSelectionPending={setFolderSelectionPending}
      legacyHref={legacyHref}
      onOpenSettings={() => { restoreExpanded(); updateWorkspaceState({ rightPanelView: 'settings', coordinationCollapsed: false }); }}
      renderWorkspaceContent={({ reconnectControl, settingsControl, settingsView }) => (
      <section ref={workspaceRef} className={`woven-workspace woven-t3-workspace${stacked ? ' is-stacked' : ''}`} style={style} data-woven-surface="dialogue">
        <style>{`
          .woven-t3-workspace .woven-right-panel { display:flex; flex-direction:column; min-width:0; height:100%; overflow:auto; }
          .woven-t3-workspace:not(.is-stacked) > .woven-region.is-collapsed > .woven-region-toggle { display:grid; place-items:center; max-width:none; color:var(--ink); font-size:1rem; }
          .woven-t3-workspace > .woven-region.is-collapsed > .woven-region-toggle::after { content:none; }
          .woven-t3-workspace > .woven-region--coordination { display:flex; flex-direction:column; }
          .woven-t3-workspace > .woven-region--coordination:not(.is-collapsed) > .woven-region-toggle { position:static; align-self:flex-end; flex:0 0 auto; margin:0.4rem 0.65rem; }
          .woven-t3-workspace > .woven-region--coordination > .woven-right-panel { height:auto; min-height:0; flex:1 1 0; }
          .woven-t3-workspace .woven-right-panel > .panel { min-height:0; flex:1; }
          .woven-t3-workspace .woven-right-panel nav { overflow-wrap:anywhere; min-width:0; }
          .woven-t3-workspace .tree-item-name { text-align:left; overflow-wrap:anywhere; min-width:0; }
          .woven-t3-workspace .tree-item-name[aria-current=true] { background:var(--ground); font-weight:600; }
          .shell--workspace:has(> .woven-t3-workspace.is-stacked) { height:auto; min-height:100vh; overflow:visible; }
          .woven-t3-workspace.is-stacked { grid-template-columns:minmax(0,1fr); grid-template-rows:minmax(620px,70vh) auto auto 32px; height:auto; overflow:visible; }
          .woven-t3-workspace.is-stacked > .woven-dialogue-region { grid-column:1; grid-row:1; }
          .woven-t3-workspace.is-stacked > .woven-region--navigator { grid-column:1; grid-row:2; max-height:none; }
          .woven-t3-workspace.is-stacked .woven-navigator { height:auto; grid-template-rows:auto minmax(0,1fr) auto; }
          .woven-t3-workspace.is-stacked > .woven-region--coordination { grid-column:1; grid-row:3; height:520px; }
          .woven-t3-workspace.is-stacked > .woven-region.is-collapsed { display:flex; flex-direction:row; align-items:center; gap:0.75rem; height:auto; min-height:56px; max-height:none; padding:0.4rem 0.75rem; }
          .woven-t3-workspace.is-stacked > .woven-region.is-collapsed > .woven-region-toggle { position:static; inset:auto; transform:none; width:auto; max-width:none; min-height:36px; padding:0.4rem 0.65rem; color:var(--ink); flex:0 0 auto; }
          .woven-t3-workspace.is-stacked > .woven-region.is-collapsed > .woven-region-toggle::after { content:none; }
          .woven-t3-workspace.is-stacked > .woven-region.is-collapsed > .woven-collapsed-label { position:static; writing-mode:horizontal-tb; transform:none; min-width:0; overflow-wrap:anywhere; }
          .woven-t3-workspace.is-stacked > .woven-resize-handle--vertical { display:none; }
          .woven-t3-workspace.is-stacked > .woven-resize-handle--horizontal { grid-column:1; grid-row:4; }
          .woven-t3-workspace.is-stacked > .woven-activity-strip { grid-column:1; grid-row:4; }
        `}</style>
        <main className="woven-dialogue-region" aria-label="Primary Dialogue">
          <DialogueViewport
            primaryDialogue={
              <>
                <Suspense fallback={<p className="panel-empty">Loading primary dialogue…</p>}>
                  <ChatPanel presentation="woven" onDraftCaptured={restoreExpanded} onActiveSessionChange={setPrimarySessionId} knownRoots={workspaceState.knownRoots ?? []} onBindingChange={setBinding} newChatRequest={newChatRequest} folderSelectionPending={folderSelectionPending} onFolderSelectionPending={setFolderSelectionPending} />
                </Suspense>
              </>
            }
          />
        </main>

        <div
          className={
            workspaceState.navigatorCollapsed
              ? 'woven-region woven-region--navigator is-collapsed'
              : 'woven-region woven-region--navigator'
          }
        >
          <button
            type="button"
            className="woven-region-toggle button-muted"
            aria-label={workspaceState.navigatorCollapsed ? 'Open Navigator' : 'Close Navigator'}
            onClick={() => {
              updateWorkspaceState({
                navigatorCollapsed: !workspaceState.navigatorCollapsed
              });
            }}
          >
            {workspaceState.navigatorCollapsed ? <span className="woven-collapsed-brand" aria-hidden="true">C</span> : <span aria-hidden="true">‹</span>}
          </button>
          {!workspaceState.navigatorCollapsed ? (
            <Navigator
              footerSlot={settingsControl}
              onNewChat={() => { if (!streaming && !folderSelectionPending) setNewChatRequest(value => value + 1); }}
              activeSurface="dialogue"
              legacyHref={legacyHref}
              sessions={sessions}
              sessionSurfaces={workspaceState.sessionSurfaces}
              liveSessionId={primarySessionId}
              selectedSessionId={selectedReplayId(replayState)}
              selectionDisabled={streaming}
              sessionsLoading={sessionsLoading}
              sessionsError={sessionsError}
              onOpenSurface={returnToPrimaryDialogue}
              onSelectSession={loadReplay}
            />
          ) : (
            <div className="woven-collapsed-settings">{settingsControl}</div>
          )}
        </div>

        <div
          className="woven-resize-handle woven-resize-handle--vertical woven-resize-handle--navigator"
          role="separator"
          tabIndex={0}
          aria-label="Resize Navigator"
          aria-orientation="vertical"
          aria-valuemin={220}
          aria-valuemax={360}
          aria-valuenow={clamp(workspaceState.navigatorWidth, 220, 360)}
          onPointerDown={(event) => {
            beginResize(event, 'navigator');
          }}
          onKeyDown={(event) => {
            if (
              ['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)
            ) {
              event.preventDefault();
              resizeByKeyboard('navigator', event.key, event.shiftKey);
            }
          }}
        />

        <div
          className="woven-resize-handle woven-resize-handle--vertical woven-resize-handle--coordination"
          role="separator"
          tabIndex={0}
          aria-label="Resize Coordination Panel"
          aria-orientation="vertical"
          aria-valuemin={280}
          aria-valuemax={maximumRightWidth}
          aria-valuenow={rightWidth}
          onPointerDown={(event) => {
            beginResize(event, 'coordination');
          }}
          onKeyDown={(event) => {
            if (
              ['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)
            ) {
              event.preventDefault();
              resizeByKeyboard('coordination', event.key, event.shiftKey);
            }
          }}
        />

        <aside
          className={
            workspaceState.coordinationCollapsed
              ? 'woven-region woven-region--coordination is-collapsed'
              : 'woven-region woven-region--coordination'
          }
        >
          {workspaceState.coordinationCollapsed ? <button type="button" className="woven-region-toggle button-muted" aria-label="Open Coordination" onClick={() => updateWorkspaceState({ coordinationCollapsed: false })}>›</button> : null}
          {!workspaceState.coordinationCollapsed ? (
            <RightPanel settingsView={settingsView} folderLocked={binding.locked || streaming || folderSelectionPending} onFolderSelectionPending={setFolderSelectionPending} folderMismatch={binding.locked && Boolean(binding.root && binding.root !== projectRoot)} state={workspaceState} sessionOpen={coordinationView === 'session'}
              replayState={replayState} recordedSessionIds={sessions.map(session => session.sessionId)}
              primarySessionId={primarySessionId} liveTurnActive={streaming} onOpenParent={loadReplay}
              onView={(view) => {
                restoreExpanded();
                updateWorkspaceState({ rightPanelView: view, ...(view === 'files' ? { openDocumentPath: null } : {}) });
                if (view === 'agents') setCoordinationView('agents');
              }}
              onOpenFile={(filePath) => {
                if (!projectRoot) return;
                const prefix = `${projectRoot.replace(/\/$/, '')}/`;
                if (!filePath.startsWith(prefix)) return;
                restoreExpanded();
                updateWorkspaceState({ openDocumentPath: filePath.slice(prefix.length), rightPanelView: 'files' });
              }}
              onExpand={toggleExpanded}
              onRefreshSessions={() => setSessionRefreshToken(token => token + 1)}
              onClose={() => {
                restoreExpanded();
                if (rightView === 'files' && workspaceState.openDocumentPath) updateWorkspaceState({ openDocumentPath: null });
                else if (rightView === 'agents' && coordinationView === 'session') setCoordinationView('agents');
                else updateWorkspaceState({ coordinationCollapsed: true });
              }}
              coordination={<CoordinationPanel embedded
              activeView={coordinationView}
              replaySlot={
                replayVisible ? (
                  <SelectedSessionReplayLens
                    state={replayState}
                    primarySessionId={primarySessionId}
                    onReturnToPrimary={returnToPrimaryDialogue}
                    onRetry={() => {
                      const sessionId = selectedReplayId(replayState);
                      if (sessionId) {
                        void replayLoaderRef.current?.load(sessionId, {
                          observedAt: new Date().toISOString(),
                          availableSessionIds: new Set(sessions.map((session) => session.sessionId))
                        });
                      }
                    }}
                  />
                ) : undefined
              }
              hierarchy={hierarchy}
              sessionsLoading={sessionsLoading}
              sessionsError={sessionsError}
              selectedSessionId={selectedReplayId(replayState)}
              selectionDisabled={streaming}
              onSelectView={(coordinationView) => {
                restoreExpanded();
                setCoordinationView(coordinationView);
              }}
              onRefreshSessions={() => {
                setSessionRefreshToken((token) => token + 1);
              }}
              onSelectSession={loadReplay}
            />} />
          ) : (
            <span className="woven-collapsed-label">Coordination</span>
          )}
        </aside>

        <ActivityStrip reconnectControl={reconnectControl} running={streaming} events={events}
          onOpenDetails={() => { restoreExpanded(); updateWorkspaceState({ rightPanelView: 'activity', coordinationCollapsed: false }); }} />
      </section>
      )}
    />
  );
}
