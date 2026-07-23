/**
 * Historical D-PEC-17 execution loop retained only for regression tests during
 * the one-cycle migration. The package production entrypoint does not import
 * or call this module. D-PEC-56 forbids using it as a runtime fallback.
 */

import type { Server } from 'node:http'
import type { SidecarConfig } from './config.ts'
import { PecAgentClient } from './pec-client.ts'
import type { AgentEnginePort } from './engine/port.ts'
import { createStubEngine } from './engine/stub.ts'
import { createSdkEngine } from './engine/sdk.ts'
import { createSidecarHttpServer } from './http.ts'

async function selectLegacyEngine(cfg: SidecarConfig): Promise<AgentEnginePort> {
  if (cfg.engine === 'sdk') return createSdkEngine(cfg)
  return createStubEngine()
}

export interface RunningLegacyAgentLoop {
  port: number
  engine: AgentEnginePort
  client: PecAgentClient
  configured: boolean
  close(): Promise<void>
}

export async function startLegacyAgentLoopForTests(cfg: SidecarConfig): Promise<RunningLegacyAgentLoop> {
  const engine = await selectLegacyEngine(cfg)
  const client = new PecAgentClient(cfg)
  let configured = false
  if (cfg.agentEmail && cfg.agentPassword) {
    await client.login()
    configured = true
  }
  const server: Server = createSidecarHttpServer({ cfg, engine, client, configured })
  await new Promise<void>((resolve, reject) => {
    server.once('error', reject)
    server.listen(cfg.port, '127.0.0.1', resolve)
  })
  const address = server.address()
  const port = typeof address === 'object' && address ? address.port : cfg.port
  return {
    port,
    engine,
    client,
    configured,
    close: () => new Promise((resolve) => server.close(() => resolve())),
  }
}
