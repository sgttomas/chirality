'use client';

import { usePathname, useSearchParams } from 'next/navigation';
import React, { FormEvent, useEffect, useMemo, useState } from 'react';
import {
  HarnessApiClientError,
  bootHarnessSession,
  createHarnessSession,
  interruptHarnessSession,
  streamHarnessTurn
} from '../../lib/harness/client';
import { toHarnessUiError, type HarnessUiError } from '../../lib/harness/error-display';
import {
  buildChatDraftStorageKey,
  persistChatDraftSnapshotToStorage,
  readChatDraftSnapshotFromStorage
} from '../../lib/harness/chat-draft';
import { type UiAttachment } from '../../lib/harness/ui-attachments';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import { CHAT_SECTION } from '../../lib/shell/loop-first';
import { resolvePersona } from '../../lib/shell/persona-resolution';
import { useHarnessEventActions } from '../workspace/harness-events-provider';
import { useToolkit } from '../workspace/toolkit-provider';
import { useWorkspace } from '../workspace/workspace-provider';
import { ChatMarkdown } from './chat-markdown';
import { FilePicker } from './file-picker';
import { PermissionRequests } from './permission-requests';
import { useRuntimeEpoch } from './runtime-connectivity-provider';

type ChatMessage = {
  id: string;
  role: 'operator' | 'assistant';
  text: string;
  attachments?: UiAttachment[];
};

type ActiveSession = {
  sessionId: string;
  projectRoot: string;
  persona: string;
  mode: string;
};

// Operator permission modes (DESIGN §3.4), mapped to the harness's canonical
// `opts.mode` values consumed by the permission overlay. Sent per turn so the
// operator can switch the posture live without re-creating the session.
type OperatorModeOption = {
  value: string;
  label: string;
};

const OPERATOR_MODES: readonly OperatorModeOption[] = [
  { value: 'readOnly', label: 'Read-only' },
  { value: 'ask', label: 'Plan (ask)' },
  { value: 'workspaceWrite', label: 'Gated-write' },
  { value: 'bypass', label: 'Autonomous' }
];

const DEFAULT_OPERATOR_MODE = 'ask';

function readTextField(data: unknown): string | undefined {
  if (!data || typeof data !== 'object') {
    return undefined;
  }

  const text = (data as Record<string, unknown>).text;
  return typeof text === 'string' ? text : undefined;
}

function resolveMode(pathname: string): string {
  if (pathname.startsWith('/workbench')) {
    return 'WORKBENCH';
  }

  if (pathname.startsWith('/pipeline')) {
    return 'PIPELINE';
  }

  if (pathname.startsWith('/chat')) {
    return CHAT_SECTION;
  }

  return 'PORTAL';
}

function mergeAttachments(existing: UiAttachment[], incoming: UiAttachment[]): UiAttachment[] {
  const deduped = new Map<string, UiAttachment>();
  for (const item of existing) {
    deduped.set(item.path, item);
  }
  for (const item of incoming) {
    deduped.set(item.path, item);
  }
  return [...deduped.values()];
}

function AttachmentChips({ items }: { items: UiAttachment[] }): JSX.Element | null {
  if (items.length === 0) {
    return null;
  }

  return (
    <ul className="attachment-chip-list">
      {items.map((item) => (
        <li key={item.path} className="attachment-chip" title={item.path}>
          <span>{item.displayName}</span>
          <small>{item.clientType}</small>
        </li>
      ))}
    </ul>
  );
}

function isHarnessEvent(value: unknown): value is HarnessEvent {
  return (
    Boolean(value) &&
    typeof value === 'object' &&
    typeof (value as Record<string, unknown>).type === 'string'
  );
}

type ChatPanelProps = {
  onActiveSessionChange?: (sessionId: string | undefined) => void;
};

export function ChatPanel({ onActiveSessionChange }: ChatPanelProps = {}): JSX.Element {
  const { projectRoot } = useWorkspace();
  const { optsPayload } = useToolkit();
  const { appendEvent, clearEvents, setStreaming } = useHarnessEventActions();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [draft, setDraft] = useState('');
  const [attachments, setAttachments] = useState<UiAttachment[]>([]);
  const [draftStorageWritable, setDraftStorageWritable] = useState(true);
  const [draftStorageWarning, setDraftStorageWarning] = useState<string | null>(null);
  const [pickerOpen, setPickerOpen] = useState(false);
  const [operatorMode, setOperatorMode] = useState<string>(DEFAULT_OPERATOR_MODE);
  const [activeSession, setActiveSession] = useState<ActiveSession | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const [runtimeStatus, setRuntimeStatus] = useState<string | null>(null);
  const [runtimeError, setRuntimeError] = useState<HarnessUiError | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'seed-1',
      role: 'assistant',
      text: 'Harness chat wiring is active. Select a Working Root and send a prompt.'
    }
  ]);

  const runtimeEpoch = useRuntimeEpoch();

  useEffect(() => {
    onActiveSessionChange?.(activeSession?.sessionId);
  }, [activeSession?.sessionId, onActiveSessionChange]);

  // The red banner under the composer is a record of one failed attempt, not a
  // live status. Once the main process reports a fresh binding, the reason it
  // gives ("runtime daemon client is not configured") is no longer true, so it
  // is dropped rather than left to outlive the outage. Cleared, never retried:
  // re-sending an operator's prompt without them asking is not ours to do.
  useEffect(() => {
    if (runtimeEpoch === 0) {
      return;
    }
    setRuntimeError(null);
  }, [runtimeEpoch]);

  const activePersona = useMemo(
    () => resolvePersona(searchParams.get('agent')),
    [searchParams]
  );
  const activeMode = useMemo(() => resolveMode(pathname), [pathname]);

  const draftStorageKey = useMemo(() => {
    if (!projectRoot) {
      return null;
    }
    return buildChatDraftStorageKey(projectRoot, activePersona, activeMode);
  }, [projectRoot, activePersona, activeMode]);

  useEffect(() => {
    setActiveSession((existing) => {
      if (
        existing &&
        existing.projectRoot === projectRoot &&
        existing.persona === activePersona &&
        existing.mode === activeMode
      ) {
        return existing;
      }
      return null;
    });
  }, [projectRoot, activePersona, activeMode]);

  useEffect(() => {
    if (!draftStorageKey || typeof window === 'undefined') {
      setDraft('');
      setAttachments([]);
      setDraftStorageWritable(true);
      setDraftStorageWarning(null);
      return;
    }

    const result = readChatDraftSnapshotFromStorage(window.localStorage, draftStorageKey);
    setDraft(result.snapshot.draft);
    setAttachments(result.snapshot.attachments);
    setDraftStorageWritable(result.writable);
    setDraftStorageWarning(result.warning);
  }, [draftStorageKey]);

  useEffect(() => {
    if (!draftStorageKey || typeof window === 'undefined' || !draftStorageWritable) {
      return;
    }

    const result = persistChatDraftSnapshotToStorage(
      window.localStorage,
      draftStorageKey,
      {
        draft,
        attachments
      }
    );

    if (!result.writable) {
      setDraftStorageWritable(false);
    }

    if (result.warning) {
      setDraftStorageWarning((existing) => existing ?? result.warning);
    }
  }, [draftStorageKey, draft, attachments, draftStorageWritable]);

  async function ensureSessionBooted(): Promise<ActiveSession> {
    if (!projectRoot) {
      throw new Error('Select a Working Root before sending a prompt.');
    }

    if (
      activeSession &&
      activeSession.projectRoot === projectRoot &&
      activeSession.persona === activePersona &&
      activeSession.mode === activeMode
    ) {
      return activeSession;
    }

    setRuntimeStatus('Creating session...');
    const session = await createHarnessSession({
      projectRoot,
      persona: activePersona,
      mode: activeMode
    });

    setRuntimeStatus('Booting session...');
    const boot = await bootHarnessSession(
      optsPayload
        ? {
            sessionId: session.sessionId,
            opts: optsPayload
          }
        : {
            sessionId: session.sessionId
          }
    );

    const nextSession: ActiveSession = {
      sessionId: boot.session.sessionId,
      projectRoot,
      persona: activePersona,
      mode: activeMode
    };
    setActiveSession(nextSession);
    return nextSession;
  }

  async function interruptTurn(): Promise<void> {
    if (!activeSession || !isRunning) {
      return;
    }

    try {
      setRuntimeStatus('Interrupt requested...');
      setRuntimeError(null);
      await interruptHarnessSession({ sessionId: activeSession.sessionId });
    } catch (error) {
      setRuntimeError(toHarnessUiError(error));
      setRuntimeStatus(null);
    }
  }

  async function submitDraft(event: FormEvent<HTMLFormElement>): Promise<void> {
    event.preventDefault();
    const text = draft.trim();

    if (!text && attachments.length === 0) {
      return;
    }

    const preservedDraft = draft;
    const preservedAttachments = attachments;

    setRuntimeError(null);
    setRuntimeStatus('Preparing turn...');
    setDraft('');
    setAttachments([]);
    setIsRunning(true);
    setStreaming(true);
    clearEvents();

    const operatorMessageId = `operator-${Date.now()}`;
    const assistantId = `assistant-${Date.now() + 1}`;

    const operatorMessage: ChatMessage = {
      id: operatorMessageId,
      role: 'operator',
      text,
      attachments: preservedAttachments
    };
    const assistantMessage: ChatMessage = {
      id: assistantId,
      role: 'assistant',
      text: ''
    };

    setMessages((existing) => [...existing, operatorMessage, assistantMessage]);

    try {
      const session = await ensureSessionBooted();

      let assistantText = '';
      let processExitError: HarnessApiClientError | Error | null = null;

      setRuntimeStatus('Running turn...');

      await streamHarnessTurn(
        {
          sessionId: session.sessionId,
          message: text,
          attachments: preservedAttachments.map((item) => item.path),
          opts: { ...(optsPayload ?? {}), mode: operatorMode }
        },
        (streamEvent) => {
          if (streamEvent.event === 'harness:event') {
            if (isHarnessEvent(streamEvent.data)) {
              appendEvent(streamEvent.data);
            }
            return;
          }

          if (streamEvent.event === 'chat:delta') {
            const chunk = readTextField(streamEvent.data);
            if (chunk) {
              assistantText += chunk;
              setMessages((existing) =>
                existing.map((item) =>
                  item.id === assistantId
                    ? {
                        ...item,
                        text: assistantText
                      }
                    : item
                )
              );
            }
            return;
          }

          if (streamEvent.event === 'chat:complete') {
            const completed = readTextField(streamEvent.data);
            if (completed) {
              assistantText = completed;
              setMessages((existing) =>
                existing.map((item) =>
                  item.id === assistantId
                    ? {
                        ...item,
                        text: assistantText
                      }
                    : item
                )
              );
            }
            return;
          }

          if (
            streamEvent.event === 'turn:error' &&
            streamEvent.data &&
            typeof streamEvent.data === 'object'
          ) {
            const payload = streamEvent.data as Record<string, unknown>;
            const fatal = payload.fatal !== false;
            const errorMessage =
              typeof payload.message === 'string' && payload.message.trim().length > 0
                ? payload.message
                : 'Turn failed during streaming.';

            if (fatal) {
              const errorType =
                typeof payload.errorType === 'string' && payload.errorType.trim().length > 0
                  ? payload.errorType
                  : 'SDK_FAILURE';
              const errorStatus = typeof payload.status === 'number' ? payload.status : 500;
              processExitError = new HarnessApiClientError(
                errorStatus,
                errorType,
                errorMessage,
                payload.details
              );
            }
            return;
          }

          if (
            streamEvent.event === 'process:exit' &&
            streamEvent.data &&
            typeof streamEvent.data === 'object'
          ) {
            const payload = streamEvent.data as Record<string, unknown>;
            const exitCode = typeof payload.exitCode === 'number' ? payload.exitCode : 0;
            const interrupted = payload.interrupted === true;

            if (interrupted && !assistantText) {
              assistantText = 'Turn interrupted by operator.';
              setMessages((existing) =>
                existing.map((item) =>
                  item.id === assistantId
                    ? {
                        ...item,
                        text: assistantText
                      }
                    : item
                )
              );
            }

            if (exitCode !== 0) {
              const errorMessage =
                typeof payload.error === 'string' && payload.error.trim().length > 0
                  ? payload.error
                  : `Turn failed with exit code ${exitCode}.`;
              const errorType =
                typeof payload.errorType === 'string' && payload.errorType.trim().length > 0
                  ? payload.errorType
                  : null;
              const errorStatus = typeof payload.status === 'number' ? payload.status : 500;

              processExitError = errorType
                ? new HarnessApiClientError(
                    errorStatus,
                    errorType,
                    errorMessage,
                    payload.errorDetails
                  )
                : new Error(errorMessage);
            }
          }
        }
      );

      if (processExitError) {
        throw processExitError;
      }

      if (!assistantText.trim()) {
        setMessages((existing) =>
          existing.map((item) =>
            item.id === assistantId
              ? {
                  ...item,
                  text: 'No assistant text was returned for this turn.'
                }
              : item
          )
        );
      }

      setRuntimeStatus(null);
    } catch (error) {
      const uiError = toHarnessUiError(error);
      setRuntimeError(uiError);
      setRuntimeStatus(null);
      setDraft(preservedDraft);
      setAttachments(preservedAttachments);
      setMessages((existing) =>
        existing.filter((item) => item.id !== operatorMessageId && item.id !== assistantId)
      );
    } finally {
      setIsRunning(false);
      setStreaming(false);
    }
  }

  return (
    <aside className="panel panel--chat">
      <header className="panel-header">
        <h2>Chat Panel</h2>
        <p className="chat-meta">
          Persona: {activePersona} | Section: {activeMode}
        </p>
        <label className="chat-mode-selector">
          <span>Operator mode</span>
          <select
            value={operatorMode}
            disabled={isRunning}
            onChange={(event) => {
              setOperatorMode(event.target.value);
            }}
          >
            {OPERATOR_MODES.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </label>
      </header>

      <div className="panel-body chat-transcript">
        {!projectRoot ? (
          <p className="panel-empty">Select a Working Root before starting a harness turn.</p>
        ) : null}
        {messages.map((message) => (
          <article key={message.id} className={`chat-bubble chat-bubble--${message.role}`}>
            {message.text ? (
              message.role === 'assistant' ? (
                <ChatMarkdown source={message.text} />
              ) : (
                <p>{message.text}</p>
              )
            ) : null}
            {message.attachments && message.attachments.length > 0 ? (
              <AttachmentChips items={message.attachments} />
            ) : null}
          </article>
        ))}
        <PermissionRequests sessionId={activeSession?.sessionId ?? null} active={isRunning} />
      </div>

      {/* Composer dock: every notice that sits between the transcript and the
          composer lives in one block, so the chat panel always lays out as
          exactly four rows (header / transcript / dock / composer). Before
          this wrapper the row count varied with state, the transcript's
          flexible row was squeezed below its own padding, and its box
          overflowed on top of the Attachments row (Stage C defect). */}
      <div className="chat-composer-dock">
        {draftStorageWarning ? (
          <div className="chat-storage-warning toolkit-warning" role="status" aria-live="polite">
            <p>{draftStorageWarning}</p>
            <button
              type="button"
              className="button-muted"
              onClick={() => {
                setDraftStorageWarning(null);
              }}
            >
              Dismiss
            </button>
          </div>
        ) : null}

        <div className="chat-attachment-preview" aria-live="polite">
          <div className="chat-attachment-header">
            <strong>Attachments</strong>
            <div>
              <button
                type="button"
                className="button-muted"
                onClick={() => {
                  setPickerOpen(true);
                }}
                disabled={!projectRoot || isRunning}
              >
                Attach Files
              </button>
              <button
                type="button"
                className="button-muted"
                onClick={() => {
                  setAttachments([]);
                }}
                disabled={attachments.length === 0 || isRunning}
              >
                Clear
              </button>
            </div>
          </div>

          {attachments.length === 0 ? (
            <p className="panel-empty">No attachments selected.</p>
          ) : (
            <ul className="attachment-chip-list">
              {attachments.map((item) => (
                <li key={item.path} className="attachment-chip" title={item.path}>
                  <span>{item.displayName}</span>
                  <small>{item.clientType}</small>
                  <button
                    type="button"
                    className="button-muted"
                    onClick={() => {
                      setAttachments((existing) =>
                        existing.filter((entry) => entry.path !== item.path)
                      );
                    }}
                  >
                    Remove
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>

        {runtimeStatus ? <p className="chat-runtime-status">{runtimeStatus}</p> : null}

        {runtimeError ? (
          <div className="chat-runtime-error">
            <p className="chat-runtime-error-title">
              {runtimeError.title}
              {runtimeError.code ? ` (${runtimeError.code})` : ''}
            </p>
            <p>{runtimeError.message}</p>
            <p>{runtimeError.nextStep}</p>
          </div>
        ) : null}
      </div>

      <form
        className="chat-input-row"
        onSubmit={(event) => {
          void submitDraft(event);
        }}
      >
        <input
          aria-label="Chat input"
          data-chat-input="primary"
          value={draft}
          disabled={!projectRoot || isRunning}
          onChange={(event) => {
            setDraft(event.target.value);
            if (runtimeError) {
              setRuntimeError(null);
            }
          }}
          placeholder={
            projectRoot ? `Send prompt as ${activePersona}...` : 'Select a Working Root first...'
          }
        />
        <button
          type="submit"
          disabled={!projectRoot || isRunning || (!draft.trim() && attachments.length === 0)}
        >
          {isRunning ? 'Running...' : 'Send'}
        </button>
        <button
          type="button"
          className="button-muted"
          onClick={() => {
            void interruptTurn();
          }}
          disabled={!isRunning || !activeSession}
        >
          Interrupt
        </button>
      </form>

      <FilePicker
        open={pickerOpen}
        projectRoot={projectRoot ?? ''}
        existingPaths={attachments.map((item) => item.path)}
        onClose={() => {
          setPickerOpen(false);
        }}
        onAddAttachments={(incoming) => {
          setAttachments((existing) => mergeAttachments(existing, incoming));
        }}
      />
    </aside>
  );
}
