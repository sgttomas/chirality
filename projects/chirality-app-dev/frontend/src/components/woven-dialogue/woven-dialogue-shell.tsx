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
import type { SessionRecord } from '@chirality/harness-contract/types';
import { listHarnessSessions, harnessApiErrorMessage } from '../../lib/harness/client';
import type {
  CoordinationWorkItem,
  SelectedSessionReplayState
} from '../../lib/woven-dialogue/contracts';
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
  writeWovenWorkspaceStateToStorage,
  type WovenWorkspaceState
} from '../../lib/woven-dialogue/woven-workspace-state';
import { useHarnessStreaming } from '../workspace/harness-events-provider';
import { useWorkspace } from '../workspace/workspace-provider';
import { ChatPanel } from '../shell/chat-panel';
import { DocumentView } from '../shell/document-view';
import { PersonaPicker } from '../shell/persona-picker';
import { ShellFrame } from '../shell/shell-frame';
import { PipelineSurface } from '../pipeline/pipeline-surface';
import { WorkbenchSurface } from '../workbench/workbench-surface';
import { ActivityShelf } from './activity-shelf';
import { CoordinationPanel } from './coordination-panel';
import { DialogueViewport, type FocusedDialogueSurface } from './dialogue-viewport';
import { Navigator, type WovenSurface } from './navigator';
import { SelectedSessionReplayLens } from './selected-session-replay-lens';

type WovenDialogueShellProps = {
  defaultSurface: WovenSurface;
};

type ResizeTarget = 'navigator' | 'coordination' | 'activity';

const EMPTY_WORK_ITEMS: readonly CoordinationWorkItem[] = [];

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

export function WovenDialogueShell({
  defaultSurface
}: WovenDialogueShellProps): JSX.Element {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const { projectRoot } = useWorkspace();
  const streaming = useHarnessStreaming();
  const [activeSurface, setActiveSurface] = useState<WovenSurface>(defaultSurface);
  const [primarySessionId, setPrimarySessionId] = useState<string>();
  const [workspaceState, setWorkspaceState] = useState<WovenWorkspaceState>(
    createDefaultWovenWorkspaceState
  );
  const [stateHydrated, setStateHydrated] = useState(false);
  const [sessions, setSessions] = useState<SessionRecord[]>([]);
  const [sessionsLoading, setSessionsLoading] = useState(false);
  const [sessionsError, setSessionsError] = useState<string | null>(null);
  const [sessionRefreshToken, setSessionRefreshToken] = useState(0);
  const replayLoaderRef = useRef<SelectedSessionReplayLoader>();
  const previousProjectRootRef = useRef(projectRoot);
  const [replayState, setReplayState] = useState<SelectedSessionReplayState>({
    status: 'IDLE'
  });
  const dialogueInputRef = useRef<HTMLInputElement | null>(null);
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
    setWorkspaceState(readWovenWorkspaceStateFromStorage(window.localStorage));
    setStateHydrated(true);
  }, []);

  useEffect(() => {
    if (!stateHydrated || typeof window === 'undefined') {
      return;
    }
    writeWovenWorkspaceStateToStorage(window.localStorage, workspaceState);
  }, [stateHydrated, workspaceState]);

  useEffect(() => {
    setActiveSurface(defaultSurface);
  }, [defaultSurface]);

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
  }, [projectRoot, sessionRefreshToken]);

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

  const returnToPrimaryDialogue = useCallback((): void => {
    replayLoaderRef.current?.cancel();
    updateWorkspaceState({ selectedReplaySessionId: null });
    setActiveSurface('dialogue');
    window.requestAnimationFrame(() => {
      const input = document.querySelector<HTMLInputElement>('[data-chat-input="primary"]');
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
      if (decision.outcome !== 'SELECT_REPLAY') {
        return;
      }

      updateWorkspaceState({ selectedReplaySessionId: sessionId });
      void replayLoaderRef.current?.load(sessionId, {
        observedAt: new Date().toISOString(),
        availableSessionIds: new Set(sessions.map((session) => session.sessionId))
      });
    },
    [
      primarySessionId,
      replayState,
      returnToPrimaryDialogue,
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
      const startValue =
        target === 'navigator'
          ? workspaceState.navigatorWidth
          : target === 'coordination'
            ? workspaceState.coordinationWidth
            : workspaceState.activityHeight;
      resizeRef.current = {
        target,
        startX: event.clientX,
        startY: event.clientY,
        startValue
      };
    },
    [workspaceState]
  );

  useEffect(() => {
    const handleMove = (event: globalThis.PointerEvent): void => {
      const resize = resizeRef.current;
      if (!resize) {
        return;
      }
      if (resize.target === 'navigator') {
        updateWorkspaceState({
          navigatorWidth: clamp(resize.startValue + event.clientX - resize.startX, 220, 620),
          navigatorCollapsed: false
        });
      } else if (resize.target === 'coordination') {
        updateWorkspaceState({
          coordinationWidth: clamp(resize.startValue - event.clientX + resize.startX, 280, 680),
          coordinationCollapsed: false
        });
      } else {
        updateWorkspaceState({
          activityHeight: clamp(resize.startValue - event.clientY + resize.startY, 120, 480),
          activityCollapsed: false
        });
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
  }, [updateWorkspaceState]);

  const resizeByKeyboard = useCallback(
    (target: ResizeTarget, key: string, shift: boolean): void => {
      const step = shift ? 40 : 16;
      if (target === 'navigator') {
        const value =
          key === 'Home'
            ? 220
            : key === 'End'
              ? 620
              : workspaceState.navigatorWidth + (key === 'ArrowRight' ? step : -step);
        updateWorkspaceState({
          navigatorWidth: clamp(value, 220, 620),
          navigatorCollapsed: key === 'Home'
        });
      } else if (target === 'coordination') {
        const value =
          key === 'Home'
            ? 280
            : key === 'End'
              ? 680
              : workspaceState.coordinationWidth + (key === 'ArrowLeft' ? step : -step);
        updateWorkspaceState({
          coordinationWidth: clamp(value, 280, 680),
          coordinationCollapsed: key === 'Home'
        });
      } else {
        const value =
          key === 'Home'
            ? 120
            : key === 'End'
              ? 480
              : workspaceState.activityHeight + (key === 'ArrowUp' ? step : -step);
        updateWorkspaceState({
          activityHeight: clamp(value, 120, 480),
          activityCollapsed: key === 'Home'
        });
      }
    },
    [updateWorkspaceState, workspaceState]
  );

  const style = {
    '--woven-navigator-width': `${
      workspaceState.navigatorCollapsed ? 56 : workspaceState.navigatorWidth
    }px`,
    '--woven-coordination-width': `${
      workspaceState.coordinationCollapsed ? 56 : workspaceState.coordinationWidth
    }px`,
    '--woven-activity-height': `${
      workspaceState.activityCollapsed ? 68 : workspaceState.activityHeight
    }px`
  } as CSSProperties;
  const replayVisible = replayState.status !== 'IDLE';
  const focusedSurfaceVisible = !replayVisible && activeSurface !== 'dialogue';
  const focusedSurface = useMemo<FocusedDialogueSurface | undefined>(() => {
    if (!focusedSurfaceVisible) {
      return undefined;
    }
    if (activeSurface === 'document') {
      return {
        id: 'document',
        title: 'Artifacts',
        content: <DocumentView />
      };
    }
    if (activeSurface === 'workbench') {
      return {
        id: 'workbench',
        title: 'Workbench',
        content: <WorkbenchSurface />
      };
    }
    return {
      id: 'pipeline',
      title: 'Pipeline',
      content: <PipelineSurface />
    };
  }, [activeSurface, focusedSurfaceVisible]);

  return (
    <ShellFrame
      section="CHAT"
      title="Woven Dialogue"
      subtitle="A shared professional workspace where dialogue produces inspectable artifacts and governed work."
      variant="workspace"
    >
      <section className="woven-workspace" style={style}>
        <main className="woven-dialogue-region" aria-label="Primary Dialogue and focused views">
          <DialogueViewport
            primaryDialogue={
              <>
                <div className="woven-dialogue-toolbar">
                  <div>
                    <p className="woven-eyebrow">Primary conversation</p>
                    <h2>Dialogue</h2>
                  </div>
                  <PersonaPicker disabled={streaming} />
                </div>
                <Suspense fallback={<p className="panel-empty">Loading primary dialogue…</p>}>
                  <ChatPanel onActiveSessionChange={setPrimarySessionId} />
                </Suspense>
              </>
            }
            replayLens={
              replayVisible ? (
                <SelectedSessionReplayLens
                  state={replayState}
                  primarySessionId={primarySessionId}
                  onReturnToPrimary={returnToPrimaryDialogue}
                  onRetry={() => {
                    const sessionId = selectedReplayId(replayState);
                    if (sessionId) {
                      loadReplay(sessionId);
                    }
                  }}
                />
              ) : undefined
            }
            focusedSurface={focusedSurface}
            onReturnToPrimary={returnToPrimaryDialogue}
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
            onClick={() => {
              updateWorkspaceState({
                navigatorCollapsed: !workspaceState.navigatorCollapsed
              });
            }}
          >
            {workspaceState.navigatorCollapsed ? 'Open Navigator' : 'Close Navigator'}
          </button>
          {!workspaceState.navigatorCollapsed ? (
            <Navigator
              activeSurface={activeSurface}
              legacyHref={legacyHref}
              onOpenSurface={(surface) => {
                replayLoaderRef.current?.cancel();
                updateWorkspaceState({ selectedReplaySessionId: null });
                setActiveSurface(surface);
              }}
            />
          ) : (
            <span className="woven-collapsed-label">Navigator</span>
          )}
        </div>

        <div
          className="woven-resize-handle woven-resize-handle--vertical woven-resize-handle--navigator"
          role="separator"
          tabIndex={0}
          aria-label="Resize Navigator"
          aria-orientation="vertical"
          aria-valuemin={220}
          aria-valuemax={620}
          aria-valuenow={workspaceState.navigatorWidth}
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
          aria-valuemax={680}
          aria-valuenow={workspaceState.coordinationWidth}
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
          <button
            type="button"
            className="woven-region-toggle button-muted"
            onClick={() => {
              updateWorkspaceState({
                coordinationCollapsed: !workspaceState.coordinationCollapsed
              });
            }}
          >
            {workspaceState.coordinationCollapsed ? 'Open Coordination' : 'Close Coordination'}
          </button>
          {!workspaceState.coordinationCollapsed ? (
            <CoordinationPanel
              activeView={workspaceState.coordinationView}
              workItems={EMPTY_WORK_ITEMS}
              hierarchy={hierarchy}
              sessionsLoading={sessionsLoading}
              sessionsError={sessionsError}
              selectedSessionId={selectedReplayId(replayState)}
              selectionDisabled={streaming}
              onSelectView={(coordinationView) => {
                updateWorkspaceState({ coordinationView });
              }}
              onRefreshSessions={() => {
                setSessionRefreshToken((token) => token + 1);
              }}
              onSelectSession={loadReplay}
            />
          ) : (
            <span className="woven-collapsed-label">Coordination</span>
          )}
        </aside>

        <div
          className="woven-resize-handle woven-resize-handle--horizontal"
          role="separator"
          tabIndex={0}
          aria-label="Resize Activity Shelf"
          aria-orientation="horizontal"
          aria-valuemin={120}
          aria-valuemax={480}
          aria-valuenow={workspaceState.activityHeight}
          onPointerDown={(event) => {
            beginResize(event, 'activity');
          }}
          onKeyDown={(event) => {
            if (['ArrowUp', 'ArrowDown', 'Home', 'End'].includes(event.key)) {
              event.preventDefault();
              resizeByKeyboard('activity', event.key, event.shiftKey);
            }
          }}
        />

        <ActivityShelf
          collapsed={workspaceState.activityCollapsed}
          onToggleCollapsed={() => {
            updateWorkspaceState({
              activityCollapsed: !workspaceState.activityCollapsed
            });
          }}
        />
      </section>
    </ShellFrame>
  );
}
