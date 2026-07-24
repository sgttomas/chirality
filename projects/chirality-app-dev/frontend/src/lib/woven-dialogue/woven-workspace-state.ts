import type { CoordinationPanelView } from './contracts';

export const WOVEN_WORKSPACE_STORAGE_KEY = 'chirality.wovenWorkspace.v1';
export const WOVEN_WORKSPACE_SCHEMA = 'chirality.woven-workspace/v1';

const LEGACY_LAYOUT_STORAGE_KEY = 'chirality.layout.v1';
const MIN_NAVIGATOR_WIDTH = 220;
const MAX_PANE_SIZE = 2000;
const MAX_REFERENCE_COUNT = 200;
const MAX_REFERENCE_LENGTH = 2048;

type WovenWorkspaceMigrationField = 'navigatorWidth' | 'navigatorCollapsed';

export type WovenWorkspaceState = {
  schema: typeof WOVEN_WORKSPACE_SCHEMA;
  navigatorWidth: number;
  coordinationWidth: number;
  activityHeight: number;
  navigatorCollapsed: boolean;
  coordinationCollapsed: boolean;
  activityCollapsed: boolean;
  coordinationView: CoordinationPanelView;
  dialogueAnchorId: string | null;
  focusedArtifact: {
    artifactReference: string;
    dialogueAnchorId: string;
  } | null;
  expandedObjectIds: string[];
  selectedReplaySessionId: string | null;
  contextReferences: string[];
  migration: {
    sourceKey: typeof LEGACY_LAYOUT_STORAGE_KEY | null;
    mappedFields: WovenWorkspaceMigrationField[];
  };
};

type WovenWorkspaceStorage = Pick<Storage, 'getItem' | 'setItem'>;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function clampNumber(value: unknown, fallback: number, minimum: number): number {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    return fallback;
  }
  return Math.max(minimum, Math.min(MAX_PANE_SIZE, value));
}

function readBoolean(value: unknown, fallback: boolean): boolean {
  return typeof value === 'boolean' ? value : fallback;
}

function readReference(value: unknown): string | null {
  if (typeof value !== 'string') {
    return null;
  }
  const reference = value.trim();
  if (!reference) {
    return null;
  }
  return reference.slice(0, MAX_REFERENCE_LENGTH);
}

function readReferenceArray(value: unknown): string[] {
  if (!Array.isArray(value)) {
    return [];
  }

  const references = new Set<string>();
  for (const entry of value) {
    const reference = readReference(entry);
    if (reference) {
      references.add(reference);
    }
    if (references.size >= MAX_REFERENCE_COUNT) {
      break;
    }
  }
  return [...references];
}

function readCoordinationView(value: unknown): CoordinationPanelView {
  return value === 'agents' ? 'agents' : 'work';
}

function readFocusedArtifact(
  value: unknown
): WovenWorkspaceState['focusedArtifact'] {
  if (!isRecord(value)) {
    return null;
  }
  const artifactReference = readReference(value.artifactReference);
  const dialogueAnchorId = readReference(value.dialogueAnchorId);
  if (!artifactReference || !dialogueAnchorId) {
    return null;
  }
  return {
    artifactReference,
    dialogueAnchorId
  };
}

function readMigration(value: unknown): WovenWorkspaceState['migration'] {
  if (!isRecord(value)) {
    return {
      sourceKey: null,
      mappedFields: []
    };
  }

  const rawFields = Array.isArray(value.mappedFields) ? value.mappedFields : [];
  const mappedFields = rawFields.filter(
    (field): field is WovenWorkspaceMigrationField =>
      field === 'navigatorWidth' || field === 'navigatorCollapsed'
  );

  return {
    sourceKey:
      value.sourceKey === LEGACY_LAYOUT_STORAGE_KEY
        ? LEGACY_LAYOUT_STORAGE_KEY
        : null,
    mappedFields: [...new Set(mappedFields)]
  };
}

export function createDefaultWovenWorkspaceState(): WovenWorkspaceState {
  return {
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
  };
}

export function clearProjectScopedWovenWorkspaceState(
  state: WovenWorkspaceState
): WovenWorkspaceState {
  return {
    ...state,
    dialogueAnchorId: null,
    focusedArtifact: null,
    expandedObjectIds: [],
    selectedReplaySessionId: null,
    contextReferences: []
  };
}

function sanitizeWovenWorkspaceState(value: unknown): WovenWorkspaceState | null {
  if (!isRecord(value) || value.schema !== WOVEN_WORKSPACE_SCHEMA) {
    return null;
  }

  const fallback = createDefaultWovenWorkspaceState();
  return {
    schema: WOVEN_WORKSPACE_SCHEMA,
    navigatorWidth: clampNumber(
      value.navigatorWidth,
      fallback.navigatorWidth,
      MIN_NAVIGATOR_WIDTH
    ),
    coordinationWidth: clampNumber(
      value.coordinationWidth,
      fallback.coordinationWidth,
      240
    ),
    activityHeight: clampNumber(value.activityHeight, fallback.activityHeight, 120),
    navigatorCollapsed: readBoolean(
      value.navigatorCollapsed,
      fallback.navigatorCollapsed
    ),
    coordinationCollapsed: readBoolean(
      value.coordinationCollapsed,
      fallback.coordinationCollapsed
    ),
    activityCollapsed: readBoolean(
      value.activityCollapsed,
      fallback.activityCollapsed
    ),
    coordinationView: readCoordinationView(value.coordinationView),
    dialogueAnchorId: readReference(value.dialogueAnchorId),
    focusedArtifact: readFocusedArtifact(value.focusedArtifact),
    expandedObjectIds: readReferenceArray(value.expandedObjectIds),
    selectedReplaySessionId: readReference(value.selectedReplaySessionId),
    contextReferences: readReferenceArray(value.contextReferences),
    migration: readMigration(value.migration)
  };
}

function migrateLegacyLayout(raw: string | null): WovenWorkspaceState {
  const state = createDefaultWovenWorkspaceState();
  if (!raw) {
    return state;
  }

  try {
    const parsed = JSON.parse(raw) as unknown;
    if (!isRecord(parsed)) {
      return state;
    }

    const widths = isRecord(parsed.widths) ? parsed.widths : {};
    const collapsed = isRecord(parsed.collapsed) ? parsed.collapsed : {};
    const mappedFields: WovenWorkspaceMigrationField[] = [];

    if (typeof widths.fileTree === 'number' && Number.isFinite(widths.fileTree)) {
      state.navigatorWidth = clampNumber(
        widths.fileTree,
        state.navigatorWidth,
        MIN_NAVIGATOR_WIDTH
      );
      mappedFields.push('navigatorWidth');
    }

    if (typeof collapsed.fileTree === 'boolean') {
      state.navigatorCollapsed = collapsed.fileTree;
      mappedFields.push('navigatorCollapsed');
    }

    if (mappedFields.length > 0) {
      state.migration = {
        sourceKey: LEGACY_LAYOUT_STORAGE_KEY,
        mappedFields
      };
    }
    return state;
  } catch {
    return state;
  }
}

export function readWovenWorkspaceStateFromStorage(
  storage: WovenWorkspaceStorage | undefined
): WovenWorkspaceState {
  if (!storage) {
    return createDefaultWovenWorkspaceState();
  }

  try {
    const currentRaw = storage.getItem(WOVEN_WORKSPACE_STORAGE_KEY);
    if (currentRaw) {
      try {
        const current = sanitizeWovenWorkspaceState(JSON.parse(currentRaw));
        if (current) {
          return current;
        }
      } catch {
        // Fall through to a non-destructive legacy migration/default recovery.
      }
    }

    const migrated = migrateLegacyLayout(storage.getItem(LEGACY_LAYOUT_STORAGE_KEY));
    writeWovenWorkspaceStateToStorage(storage, migrated);
    return migrated;
  } catch {
    return createDefaultWovenWorkspaceState();
  }
}

export function writeWovenWorkspaceStateToStorage(
  storage: Pick<Storage, 'setItem'> | undefined,
  state: WovenWorkspaceState
): void {
  if (!storage) {
    return;
  }

  const sanitized = sanitizeWovenWorkspaceState(state);
  if (!sanitized) {
    return;
  }

  try {
    storage.setItem(WOVEN_WORKSPACE_STORAGE_KEY, JSON.stringify(sanitized));
  } catch {
    // Workspace presentation state is optional convenience state.
  }
}
