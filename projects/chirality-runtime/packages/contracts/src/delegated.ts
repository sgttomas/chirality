import { RuntimeError } from "./errors.js";
import type { HarnessEventV2, EventAttributionV2 } from "./v2-events.js";
/** Additive runtime-owned v2 boundary; not a vendor wire protocol. */
export interface WorkerContinuity {
  canonicalRoot: string;
  accountId: string;
  accountEpoch: number;
  policyDigest: string;
  cwd: string;
}
export type CommandNetworkPosture = "off" | "ask-per-destination" | "on";
export interface HostedConsent {
  identity: WorkerContinuity;
  posture: CommandNetworkPosture;
  approvedBy: string;
  approvedAt: string;
}
export interface DestinationApproval {
  host: string;
  protocol: string;
  acceptForSession: boolean;
  explicitUserAct: boolean;
  approvedBy: string;
}
export interface HostedEngineConsentPort {
  read(identity: WorkerContinuity): Promise<HostedConsent | undefined>;
  grant(consent: HostedConsent): Promise<void>;
  authorizeDestination(identity: WorkerContinuity, approval: DestinationApproval): Promise<void>;
}
export interface WorkerHandle {
  workerId: string;
  generation: string;
  pid: number;
  state: "running" | "exited";
}
export interface WorkerResult {
  worker: WorkerHandle;
  exitCode: number | null;
  signal: string | null;
  threadId?: string;
  stdout: string;
  stderr: string;
}
/** Only the broker receives an instance; never expose token or socket to clients. */
export interface DelegatedHarnessProcessSupervisorPort {
  /** Host-only concrete adapter check, never a client-supplied containment assertion. */
  verifyHostedBoundary?(identity: WorkerContinuity): Promise<void>;
  acquire(workerId: string, input: string): Promise<WorkerHandle>;
  inventory(): Promise<readonly WorkerHandle[]>;
  reconnect(workerId: string, generation: string): Promise<WorkerHandle>;
  wait(workerId: string, generation: string): Promise<WorkerResult>;
  retire(workerId: string, generation: string): Promise<void>;
}
export interface WorkerTerminalRecord {
  turnId: string;
  workerId: string;
  generation: string;
  outcome: "completed" | "failed" | "interrupted";
  recordedAt: string;
}
export interface RetirementRecord {
  turnId: string;
  identity: WorkerContinuity;
  threadId?: string;
  rolePolicyDigest?: string;
  state: "prepared" | "committed" | "reconciliation-required";
  terminal?: WorkerTerminalRecord;
}
export interface WorkerRetirementCoordinatorPort {
  prepare(record: RetirementRecord): Promise<void>;
  associateThread?(turnId: string, threadId: string): Promise<void>;
  terminalize(terminal: WorkerTerminalRecord): Promise<WorkerTerminalRecord>;
  read(turnId: string): Promise<RetirementRecord | undefined>;
  reconcile(): Promise<readonly RetirementRecord[]>;
  restart(turnId: string, identity: WorkerContinuity, expectedRolePolicyDigest?: string): Promise<{ method: "thread/resume" | "thread/start"; threadId?: string }>;
}
export interface RuntimeCompatibilityIdentity {
  compatibilityIdentity: string;
  contractBasisSha256: string;
}
export interface DelegatedPreflight extends RuntimeCompatibilityIdentity {
  operationId: string;
  projectId: string;
  daemonId: string;
  nonce: string;
}
export type DelegatedRole = "untyped" | "agent0" | "agent1" | "agent2" | "task";
export type DelegatedInteractionMode = "chat" | "native-plan";
export type DelegatedAttachmentInput =
  | { type: "text"; text: string; source: "untrusted-document" }
  | { type: "localImage"; path: string; mimeType: "image/png" | "image/jpeg" | "image/gif" | "image/webp"; source: "untrusted-attachment" };
export interface DelegatedTurnRequest {
  requestedRole?: DelegatedRole;
  /** Runtime session identity is mandatory for native Plan turns. */
  sessionId?: string;
  interactionMode?: DelegatedInteractionMode;
  permissionMode?: "readOnly" | "ask" | "workspaceWrite" | "bypass";
  turnId: string;
  previousTurnId?: string;
  prompt: string;
  /** Resolved user attachments. They remain untrusted user input, never instruction context. */
  attachments?: readonly DelegatedAttachmentInput[];
  compatibility: RuntimeCompatibilityIdentity;
  preflight: DelegatedPreflight;
}
export interface DelegatedRoleEvidence {
  selectedRole: DelegatedRole;
  offeredRoles: DelegatedRole[];
  enforcementLabel: "role not mechanically enforced";
  evidencePosture: "instruction-asserted";
  policyDigest: string;
  actual: EventAttributionV2;
}
export interface DelegatedCapabilities {
  offeredRoles: DelegatedRole[];
  configuredPosture: CommandNetworkPosture;
  commandNetwork: { posture: CommandNetworkPosture; configured: boolean; executionSupported: boolean; label: string }[];
  approvalRecordsAvailable: boolean;
  approvalForwardingSupported: boolean;
}
export interface DelegatedApprovalDecisionRequest {
  turnId: string;
  workerGeneration: string;
  decision: "allow" | "deny" | "acceptForSession";
  approvedBy: string;
  explicitUserAct: true;
  compatibility: RuntimeCompatibilityIdentity;
  preflight: DelegatedPreflight;
}
export interface DelegatedTurnResponse {
  roleEvidence: DelegatedRoleEvidence;
  event: HarnessEventV2;
  terminal: WorkerTerminalRecord;
  output: string;
  providerThreadId?: string;
  evidenceClass: "controlled-worker" | "provider-observed";
}

/** Unavailable is the only qualified binding state in this increment. */
export interface HostedAccountBinding {
  schema: "chirality-hosted-account-binding/v1";
  state: "unavailable";
  reason: "canonical-identity-producer-unavailable";
}
export interface HostedManagedAuth {
  backend: "keyring";
  binding: HostedAccountBinding;
}
export interface HostedLoginStatus {
  schema: "chirality-hosted-login-status/v2";
  state: "pending" | "completed" | "failed";
  loginId?: string;
  /** Supplier presence only; never a principal or a readiness signal. */
  hasAccount?: boolean;
  evidenceClass: "exact-supply-login" | "controlled-fixture";
  binding: HostedAccountBinding;
  hostedReady: false;
}
export interface HostedBootstrapStatus {
  schema: "chirality-hosted-bootstrap-status/v1";
  projectId: string;
  ceremony: "consent-required" | "ready-to-start" | "pending" | "signed-in" | "failed" | "cancelled";
  admission: "unavailable" | "establishing" | "ready";
  canStartLogin: boolean;
}
export interface HostedProviderNetworkConsentRequest { consent: true }
export interface HostedBootstrapLoginStartResponse { loginId: string; authUrl: string }
export function validateHostedBootstrapStatus(value: unknown): HostedBootstrapStatus {
  const status = hostedRecord(value, ["schema", "projectId", "ceremony", "admission", "canStartLogin"]);
  if (status.schema !== "chirality-hosted-bootstrap-status/v1" || typeof status.projectId !== "string" || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(status.projectId)
    || !["consent-required", "ready-to-start", "pending", "signed-in", "failed", "cancelled"].includes(String(status.ceremony))
    || !["unavailable", "establishing", "ready"].includes(String(status.admission)) || typeof status.canStartLogin !== "boolean"
    || status.canStartLogin !== ["ready-to-start", "failed", "cancelled"].includes(String(status.ceremony))
    || (status.admission === "ready" && status.ceremony !== "signed-in")) {
    throw new RuntimeError("INVALID_REQUEST", "Invalid hosted bootstrap status");
  }
  return status as unknown as HostedBootstrapStatus;
}
function hostedRecord(value: unknown, allowed: readonly string[]): Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)
    || Object.keys(value).some(key => !allowed.includes(key))) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted status/configuration fields");
  return value as Record<string, unknown>;
}
export function validateHostedAccountBinding(value: unknown): HostedAccountBinding {
  const binding = hostedRecord(value, ["schema", "state", "reason"]);
  if (binding.schema !== "chirality-hosted-account-binding/v1" || binding.state !== "unavailable"
    || binding.reason !== "canonical-identity-producer-unavailable") throw new RuntimeError("INVALID_REQUEST", "Invalid unavailable hosted account binding");
  return { schema: "chirality-hosted-account-binding/v1", state: "unavailable", reason: "canonical-identity-producer-unavailable" };
}
export function validateHostedManagedAuth(value: unknown): HostedManagedAuth {
  const auth = hostedRecord(value, ["backend", "binding"]);
  if (auth.backend !== "keyring") throw new RuntimeError("INVALID_REQUEST", "Hosted managed authentication requires explicit keyring configuration");
  return { backend: "keyring", binding: validateHostedAccountBinding(auth.binding) };
}
export function validateHostedLoginStatus(value: unknown): HostedLoginStatus {
  const status = hostedRecord(value, ["schema", "state", "loginId", "hasAccount", "evidenceClass", "binding", "hostedReady"]);
  if (status.schema !== "chirality-hosted-login-status/v2" || !["pending", "completed", "failed"].includes(status.state as string)
    || !["exact-supply-login", "controlled-fixture"].includes(status.evidenceClass as string) || status.hostedReady !== false
    || ("loginId" in status && (typeof status.loginId !== "string" || status.loginId.length > 512))
    || ("hasAccount" in status && typeof status.hasAccount !== "boolean")) throw new RuntimeError("INVALID_REQUEST", "Invalid hosted login status");
  return { schema: "chirality-hosted-login-status/v2", state: status.state as HostedLoginStatus["state"],
    evidenceClass: status.evidenceClass as HostedLoginStatus["evidenceClass"], binding: validateHostedAccountBinding(status.binding), hostedReady: false,
    ...("loginId" in status ? { loginId: status.loginId as string } : {}), ...("hasAccount" in status ? { hasAccount: status.hasAccount as boolean } : {}) };
}

/** Private daemon/supervisor approval capability, never a public request-mint API. */
export type NetworkApprovalChoice = "allow" | "deny" | "acceptForSession";
export interface NetworkApprovalPrompt {
  approvalId: string;
  threadId: string;
  turnId: string;
  networkApprovalContext: { host: string; protocol: string };
  availableDecisions: NetworkApprovalChoice[];
}
export interface SupervisorNetworkApprovalPort {
  pendingNetworkApprovals(workerId: string, generation: string): Promise<readonly NetworkApprovalPrompt[]>;
  replyNetworkApproval(workerId: string, generation: string, approvalId: string, decision: NetworkApprovalChoice): Promise<{ sent: true }>;
}

/** Trusted supervisor projection of an authoritative completed Codex plan item. */
export interface NativePlanTransportEvent {
  projectId: string;
  sessionId: string;
  clientTurnId: string;
  providerThreadId: string;
  providerTurnId: string;
  eventId: string;
  occurredAt: string;
  plan: unknown;
}
export interface NativePlanClarificationQuestion {
  id: string;
  header: string;
  question: string;
  options: readonly { label: string; description: string }[];
  isOther: boolean;
  isSecret: boolean;
}
export interface NativePlanClarificationPrompt {
  projectId: string;
  sessionId: string;
  clientTurnId: string;
  providerThreadId: string;
  providerTurnId: string;
  requestId: string | number;
  itemId: string;
  questions: readonly NativePlanClarificationQuestion[];
  isBlocking: boolean;
  autoResolutionMs: number | null;
}
export type NativePlanClarificationAnswers = Readonly<Record<string, { answers: readonly string[] }>>;
export interface SupervisorNativePlanPort {
  drainNativePlanEvents(workerId: string, generation: string): Promise<readonly NativePlanTransportEvent[]>;
  pendingNativePlanClarifications(workerId: string, generation: string): Promise<readonly NativePlanClarificationPrompt[]>;
  replyNativePlanClarification(workerId: string, generation: string, requestId: string | number, answers: NativePlanClarificationAnswers): Promise<{ sent: true }>;
}

export interface RuntimeToolCallbackDeclaration {
  name: string;
  description: string;
  inputSchema: Readonly<Record<string, unknown>>;
}
export type RuntimeToolCallbackMessage =
  | { kind: "pending" }
  | { kind: "callback"; callId: string; threadId: string; turnId: string; name: string; args: Readonly<Record<string, unknown>>; nativeChild?: Readonly<{ associationId: string; supplierGeneration: string; rootThreadId: string; rootTurnId: string; parentThreadId: string; parentTurnId: string; selectedRole: import("./engine.js").NativeChildSelectedRole; inheritedToolsDigest: string }> };
export interface RuntimeToolCallbackResult {
  success: boolean;
  contentItems: readonly { type: "inputText"; text: string }[];
}
/** Private daemon-to-supervisor bridge. Tool implementations never cross it. */
export interface SupervisorRuntimeToolPort {
  acquireWithRuntimeTools(workerId: string, input: string, tools: readonly RuntimeToolCallbackDeclaration[], inheritableTools?: readonly RuntimeToolCallbackDeclaration[]): Promise<WorkerHandle>;
  nextRuntimeToolCallback(workerId: string, generation: string): Promise<RuntimeToolCallbackMessage>;
  replyRuntimeToolCallback(workerId: string, generation: string, message: Extract<RuntimeToolCallbackMessage, { kind: "callback" }>, result: RuntimeToolCallbackResult): Promise<void>;
}
export type DelegatedTurnProgressEvent =
  | { type: "started"; providerThreadId: string; providerTurnId: string }
  | { type: "text"; providerThreadId: string; providerTurnId: string; text: string };
export interface SupervisorTurnProgressPort {
  drainTurnProgress(workerId: string, generation: string): Promise<readonly DelegatedTurnProgressEvent[]>;
}

export interface SupervisorApprovalDescription {
  identity: WorkerContinuity;
  model: string;
  commandNetworkPosture: CommandNetworkPosture;
  compatibility: RuntimeCompatibilityIdentity;
  consent?: HostedConsent;
}
export interface SupervisorApprovalDescriptionPort {
  describeApprovalScope(workerId?: string, generation?: string): Promise<SupervisorApprovalDescription>;
}
