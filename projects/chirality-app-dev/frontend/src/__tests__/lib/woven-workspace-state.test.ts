import { describe, expect, it, vi } from 'vitest';
import {
  WOVEN_WORKSPACE_SCHEMA,
  WOVEN_WORKSPACE_STORAGE_KEY,
  clearProjectScopedWovenWorkspaceState,
  createDefaultWovenWorkspaceState,
  readWovenWorkspaceStateFromStorage,
  writeWovenWorkspaceStateToStorage
} from '../../lib/woven-dialogue/woven-workspace-state';

describe('Woven Dialogue workspace state', () => {
  it('clears project references without changing global layout preferences', () => {
    const state = {
      ...createDefaultWovenWorkspaceState(),
      navigatorWidth: 412,
      coordinationView: 'agents' as const,
      dialogueAnchorId: 'turn-1',
      focusedArtifact: {
        artifactReference: 'project-a/report.md',
        dialogueAnchorId: 'turn-1'
      },
      expandedObjectIds: ['project-a/report.md'],
      selectedReplaySessionId: 'session-a',
      contextReferences: ['project-a/context.md']
    };

    expect(clearProjectScopedWovenWorkspaceState(state)).toMatchObject({
      navigatorWidth: 412,
      coordinationView: 'agents',
      dialogueAnchorId: null,
      focusedArtifact: null,
      expandedObjectIds: [],
      selectedReplaySessionId: null,
      contextReferences: []
    });
  });

  it('creates reference-only defaults for the new versioned schema', () => {
    expect(createDefaultWovenWorkspaceState()).toEqual({
      schema: WOVEN_WORKSPACE_SCHEMA,
      navigatorWidth: 280,
      coordinationWidth: 360,
      activityHeight: 220,
      navigatorCollapsed: false,
      coordinationCollapsed: false,
      activityCollapsed: true,
      coordinationView: 'work',
      dialogueAnchorId: null,
      focusedArtifact: null,
      expandedObjectIds: [],
      selectedReplaySessionId: null,
      contextReferences: [],
      migration: {
        sourceKey: null,
        mappedFields: []
      }
    });
  });

  it('migrates only legacy file-tree geometry and leaves the legacy key untouched', () => {
    const legacyRaw = JSON.stringify({
      widths: {
        fileTree: 432,
        toolkit: 901,
        chat: 902
      },
      collapsed: {
        fileTree: true,
        toolkit: true,
        chat: true
      },
      authoritativePlan: {
        status: 'ACCEPTED'
      }
    });
    const setItem = vi.fn();
    const storage = {
      getItem: vi.fn((key: string) =>
        key === 'chirality.layout.v1' ? legacyRaw : null
      ),
      setItem
    };

    const state = readWovenWorkspaceStateFromStorage(storage);

    expect(state.navigatorWidth).toBe(432);
    expect(state.navigatorCollapsed).toBe(true);
    expect(state.coordinationWidth).toBe(360);
    expect(state.coordinationCollapsed).toBe(false);
    expect(state.activityHeight).toBe(220);
    expect(state.activityCollapsed).toBe(true);
    expect(state.migration).toEqual({
      sourceKey: 'chirality.layout.v1',
      mappedFields: ['navigatorWidth', 'navigatorCollapsed']
    });
    expect(state).not.toHaveProperty('authoritativePlan');
    expect(setItem).toHaveBeenCalledTimes(1);
    expect(setItem).toHaveBeenCalledWith(
      WOVEN_WORKSPACE_STORAGE_KEY,
      JSON.stringify(state)
    );
    expect(storage.getItem('chirality.layout.v1')).toBe(legacyRaw);
  });

  it('reads and sanitizes a current workspace state without rerunning migration', () => {
    const current = {
      ...createDefaultWovenWorkspaceState(),
      navigatorWidth: 510,
      coordinationView: 'agents',
      dialogueAnchorId: ' turn-17 ',
      expandedObjectIds: ['artifact-1', 'artifact-1', '', 42],
      contextReferences: [' docs/SPEC.md ', 'docs/SPEC.md'],
      selectedReplaySessionId: ' session-2 '
    };
    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY ? JSON.stringify(current) : null
      ),
      setItem: vi.fn()
    };

    const state = readWovenWorkspaceStateFromStorage(storage);

    expect(state.navigatorWidth).toBe(510);
    expect(state.coordinationView).toBe('agents');
    expect(state.dialogueAnchorId).toBe('turn-17');
    expect(state.expandedObjectIds).toEqual(['artifact-1']);
    expect(state.contextReferences).toEqual(['docs/SPEC.md']);
    expect(state.selectedReplaySessionId).toBe('session-2');
    expect(storage.setItem).not.toHaveBeenCalled();
    expect(storage.getItem).not.toHaveBeenCalledWith('chirality.layout.v1');
  });

  it('recovers from corrupt current and legacy state without throwing', () => {
    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY ? '{bad-current' : '{bad-legacy'
      ),
      setItem: vi.fn()
    };

    expect(readWovenWorkspaceStateFromStorage(storage)).toEqual(
      createDefaultWovenWorkspaceState()
    );
    expect(storage.setItem).toHaveBeenCalledWith(
      WOVEN_WORKSPACE_STORAGE_KEY,
      JSON.stringify(createDefaultWovenWorkspaceState())
    );
  });

  it('falls back to memory defaults when storage access fails', () => {
    const storage = {
      getItem: vi.fn(() => {
        throw new Error('storage unavailable');
      }),
      setItem: vi.fn()
    };

    expect(readWovenWorkspaceStateFromStorage(storage)).toEqual(
      createDefaultWovenWorkspaceState()
    );
    expect(storage.setItem).not.toHaveBeenCalled();
  });

  it('writes only the new key and ignores write failures', () => {
    const state = {
      ...createDefaultWovenWorkspaceState(),
      coordinationView: 'agents' as const,
      contextReferences: ['docs/SPEC.md']
    };
    const setItem = vi.fn();

    expect(() =>
      writeWovenWorkspaceStateToStorage({ setItem }, state)
    ).not.toThrow();
    expect(setItem).toHaveBeenCalledWith(
      WOVEN_WORKSPACE_STORAGE_KEY,
      JSON.stringify(state)
    );
    expect(setItem).not.toHaveBeenCalledWith(
      'chirality.layout.v1',
      expect.anything()
    );

    expect(() =>
      writeWovenWorkspaceStateToStorage(
        {
          setItem: () => {
            throw new Error('quota exceeded');
          }
        },
        state
      )
    ).not.toThrow();
  });
});
