import { chmod, mkdir, mkdtemp, symlink, writeFile } from 'node:fs/promises'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import assert from 'node:assert/strict'
import { test } from 'node:test'
import { createPecSharedRuntimeClient } from '../src/shared-runtime-client.ts'

async function fixture(): Promise<{
  socketPath: string
  tokens: string
}> {
  const root = await mkdtemp(join(tmpdir(), 'pec-runtime-principal-'))
  const runtime = join(root, 'runtime')
  const tokens = join(runtime, 'auth', 'tokens')
  await mkdir(tokens, { recursive: true, mode: 0o700 })
  return { socketPath: join(runtime, 'control.sock'), tokens }
}

test('PEC refuses operator, permissive, and symlink runtime token files', async () => {
  const { socketPath, tokens } = await fixture()
  const operator = join(tokens, 'operator.token')
  await writeFile(operator, 'operator-secret\n', { mode: 0o600 })
  assert.throws(
    () => createPecSharedRuntimeClient({
      CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
      CHIRALITY_PEC_RUNTIME_TOKEN_FILE: operator,
    }),
    /project-scoped/,
  )

  const permissive = join(tokens, 'project-wide.token')
  await writeFile(permissive, 'project-secret\n', { mode: 0o600 })
  await chmod(permissive, 0o644)
  assert.throws(
    () => createPecSharedRuntimeClient({
      CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
      CHIRALITY_PEC_RUNTIME_TOKEN_FILE: permissive,
    }),
    /private/,
  )

  const external = join(await mkdtemp(join(tmpdir(), 'pec-token-external-')), 'token')
  await writeFile(external, 'external-secret\n', { mode: 0o600 })
  const linked = join(tokens, 'project-linked.token')
  await symlink(external, linked)
  assert.throws(
    () => createPecSharedRuntimeClient({
      CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
      CHIRALITY_PEC_RUNTIME_TOKEN_FILE: linked,
    }),
    /private/,
  )
})
