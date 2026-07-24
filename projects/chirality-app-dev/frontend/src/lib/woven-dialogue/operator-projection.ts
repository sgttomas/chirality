import type { SessionRecord } from '@chirality/harness-contract/types';
import type {
  OperatorSessionProjection,
  ProjectionCurrency,
  ProjectionDiagnostic
} from './contracts';

type SessionSource = SessionRecord & Record<string, unknown>;

export type OperatorProjectionOptions = {
  observedAt: string;
  currencyBySessionId?: Readonly<Record<string, ProjectionCurrency>>;
};

export type OperatorProjectionResult = {
  sessions: OperatorSessionProjection[];
  diagnostics: ProjectionDiagnostic[];
};

const RUNTIME_STATUSES = new Set([
  'idle',
  'running',
  'completed',
  'failed',
  'interrupted'
] as const);

function readString(value: unknown): string | undefined {
  return typeof value === 'string' && value.trim().length > 0 ? value : undefined;
}

function recordedRole(
  source: SessionSource,
  diagnostics: ProjectionDiagnostic[],
  sourceReference: string
): OperatorSessionProjection['role'] {
  const explicitRole =
    source.role === 'agent0' || source.role === 'agent1' || source.role === 'agent2'
      ? source.role
      : undefined;
  const agentTypeRole =
    source.agentType === 0
      ? 'agent0'
      : source.agentType === 1
        ? 'agent1'
        : source.agentType === 2
          ? 'agent2'
          : undefined;

  if (explicitRole && agentTypeRole && explicitRole !== agentTypeRole) {
    diagnostics.push({
      code: 'CONFLICTING_RECORDED_ROLE',
      message: 'Recorded role and agentType disagree; role is not projected.',
      sourceReference
    });
    return undefined;
  }

  return explicitRole ?? agentTypeRole;
}

function runtimeStatus(source: SessionSource): OperatorSessionProjection['runtimeStatus'] {
  return typeof source.status === 'string' &&
    RUNTIME_STATUSES.has(
      source.status as NonNullable<OperatorSessionProjection['runtimeStatus']>
    )
    ? (source.status as OperatorSessionProjection['runtimeStatus'])
    : undefined;
}

function projectionSignature(source: SessionSource): string {
  return JSON.stringify({
    sessionId: source.sessionId,
    parentSessionId: source.parentSessionId,
    role: source.role,
    agentType: source.agentType,
    status: source.status,
    engineSelection: source.engineSelection,
    model: source.model,
    residencyEpoch: source.residencyEpoch,
    outputArtifact: source.outputArtifact,
    approvalRef: source.approvalRef
  });
}

function projectOne(
  session: SessionRecord,
  availableSessionIds: ReadonlySet<string>,
  options: OperatorProjectionOptions,
  conflictDiagnostic?: ProjectionDiagnostic
): OperatorSessionProjection {
  const source = session as unknown as SessionSource;
  const sourceReference = `session:${session.sessionId}`;
  const diagnostics: ProjectionDiagnostic[] = [];
  if (conflictDiagnostic) {
    diagnostics.push(conflictDiagnostic);
  }

  const role = recordedRole(source, diagnostics, sourceReference);
  const parentSessionId = readString(source.parentSessionId);
  const engineSelection =
    source.engineSelection && typeof source.engineSelection === 'object'
      ? source.engineSelection
      : undefined;
  const selectedCurrency = options.currencyBySessionId?.[session.sessionId] ?? 'UNKNOWN';
  const hasConflict =
    Boolean(conflictDiagnostic) ||
    diagnostics.some((diagnostic) => diagnostic.code.startsWith('CONFLICTING_'));
  const persona = readString(source.persona);
  const status = runtimeStatus(source);
  const adapterId = readString(engineSelection?.adapterId);
  const providerId = readString(engineSelection?.providerId);
  const model = readString(engineSelection?.model) ?? readString(source.model);
  const residencyEpoch = readString(source.residencyEpoch);
  const outputArtifactReference = readString(source.outputArtifact);
  const approvalEvidenceReference = readString(source.approvalRef);

  return {
    projectionId: `operator-session:${session.sessionId}`,
    sourceReference,
    sessionId: session.sessionId,
    observedAt: options.observedAt,
    currency: hasConflict ? 'CONFLICTING' : selectedCurrency,
    ...(persona ? { persona } : {}),
    ...(role ? { role } : {}),
    ...(status ? { runtimeStatus: status } : {}),
    ...(adapterId ? { adapterId } : {}),
    ...(providerId ? { providerId } : {}),
    ...(model ? { model } : {}),
    ...(residencyEpoch ? { residencyEpoch } : {}),
    parentage: parentSessionId
      ? {
          state: 'RECORDED',
          parentSessionId,
          parentAvailable: availableSessionIds.has(parentSessionId)
        }
      : { state: 'NOT_RECORDED' },
    ...(outputArtifactReference ? { outputArtifactReference } : {}),
    ...(approvalEvidenceReference ? { approvalEvidenceReference } : {}),
    diagnostics
  };
}

/**
 * Build a disposable, provider-neutral view over exact canonical session
 * fields. No relationship, role, model, status, approval, or currency is
 * derived from persona, prose, timestamp order, or visual placement.
 */
export function buildOperatorSessionProjection(
  sourceSessions: readonly SessionRecord[],
  options: OperatorProjectionOptions
): OperatorProjectionResult {
  const grouped = new Map<string, SessionRecord[]>();
  for (const session of sourceSessions) {
    const records = grouped.get(session.sessionId) ?? [];
    records.push(session);
    grouped.set(session.sessionId, records);
  }

  const availableSessionIds = new Set(grouped.keys());
  const diagnostics: ProjectionDiagnostic[] = [];
  const sessions: OperatorSessionProjection[] = [];

  for (const [sessionId, records] of grouped) {
    const first = records[0];
    if (!first) {
      continue;
    }
    const conflicting =
      new Set(
        records.map((record) =>
          projectionSignature(record as unknown as SessionSource)
        )
      ).size > 1;
    const conflictDiagnostic = conflicting
      ? {
          code: 'CONFLICTING_SESSION_RECORDS',
          message: `Canonical sources disagree for session ${sessionId}; the first record is shown without resolving the conflict.`,
          sourceReference: `session:${sessionId}`
        }
      : undefined;

    if (conflictDiagnostic) {
      diagnostics.push(conflictDiagnostic);
    }
    sessions.push(projectOne(first, availableSessionIds, options, conflictDiagnostic));
  }

  return { sessions, diagnostics };
}

export function projectOperatorSession(
  session: SessionRecord,
  availableSessionIds: ReadonlySet<string>,
  options: OperatorProjectionOptions
): OperatorSessionProjection {
  return projectOne(session, availableSessionIds, options);
}
