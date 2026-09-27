import { mkdtemp, mkdir, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

/*
 * Route test for GET /api/working-root/deliverable/content, the read route the
 * document viewer uses. SCA-APP-011 retired the status, transition and
 * dependency routes; their cases moved to the library-level test
 * `__tests__/lib/deliverable-contracts.test.ts`.
 */

type RouteModules = {
  contentRoute: typeof import('../../../app/api/working-root/deliverable/content/route');
};

type FixtureContext = {
  tmpRoot: string;
  projectRoot: string;
  deliverablePath: string;
  statusFilePath: string;
};

const INITIAL_STATUS = `# Status: DEL-05-03 Lifecycle State Handling

**Current State:** INITIALIZED
**Last Updated:** 2026-02-22

## History
- 2026-02-21 - State set to OPEN (PREPARATION)
- 2026-02-22 - State set to INITIALIZED (4_DOCUMENTS)
`;

let fixture: FixtureContext;

async function importRouteModules(): Promise<RouteModules> {
  vi.resetModules();
  const contentRoute = await import('../../../app/api/working-root/deliverable/content/route');
  return { contentRoute };
}

function contentRequest(
  projectRoot: string,
  deliverablePath: string,
  file?: string
): Request {
  const params = new URLSearchParams({ projectRoot, deliverablePath });
  if (file !== undefined) {
    params.set('file', file);
  }
  return new Request(`http://localhost/api/working-root/deliverable/content?${params.toString()}`);
}

beforeEach(async () => {
  const tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-working-root-content-'));
  const projectRoot = path.join(tmpRoot, 'project-root');
  const deliverablePath = path.join(
    projectRoot,
    'execution',
    'PKG-05_Filesystem_Execution_Model',
    '1_Working',
    'DEL-05-03_Lifecycle_State_Handling'
  );
  const statusFilePath = path.join(deliverablePath, '_STATUS.md');

  await mkdir(deliverablePath, { recursive: true });
  await writeFile(statusFilePath, INITIAL_STATUS, 'utf8');

  fixture = {
    tmpRoot,
    projectRoot,
    deliverablePath,
    statusFilePath
  };
});

afterEach(async () => {
  await rm(fixture.tmpRoot, { recursive: true, force: true });
});

describe('working-root deliverable content route', () => {
  it('serves _STATUS.md content by default when no file is requested', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath)
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe('_STATUS.md');
    expect(body.content).toContain('**Current State:** INITIALIZED');
  });

  it('serves an explicit relative file within the deliverable', async () => {
    await writeFile(
      path.join(fixture.deliverablePath, 'Specification.md'),
      '# Spec\n\nThe body of the deliverable.\n',
      'utf8'
    );
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'Specification.md')
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe('Specification.md');
    expect(body.content).toContain('The body of the deliverable.');
  });

  it('rejects a file that traverses out of the deliverable directory', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '../_STATUS.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('rejects an absolute file path', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '/etc/hosts')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('returns 404 for a missing file in the deliverable', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'Datasheet.md')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });

  it('rejects a symlinked file that resolves outside the deliverable', async () => {
    const externalSecret = path.join(fixture.tmpRoot, 'outside-secret.md');
    await writeFile(externalSecret, '# Secret\n\nshould never be served.\n', 'utf8');
    const escapingLink = path.join(fixture.deliverablePath, 'escape.md');
    await symlink(externalSecret, escapingLink);

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'escape.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('rejects a file reached through a symlinked directory component that escapes', async () => {
    // The escape is via an intermediate directory symlink, not a leaf-file symlink:
    // the post-realpath containment re-check must catch mid-path symlink resolution.
    const externalDir = path.join(fixture.tmpRoot, 'outside-dir');
    await mkdir(externalDir, { recursive: true });
    await writeFile(path.join(externalDir, 'Spec.md'), '# External\n\nleaked.\n', 'utf8');
    await symlink(externalDir, path.join(fixture.deliverablePath, 'linkdir'));

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'linkdir/Spec.md')
    );

    expect(response.status).toBe(400);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_FILE_OUTSIDE_DELIVERABLE' }
    });
  });

  it('serves a valid file nested in a subdirectory and reports its relative path', async () => {
    await mkdir(path.join(fixture.deliverablePath, 'attachments'), { recursive: true });
    await writeFile(
      path.join(fixture.deliverablePath, 'attachments', 'diagram.md'),
      '# Diagram\n\nnested body.\n',
      'utf8'
    );

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'attachments/diagram.md')
    );

    expect(response.status).toBe(200);
    const body = (await response.json()) as { content: string; file: string };
    expect(body.file).toBe(path.join('attachments', 'diagram.md'));
    expect(body.content).toContain('nested body.');
  });

  it('returns 404 when the requested file is the deliverable directory itself', async () => {
    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, '.')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });

  it('returns 404 when the requested file is a subdirectory, not a regular file', async () => {
    await mkdir(path.join(fixture.deliverablePath, 'subdir'), { recursive: true });

    const routes = await importRouteModules();
    const response = await routes.contentRoute.GET(
      contentRequest(fixture.projectRoot, fixture.deliverablePath, 'subdir')
    );

    expect(response.status).toBe(404);
    expect(await response.json()).toMatchObject({
      error: { type: 'DELIVERABLE_CONTENT_NOT_FOUND' }
    });
  });
});
