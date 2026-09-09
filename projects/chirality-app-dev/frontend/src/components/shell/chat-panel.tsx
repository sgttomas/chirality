'use client';

import { usePathname, useSearchParams } from 'next/navigation';
import React, { FormEvent, useEffect, useMemo, useRef, useState, useCallback } from 'react';
import {
  HarnessApiClientError,
  bootHarnessSession,
  createHarnessSession,
  interruptHarnessSession,
  replaySessionEvents,
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
import { FolderSelect, getNativeFolderBridge } from './folder-select';
import { PersonaPicker } from './persona-picker';
import { ChatMarkdown } from './chat-markdown';
import { FilePicker } from './file-picker';
import { PermissionRequests } from './permission-requests';
import { useRuntimeEpoch } from './runtime-connectivity-provider';
import {
  getNativePlanCapability,
  exportNativePlanRevision,
  listNativePlanRevisions,
  replaceSelectedMethods,
  resolveSelectedContext,
  type InteractionMode,
  type QualifiedMethodReference,
  type ChiralityRoleName,
  MethodSelectionClientError
} from '../../lib/harness/method-selection-client';
import type { FrozenInstructionBasisV3, InstructionHistoryRecordV3, NativePlanCapabilityResponse, NativePlanRevision } from '@chirality/runtime-contracts/v3';
import type { SelectedSessionReplayProjection } from '../../lib/woven-dialogue/contracts';
import type { RuntimeSessionRecordV3 } from '@chirality/runtime-contracts';

type ChatMessage = {
  id: string;
  role: 'operator' | 'assistant';
  persona?: string;
  projectRoot?: string;
  text: string;
  attachments?: UiAttachment[];
  methods?: QualifiedMethodReference[];
  instructionBasis?: FrozenInstructionBasisV3;
  instructionHistory?: readonly InstructionHistoryRecordV3[];
};

type ActiveSession = {
  sessionId: string;
  projectRoot: string;
  selectedRootAtBinding: string;
  persona: string;
  mode: string;
  selectedMethods: readonly QualifiedMethodReference[];
  methodSelectionRevision: number;
  instructionBasisId: string;
};

export type ResumeConversationRequest = {
  requestId: number;
  projection: SelectedSessionReplayProjection;
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
  { value: 'ask', label: 'Ask before changes' },
  { value: 'workspaceWrite', label: 'Gated-write' },
  { value: 'bypass', label: 'Autonomous' }
];

const DEFAULT_OPERATOR_MODE = 'ask';
const PLAIN_MODE_LABELS: Record<string, string> = { readOnly: 'Read only', ask: 'Ask before changes', workspaceWrite: 'Approve each write', bypass: 'Run on its own' };

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

function sameMethodSelection(
  left: readonly QualifiedMethodReference[],
  right: readonly QualifiedMethodReference[]
): boolean {
  return left.length === right.length && left.every((item, index) => {
    const other = right[index];
    return other !== undefined && item.kind === other.kind && item.name === other.name &&
      item.source === other.source && item.sourceRootId === other.sourceRootId;
  });
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

function nativePlanText(revision: NativePlanRevision): string {
  const plan = revision.sourceEvent.plan;
  return typeof plan === 'string' ? plan : JSON.stringify(plan, null, 2);
}

function instructionActivityLabel(record: InstructionHistoryRecordV3): string {
  switch (record.type) {
    case 'selection.changed': return 'Role or method selection updated';
    case 'resource.loaded': return 'Method resource loaded';
    case 'instruction-basis.resolved': return 'Instruction basis recorded';
    case 'native-plan.revised': return 'Native plan revised';
    case 'provider-span.continued': return 'Conversation continued with a new provider span';
    default: return 'Instruction context updated';
  }
}

function recordedRoleForTurn(
  turnId: string | undefined,
  history: readonly InstructionHistoryRecordV3[],
  bases: readonly FrozenInstructionBasisV3[]
): ChiralityRoleName | undefined {
  if (!turnId) return undefined;
  const basisRecord = history.find(record => record.type === 'instruction-basis.resolved' && record.turnId === turnId);
  const basisId = basisRecord && typeof basisRecord.basisId === 'string' ? basisRecord.basisId : undefined;
  return basisId ? bases.find(basis => basis.basisId === basisId)?.roleId : undefined;
}

function isHarnessEvent(value: unknown): value is HarnessEvent {
  return (
    Boolean(value) &&
    typeof value === 'object' &&
    typeof (value as Record<string, unknown>).type === 'string'
  );
}

type ChatPanelProps = {
  presentation?: 'woven';
  knownRoots?: readonly { path: string; lastUsedAt: string }[];
  newChatRequest?: number;
  folderSelectionPending?: boolean;
  onFolderSelectionPending?: (pending: boolean) => void;
  onBindingChange?: (binding: { root: string | null; locked: boolean }) => void;
  onDraftCaptured?: () => void;
  onActiveSessionChange?: (sessionId: string | undefined) => void;
  onSessionBootedPrompt?: (input: { sessionId: string; prompt: string; persona: string }) => void;
  fileCatalog?: readonly string[];
  onOpenFile?: (path: string) => void;
  selectedMethods?: QualifiedMethodReference[];
  onSelectedMethodsChange?: (methods: QualifiedMethodReference[]) => void;
  onOpenMethods?: () => void;
  resumeConversation?: ResumeConversationRequest;
  onConversationResumed?: (sessionId: string) => void;
};

export function ChatPanel({ onDraftCaptured, onActiveSessionChange, onSessionBootedPrompt, presentation, knownRoots = [], newChatRequest = 0, folderSelectionPending = false, onFolderSelectionPending, onBindingChange, fileCatalog = [], onOpenFile, selectedMethods = [], onSelectedMethodsChange = () => {}, onOpenMethods, resumeConversation, onConversationResumed }: ChatPanelProps = {}): JSX.Element {
  const { projectRoot, applyProjectRoot } = useWorkspace();
  const { optsPayload } = useToolkit();
  const { appendEvent, clearEvents, setStreaming } = useHarnessEventActions();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [draft, setDraft] = useState('');
  const [attachments, setAttachments] = useState<UiAttachment[]>([]);
  const [draftStorageWritable, setDraftStorageWritable] = useState(true);
  const [draftStorageWarning, setDraftStorageWarning] = useState<string | null>(null);
  const [loadedDraftKey, setLoadedDraftKey] = useState<string | null>(null);
  const [pickerOpen, setPickerOpen] = useState(false);
  const [operatorMode, setOperatorMode] = useState<string>(DEFAULT_OPERATOR_MODE);
  const [interactionMode, setInteractionMode] = useState<InteractionMode>('chat');
  const [planCapability, setPlanCapability] = useState<NativePlanCapabilityResponse>({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'Start a chat to check native Plan Mode support.' });
  const [planRevisions, setPlanRevisions] = useState<readonly NativePlanRevision[]>([]);
  const [planExportStatus, setPlanExportStatus] = useState<string | null>(null);
  const [conversationBinding, setConversationBinding] = useState<{ projectRoot: string; selectedRootAtBinding: string } | null>(null);
  const [activeSession, setActiveSession] = useState<ActiveSession | null>(null);
  const activeSessionIdRef = useRef<string>();
  const lastInstructionSequenceRef = useRef(0);
  const [isRunning, setIsRunning] = useState(false);
  const [nativeFolderError, setNativeFolderError] = useState<string | null>(null);
  const nativeSelectionActive = useRef(false);
  const [folderSyncError, setFolderSyncError] = useState<string | null>(null);
  const composerRef = useRef<HTMLTextAreaElement | null>(null);
  const bindingGeneration = useRef(0);
  const canonicalTransition = useRef<{ from: string; to: string; persona: string; mode: string } | null>(null);
  const previousContext = useRef<{ root: string | null; persona: string; mode: string } | null>(null);
  const newChatSeen = useRef(newChatRequest);
  const resumeRequestSeen = useRef(0);
  const capturedTitleSessions = useRef(new Set<string>());
  const selectedMethodsSnapshot = useRef<readonly QualifiedMethodReference[]>(selectedMethods);
  const selectedMethodsRevision = useRef(0);
  const [runtimeStatus, setRuntimeStatus] = useState<string | null>(null);
  const [runtimeError, setRuntimeError] = useState<HarnessUiError | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'seed-1',
      role: 'assistant',
      persona: resolvePersona(searchParams.get('agent')),
      text: presentation === 'woven' ? 'What would you like to work on?' : 'Harness chat wiring is active. Select a Working Root and send a prompt.'
    }
  ]);

  const runtimeEpoch = useRuntimeEpoch();

  useEffect(() => {
    activeSessionIdRef.current = activeSession?.sessionId;
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
  const personaLabel = activePersona.toLowerCase().split('_').map(word => word[0].toUpperCase() + word.slice(1)).join(' ');
  const activeMode = useMemo(() => resolveMode(pathname), [pathname]);

  if (!sameMethodSelection(selectedMethodsSnapshot.current, selectedMethods)) {
    selectedMethodsSnapshot.current = selectedMethods;
    selectedMethodsRevision.current += 1;
  }

  const draftRoot = activeSession?.projectRoot ?? conversationBinding?.selectedRootAtBinding ?? projectRoot;
  // Unbound entry drafts remain role-specific. Once a Runtime session exists,
  // its stable id owns the draft across role transitions and keeps two chats
  // with the same root and role isolated from one another.
  const draftPersona = activeSession ? `session:${activeSession.sessionId}` : activePersona;
  const draftStorageKey = useMemo(() => {
    if (!draftRoot) {
      return null;
    }
    return buildChatDraftStorageKey(draftRoot, draftPersona, activeMode);
  }, [draftRoot, draftPersona, activeMode]);
  const draftIdentityReady = typeof window === 'undefined' || Boolean(draftStorageKey && loadedDraftKey === draftStorageKey);

  useEffect(() => {
    setActiveSession((existing) => {
      if (
        existing &&
        (existing.projectRoot === projectRoot || existing.selectedRootAtBinding === projectRoot) &&
        existing.mode === activeMode
      ) {
        return existing;
      }
      return null;
    });
  }, [projectRoot, activePersona, activeMode]);

  useEffect(() => {
    if (!draftStorageKey || typeof window === 'undefined') {
      setLoadedDraftKey(null);
      setDraft('');
      setAttachments([]);
      onSelectedMethodsChange([]);
      setDraftStorageWritable(true);
      setDraftStorageWarning(null);
      return;
    }

    const result = readChatDraftSnapshotFromStorage(window.localStorage, draftStorageKey);
    setDraft(result.snapshot.draft);
    setAttachments(result.snapshot.attachments);
    const hydratedMethods = isRunning && activeSession && result.snapshot.methods.length === 0
      ? selectedMethodsSnapshot.current
      : result.snapshot.methods;
    onSelectedMethodsChange([...hydratedMethods]);
    setDraftStorageWritable(result.writable);
    setDraftStorageWarning(result.warning);
    setLoadedDraftKey(draftStorageKey);
  }, [draftStorageKey]);

  useEffect(() => {
    if (!draftStorageKey || loadedDraftKey !== draftStorageKey || typeof window === 'undefined' || !draftStorageWritable) {
      return;
    }

    const result = persistChatDraftSnapshotToStorage(
      window.localStorage,
      draftStorageKey,
      {
        draft,
        attachments,
        methods: selectedMethods
      }
    );

    if (!result.writable) {
      setDraftStorageWritable(false);
    }

    if (result.warning) {
      setDraftStorageWarning((existing) => existing ?? result.warning);
    }
  }, [draftStorageKey, loadedDraftKey, draft, attachments, selectedMethods, draftStorageWritable]);

  useEffect(() => {
    if (!activeSession) {
      setPlanExportStatus(null);
      setPlanCapability({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'Start a chat to check native Plan Mode support.' });
      setPlanRevisions([]);
      setInteractionMode('chat');
      return;
    }
    const controller = new AbortController();
    void getNativePlanCapability(activeSession.sessionId, controller.signal)
      .then(capability => {
        if (controller.signal.aborted) return;
        setPlanCapability(capability);
        if (capability.status !== 'qualified') setInteractionMode('chat');
      })
      .catch(error => {
        if (controller.signal.aborted) return;
        setPlanCapability({ schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: error instanceof Error ? error.message : 'Native Plan Mode is unavailable.' });
        setInteractionMode('chat');
      });
    void listNativePlanRevisions(activeSession.sessionId, controller.signal)
      .then(result => { if (!controller.signal.aborted) setPlanRevisions(result.revisions); })
      .catch(() => { if (!controller.signal.aborted) setPlanRevisions([]); });
    return () => controller.abort();
  }, [activeSession?.sessionId]);

  useEffect(() => {
    const expected = canonicalTransition.current;
    const previous = previousContext.current;
    const isCanonicalSynchronization = expected && previous?.root === expected.from && projectRoot === expected.to && activePersona === expected.persona && activeMode === expected.mode;
    if (!isCanonicalSynchronization) bindingGeneration.current++;
    canonicalTransition.current = null;
    previousContext.current = { root: projectRoot, persona: activePersona, mode: activeMode };
  }, [projectRoot, activePersona, activeMode]);

  useEffect(() => {
    onBindingChange?.({ root: conversationBinding?.projectRoot ?? projectRoot, locked: Boolean(conversationBinding) || isRunning });
  }, [conversationBinding, projectRoot, isRunning, onBindingChange]);

  useEffect(() => {
    const field = composerRef.current;
    if (!field) return;
    field.style.height = 'auto';
    field.style.height = `${Math.min(field.scrollHeight, 132)}px`;
  }, [draft]);

  useEffect(() => {
    if (newChatSeen.current === newChatRequest) return;
    newChatSeen.current = newChatRequest;
    if (isRunning || folderSelectionPending) return;
    if ((draft.trim() || attachments.length || selectedMethods.length) && !window.confirm('Start a new chat and discard the unsent draft, attachments, and methods?')) return;
    bindingGeneration.current++;
    activeSessionIdRef.current = undefined;
    lastInstructionSequenceRef.current = 0;
    setActiveSession(null); setConversationBinding(null); setDraft(''); setAttachments([]); onSelectedMethodsChange([]); setMessages([]);
    setRuntimeError(null); setRuntimeStatus(null); setFolderSyncError(null);
    // This clears only the current local view; no runtime record is deleted.
    clearEvents();
  }, [newChatRequest, isRunning, folderSelectionPending, draft, attachments, selectedMethods, clearEvents, onSelectedMethodsChange]);

  useEffect(() => {
    if (!resumeConversation || resumeConversation.requestId === resumeRequestSeen.current || isRunning) return;
    const { projection } = resumeConversation;
    const continuation = projection.session?.continuation;
    if (!continuation || continuation.roleId !== activePersona || continuation.projectRoot !== projectRoot) return;
    resumeRequestSeen.current = resumeConversation.requestId;
    bindingGeneration.current += 1;
    lastInstructionSequenceRef.current = projection.instructionHistory.reduce((maximum, record) => Math.max(maximum, record.sequence), 0);
    const nextMessages: ChatMessage[] = projection.transcript.items.flatMap(item => {
      if (item.kind !== 'message' || !item.role || !item.text) return [];
      const recordedRole = item.role === 'assistant'
        ? recordedRoleForTurn(item.turnId, projection.instructionHistory, projection.instructionBases)
        : undefined;
      return [{ id: `replay-${item.key}`, role: item.role === 'user' ? 'operator' as const : 'assistant' as const,
        ...(item.role === 'assistant' ? { ...(recordedRole ? { persona: recordedRole } : {}), projectRoot: continuation.projectRoot } : {}), text: item.text }];
    });
    const latestBasis = projection.instructionBases.at(-1);
    let lastOperatorIndex = -1;
    for (let index = nextMessages.length - 1; index >= 0; index -= 1) {
      if (nextMessages[index]?.role === 'operator') { lastOperatorIndex = index; break; }
    }
    if (lastOperatorIndex >= 0 && (latestBasis || projection.instructionHistory.length)) {
      nextMessages[lastOperatorIndex] = { ...nextMessages[lastOperatorIndex],
        ...(latestBasis ? { instructionBasis: latestBasis } : {}), instructionHistory: projection.instructionHistory };
    }
    const nextSession: ActiveSession = {
      sessionId: projection.selectedSessionId,
      projectRoot: continuation.projectRoot,
      selectedRootAtBinding: continuation.projectRoot,
      persona: continuation.roleId,
      mode: activeMode,
      selectedMethods: continuation.selectedMethods,
      methodSelectionRevision: continuation.methodSelectionRevision,
      instructionBasisId: continuation.instructionBasisId
    };
    activeSessionIdRef.current = nextSession.sessionId;
    setConversationBinding({ projectRoot: continuation.projectRoot, selectedRootAtBinding: continuation.projectRoot });
    setActiveSession(nextSession);
    setOperatorMode(continuation.permissionMode);
    setInteractionMode(continuation.interactionMode);
    setMessages(nextMessages.length ? nextMessages : [{ id: `resumed-${projection.selectedSessionId}`, role: 'assistant', persona: continuation.roleId, projectRoot: continuation.projectRoot, text: 'Continue this conversation when you are ready.',
      ...(latestBasis ? { instructionBasis: latestBasis } : {}), instructionHistory: projection.instructionHistory }]);
    setRuntimeError(null); setRuntimeStatus(null); setFolderSyncError(null);
    clearEvents();
    onConversationResumed?.(nextSession.sessionId);
  }, [resumeConversation, isRunning, activePersona, activeMode, projectRoot, clearEvents, onConversationResumed]);

  const selectNativeFolder = useCallback(async (intent: { path?: string; error?: string }) => {
    if (intent.error) { setNativeFolderError(intent.error); return; }
    if (conversationBinding || isRunning || folderSelectionPending || nativeSelectionActive.current) {
      setNativeFolderError('Start a new chat before opening another folder.'); return;
    }
    if (!intent.path) { setNativeFolderError('Drop a folder from Finder to choose it.'); return; }
    nativeSelectionActive.current = true; onFolderSelectionPending?.(true); setNativeFolderError(null);
    try {
      if (!await applyProjectRoot(intent.path)) setNativeFolderError('This folder could not be selected.');
    } finally { nativeSelectionActive.current = false; onFolderSelectionPending?.(false); }
  }, [conversationBinding, isRunning, folderSelectionPending, applyProjectRoot, onFolderSelectionPending]);

  useEffect(() => {
    if (presentation !== 'woven') return;
    return getNativeFolderBridge()?.subscribeOpen(intent => { void selectNativeFolder(intent); });
  }, [presentation, selectNativeFolder]);

  useEffect(() => {
    if (presentation !== 'woven' || !projectRoot) return;
    let cancelled = false;
    void getNativeFolderBridge()?.registerRecent(projectRoot).then(result => {
      if (!cancelled && !result.ok) setNativeFolderError(result.error ?? 'Unable to register this folder in Open Recent.');
    }).catch(() => { if (!cancelled) setNativeFolderError('Unable to register this folder in Open Recent.'); });
    return () => { cancelled = true; };
  }, [presentation, projectRoot]);

  async function ensureSessionBooted(): Promise<ActiveSession> {
    if (!projectRoot) {
      throw new Error('Select a Working Root before sending a prompt.');
    }

    if (
      activeSession &&
      (activeSession.projectRoot === projectRoot || activeSession.selectedRootAtBinding === projectRoot) &&
      activeSession.mode === activeMode
    ) {
      return activeSession;
    }

    const generation = bindingGeneration.current;
    const selectedRootAtBinding = conversationBinding?.selectedRootAtBinding ?? projectRoot;
    setRuntimeStatus('Creating session...');
    const session = await createHarnessSession({
      projectRoot: conversationBinding?.projectRoot ?? projectRoot,
      persona: activePersona,
      roleId: activePersona,
      mode: activeMode,
      interactionMode,
      permissionMode: operatorMode as 'readOnly' | 'ask' | 'workspaceWrite' | 'bypass',
      selectedMethods
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

    if (generation !== bindingGeneration.current) throw new Error('The chat context changed while the session was starting.');
    const runtimeSession = boot.session as typeof boot.session & Partial<RuntimeSessionRecordV3>;
    const nextSession: ActiveSession = {
      sessionId: boot.session.sessionId,
      projectRoot: boot.session.projectRoot,
      selectedRootAtBinding,
      persona: activePersona,
      mode: activeMode,
      selectedMethods: runtimeSession.schemaVersion === 'chirality.session/v3' && Array.isArray(runtimeSession.selectedMethods)
        ? runtimeSession.selectedMethods : selectedMethods,
      methodSelectionRevision: runtimeSession.schemaVersion === 'chirality.session/v3' && typeof runtimeSession.methodSelectionRevision === 'number'
        ? runtimeSession.methodSelectionRevision : 0,
      instructionBasisId: runtimeSession.schemaVersion === 'chirality.session/v3' && typeof runtimeSession.instructionBasisId === 'string'
        ? runtimeSession.instructionBasisId : ''
    };
    activeSessionIdRef.current = nextSession.sessionId;
    if (conversationBinding && nextSession.projectRoot !== conversationBinding.projectRoot) {
      throw new Error('The new agent session returned a different folder. Start a new chat to use that folder.');
    }
    if (presentation === 'woven') {
      setConversationBinding(existing => existing ?? { projectRoot: nextSession.projectRoot, selectedRootAtBinding });
    }
    setActiveSession(nextSession);
    if (presentation === 'woven' && nextSession.projectRoot !== projectRoot) {
      canonicalTransition.current = { from: projectRoot, to: nextSession.projectRoot, persona: activePersona, mode: activeMode };
      const applied = await applyProjectRoot(nextSession.projectRoot);
      if (!applied) canonicalTransition.current = null;
      if (generation !== bindingGeneration.current) throw new Error('The chat context changed while its folder was being synchronized.');
      if (!applied) setFolderSyncError('The session is bound to its recorded folder, but file browsing could not switch to it. Start a new chat to choose a folder again.');
    }
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
    if (isRunning || folderSelectionPending || nativeSelectionActive.current || !draftIdentityReady) return;
    const text = draft.trim();

    if (!text && attachments.length === 0) {
      return;
    }

    const requestGeneration = bindingGeneration.current;
    const preservedDraft = draft;
    const preservedAttachments = attachments;
    const preservedMethods = [...selectedMethods];
    const submittedMethodsRevision = selectedMethodsRevision.current;
    const submittedDraftStorageKey = draftStorageKey;
    const submittedWithoutSession = activeSession === null;

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
      attachments: preservedAttachments,
      methods: preservedMethods
    };
    const assistantMessage: ChatMessage = {
      id: assistantId,
      role: 'assistant',
      persona: activePersona,
      text: ''
    };

    setMessages((existing) => [...existing, operatorMessage, assistantMessage]);

    try {
      const session = await ensureSessionBooted();
      const roleChanged = session.persona !== activePersona;
      let activeMethods = session.selectedMethods;
      let activeRevision = session.methodSelectionRevision;
      let activeBasisId = session.instructionBasisId;
      if (preservedMethods.length > 0 || roleChanged) {
        const replacement = await replaceSelectedMethods(session.sessionId, preservedMethods.length ? preservedMethods : undefined, {
          ...(roleChanged ? { roleId: activePersona as ChiralityRoleName } : {}),
          boundaryConfirmed: true,
          ...(preservedMethods.length ? { selectionMode: 'merge' as const } : {}),
          ...(session.methodSelectionRevision > 0 ? { expectedRevision: session.methodSelectionRevision } : {}),
          ...(session.instructionBasisId ? { expectedBasisId: session.instructionBasisId } : {})
        });
        activeMethods = replacement.methods;
        activeRevision = replacement.revision;
        activeBasisId = replacement.basisPreview.id;
        // The transition is durable even if the subsequent provider turn
        // fails. Advance the local CAS projection immediately so a retry does
        // not submit the pre-transition revision.
        setActiveSession(existing => existing?.sessionId === session.sessionId ? {
          ...existing,
          persona: activePersona,
          selectedMethods: activeMethods,
          methodSelectionRevision: activeRevision,
          instructionBasisId: activeBasisId
        } : existing);
      }
      await resolveSelectedContext({
        sessionId: session.sessionId,
        roleId: activePersona as ChiralityRoleName,
        methods: activeMethods,
        interactionMode,
        permissionMode: operatorMode as 'readOnly' | 'ask' | 'workspaceWrite' | 'bypass'
      });
      setMessages((existing) => existing.map((item) => item.id === assistantId ? { ...item, projectRoot: session.projectRoot } : item));
      if (text && !capturedTitleSessions.current.has(session.sessionId)) {
        capturedTitleSessions.current.add(session.sessionId);
        onSessionBootedPrompt?.({ sessionId: session.sessionId, prompt: text, persona: activePersona });
      }

      let assistantText = '';
      let processExitError: HarnessApiClientError | Error | null = null;

      setRuntimeStatus('Running turn...');

      await streamHarnessTurn(
        {
          sessionId: session.sessionId,
          message: text,
          attachments: preservedAttachments.map((item) => item.path),
          interactionMode,
          permissionMode: operatorMode as 'readOnly' | 'ask' | 'workspaceWrite' | 'bypass',
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
      const replay = await replaySessionEvents(session.sessionId).catch(() => undefined);
      const recordedBasis = replay?.instructionBases.at(-1);
      const replaySession = replay?.session;
      const replayRuntimeSession: RuntimeSessionRecordV3 | undefined = replaySession && 'schemaVersion' in replaySession && replaySession.schemaVersion === 'chirality.session/v3'
        ? replaySession as RuntimeSessionRecordV3
        : undefined;
      const newInstructionHistory = replay?.instructionHistory.filter(record => record.sequence > lastInstructionSequenceRef.current) ?? [];
      if (replay?.instructionHistory.length) {
        lastInstructionSequenceRef.current = Math.max(...replay.instructionHistory.map(record => record.sequence));
      }
      if (recordedBasis || newInstructionHistory.length) {
        setMessages(existing => existing.map(item => item.id === operatorMessageId ? { ...item, ...(recordedBasis ? { instructionBasis: recordedBasis } : {}), instructionHistory: newInstructionHistory } : item));
      }
      setActiveSession(existing => existing?.sessionId === session.sessionId ? {
        ...existing,
        persona: activePersona,
        selectedMethods: replayRuntimeSession?.selectedMethods ?? recordedBasis?.selectedMethods ?? activeMethods,
        methodSelectionRevision: replayRuntimeSession?.methodSelectionRevision ?? activeRevision,
        instructionBasisId: replayRuntimeSession?.instructionBasisId ?? recordedBasis?.basisId ?? activeBasisId
      } : existing);
      // Composer method references apply to the submitted message. A selection
      // made while this turn was streaming belongs to the next message and must
      // survive completion of the earlier turn.
      if (selectedMethodsRevision.current === submittedMethodsRevision) {
        onSelectedMethodsChange([]);
      }
      // The first successful turn moves draft ownership from the entry key to
      // the canonical Runtime session key. Consume the exact prior entry key
      // so its submitted method references cannot reappear in a later New
      // chat. Edits made during the turn already belong to the session key.
      if (submittedWithoutSession && submittedDraftStorageKey && typeof window !== 'undefined') {
        persistChatDraftSnapshotToStorage(window.localStorage, submittedDraftStorageKey, {
          draft: '', attachments: [], methods: []
        });
      }
      if (interactionMode === 'native-plan') {
        void listNativePlanRevisions(session.sessionId)
          .then(result => {
            if (activeSessionIdRef.current === session.sessionId) {
              setPlanRevisions(result.revisions);
            }
          })
          .catch(() => {});
      }
    } catch (error) {
      const uiError = toHarnessUiError(error);
      setRuntimeError(uiError);
      setRuntimeStatus(null);
      if (requestGeneration === bindingGeneration.current) {
        setDraft(preservedDraft);
        setAttachments(preservedAttachments);
        // The unbound-to-session draft-key transition may have hydrated an
        // empty composer while the first turn was starting. Restore the
        // submitted references unless the operator already chose a newer
        // nonempty set for the next message during the turn.
        if (preservedMethods.length > 0 && selectedMethodsRevision.current === submittedMethodsRevision) {
          onSelectedMethodsChange(preservedMethods);
        }
      }
      setMessages((existing) =>
        existing.filter((item) => item.id !== operatorMessageId && item.id !== assistantId)
      );
    } finally {
      setIsRunning(false);
      setStreaming(false);
    }
  }

  return (
    <aside className={`panel panel--chat${presentation === 'woven' ? ' chat-panel--woven' : ''}`}>
      {presentation !== 'woven' ? <header className="panel-header">
        <h2>Chat Panel</h2>
        <p className="chat-meta">
          Role: {activePersona} | Section: {activeMode}
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
      </header> : null}

      <div className="panel-body chat-transcript">
        {!projectRoot ? (
          <p className="panel-empty">{presentation === 'woven' ? 'Choose a folder below to start a chat.' : 'Select a Working Root before starting a harness turn.'}</p>
        ) : null}
        {messages.map((message) => (
          <article key={message.id} className={`chat-bubble chat-bubble--${message.role}`}>
            {presentation === 'woven' ? <p className="chat-speaker" title={message.role === 'assistant' ? message.persona : undefined}>{message.role === 'operator' ? 'You' : (message.persona ?? 'Assistant').toLowerCase().split('_').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')}</p> : null}
            {message.text ? (
              message.role === 'assistant' ? (
                <ChatMarkdown source={message.text} projectRoot={message.projectRoot} fileCatalog={fileCatalog} onOpenFile={onOpenFile} />
              ) : (
                <p>{message.text}</p>
              )
            ) : null}
            {message.attachments && message.attachments.length > 0 ? (
              <AttachmentChips items={message.attachments} />
            ) : null}
            {message.methods?.length ? <ul className="method-chip-list" aria-label="Selected methods">{message.methods.map(method => <li key={`${method.sourceRootId}:${method.kind}:${method.name}`} className="method-chip"><span>{method.name}</span><small>{method.source}</small></li>)}</ul> : null}
            {message.instructionBasis ? <details className="chat-instruction-basis">
              <summary>Recorded instruction basis · {message.instructionBasis.suppliedEntries.length} supplied</summary>
              <p><code>{message.instructionBasis.basisId}</code> · {message.instructionBasis.roleId}</p>
              <ul>{message.instructionBasis.suppliedEntries.map((entry, index) => <li key={`${entry.sha256}:${index}`}><strong>{entry.kind}</strong> · {entry.id} · <code>{entry.sha256.slice(0, 12)}</code></li>)}</ul>
            </details> : null}
            {message.instructionHistory?.length ? <ul className="chat-instruction-events" aria-label="Recorded instruction activity">
              {message.instructionHistory.map(record => <li key={record.historyId}>{instructionActivityLabel(record)}</li>)}
            </ul> : null}
          </article>
        ))}
        {planRevisions.map(revision => <article key={`native-plan-${revision.revision}`} className="chat-bubble chat-bubble--assistant native-plan-revision">
          <p className="chat-speaker">Native plan · revision {revision.revision}</p>
          <ChatMarkdown source={nativePlanText(revision)} projectRoot={activeSession?.projectRoot} fileCatalog={fileCatalog} onOpenFile={onOpenFile} />
          <button type="button" className="button-muted" onClick={() => {
            if (!activeSession) return;
            const targetRelativePath = window.prompt(`Save this plan in ${activeSession.projectRoot} as`, `plans/native-plan-${revision.revision}.md`)?.trim();
            if (!targetRelativePath) return;
            setPlanExportStatus('Saving plan…');
            const sessionId = activeSession.sessionId;
            const request = { sessionId, revision: revision.revision, targetRelativePath };
            void exportNativePlanRevision(request)
              .then(result => { if (activeSessionIdRef.current === sessionId) setPlanExportStatus(`Plan saved to ${activeSession.projectRoot}/${result.targetRelativePath}`); })
              .catch(error => {
                if (activeSessionIdRef.current !== sessionId) return;
                if (error instanceof MethodSelectionClientError && error.status === 409 && window.confirm(`${targetRelativePath} already exists. Replace it?`)) {
                  void exportNativePlanRevision({ ...request, overwrite: true })
                    .then(result => { if (activeSessionIdRef.current === sessionId) setPlanExportStatus(`Plan saved to ${activeSession.projectRoot}/${result.targetRelativePath}`); })
                    .catch(reason => { if (activeSessionIdRef.current === sessionId) setPlanExportStatus(reason instanceof Error ? reason.message : 'The plan could not be saved.'); });
                  return;
                }
                setPlanExportStatus(error instanceof Error ? error.message : 'The plan could not be saved.');
              });
          }}>Export plan…</button>
        </article>)}
        {planExportStatus ? <p role="status">{planExportStatus}</p> : null}
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

        {presentation !== 'woven' ? (        <div className="chat-attachment-preview" aria-live="polite">
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
        </div>) : null}

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
        onDragOver={presentation === 'woven' ? event => { if (event.dataTransfer.types.includes('Files')) event.preventDefault(); } : undefined}
        onDrop={presentation === 'woven' ? event => {
          event.preventDefault();
          const bridge = getNativeFolderBridge();
          const files = event.dataTransfer.files;
          if (!bridge || files.length !== 1) { setNativeFolderError('Drop one folder from Finder to choose it.'); return; }
          void selectNativeFolder({ path: bridge.pathForFile(files[0]) });
        } : undefined}
        onSubmit={(event) => {
          void submitDraft(event);
        }}
      >
        {presentation === 'woven' && attachments.length ? <ul className="attachment-chip-list">{attachments.map(item => <li key={item.path} className="attachment-chip" title={item.path}>
          <span>{item.displayName}</span><button type="button" aria-label={`Remove ${item.displayName}`} disabled={isRunning} onClick={() => setAttachments(current => current.filter(entry => entry.path !== item.path))}>×</button>
        </li>)}</ul> : null}
        {presentation === 'woven' && selectedMethods.length ? <ul className="method-chip-list" aria-label="Methods for next turn">{selectedMethods.map(method => <li key={`${method.sourceRootId}:${method.kind}:${method.name}`} className="method-chip" title={`${method.source} · ${method.kind}`}>
          <span>{method.name}</span><small>{method.source}</small><button type="button" aria-label={`Remove ${method.name}`} disabled={isRunning} onClick={() => onSelectedMethodsChange(selectedMethods.filter(item => item !== method))}>×</button>
        </li>)}</ul> : null}
        <div className={presentation === 'woven' ? 'chat-composer-line' : 'chat-composer-line--legacy'}>
        {presentation === 'woven' ? (        <textarea
          ref={composerRef}
          rows={1}
          aria-label="Chat input"
          data-chat-input="primary"
          value={draft}
          disabled={!projectRoot || isRunning || folderSelectionPending || !draftIdentityReady}
          onKeyDown={event => {
            if (event.key === 'Enter' && !event.shiftKey && !event.nativeEvent.isComposing) {
              event.preventDefault(); event.currentTarget.form?.requestSubmit();
            }
          }}
          onCompositionEnd={event => {
            setDraft(event.currentTarget.value);
            onDraftCaptured?.();
          }}
          onChange={(event) => {
            setDraft(event.target.value);
            if (!(event.nativeEvent as InputEvent | undefined)?.isComposing) onDraftCaptured?.();
            if (runtimeError) {
              setRuntimeError(null);
            }
          }}
          placeholder={
            projectRoot ? presentation === 'woven' ? `Message ${personaLabel}…` : `Send prompt as ${activePersona}...` : presentation === 'woven' ? 'Choose a folder first…' : 'Select a Working Root first...'
          }
        />) : (        <input
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
            projectRoot ? presentation === 'woven' ? `Message ${personaLabel}…` : `Send prompt as ${activePersona}...` : presentation === 'woven' ? 'Choose a folder first…' : 'Select a Working Root first...'
          }
        />)}
        {presentation === 'woven' ? <button type="button" aria-label="Attach files" title="Attach files" disabled={!projectRoot || isRunning || folderSelectionPending || !draftIdentityReady} onClick={() => setPickerOpen(true)}>⊕</button> : null}
        {presentation === 'woven' ? <button type="button" aria-label="Choose methods" title="Choose methods" disabled={!projectRoot || isRunning || folderSelectionPending || !draftIdentityReady} onClick={onOpenMethods}>Method</button> : null}
        <button
          type="submit"
          aria-label={isRunning ? 'Running' : 'Send'}
          disabled={!projectRoot || isRunning || folderSelectionPending || !draftIdentityReady || (!draft.trim() && attachments.length === 0)}
        >
          {presentation === 'woven' ? '↑' : isRunning ? 'Running...' : 'Send'}
        </button>
        {presentation !== 'woven' || isRunning ? (        <button
          type="button"
          className="button-muted"
          onClick={() => {
            void interruptTurn();
          }}
          disabled={!isRunning || !activeSession}
        >
          Interrupt
        </button>) : null}
        </div>
      </form>
      {presentation === 'woven' ? <div className="chat-context" role="group" aria-label="Chat context">
        <span>{conversationBinding ? 'Working in' : 'Start in'}</span>
        <FolderSelect knownRoots={knownRoots} root={conversationBinding?.projectRoot ?? projectRoot} locked={Boolean(conversationBinding)} disabled={isRunning || folderSelectionPending} onPendingChange={onFolderSelectionPending} />
        <span aria-hidden="true">·</span><PersonaPicker compact disabled={isRunning} />
        <span aria-hidden="true">·</span><label className="chat-mode-selector"><span className="visually-hidden">Operator mode</span><select value={operatorMode} disabled={isRunning} onChange={event => setOperatorMode(event.target.value)}>{OPERATOR_MODES.map(option => <option key={option.value} value={option.value}>{PLAIN_MODE_LABELS[option.value]}</option>)}</select></label>
        <span aria-hidden="true">·</span><label className="chat-mode-selector"><span className="visually-hidden">Interaction mode</span><select aria-label="Interaction mode" value={interactionMode} disabled={isRunning} onChange={event => setInteractionMode(event.target.value as InteractionMode)}>
          <option value="chat">Chat</option><option value="native-plan" disabled={planCapability.status !== 'qualified'}>Plan Mode</option>
        </select></label>
        {planCapability.status === 'unavailable' ? <span title={planCapability.reason}>Plan Mode unavailable</span> : null}
        {folderSyncError ? <p role="alert">{folderSyncError}</p> : null}
        {nativeFolderError ? <p role="alert">{nativeFolderError}</p> : null}
      </div> : null}

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
