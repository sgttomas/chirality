import { createHash } from 'node:crypto';
import {
  CHIRALITY_MCP_SERVER_NAME,
  CHIRALITY_MCP_SERVER_VERSION,
  CHIRALITY_MCP_TOOL_NAMES
} from './mcp/tool-names';
import { HARNESS_PERMISSION_POLICY_VERSION } from './permission-overlay';
import { PERSONA_COMPOSER_VERSION } from './persona-manager';
import { CLAUDE_AGENT_SDK_PACKAGE_VERSION } from './sdk-version';
import { SUBAGENT_BRIDGE_POLICY_VERSION } from './subagent-bridge';
import { HARNESS_TOOL_REGISTRY_VERSION } from './tool-descriptor';
import type { HarnessRuntimeFingerprint } from './types';

export const HARNESS_RUNTIME_FINGERPRINT_SCHEMA_VERSION = 'harness-runtime-fingerprint.v1';

function sha256Hex(value: string): string {
  return createHash('sha256').update(value).digest('hex');
}

export function buildHarnessRuntimeFingerprint(): HarnessRuntimeFingerprint {
  const fingerprintInput = {
    schemaVersion: HARNESS_RUNTIME_FINGERPRINT_SCHEMA_VERSION,
    personaComposerVersion: PERSONA_COMPOSER_VERSION,
    permissionPolicyVersion: HARNESS_PERMISSION_POLICY_VERSION,
    subagentPolicyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
    toolRegistryVersion: HARNESS_TOOL_REGISTRY_VERSION,
    sdkPackageVersion: CLAUDE_AGENT_SDK_PACKAGE_VERSION,
    mcpServers: [
      {
        name: CHIRALITY_MCP_SERVER_NAME,
        version: CHIRALITY_MCP_SERVER_VERSION,
        toolNames: [...CHIRALITY_MCP_TOOL_NAMES]
      }
    ]
  };

  return {
    ...fingerprintInput,
    fingerprintSha256: sha256Hex(JSON.stringify(fingerprintInput))
  };
}
