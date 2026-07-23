/**
 * PEC deterministic project-adapter entrypoint (D-PEC-56).
 *
 * The root Chirality runtime owns models, credentials, conversations,
 * sessions, delegation, interruption, and residency. This process owns only
 * person-bound PEC deterministic acts and their RBAC/data-boundary guards.
 */

import type { Server } from 'node:http'
import { readFile, stat } from 'node:fs/promises'
import { pathToFileURL } from 'node:url'
import type { ProjectAdapterConfig } from './config.ts'
import { loadProjectAdapterConfig } from './config.ts'
import { PecAgentClient } from './pec-client.ts'
import { createProjectAdapterHttpServer } from './project-adapter-http.ts'

export interface RunningProjectAdapter {
  port: number
  client: PecAgentClient
  configured: boolean
  close(): Promise<void>
}

export async function startProjectAdapter(cfg: ProjectAdapterConfig): Promise<RunningProjectAdapter> {
  const tokenStat = await stat(cfg.adapterTokenFile)
  if (!tokenStat.isFile() || (tokenStat.mode & 0o077) !== 0) {
    throw new Error('PEC adapter credential file must be a regular mode-0600 file')
  }
  const adapterToken = (await readFile(cfg.adapterTokenFile, 'utf8')).trim()
  if (adapterToken.length < 32) {
    throw new Error('PEC adapter credential must contain at least 32 non-whitespace characters')
  }
  const client = new PecAgentClient(cfg)
  let configured = false
  if (cfg.agentEmail && cfg.agentPassword) {
    // Fatal on misprovisioning: the adapter must never impersonate a human or
    // operate with import.accept/admin authority.
    await client.login()
    configured = true
  }
  const server: Server = createProjectAdapterHttpServer({
    cfg,
    client,
    configured,
    adapterToken,
  })
  await new Promise<void>((resolve, reject) => {
    server.once('error', reject)
    server.listen(cfg.port, '127.0.0.1', resolve)
  })
  const address = server.address()
  const port = typeof address === 'object' && address ? address.port : cfg.port
  return {
    port,
    client,
    configured,
    close: () => new Promise((resolve) => server.close(() => resolve())),
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const cfg = loadProjectAdapterConfig()
  startProjectAdapter(cfg).then(
    (adapter) => {
      console.log(`pec deterministic project adapter on http://127.0.0.1:${adapter.port} `
        + `(${adapter.configured ? `agent: ${adapter.client.whoami()?.email ?? '?'}` : 'unconfigured — set PEC_AGENT_EMAIL/PEC_AGENT_PASSWORD'})`)
    },
    (error) => {
      console.error(`project adapter failed to start: ${error instanceof Error ? error.message : String(error)}`)
      process.exit(1)
    },
  )
}
