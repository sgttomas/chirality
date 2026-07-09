import type { AgentEvent, BoundActs } from './engine/port.ts'

const reply = (text: string): AgentEvent => ({ type: 'agent:reply', text })

const toEvents = (r: Awaited<ReturnType<BoundActs['readReport']>>): AgentEvent[] =>
  r.kind === 'result'
    ? [{ type: 'act:result', act: r.act, ok: r.ok, summary: r.summary, payload: r.payload }]
    : [{ type: 'act:refused', act: r.act, reason: r.reason }]

function unsupportedReason(message: string): string | null {
  if (/\b(accept|apply|force|approve|issue|certify|seal|go[- ]?live|ready for construction)\b/i.test(message)) {
    return 'I cannot produce a report that performs or claims approval, issuance, certification, go-live, force, accept, or apply acts.'
  }
  if (/\b(forecast|predict|will be|guarantee|professional opinion)\b/i.test(message)) {
    return 'I cannot forecast or provide professional opinions; I can report only recorded facts and stated absent support.'
  }
  if (/\b(hidden|private|all database|raw sql|secret)\b/i.test(message)) {
    return 'I cannot report hidden data or bypass the bounded PEC read surface.'
  }
  return null
}

function reportNameFor(message: string): string | null {
  const lower = message.toLowerCase()
  if (/\bdiscipline\b/.test(lower)) return 'weekly-project-status-by-discipline'
  if (/\bpackage\b.*\b(issue|issues|risk|hold|decision|action)\b/.test(lower)) return 'package-issue-summary'
  if (/\bdeliverable|mdl|completeness\b/.test(lower)) return 'deliverable-completeness'
  if (/\bweekly|status|project\b/.test(lower)) return 'weekly-project-status'
  return null
}

export function isUserDefinedReportRequest(message: string): boolean {
  return /\b(user[- ]defined|custom|novel|draft|make|create|write)\b.*\breport\b/i.test(message)
    || /\breport\s+(on|about|for)\b/i.test(message)
}

export async function runUserDefinedReport(input: { pid: number; message: string }, acts: BoundActs): Promise<AgentEvent[]> {
  const unsupported = unsupportedReason(input.message)
  if (unsupported) return [{ type: 'act:refused', act: 'report.user_defined', reason: unsupported }]
  const report = reportNameFor(input.message)
  if (!report) {
    return [{
      type: 'act:refused',
      act: 'report.user_defined',
      reason: 'I need a report basis I can read: weekly project status, discipline status, package issue summary, or deliverable completeness.',
    }]
  }
  const r = await acts.readReport({ report })
  const events = toEvents(r)
  if (r.kind === 'refused') return events
  const payload = r.payload as { markdown?: string; absent?: Array<{ figure: string; reason: string }> } | undefined
  const absent = payload?.absent?.length
    ? `\nUnsupported or absent figures:\n${payload.absent.map((a) => `- ${a.figure}: ${a.reason}`).join('\n')}`
    : ''
  return [
    ...events,
    reply([
      `User-defined report draft from ${report}.`,
      payload?.markdown ?? r.summary,
      absent,
      `Basis: bounded PEC report read; accept/apply/issue remain human acts in Admin: /p/${input.pid}/admin`,
    ].filter(Boolean).join('\n\n')),
  ]
}
