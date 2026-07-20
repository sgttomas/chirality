import { createHash } from 'node:crypto';
import { spawn } from 'node:child_process';
import { constants as fsConstants } from 'node:fs';
import { access, readFile, realpath, stat } from 'node:fs/promises';
import path from 'node:path';
import { HarnessError } from '@chirality/harness-contract/errors';

export const OPEN_PIPE_STRESS_RUNNER_PATH_ENV =
  'CHIRALITY_OPEN_PIPE_STRESS_RUNNER_PATH';
export const OPEN_PIPE_STRESS_RUNNER_SHA256_ENV =
  'CHIRALITY_OPEN_PIPE_STRESS_RUNNER_SHA256';

export const HEADLESS_RUNNER_TIMEOUT_MS = 30_000;
export const HEADLESS_RUNNER_STDOUT_LIMIT_BYTES = 2 * 1024 * 1024;
export const HEADLESS_RUNNER_STDERR_LIMIT_BYTES = 2 * 1024 * 1024;

type RunnerExit = {
  exitCode: 0 | 1;
  result: Record<string, unknown>;
};

export type HeadlessRunnerEnvironment = Readonly<Record<string, string | undefined>>;

function fail(
  code: string,
  status = 400,
  details: Record<string, unknown> = {}
): never {
  throw new HarnessError('INVALID_REQUEST', status, code, {
    errorCode: code,
    ...details
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function hasNonEmptyString(record: Record<string, unknown>, key: string): boolean {
  return typeof record[key] === 'string' && record[key].trim().length > 0;
}

function hasRecord(record: Record<string, unknown>, key: string): boolean {
  return isRecord(record[key]);
}

function hasNonEmptyArray(record: Record<string, unknown>, key: string): boolean {
  return Array.isArray(record[key]) && record[key].length > 0;
}

function assertCompleteDec065SolveRequest(value: unknown): asserts value is Record<string, unknown> {
  if (!isRecord(value) || !isRecord(value.request) || !isRecord(value.solve)) {
    fail('HEADLESS_RUNNER_INPUT_SCHEMA_MISMATCH');
  }

  const request = value.request;
  const solve = value.solve;
  const complete =
    hasNonEmptyString(request, 'request_id') &&
    request.operation === 'solve' &&
    hasRecord(request, 'operation_ref') &&
    hasRecord(request, 'project_ref') &&
    hasRecord(request, 'model_ref') &&
    hasRecord(request, 'unit_system_ref') &&
    hasNonEmptyArray(request, 'load_basis_refs') &&
    hasRecord(request, 'input_manifest_ref') &&
    hasNonEmptyArray(request, 'requested_outputs') &&
    hasRecord(request, 'privacy') &&
    hasRecord(request, 'provenance') &&
    hasRecord(request, 'professional_boundary') &&
    hasRecord(request, 'tbd_decisions') &&
    hasRecord(solve, 'preview_model');

  if (!complete) {
    fail('HEADLESS_RUNNER_INPUT_SCHEMA_MISMATCH');
  }
}

function collectDiagnostics(value: unknown): Record<string, unknown>[] {
  if (!isRecord(value)) {
    return [];
  }
  const diagnosticGroups = [
    value.diagnostics,
    isRecord(value.request_validation) ? value.request_validation.diagnostics : undefined,
    isRecord(value.result_validation) ? value.result_validation.diagnostics : undefined,
    isRecord(value.runner_result) ? value.runner_result.diagnostics : undefined
  ];
  return diagnosticGroups.flatMap((group) =>
    Array.isArray(group) ? group.filter(isRecord) : []
  );
}

function assertDec065Result(value: unknown, exitCode: number): asserts value is Record<string, unknown> {
  if (!isRecord(value)) {
    fail('HEADLESS_RUNNER_RESULT_SCHEMA_MISMATCH', 502);
  }
  const structurallyValid =
    value.artifact === 'openpipestress.headless_runner_cli_output' &&
    hasNonEmptyString(value, 'schema_version') &&
    value.command === 'solve' &&
    value.operation === 'solve' &&
    hasRecord(value, 'policy') &&
    hasRecord(value, 'request_validation') &&
    hasRecord(value, 'result_validation');
  if (!structurallyValid) {
    fail('HEADLESS_RUNNER_RESULT_SCHEMA_MISMATCH', 502);
  }

  const blocking = collectDiagnostics(value).some(
    (diagnostic) => diagnostic.severity === 'blocking' || diagnostic.severity === 'Blocking'
  );
  if (exitCode === 0 && (!hasRecord(value, 'runner_result') || blocking)) {
    fail('HEADLESS_RUNNER_EXIT_RESULT_MISMATCH', 502);
  }
  if (exitCode === 1 && !blocking) {
    fail('HEADLESS_RUNNER_EXIT_RESULT_MISMATCH', 502);
  }
}

async function resolveVerifiedRunner(config: HeadlessRunnerEnvironment): Promise<string> {
  const configuredPath = config[OPEN_PIPE_STRESS_RUNNER_PATH_ENV];
  const expectedSha256 = config[OPEN_PIPE_STRESS_RUNNER_SHA256_ENV];
  if (!configuredPath || !expectedSha256) {
    fail('HEADLESS_RUNNER_CONFIG_MISSING');
  }
  if (!path.isAbsolute(configuredPath)) {
    fail('HEADLESS_RUNNER_PATH_NOT_ABSOLUTE');
  }
  if (!/^[0-9a-f]{64}$/.test(expectedSha256)) {
    fail('HEADLESS_RUNNER_SHA256_INVALID');
  }

  let resolvedPath: string;
  try {
    resolvedPath = await realpath(configuredPath);
  } catch {
    fail('HEADLESS_RUNNER_PATH_INVALID');
  }

  let runnerStat;
  try {
    runnerStat = await stat(resolvedPath);
  } catch {
    fail('HEADLESS_RUNNER_PATH_INVALID');
  }
  if (!runnerStat.isFile()) {
    fail('HEADLESS_RUNNER_NOT_REGULAR_FILE');
  }
  try {
    await access(resolvedPath, fsConstants.X_OK);
  } catch {
    fail('HEADLESS_RUNNER_NOT_EXECUTABLE');
  }

  let executableBytes: Buffer;
  try {
    executableBytes = await readFile(resolvedPath);
  } catch {
    fail('HEADLESS_RUNNER_PATH_INVALID');
  }
  const actualSha256 = createHash('sha256').update(executableBytes).digest('hex');
  if (actualSha256 !== expectedSha256) {
    fail('HEADLESS_RUNNER_SHA256_MISMATCH');
  }
  return resolvedPath;
}

async function collectChildResult(input: {
  executablePath: string;
  stdinBytes: Buffer;
  timeoutMs: number;
}): Promise<{ exitCode: number | null; signal: NodeJS.Signals | null; stdout: Buffer }> {
  return new Promise((resolve, reject) => {
    const child = spawn(input.executablePath, ['solve'], {
      shell: false,
      windowsHide: true,
      stdio: ['pipe', 'pipe', 'pipe'],
      env: {
        NODE_ENV: 'production',
        LANG: 'C',
        LC_ALL: 'C'
      }
    });
    const stdoutChunks: Buffer[] = [];
    let stdoutBytes = 0;
    let stderrBytes = 0;
    let failureCode: string | undefined;
    let settled = false;

    const terminate = (code: string) => {
      if (!failureCode) {
        failureCode = code;
        child.kill('SIGKILL');
      }
    };
    const timeout = setTimeout(() => terminate('HEADLESS_RUNNER_TIMEOUT'), input.timeoutMs);

    child.stdout.on('data', (chunk: Buffer | string) => {
      const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
      stdoutBytes += buffer.byteLength;
      if (stdoutBytes > HEADLESS_RUNNER_STDOUT_LIMIT_BYTES) {
        terminate('HEADLESS_RUNNER_STDOUT_OVERSIZE');
        return;
      }
      stdoutChunks.push(buffer);
    });
    child.stderr.on('data', (chunk: Buffer | string) => {
      const buffer = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
      stderrBytes += buffer.byteLength;
      if (stderrBytes > HEADLESS_RUNNER_STDERR_LIMIT_BYTES) {
        terminate('HEADLESS_RUNNER_STDERR_OVERSIZE');
      }
    });
    child.once('error', () => {
      clearTimeout(timeout);
      if (!settled) {
        settled = true;
        reject(new HarnessError('INVALID_REQUEST', 502, 'HEADLESS_RUNNER_SPAWN_FAILED', {
          errorCode: 'HEADLESS_RUNNER_SPAWN_FAILED'
        }));
      }
    });
    child.once('close', (exitCode, signal) => {
      clearTimeout(timeout);
      if (settled) {
        return;
      }
      settled = true;
      if (failureCode) {
        reject(new HarnessError('INVALID_REQUEST', 502, failureCode, { errorCode: failureCode }));
        return;
      }
      resolve({
        exitCode,
        signal,
        stdout: Buffer.concat(stdoutChunks, stdoutBytes)
      });
    });

    child.stdin.on('error', () => {
      terminate('HEADLESS_RUNNER_STDIN_FAILED');
    });
    child.stdin.end(input.stdinBytes);
  });
}

export async function runConfiguredHeadlessPreview(input: {
  requestBytes: Buffer;
  env?: HeadlessRunnerEnvironment;
  timeoutMs?: number;
}): Promise<RunnerExit> {
  let parsedInput: unknown;
  try {
    parsedInput = JSON.parse(input.requestBytes.toString('utf8'));
  } catch {
    fail('HEADLESS_RUNNER_INPUT_JSON_INVALID');
  }
  assertCompleteDec065SolveRequest(parsedInput);

  const executablePath = await resolveVerifiedRunner(input.env ?? process.env);
  const childResult = await collectChildResult({
    executablePath,
    stdinBytes: input.requestBytes,
    timeoutMs: input.timeoutMs ?? HEADLESS_RUNNER_TIMEOUT_MS
  });
  if (childResult.signal) {
    fail('HEADLESS_RUNNER_SIGNALLED', 502);
  }
  if (childResult.exitCode === 2) {
    fail('HEADLESS_RUNNER_INPUT_REFUSED');
  }
  if (childResult.exitCode !== 0 && childResult.exitCode !== 1) {
    fail('HEADLESS_RUNNER_EXIT_UNSUPPORTED', 502);
  }

  let parsedResult: unknown;
  try {
    parsedResult = JSON.parse(childResult.stdout.toString('utf8'));
  } catch {
    fail('HEADLESS_RUNNER_RESULT_JSON_INVALID', 502);
  }
  assertDec065Result(parsedResult, childResult.exitCode);
  return {
    exitCode: childResult.exitCode,
    result: parsedResult
  };
}
