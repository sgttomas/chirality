import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it } from 'vitest';
import {
  DOMAIN_ENGINE_PROFILE_REGISTRY,
  listRegisteredDomainProfileIds,
  resolveDomainEngineProfile
} from '../../lib/harness/mcp/domain-profile-registry';

const REGISTRY_MODULE_PATH = path.resolve(
  process.cwd(),
  'src',
  'lib',
  'harness',
  'mcp',
  'domain-profile-registry.ts'
);
const READ_TOOLS_MODULE_PATH = path.resolve(
  process.cwd(),
  'src',
  'lib',
  'harness',
  'mcp',
  'read-tools.ts'
);

async function directoryExists(candidate: string): Promise<boolean> {
  try {
    return (await stat(candidate)).isDirectory();
  } catch {
    return false;
  }
}

/**
 * Walks up from the frontend working directory until a `_DomainEngines/profiles/`
 * directory is found (the chirality monorepo root). Returns null when the test
 * run is not hosted in the monorepo.
 */
async function findMonorepoProfilesDirectory(): Promise<string | null> {
  let current = process.cwd();
  for (;;) {
    const candidate = path.join(current, '_DomainEngines', 'profiles');
    if (await directoryExists(candidate)) {
      return candidate;
    }
    const parent = path.dirname(current);
    if (parent === current) {
      return null;
    }
    current = parent;
  }
}

describe('D-APP-51 domain engine profile registry', () => {
  it('is closed to exactly the two ruled profileIds and records the separate headless binding', () => {
    expect(listRegisteredDomainProfileIds()).toEqual(['open_pipe_stress', 'pec']);
    expect(DOMAIN_ENGINE_PROFILE_REGISTRY).toHaveLength(2);
    for (const entry of DOMAIN_ENGINE_PROFILE_REGISTRY) {
      expect(entry.readTransportBinding).toBe('in-process-read-evidence');
    }
    expect(resolveDomainEngineProfile('open_pipe_stress')).toMatchObject({
      profileRelativePath: '_DomainEngines/profiles/open_pipe_stress.yaml',
      engineKind: 'deterministic-cli',
      headlessPreviewTransportBinding: 'configured-local-process',
      identityMarker: 'id: "open_pipe_stress"',
      toolGate: {
        completeness_checker: {
          requiredMarker: '- id: "completeness_checker"',
          declaredDeterministicToolId: 'completeness_checker'
        },
        rule_check_runner: {
          requiredMarker: '- id: "rule_check_runner"',
          declaredDeterministicToolId: 'rule_check_runner'
        },
        headless_runner: {
          requiredMarker: '- id: "headless_runner"',
          declaredDeterministicToolId: 'headless_runner'
        }
      }
    });
    expect(resolveDomainEngineProfile('pec')).toMatchObject({
      profileRelativePath: '_DomainEngines/profiles/pec.yaml',
      engineKind: 'http-api',
      identityMarker: 'id: "pec"',
      toolGate: {
        completeness_checker: {
          requiredMarker: null,
          declaredDeterministicToolId: null
        },
        rule_check_runner: {
          requiredMarker: null,
          declaredDeterministicToolId: null
        },
        headless_runner: {
          requiredMarker: null,
          declaredDeterministicToolId: null
        }
      }
    });
  });

  it('refuses unregistered profileIds with the unchanged refusal contract', () => {
    let caught: unknown;
    try {
      resolveDomainEngineProfile('unregistered_engine');
    } catch (error) {
      caught = error;
    }
    expect(caught).toMatchObject({
      name: 'HarnessError',
      type: 'INVALID_REQUEST',
      status: 400,
      message: 'profileId is not registered for this domain transport',
      details: {
        profileId: 'unregistered_engine',
        supportedProfileIds: ['open_pipe_stress', 'pec']
      }
    });
  });

  it('imports no network or child-process capability in the registry or read-tools modules', async () => {
    const forbiddenModuleSpecifiers = [
      'node:http',
      'node:https',
      'node:net',
      'node:tls',
      'node:dgram',
      'node:child_process',
      'child_process',
      'undici',
      'axios',
      'node-fetch'
    ];
    for (const modulePath of [REGISTRY_MODULE_PATH, READ_TOOLS_MODULE_PATH]) {
      const source = await readFile(modulePath, 'utf8');
      for (const specifier of forbiddenModuleSpecifiers) {
        expect(source).not.toContain(`'${specifier}'`);
        expect(source).not.toContain(`"${specifier}"`);
      }
      expect(source).not.toMatch(/\bfetch\s*\(/);
      expect(source).not.toMatch(/require\s*\(\s*['"](?:node:)?(?:http|https|net|child_process)['"]\s*\)/);
    }
  });

  // Thin live-profile marker-sync guard (D-APP-51 impl-plan test 2.2): the
  // vendored fixtures in chirality-read-mcp.test.ts are the primary, hermetic
  // pin; this single guard additionally asserts the registry's marker byte
  // strings against the LIVE _DomainEngines/profiles/*.yaml files so fixture
  // drift can never mask a V-9-class defect again. It FAILS (not skips) when
  // the live profiles are present but a marker is absent; it skips, with a
  // logged reason, only when the monorepo root is not present at all.
  it('keeps every registry marker byte string in sync with the live profile files', async (ctx) => {
    const profilesDirectory = await findMonorepoProfilesDirectory();
    if (profilesDirectory === null) {
      console.warn(
        'domain-profile-registry marker-sync guard skipped: no _DomainEngines/profiles/ directory found above',
        process.cwd()
      );
      ctx.skip();
      return;
    }

    for (const entry of DOMAIN_ENGINE_PROFILE_REGISTRY) {
      const liveProfilePath = path.join(profilesDirectory, `${entry.profileId}.yaml`);
      const content = await readFile(liveProfilePath, 'utf8');
      expect(content, `${liveProfilePath} must contain identity marker ${entry.identityMarker}`).toContain(
        entry.identityMarker
      );
      for (const [toolId, gate] of Object.entries(entry.toolGate)) {
        if (gate.requiredMarker !== null) {
          expect(
            content,
            `${liveProfilePath} must contain ${toolId} marker ${gate.requiredMarker}`
          ).toContain(gate.requiredMarker);
        }
      }
    }
  });
});
