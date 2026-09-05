#!/usr/bin/env python3
"""SCA-APP-010 Gate 3 — exact candidate builder.

Reads the decomposition and companion register at the Gate-1 basis identities,
applies the Gate-2-accepted amendment as exact line transactions (fail closed
on any missing, duplicated, or drifted pre-image), writes the two candidate
post-images beside this script, and prints their SHA-256 and a validation
summary. It never touches the live files.

Run from the repository root:
    python3 projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Gate3/build_gate3_candidate.py
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
DECOMP = ROOT / "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
COMPANION = ROOT / "projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv"
DECOMP_PRE = "e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97"
COMPANION_PRE = "e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70"

DECOMP_OUT = HERE / "DECOMP_POSTIMAGE_CANDIDATE.md"
COMPANION_OUT = HERE / "COMPANION_POSTIMAGE_CANDIDATE.csv"
TX_OUT = HERE / "TRANSACTIONS.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Doc:
    def __init__(self, text: str) -> None:
        self.lines = text.split("\n")
        self.tx: list[dict] = []

    def _find(self, prefix: str) -> int:
        hits = [i for i, l in enumerate(self.lines) if l.startswith(prefix)]
        if len(hits) != 1:
            raise SystemExit(f"FAIL_CLOSED: prefix matched {len(hits)} lines: {prefix!r}")
        return hits[0]

    def replace_line(self, tid: str, prefix: str, new_line: str) -> None:
        i = self._find(prefix)
        self.tx.append({"id": tid, "kind": "REPLACE_LINE", "line": i + 1, "pre": self.lines[i], "post": new_line})
        self.lines[i] = new_line

    def edit_line(self, tid: str, prefix: str, edits: list[tuple[str, str]]) -> None:
        i = self._find(prefix)
        old = self.lines[i]
        new = old
        for a, b in edits:
            if new.count(a) != 1:
                raise SystemExit(f"FAIL_CLOSED: substring occurs {new.count(a)} times in line {i+1}: {a!r}")
            new = new.replace(a, b)
        self.tx.append({"id": tid, "kind": "EDIT_LINE", "line": i + 1, "pre": old, "post": new})
        self.lines[i] = new

    def insert_after(self, tid: str, prefix: str, new_lines: list[str]) -> None:
        i = self._find(prefix)
        self.tx.append({"id": tid, "kind": "INSERT_AFTER", "line": i + 1, "pre": self.lines[i], "post": "\n".join(new_lines)})
        self.lines[i + 1 : i + 1] = new_lines

    def text(self) -> str:
        return "\n".join(self.lines)


def build_decomposition(src: str) -> Doc:
    d = Doc(src)

    # ---- A001 OBJ-001 ----
    d.replace_line("A001", "| OBJ-001 | ",
        "| OBJ-001 | Provide a governed local desktop harness centred on actual human–agent dialogue as the invariant primary surface, with explicit turn context, a per-chat specification (folder, agent, permissions, delegation, and optionally a governed workflow) that the harness may propose and only the human accepts, provenance-bearing side-panel artifact and coordination views, and evidence-derived supervision. | SOW-001-SOW-008, SOW-023, SOW-081-SOW-082 | Dialogue, artifact collaboration, and operator workflow objective; the prompted ladder is proposed by the harness and accepted by the human; shared intent remains emergent rather than a stored UI authority object. |")

    # ---- SSOW rows ----
    d.replace_line("A002", "| SOW-001 | IN | REF-006 Section 8.1 |",
        "| SOW-001 | IN | REF-006 Section 8.1; SCA-APP-010 SR-01/SR-02/SR-06 | Provide a dialogue-centred desktop shell in which the centre dialogue is the invariant primary surface, the left panel is the chat history and navigator, and the right panel presents one tertiary view at a time (files, document, workflows, who is working, activity, session, settings). | The centre dialogue is never hidden, unmounted, or replaced; existing routes and the loop-first UI remain compatibility surfaces, and the retired `/workbench` and `/pipeline` routes remain reachable but unmounted from the active shell until separately ruled (Q3); shared intent is not a stored UI object. |")
    d.replace_line("A003", "| SOW-002 | IN | REF-006 Section 8.1, REF-003 Section 1 |",
        "| SOW-002 | IN | REF-006 Section 8.1, REF-003 Section 1; SCA-APP-010 SR-20/SR-21 | Support per-chat working-folder selection and validation with an app-scoped set of known folders, chosen in the composer before a chat's first message and fixed thereafter. | Must reject invalid and instruction-root-contained paths; a chat may have no folder; DEL-07-01 retains validation ownership. |")
    d.replace_line("A004", "| SOW-004 | IN | REF-006 Section 8.1, Section 8.7 |",
        "| SOW-004 | IN | REF-006 Section 8.1, Section 8.7; SCA-APP-010 SR-02/SR-05/SR-07 | Support professional resizable left-panel, centre-dialogue, right-panel (per-view widths and an expand state), and activity-strip layouts with versioned local UI state. | Layout, view, transcript selection, anchors, and panel state are non-authoritative convenience state and migrate non-destructively; the artifact-focus and resizable activity-shelf layouts are retired from the active shell; new fields are additive under the existing schema string. |")
    d.replace_line("A005", "| SOW-006 | IN | REF-006 Section 8.2 |",
        "| SOW-006 | IN | REF-006 Section 8.2; SCA-APP-010 SR-02/SR-08 | Present active dialogue/persona context, a right-panel \"Who is working\" view over canonical session parentage, a read-only right-panel Session view for selectable recorded-session replay, and Agent 0/1/2 role entry for Codex sessions under the per-folder settings. | The Session view is read-only, never takes the centre, and is distinct from the mounted primary live dialogue; the Work projection is unmounted until an explicitly recorded plan/task source exists. Role entry presents accepted state rather than inferring enforcement: Agent 2/TASK is labelled `role not mechanically enforced` when G-ROLE cannot mechanically prove non-delegation, and the product posture is labelled `Opt-in Preview`; missing plans, tasks, relationships, transcripts, or enforcement evidence remain explicitly absent or unknown. |")
    d.replace_line("A006", "| SOW-007 | IN | REF-006 Section 8.2 |",
        "| SOW-007 | IN | REF-006 Section 8.2; SCA-APP-010 SR-06 | Own presentation-neutral DECOMP/PREP/TASK/AUDIT dispatch lane semantics, category/task-scope interpretation, dynamic scope, and disabled-option rules without an active-shell mount. | The contextual Pipeline controls are retired from the active shell by SCA-APP-010 (presentation half retired by owner ruling; code, routes, and tests retained, not deleted); DEL-08-03 retains dispatch semantics; any later re-hosting of a presentation is a separate amendment. |")
    d.replace_line("A007", "| SOW-008 | IN | REF-006 Section 8.7 |",
        "| SOW-008 | IN | REF-006 Section 8.7; SCA-APP-010 SR-03/SR-24 | Expose per-turn toolkit options and preserve dialogue drafts, presets, explicit next-turn context references, artifact anchors, panel selections, chat annotations (titles, pins, groups, archive), known folders, and each chat's specification rung and declined proposal triggers as local convenience state. | Visible artifacts are not automatically model context; local state must not override runtime governance, rewrite sent-turn history, transfer primary-session context to a selected replay, or stand in for the workflow file or the session record. |")
    d.replace_line("A008", "| SOW-010 | IN | REF-006 Section 8.3, Section 8.4 |",
        "| SOW-010 | IN | REF-006 Section 8.3, Section 8.4; SCA-APP-010 SR-24 | Bind App client session-creation and boot requests to registered project identity/root, persona, mode, delegation policy, and options while the daemon owns runtime session state. | Boot fingerprint should reflect real project/policy inputs; the stored session-record field for delegation policy is Root-owned (OI-008). |")
    d.insert_after("A009-A012-SSOW", "| SOW-080 | IN | SCA-APP-008 Carrier Map WP-03;", [
        "| SOW-081 | IN | SCA-APP-010 SR-23/SR-24 (Q10 ruled) | Provide governed workflow files under the chat's folder at `.chirality/workflows/<slug>.md` declaring agent role, folder, permission, delegation policy, where briefs run, roadmap source and hash, and a roadmap with human-gate markers, together with a right-panel Workflows view to list, open, follow, pause, create, and bind workflows from a library of other known folders and skill-declared templates. | A workflow file steers the chat by delimited context injection and cites accepted truth; it never holds status, approvals, or evidence, which stay in deliverable records. Creation refuses a file with role, folder, or delegation policy unset. Writes obey K-PATH-2 containment. Q15 currency reporting and Q16 shared-folder position advance remain OI-008. |",
        "| SOW-082 | IN | SCA-APP-010 SR-24/SR-26 (Q13 ruled) | Provide the prompted specification ladder: a registered in-process deterministic `propose` tool available to Agent 0 and Agent 1 personas that validates the specification tuple and plan reference, refuses a trigger already declined in the chat, and emits `proposal.offered`; App consumption of the additive `proposal.offered`, `proposal.accepted`, `proposal.adjusted`, and `proposal.declined` event types; a transcript proposal card whose Accept, Adjust, and Not now actions are human acts applied by the app; and instruction-package clauses naming the few triggers. | Nothing is promoted silently; one proposal per chat per trigger. The event types are additive candidates against the Root-owned closed `HarnessEvent` schema v2 (K-EVENT-3) and are proposed to Root DEL-02-10 by routed notice (OI-008); App consumes them only after acceptance. The tool passes the same K-MCP-1 policy as every in-process tool. |",
        "| SOW-083 | IN | SCA-APP-010 SR-24 | Carry a per-chat delegation policy (`none` by default; ask before each brief; approve each brief's writes; bounded briefs) with the session and honour it in the Chirality-managed delegation bridge. | The policy only narrows what SCA-APP-008's prospective carrier text allows; it adds no delegation class. The daemon-owned session-record field is Root DEL-02-11's (OI-008); App binds the request (SOW-010). |",
        "| SOW-084 | IN | SCA-APP-010 SR-25 (Q14 ruled) | Provide a layered instruction root: the bundled base plus a client-owned, hash-pinned organisation layer of agents, skills, and workflow templates under the same protections as the instruction root and separate from the working root. | K-ROOT-1 applies to both layers; the organisation layer is read-only during ordinary project execution, hash-pinned, and packaging-checked; it is not a working root and never a proposal path. |",
    ])

    # ---- Vocabulary Map ----
    d.replace_line("A026-a", "| Working Root | `projectRoot`, selected workspace |",
        "| Working Root | `projectRoot`, selected workspace, folder (surface term) | Mutable project execution location; chosen per chat and fixed after the first message (SCA-APP-010). |")
    d.insert_after("A026-b", "| OpenPipeStress fixture | first domain example |", [
        "| HELP_HUMAN | Assistant | Surface display name of the default Agent 0 persona (SCA-APP-010 SR-26); the doctrine name stays in code, agents, and tooltips. |",
        "| Agent 1 persona | Role | Surface term for a chosen Agent 1 persona, shown by what it does; doctrine name in the tooltip. |",
        "| Governed workflow | Workflow | A `.chirality/workflows/<slug>.md` file that steers a chat; \"governed\" stays in the doctrine. |",
        "| Roadmap | Plan, step n of m | The workflow's ordered steps with human-gate markers. |",
        "| Bounded brief, child session | Delegated task, task | Surface term for an Agent 2 brief or the child session that runs it. |",
        "| Delegation policy | Delegation | Per-chat setting: no delegation, ask before delegating, delegate and approve changes, delegate freely. |",
        "| Operator mode | Permissions | Per-chat setting: read only, ask before changes, approve each change, make changes freely. |",
        "| Agent 0/1/2 session role | Supervisor, Manager, Specialist | Surface labels; the K-ROLE labels stay verbatim in the tooltip. |",
    ])

    # ---- Packages ----
    d.replace_line("A013", "| PKG-02 | Woven Dialogue Shell, Navigation, and Operator State |",
        "| PKG-02 | Woven Dialogue Shell, Navigation, and Operator State | Dialogue-centred shell with an invariant centre dialogue, left chat navigator, one-view-at-a-time right panel (files, document, workflows, who is working, activity, session, settings), activity strip, composer context line, account row and settings presentation, compatibility surfaces, and non-authoritative local UI state. | Human–agent dialogue, artifact collaboration, coordination presentation, and operator workflow behavior. | Runtime engine internals, canonical session/evidence ownership, arbitrary orchestration graphs, automatic intent inference, and project-control-plane authority. |")

    # ---- Deliverables ----
    d.replace_line("A014", "| DEL-02-01 | ",
        "| DEL-02-01 | Woven Dialogue Shell and Compatibility Navigation | TBD | UX_UI_SLICE | Compose the persistent primary human–agent transcript and composer with its context line (folder, agent, permissions, delegation, rung), the header-less three-panel frame, the left-panel chat navigator with local organisation, per-chat folder selection over the known-folder set, the account row host, and compatibility navigation without creating a second evidence store. | Dialogue shell; composer context line; chat navigator; account row host; route/query and compatibility tests | SOW-001, SOW-005 | OBJ-001 | M | Shell integration owns presentation only; work, hierarchy, transcript, and artifact facts remain governed by their existing semantic owners; the direct shell items are seated as Remaining work by the owner, not by this row. |")
    d.replace_line("A015", "| DEL-02-02 | ",
        "| DEL-02-02 | Right-Panel Coordination, Workflows, and Proposal UX | TBD | UX_UI_SLICE | Present, in the right panel, the \"Who is working\" view over recorded agent/session selections and Agent 0/1/2 role entry for Codex sessions with source, authority class, responsible reference, currency, and evidence; the Workflows view, roadmap, New workflow form, library, and bind actions over governed workflow files; and the transcript proposal card rendered from `proposal.*` events. Workbench and Pipeline are retired from the active shell (code, routes, and tests retained) and the Work projection is unmounted until an explicitly recorded plan/task source exists. | Who is working view; Workflows view, roadmap, and forms; proposal card; role-entry controls; exact `role not mechanically enforced` and `Opt-in Preview` posture labels; provenance labels; stale/empty-state, label, and query compatibility tests | SOW-006, SOW-081, SOW-082 | OBJ-001, OBJ-007 | M | DEL-08-02 retains routing, DEL-08-03 retains dispatch, DEL-08-04 retains role/delegation semantics, DEL-08-05 retains child records, DEL-05-04 retains replay/projection semantics, DEL-07-03 owns the workflow file contract, and DEL-06-03 owns the `propose` tool; this deliverable only composes accepted presentation, applies human proposal decisions, and does not infer enforcement. Split trigger: if implementation review finds cross-domain churn between the coordination and workflow views, propose a split before widening the envelope. |")
    d.replace_line("A016", "| DEL-02-04 | ",
        "| DEL-02-04 | Dialogue Toolkit, Context, and Local UI State | TBD | UX_UI_SLICE | Expose runtime options and preserve versioned layout (per-view right-panel widths, expand state), drafts, explicit next-turn context references, artifact anchors, selected replay references, panel state, chat annotations, known folders, chat rung and declined proposal triggers, and local presets as non-authoritative convenience state with rollback-safe migration; present the one-line activity strip in place of the resizable shelf. | Toolkit controls; workspace-state schema (additive v1 fields); resize/expand/anchor behavior; activity strip; context-reference, draft/preset, annotation, and migration guards | SOW-004, SOW-008, SOW-016 | OBJ-001, OBJ-004 | S | Convenience state stores references and presentation only; it never stores authoritative workflow, hierarchy, permission, or acceptance conclusions; the workflow file and the session record own rung-related truth. |")
    d.edit_line("A017", "| DEL-02-05 | ", [
        ("explaining per-root login and root-private app-owned `CODEX_HOME`,",
         "presenting one app-wide account and explaining per-folder consent over the root-private app-owned `CODEX_HOME`,"),
        ("| API key and account settings panel; `HostedEngineConsentPort` UI adapter;",
         "| API key and account settings panel; account row and popover; Settings view account and folder groups; `HostedEngineConsentPort` UI adapter;"),
        ("Live claims remain gated by the accepted Root/App account/consent contract, G3, G-CSP, and G4. |",
         "Live claims remain gated by the accepted Root/App account/consent contract, G3, G-CSP, and G4. Presenting the account as app-wide (SCA-APP-010 SR-19) does not change the port's per-root login semantics; the root-private login home is Root-owned and the shared-login amendment routes through Root DEL-02-09 (OI-008). |"),
    ])
    d.edit_line("A018", "| DEL-03-02 | ", [
        ("bind project/persona/mode/options requests,", "bind project/persona/mode/delegation-policy/options requests,"),
        ("| SOW-009, SOW-010, SOW-011, SOW-038 |", "| SOW-009, SOW-010, SOW-011, SOW-038, SOW-083 |"),
        ("generic TurnEngine and lock ownership remain Root-owned. |",
         "generic TurnEngine and lock ownership remain Root-owned; the stored delegation-policy field is Root-owned (SOW-083, OI-008). |"),
    ])
    d.replace_line("A019", "| DEL-04-04 | ",
        "| DEL-04-04 | PersonaComposer from Instruction Root | TBD | BACKEND_FEATURE_SLICE | Replace stub prompt behavior with instruction-root governance composed from the bundled base and the client-owned organisation layer, active persona, working-root policy, mode, tool-surface composition, and a clearly delimited roadmap-injection block for a followed governed workflow. | `persona-composer.ts`; persona content hash tests; layered-root composition tests; roadmap-block delimiting tests; boot fingerprint updates | SOW-017, SOW-030, SOW-081, SOW-084 | OBJ-004, OBJ-007 | M | Prompt composition slice with bounded artifacts; injected roadmap content is steering context from a K-PATH-2-contained file, never authority. |")
    d.edit_line("A020", "| DEL-05-02 | ", [
        ("without owning the generic event schema or writer. |",
         "without owning the generic event schema or writer; consume the additive `proposal.*` event types for replay and the proposal card once Root accepts them (SOW-082). |"),
        ("| SOW-014, SOW-015, SOW-039 |", "| SOW-014, SOW-015, SOW-039, SOW-082 |"),
    ])
    d.edit_line("A021", "| DEL-06-03 | ", [
        ("scope scan, and scaffold preview/dry-run, and document",
         "scope scan, scaffold preview/dry-run, and the `propose` specification-ladder tool, and document"),
        ("in-process extension-boundary notes; MCP tool tests |",
         "in-process extension-boundary notes; `propose` tool schema, validation, and once-per-chat tests; MCP tool tests |"),
        ("| SOW-048, SOW-050, SOW-064 |", "| SOW-048, SOW-050, SOW-064, SOW-082 |"),
    ])
    d.edit_line("A022", "| DEL-07-01 | ", [
        ("and instruction-root write protection. |",
         "and instruction-root write protection for both the bundled base and the client-owned, hash-pinned organisation layer. |"),
        ("instruction-root protection fixtures |",
         "instruction-root protection fixtures; organisation-layer pin and protection fixtures |"),
        ("| SOW-002, SOW-027, SOW-075 |", "| SOW-002, SOW-027, SOW-075, SOW-084 |"),
    ])
    d.edit_line("A023", "| DEL-07-03 | ", [
        ("semantic placeholders, and document kit buckets. |",
         "semantic placeholders, and document kit buckets; define the governed workflow file contract (front matter, roadmap grammar with gate markers, app-maintained position, library/bind copy semantics) and the rule that the file steers and never records. |"),
        ("`_MEMORY.md` rejection tests |", "`_MEMORY.md` rejection tests; workflow file contract and validator tests |"),
        ("| SOW-026 |", "| SOW-026, SOW-081 |"),
    ])
    d.edit_line("A024", "| DEL-08-01 | ", [
        ("naming, and section markers. |",
         "naming, section markers, the proposal clauses and named triggers in Agent 0 and Agent 1 packages, skill-declared workflow templates, and organisation-layer packaging and pins. |"),
        ("source-completeness checklist |",
         "source-completeness checklist; proposal-clause and template conformance checks; organisation-layer integrity checks |"),
        ("| SOW-030, SOW-031, SOW-073 |", "| SOW-030, SOW-031, SOW-073, SOW-082, SOW-084 |"),
        ("no runtime capability expansion. |",
         "no runtime capability expansion; instruction-file changes under `agents/` or `skills/` ship the routed agent-index change notice. |"),
    ])
    d.edit_line("A030", "| DEL-08-03 | ", [
        ("Semantic dispatch owner; DEL-02-02 owns presentation and may not infer plans/tasks from conversational prose. |",
         "Semantic dispatch owner; the contextual Pipeline presentation is retired from the active shell by SCA-APP-010 (code retained), so no active presentation consumer exists; any later consumer may not infer plans/tasks from conversational prose. |"),
    ])
    d.edit_line("A025", "| DEL-08-04 | ", [
        ("when G-ROLE cannot mechanically prove non-delegation. |",
         "when G-ROLE cannot mechanically prove non-delegation. Honour the per-chat delegation policy carried with the session (`none` by default) as a narrowing input to managed delegation. |"),
        ("| SOW-063 |", "| SOW-063, SOW-083 |"),
    ])

    # ---- Scope Ledger ----
    d.replace_line("A002-L", "| SOW-001 | IN | Woven Dialogue shell",
        "| SOW-001 | IN | Dialogue-centred shell: invariant centre dialogue, left chat navigator, one-view-at-a-time right panel, no header row. | REF-006 Section 8.1; SCA-APP-010 | PKG-02 | DEL-02-01 | OBJ-001 | DEC-004; DEC-025 | FALSE | Existing routes and loop-first UI remain compatibility surfaces; retired Workbench/Pipeline routes stay reachable but unmounted pending Q3. |")
    d.replace_line("A003-L", "| SOW-002 | IN | Working-root selection and validation.",
        "| SOW-002 | IN | Per-chat working-folder selection and validation with an app-scoped known-folder set. | REF-006 Section 8.1; SCA-APP-010 | PKG-07 | DEL-07-01, DEL-02-03 | OBJ-006, OBJ-008 | DEC-004; DEC-025 | FALSE | DEL-07-01 retains filesystem-policy ownership; DEL-02-03 provides the UI touchpoint; the composer folder control is shell presentation under SOW-001. |")
    d.replace_line("A004-L", "| SOW-004 | IN | Resizable dialogue/navigation/coordination/focus layout",
        "| SOW-004 | IN | Resizable left/centre/right/strip layout with per-view right-panel widths, expand state, and non-authoritative local UI state. | REF-006 Section 8.1; SCA-APP-010 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004; DEC-025 | FALSE | Versioned migration preserves prior state for rollback; additive fields only under the existing schema string. |")
    d.replace_line("A005-L", "| SOW-006 | IN | Active dialogue/persona plus Work/Agents coordination",
        "| SOW-006 | IN | Active dialogue/persona plus right-panel Who is working and read-only Session views over canonical hierarchy and selected-session replay, and Agent 0/1/2 role entry for Codex sessions with exact non-enforcement/preview posture labels. | REF-006 Section 8.2; SCA-APP-010 | PKG-02 | DEL-02-02, DEL-05-04, DEL-08-02 | OBJ-001, OBJ-007 | DEC-004; DEC-024; DEC-025 | FALSE | Selected replay is observational, read-only, and never takes the centre; the Work projection is unmounted; DEL-08-04 retains role/delegation semantics and DEL-08-05 remains the unchanged parent-child record owner. The UI presents accepted state and never infers enforcement. |")
    d.replace_line("A006-L", "| SOW-007 | IN | Contextual Pipeline category/task-scope controls",
        "| SOW-007 | IN | Presentation-neutral DECOMP/PREP/TASK/AUDIT dispatch lane semantics without an active-shell mount. | REF-006 Section 8.2; SCA-APP-010 | PKG-08 | DEL-08-03 | OBJ-001, OBJ-007 | DEC-004; DEC-025 | FALSE | DEL-08-03 is semantic owner; the contextual Pipeline presentation is retired from the active shell (code retained), so no presentation consumer is mapped. |")
    d.replace_line("A007-L", "| SOW-008 | IN | Toolkit, drafts,",
        "| SOW-008 | IN | Toolkit, drafts, explicit next-turn context references, artifact anchors, chat annotations, known folders, chat rung and declined triggers, and dialogue workspace state. | REF-006 Section 8.7; SCA-APP-010 | PKG-02 | DEL-02-04 | OBJ-001 | DEC-004; DEC-025 | FALSE | Visible artifacts are not automatic context; convenience state does not transfer session authority and never stands in for the workflow file or the session record. |")
    d.replace_line("A008-L", "| SOW-010 | IN | App-client session boot-request binding",
        "| SOW-010 | IN | App-client session boot-request binding, including per-chat delegation policy, and daemon-session conformance. | REF-006 Section 8.3; SCA-APP-010 | PKG-03 | DEL-03-02 | OBJ-002 | DEC-004; DEC-025 | FALSE | The stored delegation-policy field is Root DEL-02-11's (OI-008). |")
    d.insert_after("A009-A012-L", "| SOW-080 | IN | App-side two-job installer transaction", [
        "| SOW-081 | IN | Governed workflow files under `.chirality/workflows/` and the right-panel Workflows view with follow, pause, create, library, and bind. | SCA-APP-010 SR-23/SR-24 | PKG-07 | DEL-07-03, DEL-02-02, DEL-04-04 | OBJ-001, OBJ-006, OBJ-007 | DEC-025 | TRUE | OI-008. DEL-07-03 owns the file contract; DEL-02-02 owns the view and forms; DEL-04-04 owns the delimited roadmap-injection seam. The file steers and never records. |",
        "| SOW-082 | IN | Prompted specification ladder: `propose` tool, additive `proposal.*` event consumption, proposal card, and instruction-package proposal clauses. | SCA-APP-010 SR-24/SR-26 | PKG-06 | DEL-06-03, DEL-05-02, DEL-02-02, DEL-08-01 | OBJ-001, OBJ-005, OBJ-007 | DEC-025 | TRUE | OI-008. DEL-06-03 owns the tool; DEL-06-02 retains catalog and collision validation; DEL-05-02 consumes the event types after Root acceptance; DEL-02-02 owns the card; DEL-08-01 owns instruction-clause conformance. |",
        "| SOW-083 | IN | Per-chat delegation policy carried with the session and honoured by the managed delegation bridge. | SCA-APP-010 SR-24 | PKG-08 | DEL-08-04, DEL-03-02 | OBJ-005, OBJ-007 | DEC-025 | TRUE | OI-008 for the Root-owned session-record field. `none` is the default; no new delegation class. |",
        "| SOW-084 | IN | Layered instruction root: bundled base plus a client-owned, hash-pinned organisation layer under instruction-root protections. | SCA-APP-010 SR-25 | PKG-07 | DEL-07-01, DEL-08-01, DEL-04-04 | OBJ-006, OBJ-007 | DEC-025 | FALSE | Q14 ruled 2026-09-04 (G2-CONFIRM). DEL-07-01 owns protection and separation; DEL-08-01 owns packaging and conformance checks; DEL-04-04 composes from both layers. |",
    ])

    # ---- Coverage and Telemetry ----
    d.replace_line("A029-T1", "| Revision | v3.2 source-governed working surface amended by SCA-APP-009 |",
        "| Revision | v3.2 source-governed working surface amended by SCA-APP-010 |")
    d.replace_line("A029-T2", "| ScopeItemCount | 80 |", "| ScopeItemCount | 84 |")
    d.replace_line("A029-T3", "| OpenIssuesByType | ",
        "| OpenIssuesByType | FIRST_ADAPTER_PROBE=1, SDK_TRANSCRIPT=1, PACKAGING=1, SOURCE_COMPLETENESS=1, DOMAIN_FUTURE=1, PROVIDER_EXPANSION=1, SHARED_RUNTIME=1, SHELL_LADDER_BOUNDARY=1 |")
    d.replace_line("A029-T4", "| OpenIssueAffectedScopeCounts | ",
        "| OpenIssueAffectedScopeCounts | FIRST_ADAPTER_PROBE=3, SDK_TRANSCRIPT=1, PACKAGING=2, SOURCE_COMPLETENESS=2, DOMAIN_FUTURE=6, PROVIDER_EXPANSION=3, SHARED_RUNTIME=10, SHELL_LADDER_BOUNDARY=4 |")
    d.replace_line("A029-T5", "| Topology stability | SCA-APP-009 expressly authorizes 80 scope items,",
        "| Topology stability | SCA-APP-010 expressly authorizes 84 scope items, 10 packages, 52 deliverables, 10 objectives, and S=9/M=41/L=2/XL=0; no other topology change is accepted. |")

    # ---- Open Issues ----
    d.insert_after("A029-OI", "| OI-007 | SHARED_RUNTIME |", [
        "| OI-008 | SHELL_LADDER_BOUNDARY | SOW-010, SOW-081, SOW-082, SOW-083 | The shell redesign's specification ladder depends on three Root-owned semantics the App only presents and consumes: the root-private login home behind an app-wide account presentation (K-KEY-1; Root DEL-02-09), additive `proposal.*` event types against the closed `HarnessEvent` schema v2 (K-EVENT-3; Root DEL-02-10), and a delegation-policy field on the daemon session record (Root DEL-02-11). Q15 (leave-behind currency reporting) and Q16 (shared-folder position advance) remain owner questions. | Route one App coordination notice to Root after Gate 5; consume each contract only after its accepted return is routed to App; the owner rules Q15 and Q16 before the Workflows view's acceptance text is final. |",
    ])

    # ---- Decision Log / Change Log / Downstream notes ----
    d.insert_after("A028-DEC", "| DEC-024 | 2026-09-04 |", [
        "| DEC-025 | 2026-09-04 | SCA-APP-010 makes the centre dialogue the invariant primary surface, retires Workbench and Pipeline presentation from the active shell (code retained), unmounts the Work projection, and seats the governed-workflow file and Workflows view (SOW-081), the prompted specification ladder with the `propose` tool and `proposal.*` events (SOW-082), the per-chat delegation policy (SOW-083), and the layered instruction root with a client-owned organisation layer (SOW-084) on existing carriers, changing the Scope Ledger from 80 to 84 rows without changing topology. | Ryan Tufts adopted the shell-redesign design basis (`plans/shell-redesign_2026-09-04/`, SR-01 to SR-26), confirmed the Gate-1 envelope, accepted the Gate-2 impact assessment, ruled SOW-007's presentation half retired, and ruled Q14's organisation-layer default. Root retains login-home, event-schema, and session-record semantics (OI-008); the direct shell items are owner-seated Remaining work, not decomposition scope. |",
    ])
    d.insert_after("A028-CL", "- 2026-09-04: SCA-APP-009 seated S-1/S-2/S-4a/S-7,", [
        "- 2026-09-04: SCA-APP-010 seated the dialogue-centred shell redesign: invariant centre dialogue, Workbench/Pipeline presentation retired from the active shell, Work projection unmounted, SOW-081 to SOW-084 added on existing carriers, Vocabulary Map surface terms added, and OI-008 opened, changing the Scope Ledger from 80 to 84 rows without changing package/deliverable topology, lifecycle, dependencies, estimates, schedule, implementation authority, or release authority.",
    ])
    d.insert_after("A028-DSN", "- SCA-APP-004 selects Woven Dialogue with a Work/Agents Coordination Panel", [
        "- SCA-APP-010 supersedes the Coordination Panel presentation of SCA-APP-004 with the right-panel views and the prompted specification ladder. The centre dialogue is never hidden; Workbench, Pipeline, and the Work projection are unmounted, not deleted; workflow files steer and never record; proposals are human acts; the organisation layer is instruction root, not working root.",
    ])
    return d


def build_companion(src: str, new_decomp_sha: str) -> tuple[str, list[dict]]:
    tx = []
    old_pin = f"#candidate-sha256={DECOMP_PRE}"
    new_pin = f"#candidate-sha256={new_decomp_sha}"
    n = src.count(old_pin)
    if n != 83:
        raise SystemExit(f"FAIL_CLOSED: expected 83 decomposition pins, found {n}")
    out = src.replace(old_pin, new_pin)
    tx.append({"id": "A027-rebind", "kind": "REPLACE_ALL", "count": n, "pre": old_pin, "post": new_pin})
    lines = out.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("K-PATH-2,")]
    if len(idx) != 1:
        raise SystemExit("FAIL_CLOSED: K-PATH-2 row not unique")
    old = lines[idx[0]]
    new = old
    for a, b in [
        (",DEL-06-04;DEL-07-01;DEL-07-05;DEL-09-03,", ",DEL-06-04;DEL-07-01;DEL-07-03;DEL-07-05;DEL-09-03,"),
        ("Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#SOW-027;", "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#SOW-027;projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#SOW-081;"),
    ]:
        if new.count(a) != 1:
            raise SystemExit(f"FAIL_CLOSED: K-PATH-2 substring count {new.count(a)}: {a!r}")
        new = new.replace(a, b)
    tx.append({"id": "A027-kpath2", "kind": "EDIT_LINE", "line": idx[0] + 1, "pre": old, "post": new})
    lines[idx[0]] = new
    return "\n".join(lines), tx


def validate(decomp: str, companion: str) -> dict:
    lines = decomp.split("\n")
    ssow = [l for l in lines if re.match(r"^\| SOW-\d{3} \| (IN|OUT|TBD) \| ", l)]
    # SSOW rows have SourceRef in column 3; ledger rows have a statement. Split by section.
    sec = {}
    cur = None
    for l in lines:
        if l.startswith("## "):
            cur = l
        sec.setdefault(cur, []).append(l)
    ssow_sec = next(k for k in sec if k and k.startswith("## 5."))
    ledger_sec = next(k for k in sec if k and k.startswith("## 9."))
    deliv_sec = next(k for k in sec if k and k.startswith("## 8."))
    pkg_sec = next(k for k in sec if k and k.startswith("## 7."))
    obj_sec = next(k for k in sec if k and k.startswith("## 6."))
    ssow_rows = [l for l in sec[ssow_sec] if re.match(r"^\| SOW-\d{3} \|", l)]
    ledger_rows = [l for l in sec[ledger_sec] if re.match(r"^\| SOW-\d{3} \|", l)]
    del_rows = [l for l in sec[deliv_sec] if re.match(r"^\| DEL-\d{2}-\d{2} \|", l)]
    pkg_rows = [l for l in sec[pkg_sec] if re.match(r"^\| PKG-\d{2} \|", l)]
    obj_rows = [l for l in sec[obj_sec] if re.match(r"^\| OBJ-\d{3} \|", l)]

    def cells(l):
        return [c.strip() for c in l.strip().strip("|").split("|")]

    ssow_ids = [cells(l)[0] for l in ssow_rows]
    ledger_ids = [cells(l)[0] for l in ledger_rows]
    status = {}
    for l in ledger_rows:
        c = cells(l)
        status[c[1]] = status.get(c[1], 0) + 1
    # reverse view parity
    covers = {}
    envelopes = {}
    for l in del_rows:
        c = cells(l)
        covers[c[0]] = set(x.strip() for x in c[6].split(",") if x.strip())
        envelopes[c[8]] = envelopes.get(c[8], 0) + 1
    ledger_map = {}
    for l in ledger_rows:
        c = cells(l)
        ledger_map[c[0]] = set(x.strip() for x in c[5].split(",") if x.strip())
    missing, extra = [], []
    for sow, dels in ledger_map.items():
        for dl in dels:
            if dl not in covers:
                missing.append((sow, dl, "deliverable row absent"))
            elif sow not in covers[dl]:
                missing.append((sow, dl, "ledger->deliverable not reflected"))
    for dl, sows in covers.items():
        for sow in sows:
            if sow not in ledger_map or dl not in ledger_map[sow]:
                extra.append((dl, sow, "deliverable->ledger not reflected"))
    reader = csv.reader(io.StringIO(companion))
    crow = list(reader)
    header, body = crow[0], crow[1:]
    fams = {r[1] for r in body}
    return {
        "ssow_count": len(ssow_rows),
        "ledger_count": len(ledger_rows),
        "ssow_ids_unique": len(set(ssow_ids)) == len(ssow_ids),
        "ids_equal": set(ssow_ids) == set(ledger_ids),
        "status_counts": status,
        "package_count": len(pkg_rows),
        "deliverable_count": len(del_rows),
        "objective_count": len(obj_rows),
        "envelopes": envelopes,
        "reverse_view_missing": missing,
        "reverse_view_extra": extra,
        "companion_columns": len(header),
        "companion_rows": len(body),
        "companion_unique_ids": len({r[0] for r in body}),
        "companion_families": len(fams),
        "companion_bad_width": [r[0] for r in body if len(r) != len(header)],
    }


def main() -> int:
    src = DECOMP.read_bytes()
    if sha256(src) != DECOMP_PRE:
        raise SystemExit(f"FAIL_CLOSED: decomposition pre-image drift: {sha256(src)}")
    csrc = COMPANION.read_bytes()
    if sha256(csrc) != COMPANION_PRE:
        raise SystemExit(f"FAIL_CLOSED: companion pre-image drift: {sha256(csrc)}")
    for pre in ("SOW-081", "SOW-082", "SOW-083", "SOW-084", "DEC-025", "OI-008"):
        if pre.encode() in src:
            raise SystemExit(f"FAIL_CLOSED: new ID already present: {pre}")

    d = build_decomposition(src.decode("utf-8"))
    out = d.text().encode("utf-8")
    DECOMP_OUT.write_bytes(out)
    dsha = sha256(out)
    cout, ctx = build_companion(csrc.decode("utf-8"), dsha)
    COMPANION_OUT.write_bytes(cout.encode("utf-8"))
    csha = sha256(cout.encode("utf-8"))
    TX_OUT.write_text(json.dumps({"decomposition": d.tx, "companion": ctx}, indent=2, ensure_ascii=False) + "\n")
    v = validate(out.decode("utf-8"), cout)
    print(json.dumps({"decomposition_postimage_sha256": dsha, "companion_postimage_sha256": csha, "validation": v}, indent=2))
    ok = (v["ssow_count"] == 84 and v["ledger_count"] == 84 and v["ids_equal"] and v["ssow_ids_unique"]
          and v["package_count"] == 10 and v["deliverable_count"] == 52 and v["objective_count"] == 10
          and not v["reverse_view_missing"] and not v["reverse_view_extra"]
          and v["companion_rows"] == 83 and v["companion_unique_ids"] == 83 and v["companion_families"] == 50
          and v["companion_columns"] == 18 and not v["companion_bad_width"]
          and v["envelopes"] == {"S": 9, "M": 41, "L": 2})
    print("VALIDATION:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
