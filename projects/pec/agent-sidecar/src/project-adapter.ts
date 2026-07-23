/**
 * Deterministic PEC project adapter.
 *
 * The root runtime decides which governed tools a session receives. This
 * service executes a named PEC act under the owner-provisioned, person-bound
 * PEC agent identity. Human-only acts are absent from the dispatch table and
 * remain denied again by PecAgentClient and PEC server RBAC.
 */

import type { AccessBasis } from './config.ts'
import type { BoundActs, ActResult } from './engine/port.ts'

export const PEC_ADAPTER_ACTS = [
  'import.propose',
  'import.refresh',
  'import.withdraw',
  'import.status',
  'intake.triage',
  'intake.summary',
  'screen.read',
  'read.overview',
  'read.register',
  'read.history',
  'read.explain',
  'read.report',
  'report.draftDocx',
] as const

export type PecAdapterAct = (typeof PEC_ADAPTER_ACTS)[number]

export interface PecAdapterExecution {
  pid: number
  act: PecAdapterAct
  input?: unknown
}

export interface PecAdapterDescriptor {
  service: 'pec-project-adapter'
  schemaVersion: 'pec.adapter/v1'
  access: AccessBasis
  acts: readonly PecAdapterAct[]
  configured: boolean
  agent: { name: string; email: string } | null
}

function recordInput(value: unknown): Record<string, unknown> {
  if (value == null) return {}
  if (typeof value !== 'object' || Array.isArray(value)) throw Object.assign(
    new Error('adapter act input must be an object'),
    { code: 'BAD_REQUEST' },
  )
  return value as Record<string, unknown>
}

function requiredString(input: Record<string, unknown>, key: string): string {
  const value = input[key]
  if (typeof value !== 'string' || !value.trim()) throw Object.assign(
    new Error(`${key} must be a non-empty string`),
    { code: 'BAD_REQUEST' },
  )
  return value
}

function optionalString(input: Record<string, unknown>, key: string): string | undefined {
  const value = input[key]
  if (value == null) return undefined
  if (typeof value !== 'string') throw Object.assign(new Error(`${key} must be a string`), { code: 'BAD_REQUEST' })
  return value
}

function requiredPositiveInteger(input: Record<string, unknown>, key: string): number {
  const value = Number(input[key])
  if (!Number.isInteger(value) || value <= 0) throw Object.assign(
    new Error(`${key} must be a positive integer`),
    { code: 'BAD_REQUEST' },
  )
  return value
}

/**
 * Closed dispatch table. Notably absent: import.accept/apply, force,
 * approval/decision/check outcomes, condition waiver, access changes, issue,
 * attestation, and consequence closure.
 */
export async function executePecAdapterAct(
  acts: BoundActs,
  execution: PecAdapterExecution,
): Promise<ActResult> {
  const input = recordInput(execution.input)
  switch (execution.act) {
    case 'import.propose':
      return acts.proposeCsv({
        csv: optionalString(input, 'csv'),
        xlsxBase64: optionalString(input, 'xlsxBase64'),
        sheet: optionalString(input, 'sheet'),
        filename: optionalString(input, 'filename'),
        contract: optionalString(input, 'contract'),
        coverageStart: optionalString(input, 'coverageStart'),
        coverageEnd: optionalString(input, 'coverageEnd'),
      })
    case 'import.refresh':
      return acts.refreshProposal({ ref: requiredString(input, 'ref') })
    case 'import.withdraw':
      return acts.withdrawProposal({
        ref: requiredString(input, 'ref'),
        reason: requiredString(input, 'reason'),
      })
    case 'import.status':
      return acts.proposalStatus()
    case 'intake.triage':
      return acts.triageItem({
        ref: requiredString(input, 'ref'),
        disposition: optionalString(input, 'disposition'),
        grounds: optionalString(input, 'grounds'),
      })
    case 'intake.summary':
      return acts.intakeSummary()
    case 'screen.read': {
      const records = input.records
      if (!Array.isArray(records)) throw Object.assign(new Error('records must be an array'), { code: 'BAD_REQUEST' })
      return acts.readScreenContext({
        route: requiredString(input, 'route'),
        records: records.map((record) => {
          const row = recordInput(record)
          return {
            recordType: requiredString(row, 'recordType'),
            ref: requiredString(row, 'ref'),
            id: requiredPositiveInteger(row, 'id'),
          }
        }),
      })
    }
    case 'read.overview':
      return acts.projectOverview()
    case 'read.register':
      return acts.readRegister({ register: requiredString(input, 'register') })
    case 'read.history':
      return acts.recordHistory({
        recordType: requiredString(input, 'recordType'),
        id: requiredPositiveInteger(input, 'id'),
      })
    case 'read.explain':
      return acts.explainRevision({ id: requiredPositiveInteger(input, 'id') })
    case 'read.report':
      return acts.readReport({
        report: requiredString(input, 'report'),
        ...(input.id == null ? {} : { id: requiredPositiveInteger(input, 'id') }),
      })
    case 'report.draftDocx':
      return acts.draftDocx({
        periodStart: optionalString(input, 'periodStart'),
        periodEnd: optionalString(input, 'periodEnd'),
      })
    default:
      throw Object.assign(
        new Error(`act is not exposed by the PEC project adapter: ${String(execution.act)}`),
        { code: 'AGENT_FORBIDDEN_ACT' },
      )
  }
}
