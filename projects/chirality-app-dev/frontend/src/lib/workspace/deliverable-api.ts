import type { DeliverableRecordedRegister } from '../dependencies/recorded-register';
import type { DependencyRegisterRow } from '../dependencies/schema';
import type { LifecycleState, ParsedStatusDocument } from '../lifecycle/status-parser';

const BLOCKING_DEPENDENCY_TYPES = new Set(['PREREQUISITE', 'CONSTRAINT']);
const NON_BLOCKING_SATISFACTION = new Set(['SATISFIED', 'WAIVED', 'NOT_APPLICABLE']);
const BLOCKER_SUBSET_DEPENDENCY_CLASS = 'EXECUTION';
const BLOCKER_SUBSET_TARGET_TYPE = 'DELIVERABLE';
const HUMAN_GATE_TARGETS = new Set(['CHECKING', 'ISSUED']);
const LIFECYCLE_TRANSITION_AGENTS = new Set(['CHANGE', 'WORKING_ITEMS']);

const NEXT_LIFECYCLE_TARGETS: Record<LifecycleState, LifecycleState[]> = {
  OPEN: ['INITIALIZED'],
  INITIALIZED: ['SEMANTIC_READY', 'IN_PROGRESS'],
  SEMANTIC_READY: ['IN_PROGRESS'],
  IN_PROGRESS: ['CHECKING'],
  CHECKING: ['ISSUED'],
  ISSUED: []
};

type WorkspaceErrorPayload = {
  error?: {
    type?: string;
    message?: string;
    details?: unknown;
  };
};

export class WorkspaceApiClientError extends Error {
  readonly status: number;
  readonly code: string;
  readonly details?: unknown;

  constructor(status: number, code: string, message: string, details?: unknown) {
    super(message);
    this.name = 'WorkspaceApiClientError';
    this.status = status;
    this.code = code;
    this.details = details;
  }
}

async function readJson<T>(response: Response): Promise<T | undefined> {
  try {
    return (await response.json()) as T;
  } catch {
    return undefined;
  }
}

async function requestWorkspaceApi<T>(
  input: RequestInfo | URL,
  init: RequestInit,
  fallbackMessage: string
): Promise<T> {
  const response = await fetch(input, init);
  const payload = await readJson<T & WorkspaceErrorPayload>(response);

  if (!response.ok) {
    const type = payload?.error?.type ?? 'WORKSPACE_API_ERROR';
    const message = payload?.error?.message ?? fallbackMessage;
    throw new WorkspaceApiClientError(response.status, type, message, payload?.error?.details);
  }

  if (!payload) {
    throw new WorkspaceApiClientError(
      response.status,
      'INVALID_RESPONSE',
      'Workspace API returned an empty response body'
    );
  }

  return payload as T;
}

export interface DeliverableStatusSnapshot {
  projectRoot: string;
  deliverablePath: string;
  statusFilePath: string;
  status: ParsedStatusDocument;
}

export interface DeliverableStatusTransitionResult extends DeliverableStatusSnapshot {
  transition: {
    from: string;
    to: string;
    actor: string;
  };
}

export interface DeliverableDependenciesSnapshot {
  projectRoot: string;
  deliverablePath: string;
  dependenciesFilePath: string;
  dependenciesSummaryPath?: string;
  registerPresent: boolean;
  secondarySummaryPresent: boolean;
  headers: string[];
  /** Raw Dependencies.csv rows: register evidence, not a blocker judgment. */
  rows: DependencyRegisterRow[];
  warnings: string[];
  /** The recorded register and supplier-judged blocker verdict (App SPEC §5.2). */
  recordedRegister?: DeliverableRecordedRegister;
}

export interface DeliverableStatusTransitionInput {
  projectRoot: string;
  deliverablePath: string;
  targetState: string;
  actor: string;
  date?: string;
  metadata?: Record<string, string>;
  approvalSha?: string;
  ruling?: string;
  /** Accepted scope-change amendment (ID or path) authorizing ISSUED -> IN_PROGRESS. */
  amendment?: string;
}

export interface DependencyRowSummary {
  /** Dependencies.csv rows. */
  totalRows: number;
  activeRows: number;
  /**
   * With a recorded register that gives a verdict: the number of upstream
   * suppliers blocking the deliverable (repo-root SPEC §5.3–§5.4). Without one:
   * the CSV blocker-subset row count, which is register evidence only.
   */
  activeUpstreamBlockerCandidates: number;
  bySatisfaction: Record<string, number>;
  /** CSV blocker-subset rows (`isExecutionBlockerSubsetRow`), whatever the verdict. */
  csvBlockerSubsetRows: number;
  /** `CSV_EVIDENCE` when no recorded register was read. */
  blockerState: DeliverableRecordedRegister['blockers']['blockerState'] | 'CSV_EVIDENCE';
  blockingUpstreamDeliverables: string[];
  dagPending: boolean;
  dagPendingReasons: string[];
  disagreementCount: number;
  declaredOnlyRows: number;
  /** The deliverable's tracking mode from `_DEPENDENCIES.md`, or null when no recorded register was read. */
  trackingMode: string | null;
  /** Why no verdict was given, when the state is `NOT_ASSESSED`. */
  notAssessedReason: string | null;
}

export function workspaceApiErrorMessage(error: unknown): string {
  if (error instanceof WorkspaceApiClientError) {
    return `${error.code}: ${error.message}`;
  }

  if (error instanceof Error) {
    return error.message;
  }

  return 'Unexpected workspace API failure';
}

export function currentIsoDate(now = new Date()): string {
  return now.toISOString().slice(0, 10);
}

export function nextLifecycleTargets(currentState: LifecycleState): LifecycleState[] {
  return NEXT_LIFECYCLE_TARGETS[currentState] ?? [];
}

export function requiresApprovalShaForTarget(targetState: string | undefined): boolean {
  return HUMAN_GATE_TARGETS.has((targetState ?? '').trim().toUpperCase());
}

export function canAgentTransitionLifecycle(agent: string | undefined): boolean {
  return LIFECYCLE_TRANSITION_AGENTS.has((agent ?? '').trim().toUpperCase());
}

function hasUnresolvedAssumptionGate(notes: string | undefined): boolean {
  const normalizedNotes = (notes ?? '').trim().toUpperCase();
  if (!normalizedNotes.includes('ASSUMPTION')) {
    return false;
  }

  return !normalizedNotes.includes('RESOLVED') && !normalizedNotes.includes('CLOSED');
}

export function isExecutionBlockerSubsetRow(row: DependencyRegisterRow): boolean {
  const normalizedClass = (row.DependencyClass ?? '').trim().toUpperCase();
  const normalizedStatus = (row.Status ?? '').trim().toUpperCase();
  const normalizedDirection = (row.Direction ?? '').trim().toUpperCase();
  const normalizedType = (row.DependencyType ?? '').trim().toUpperCase();
  const normalizedTargetType = (row.TargetType ?? '').trim().toUpperCase();
  const normalizedSatisfaction = (row.SatisfactionStatus ?? 'TBD').trim().toUpperCase() || 'TBD';

  if (normalizedClass !== BLOCKER_SUBSET_DEPENDENCY_CLASS) {
    return false;
  }
  if (normalizedStatus !== 'ACTIVE') {
    return false;
  }
  if (normalizedDirection !== 'UPSTREAM') {
    return false;
  }
  if (!BLOCKING_DEPENDENCY_TYPES.has(normalizedType)) {
    return false;
  }
  if (normalizedTargetType !== BLOCKER_SUBSET_TARGET_TYPE) {
    return false;
  }
  if (NON_BLOCKING_SATISFACTION.has(normalizedSatisfaction)) {
    return false;
  }

  return !hasUnresolvedAssumptionGate(row.Notes);
}

export function summarizeDependencyRows(
  rows: DependencyRegisterRow[],
  recordedRegister?: DeliverableRecordedRegister
): DependencyRowSummary {
  const bySatisfaction: Record<string, number> = {};
  let activeRows = 0;
  let csvBlockerSubsetRows = 0;

  for (const row of rows) {
    const normalizedStatus = (row.Status ?? '').trim().toUpperCase();
    const normalizedSatisfaction = (row.SatisfactionStatus ?? 'TBD').trim().toUpperCase() || 'TBD';

    bySatisfaction[normalizedSatisfaction] = (bySatisfaction[normalizedSatisfaction] ?? 0) + 1;

    if (normalizedStatus === 'ACTIVE') {
      activeRows += 1;
    }

    if (isExecutionBlockerSubsetRow(row)) {
      csvBlockerSubsetRows += 1;
    }
  }

  const blockers = recordedRegister?.blockers;
  return {
    totalRows: rows.length,
    activeRows,
    activeUpstreamBlockerCandidates: blockers
      ? blockers.blockingUpstreamCount ?? 0
      : csvBlockerSubsetRows,
    bySatisfaction,
    csvBlockerSubsetRows,
    blockerState: blockers?.blockerState ?? 'CSV_EVIDENCE',
    blockingUpstreamDeliverables: blockers?.blockingUpstreamDeliverables ?? [],
    dagPending: blockers?.dagPending ?? false,
    dagPendingReasons: blockers?.dagPendingReasons ?? [],
    disagreementCount: recordedRegister?.disagreements.length ?? 0,
    declaredOnlyRows: recordedRegister?.declaredOnlyRows.length ?? 0,
    trackingMode: recordedRegister?.trackingMode ?? null,
    notAssessedReason: blockers?.notAssessedReason ?? null
  };
}

/** Shown when no dependency summary has been read. */
export const NO_METRIC = '—';

/** The reason code of a `NOT_ASSESSED` judgment (the text before its first colon). */
function notAssessedCode(reason: string | null): string | null {
  if (!reason) {
    return null;
  }
  const separator = reason.indexOf(':');
  return (separator < 0 ? reason : reason.slice(0, separator)).trim() || null;
}

/**
 * Display text for the blocking-upstream metric: the count with its verdict,
 * or the reason no verdict is given (a zero count alone would read as
 * unblocked). A dash when nothing has been read.
 */
export function formatBlockingUpstreamMetric(summary: DependencyRowSummary | null): string {
  if (!summary) {
    return NO_METRIC;
  }
  switch (summary.blockerState) {
    case 'BLOCKED':
    case 'UNBLOCKED':
      return `${summary.activeUpstreamBlockerCandidates} (${summary.blockerState})`;
    case 'DAG_PENDING':
      return 'DAG pending (no verdict)';
    case 'NOT_TRACKED':
      return 'Not tracked (no verdict)';
    case 'NOT_ASSESSED': {
      const code = notAssessedCode(summary.notAssessedReason);
      return code ? `Not assessed (${code})` : 'Not assessed (no verdict)';
    }
    default:
      return `${summary.activeUpstreamBlockerCandidates} CSV rows (evidence only)`;
  }
}

/** Root SPEC §5.3: under DECLARED the recorded edges are a partial, human-curated view. */
export const DECLARED_READINESS_CAVEAT =
  'DECLARED tracking: the recorded register holds only the critical dependencies, so no recorded blocker is not a complete readiness judgment (SPEC §5.3).';

/**
 * A note to show under the blocking-upstream metric, or null: the full reason
 * a judgment was not assessed, or the SPEC §5.3 caveat when the deliverable's
 * tracking mode is `DECLARED` and a verdict is given.
 */
export function formatBlockingUpstreamNote(summary: DependencyRowSummary | null): string | null {
  if (!summary) {
    return null;
  }
  if (summary.blockerState === 'NOT_ASSESSED') {
    return `Not assessed: ${summary.notAssessedReason ?? 'no reason was recorded'}.`;
  }
  if (
    summary.trackingMode === 'DECLARED' &&
    (summary.blockerState === 'BLOCKED' || summary.blockerState === 'UNBLOCKED')
  ) {
    return DECLARED_READINESS_CAVEAT;
  }
  return null;
}

export async function fetchDeliverableStatus(
  projectRoot: string,
  deliverablePath: string
): Promise<DeliverableStatusSnapshot> {
  const query = new URLSearchParams({ projectRoot, deliverablePath });
  return requestWorkspaceApi<DeliverableStatusSnapshot>(
    `/api/working-root/deliverable/status?${query.toString()}`,
    { method: 'GET' },
    'Unable to read deliverable lifecycle status'
  );
}

export async function transitionDeliverableStatus(
  input: DeliverableStatusTransitionInput
): Promise<DeliverableStatusTransitionResult> {
  return requestWorkspaceApi<DeliverableStatusTransitionResult>(
    '/api/working-root/deliverable/status/transition',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to apply lifecycle transition'
  );
}

export async function fetchDeliverableDependencies(
  projectRoot: string,
  deliverablePath: string
): Promise<DeliverableDependenciesSnapshot> {
  const query = new URLSearchParams({ projectRoot, deliverablePath });
  return requestWorkspaceApi<DeliverableDependenciesSnapshot>(
    `/api/working-root/deliverable/dependencies?${query.toString()}`,
    { method: 'GET' },
    'Unable to read deliverable dependency register'
  );
}
