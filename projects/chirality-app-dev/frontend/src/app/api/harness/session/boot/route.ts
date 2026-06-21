import { NextResponse } from 'next/server';
import { HarnessError } from '../../../../../lib/harness/errors';
import {
  errorResponse,
  readJsonBody,
  requireNonEmptyString
} from '../../../../../lib/harness/http';
import { resolveRuntimeOptions } from '../../../../../lib/harness/options';
import { buildHarnessRuntimeFingerprint } from '../../../../../lib/harness/runtime-fingerprint';
import { getHarnessRuntime } from '../../../../../lib/harness/runtime';
import { assertProjectRootAccessible } from '../../../../../lib/harness/session-manager';
import { SessionBootRequest } from '../../../../../lib/harness/types';

export async function POST(request: Request): Promise<Response> {
  try {
    const body = await readJsonBody<SessionBootRequest>(request);
    const sessionId = requireNonEmptyString(body.sessionId, 'sessionId');

    const runtime = getHarnessRuntime();
    const session = await runtime.sessionManager.resume(sessionId);
    await assertProjectRootAccessible(session.projectRoot);
    const resolvedOpts = await resolveRuntimeOptions(session, body.opts);

    await runtime.personaManager.buildSystemPrompt(
      session.projectRoot,
      resolvedOpts.persona,
      resolvedOpts.mode,
      resolvedOpts.tools
    );

    const bootFingerprint = runtime.personaManager.getBootFingerprint(
      resolvedOpts.persona,
      resolvedOpts.mode,
      session.projectRoot,
      resolvedOpts.tools
    );

    let engineSessionId = session.engineSessionId ?? session.claudeSessionId;
    let claudeSessionId = session.claudeSessionId;

    for await (const event of runtime.agentSdkManager.startTurn(
      session,
      'bootstrap',
      resolvedOpts
    )) {
      if (event.type === 'session:init') {
        engineSessionId = event.data.engineSessionId ?? event.data.claudeSessionId;
        claudeSessionId = event.data.claudeSessionId;
      }
      if (event.type === 'process:exit' && event.data.exitCode !== 0) {
        throw new HarnessError('SDK_FAILURE', 500, 'Boot turn failed before completion', {
          exitCode: event.data.exitCode
        });
      }
    }

    const bootedAt = new Date().toISOString();
    const runtimeFingerprint = buildHarnessRuntimeFingerprint();
    const updatedSession = await runtime.sessionManager.save(sessionId, {
      engineSessionId,
      claudeSessionId,
      sdkPackageVersion: runtimeFingerprint.sdkPackageVersion,
      bootFingerprint,
      runtimeFingerprint,
      bootedAt,
      model: resolvedOpts.model
    });

    return NextResponse.json(
      {
        session: updatedSession,
        boot: {
          engineSessionId,
          claudeSessionId,
          bootFingerprint,
          runtimeFingerprint,
          bootedAt
        }
      },
      { status: 200 }
    );
  } catch (error) {
    return errorResponse(error);
  }
}
