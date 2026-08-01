/**
 * Run the workspace test suites concurrently (root `npm test`).
 *
 * Each workspace's output is buffered and printed as a single attributed block
 * when that workspace finishes, so interleaved parallel output never obscures
 * which workspace a failure belongs to. Exits nonzero if ANY workspace fails.
 *
 * Zero dependencies: plain node:child_process against the same
 * `npm run test --workspace <name>` commands the previous serial script ran.
 */

import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { join } from 'node:path'

const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..')
const WORKSPACES = ['core', 'server', 'agent-sidecar']

interface WorkspaceResult { workspace: string; code: number; output: string; ms: number }

function runWorkspace(workspace: string): Promise<WorkspaceResult> {
  return new Promise((resolve) => {
    const start = Date.now()
    const child = spawn('npm', ['run', 'test', '--workspace', workspace], {
      cwd: ROOT,
      env: process.env,
      stdio: ['ignore', 'pipe', 'pipe'],
    })
    const chunks: Buffer[] = []
    child.stdout.on('data', (c: Buffer) => chunks.push(c))
    child.stderr.on('data', (c: Buffer) => chunks.push(c))
    child.on('error', (err) => {
      resolve({ workspace, code: 1, output: `failed to spawn npm: ${err.message}\n`, ms: Date.now() - start })
    })
    child.on('close', (code) => {
      resolve({ workspace, code: code ?? 1, output: Buffer.concat(chunks).toString('utf8'), ms: Date.now() - start })
    })
  })
}

const results: WorkspaceResult[] = []
await Promise.all(WORKSPACES.map(async (workspace) => {
  const result = await runWorkspace(workspace)
  // Print each workspace as one contiguous block the moment it finishes.
  const status = result.code === 0 ? 'PASS' : `FAIL (exit ${result.code})`
  console.log(`\n===== ${workspace}: ${status} in ${(result.ms / 1000).toFixed(1)}s =====\n`)
  process.stdout.write(result.output)
  results.push(result)
}))

const failed = results.filter((r) => r.code !== 0)
console.log('\n===== summary =====')
for (const r of results.sort((a, b) => WORKSPACES.indexOf(a.workspace) - WORKSPACES.indexOf(b.workspace))) {
  console.log(`${r.code === 0 ? 'PASS' : 'FAIL'}  ${r.workspace} (${(r.ms / 1000).toFixed(1)}s)`)
}
if (failed.length > 0) {
  console.error(`\n${failed.length} workspace(s) failed: ${failed.map((r) => r.workspace).join(', ')}`)
  process.exit(1)
}
