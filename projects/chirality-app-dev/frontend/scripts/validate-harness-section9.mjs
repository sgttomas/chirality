#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { constants as fsConstants } from 'node:fs';
import { access, copyFile, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

const TMP_ROOT = path.join(
  process.env.TMPDIR ?? os.tmpdir(),
  'chirality-harness-section9-validation',
  'latest'
);
const LOG_DIR = path.join(TMP_ROOT, 'logs');
const TMP_SUMMARY_PATH = path.join(TMP_ROOT, 'summary.json');
const STABLE_SUMMARY_PATH = path.resolve(
  process.cwd(),
  'artifacts',
  'harness',
  'section9',
  'latest',
  'summary.json'
);

const SECTION9_CHECKS = [
  {
    id: 'section9.runtime_engine_contract',
    testFiles: ['src/__tests__/lib/engine-conformance.test.ts']
  },
  {
    id: 'section9.adapter_turn_engine_event_log',
    testFiles: ['src/__tests__/lib/turn-engine.test.ts']
  },
  {
    id: 'section9.adapter_message_mapper',
    testFiles: ['src/__tests__/lib/sdk-message-mapper.test.ts']
  },
  {
    id: 'section9.session_event_replay',
    testFiles: [
      'src/__tests__/lib/session-events.test.ts',
      'src/__tests__/lib/transcript-replay.test.ts'
    ]
  },
  {
    id: 'section9.sdk_session_link_resume',
    testFiles: [
      'src/__tests__/lib/sdk-options-builder.test.ts',
      'src/__tests__/lib/session-manager.test.ts',
      'src/__tests__/lib/transcript-replay.test.ts'
    ]
  },
  {
    id: 'section9.settingsources_isolation',
    testFiles: ['src/__tests__/lib/sdk-options-builder.test.ts']
  },
  {
    id: 'section9.permission_overlay_hard_deny_precedence',
    testFiles: ['src/__tests__/lib/permission-overlay.test.ts']
  },
  {
    id: 'section9.tool_runtime_read_file',
    testFiles: ['src/__tests__/lib/chirality-read-mcp.test.ts']
  },
  {
    id: 'section9.chirality_mcp_status_dependencies',
    testFiles: [
      'src/__tests__/lib/chirality-read-mcp.test.ts',
      'src/__tests__/lib/dependencies-register-contract.test.ts'
    ]
  },
  {
    id: 'section9.path_containment_hook',
    testFiles: [
      'src/__tests__/lib/chirality-hooks.test.ts',
      'src/__tests__/lib/permission-overlay.test.ts'
    ]
  },
  {
    id: 'section9.instruction_root_protection_hook',
    testFiles: [
      'src/__tests__/lib/harness-instruction-root.test.ts',
      'src/__tests__/scripts/verify-instruction-root-integrity.test.ts'
    ]
  },
  {
    id: 'section9.tool_result_budget',
    testFiles: [
      'src/__tests__/lib/tool-evidence.test.ts',
      'src/__tests__/lib/tool-result-artifacts.test.ts',
      'src/__tests__/lib/sdk-message-mapper.test.ts',
      'src/__tests__/lib/chirality-hooks.test.ts'
    ]
  },
  {
    id: 'section9.context_compaction_boundary',
    testFiles: [
      'src/__tests__/lib/sdk-message-mapper.test.ts',
      'src/__tests__/lib/session-events.test.ts'
    ]
  },
  {
    id: 'section9.subagent_governance_hook',
    testFiles: [
      'src/__tests__/lib/harness-subagent-governance.test.ts',
      'src/__tests__/lib/agent-runtime-contract.test.ts'
    ]
  }
];

function nowIso() {
  return new Date().toISOString();
}

function npmCommand() {
  return process.platform === 'win32' ? 'npm.cmd' : 'npm';
}

function safeSegment(value) {
  return value.replace(/[^A-Za-z0-9_.-]/g, '_').slice(0, 120);
}

async function ensureReadableFile(filePath) {
  await access(filePath, fsConstants.R_OK);
}

async function ensureTestFilesExist(testFiles) {
  for (const testFile of testFiles) {
    await ensureReadableFile(path.resolve(process.cwd(), testFile));
  }
}

async function writeJson(filePath, value) {
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

function runVitest(testFiles) {
  return new Promise((resolve, reject) => {
    const startedAt = nowIso();
    const startMs = Date.now();
    const child = spawn(npmCommand(), ['run', 'test', '--', ...testFiles], {
      cwd: process.cwd(),
      env: process.env,
      stdio: ['ignore', 'pipe', 'pipe']
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (chunk) => {
      const text = chunk.toString();
      stdout += text;
      process.stdout.write(text);
    });

    child.stderr.on('data', (chunk) => {
      const text = chunk.toString();
      stderr += text;
      process.stderr.write(text);
    });

    child.on('error', reject);
    child.on('close', (code) => {
      resolve({
        code: code ?? 1,
        stdout,
        stderr,
        startedAt,
        endedAt: nowIso(),
        durationMs: Date.now() - startMs
      });
    });
  });
}

async function runCheck(check) {
  const startedAt = nowIso();
  const startMs = Date.now();
  const logBase = path.join(LOG_DIR, safeSegment(check.id));
  const stdoutLog = `${logBase}.stdout.log`;
  const stderrLog = `${logBase}.stderr.log`;

  try {
    await ensureTestFilesExist(check.testFiles);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    await writeFile(stdoutLog, '', 'utf8');
    await writeFile(stderrLog, `${message}\n`, 'utf8');
    return {
      id: check.id,
      status: 'fail',
      durationMs: Date.now() - startMs,
      testFiles: check.testFiles,
      details: {
        exitCode: 1,
        stdoutLog,
        stderrLog
      },
      error: `Missing or unreadable test file: ${message}`,
      startedAt,
      endedAt: nowIso()
    };
  }

  const result = await runVitest(check.testFiles);
  await writeFile(stdoutLog, result.stdout, 'utf8');
  await writeFile(stderrLog, result.stderr, 'utf8');

  return {
    id: check.id,
    status: result.code === 0 ? 'pass' : 'fail',
    durationMs: result.durationMs,
    testFiles: check.testFiles,
    details: {
      exitCode: result.code,
      stdoutLog,
      stderrLog
    },
    ...(result.code === 0 ? {} : { error: `Vitest exited with code ${result.code}` }),
    startedAt: result.startedAt,
    endedAt: result.endedAt
  };
}

async function main() {
  await rm(TMP_ROOT, { recursive: true, force: true });
  await mkdir(LOG_DIR, { recursive: true });

  const results = [];
  for (const check of SECTION9_CHECKS) {
    console.log(`HARNESS_SECTION9_CHECK_START=${check.id}`);
    results.push(await runCheck(check));
  }

  const status = results.every((result) => result.status === 'pass') ? 'pass' : 'fail';
  const summary = {
    generatedAt: nowIso(),
    status,
    testCount: results.length,
    results
  };

  await writeJson(TMP_SUMMARY_PATH, summary);

  // Warm read to ensure summary is parseable and stable before copying it.
  JSON.parse(await readFile(TMP_SUMMARY_PATH, 'utf8'));

  await mkdir(path.dirname(STABLE_SUMMARY_PATH), { recursive: true });
  await copyFile(TMP_SUMMARY_PATH, STABLE_SUMMARY_PATH);
  await ensureReadableFile(STABLE_SUMMARY_PATH);

  console.log(`HARNESS_SECTION9_SUMMARY_PATH=${STABLE_SUMMARY_PATH}`);
  console.log(`HARNESS_SECTION9_SOURCE_SUMMARY_PATH=${TMP_SUMMARY_PATH}`);
  console.log(`HARNESS_SECTION9_STATUS=${status}`);
  console.log(`HARNESS_SECTION9_TEST_COUNT=${results.length}`);

  process.exitCode = status === 'pass' ? 0 : 1;
}

main().catch((error) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Harness Section 9 validation failed: ${message}`);
  console.log(`HARNESS_SECTION9_SUMMARY_PATH=${STABLE_SUMMARY_PATH}`);
  console.log(`HARNESS_SECTION9_SOURCE_SUMMARY_PATH=${TMP_SUMMARY_PATH}`);
  console.log('HARNESS_SECTION9_STATUS=fail');
  console.log(`HARNESS_SECTION9_TEST_COUNT=${SECTION9_CHECKS.length}`);
  process.exitCode = 1;
});
