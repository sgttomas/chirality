import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

const WORKFLOW_PATH = path.resolve(
  process.cwd(),
  '..',
  '..',
  '..',
  '.github',
  'workflows',
  'harness-premerge.yml'
);

describe('repo-root harness premerge workflow', () => {
  it('enforces the ORN-01 gate set on pull requests without provider secrets', async () => {
    const workflow = await readFile(WORKFLOW_PATH, 'utf8');

    expect(workflow).toContain('pull_request:');
    expect(workflow).toContain('CHIRALITY_HARNESS_PROVIDER: stub');
    expect(workflow).toContain('HARNESS_PROJECT_ROOT: ${{ runner.temp }}/chirality-harness-workroot');
    expect(workflow).toContain('mkdir -p "${HARNESS_PROJECT_ROOT}"');
    expect(workflow).toContain('run: npm run typecheck');
    expect(workflow).toContain('run: npm run test -- --testTimeout=60000');
    expect(workflow).toContain('npm run instruction-root:integrity --');
    expect(workflow).toContain('run: npm run validate:release-quality');
    expect(workflow).toContain('artifacts/harness/section8/latest/summary.json');
    expect(workflow).toContain('artifacts/harness/release-quality/latest/summary.json');
    expect(workflow).toContain('artifacts/harness/instruction-root-integrity/latest/summary.json');
    expect(workflow).not.toContain('secrets.ANTHROPIC_API_KEY');
    expect(workflow).not.toContain('command -v claude');
  });
});
