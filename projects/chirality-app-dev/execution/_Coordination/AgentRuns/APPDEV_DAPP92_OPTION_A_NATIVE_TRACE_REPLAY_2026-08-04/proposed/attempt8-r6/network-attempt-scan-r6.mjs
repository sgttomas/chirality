import { spawnSync } from 'node:child_process';
import { writeFileSync } from 'node:fs';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const EVIDENCE = `${ROOT}/evidence`;
const pattern = 'https?://|download|fetch|network|ECONN|ENET|EAI_AGAIN|registry|proxy|TLS';
const result = spawnSync('/usr/bin/grep', ['-E', '-i', pattern, `${EVIDENCE}/attempt8-package.stdout-stderr.txt`], { encoding: 'utf8', timeout: 10000 });
writeFileSync(`${EVIDENCE}/network-scan.matches.txt`, result.stdout ?? '', { flag: 'wx', mode: 0o600 });
writeFileSync(`${EVIDENCE}/network-scan.status.json`, `${JSON.stringify({ schema: 'chirality-dapp92-network-scan-r6/v1', actionId: 'C1048', status: result.status, signal: result.signal, error: result.error?.message ?? null, matchBytes: Buffer.byteLength(result.stdout ?? '') }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
if (result.status !== 1 || result.signal !== null || result.error || (result.stdout ?? '') !== '') throw new Error('network-attempt scan did not return status 1 with zero bytes');
