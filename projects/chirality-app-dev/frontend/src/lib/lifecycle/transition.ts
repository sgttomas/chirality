import { readFile, realpath } from 'node:fs/promises';
import path from 'node:path';
import { writeTextFileAtomically } from '../atomic-write';
import {
  AmendmentReopenDecision,
  AmendmentReopenUsageError,
  checkAmendmentForReopen
} from './amendment-reopen';
import { LifecycleState, LIFECYCLE_STATES, parseLifecycleState, parseStatusDocument } from './status-parser';
import { StatusWriteError, updateStatusDocument } from './status-writer';

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
  /**
   * Reopening under an accepted scope-change amendment (SPEC §4.3; D-GOV-50):
   * requires an `amendment` reference that passes the amendment check.
   */
  amendmentReopen?: true;
}

const TRANSITION_RULES: TransitionRule[] = [
  { from: 'OPEN', to: 'INITIALIZED', actors: ['4_DOCUMENTS'] },
  { from: 'INITIALIZED', to: 'SEMANTIC_READY', actors: ['CHIRALITY_FRAMEWORK'] },
  { from: 'INITIALIZED', to: 'IN_PROGRESS', actors: ['HUMAN', 'WORKING_ITEMS'] },
  { from: 'SEMANTIC_READY', to: 'IN_PROGRESS', actors: ['HUMAN', 'WORKING_ITEMS'] },
  { from: 'IN_PROGRESS', to: 'CHECKING', actors: ['HUMAN'] },
  { from: 'CHECKING', to: 'ISSUED', actors: ['HUMAN'] },
  // SPEC §4.3 human-ruled reversal: the sole exit from an unsuccessful or withdrawn check.
  { from: 'CHECKING', to: 'IN_PROGRESS', actors: ['HUMAN'], rulingReversal: true },
  // SPEC §4.3 reopening: only with an accepted amendment that names the deliverable.
  { from: 'ISSUED', to: 'IN_PROGRESS', actors: ['HUMAN'], amendmentReopen: true }
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
  | 'RULING_NOT_APPLICABLE'
  | 'AMENDMENT_NOT_APPLICABLE'
  | 'INVALID_AMENDMENT_REFERENCE'
  | 'AMENDMENT_NOT_ADMITTED'
  | 'AMENDMENT_CHECK_ERROR'
  | 'HISTORY_NOT_PRESERVED'
  | 'INVALID_METADATA';

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
  /**
   * Ruling record authorizing a human gate: required for the `CHECKING -> IN_PROGRESS`
   * reversal, optional for `IN_PROGRESS -> CHECKING` and `CHECKING -> ISSUED`, and
   * rejected for every other transition.
   */
  ruling?: string;
  /**
   * Accepted scope-change amendment authorizing `ISSUED -> IN_PROGRESS`: an
   * amendment ID (`SCA-NNN`, `SCA-APP-NNN`) or its snapshot or group-3 decision
   * path. Required for that reopening and rejected for every other transition.
   */
  amendment?: string;
}

/** Facts the synchronous validator cannot gather itself. */
export interface LifecycleTransitionContext {
  /**
   * The amendment check's decision for `options.amendment`. `transitionStatusFile`
   * runs the check; a reopening without an admitted decision is refused.
   */
  amendmentDecision?: AmendmentReopenDecision;
  /**
   * The deliverable the status file belongs to. The decision must name it;
   * when omitted, the deliverable ID in the status title is used.
   */
  deliverableId?: string;
}

/** Context for `transitionStatusFile`. */
export interface LifecycleTransitionFileContext {
  /** The working root; the amendment check for a reopening runs inside it. */
  projectRoot?: string;
}

export interface LifecycleTransitionResult {
  from: LifecycleState;
  to: LifecycleState;
  actor: string;
  content: string;
}

const APPROVAL_SHA_PATTERN = /^[0-9a-f]{7,64}$/i;
const RULING_REFERENCE_MAX_LENGTH = 512;
// The ruling reference is recorded inside a `[...]` history note whose parts are
// separated by `; `, so it must be one line without brackets, semicolons or
// control characters.
const RULING_REFERENCE_FORBIDDEN = /[\u0000-\u001f\u007f-\u009f\u2028\u2029[\];]/;
// The CHECKING entry records its approval SHA in this field; the reversal removes it.
const CHECKING_APPROVAL_SHA_FIELD = 'Checking Approval SHA';
const APPROVAL_SHA_FIELD_LABELS = new Set(['approvalsha', 'checkingapprovalsha']);
// Gate evidence callers may record through metadata, but only on a HUMAN-actor
// transition (owner decision D2, 2026-09-26). Matched by normalized label.
const HUMAN_ONLY_FIELD_LABELS = new Set([
  'authorizationbasis',
  'acceptedbasissha',
  'acceptedscopeofworksha256'
]);
const AMENDMENT_REFERENCE_MAX_LENGTH = 512;

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
  return (
    rule.to === 'CHECKING' ||
    rule.to === 'ISSUED' ||
    rule.rulingReversal === true ||
    rule.amendmentReopen === true
  );
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
        : rule.amendmentReopen
          ? `Reopening ${from} -> ${to} requires approvalSha evidence`
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
 * Returns the ruling reference for a human gate, or `undefined` when none was
 * supplied to a gate where it is optional. The human-ruled reversal requires one;
 * the forward gates into `CHECKING` and `ISSUED` accept one. A ruling supplied to
 * any other transition is denied rather than silently dropped (deny-first).
 */
function parseRulingReference(
  rule: TransitionRule,
  options: LifecycleTransitionOptions
): string | undefined {
  const ruling = options.ruling?.trim() || undefined;
  const { from, to } = rule;

  // The accepted amendment, not a ruling, authorizes a reopening.
  if (!isHumanGateTransition(rule) || rule.amendmentReopen) {
    if (ruling) {
      throw new LifecycleTransitionError(
        'RULING_NOT_APPLICABLE',
        `Transition ${from} -> ${to} does not take a ruling reference`,
        { from, to }
      );
    }
    return undefined;
  }

  if (!ruling && !rule.rulingReversal) {
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
      `ruling must be a single-line reference of at most ${RULING_REFERENCE_MAX_LENGTH} characters without brackets or semicolons`,
      { from, to }
    );
  }
  return ruling;
}

/**
 * History note for a human gate that carries a ruling: the reversal is marked as
 * such, and a forward gate records the ruling it was given.
 */
function rulingHistoryNote(
  rule: TransitionRule,
  ruling: string | undefined,
  approvalSha: string | undefined
): string | undefined {
  if (!ruling) {
    return undefined;
  }
  const parts = rule.rulingReversal
    ? ['reversal from CHECKING', `ruling: ${ruling}`]
    : [`ruling: ${ruling}`];
  if (approvalSha) {
    parts.push(`approval SHA: ${approvalSha}`);
  }
  return parts.join('; ');
}

/**
 * Returns the amendment reference of a reopening. The reopening requires one
 * (its absence is refused earlier as a backward transition); any other
 * transition rejects one rather than dropping it.
 */
function parseAmendmentReference(
  rule: TransitionRule,
  options: LifecycleTransitionOptions
): string | undefined {
  const amendment = options.amendment?.trim() || undefined;
  const { from, to } = rule;
  if (!rule.amendmentReopen) {
    if (amendment) {
      throw new LifecycleTransitionError(
        'AMENDMENT_NOT_APPLICABLE',
        `Transition ${from} -> ${to} does not take an amendment; only ISSUED -> IN_PROGRESS does`,
        { from, to }
      );
    }
    return undefined;
  }
  if (
    !amendment ||
    amendment.length > AMENDMENT_REFERENCE_MAX_LENGTH ||
    RULING_REFERENCE_FORBIDDEN.test(amendment)
  ) {
    throw new LifecycleTransitionError(
      'INVALID_AMENDMENT_REFERENCE',
      `amendment must be a single-line amendment ID or path of at most ${AMENDMENT_REFERENCE_MAX_LENGTH} characters without brackets or semicolons`,
      { from, to }
    );
  }
  return amendment;
}

/** History note of an admitted reopening, mirroring `write_status.sh`. */
function reopenHistoryNote(decision: AmendmentReopenDecision, approvalSha: string | undefined): string {
  return [
    'reopened from ISSUED',
    `amendment: ${decision.amendmentId} (${decision.group3Snapshot})`,
    `action: ${decision.registerPath} ActionSeq ${decision.actionSeq || '?'} ${decision.actionType}`,
    `register SHA-256: ${decision.registerSha256}`,
    `approval SHA: ${approvalSha ?? ''}`
  ].join('; ');
}

function mergeTransitionMetadata(
  to: LifecycleState,
  options: LifecycleTransitionOptions,
  approvalSha: string | undefined,
  normalizedActor: string
): Record<string, string> | undefined {
  const metadata: Record<string, string> = { ...(options.metadata ?? {}) };
  for (const key of Object.keys(metadata)) {
    const label = key.toLowerCase().replace(/[^a-z0-9]/g, '');
    // Approval SHA fields are gate evidence: only the transition sets them, from
    // a validated approvalSha on the gate that records it.
    if (APPROVAL_SHA_FIELD_LABELS.has(label)) {
      throw new LifecycleTransitionError(
        'INVALID_METADATA',
        `Status field '${key}' is set only by the transition's approvalSha`,
        { key }
      );
    }
    // Authorization and accepted-basis fields are gate evidence a human records.
    if (HUMAN_ONLY_FIELD_LABELS.has(label) && normalizedActor !== 'HUMAN') {
      throw new LifecycleTransitionError(
        'INVALID_METADATA',
        `Status field '${key}' is gate evidence; only a HUMAN-actor transition may set it`,
        { key }
      );
    }
  }
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

interface ValidatedTransition {
  from: LifecycleState;
  to: LifecycleState;
  rule: TransitionRule;
  actor: string;
  approvalSha: string | undefined;
  ruling: string | undefined;
  amendment: string | undefined;
  metadata: Record<string, string> | undefined;
}

/**
 * Checks everything about a transition except the amendment record: the state
 * table, actor, approval SHA, ruling and amendment references, and metadata.
 */
function validateLifecycleTransition(
  currentStatusContent: string,
  targetStateInput: string,
  actorInput: string,
  options: LifecycleTransitionOptions
): ValidatedTransition {
  const parsed = parseStatusDocument(currentStatusContent);
  const from = parsed.currentState;

  let to: LifecycleState;
  try {
    to = parseLifecycleState(targetStateInput);
  } catch (error) {
    throw new LifecycleTransitionError('INVALID_STATE', 'Target state is invalid', { error });
  }

  const rule = findTransitionRule(from, to);
  // A reopening without an amendment stays a refused backward move.
  if ((!rule || (rule.amendmentReopen && !options.amendment?.trim())) && isBackwardTransition(from, to)) {
    throw new LifecycleTransitionError(
      'BACKWARD_TRANSITION',
      from === 'ISSUED'
        ? `Backward transitions are not allowed (${from} -> ${to}) without an amendment; ISSUED changes use the governed scope-change process, and reopening ISSUED -> IN_PROGRESS needs an accepted amendment`
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

  // Record the actor on one line: whitespace runs collapse to a single space.
  const actor = actorInput.trim().replace(/\s+/g, ' ') || normalizedActor;
  const approvalSha = parseApprovalShaForTransition(rule, options);
  const ruling = parseRulingReference(rule, options);
  const amendment = parseAmendmentReference(rule, options);
  const metadata = mergeTransitionMetadata(to, options, approvalSha, normalizedActor);
  return { from, to, rule, actor, approvalSha, ruling, amendment, metadata };
}

const AMENDMENT_ID_PATTERN = /^SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+$/u;
const AMENDMENT_FOLDER_PATTERN = /^(SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+)_/u;
const DELIVERABLE_ID_IN_TEXT = /\bDEL-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)+/;
// The reopening marker the amendment check reads (AMENDMENT_ALREADY_USED).
const REOPENING_MARKER = /reopened from ISSUED; amendment: (SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+)(?=[\s(;\]]|$)/gmu;

/**
 * The amendment ID a reference names: the ID itself, or the `SCA-..._` prefix
 * of the last path component that carries one (a snapshot or decision folder).
 */
function requestedAmendmentId(reference: string): string | undefined {
  const value = reference.trim();
  if (AMENDMENT_ID_PATTERN.test(value)) {
    return value;
  }
  const components = value.split(/[\\/]+/).filter(Boolean).reverse();
  for (const component of components) {
    const match = AMENDMENT_FOLDER_PATTERN.exec(component);
    if (match) {
      return match[1];
    }
  }
  return undefined;
}

/** Reopening markers by amendment ID, counted. */
function reopeningMarkers(content: string): Map<string, number> {
  const counts = new Map<string, number>();
  for (const match of content.matchAll(REOPENING_MARKER)) {
    counts.set(match[1], (counts.get(match[1]) ?? 0) + 1);
  }
  return counts;
}

export function applyLifecycleTransition(
  currentStatusContent: string,
  targetStateInput: string,
  actorInput: string,
  options: LifecycleTransitionOptions = {},
  context: LifecycleTransitionContext = {}
): LifecycleTransitionResult {
  const { from, to, rule, actor, approvalSha, ruling, amendment, metadata } =
    validateLifecycleTransition(currentStatusContent, targetStateInput, actorInput, options);

  let notes = rulingHistoryNote(rule, ruling, approvalSha);
  if (rule.amendmentReopen) {
    const decision = context.amendmentDecision;
    if (!decision) {
      throw new LifecycleTransitionError(
        'AMENDMENT_NOT_ADMITTED',
        `Reopening ${from} -> ${to} requires the amendment record check, which did not run`,
        { from, to, amendment }
      );
    }
    if (!decision.admitted || decision.code !== 'ADMITTED') {
      throw new LifecycleTransitionError(
        'AMENDMENT_NOT_ADMITTED',
        `${decision.code}: ${decision.reason}`,
        { from, to, amendment, refusalCode: decision.code }
      );
    }
    // The decision must be for this request: the amendment it names and the
    // deliverable this status file belongs to.
    const expectedAmendment = amendment !== undefined ? requestedAmendmentId(amendment) : undefined;
    const expectedDeliverable =
      context.deliverableId ?? DELIVERABLE_ID_IN_TEXT.exec(parseStatusDocument(currentStatusContent).title)?.[0];
    if (
      expectedAmendment === undefined ||
      decision.amendmentId !== expectedAmendment ||
      expectedDeliverable === undefined ||
      decision.deliverableId !== expectedDeliverable
    ) {
      throw new LifecycleTransitionError(
        'AMENDMENT_NOT_ADMITTED',
        `The amendment decision (${decision.amendmentId || '?'} for ${decision.deliverableId || '?'}) does not match ` +
          `the request (${expectedAmendment ?? '?'} for ${expectedDeliverable ?? '?'})`,
        { from, to, amendment }
      );
    }
    notes = reopenHistoryNote(decision, approvalSha);
  }

  let updated: ReturnType<typeof updateStatusDocument>;
  try {
    updated = updateStatusDocument(currentStatusContent, {
      targetState: to,
      actor,
      date: options.date,
      metadata,
      // The reversal withdraws the check, so its approval SHA no longer describes
      // the current state; the history line keeps the record.
      removeFields: rule.rulingReversal ? [CHECKING_APPROVAL_SHA_FIELD] : undefined,
      notes
    });
  } catch (error) {
    if (error instanceof StatusWriteError) {
      throw new LifecycleTransitionError('INVALID_METADATA', error.message, error.details);
    }
    throw error;
  }

  // Safety net: a transition never loses a recorded reopening, which the
  // amendment check relies on to refuse a second reopening (AMENDMENT_ALREADY_USED).
  const before = reopeningMarkers(currentStatusContent);
  const after = reopeningMarkers(updated.content);
  for (const [amendmentId, count] of before) {
    if ((after.get(amendmentId) ?? 0) < count) {
      throw new LifecycleTransitionError(
        'HISTORY_NOT_PRESERVED',
        `The transition would drop the recorded reopening under ${amendmentId} from _STATUS.md`,
        { from, to, amendmentId }
      );
    }
  }

  return {
    from,
    to,
    actor,
    content: updated.content
  };
}

/**
 * Applies a transition to a `_STATUS.md` file. A reopening (`ISSUED ->
 * IN_PROGRESS`) first passes every other check, then runs the amendment check
 * on the deliverable folder inside `context.projectRoot`.
 */
export async function transitionStatusFile(
  statusFilePath: string,
  targetStateInput: string,
  actorInput: string,
  options: LifecycleTransitionOptions = {},
  context: LifecycleTransitionFileContext = {}
): Promise<LifecycleTransitionResult> {
  const existingContent = await readFile(statusFilePath, 'utf8');
  const deliverableFolder = path.dirname(statusFilePath);
  const validated = validateLifecycleTransition(existingContent, targetStateInput, actorInput, options);
  let amendmentDecision: AmendmentReopenDecision | undefined;
  if (validated.amendment !== undefined) {
    if (!context.projectRoot) {
      throw new LifecycleTransitionError(
        'AMENDMENT_CHECK_ERROR',
        'Reopening needs the project root to check the amendment record',
        { amendment: validated.amendment }
      );
    }
    try {
      amendmentDecision = await checkAmendmentForReopen({
        workingRoot: context.projectRoot,
        deliverablePath: deliverableFolder,
        amendment: validated.amendment,
        // A reopening already recorded under this amendment is refused
        // (AMENDMENT_ALREADY_USED).
        statusText: existingContent
      });
    } catch (error) {
      if (error instanceof AmendmentReopenUsageError) {
        throw new LifecycleTransitionError(
          'AMENDMENT_CHECK_ERROR',
          `The amendment check could not decide: ${error.message}`,
          { amendment: validated.amendment }
        );
      }
      throw error;
    }
  }
  let deliverableId: string | undefined;
  if (amendmentDecision !== undefined) {
    // The checker names the deliverable from its real folder name.
    let folderName = path.basename(deliverableFolder);
    try {
      folderName = path.basename(await realpath(deliverableFolder));
    } catch {
      // Keep the lexical name; a mismatch is refused below.
    }
    deliverableId = folderName.split('_')[0];
  }
  // The amendment check runs without a lock: a concurrent write to _STATUS.md
  // during it can be overwritten (App SPEC §4.3 known limit).
  const result = applyLifecycleTransition(
    existingContent,
    targetStateInput,
    actorInput,
    options,
    { amendmentDecision, deliverableId }
  );
  await writeTextFileAtomically(statusFilePath, result.content);
  return result;
}
