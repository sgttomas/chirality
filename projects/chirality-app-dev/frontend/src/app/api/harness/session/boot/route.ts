import { NextResponse } from 'next/server';
import { HarnessError } from '@chirality/harness-contract/errors';
import {
  errorResponse,
  readJsonBody,
  requireNonEmptyString
} from '../../../../../lib/harness/http';
import { resolveRuntimeOptions } from '../../../../../lib/harness/options';
import { buildHarnessRuntimeFingerprint } from '../../../../../lib/harness/runtime-fingerprint';
import { getHarnessRuntime } from '../../../../../lib/harness/runtime';
import { assertProjectRootAccessible } from '../../../../../lib/harness/session-manager';
import { SessionBootRequest } from '@chirality/harness-contract/types';
import { randomUUID } from 'node:crypto';

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

    const engine = runtime.resolveEngine(session, resolvedOpts);
    const effectiveOpts = engine.selection.model
      ? { ...resolvedOpts, model: engine.selection.model }
      : resolvedOpts;
    const turnId = `turn_${randomUUID()}`;
    const runInput = {
      session,
      message: 'bootstrap',
      opts: effectiveOpts,
      turnId
    };
    await engine.port.preflight(runInput);

    let engineSessionId = session.adapterSession?.engineSessionId ?? session.engineSessionId;
    let adapterId = engine.selection.adapterId;
    let providerId = engine.selection.providerId;
    let model = effectiveOpts.model;
    let claudeSessionId =
      providerId === 'anthropic' ? session.claudeSessionId : undefined;

    for await (const event of engine.port.startTurn(runInput)) {
      if (event.type === 'session:init') {
        engineSessionId = event.data.engineSessionId;
        adapterId = event.data.adapterId;
        providerId = event.data.providerId;
        model = event.data.model;
        claudeSessionId =
          providerId === 'anthropic' ? event.data.claudeSessionId : undefined;
      }
      if (event.type === 'process:exit' && event.data.exitCode !== 0) {
        throw new HarnessError('SDK_FAILURE', 500, 'Boot turn failed before completion', {
          exitCode: event.data.exitCode
        });
      }
    }

    if (!engineSessionId) {
      throw new HarnessError('SDK_FAILURE', 500, 'Boot turn did not initialize an engine session');
    }

    const bootedAt = new Date().toISOString();
    const runtimeFingerprint = buildHarnessRuntimeFingerprint(engine.port.descriptor, {
      adapterId,
      providerId,
      model
    });
    const updatedSession = await runtime.sessionManager.save(sessionId, {
      engineSessionId,
      engineSelection: { adapterId, providerId, model },
      adapterSession: {
        ...session.adapterSession,
        engineSessionId,
        packageName: engine.port.descriptor.packageName,
        packageVersion: engine.port.descriptor.packageVersion
      },
      ...(providerId === 'anthropic' ? { claudeSessionId } : {}),
      ...(adapterId === 'claude-agent-sdk'
        ? {
            sdkSessionId: engineSessionId,
            sdkPackageVersion: engine.port.descriptor.packageVersion
          }
        : {}),
      bootFingerprint,
      runtimeFingerprint,
      bootedAt,
      model
    });

    return NextResponse.json(
      {
        session: updatedSession,
        boot: {
          engineSessionId,
          adapterId,
          providerId,
          model,
          ...(providerId === 'anthropic' && claudeSessionId ? { claudeSessionId } : {}),
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
