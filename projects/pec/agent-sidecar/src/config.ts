/**
 * Sidecar configuration (D-PEC-17). Env-driven; the engine is config-selected
 * ('stub' default — the only engine exercised while no ANTHROPIC_API_KEY exists;
 * Receipt 32 item 4). The pec base URL is loopback-only BY CONSTRUCTION
 * (D-T0-19 O-2A localhost transport): a non-loopback host is refused at load
 * time, not at request time. Credentials never appear in errors or logs.
 */

export type EngineName = 'stub' | 'sdk'

/**
 * Access basis for model-provider-egress reads (D-T0-21 O-B, dual basis):
 * 'enumerated' (default) — the D-T0-20 O-B clamp exactly as ruled; 'broad' —
 * RBAC-visible reads pass for model-provider engines too (owner-selected per
 * launch; the human-only acts are excluded regardless of basis).
 */
export type AccessBasis = 'enumerated' | 'broad'

export interface SidecarConfig {
  engine: EngineName
  /** D-T0-21 O-B access basis; default 'enumerated' — never widened silently */
  access: AccessBasis
  /** pec server base URL — loopback only (127.0.0.1 / ::1 / localhost). */
  pecBaseUrl: string
  /** port the sidecar's own loopback HTTP surface listens on */
  port: number
  /** owner-provisioned agent person (is_admin=0, coordinator-class); null ⇒ unconfigured mode */
  agentEmail: string | null
  /** never logged, never echoed into responses or errors */
  agentPassword: string | null
}

const LOOPBACK_HOSTNAMES = ['127.0.0.1', '::1', '[::1]', 'localhost']

/** Refuse non-loopback pec hosts by construction (D-T0-19 O-2A; brief §3). */
export function assertLoopbackBaseUrl(baseUrl: string): void {
  let url: URL
  try {
    url = new URL(baseUrl)
  } catch {
    throw new Error(`PEC_BASE_URL is not a valid URL: ${baseUrl}`)
  }
  if (!LOOPBACK_HOSTNAMES.includes(url.hostname.toLowerCase())) {
    throw new Error(
      `PEC_BASE_URL must be loopback (127.0.0.1, ::1, or localhost) — refused: ${url.hostname} (D-T0-19 O-2A)`,
    )
  }
}

export function loadConfig(env: Record<string, string | undefined> = process.env): SidecarConfig {
  const engineRaw = (env.PEC_AGENT_ENGINE ?? 'stub').trim()
  if (engineRaw !== 'stub' && engineRaw !== 'sdk') {
    throw new Error(`PEC_AGENT_ENGINE must be 'stub' or 'sdk' — got '${engineRaw}'`)
  }
  const accessRaw = (env.PEC_AGENT_ACCESS ?? 'enumerated').trim()
  if (accessRaw !== 'enumerated' && accessRaw !== 'broad') {
    throw new Error(`PEC_AGENT_ACCESS must be 'enumerated' or 'broad' — got '${accessRaw}'`)
  }
  const pecBaseUrl = (env.PEC_BASE_URL ?? 'http://127.0.0.1:4810').trim().replace(/\/+$/, '')
  assertLoopbackBaseUrl(pecBaseUrl)
  const port = Number(env.PEC_AGENT_PORT ?? 4812)
  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    throw new Error(`PEC_AGENT_PORT must be a valid port number — got '${env.PEC_AGENT_PORT}'`)
  }
  const agentEmail = env.PEC_AGENT_EMAIL?.trim() || null
  const agentPassword = env.PEC_AGENT_PASSWORD || null
  return { engine: engineRaw, access: accessRaw, pecBaseUrl, port, agentEmail, agentPassword }
}
