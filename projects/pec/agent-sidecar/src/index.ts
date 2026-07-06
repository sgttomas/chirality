/**
 * Sidecar entrypoint (D-PEC-17): loadConfig → engine selection ('stub'
 * default; 'sdk' via the key-droppable loader) → agent login when configured
 * (fatal on misprovisioning, rider 3) → loopback-only listen.
 *
 * Also exports startSidecar() for the e2e test: in-process start against a
 * harness-spawned pec server, no child processes needed.
 */

import type { Server } from 'node:http'
import { pathToFileURL } from 'node:url'
import type { SidecarConfig } from './config.ts'
import { loadConfig } from './config.ts'
import { PecAgentClient } from './pec-client.ts'
import type { AgentEnginePort } from './engine/port.ts'
import { createStubEngine } from './engine/stub.ts'
import { createSdkEngine } from './engine/sdk.ts'
import { createSidecarHttpServer } from './http.ts'

async function selectEngine(cfg: SidecarConfig): Promise<AgentEnginePort> {
  if (cfg.engine === 'sdk') return createSdkEngine(cfg)
  return createStubEngine()
}

export interface RunningSidecar {
  port: number
  engine: AgentEnginePort
  client: PecAgentClient
  configured: boolean
  close(): Promise<void>
}

export async function startSidecar(cfg: SidecarConfig): Promise<RunningSidecar> {
  const engine = await selectEngine(cfg)
  const client = new PecAgentClient(cfg)
  let configured = false
  if (cfg.agentEmail && cfg.agentPassword) {
    // fatal on misprovisioning (AGENT_MISPROVISIONED propagates)
    await client.login()
    configured = true
  }
  const server: Server = createSidecarHttpServer({ cfg, engine, client, configured })
  await new Promise<void>((resolve, reject) => {
    server.once('error', reject)
    server.listen(cfg.port, '127.0.0.1', resolve)
  })
  const addr = server.address()
  const port = typeof addr === 'object' && addr ? addr.port : cfg.port
  return {
    port, engine, client, configured,
    close: () => new Promise((resolve) => server.close(() => resolve())),
  }
}

// direct execution: node src/index.ts
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const cfg = loadConfig()
  startSidecar(cfg).then(
    (s) => {
      console.log(`pec agent sidecar on http://127.0.0.1:${s.port} `
        + `(engine: ${s.engine.subject}, egress: ${s.engine.egress}, `
        + `${s.configured ? `agent: ${s.client.whoami()?.email ?? '?'}` : 'unconfigured — set PEC_AGENT_EMAIL/PEC_AGENT_PASSWORD'})`)
    },
    (e) => {
      console.error(`sidecar failed to start: ${e instanceof Error ? e.message : String(e)}`)
      process.exit(1)
    },
  )
}
