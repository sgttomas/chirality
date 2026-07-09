/**
 * AgentEnginePort (D-PEC-17): the config-selected seam between the sidecar and
 * whatever produces agent turns. The deterministic stub is the v1 default; the
 * SDK engine is a key-droppable loader (engine/sdk.ts). The shape deliberately
 * mirrors app-dev harness-contract's agent-engine-port.ts (subject-discriminated
 * port, event stream) WITHOUT importing it — no cross-project dependency in v1;
 * convergence on a shared package is a future bridge-lane item. v1 is
 * request/response; the event array is the same schema a later SSE upgrade
 * would stream.
 */

export type EngineSubject = 'stub' | 'sdk'

/**
 * Egress class keys the D-T0-20 O-B enumeration clamp in acts.ts: 'none' (stub —
 * no external-model session exists, nothing routes to any provider) vs
 * 'model-provider' (sdk). Convention of record (GOV NIT-3): any future engine
 * subject whose egress class is undeclared or unknown defaults to
 * 'model-provider' — the conservative bound.
 */
export type EgressClass = 'none' | 'model-provider'

export interface ScreenContextRecord {
  recordType: string
  ref: string
  id: number
}

/**
 * One prior turn of the conversation, flattened to text by the client
 * (D-PEC-21 item 2). The transcript rides the REQUEST — the sidecar stores
 * nothing between requests; a request without history is a fresh start.
 */
export interface HistoryEntry {
  who: 'you' | 'agent'
  text: string
}

export interface AgentTurnInput {
  pid: number
  message: string
  /** screen-context grounding: route + visible record ids only (rider 5) */
  context?: {
    route: string
    records: ScreenContextRecord[]
  }
  /** CSV/TSV/plain tabular text only (D-PEC-35 O-A), ≤ 5 MiB of UTF-8 text */
  attachment?: {
    name: string
    text: string
  }
  /** prior turns, newest last (D-PEC-21: ≤ 40 entries, each ≤ 8 KiB — http.ts validates) */
  history?: HistoryEntry[]
}

export type AgentEvent =
  | { type: 'agent:reply'; text: string }
  | { type: 'act:result'; act: string; ok: boolean; summary: string; payload?: unknown }
  | { type: 'act:refused'; act: string; reason: string }
  | { type: 'turn:error'; code: string; message: string }

/** What one act call produced; the engine formats but never invents (F-PEC-2). */
export type ActResult =
  | { kind: 'result'; act: string; ok: boolean; summary: string; payload?: unknown }
  | { kind: 'refused'; act: string; reason: string }

/**
 * The bounded act surface both engines drive (acts.ts). There is deliberately
 * no accept/apply/reject-of-others/force/approval-outcome act — the human-act
 * boundary is structural (rider 4).
 */
export interface BoundActs {
  /** the agent person's identity for WF-8 attribution lines; null when not logged in */
  whoami(): { personId: number; name: string; email: string } | null
  proposeCsv(input: { csv: string; filename?: string; contract?: string; coverageStart?: string; coverageEnd?: string }): Promise<ActResult>
  refreshProposal(input: { ref: string }): Promise<ActResult>
  withdrawProposal(input: { ref: string; reason: string }): Promise<ActResult>
  proposalStatus(): Promise<ActResult>
  triageItem(input: { ref: string; disposition?: string; grounds?: string }): Promise<ActResult>
  intakeSummary(): Promise<ActResult>
  readScreenContext(input: { route: string; records: ScreenContextRecord[] }): Promise<ActResult>
  // ---- read acts over existing RBAC'd GET routes (D-PEC-20 item 3; D-T0-21
  // O-B basis-gated for model-provider engines — refused under 'enumerated',
  // RBAC-visible under 'broad'). Read-only; summaries carry record refs. ----
  projectOverview(): Promise<ActResult>
  readRegister(input: { register: string }): Promise<ActResult>
  recordHistory(input: { recordType: string; id: number }): Promise<ActResult>
  explainRevision(input: { id: number }): Promise<ActResult>
  readReport(input: { report: string; id?: number }): Promise<ActResult>
}

export interface AgentEnginePort {
  readonly subject: EngineSubject
  readonly egress: EgressClass
  runTurn(input: AgentTurnInput, acts: BoundActs): Promise<AgentEvent[]>
}
