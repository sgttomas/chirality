import { readFile } from 'node:fs/promises';
import { writeTextFileAtomically } from '../atomic-write';
import { LifecycleState, LIFECYCLE_STATES, parseLifecycleState, parseStatusDocument } from './status-parser';
import { updateStatusDocument } from './status-writer';

const STATE_INDEX = new Map<LifecycleState, number>(
  LIFECYCLE_STATES.map((state, index) => [state, index])
);

type ActorRequirement =
  | 'PREPARATION'
  | '4_DOCUMENTS'
  | 'CHIRALITY_FRAMEWORK'
  | 'WORKING_ITEMS'
  | 'HUMAN';

interface TransitionRule {
  from: LifecycleState;
  to: LifecycleState;
  actors: readonly ActorRequirement[];
  /** Human-ruled reversal (SPEC §4.3): requires a `ruling` record reference. */
  rulingReversal?: true;
}

const TRANSITION_RULES: TransitionRule[] = [
  { from: 'OPEN', to: 'INITIALIZED', actors: ['4_DOCUMENTS'] },
  { from: 'INITIALIZED', to: 'SEMANTIC_READY', actors: ['CHIRALITY_FRAMEWORK'] },
  { from: 'INITIALIZED', to: 'IN_PROGRESS', actors: ['HUMAN', 'WORKING_ITEMS'] },
  { from: 'SEMANTIC_READY', to: 'IN_PROGRESS', actors: ['HUMAN', 'WORKING_ITEMS'] },
  { from: 'IN_PROGRESS', to: 'CHECKING', actors: ['HUMAN'] },
  { from: 'CHECKING', to: 'ISSUED', actors: ['HUMAN'] },
  // SPEC §4.3 human-ruled reversal: the sole exit from an unsuccessful or withdrawn check.
  { from: 'CHECKING', to: 'IN_PROGRESS', actors: ['HUMAN'], rulingReversal: true }
];

export type TransitionErrorCode =
  | 'INVALID_STATE'
  | 'BACKWARD_TRANSITION'
  | 'TRANSITION_NOT_ALLOWED'
  | 'UNAUTHORIZED_ACTOR'
  | 'APPROVAL_SHA_REQUIRED'
  | 'INVALID_APPROVAL_SHA'
  | 'RULING_REQUIRED'
  | 'INVALID_RULING_REFERENCE'
  | 'RULING_NOT_APPLICABLE';

export class LifecycleTransitionError extends Error {
  readonly code: TransitionErrorCode;
  readonly details?: unknown;

  constructor(code: TransitionErrorCode, message: string, details?: unknown) {
    super(message);
    this.name = 'LifecycleTransitionError';
    this.code = code;
    this.details = details;
  }
}

export interface LifecycleTransitionOptions {
  date?: string;
  metadata?: Record<string, string>;
  approvalSha?: string;
  /** Ruling record authorizing `CHECKING -> IN_PROGRESS`; required for that reversal only. */
  ruling?: string;
}

export interface LifecycleTransitionResult {
  from: LifecycleState;
  to: LifecycleState;
  actor: string;
  content: string;
}

const APPROVAL_SHA_PATTERN = /^[0-9a-f]{7,64}$/i;
const RULING_REFERENCE_MAX_LENGTH = 512;
// The ruling reference is recorded inside a `[...]` history note, so it must be
// one line without brackets or control characters.
const RULING_REFERENCE_FORBIDDEN = /[\u0000-\u001f\u007f[\]]/;

function normalizeActor(actor: string): string {
  const normalized = actor.trim().toUpperCase().replace(/\s+/g, '_');
  if (normalized === 'HUMAN' || normalized === 'USER' || normalized === 'OPERATOR') {
    return 'HUMAN';
  }
  return normalized;
}

function isBackwardTransition(from: LifecycleState, to: LifecycleState): boolean {
  const fromIndex = STATE_INDEX.get(from);
  const toIndex = STATE_INDEX.get(to);
  if (fromIndex === undefined || toIndex === undefined) {
    return false;
  }
  return toIndex < fromIndex;
}

function findTransitionRule(from: LifecycleState, to: LifecycleState): TransitionRule | undefined {
  return TRANSITION_RULES.find((rule) => rule.from === from && rule.to === to);
}

/**
 * Human gates take the same approval-SHA evidence: entry to `CHECKING` or
 * `ISSUED`, and the human-ruled reversal out of `CHECKING`.
 */
function isHumanGateTransition(rule: TransitionRule): boolean {
  return rule.to === 'CHECKING' || rule.to === 'ISSUED' || rule.rulingReversal === true;
}

function parseApprovalShaForTransition(
  rule: TransitionRule,
  options: LifecycleTransitionOptions
): string | undefined {
  const { from, to } = rule;
  const approvalSha = options.approvalSha?.trim();
  if (!isHumanGateTransition(rule)) {
    return approvalSha;
  }

  if (!approvalSha) {
    throw new LifecycleTransitionError(
      'APPROVAL_SHA_REQUIRED',
      rule.rulingReversal
        ? `Reversal ${from} -> ${to} requires approvalSha evidence`
        : `Transition ${to} requires approvalSha evidence`,
      { from, to }
    );
  }

  if (!APPROVAL_SHA_PATTERN.test(approvalSha)) {
    throw new LifecycleTransitionError(
      'INVALID_APPROVAL_SHA',
      'approvalSha must be a git SHA-like hexadecimal token (7-64 chars)',
      { from, to, approvalSha }
    );
  }

  return approvalSha;
}

/**
 * Returns the ruling reference the human-ruled reversal requires, or `undefined`
 * for a transition that takes none. A ruling supplied to any other transition is
 * denied rather than silently dropped (deny-first).
 */
function parseRulingReference(
  rule: TransitionRule,
  options: LifecycleTransitionOptions
): string | undefined {
  const ruling = options.ruling?.trim() || undefined;
  const { from, to } = rule;

  if (!rule.rulingReversal) {
    if (ruling) {
      throw new LifecycleTransitionError(
        'RULING_NOT_APPLICABLE',
        `Transition ${from} -> ${to} does not take a ruling reference`,
        { from, to }
      );
    }
    return undefined;
  }

  if (!ruling) {
    throw new LifecycleTransitionError(
      'RULING_REQUIRED',
      `Reversal ${from} -> ${to} requires a ruling reference naming the human ruling record`,
      { from, to }
    );
  }
  if (ruling.length > RULING_REFERENCE_MAX_LENGTH || RULING_REFERENCE_FORBIDDEN.test(ruling)) {
    throw new LifecycleTransitionError(
      'INVALID_RULING_REFERENCE',
      `ruling must be a single-line reference of at most ${RULING_REFERENCE_MAX_LENGTH} characters without brackets`,
      { from, to }
    );
  }
  return ruling;
}

function reversalHistoryNote(
  ruling: string | undefined,
  approvalSha: string | undefined
): string | undefined {
  if (!ruling) {
    return undefined;
  }
  const basis = `reversal from CHECKING; ruling: ${ruling}`;
  return approvalSha ? `${basis}; approval SHA: ${approvalSha}` : basis;
}

function mergeTransitionMetadata(
  to: LifecycleState,
  options: LifecycleTransitionOptions,
  approvalSha: string | undefined
): Record<string, string> | undefined {
  const metadata: Record<string, string> = { ...(options.metadata ?? {}) };
  if (approvalSha) {
    if (to === 'CHECKING') {
      metadata.checkingApprovalSha = approvalSha;
    }
    if (to === 'ISSUED') {
      metadata.approvalSha = approvalSha;
    }
  }
  return Object.keys(metadata).length > 0 ? metadata : undefined;
}

export function applyLifecycleTransition(
  currentStatusContent: string,
  targetStateInput: string,
  actorInput: string,
  options: LifecycleTransitionOptions = {}
): LifecycleTransitionResult {
  const parsed = parseStatusDocument(currentStatusContent);
  const from = parsed.currentState;

  let to: LifecycleState;
  try {
    to = parseLifecycleState(targetStateInput);
  } catch (error) {
    throw new LifecycleTransitionError('INVALID_STATE', 'Target state is invalid', { error });
  }

  const rule = findTransitionRule(from, to);
  if (!rule && isBackwardTransition(from, to)) {
    throw new LifecycleTransitionError(
      'BACKWARD_TRANSITION',
      from === 'ISSUED'
        ? `Backward transitions are not allowed (${from} -> ${to}); ISSUED changes use the governed scope-change process, which this tool does not perform`
        : `Backward transitions are not allowed (${from} -> ${to}); the only admitted reversal is the human-ruled CHECKING -> IN_PROGRESS`,
      { from, to }
    );
  }

  if (!rule) {
    throw new LifecycleTransitionError(
      'TRANSITION_NOT_ALLOWED',
      `Transition ${from} -> ${to} is not allowed`,
      { from, to }
    );
  }

  const normalizedActor = normalizeActor(actorInput);
  if (!rule.actors.includes(normalizedActor as ActorRequirement)) {
    throw new LifecycleTransitionError(
      'UNAUTHORIZED_ACTOR',
      `Actor '${actorInput}' is not authorized for transition ${from} -> ${to}`,
      { from, to, actor: actorInput, expected: rule.actors }
    );
  }

  const actor = actorInput.trim() || normalizedActor;
  const approvalSha = parseApprovalShaForTransition(rule, options);
  const ruling = parseRulingReference(rule, options);
  const metadata = mergeTransitionMetadata(to, options, approvalSha);
  const updated = updateStatusDocument(currentStatusContent, {
    targetState: to,
    actor,
    date: options.date,
    metadata,
    notes: reversalHistoryNote(ruling, approvalSha)
  });

  return {
    from,
    to,
    actor,
    content: updated.content
  };
}

export async function transitionStatusFile(
  statusFilePath: string,
  targetStateInput: string,
  actorInput: string,
  options: LifecycleTransitionOptions = {}
): Promise<LifecycleTransitionResult> {
  const existingContent = await readFile(statusFilePath, 'utf8');
  const result = applyLifecycleTransition(
    existingContent,
    targetStateInput,
    actorInput,
    options
  );
  await writeTextFileAtomically(statusFilePath, result.content);
  return result;
}
