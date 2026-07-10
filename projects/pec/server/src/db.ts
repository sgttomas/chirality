/**
 * SQLite schema and connection (ADR-003). node:sqlite, WAL mode.
 * Append-only tables (history_entry, audit_event) are protected by triggers that
 * RAISE on UPDATE/DELETE (I-7, PEC-NFR-001). intake_item.statement_verbatim is
 * trigger-frozen (OM-3). Controlled records have no delete path in the repo layer;
 * delete triggers add defense in depth (PEC-NFR-002).
 */

import { DatabaseSync } from 'node:sqlite'

export type Db = DatabaseSync

const CONTROLLED_TABLES = [
  'package', 'deliverable', 'revision', 'intake_item', 'work_item', 'hold',
  'check_record', 'review_comment', 'approval_record', 'decision', 'risk',
  'interface_item', 'condition_record', 'issue_event',
  // P2: plan placements, the plan-change log, its links, and supersession links are
  // records of planning state/change — no delete path (move to 'later' instead)
  'plan_item', 'plan_shift', 'plan_shift_link', 'supersession_link',
  // D-PEC-08: import proposals are controlled records — reject, never delete
  'import_proposal',
]

// D-PEC-13 (as amended): imported Package Tracker rows — §16 tracker contract, import-owned
// like schedule_activity. One row per package: the resolved package is the idempotency key;
// the CoA tracking number is kept verbatim as plain data (owner amendment). Shared between
// the base schema and the old-shape rebuild in openDb.
const PACKAGE_TRACKER_DDL = `
CREATE TABLE IF NOT EXISTS package_tracker (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  tracking_no TEXT,                -- CoA number, kept verbatim; data only, NOT the key
  package_name TEXT NOT NULL,
  discipline TEXT,
  area TEXT,
  package_type_approved TEXT,
  package_type_proposed TEXT,
  line_items TEXT,
  vendors_engaged TEXT,
  vendor_awarded TEXT,
  expected_delivery_date TEXT,
  cost_estimate_cad TEXT,
  comments TEXT,
  stage_budgetary_datasheet TEXT,
  stage_cost_estimate TEXT,
  stage_package_datasheet TEXT,
  stage_package TEXT,
  stage_rfq TEXT,
  stage_review TEXT,
  stage_vendor_bids TEXT,
  stage_clarifications TEXT,
  stage_evaluation TEXT,
  stage_eng_req TEXT,
  stage_po TEXT,
  stage_databook TEXT,
  package_id INTEGER NOT NULL REFERENCES package(id),  -- the §16 idempotency key
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, package_id)
);`

const SCHEMA = `
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS person (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  is_admin INTEGER NOT NULL DEFAULT 0,
  discipline TEXT,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS session (
  token TEXT PRIMARY KEY,
  person_id INTEGER NOT NULL REFERENCES person(id),
  created_at TEXT NOT NULL,
  expires_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS project (
  id INTEGER PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  timezone TEXT NOT NULL DEFAULT 'UTC',
  weekend_days TEXT NOT NULL DEFAULT '["Sat","Sun"]',
  holidays TEXT NOT NULL DEFAULT '[]',
  thresholds TEXT NOT NULL DEFAULT '{}',
  config TEXT NOT NULL DEFAULT '{}',
  version INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS project_role (
  project_id INTEGER NOT NULL REFERENCES project(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  role TEXT NOT NULL,
  UNIQUE(project_id, person_id, role)
);

CREATE TABLE IF NOT EXISTS seq (
  project_id INTEGER NOT NULL,
  kind TEXT NOT NULL,
  next_val INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (project_id, kind)
);

CREATE TABLE IF NOT EXISTS package (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  code TEXT NOT NULL,
  name TEXT NOT NULL,
  lead_id INTEGER REFERENCES person(id),
  description TEXT,
  milestone TEXT,
  area TEXT,                       -- §16 mdl optional column (D-PEC-23)
  package_type TEXT,               -- §16 mdl optional column (D-PEC-23)
  discipline TEXT,                 -- contract v2 (D-PEC-41): attested package discipline
  source_payload TEXT,             -- D-PEC-41 full-fidelity capture: verbatim unmapped columns (JSON)
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, code)
);

-- D-PEC-51: one package may carry multiple attested disciplines, and the
-- association is source-qualified so MDL and RAIL can coexist losslessly.
CREATE TABLE IF NOT EXISTS package_discipline (
  project_id INTEGER NOT NULL REFERENCES project(id),
  package_id INTEGER NOT NULL REFERENCES package(id),
  discipline TEXT NOT NULL,
  source_contract TEXT NOT NULL,
  PRIMARY KEY (project_id, package_id, discipline, source_contract)
);
CREATE INDEX IF NOT EXISTS idx_package_discipline_package
  ON package_discipline(project_id, package_id);

CREATE TABLE IF NOT EXISTS deliverable (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  package_id INTEGER NOT NULL REFERENCES package(id),
  doc_no TEXT NOT NULL,
  title TEXT NOT NULL,
  discipline TEXT,
  deliverable_type TEXT,
  owner_id INTEGER REFERENCES person(id),
  dc_ref TEXT,
  client_no TEXT,
  milestone TEXT,
  due_date TEXT,
  issue_purpose_plan TEXT,
  remarks TEXT,
  -- Contract v2 (D-PEC-41): PE-attested import fields — never in-app editable, never
  -- derived (reconciliation 1); absent from the updateDeliverable editable whitelist.
  project_phase TEXT,
  target_completeness TEXT,
  working_status TEXT,
  percent_complete INTEGER,        -- attested 0..100 integer, or NULL
  percent_complete_verbatim TEXT,  -- attested non-numeric marker (e.g. "Next Phase"), verbatim
  source_payload TEXT,             -- full-fidelity capture: verbatim unmapped columns (JSON)
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, doc_no)
);
CREATE INDEX IF NOT EXISTS idx_deliverable_project ON deliverable(project_id, package_id);

CREATE TABLE IF NOT EXISTS revision (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  deliverable_id INTEGER NOT NULL REFERENCES deliverable(id),
  rev_code TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'in_work',
  created_at TEXT NOT NULL,
  created_by INTEGER NOT NULL,
  superseded_by_revision_id INTEGER,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_revision_deliverable ON revision(deliverable_id);
CREATE INDEX IF NOT EXISTS idx_revision_project ON revision(project_id);

CREATE TABLE IF NOT EXISTS intake_item (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  statement_verbatim TEXT NOT NULL,
  quick_type TEXT NOT NULL,
  anchor_suggestion TEXT,
  need_by TEXT,
  suggested_owner_id INTEGER,
  log TEXT NOT NULL DEFAULT 'internal',
  raised_by INTEGER NOT NULL,
  raised_at TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'raised',
  disposition TEXT,
  disposition_note TEXT,
  merged_into_intake_id INTEGER,
  area TEXT,                       -- §16 rail optional column (D-PEC-23)
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_intake_project ON intake_item(project_id, state);

CREATE TABLE IF NOT EXISTS intake_link (
  id INTEGER PRIMARY KEY,
  intake_id INTEGER NOT NULL REFERENCES intake_item(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS work_item (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  statement TEXT,
  kind TEXT NOT NULL DEFAULT 'action',
  log TEXT NOT NULL DEFAULT 'internal',
  anchor_type TEXT NOT NULL,
  anchor_id INTEGER NOT NULL,
  package_id INTEGER,
  owner_id INTEGER NOT NULL,
  need_by TEXT,
  priority TEXT,
  priority_provenance TEXT,
  state TEXT NOT NULL DEFAULT 'open',
  committed_week TEXT,
  commit_source TEXT,             -- manual | plan (PEC-PLAN-007)
  source_type TEXT,
  source_id INTEGER,
  closing_statement TEXT,
  closed_by INTEGER,
  closed_at TEXT,
  cancel_reason TEXT,
  area TEXT,                       -- §16 rail optional column (D-PEC-23)
  needs_audience TEXT,             -- D-PEC-47 explicit source classification: internal | client | NULL
  responsible_party TEXT,          -- contract v2 (D-PEC-41): attested discipline/function, verbatim
  source_issue_type TEXT,          -- contract v2: attested RAIL issue type, verbatim
  source_payload TEXT,             -- D-PEC-41 full-fidelity capture: verbatim unmapped columns (JSON)
  created_by INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_work_item_project ON work_item(project_id, state);
CREATE INDEX IF NOT EXISTS idx_work_item_owner ON work_item(project_id, owner_id, state);
CREATE INDEX IF NOT EXISTS idx_work_item_anchor ON work_item(anchor_type, anchor_id);

CREATE TABLE IF NOT EXISTS work_item_link (
  id INTEGER PRIMARY KEY,
  work_item_id INTEGER NOT NULL REFERENCES work_item(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS hold (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  cause TEXT NOT NULL,
  statement TEXT,
  owner_id INTEGER NOT NULL,
  need_by TEXT,
  raised_by INTEGER NOT NULL,
  raised_at TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'active',
  resolution_kind TEXT,
  resolution_note TEXT,
  resolved_at TEXT,
  resolving_ref_type TEXT,
  resolving_ref_id INTEGER,
  log TEXT NOT NULL DEFAULT 'internal',
  needs_audience TEXT,             -- D-PEC-47 explicit source classification: internal | client | NULL
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_hold_project ON hold(project_id, state);

CREATE TABLE IF NOT EXISTS hold_link (
  id INTEGER PRIMARY KEY,
  hold_id INTEGER NOT NULL REFERENCES hold(id),
  target_type TEXT NOT NULL,
  target_id INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_hold_link_target ON hold_link(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_hold_link_hold ON hold_link(hold_id);

CREATE TABLE IF NOT EXISTS checklist_template (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  name TEXT NOT NULL,
  discipline TEXT,
  deliverable_type TEXT,
  items TEXT NOT NULL DEFAULT '[]',
  version INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS check_record (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  revision_id INTEGER NOT NULL REFERENCES revision(id),
  checker_id INTEGER NOT NULL,
  template_id INTEGER,
  state TEXT NOT NULL DEFAULT 'open',
  checklist TEXT NOT NULL DEFAULT '[]',
  accepted_at TEXT,
  independence_warning INTEGER NOT NULL DEFAULT 0,
  reopen_reason TEXT,
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_check_revision ON check_record(revision_id);
CREATE INDEX IF NOT EXISTS idx_check_project ON check_record(project_id, state);

CREATE TABLE IF NOT EXISTS review_comment (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  check_id INTEGER REFERENCES check_record(id),
  revision_id INTEGER REFERENCES revision(id),
  originator_id INTEGER NOT NULL,
  responder_id INTEGER NOT NULL,
  text TEXT NOT NULL,
  response TEXT,
  disposition TEXT NOT NULL DEFAULT 'open',
  closure_evidence_id INTEGER,
  log TEXT NOT NULL DEFAULT 'internal',
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CHECK (check_id IS NOT NULL OR revision_id IS NOT NULL)
);
CREATE INDEX IF NOT EXISTS idx_comment_check ON review_comment(check_id);
CREATE INDEX IF NOT EXISTS idx_comment_project ON review_comment(project_id, disposition);

CREATE TABLE IF NOT EXISTS approval_record (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  approval_type TEXT NOT NULL,
  authority_source TEXT,
  applies_to_type TEXT NOT NULL,
  applies_to_id INTEGER NOT NULL,
  authority_holder TEXT,
  required_decision_type TEXT,
  signatory_ids TEXT NOT NULL DEFAULT '[]',
  basis_ref TEXT,
  due_date TEXT,
  hold_point INTEGER NOT NULL DEFAULT 0,
  state TEXT NOT NULL DEFAULT 'required',
  outcome_decision_id INTEGER,
  superseded_by_id INTEGER,
  ready_at TEXT,
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_approval_project ON approval_record(project_id, state);
CREATE INDEX IF NOT EXISTS idx_approval_applies ON approval_record(applies_to_type, applies_to_id);

CREATE TABLE IF NOT EXISTS decision (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  statement TEXT NOT NULL,
  preparer_id INTEGER,
  authority_id INTEGER NOT NULL,
  need_by TEXT,
  state TEXT NOT NULL DEFAULT 'identified',
  outcome TEXT,
  rationale TEXT,
  options_considered TEXT,
  recommendation TEXT,
  decided_at TEXT,
  decided_by INTEGER,
  kind TEXT NOT NULL DEFAULT 'standalone',
  approval_record_id INTEGER,
  condition_id INTEGER,
  superseded_by_id INTEGER,
  package_id INTEGER,
  log TEXT NOT NULL DEFAULT 'internal',
  open_date TEXT,                  -- §16 decisions optional column (D-PEC-23)
  area TEXT,                       -- §16 decisions optional column (D-PEC-23)
  source TEXT,                     -- §16 decisions optional column (D-PEC-23)
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_decision_project ON decision(project_id, state);

CREATE TABLE IF NOT EXISTS decision_link (
  id INTEGER PRIMARY KEY,
  decision_id INTEGER NOT NULL REFERENCES decision(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  relation TEXT NOT NULL DEFAULT 'affects'
);
CREATE INDEX IF NOT EXISTS idx_decision_link ON decision_link(decision_id);

CREATE TABLE IF NOT EXISTS risk (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  cause TEXT,
  consequence TEXT,
  package_id INTEGER,
  deliverable_id INTEGER,
  owner_id INTEGER,
  probability INTEGER,
  impact INTEGER,
  mitigation TEXT,
  need_by TEXT,
  state TEXT NOT NULL DEFAULT 'open',
  category TEXT,                   -- §16 risks optional column (D-PEC-23)
  risk_type TEXT,                  -- §16 risks optional column (D-PEC-23)
  treatment TEXT,                  -- §16 risks optional column (D-PEC-23)
  residual_probability INTEGER,    -- §16 risks optional column (D-PEC-23)
  residual_impact INTEGER,         -- §16 risks optional column (D-PEC-23)
  version INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS interface_item (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  title TEXT NOT NULL,
  giving_party TEXT NOT NULL,
  receiving_party TEXT NOT NULL,
  giving_package_id INTEGER,
  receiving_package_id INTEGER,
  required_info TEXT,
  need_by TEXT,
  state TEXT NOT NULL DEFAULT 'open',
  log TEXT NOT NULL DEFAULT 'internal',
  version INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS interface_deliverable (
  id INTEGER PRIMARY KEY,
  interface_id INTEGER NOT NULL REFERENCES interface_item(id),
  deliverable_id INTEGER NOT NULL REFERENCES deliverable(id)
);

CREATE TABLE IF NOT EXISTS condition_template (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  name TEXT NOT NULL,
  deliverable_type TEXT,
  issue_purpose TEXT,
  package_id INTEGER,
  transition TEXT NOT NULL,
  type TEXT NOT NULL,
  severity TEXT NOT NULL DEFAULT 'warn',
  description TEXT NOT NULL,
  required_artifact_name TEXT
);

CREATE TABLE IF NOT EXISTS condition_record (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  parent_type TEXT NOT NULL,
  parent_id INTEGER NOT NULL,
  gated_transition TEXT NOT NULL,
  type TEXT NOT NULL,
  description TEXT NOT NULL,
  required_ref_type TEXT,
  required_ref_id INTEGER,
  required_artifact_name TEXT,
  source TEXT NOT NULL DEFAULT 'manual',
  source_ref TEXT,
  severity TEXT NOT NULL DEFAULT 'warn',
  owner_id INTEGER,
  need_by TEXT,
  state TEXT NOT NULL DEFAULT 'open',
  satisfied_by_type TEXT,
  satisfied_by_id INTEGER,
  satisfied_at TEXT,
  waiver_decision_id INTEGER,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_condition_parent ON condition_record(parent_type, parent_id);
CREATE INDEX IF NOT EXISTS idx_condition_project ON condition_record(project_id, state);

CREATE TABLE IF NOT EXISTS issue_event (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  revision_id INTEGER NOT NULL REFERENCES revision(id),
  purpose TEXT NOT NULL,
  transmittal_ref TEXT NOT NULL,
  recipients TEXT NOT NULL DEFAULT '[]',
  issued_at TEXT NOT NULL,
  issued_by INTEGER NOT NULL,
  approval_record_ids TEXT NOT NULL DEFAULT '[]',
  decision_ids TEXT NOT NULL DEFAULT '[]',
  archive_ref TEXT,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_issue_revision ON issue_event(revision_id);

CREATE TABLE IF NOT EXISTS evidence (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  kind TEXT NOT NULL,
  label TEXT NOT NULL,
  url_or_path TEXT,
  content TEXT,
  added_by INTEGER NOT NULL,
  added_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_evidence_record ON evidence(record_type, record_id);

CREATE TABLE IF NOT EXISTS basis_reference (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  basis_kind TEXT NOT NULL,
  reference TEXT NOT NULL,
  note TEXT,
  state TEXT NOT NULL DEFAULT 'active',
  superseded_by_id INTEGER
);

CREATE TABLE IF NOT EXISTS history_entry (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL,
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  at TEXT NOT NULL,
  actor_id INTEGER NOT NULL,
  kind TEXT NOT NULL,
  summary TEXT NOT NULL,
  payload TEXT,
  authority_ref TEXT
);
CREATE INDEX IF NOT EXISTS idx_history_record ON history_entry(record_type, record_id);
CREATE INDEX IF NOT EXISTS idx_history_project ON history_entry(project_id, at);

CREATE TABLE IF NOT EXISTS audit_event (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL,
  at TEXT NOT NULL,
  actor_id INTEGER NOT NULL,
  action TEXT NOT NULL,
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  prior_value TEXT,
  new_value TEXT,
  authority_ref TEXT
);

CREATE TABLE IF NOT EXISTS notification (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL,
  person_id INTEGER NOT NULL,
  at TEXT NOT NULL,
  event TEXT NOT NULL,
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL,
  record_ref TEXT NOT NULL,
  reason TEXT NOT NULL,
  next_action TEXT NOT NULL,
  due TEXT,
  severity TEXT NOT NULL DEFAULT 'info',
  read_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_notification_person ON notification(project_id, person_id, read_at);

-- ---------- P2 planning & capacity (PRD §12.4, §13.1) ----------

CREATE TABLE IF NOT EXISTS plan_item (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  item_type TEXT NOT NULL,         -- work_item | check | approval_record (I-9)
  item_id INTEGER NOT NULL,
  horizon TEXT NOT NULL DEFAULT 'later',  -- now | next | later (PEC-PLAN-001)
  week TEXT,                       -- ISO 'YYYY-Www'; null = unscheduled backlog
  discipline TEXT,                 -- capacity discipline (denormalized, ADR-013)
  planned_hours REAL NOT NULL DEFAULT 0,
  created_by INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, item_type, item_id)
);
CREATE INDEX IF NOT EXISTS idx_plan_item_week ON plan_item(project_id, week);

CREATE TABLE IF NOT EXISTS plan_period (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  week TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'open',   -- open | committed (PEC-PLAN-007)
  committed_at TEXT,
  committed_by INTEGER,
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, week)
);

CREATE TABLE IF NOT EXISTS capacity_entry (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  week TEXT NOT NULL,
  discipline TEXT NOT NULL,
  hours REAL NOT NULL DEFAULT 0,
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, week, discipline)
);

CREATE TABLE IF NOT EXISTS schedule_activity (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  activity_id TEXT NOT NULL,       -- external id, the §16 idempotency key
  description TEXT NOT NULL,
  start_date TEXT NOT NULL,
  finish_date TEXT NOT NULL,
  package_id INTEGER,
  deliverable_id INTEGER,
  row_type TEXT,                   -- §16 schedule optional columns (D-PEC-23)
  outline_level INTEGER,
  parent_activity_id TEXT,
  percent_complete INTEGER,
  duration_days REAL,
  baseline_start TEXT,
  baseline_finish TEXT,
  version INTEGER NOT NULL DEFAULT 1,
  UNIQUE(project_id, activity_id)
);

${PACKAGE_TRACKER_DDL}

CREATE TABLE IF NOT EXISTS plan_shift (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  plan_item_id INTEGER NOT NULL REFERENCES plan_item(id),
  from_horizon TEXT NOT NULL,
  to_horizon TEXT NOT NULL,
  from_week TEXT,
  to_week TEXT,
  reason TEXT NOT NULL,            -- PEC-PLAN-006: every shift records its reason
  impact_statement TEXT,           -- PEC-PLAN-005
  cross_package INTEGER NOT NULL DEFAULT 0,
  affected_package_ids TEXT NOT NULL DEFAULT '[]',
  state TEXT NOT NULL DEFAULT 'applied',  -- applied | proposed | rejected
  created_by INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  reviewed_by INTEGER,
  reviewed_at TEXT,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_plan_shift_project ON plan_shift(project_id, state);

CREATE TABLE IF NOT EXISTS plan_shift_link (
  id INTEGER PRIMARY KEY,
  plan_shift_id INTEGER NOT NULL REFERENCES plan_shift(id),
  record_type TEXT NOT NULL,
  record_id INTEGER NOT NULL
);

-- D-PEC-08: proposed imports (profile operation_proposal_contract lifecycle:
-- draft → ready_for_review → accepted → rejected/applied). The uploaded CSV lives
-- in-row so the single-file backup path (VACUUM INTO) covers it (RV-19).
CREATE TABLE IF NOT EXISTS import_proposal (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  ref TEXT NOT NULL,
  contract TEXT NOT NULL,
  source_name TEXT,
  source_sha256 TEXT NOT NULL,
  source_bytes INTEGER NOT NULL,
  source_csv TEXT NOT NULL,
  coverage_start TEXT,             -- D-PEC-39: PE-declared coverage, per uploaded document
  coverage_end TEXT,               -- D-PEC-39: declared, never inferred; null = undeclared
  source_extras TEXT,              -- D-PEC-41 full-fidelity capture: verbatim non-tabular source sheets (JSON)
  state TEXT NOT NULL DEFAULT 'draft',
  basis_history_id INTEGER,
  dry_run_report TEXT,
  dry_run_at TEXT,
  accepted_by INTEGER,
  accepted_at TEXT,
  accepted_sha256 TEXT,
  rejected_by INTEGER,
  rejected_at TEXT,
  reject_reason TEXT,
  applied_by INTEGER,
  applied_at TEXT,
  apply_report TEXT,
  created_by INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  version INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS idx_import_proposal_project ON import_proposal(project_id, state);

CREATE TABLE IF NOT EXISTS supersession_link (
  id INTEGER PRIMARY KEY,
  project_id INTEGER NOT NULL REFERENCES project(id),
  record_type TEXT NOT NULL,       -- approval_record | decision | revision | basis_reference
  old_id INTEGER NOT NULL,
  new_id INTEGER,
  affected TEXT NOT NULL DEFAULT '[]',  -- [{recordType, id, ref}] (PEC-AUTH-005)
  created_by INTEGER NOT NULL,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_supersession_old ON supersession_link(record_type, old_id);

-- Append-only enforcement (I-7, PEC-NFR-001)
CREATE TRIGGER IF NOT EXISTS history_no_update BEFORE UPDATE ON history_entry
BEGIN SELECT RAISE(ABORT, 'history_entry is append-only (I-7)'); END;
CREATE TRIGGER IF NOT EXISTS history_no_delete BEFORE DELETE ON history_entry
BEGIN SELECT RAISE(ABORT, 'history_entry is append-only (I-7)'); END;
CREATE TRIGGER IF NOT EXISTS audit_no_update BEFORE UPDATE ON audit_event
BEGIN SELECT RAISE(ABORT, 'audit_event is append-only (PEC-NFR-001)'); END;
CREATE TRIGGER IF NOT EXISTS audit_no_delete BEFORE DELETE ON audit_event
BEGIN SELECT RAISE(ABORT, 'audit_event is append-only (PEC-NFR-001)'); END;

-- Intake statement preserved verbatim after insert (OM-3, PEC-AHL-004)
CREATE TRIGGER IF NOT EXISTS intake_statement_frozen BEFORE UPDATE OF statement_verbatim ON intake_item
WHEN OLD.statement_verbatim <> NEW.statement_verbatim
BEGIN SELECT RAISE(ABORT, 'intake statement is preserved verbatim (OM-3)'); END;
`

/** No-hard-delete triggers for every controlled table (PEC-NFR-002). */
function deleteGuards(): string {
  return CONTROLLED_TABLES.map((t) => `
CREATE TRIGGER IF NOT EXISTS ${t}_no_delete BEFORE DELETE ON ${t}
BEGIN SELECT RAISE(ABORT, 'controlled records are never hard-deleted (PEC-NFR-002)'); END;`).join('\n')
}

/** Add a column to a pre-P2 database if it is missing (CREATE TABLE IF NOT EXISTS won't). */
function ensureColumn(db: Db, table: string, column: string, ddl: string): void {
  const cols = db.prepare(`PRAGMA table_info(${table})`).all() as Array<{ name: string }>
  if (!cols.some((c) => c.name === column)) {
    db.exec(`ALTER TABLE ${table} ADD COLUMN ${column} ${ddl}`)
  }
}

export function openDb(path: string): Db {
  const db = new DatabaseSync(path, { enableForeignKeyConstraints: true })
  db.exec(SCHEMA)
  db.exec(deleteGuards())
  // P2 columns on P1 tables (existing databases predate the CREATE TABLE defaults)
  ensureColumn(db, 'notification', 'severity', "TEXT NOT NULL DEFAULT 'info'")
  ensureColumn(db, 'work_item', 'commit_source', 'TEXT')
  // D-PEC-23 §16 optional-column additions (additive; inert until an import populates them)
  ensureColumn(db, 'package', 'area', 'TEXT')
  ensureColumn(db, 'package', 'package_type', 'TEXT')
  ensureColumn(db, 'work_item', 'area', 'TEXT')
  ensureColumn(db, 'work_item', 'needs_audience', 'TEXT')
  ensureColumn(db, 'intake_item', 'area', 'TEXT')
  ensureColumn(db, 'hold', 'needs_audience', 'TEXT')
  ensureColumn(db, 'decision', 'open_date', 'TEXT')
  ensureColumn(db, 'decision', 'area', 'TEXT')
  ensureColumn(db, 'decision', 'source', 'TEXT')
  ensureColumn(db, 'risk', 'category', 'TEXT')
  ensureColumn(db, 'risk', 'risk_type', 'TEXT')
  ensureColumn(db, 'risk', 'treatment', 'TEXT')
  ensureColumn(db, 'risk', 'residual_probability', 'INTEGER')
  ensureColumn(db, 'risk', 'residual_impact', 'INTEGER')
  ensureColumn(db, 'schedule_activity', 'row_type', 'TEXT')
  ensureColumn(db, 'schedule_activity', 'outline_level', 'INTEGER')
  ensureColumn(db, 'schedule_activity', 'parent_activity_id', 'TEXT')
  ensureColumn(db, 'schedule_activity', 'percent_complete', 'INTEGER')
  ensureColumn(db, 'schedule_activity', 'duration_days', 'REAL')
  ensureColumn(db, 'schedule_activity', 'baseline_start', 'TEXT')
  ensureColumn(db, 'schedule_activity', 'baseline_finish', 'TEXT')
  // D-PEC-39 coverage declarations (additive; existing proposals read as undeclared)
  ensureColumn(db, 'import_proposal', 'coverage_start', 'TEXT')
  ensureColumn(db, 'import_proposal', 'coverage_end', 'TEXT')
  // D-PEC-41 contract v2 (additive; inert until a v2 import populates them)
  ensureColumn(db, 'package', 'discipline', 'TEXT')
  ensureColumn(db, 'package', 'source_payload', 'TEXT')
  ensureColumn(db, 'deliverable', 'discipline', 'TEXT')
  ensureColumn(db, 'deliverable', 'project_phase', 'TEXT')
  ensureColumn(db, 'deliverable', 'target_completeness', 'TEXT')
  ensureColumn(db, 'deliverable', 'working_status', 'TEXT')
  ensureColumn(db, 'deliverable', 'percent_complete', 'INTEGER')
  ensureColumn(db, 'deliverable', 'percent_complete_verbatim', 'TEXT')
  ensureColumn(db, 'deliverable', 'source_payload', 'TEXT')
  ensureColumn(db, 'work_item', 'responsible_party', 'TEXT')
  ensureColumn(db, 'work_item', 'source_issue_type', 'TEXT')
  ensureColumn(db, 'work_item', 'source_payload', 'TEXT')
  ensureColumn(db, 'import_proposal', 'source_extras', 'TEXT')
  // D-PEC-51 additive migration: preserve any previously imported scalar
  // package discipline and reconstruct the MDL associations already attested
  // on deliverables. This upgrades populated projects without a rebuild while
  // future contract imports continue to record source-qualified associations.
  db.exec(`
    INSERT OR IGNORE INTO package_discipline
      (project_id, package_id, discipline, source_contract)
    SELECT project_id, id, trim(discipline), 'legacy'
    FROM package
    WHERE discipline IS NOT NULL AND trim(discipline) <> '';

    INSERT OR IGNORE INTO package_discipline
      (project_id, package_id, discipline, source_contract)
    SELECT project_id, package_id, trim(discipline), 'mdl-backfill'
    FROM deliverable
    WHERE discipline IS NOT NULL AND trim(discipline) <> '';
  `)
  // D-PEC-13 owner amendment: the tracker key moved from tracking_no to the resolved package.
  // Old-shape tables (nullable package_id, UNIQUE on tracking_no) exist only on scratch
  // instances and hold import-owned, reproducible rows — rebuild at the new shape; the next
  // tracker import repopulates.
  const trackerCols = db.prepare('PRAGMA table_info(package_tracker)').all() as Array<{ name: string; notnull: number }>
  if (trackerCols.some((c) => c.name === 'package_id' && c.notnull === 0)) {
    db.exec('DROP TABLE package_tracker')
    db.exec(PACKAGE_TRACKER_DDL)
  }
  return db
}

/** Run fn inside a transaction; rolls back on throw. */
export function withTx<T>(db: Db, fn: () => T): T {
  db.exec('BEGIN IMMEDIATE')
  try {
    const out = fn()
    db.exec('COMMIT')
    return out
  } catch (e) {
    db.exec('ROLLBACK')
    throw e
  }
}
