import type { EngineSelection, SessionRecord } from "./harness/types.js";
import type { HarnessOpts } from "./harness/types.js";
import type {
  ChiralityRoleName,
  MethodReference,
  QualifiedMethodReference
} from "./v3.js";

export interface RuntimeSessionRecord extends SessionRecord {
  schemaVersion: "chirality.session/v2" | "chirality.session/v3";
  projectId: string;
  projectRoot: string;
  sessionId: string;
  createdAt: string;
  updatedAt: string;
  role: "agent0" | "agent1" | "agent2";
  roleId?: ChiralityRoleName;
  interactionMode?: "chat" | "native-plan";
  permissionMode?: "readOnly" | "ask" | "workspaceWrite" | "bypass";
  selectedMethods?: readonly QualifiedMethodReference[];
  methodSelectionRevision?: number;
  instructionBasisId?: string;
  parentSessionId?: string;
  engineSelection: EngineSelection;
  engineSessionId?: string;
  residencyEpoch?: string;
  status: "idle" | "running" | "completed" | "failed" | "interrupted";
  legacy?: {
    sourcePath: string;
    migratedAt: string;
  };
}

/** Additive v3 reader shape; v2 records remain accepted during migration. */
export interface RuntimeSessionRecordV3 extends Omit<RuntimeSessionRecord, "schemaVersion" | "roleId" | "interactionMode" | "permissionMode" | "selectedMethods" | "methodSelectionRevision" | "instructionBasisId"> {
  schemaVersion: "chirality.session/v3";
  roleId: ChiralityRoleName;
  agentType: 0 | 1 | 2;
  interactionMode: "chat" | "native-plan";
  permissionMode: "readOnly" | "ask" | "workspaceWrite" | "bypass";
  selectedMethods: readonly QualifiedMethodReference[];
  methodSelectionRevision: number;
  instructionBasisId: string;
}

export type ReadableRuntimeSessionRecord = RuntimeSessionRecord | RuntimeSessionRecordV3;

export interface CreateSessionRequest {
  projectId: string;
  role?: RuntimeSessionRecord["role"];
  roleId?: ChiralityRoleName;
  interactionMode?: "chat" | "native-plan";
  permissionMode?: "readOnly" | "ask" | "workspaceWrite" | "bypass";
  selectedMethods?: readonly MethodReference[];
  engineSelection?: EngineSelection;
  persona?: string;
  mode?: string;
  parentSessionId?: string;
  approvalRef?: string;
  declaredContext?: string[];
  allowedWriteTargets?: string[];
}

export interface SessionTurnRequest {
  message?: string;
  prompt?: string;
  opts?: HarnessOpts;
  attachments?: string[];
  turnId?: string;
  interactionMode?: "chat" | "native-plan";
  permissionMode?: "readOnly" | "ask" | "workspaceWrite" | "bypass";
  methods?: readonly MethodReference[];
  /** Compatibility selector normalized through the legacy method adapter. */
  workflow?: string;
  /** Legacy compatibility selector; accepted only through convertedWorkflowAliases. */
  taskSkill?: string;
}
