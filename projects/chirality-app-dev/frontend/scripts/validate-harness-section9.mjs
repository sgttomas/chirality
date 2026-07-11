#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { constants as fsConstants } from 'node:fs';
import { access, copyFile, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const TMP_ROOT = path.join(
  process.env.TMPDIR ?? os.tmpdir(),
  'chirality-harness-section9-validation',
  'latest'
);
const LOG_DIR = path.join(TMP_ROOT, 'logs');
const TMP_SUMMARY_PATH = path.join(TMP_ROOT, 'summary.json');
const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const SOURCE_MANIFEST_PATH = path.join(SCRIPT_DIR, 'harness-section9-manifest.json');
const STABLE_SUMMARY_PATH = path.resolve(
  process.cwd(),
  'artifacts',
  'harness',
  'section9',
  'latest',
  'summary.json'
);
const STABLE_MANIFEST_PATH = path.resolve(
  process.cwd(),
  'artifacts',
  'harness',
  'section9',
  'latest',
  'manifest.json'
);

const SECTION9_IDS = [
  'section9.runtime_engine_contract',
  'section9.adapter_turn_engine_event_log',
  'section9.adapter_message_mapper',
  'section9.session_event_replay',
  'section9.reliance_boundary_register',
  'section9.settingsources_isolation',
  'section9.sdk_session_link_resume',
  'section9.permission_overlay_hard_deny_precedence',
  'section9.tool_runtime_read_file',
  'section9.chirality_mcp_status_dependencies',
  'section9.path_containment_hook',
  'section9.instruction_root_protection_hook',
  'section9.tool_result_budget',
  'section9.context_compaction_boundary',
  'section9.subagent_governance_hook',
  'section9.domain_profile_validation'
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

function requireNonEmptyStringArray(value, label, checkId) {
  if (!Array.isArray(value) || value.length === 0 || value.some((item) => typeof item !== 'string' || item.length === 0)) {
    throw new Error(`${checkId} must declare a non-empty ${label} array.`);
  }
}

async function loadManifest() {
  const manifest = JSON.parse(await readFile(SOURCE_MANIFEST_PATH, 'utf8'));
  if (manifest.schemaVersion !== 1) {
    throw new Error('Section 9 manifest schemaVersion must be 1.');
  }
  if (!Array.isArray(manifest.checks)) {
    throw new Error('Section 9 manifest checks must be an array.');
  }

  const ids = manifest.checks.map((check) => check?.id);
  if (new Set(ids).size !== ids.length) {
    throw new Error('Section 9 manifest contains duplicate check IDs.');
  }
  if (ids.length !== SECTION9_IDS.length || SECTION9_IDS.some((id) => !ids.includes(id))) {
    throw new Error('Section 9 manifest must contain the exact governed 16-ID inventory.');
  }

  for (const check of manifest.checks) {
    requireNonEmptyStringArray(check.sourceReferences, 'sourceReferences', check.id);
    requireNonEmptyStringArray(check.testFiles, 'testFiles', check.id);
    requireNonEmptyStringArray(check.evidenceFiles, 'evidenceFiles', check.id);
    if (!Array.isArray(check.warnings) || !Array.isArray(check.blockers)) {
      throw new Error(`${check.id} must declare warnings and blockers arrays.`);
    }
    await ensureTestFilesExist([...check.testFiles, ...check.evidenceFiles]);
  }

  return manifest;
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
      sourceReferences: check.sourceReferences,
      evidenceFiles: check.evidenceFiles,
      warnings: check.warnings,
      blockers: check.blockers,
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
    sourceReferences: check.sourceReferences,
    evidenceFiles: check.evidenceFiles,
    warnings: check.warnings,
    blockers: check.blockers,
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
  const manifest = await loadManifest();
  await rm(TMP_ROOT, { recursive: true, force: true });
  await mkdir(LOG_DIR, { recursive: true });

  const results = [];
  for (const check of manifest.checks) {
    console.log(`HARNESS_SECTION9_CHECK_START=${check.id}`);
    results.push(await runCheck(check));
  }

  const status = results.every((result) => result.status === 'pass') ? 'pass' : 'fail';
  const summary = {
    generatedAt: nowIso(),
    status,
    testCount: results.length,
    manifestPath: STABLE_MANIFEST_PATH,
    results
  };

  await writeJson(TMP_SUMMARY_PATH, summary);

  // Warm read to ensure summary is parseable and stable before copying it.
  JSON.parse(await readFile(TMP_SUMMARY_PATH, 'utf8'));

  await mkdir(path.dirname(STABLE_SUMMARY_PATH), { recursive: true });
  await copyFile(SOURCE_MANIFEST_PATH, STABLE_MANIFEST_PATH);
  await copyFile(TMP_SUMMARY_PATH, STABLE_SUMMARY_PATH);
  await ensureReadableFile(STABLE_MANIFEST_PATH);
  await ensureReadableFile(STABLE_SUMMARY_PATH);

  console.log(`HARNESS_SECTION9_SUMMARY_PATH=${STABLE_SUMMARY_PATH}`);
  console.log(`HARNESS_SECTION9_MANIFEST_PATH=${STABLE_MANIFEST_PATH}`);
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
  console.log(`HARNESS_SECTION9_TEST_COUNT=${SECTION9_IDS.length}`);
  process.exitCode = 1;
});
