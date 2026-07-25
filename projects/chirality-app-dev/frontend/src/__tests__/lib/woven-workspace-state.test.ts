import { describe, expect, it, vi } from 'vitest';
import {
  MAX_SESSION_SURFACE_ATTRIBUTIONS,
  WOVEN_WORKSPACE_SCHEMA,
  WOVEN_WORKSPACE_STORAGE_KEY,
  clearProjectScopedWovenWorkspaceState,
  createDefaultWovenWorkspaceState,
  readWovenWorkspaceStateFromStorage,
  recordWovenSessionSurface,
  toggleWovenNavigatorExpandedSurface,
  writeWovenWorkspaceStateToStorage,
  writeWovenWorkspaceThemeToStorage
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
      theme: 'light',
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
      sessionSurfaces: {},
      navigatorExpandedSurfaces: ['dialogue'],
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
  it('defaults the theme to light and keeps stored v1 blobs loadable', () => {
    const legacyBlob = {
      ...createDefaultWovenWorkspaceState(),
      navigatorWidth: 340
    } as Record<string, unknown>;
    delete legacyBlob.theme;

    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY ? JSON.stringify(legacyBlob) : null
      ),
      setItem: vi.fn()
    };

    const state = readWovenWorkspaceStateFromStorage(storage);

    expect(state.theme).toBe('light');
    expect(state.navigatorWidth).toBe(340);
    expect(state.schema).toBe(WOVEN_WORKSPACE_SCHEMA);
  });

  it('falls back to light for an unrecognised stored theme', () => {
    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY
          ? JSON.stringify({ ...createDefaultWovenWorkspaceState(), theme: 'sepia' })
          : null
      ),
      setItem: vi.fn()
    };

    expect(readWovenWorkspaceStateFromStorage(storage).theme).toBe('light');
  });

  it('persists a chosen theme without bumping the schema string', () => {
    const store = new Map<string, string>();
    const storage = {
      getItem: (key: string) => store.get(key) ?? null,
      setItem: (key: string, value: string) => {
        store.set(key, value);
      }
    };

    writeWovenWorkspaceThemeToStorage(storage, 'dark');

    const persisted = JSON.parse(
      store.get(WOVEN_WORKSPACE_STORAGE_KEY) as string
    ) as Record<string, unknown>;
    expect(persisted.theme).toBe('dark');
    expect(persisted.schema).toBe(WOVEN_WORKSPACE_SCHEMA);
    expect(readWovenWorkspaceStateFromStorage(storage).theme).toBe('dark');
  });

  it('keeps stored v1 blobs loadable when the navigator fields are absent', () => {
    const legacyBlob = {
      ...createDefaultWovenWorkspaceState(),
      navigatorWidth: 340
    } as Record<string, unknown>;
    delete legacyBlob.sessionSurfaces;
    delete legacyBlob.navigatorExpandedSurfaces;

    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY ? JSON.stringify(legacyBlob) : null
      ),
      setItem: vi.fn()
    };

    const state = readWovenWorkspaceStateFromStorage(storage);

    expect(state.schema).toBe(WOVEN_WORKSPACE_SCHEMA);
    expect(state.sessionSurfaces).toEqual({});
    expect(state.navigatorExpandedSurfaces).toEqual(['dialogue']);
    expect(state.navigatorWidth).toBe(340);
  });

  it('drops unrecognised session attributions and keeps an empty expansion set', () => {
    const stored = {
      ...createDefaultWovenWorkspaceState(),
      sessionSurfaces: {
        'session-a': 'workbench',
        'session-b': 'document',
        'session-c': 42,
        '   ': 'dialogue'
      },
      navigatorExpandedSurfaces: ['pipeline', 'pipeline', 'document', 7]
    };
    const storage = {
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY ? JSON.stringify(stored) : null
      ),
      setItem: vi.fn()
    };

    const state = readWovenWorkspaceStateFromStorage(storage);

    expect(state.sessionSurfaces).toEqual({ 'session-a': 'workbench' });
    expect(state.navigatorExpandedSurfaces).toEqual(['pipeline']);

    const collapsed = readWovenWorkspaceStateFromStorage({
      getItem: vi.fn((key: string) =>
        key === WOVEN_WORKSPACE_STORAGE_KEY
          ? JSON.stringify({
              ...createDefaultWovenWorkspaceState(),
              navigatorExpandedSurfaces: []
            })
          : null
      ),
      setItem: vi.fn()
    });

    expect(collapsed.navigatorExpandedSurfaces).toEqual([]);
  });

  it('records the first surface a session was observed on and never retags it', () => {
    const state = createDefaultWovenWorkspaceState();

    const tagged = recordWovenSessionSurface(state, ' session-a ', 'pipeline');
    expect(tagged.sessionSurfaces).toEqual({ 'session-a': 'pipeline' });

    const retagged = recordWovenSessionSurface(tagged, 'session-a', 'dialogue');
    expect(retagged).toBe(tagged);

    expect(recordWovenSessionSurface(state, '   ', 'dialogue')).toBe(state);
    expect(recordWovenSessionSurface(state, undefined, 'dialogue')).toBe(state);
  });

  it('evicts the oldest attributions beyond the bounded map size', () => {
    let state = createDefaultWovenWorkspaceState();
    for (let index = 0; index < MAX_SESSION_SURFACE_ATTRIBUTIONS + 3; index += 1) {
      state = recordWovenSessionSurface(state, `session-${index}`, 'dialogue');
    }

    const sessionIds = Object.keys(state.sessionSurfaces);
    expect(sessionIds).toHaveLength(MAX_SESSION_SURFACE_ATTRIBUTIONS);
    expect(sessionIds).not.toContain('session-0');
    expect(sessionIds).not.toContain('session-2');
    expect(sessionIds[0]).toBe('session-3');
    expect(sessionIds[sessionIds.length - 1]).toBe(
      `session-${MAX_SESSION_SURFACE_ATTRIBUTIONS + 2}`
    );
  });

  it('round-trips the navigator fields through storage without a schema bump', () => {
    const store = new Map<string, string>();
    const storage = {
      getItem: (key: string) => store.get(key) ?? null,
      setItem: (key: string, value: string) => {
        store.set(key, value);
      }
    };
    const state = recordWovenSessionSurface(
      {
        ...createDefaultWovenWorkspaceState(),
        navigatorExpandedSurfaces: ['workbench']
      },
      'session-a',
      'workbench'
    );

    writeWovenWorkspaceStateToStorage(storage, state);
    const persisted = JSON.parse(
      store.get(WOVEN_WORKSPACE_STORAGE_KEY) as string
    ) as Record<string, unknown>;

    expect(persisted.schema).toBe(WOVEN_WORKSPACE_SCHEMA);
    expect(persisted.sessionSurfaces).toEqual({ 'session-a': 'workbench' });
    expect(readWovenWorkspaceStateFromStorage(storage)).toEqual(state);
  });

  it('toggles a navigator mode group without disturbing the others', () => {
    const state = createDefaultWovenWorkspaceState();

    const expanded = toggleWovenNavigatorExpandedSurface(state, 'pipeline');
    expect(expanded.navigatorExpandedSurfaces).toEqual(['dialogue', 'pipeline']);

    const collapsed = toggleWovenNavigatorExpandedSurface(expanded, 'dialogue');
    expect(collapsed.navigatorExpandedSurfaces).toEqual(['pipeline']);
  });

  it('keeps session attributions when project-scoped references are cleared', () => {
    const state = recordWovenSessionSurface(
      createDefaultWovenWorkspaceState(),
      'session-a',
      'workbench'
    );

    expect(clearProjectScopedWovenWorkspaceState(state)).toMatchObject({
      sessionSurfaces: { 'session-a': 'workbench' },
      navigatorExpandedSurfaces: ['dialogue'],
      selectedReplaySessionId: null
    });
  });

  it('never lets a stale layout snapshot revert the stored theme', () => {
    const store = new Map<string, string>();
    const storage = {
      getItem: (key: string) => store.get(key) ?? null,
      setItem: (key: string, value: string) => {
        store.set(key, value);
      }
    };
    const staleSnapshot = createDefaultWovenWorkspaceState();

    writeWovenWorkspaceThemeToStorage(storage, 'system');
    writeWovenWorkspaceStateToStorage(storage, {
      ...staleSnapshot,
      navigatorWidth: 300
    });

    const persisted = JSON.parse(
      store.get(WOVEN_WORKSPACE_STORAGE_KEY) as string
    ) as Record<string, unknown>;
    expect(persisted.theme).toBe('system');
    expect(persisted.navigatorWidth).toBe(300);
  });
});
