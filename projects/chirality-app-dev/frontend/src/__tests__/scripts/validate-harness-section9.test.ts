import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

const MANIFEST_PATH = path.resolve(process.cwd(), 'scripts', 'harness-section9-manifest.json');

const REQUIRED_IDS = [
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

type ManifestCheck = {
  id: string;
  sourceReferences: string[];
  testFiles: string[];
  evidenceFiles: string[];
  warnings: string[];
  blockers: string[];
};

describe('Section 9 governed manifest', () => {
  it('pins the exact source-defined inventory and review metadata', async () => {
    const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as {
      schemaVersion: number;
      checks: ManifestCheck[];
    };

    expect(manifest.schemaVersion).toBe(1);
    expect(manifest.checks.map((check) => check.id)).toEqual(REQUIRED_IDS);
    for (const check of manifest.checks) {
      expect(check.sourceReferences.length).toBeGreaterThan(0);
      expect(check.testFiles.length).toBeGreaterThan(0);
      expect(check.evidenceFiles.length).toBeGreaterThan(0);
      expect(Array.isArray(check.warnings)).toBe(true);
      expect(Array.isArray(check.blockers)).toBe(true);
    }
  });

  // The runner/wrapper substring pins ("emits the stable manifest and makes
  // the release-quality wrapper validate it") moved to the consolidated
  // src/__tests__/contract-pins.manifest.ts (checked by contract-pins.test.ts).
});
