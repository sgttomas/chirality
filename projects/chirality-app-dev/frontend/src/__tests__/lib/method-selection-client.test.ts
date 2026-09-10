import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  getNativePlanCapability,
  exportNativePlanRevision,
  listMethods,
  replaceSelectedMethods,
  resolveSelectedContext
} from '../../lib/harness/method-selection-client';

afterEach(() => vi.unstubAllGlobals());

describe('Runtime method selection client', () => {
  it('reads the Runtime catalog without accepting method bodies from the caller', async () => {
    const response = { schemaVersion: 'chirality.methods/v3', methods: [], malformedPackages: [] };
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(response), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);

    await expect(listMethods('/tmp/project', 'setup')).resolves.toEqual(response);
    expect(fetchMock).toHaveBeenCalledWith('/api/harness/methods?projectRoot=%2Ftmp%2Fproject&query=setup', expect.objectContaining({ signal: undefined }));
  });

  it('preserves ordered source-qualified selections', async () => {
    const methods = [
      { kind: 'workflow', name: 'project-setup', source: 'project', sourceRootId: 'project-one' },
      { kind: 'skill', name: 'researcher', source: 'user', sourceRootId: 'user-one' }
    ] as const;
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      schemaVersion: 'chirality.selected-methods/v3', sessionId: 'sess-1', revision: 1, methods, basisPreview: {}
    }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);

    await replaceSelectedMethods('sess-1', methods, { expectedBasisId: 'basis-1', roleId: 'HELPS_HUMANS', boundaryConfirmed: true, selectionMode: 'merge' });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ methods, expectedBasisId: 'basis-1', roleId: 'HELPS_HUMANS', boundaryConfirmed: true, selectionMode: 'merge' });
  });

  it('omits methods for a role-only transition so the active selection is preserved', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ schemaVersion: 'chirality.selected-methods/v3' }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    await replaceSelectedMethods('sess-1', undefined, { roleId: 'WORKING_ITEMS', boundaryConfirmed: true });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ roleId: 'WORKING_ITEMS', boundaryConfirmed: true });
  });

  it('sends interaction and permission modes as independent fields', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ schemaVersion: 'chirality.selected-context/v3' }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    await resolveSelectedContext({ sessionId: 'sess-1', roleId: 'HELP_HUMAN', methods: [], interactionMode: 'native-plan', permissionMode: 'readOnly' });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ roleId: 'HELP_HUMAN', methods: [], interactionMode: 'native-plan', permissionMode: 'readOnly' });
  });

  it('reports Runtime native Plan Mode unavailability without a local fallback', async () => {
    const unavailable = { schemaVersion: 'chirality.native-plan-capability/v3', status: 'unavailable', reason: 'No qualified adapter' };
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify(unavailable), { status: 200 })));
    await expect(getNativePlanCapability('sess-1')).resolves.toEqual(unavailable);
  });

  it('exports a stored plan revision only to an explicit project-relative target', async () => {
    const response = { schemaVersion: 'chirality.native-plan-export/v3', sessionId: 'sess-1', revision: 2, targetRelativePath: 'plans/plan.md', sha256: 'a'.repeat(64) };
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(response), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    await expect(exportNativePlanRevision({ sessionId: 'sess-1', revision: 2, targetRelativePath: 'plans/plan.md' })).resolves.toEqual(response);
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({ revision: 2, targetRelativePath: 'plans/plan.md' });
  });
});
