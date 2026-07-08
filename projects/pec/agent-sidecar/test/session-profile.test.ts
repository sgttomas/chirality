/**
 * D-T0-22/D-PEC-22 pins: the opt-in session profile. What is pinned:
 * config parse (default hermetic, open accepted, anything else refused at
 * load); the hermetic query-options shape is BYTE-IDENTICAL to the ruled
 * D-PEC-21 session (the adversarial pin in engine-sdk-loop.test.ts also
 * stands unmodified); under 'open' the `tools` restrictor is absent, the
 * three setting sources load, the pec tools stay auto-approved, and
 * canUseTool allows built-ins (while the hermetic deny still refuses them);
 * /agent/health discloses the active profile.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createServer } from 'node:http'
import type { Server } from 'node:http'
import { loadConfig, parseSessionProfile } from '../src/config.ts'
import type { SidecarConfig } from '../src/config.ts'
import { buildQueryOptions, PEC_TOOL_NAMES } from '../src/engine/sdk.ts'
import { startSidecar } from '../src/index.ts'

type CanUseTool = (name: string, input: unknown) => Promise<{ behavior: string; message?: string }>

// ---------- config ----------

test('PEC_AGENT_SESSION: default hermetic, open accepted, anything else refused at load', () => {
  const env = { PEC_BASE_URL: 'http://127.0.0.1:4810' }
  assert.equal(loadConfig({ ...env }).session, 'hermetic')
  assert.equal(loadConfig({ ...env, PEC_AGENT_SESSION: 'hermetic' }).session, 'hermetic')
  assert.equal(loadConfig({ ...env, PEC_AGENT_SESSION: 'open' }).session, 'open')
  assert.throws(() => loadConfig({ ...env, PEC_AGENT_SESSION: 'broad' }), /PEC_AGENT_SESSION/)
  assert.throws(() => loadConfig({ ...env, PEC_AGENT_SESSION: 'OPEN' }), /PEC_AGENT_SESSION/)
  assert.throws(() => parseSessionProfile('full'), /PEC_AGENT_SESSION/)
})

// ---------- query options: hermetic default unchanged, open lifts exactly two restrictors ----------

test('hermetic profile (default and explicit): the ruled D-PEC-21 session shape, unchanged', async () => {
  for (const env of [{}, { PEC_AGENT_SESSION: 'hermetic' }]) {
    const opts = buildQueryOptions({ marker: 'server' }, env)
    assert.deepEqual(opts.tools, [], 'tools: [] is the load-bearing restrictor')
    assert.deepEqual(opts.settingSources, [])
    assert.deepEqual(opts.allowedTools, PEC_TOOL_NAMES.map((n) => `mcp__pec__${n}`))
    const canUse = opts.canUseTool as CanUseTool
    assert.equal((await canUse('mcp__pec__read_register', {})).behavior, 'allow')
    assert.equal((await canUse('Bash', {})).behavior, 'deny')
    assert.equal((await canUse('Read', {})).behavior, 'deny')
    assert.ok(!String(opts.systemPrompt).includes('OPEN session profile'))
  }
})

test("open profile: no tools restrictor, harness setting sources, pec tools still auto-approved, built-ins allowed", async () => {
  const opts = buildQueryOptions({ marker: 'server' }, { PEC_AGENT_SESSION: 'open' })
  assert.ok(!('tools' in opts), "the 'tools' restrictor is omitted — the SDK's built-in tool set loads")
  assert.deepEqual(opts.settingSources, ['user', 'project', 'local'])
  assert.deepEqual(opts.allowedTools, PEC_TOOL_NAMES.map((n) => `mcp__pec__${n}`))
  const canUse = opts.canUseTool as CanUseTool
  assert.equal((await canUse('mcp__pec__read_register', {})).behavior, 'allow')
  assert.equal((await canUse('Bash', {})).behavior, 'allow')
  assert.equal((await canUse('Read', {})).behavior, 'allow')
  assert.ok(String(opts.systemPrompt).includes('OPEN session profile'))
  assert.ok(String(opts.systemPrompt).includes('remain human acts in Admin'))
})

test('open profile leaves the shared knobs intact (budget/model ride the same env)', () => {
  const opts = buildQueryOptions({ marker: 'server' }, {
    PEC_AGENT_SESSION: 'open', PEC_AGENT_MAX_ACTS: '32', PEC_AGENT_MODEL: 'claude-fable-5',
  })
  assert.equal(opts.maxTurns, 36)
  assert.equal(opts.model, 'claude-fable-5')
  assert.deepEqual((opts.mcpServers as Record<string, unknown>).pec, { marker: 'server' })
})

// ---------- health disclosure ----------

let server: Server
let base = ''
before(async () => {
  server = createServer((_req, res) => {
    res.writeHead(200, { 'content-type': 'application/json' })
    res.end('{}')
  })
  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve))
  const addr = server.address()
  base = `http://127.0.0.1:${typeof addr === 'object' && addr ? addr.port : 0}`
})
after(async () => { await new Promise<void>((r) => server.close(() => r())) })

test('/agent/health states the active session profile (hermetic and open)', async () => {
  for (const session of ['hermetic', 'open'] as const) {
    const cfg: SidecarConfig = {
      engine: 'stub', access: 'enumerated', session, pecBaseUrl: base, port: 0,
      agentEmail: null, agentPassword: null,
    }
    const s = await startSidecar(cfg)
    try {
      const health = await fetch(`http://127.0.0.1:${s.port}/agent/health`)
      const h = await health.json() as Record<string, unknown>
      assert.equal(h.session, session)
    } finally {
      await s.close()
    }
  }
})
