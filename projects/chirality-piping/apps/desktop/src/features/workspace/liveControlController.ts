import type { EditorOperationIntent } from "../../types";
import { computeModelHash } from "../../services/hashService";
import { validateOperationBatch } from "../../services/operationBatchService";
import type { OperationBatch } from "../../services/operationBatchService";
import type { LiveAdmission, LiveBasis, LiveIdentity, LivePublication, LiveReceipt, LiveRequest, LiveResponse, LiveSnapshot } from "./liveControlTypes";
const copy = <T,>(value: T): T => structuredClone(value);
export const liveId = () => crypto.randomUUID();
function fail(code: string, message: string): never {
  throw {
    liveError: true,
    code,
    message,
    retryable: ["not_ready", "busy"].includes(code),
    next_action: "Inspect current state; for uncertain submit retry the original workspace, preview and idempotency key."
  };
}
function object(value: unknown, keys: string[]): Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value))
    fail("invalid_request", "Expected an object.");
  const record = value as Record<string, unknown>;
  if (Object.keys(record).some(k => !keys.includes(k)) || keys.some(k => !(k in record)))
    fail("invalid_request", "Unexpected or missing fields.");
  return record;
}
function string(value: unknown): string {
  if (typeof value !== "string" || !value.length)
    fail("invalid_request", "Expected a nonempty string.");
  return value;
}
type Preview = {
  admission: LiveAdmission;
  basis: LiveBasis;
  preview: string;
};
type Ticket = {
  preview: Preview;
  state: string;
  reason: string | null;
  receipt: LiveReceipt | null;
  published: boolean;
  cancelled: boolean;
  pending: Promise<unknown>;
  resolve: (v: unknown) => void;
  reject: (e: unknown) => void;
  applying?: boolean;
  observed?: LivePublication;
  hashing?: Promise<void>;
};
export type LiveHost = {
  busy?: () => boolean;
  snapshot: () => LiveSnapshot | null;
  enqueue: (admission: LiveAdmission) => void;
  remove: (token: string) => void;
};
/** Registry lifetime is the hook lifetime, never the project lifetime. No model store or Apply entry point. */
export class LiveControlController {
  readonly sessionId = liveId();
  private appId: string | null = null;
  private workspace = "";
  private generation = -1;
  private bases = new Map<string, {
    snapshot: LiveSnapshot;
    identity: LiveBasis;
  }>();
  private previewReservations = 0;
  private previews = new Map<string, Preview>();
  private keys = new Map<string, Ticket>();
  private tickets = new Map<string, Ticket>();
  private active = true;
  constructor(private host: LiveHost) {
  }
  bind(appId: string) {
    this.appId = appId;
    this.active = true;
  }
  retire() {
    this.active = false;
    for (const t of this.tickets.values())
      if (!t.published && !t.observed) {
        t.state = "outcome_unknown";
        t.reason = "controller_retired";
        t.resolve(this.result(t));
      }
  }
  private current() {
    const s = this.host.snapshot();
    if (!this.active || !this.appId || !s)
      fail("not_ready", "A coherent published model is not ready.");
    if (this.generation !== s.generation) {
      this.generation = s.generation;
      this.workspace = liveId();
    }
    const identity: LiveIdentity = {
      app_instance_id: this.appId,
      controller_session_id: this.sessionId,
      workspace_id: this.workspace,
      project_generation: s.generation,
      project_id: s.model.project.id
    };
    return {
      s,
      identity
    };
  }
  private fresh(p: Preview) {
    const { s, identity } = this.current();
    if (identity.workspace_id !== p.admission.workspace)
      fail("wrong_workspace", "Workspace was replaced.");
    if (s.revision !== p.basis.model_revision || s.hash.value !== p.basis.model_hash.value)
      fail("stale_basis", "Published model changed.");
  }
  private result(t: Ticket) {
    return {
      workspace: t.preview.admission.workspace,
      ticket: t.preview.admission.ticket,
      state: t.state,
      reason: t.reason,
      receipt: copy(t.receipt)
    };
  }
  async request(request: LiveRequest, signal: AbortSignal): Promise<LiveResponse> {
    try {
      if (!this.active || request.controller_session_id !== this.sessionId || request.app_instance_id !== this.appId)
        fail("controller_unavailable", "Controller registration is unavailable.");
      let result: unknown;
      switch (request.method) {
        case "inspect":
          result = this.inspect(request.params);
          break;
        case "preview":
          result = await this.preview(request.params, request.request_id, signal);
          break;
        case "submit":
          result = await this.submit(request.params, signal);
          break;
        case "status":
          result = await this.status(request.params);
          break;
        default: fail("unsupported_method", "Only inspect, preview, submit and status are supported.");
      }
      return {
        result
      };
    }
    catch (error) {
      const e = error as {
        liveError?: boolean;
        code: string;
        message: string;
        retryable: boolean;
        next_action: string;
      };
      return {
        error: e?.liveError ? {
          code: e.code,
          message: e.message,
          retryable: e.retryable,
          next_action: e.next_action
        } : {
          code: "internal_error",
          message: "Live control could not complete this request.",
          retryable: false,
          next_action: "Reconcile status; retry uncertain submit with its original workspace, preview and key."
        }
      };
    }
  }
  private inspect(params: unknown) {
    const scope = (params as {
      scope?: unknown;
    })?.scope;
    const p = object(params, scope === "workspace" ? ["scope"] : ["scope", "workspace", "node_ids"]);
    const { s, identity } = this.current();
    const unit = s.model.project.units.length;
    if (scope === "workspace")
      return {
        workspace: identity.workspace_id,
        identity,
        readiness: "ready",
        selection: copy(s.selection),
        supported: {
          object_type: "Node",
          field_path: "position.x",
          operation_kind: "modify",
          change_kind: "set_field",
          dimension: "length",
          length_unit: unit
        },
        limits: {
          max_node_ids: 128,
          max_changes: 64
        }
      };
    if (scope !== "nodes")
      fail("invalid_request", "Unknown inspection scope.");
    if (p.workspace !== identity.workspace_id)
      fail("wrong_workspace", "Inspect the current workspace first.");
    if (!Array.isArray(p.node_ids) || !p.node_ids.length || p.node_ids.length > 128)
      fail("invalid_request", "Supply 1 to 128 explicit node IDs.");
    const nodes = p.node_ids.map(id => {
      const node = s.model.nodes.find(n => n.id === string(id));
      if (!node)
        fail("invalid_request", "Unknown node.");
      return copy({
        id: node.id,
        label: node.label,
        position: node.position
      });
    });
    const existing = [...this.bases.entries()].find(([, b]) => b.identity.workspace_id === identity.workspace_id && b.identity.model_revision === s.revision && b.identity.model_hash.value === s.hash.value);
    const basis = existing?.[0] ?? liveId(), basis_identity = {
      ...identity,
      model_revision: s.revision,
      model_hash: copy(s.hash)
    };
    this.bases.clear();
    this.bases.set(basis, {
      snapshot: copy(s),
      identity: basis_identity
    });
    return {
      workspace: identity.workspace_id,
      identity,
      basis,
      basis_identity,
      nodes,
      length_unit: unit
    };
  }
  private async preview(params: unknown, requestId: string, signal: AbortSignal) {
    const p = object(params, ["workspace", "basis", "changes"]);
    const b = this.bases.get(string(p.basis));
    if (!b)
      fail("stale_basis", "Unknown basis; inspect nodes again.");
    if (p.workspace !== b.identity.workspace_id)
      fail("wrong_workspace", "Basis belongs to another workspace.");
    if (!Array.isArray(p.changes) || !p.changes.length || p.changes.length > 64)
      fail("invalid_request", "Supply 1 to 64 ordered changes.");
    if (this.previews.size + this.previewReservations >= 256)
      fail("capacity", "Controller preview capacity reached.");
    const batch: OperationBatch = {
      batch_id: `live-batch-${liveId()}`,
      operations: p.changes.map(raw => {
        const c = object(raw, ["target", "field_path", "before", "after", "unit", "dimension"]), target = object(c.target, ["object_type", "ref"]);
        if (target.object_type !== "Node" || c.field_path !== "position.x" || c.dimension !== "length" || c.unit !== b.snapshot.model.project.units.length)
          fail("unsupported_change", "Only Node position.x in the inspected length unit is supported.");
        const op: EditorOperationIntent = {
          operation_id: `live-operation-${liveId()}`,
          operation_kind: "modify",
          operation_status: "proposed",
          author_type: "agent",
          source: {
            source_ref: `local_json_cli:${this.sessionId}:${requestId}`,
            source_channel: "local_json_cli",
            source_role: "external_agent_proposal"
          },
          target: {
            object_type: "Node",
            ref: string(target.ref)
          },
          change: {
            change_id: `live-change-${liveId()}`,
            change_kind: "set_field",
            field_label: "Node X coordinate",
            field_path: "position.x",
            before: string(c.before),
            after: string(c.after),
            unit: string(c.unit),
            dimension: "length",
            source_note: "External local JSON proposal; explicit local review required."
          },
          validation: {
            schema_validation: "not_run",
            constraint_validation: "not_run",
            unit_validation: "not_run",
            diff_preview_status: "not_generated",
            application_status: "not_applied"
          },
          audit_boundary: {
            mutation_route: "structured_operations_only",
            direct_model_mutation_allowed: false,
            requires_user_acceptance: true,
            mutates_accepted_model_state: false
          },
          professional_boundary: {
            human_review_required: true,
            software_makes_compliance_claim: false,
            software_makes_certification_claim: false,
            software_makes_sealing_claim: false,
            software_makes_approval_claim: false,
            software_makes_authentication_claim: false
          },
          rationale: "Proposed Node coordinate edit for local review."
        };
        return op;
      })
    };
    const preview = liveId();
    const record: Preview = {
      preview,
      basis: copy(b.identity),
      admission: {
        token: liveId(),
        ticket: liveId(),
        workspace: b.identity.workspace_id,
        batch,
        model: copy(b.snapshot.model),
        hash: copy(b.snapshot.hash),
        internalRevision: b.snapshot.internalRevision,
        generation: b.snapshot.generation,
        revision: b.snapshot.revision,
        requestId
      }
    };
    this.fresh(record);
    this.previewReservations += 1;
    let outcome;
    try {
      outcome = await validateOperationBatch(copy(record.admission.model), copy(batch), copy(record.admission.hash));
    }
    finally {
      this.previewReservations -= 1;
    }
    this.fresh(record);
    if (signal.aborted)
      fail("cancelled_before_publication", "Preview cancelled without publication.");
    if (outcome.batch_id !== batch.batch_id || outcome.initial_model_hash?.value !== record.admission.hash.value ||
      outcome.applied_model || outcome.acceptance || outcome.validation.application_status === "applied_to_session_model" ||
      outcome.mode !== "validate_only")
      fail("internal_error", "Validation did not match the frozen proposal.");
    const passed = outcome.validation.batch_validation_status === "passed";
    if (passed)
      this.previews.set(preview, record);
    return {
      workspace: p.workspace,
      preview_ref: passed ? preview : null,
      basis: p.basis,
      basis_identity: copy(b.identity),
      validation: passed ? "passed" : "blocked",
      outcome
    };
  }
  private async submit(params: unknown, signal: AbortSignal) {
    const p = object(params, ["workspace", "preview_ref", "idempotency_key"]), key = string(p.idempotency_key);
    const previous = this.keys.get(key);
    if (previous) {
      if (p.workspace !== previous.preview.admission.workspace || p.preview_ref !== previous.preview.preview)
        fail("idempotency_conflict", "Key is already bound to another proposal.");
      return this.recover(previous);
    }
    const preview = this.previews.get(string(p.preview_ref));
    if (!preview)
      fail("unknown_preview", "Unknown preview.");
    if (p.workspace !== preview.admission.workspace)
      fail("wrong_workspace", "Preview belongs to another workspace.");
    this.fresh(preview);
    if (this.host.busy?.())
      fail("busy", "A local operation or project transaction owns the session.");
    if (this.keys.size >= 1024)
      fail("capacity", "Controller idempotency capacity reached.");
    let resolve!: (v: unknown) => void, reject!: (e: unknown) => void;
    const pending = new Promise<unknown>((yes, no) => {
      resolve = yes;
      reject = no;
    });
    // Reservation is synchronous, preceding queue scheduling and every await.
    const t: Ticket = {
      preview: copy(preview),
      state: "outcome_unknown",
      reason: null,
      receipt: null,
      published: false,
      cancelled: false,
      pending,
      resolve,
      reject
    };
    // Each independently keyed admission gets a distinct ticket/token.
    t.preview.admission.ticket = liveId();
    t.preview.admission.token = liveId();
    this.keys.set(key, t);
    this.tickets.set(t.preview.admission.ticket, t);
    const cancel = () => {
      if (!t.published && !t.observed) {
        t.cancelled = true;
        this.host.remove(t.preview.admission.token);
      }
    };
    signal.addEventListener("abort", cancel, {
      once: true
    });
    if (signal.aborted) {
      t.cancelled = true;
      t.reason = "cancelled_before_publication";
      t.state = "expired";
      t.resolve(this.result(t));
    }
    else
      this.host.enqueue(copy(t.preview.admission));
    try {
      await pending;
      return this.recover(t);
    }
    finally {
      signal.removeEventListener("abort", cancel);
    }
  }
  private async status(params: unknown) {
    const p = object(params, ["workspace", "ticket"]);
    const t = this.tickets.get(string(p.ticket));
    if (!t)
      fail("unknown_ticket", "Unknown ticket; reconcile the model before resubmitting.");
    if (p.workspace !== t.preview.admission.workspace)
      fail("wrong_workspace", "Ticket belongs to another workspace.");
    return this.recover(t);
  }
  private async recover(t: Ticket): Promise<unknown> {
    if (!t.published && !t.observed && !t.reason && t.state === "outcome_unknown") {
      await t.pending;
      return this.recover(t);
    }
    if (t.reason === "cancelled_before_publication")
      fail("cancelled_before_publication", "Committed observation confirmed no queue publication.");
    if (t.observed && !t.receipt) {
      const failed = t.reason === "observed_commit_hash_unavailable";
      if (!t.hashing)
        this.hash(t);
      if (failed)
        return this.result(t);
      fail("not_ready", "Observed commit receipt is being hashed; retry status.");
    }
    return this.result(t);
  }
  /** Called only from a committed layout effect. */
  observe(tokens: Set<string>, generation: number, revision: number, publications: LivePublication[]) {
    for (const t of this.tickets.values()) {
      if (t.observed || t.receipt || ["rejected", "withdrawn", "expired"].includes(t.state))
        continue;
      const a = t.preview.admission, publication = publications.find(p => p.token === a.token);
      if (publication) {
        t.observed = copy(publication);
        this.hash(t);
        continue;
      }
      if (t.applying) {
        t.state = "outcome_unknown";
        t.reason = "application_publication_unconfirmed";
        continue;
      }
      if (generation !== a.generation || revision !== a.revision) {
        t.state = "expired";
        t.reason = generation !== a.generation ? "workspace_replaced" : "stale_basis";
        t.resolve(this.result(t));
      }
      else if (tokens.has(a.token)) {
        if (!t.published) {
          t.published = true;
          t.state = "queued";
          t.resolve(this.result(t));
        }
      }
      else if (t.cancelled && !t.published) {
        t.state = "expired";
        t.reason = "cancelled_before_publication";
        t.resolve(this.result(t));
      }
      else if (t.published && t.state === "queued") {
        t.state = "withdrawn";
        t.reason = "cleared_in_review";
      }
    }
  }
  beginApply(token: string) {
    for (const t of this.tickets.values())
      if (t.preview.admission.token === token && t.published && !t.observed) {
        t.applying = true;
        t.state = "outcome_unknown";
        t.reason = "application_publication_pending";
      }
  }
  reject(token: string) {
    for (const t of this.tickets.values())
      if (t.preview.admission.token === token && !t.observed) {
        t.state = "rejected";
        t.reason = "validation_rejected";
      }
  }
  private hash(t: Ticket) {
    const observed = t.observed!; // immutable copy captured before the first hash await
    t.hashing = (async () => {
      try {
        const hash = await computeModelHash(observed.model);
        if (!hash)
          throw new Error("missing hash");
        const a = t.preview.admission;
        t.receipt = {
          ticket: a.ticket,
          workspace: a.workspace,
          identity: {
            app_instance_id: t.preview.basis.app_instance_id,
            controller_session_id: this.sessionId,
            workspace_id: a.workspace,
            project_generation: a.generation,
            project_id: a.model.project.id
          },
          batch_id: a.batch.batch_id,
          operation_ids: a.batch.operations.map(o => o.operation_id),
          origin: {
            actor_type: "agent",
            source_channel: "local_json_cli",
            request_id: a.requestId
          },
          acceptance: {
            route: "local_review_apply",
            identity_verification: "not_performed",
            professional_approval: false
          },
          before: {
            model_revision: a.revision,
            model_hash: copy(a.hash)
          },
          after: {
            model_revision: observed.revision,
            model_hash: hash
          },
          publication: {
            undo_checkpoint_id: observed.undoCheckpointId,
            applied_receipt_id: observed.appliedReceiptId,
            batch_receipt_id: observed.batchReceiptId,
            queue_entry_removed: true,
            computed_results_invalidated: true
          },
          persistence_status: "session_state_only_not_yet_saved"
        };
        t.state = "committed";
        t.reason = null;
        t.resolve(this.result(t));
      }
      catch {
        t.state = "outcome_unknown";
        t.reason = "observed_commit_hash_unavailable";
      }
      finally {
        t.hashing = undefined;
      }
    })();
  }
}
