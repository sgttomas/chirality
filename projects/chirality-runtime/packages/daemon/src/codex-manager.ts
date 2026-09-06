import { createHash } from 'node:crypto';
import { RuntimeError, type RuntimeSessionRecord, type Agent1RunRequest, type UIEvent, type WorkerHandle } from '@chirality/runtime-contracts';
import type { Agent1ManagerRuntimePort, Agent1ManagerHooks } from '@chirality/runtime-core';
import type { CodexDynamicTool, CodexDynamicToolResult } from './codex-session.js';

export type ManagerMessage = { kind: 'callback'; callId: string; threadId: string; turnId: string; name: 'delegate_agent' | 'review'; args: Readonly<Record<string, unknown>> } | { kind: 'done'; text: string } | { kind: 'pending' };
export interface SupervisorManagerPort {
  startManager(workerId: string, input: string): Promise<WorkerHandle>;
  nextManager(workerId: string, generation: string): Promise<ManagerMessage>;
  replyManager(workerId: string, generation: string, input: string): Promise<void>;
  retire(workerId: string, generation: string): Promise<void>;
}
export const managerToolSchemas = Object.freeze({
  delegate_agent: { type: 'object', properties: { sealedBrief: { type: 'string', minLength: 1, maxLength: 32768 } }, required: ['sealedBrief'], additionalProperties: false },
  review: { type: 'object', properties: { childSessionId: { type: 'string', minLength: 1, maxLength: 128 }, decision: { type: 'string', enum: ['accepted', 'rejected'] }, rationale: { type: 'string', minLength: 1, maxLength: 8192 } }, required: ['childSessionId', 'decision', 'rationale'], additionalProperties: false }
});
/** Supervisor-owned bounded callback mailbox. No public input supplies tool declarations. */
export class ManagerMailbox {
  private pending?: { message: Extract<ManagerMessage, {kind:'callback'}>; resolve(value: CodexDynamicToolResult): void; reject(error: Error): void };
  private delivered = false;
  private wake?: () => void;
  private polling = false;
  private terminal?: { text?: string; error?: Error };
  readonly tools: readonly CodexDynamicTool[] = (['delegate_agent', 'review'] as const).map(name => ({
    name, description: name === 'delegate_agent' ? 'Execute the approved bounded Agent 2 delegation.' : 'Review the actual governed child return.', inputSchema: managerToolSchemas[name],
    handler: async (args, context) => {
      if (this.pending || this.terminal || context.signal.aborted) throw new Error('Manager callback unavailable');
      return await new Promise<CodexDynamicToolResult>((resolve, reject) => {
        const abort = () => { if (this.pending?.message.callId === context.callId) { this.pending = undefined; reject(new Error('Manager callback cancelled')); } };
        context.signal.addEventListener('abort', abort, { once: true });
        this.pending = { message: { kind: 'callback', callId: context.callId, threadId: context.threadId, turnId: context.turnId, name, args },
          resolve: value => { context.signal.removeEventListener('abort', abort); resolve(value); }, reject: error => { context.signal.removeEventListener('abort', abort); reject(error); } };
        this.delivered = false; this.wake?.();
      });
    }
  }));
  finish(text?: string, error?: Error): void { this.terminal = { text, error }; this.pending?.reject(error ?? new Error('Manager ended')); this.pending = undefined; this.wake?.(); }
  async next(): Promise<ManagerMessage> {
    if (this.polling) throw new Error('Concurrent manager poll');
    this.polling = true;
    let timer: ReturnType<typeof setTimeout> | undefined;
    try {
      if (!this.terminal && (!this.pending || this.delivered)) await new Promise<void>(resolve => { this.wake = resolve; timer = setTimeout(resolve, 1000); });
      if (this.terminal?.error) throw this.terminal.error;
      if (this.terminal) return { kind: 'done', text: this.terminal.text ?? '' };
      if (this.pending && !this.delivered) { this.delivered = true; return this.pending.message; }
      return { kind: 'pending' };
    } finally { clearTimeout(timer); this.wake = undefined; this.polling = false; }
  }
  reply(input: string): void {
    if (Buffer.byteLength(input) > 65536) throw new Error('Manager reply exceeds bound');
    const r = JSON.parse(input);
    const p = this.pending;
    if (!p || !this.delivered || !r || Object.keys(r).sort().join(',') !== 'callId,result,threadId,turnId' || r.callId !== p.message.callId || r.threadId !== p.message.threadId || r.turnId !== p.message.turnId || !r.result || typeof r.result.success !== 'boolean' || !Array.isArray(r.result.contentItems) || r.result.contentItems.length !== 1 || r.result.contentItems[0]?.type !== 'inputText' || typeof r.result.contentItems[0].text !== 'string' || Object.keys(r.result).sort().join(',') !== 'contentItems,success' || Object.keys(r.result.contentItems[0]).sort().join(',') !== 'text,type') throw new Error('Unknown or stale manager callback reply');
    this.pending = undefined; p.resolve(r.result);
  }
}
export class CodexAgent1ManagerPort implements Agent1ManagerRuntimePort {
  constructor(private readonly options: { channel: SupervisorManagerPort; loadInstructions(session: RuntimeSessionRecord, request: Agent1RunRequest): Promise<string>; callbackTimeoutMs?: number; approvals?: { register(session: RuntimeSessionRecord, handle: WorkerHandle, scopeDigest: string): Promise<() => Promise<void>> } }) {
    const timeout = options.callbackTimeoutMs ?? 120000;
    if (!Number.isSafeInteger(timeout) || timeout < 1 || timeout > 120000) throw new RuntimeError('INVALID_REQUEST', 'Invalid manager callback timeout');
  }
  async *execute(session: RuntimeSessionRecord, request: Agent1RunRequest, hooks: Agent1ManagerHooks, signal: AbortSignal): AsyncIterable<UIEvent> {
    if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(session.sessionId ?? '') || session.role !== 'agent1' || session.engineSelection.adapterId !== 'codex-app-server' || signal.aborted) throw new RuntimeError('ENGINE_UNAVAILABLE', 'Hosted Codex Agent 1 required', 503);
    const instructions = await this.options.loadInstructions(session, request);
    if (!instructions.trim()) throw new RuntimeError('INVALID_REQUEST', 'Manager instructions required');
    const handle = await this.options.channel.startManager(session.sessionId, JSON.stringify({ canonicalRoot: session.projectRoot, model: session.engineSelection.model, prompt: `${instructions}\n\nRole: Agent 1. role not mechanically enforced; evidence posture: instruction-asserted.\nUse delegate_agent for the approved local child and review for its actual return. Never represent a text claim as tool execution.\n\nApproved run:\n${JSON.stringify(request)}` }));
    let releaseApprovals: (() => Promise<void>) | undefined;
    try { releaseApprovals = await this.options.approvals?.register(session, handle, createHash('sha256').update(JSON.stringify({ sessionId: session.sessionId, projectId: session.projectId, root: session.projectRoot, model: session.engineSelection, role: session.role, request, instructions })).digest('hex')); }
    catch (error) { await this.options.channel.retire(handle.workerId, handle.generation); throw error; }
    let retirement: Promise<void> | undefined;
    const retire = () => retirement ??= this.options.channel.retire(handle.workerId, handle.generation);
    const abort = () => { void retire().catch(() => {}); };
    signal.addEventListener('abort', abort, { once: true });
    if (signal.aborted) abort();
    try {
      while (!signal.aborted) {
        const message = await this.options.channel.nextManager(handle.workerId, handle.generation);
        if (message.kind === 'pending') continue;
        if (message.kind === 'done') { yield { type: 'chat:complete', data: { text: message.text } }; return; }
        let result: CodexDynamicToolResult;
        let callbackFailure: unknown;
        let timer: ReturnType<typeof setTimeout> | undefined;
        let cancelCallback: (() => void) | undefined;
        try {
          if (signal.aborted) throw new Error('Interrupted');
          const callback = message.name === 'delegate_agent' ? hooks.delegate(message.args as {sealedBrief:string}) : hooks.review(message.args as {childSessionId:string;decision:'accepted'|'rejected';rationale:string});
          const value = await Promise.race([callback, new Promise<never>((_, reject) => {
            cancelCallback = () => reject(new RuntimeError('INTERRUPTED', 'Manager callback interrupted', 499));
            signal.addEventListener('abort', cancelCallback, { once: true });
            timer = setTimeout(() => reject(new RuntimeError('ENGINE_UNAVAILABLE', 'Manager callback timed out', 503)), this.options.callbackTimeoutMs ?? 120000);
            if (signal.aborted) cancelCallback();
          })]);
          result = { success: true, contentItems: [{ type: 'inputText', text: JSON.stringify(value ?? { reviewed: true }) }] };
        } catch (error) { callbackFailure = error; result = { success: false, contentItems: [{ type: 'inputText', text: 'Governed callback failed' }] }; }
        finally { clearTimeout(timer); if (cancelCallback) signal.removeEventListener('abort', cancelCallback); }
        if (signal.aborted) break;
        await this.options.channel.replyManager(handle.workerId, handle.generation, JSON.stringify({ callId: message.callId, threadId: message.threadId, turnId: message.turnId, result }));
        if (callbackFailure) throw callbackFailure;
      }
      throw new RuntimeError('INTERRUPTED', 'Manager interrupted', 499);
    } finally { signal.removeEventListener('abort', abort); try { await releaseApprovals?.(); } finally { await retire(); } }
  }
}
export function createSupervisorAgent1ManagerPort(options: ConstructorParameters<typeof CodexAgent1ManagerPort>[0]): Agent1ManagerRuntimePort { return new CodexAgent1ManagerPort(options); }
