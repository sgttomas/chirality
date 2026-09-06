import { readdir } from "node:fs/promises";
import { randomUUID } from "node:crypto";
import { join, relative, isAbsolute, resolve, sep } from "node:path";
import { isIP } from "node:net";
import { RuntimeError, type WorkerContinuity, type HostedEngineConsentPort } from "@chirality/runtime-contracts";
import { assertContinuity, sameContinuity, privateDirectory, privateRead, publishPrivate, recordKey } from "./hosted-consent.js";

export interface ApprovalBinding extends WorkerContinuity { sessionId: string; turnId: string; workerGeneration: string; scopeDigest?: string }
export interface NetworkApprovalContext { host: string; protocol: string }
export interface ApprovalDecisionInput { decision: "allow" | "deny" | "acceptForSession"; approvedBy: string; explicitUserAct: true }
export interface ApprovalRequest {
  requestId: string; binding: ApprovalBinding; networkApprovalContext: NetworkApprovalContext;
  requestedBy: string; requestedAt: string; consentDigest: string; caveat: string;
}
export interface ApprovalDecision extends ApprovalDecisionInput { requestId: string; requestDigest: string; decidedAt: string }
export interface ApprovalRecord { request: ApprovalRequest; decision?: ApprovalDecision; resolution?: { requestId: string; requestDigest: string; resolvedBy: string; resolvedAt: string; reason: "provider-resolved" } }
const forbidden = (message: string) => new RuntimeError("FORBIDDEN", message, 403);
const invalid = (message: string) => new RuntimeError("INVALID_REQUEST", message);
const text = (value: unknown): value is string => typeof value === "string" && value.trim().length > 0 && value.length <= 512 && !/[\x00-\x1f\x7f]/.test(value);
export function validateNetworkApprovalContext(value: unknown): NetworkApprovalContext {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw invalid("networkApprovalContext requires host and protocol");
  const obj = value as Record<string, unknown>;
  if (Object.keys(obj).some(key => key !== "host" && key !== "protocol") || !text(obj.host) || !text(obj.protocol)) throw invalid("Unknown or invalid network approval fields");
  const host = obj.host;
  const ip = host.startsWith("[") && host.endsWith("]") ? host.slice(1, -1) : host;
  if ((!isIP(ip) && !(host.length <= 253 && host.split(".").every(label => /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i.test(label)))) || !(/^[a-z][a-z0-9+.-]{0,31}$/.test(obj.protocol) || ["socks5Tcp", "socks5Udp"].includes(obj.protocol))) throw invalid("Destination must contain only a hostname or IP and protocol, without URL paths or credentials");
  return { host, protocol: obj.protocol };
}
function bindingEqual(a: ApprovalBinding, b: ApprovalBinding): boolean {
  return sameContinuity(a, b) && a.sessionId === b.sessionId && a.turnId === b.turnId && a.workerGeneration === b.workerGeneration && a.scopeDigest === b.scopeDigest;
}
/** Durable runtime authorization evidence, not a vendor network enforcement mechanism. */
export class ApprovalStore {
  constructor(private readonly options: { canonicalRoot: string; storageRoot: string; consent: HostedEngineConsentPort; isLive: (binding: ApprovalBinding) => boolean | Promise<boolean> }) {}
  private async ready(binding: ApprovalBinding): Promise<void> {
    await assertContinuity(binding);
    if (binding.canonicalRoot !== this.options.canonicalRoot || ![binding.sessionId, binding.turnId, binding.workerGeneration].every(text)) throw forbidden("Invalid approval binding");
    if (binding.scopeDigest !== undefined && !/^[a-f0-9]{64}$/.test(binding.scopeDigest)) throw forbidden("Invalid approval scope digest");
    const rel = relative(this.options.canonicalRoot, this.options.storageRoot);
    if (!isAbsolute(this.options.storageRoot) || resolve(this.options.storageRoot) !== this.options.storageRoot || !rel || (rel !== ".." && !rel.startsWith(`..${sep}`) && !isAbsolute(rel))) throw forbidden("Approval control storage must be private and outside the worker canonical root");
    if (typeof this.options.isLive !== "function" || !await this.options.isLive(binding)) throw forbidden("Approval binding is not a live worker turn");
    await privateDirectory(this.options.storageRoot);
    const marker = join(this.options.storageRoot, "chirality-approval-root.json");
    await publishPrivate(marker, { canonicalRoot: this.options.canonicalRoot }, true);
    if ((await privateRead<{ canonicalRoot: string }>(marker))?.canonicalRoot !== this.options.canonicalRoot) throw forbidden("Approval control storage is bound to another root");
  }
  private path(requestId: string, kind: "request" | "decision" | "resolution"): string {
    if (typeof requestId !== "string" || !/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(requestId)) throw invalid("Unknown approval request ID");
    return join(this.options.storageRoot, `${requestId}.${kind}.json`);
  }
  async request(binding: ApprovalBinding, context: NetworkApprovalContext, requestedBy: string): Promise<ApprovalRequest> {
    await this.ready(binding);
    if (!text(requestedBy)) throw invalid("Approval request requires attribution");
    const networkApprovalContext = validateNetworkApprovalContext(context);
    const consent = await this.options.consent.read(binding);
    const request: ApprovalRequest = { requestId: randomUUID(), binding: { canonicalRoot: binding.canonicalRoot, cwd: binding.cwd, accountId: binding.accountId, accountEpoch: binding.accountEpoch, policyDigest: binding.policyDigest, sessionId: binding.sessionId, turnId: binding.turnId, workerGeneration: binding.workerGeneration, ...(binding.scopeDigest ? { scopeDigest: binding.scopeDigest } : {}) }, networkApprovalContext, requestedBy, requestedAt: new Date().toISOString(), consentDigest: recordKey(consent ?? null), caveat: "A grant may unblock queued requests to the same destination. acceptForSession requires an explicit user act. This record does not enforce the vendor network boundary." };
    await this.ready(binding);
    if (!await publishPrivate(this.path(request.requestId, "request"), request, true)) throw new RuntimeError("INTERNAL_FAILURE", "Approval request ID collision", 500);
    return request;
  }
  async read(requestId: string, binding: ApprovalBinding): Promise<ApprovalRecord> {
    await this.ready(binding);
    const request = await privateRead<ApprovalRequest>(this.path(requestId, "request"));
    if (!request || request.requestId !== requestId || !request.binding || !bindingEqual(request.binding, binding) || !text(request.requestedBy)) throw forbidden("Approval request is unknown or belongs to another binding");
    validateNetworkApprovalContext(request.networkApprovalContext);
    const decision = await privateRead<ApprovalDecision>(this.path(requestId, "decision"));
    if (decision && (decision.requestId !== requestId || decision.requestDigest !== recordKey(request) || !["allow", "deny", "acceptForSession"].includes(decision.decision) || decision.explicitUserAct !== true || !text(decision.approvedBy))) throw forbidden("Invalid approval decision evidence");
    const resolution = await privateRead<NonNullable<ApprovalRecord["resolution"]>>(this.path(requestId, "resolution"));
    if (resolution && (resolution.requestId !== requestId || resolution.requestDigest !== recordKey(request) || !text(resolution.resolvedBy) || resolution.reason !== "provider-resolved")) throw forbidden("Invalid approval resolution evidence");
    return { request, ...(decision ? { decision } : {}), ...(resolution ? { resolution } : {}) };
  }
  async listPending(binding: ApprovalBinding): Promise<ApprovalRequest[]> {
    await this.ready(binding);
    const result: ApprovalRequest[] = [];
    for (const name of await readdir(this.options.storageRoot)) {
      if (!name.endsWith(".request.json")) continue;
      const id = name.slice(0, -".request.json".length);
      const request = await privateRead<ApprovalRequest>(this.path(id, "request"));
      if (!request?.binding || !bindingEqual(request.binding, binding)) continue;
      const record = await this.read(id, binding);
      if (!record.decision && !record.resolution) result.push(record.request);
    }
    await this.ready(binding);
    return result.sort((a, b) => a.requestedAt.localeCompare(b.requestedAt));
  }
  async decide(requestId: string, binding: ApprovalBinding, input: ApprovalDecisionInput): Promise<ApprovalRecord> {
    if (!input || !["allow", "deny", "acceptForSession"].includes(input.decision) || input.explicitUserAct !== true || !text(input.approvedBy) || Object.keys(input).some(key => !["decision", "approvedBy", "explicitUserAct"].includes(key))) throw invalid("Approval decision requires an attributed explicit user act");
    const { request, resolution } = await this.read(requestId, binding);
    if (resolution) throw forbidden("Approval request was resolved by provider");
    const consent = await this.options.consent.read(binding);
    if (input.decision !== "deny" && (!consent || consent.posture === "off" || recordKey(consent) !== request.consentDigest)) throw forbidden("Approval cannot override absent, off, or changed standing consent");
    const decision: ApprovalDecision = { decision: input.decision, approvedBy: input.approvedBy, explicitUserAct: true, requestId, requestDigest: recordKey(request), decidedAt: new Date().toISOString() };
    await this.ready(binding);
    if (!await publishPrivate(this.path(requestId, "decision"), decision, true)) {
      const prior = (await this.read(requestId, binding)).decision;
      if (!prior || prior.decision !== input.decision || prior.approvedBy !== input.approvedBy) throw forbidden("Approval already has an immutable conflicting decision");
    }
    return this.read(requestId, binding);
  }
  async resolve(requestId: string, binding: ApprovalBinding, resolvedBy: string): Promise<void> {
    if (!text(resolvedBy)) throw invalid("Approval resolution requires attribution");
    const { request } = await this.read(requestId, binding);
    await this.ready(binding);
    await publishPrivate(this.path(requestId, "resolution"), { requestId, requestDigest: recordKey(request), resolvedBy, resolvedAt: new Date().toISOString(), reason: "provider-resolved" }, true);
  }
  async authorize(requestId: string, binding: ApprovalBinding): Promise<boolean> {
    const { request, decision, resolution } = await this.read(requestId, binding);
    if (resolution) return false;
    const consent = await this.options.consent.read(binding);
    await this.ready(binding);
    if (!consent || !sameContinuity(consent.identity, binding) || !text(consent.approvedBy) || !Number.isFinite(Date.parse(consent.approvedAt)) || consent.posture === "off" || recordKey(consent) !== request.consentDigest || decision?.decision === "deny") return false;
    if (consent.posture === "on") return true;
    return consent.posture === "ask-per-destination" && (decision?.decision === "allow" || decision?.decision === "acceptForSession");
  }
}
