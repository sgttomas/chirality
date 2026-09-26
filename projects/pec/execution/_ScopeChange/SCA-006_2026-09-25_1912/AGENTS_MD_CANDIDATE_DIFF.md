---
doc_id: PEC-SCA006-CP2-AGENTS-MD-CANDIDATE-DIFF
doc_kind: scope_change.instruction_candidate_diff
status: candidate_pending_checkpoint_2
amendment: SCA-006
prepared: 2026-09-25
revision: 2 (r1 manager decisions on observations O-2, O-3 and O-5, see §8; r2 I1 hunks made true at origin/main 7f33b4dd5, see §4.2)
prepared_by: TASK child T3 (Type 2) under the WORKING_ITEMS manager for brief B5, HELP_HUMAN undertaking HELP-HUMAN-PEC-20260925-POST-SCA005, work-graph node R2; roles instruction-asserted, not mechanically enforced
preimage: projects/pec/AGENTS.md
preimage_sha256: c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a
candidate_with_I1: CP2_CANDIDATE/AGENTS.candidate.md
candidate_with_I1_sha256: 49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d
candidate_with_I1_lines: 454
candidate_without_I1: CP2_CANDIDATE/AGENTS.candidate_without_I1.md
candidate_without_I1_sha256: a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188
candidate_without_I1_lines: 448
preimage_lines: 434
---

# SCA-006 checkpoint 2 — `projects/pec/AGENTS.md` instruction candidate and diff

This file prepares the exact `projects/pec/AGENTS.md` text for the owner's
SCA-006 checkpoint-2 decision. It is a candidate. It changes no live file,
records no owner act, and grants nothing. Under INS-a (selected at checkpoint
1) the accepted text is applied at checkpoint 3 as an instruction tranche with
the manifest drafted in §6. The two candidate files are named
`AGENTS.candidate*.md` rather than `AGENTS.md` so that no harness discovers
them as live nested instructions.

Two candidates are offered. They differ only by the I1 hunks of §4:

- `CP2_CANDIDATE/AGENTS.candidate.md` carries SCA-006 Seq 14–17 plus the
  work-graph node I1 residual corrections;
- `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` carries SCA-006 Seq 14–17
  only.

Both hashes are computed with every acceptance-bound slot at its default
value (§9).

## 1. Identities

| Item | Value |
|---|---|
| Amendment | SCA-006, snapshot `execution/_ScopeChange/SCA-006_2026-09-25_1912/` (paths in this file are relative to `projects/pec/` unless they start with `projects/`, `docs/` or `execution/_Coordination/NOTICE`) |
| Undertaking | HELP_HUMAN `HELP-HUMAN-PEC-20260925-POST-SCA005`, node R2 (checkpoint 2); I1 is the graph's residual-correction node, which "may ride R3's instruction change" |
| Brief | B5 `BRIEF_T3_AGENTS.md`, SHA-256 `508761093efb04e63b780623c3dd734ccc58b45c09f4581bf9af8966ddb44175` (manager scratchpad; not in the repository) |
| Shared canon | B5 `CANON.md`, SHA-256 `5617eb1c0ead3cfb04246945fc033b3e5c0744b7d091ac2d47affae4cb0e67d0` (manager scratchpad; binding for the texts of §3) |
| Executor | TASK child T3, claude-opus-5-5 at high reasoning effort as steered; the runtime exposed that model name; no delegation |
| Repository basis | Preimage basis: `4d5f7b91102b7106ff74b98118b2bda2fe873f36` (the SCA-006 hunks and the preimage `c9d3b44d…` are unchanged there and at the current head). I1 facts (roles, workflows, skills) verified at `origin/main` `7f33b4dd51f93553f17607167077c28ddd773ff6`, merged into the branch by the manager as HEAD `005a454454cc5f7232dc630bc85c605ea7c35372` (revision 2). This task made no Git state change. Other TASK children wrote their own untracked files in the same snapshot concurrently (`PRD_V2_4_SUCCESSOR_DIFF.md`, `CP2_CANDIDATE/docs/`, `CP2_CANDIDATE/_Decomposition/`); this task did not read or touch them |
| Preimage | `projects/pec/AGENTS.md`, SHA-256 `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a`, 434 lines |
| Candidate with I1 | `CP2_CANDIDATE/AGENTS.candidate.md`, SHA-256 `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d`, 454 lines |
| Candidate without I1 | `CP2_CANDIDATE/AGENTS.candidate_without_I1.md`, SHA-256 `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188`, 448 lines |
| Draft tranche manifest | full text in §6.1 (SHA-256 of the draft bytes `852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45`); not written into `docs/` |
| Draft notices | full texts in §6.3 (Root `43cfa3183ed242d7ec3d349e77cce6403e2355bc8965ed93560f2917c132b930`, App `eb927e1f061fd81760079868e78ee288134d180ad41a9c20c0bbdf8ed00b704a`, Runtime `385e5e2f5495634470c1c3439b6c8937edc88074132b4f89de211b67ffadc8bc`) |

## 2. Basis (every hash recomputed before drafting; all matched)

| File | SHA-256 | Use |
|---|---|---|
| `projects/pec/AGENTS.md` (preimage) | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` | the text amended |
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` | instruction-change and notice rules |
| `SCA-006_2026-09-25_1912/Impact_Assessment.md` (accepted at checkpoint 1) | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` | Annex B loci (AGENTS.md L40–43, L47–50, L26–32 with L180–189, L409); §8.3 instruction route |
| `SCA-006_2026-09-25_1912/Amendment_Actions.csv` (accepted intake) | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` | Seq 14–17 |
| `docs/governance_harness/tranche_manifests/PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml` (precedent) | `0ccddebe999f1ee3a35ff0672069fce20302ab9ae56517836e825c68a3beb783` | manifest shape |
| `execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (precedent) | `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b` | tranche precedent |
| `agents/registry.json` | `767fdfe25f3722b8b0428cdd4146182d54c67e0f601e11e9c3321ffc5f868cf4` | role identities (I1) |
| `workflows/index.json` at `7f33b4dd5` (revision 2) | `083277c5c8eb35d28a1a39ed99f9a9ec829e673df3d8b556c2193fcbb4ac75bb` (was `213a0738…` at `4d5f7b911`) | workflow and skill identities, `legacy.retiredRoles`, `legacy.historicalOnly` (I1) |
| `workflows/construct-local-work-graph/WORKFLOW.md` at `7f33b4dd5` | `3e197c9ddc75d40daa02929dc3df653a66f7d76ab6996239e823bba647dd9dc3` | implementation-node requirements (L62–64) (I1) |
| `agents/AGENT_HELPS_HUMANS.md` | `a0c9fb9443d8671d694c1f7b24ff3c402ffd626c781a2739342c938f2f3c3d1e` | consulted, as the brief permits, for instruction-candidate comparison |
| `projects/chirality-runtime/…/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md` | `2e66ee8681800307f5675db63c9870413bb6148bc5cace8e3423ac89b4eeaefe` | Runtime notice basis (read scope item 5, L459–461) |
| `projects/chirality-runtime/…/_run_records/DEL-02-06-RUNTIME-SPEC-001/clients/SOURCE_PINS.json` | `796cd368d44d67b4371cc47b7596740e6d0edddba2035a76dc27c8e764e2f71b` | Runtime notice basis (S4–S6) |

Owner acts relied on (observed as records on this branch; none is claimed
beyond its record):

- SCA-006 checkpoint 1, verbatim "SCA-006 CP1: accept; DQ a; ENV a; BUD a;
  GATE a; INS a; R-C excluded"
  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md` L33).
- `D-PEC-90` R-A (`execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`),
  grant item 3: prepare the exact PRD and `projects/pec/AGENTS.md` amendment.

No checkpoint-2 act exists yet. §6 and §9 carry it only as a slot.

## 3. SCA-006 hunks (Seq 14–17)

Diffs run from the preimage to `AGENTS.candidate_without_I1.md`; the line
numbers on the left are preimage lines and on the right candidate-without-I1
lines. Each hunk uses the canonical text of CANON §4 verbatim, with line
wrapping fitted to the file, except for two manager-directed fittings made in
revision 1 (§3.5): "PRD §12" in the K-02 gloss and the front-matter
`amended:` line as a Seq 16 lineage hunk. No other SCA-006 byte changes.

### 3.1 Seq 14 — K-02 gloss (Annex B: L40–43)

"PEC output is never citable as authority. Rulings and lifecycle state
remain file-native (K-AUTH-1)." is kept byte-for-byte: L40–41 are unchanged,
and the changed L42 keeps its first words "view, or verdict is labeled
non-authoritative data". The verify-before-rely sentence is replaced by the
canonical text, with "§12" written "PRD §12" as a manager-directed fitting
(revision 1, O-2).

```diff
@@ -42,2 +45,8 @@
-  view, or verdict is labeled non-authoritative data, verified against its
-  cited source before reliance.
+  view, or verdict is labeled non-authoritative data in that authority sense.
+  Operational reliance on it (acting on a record-tier claim as true as of its
+  examined-through SHA, within the pin, coverage and tier the response
+  declares, with file fallback; PEC-K-03, `D-PEC-90`) applies only to a PEC
+  release whose PRD §12 reliance-advertisement gate has passed. Until then,
+  read the files directly. Operational reliance is distinct from the
+  reliance-hold control (§Active Reliance Holds) and from professional
+  reliance.
```

### 3.2 Seq 15 — consumer-owned-use bullet (Annex B: L47–50)

"PEC is pull-oriented, mode-capable, and never forced." is kept; the bullet
becomes the canonical text.

```diff
@@ -48,3 +57,6 @@
-  and never forced. An explicitly enabled consumer owns whether and when it
-  consumes and whether it injects labeled PEC data; no external cadence or
-  receiving-loop duty is inferred (`D-PEC-67`, `D-PEC-68`).
+  and never forced. An explicitly enabled consumer, whether a harness or an
+  agent querying through tool calls under the read-only `agent` access class,
+  owns whether and when it consumes and whether it injects labeled PEC data;
+  no external cadence or receiving-loop duty is inferred (`D-PEC-67`,
+  `D-PEC-68`, `D-PEC-90`). Injected or queried PEC data carries its reliance
+  envelope (PEC-ORI-007).
```

### 3.3 Seq 16 — lineage (Annex B: L26–32; L180–189; front matter L6)

Front matter (manager-directed, revision 1, O-3). The `amended:` line is
lineage and takes the date the tranche is applied at checkpoint 3 (an
application-date slot, §9); the earlier adoption stays named.

```diff
@@ -6 +6 @@
-amended: 2026-09-25 (shared development-loop adoption under D-PEC-94)
+amended: 2026-09-25 (SCA-006 operational-reliance instruction tranche; earlier, shared development-loop adoption under D-PEC-94)
```

Product Posture names PRD v2.4 and adds the v2.4 lineage item. The sentence
"Implementation does not exist yet; nothing in the PRD is an implementation
mandate." is not an SCA-006 locus; its words are unchanged and it is only
re-wrapped onto its own lines (without-I1 L35–36) so that I1 (§4.1) can
replace whole lines without touching SCA-006 bytes.

```diff
@@ -28 +28 @@
-loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.3 is the
+loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.4 is the
@@ -32,2 +32,5 @@
-adopted through SCA-005 checkpoint group 2 under `D-PEC-92`). Implementation
-does not exist yet; nothing in the PRD is an implementation mandate.
+adopted through SCA-005 checkpoint group 2 under `D-PEC-92`; the v2.4
+successor, carrying the `D-PEC-90` operational-reliance direction, adopted
+through SCA-006 checkpoint group 2).
+Implementation does not exist yet; nothing in the PRD is an implementation
+mandate.
```

Governance Pointers gain `D-PEC-90` and the SCA-006 checkpoint-group-2
adoption of PRD v2.4, with the group-2 snapshot folder as the pointer (no
D-PEC number is named for the adoption, per CANON §1). The items are appended
at the end of the existing parenthesis, which changes one preimage line.

```diff
@@ -189 +201,3 @@
-  shared development-loop adoption)
+  shared development-loop adoption; `D-PEC-90` operational reliance on PEC
+  data (R-A); SCA-006 checkpoint group 2 — PRD v2.4 adopted
+  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`))
```

### 3.4 Seq 17 — "Product release/reconciliation work" checks row (Annex B: L409)

```diff
@@ -409 +423 @@
-| Product release/reconciliation work | The packet's standing kill test and practitioner-harness parity diff, with rerunnable evidence; absent implementations are unmet gates, never fabricated passes |
+| Product release/reconciliation work | The packet's standing kill test and practitioner-harness parity diff, with rerunnable evidence; a release that advertises operational reliance also passes the PRD §12 reliance-advertisement gate (parity clean or explained, coverage statements under seeded feed failures, the reliance envelope, parser fixture suites, the kill test); absent implementations are unmet gates, never fabricated passes |
```

### 3.5 Conformance to CANON §4

| Locus | Canonical text | Adaptation |
|---|---|---|
| Seq 14 | CANON §4 K-02 gloss, both kept sentences and the replacement | line wrapping; "whose §12 reliance-advertisement gate" written "whose PRD §12 reliance-advertisement gate" as a manager-directed fitting of the canon text (revision 1, O-2), matching the canon's own "PRD §12" in the Seq 17 row |
| Seq 15 | CANON §4 consumer-owned use, verbatim | line wrapping only |
| Seq 16 | "`docs/PRD.md` v2.4"; lineage item "the v2.4 successor, carrying the `D-PEC-90` operational-reliance direction, adopted through SCA-006 checkpoint group 2", verbatim; pointers "`D-PEC-90` operational reliance on PEC data (R-A)" and "SCA-006 checkpoint group 2 — PRD v2.4 adopted" with the group-2 folder slot | list punctuation fitted to the host list; plus the manager-directed front-matter lineage line `amended: 2026-09-25 (SCA-006 operational-reliance instruction tranche; earlier, shared development-loop adoption under D-PEC-94)` (revision 1, O-3), whose date is an application-date slot |
| Seq 17 | CANON §4 checks row, verbatim | table-cell syntax |

## 4. I1 residual corrections (separate from SCA-006)

These hunks are the complete difference between the two candidates. They are
not SCA-006 actions; they come from work-graph node I1
(`execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`
L45 and L69: "Implementation does not exist yet"; pre-v3 role names), also
recorded in the loop-migration return
`execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/M1_PEC_LOOP_MIGRATION.md`
§7 item 5 (L245–247). The owner decides at checkpoint 2 whether I1 rides this
tranche by choosing a candidate.

Proof that the I1 hunks are exactly the difference:
`diff -U0 CP2_CANDIDATE/AGENTS.candidate_without_I1.md CP2_CANDIDATE/AGENTS.candidate.md`
yields exactly the four hunks below and nothing else; and the preimage-to-
without-I1 diff (§3) contains no I1 text. The build script applies the six
SCA-006 replacements to the preimage, writes the without-I1 file, then applies
the nine I1 replacements (each asserted to match exactly once) to that text
to write the full candidate.

### 4.1 I1 (i) — "Implementation does not exist yet" (Product Posture)

```diff
@@ -35,2 +35,4 @@
-Implementation does not exist yet; nothing in the PRD is an implementation
-mandate.
+Implementation so far consists of owner-ruled `v2/**` source slices
+(`D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84`, `D-PEC-85`, `D-PEC-87`,
+`D-PEC-89`, `D-PEC-91`); no consumer surface exists yet, and nothing in the
+PRD is an implementation mandate.
```

Evidence. The PEC decision register
(`execution/_Coordination/_DECISIONS/_REGISTER.md`) and Git history show
owner-ruled `v2/**` source slices:

| Decision | Slice | Commit(s) adding or changing `projects/pec/v2/` | Register state |
|---|---|---|---|
| `D-PEC-74` O-A | DEL-08-02 API contract schema, tests, fixtures | `e9fec7fff` (2026-08-01) | RULED / DEL-08-02 CHECKING / exact bytes accepted |
| `D-PEC-75` O-A | DEL-01-06 loop registry (`v2/config/loops*.json`, `pec_v2` port and adapter, tests) | `d4f53a70e` (2026-08-02) | RULED O-A; lifecycle `INITIALIZED` under HOLD |
| `D-PEC-77` O-A / G-A | DEL-01-05 enforcement (`v2/tools/check_service_core_posture.py`, `v2/docs/SERVICE_CORE_POSTURE.md`, enforcement tests) | `34134e093` (2026-08-03) | RULED; exact artifacts accepted |
| `D-PEC-84` S-A | DEL-01-05 bounded scanner repair | `52bb1dddc` (2026-09-08) | RULED |
| `D-PEC-85` P-A | DEL-01-03 store lifecycle and content-minimal guard | `c49bf7938` (2026-09-08) | RULED / EFFECTIVE ON MERGE |
| `D-PEC-87` C-A | DEL-01-03 correction slice R1–R8 | `91830dde8` (PR #893) | RULED / EFFECTIVE ON MERGE |
| `D-PEC-89` A | DEL-01-03 exact-type closure R9–R14 | `4b155c2e3` (PR #897) | RULED A / EFFECTIVE ON MERGE |
| `D-PEC-91` A-53 | DEL-01-03 COUNT domain R15–R17 | `d9dcb0126` | RULED A-53 / EFFECTIVE ON MERGE |

`git log -- projects/pec/v2` lists exactly these commits plus `ca49b846d`,
the `D-PEC-80` path migration, which edited path strings in five existing
DEL-01-06 files and added no implementation. `docs/STATUS.md` L197–200 names
the slices "granted by `D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84` S-A and
`D-PEC-85` P-A"; the register adds `D-PEC-87`, `D-PEC-89` and `D-PEC-91`.
The M1 return cited only `D-PEC-87/89/91`; the list above is the verified,
complete set. "No consumer surface exists yet" is the `D-PEC-90` ruling's own
clarification ("the point it supports, that no consumer surface exists yet,
holds"). It keeps the replaced sentence's force that PEC is not usable now,
which matters for the operational-reliance gating of §3.1. "Nothing in the
PRD is an implementation mandate" is kept verbatim.

### 4.2 I1 (ii) — pre-v3 role names in the Primary Agents table

```diff
@@ -116 +118 @@
-| Agent | Type | Role in this project |
+| Role and method | Type | Role in this project |
@@ -118,3 +120,3 @@
-| `SOFTWARE_DECOMP` | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
-| `PROJECT_SETUP` | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
-| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the five `software-*` TASK skills (roster: root `AGENTS.md` agent index and `{REPO_ROOT}/skills/software-*`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
+| `WORKING_ITEMS` with `software-decomp` (formerly `SOFTWARE_DECOMP`) | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
+| `WORKING_ITEMS` with `project-setup` (formerly `PROJECT_SETUP`) | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
+| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the `software-repository-reconnaissance` and `software-test-planning` workflows and the `software-code-review` and `software-defect-diagnosis` skills, with implementation commissioned as a bounded TASK assignment under the implementation-node requirements of `construct-local-work-graph` (catalog: `{REPO_ROOT}/workflows/index.json`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
@@ -122,5 +124,9 @@
-| `CHANGE` | 1 | Performs scoped Git/file-state closeout for validated tranches. CHANGE owns Git state; PEC never will. |
-| `REVIEW` | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
-| `RECONCILIATION` | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
-| `RESEARCH` | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
-| `AUDIT_*` | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |
+| `WORKING_ITEMS` with the project `chirality-change` skill (formerly `CHANGE`, whose legacy mapping is the `change` workflow) | 1 | Performs scoped Git/file-state closeout for validated tranches. The agent performing it owns Git state; PEC never will. |
+| `WORKING_ITEMS` with `review` (formerly `REVIEW`) | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
+| `WORKING_ITEMS` with `reconciliation` (formerly `RECONCILIATION`) | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
+| `WORKING_ITEMS` with `research-orchestration` (formerly `RESEARCH`) | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
+| `TASK` with an `audit-*` workflow (formerly `AUDIT_*`) | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |
+
+The roles are Root's four (`{REPO_ROOT}/agents/registry.json`). The former
+agent names map to these role and method pairs in
+`{REPO_ROOT}/workflows/index.json` (`legacy.retiredRoles`).
```

Evidence and identities used (revision 2: all rechecked at `7f33b4dd5`
against `workflows/index.json` `083277c5…` and `agents/registry.json`
`767fdfe2…`, whose roles are HELP_HUMAN, HELPS_HUMANS, WORKING_ITEMS and TASK;
every named method's package file exists):

| Preimage row | Candidate label | Where defined |
|---|---|---|
| `SOFTWARE_DECOMP` (1) | `WORKING_ITEMS` with `software-decomp` | `workflows/index.json` `legacy.retiredRoles.SOFTWARE_DECOMP` = {role WORKING_ITEMS, workflow software-decomp}; `workflows/software-decomp/WORKFLOW.md` |
| `PROJECT_SETUP` (1) | `WORKING_ITEMS` with `project-setup` | `legacy.retiredRoles.PROJECT_SETUP`; `workflows/project-setup/WORKFLOW.md` |
| `WORKING_ITEMS` (1): "five `software-*` TASK skills (roster: root `AGENTS.md` agent index and `{REPO_ROOT}/skills/software-*`)" | same role; the current software methods named with their kinds, and implementation "commissioned as a bounded TASK assignment under the implementation-node requirements of `construct-local-work-graph`"; the catalog pointer and the `SOFTWARE_WORKFLOW_PROFILE.md` conformance clause kept | Root `AGENTS.md` has no agent index and `skills/` does not exist. At `7f33b4dd5`, `workflows/index.json` lists `software-repository-reconnaissance` and `software-test-planning` as bundled workflows (`workflows/<name>/WORKFLOW.md`) and `software-code-review` and `software-defect-diagnosis` as bundled skills (`.agents/skills/<name>/SKILL.md`; no workflow package remains). `software-bounded-implementation` is retired with no successor and listed in `legacy.historicalOnly`; it is not named. Root commit `ea5009d05` (tranche `ROOT-WORKFLOW-WAVE2A-EXECUTION-20260926`) and PEC's notice `execution/_Coordination/NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md` say implementation "is commissioned as a bounded TASK assignment" and that `construct-local-work-graph` states the implementation-node requirements (its `WORKFLOW.md` L62: "An implementation node is a bounded TASK assignment."). `software-decomp` is also `software-*` but is a decomposition method, so the methods are named rather than globbed |
| `TASK` (2) | unchanged | `agents/registry.json` |
| `CHANGE` (1) | `WORKING_ITEMS` with the project `chirality-change` skill (the legacy `change` workflow named only as the retired role's mapping) | `legacy.retiredRoles.CHANGE` = {role WORKING_ITEMS, workflow change, canonical_successor skill chirality-change (project)}; index kind `skill`, source `project`, execution roles HELPS_HUMANS, WORKING_ITEMS, TASK; `.agents/skills/chirality-change/SKILL.md`; Root `AGENTS.md` cites that skill for PR records, and at `7f33b4dd5` the Root loop names it for Git closeout (`execution/_Coordination/LOOP_INIT.md` L19). "CHANGE owns Git state; PEC never will." becomes "The agent performing it owns Git state; PEC never will." |
| `REVIEW` (1) | `WORKING_ITEMS` with `review` | `legacy.retiredRoles.REVIEW`; `workflows/review/WORKFLOW.md` |
| `RECONCILIATION` (1) | `WORKING_ITEMS` with `reconciliation` | `legacy.retiredRoles.RECONCILIATION`; `workflows/reconciliation/WORKFLOW.md` |
| `RESEARCH` (1) | `WORKING_ITEMS` with `research-orchestration` | `legacy.retiredRoles.RESEARCH`; `workflows/research-orchestration/WORKFLOW.md` |
| `AUDIT_*` (2) | `TASK` with an `audit-*` workflow | `legacy.retiredRoles.AUDIT_*` (seven entries, each role TASK); `workflows/audit-*/WORKFLOW.md` |

Each row's "Role in this project" text is unchanged except the `WORKING_ITEMS`
method list and the one `CHANGE` sentence above; the Type column is unchanged in every row, because each
retired name maps to a role of the same type. The column header "Agent"
becomes "Role and method" because the first cell now names a role and the
method it runs. The two-sentence note after the table gives the source of the
mapping and keeps the former names readable for historical receipts. The
section heading "Primary Agents", its introductory paragraph and the
"Agent Posture" table are unchanged.

## 5. Governance self-check

Method: `selfcheck.py` (scratch) splits preimage and candidates at every
`##`/`###` heading and compares each section byte-for-byte, checks eleven
invariant passages as exact substrings, and compares the checks table row by
row; `term_check.py` scans every added line for bare "reliance"/"rely" and
trailing whitespace.

**Sections.** Both candidates keep every heading, in order. Only these
sections differ from the preimage: the front matter (the `amended:` line
only), Product Posture, Governance Pointers, Development checks and evidence
(both candidates) and Primary Agents (candidate with I1 only). The title and
opening paragraph, Path Anchors, Frozen Reference Corpus, Agent Posture, Session model convention, Write Scopes And Fences,
Shared Runtime Boundary, Data And Residency, Project-Wide Execution
Discipline, Deliverable records and loop ownership, Selection and decisions,
Issue-Plan Rule, Closeout And Git Discipline and Active Reliance Holds are
byte-identical.

**(a) Authority invariants unchanged in meaning.** "PEC output is never
citable as authority." and "Rulings and lifecycle state remain file-native
(K-AUTH-1)." are byte-identical. The PEC-K-01 and PEC-K-06 bullets and the
permanent-non-goals bullet are byte-identical. "Non-authoritative" is kept
and now says explicitly that it is in the authority sense. Consumer-owned use
keeps "pull-oriented, mode-capable, and never forced", consumer ownership of
whether and when to consume and inject, and "no external cadence or
receiving-loop duty is inferred"; it adds an agent consumer and the envelope,
and cites `D-PEC-90`. The L-A1 "Active Reliance Holds" section, its preflight
command and its operation list are byte-identical, and the new K-02 text says
operational reliance "is distinct from the reliance-hold control". The
Development-checks row "Any dispatch, review, fan-in, promotion, or reliance"
(the L-A1 sense) is byte-identical.

**(b) No availability now.** The only permissive sentence, in K-02, is
conditioned: operational reliance "applies only to a PEC release whose PRD
§12 reliance-advertisement gate has passed. Until then, read the files
directly." Seq 15 describes who owns use; it grants no use. Seq 17 adds a
gate, not a capability. No PEC release exists: the register records none,
and `D-PEC-90` states that no consumer surface exists yet. With I1 the
Product Posture also says so. PEC-K-01 ("No governed act may require a PEC
read or write") is unchanged.

**(c) Fences and checks unchanged.** The F-PEC-1..4 paragraph, the whole
"Write Scopes And Fences" section (default-writable surfaces, the owner-ruled
`D-PEC` packet rule, parked source work), the "Frozen Reference Corpus"
section and the "Data And Residency" section are byte-identical. The checks
table has the same nine rows; eight are byte-identical and only "Product
release/reconciliation work" changes (Seq 17), keeping its kill test, parity
diff, rerunnable evidence and "absent implementations are unmet gates, never
fabricated passes".

**(d) Root not weakened.** The candidate adds no authority for instruction
changes: it is applied only as the tranche of §6 (Root `AGENTS.md`:
"Instruction changes require their own authorized scope and tranche
manifest") with notices to the loops that pin the changed text ("Notify each
affected project loop whose authority corpus or contract mirrors pin changed
instructions"). The Shared Runtime Boundary, Closeout And Git Discipline (Root
standing Git authorization) and "Selection and decisions" ("Never record a
ruling that did not occur; role assertion is not mechanical enforcement")
are byte-identical. The I1 table names only Root's four roles and existing
workflow and skill identities; it creates no role and delegates nothing
(`validate_instruction_entrypoints.py` PASS, §7).

**Terminology (CANON §1).** No added line uses bare "reliance" or "rely".
The scanner's only hits are line-wrap artifacts of canonical compounds
("professional / reliance." at candidate L54, without-I1 L52; "reliance /
envelope" at candidate L63, without-I1 L61) and, in the drafts
of §6, the quoted name of the superseded "verify-before-rely" precondition
and one wrapped "Operational / reliance". No D-PEC number is invented;
`D-PEC-90` exists (register row, ruling file). No trailing whitespace or tab
in any added line.

**Byte-level list of every changed line** (preimage → candidate with I1; the
without-I1 candidate is the same list minus the I1 hunks of §4, with the
Product Posture hunk ending at its L36 in the unchanged-wording form shown in
§3.3):

```diff
--- preimage projects/pec/AGENTS.md (c9d3b44d)
+++ AGENTS.candidate.md
@@ -6 +6 @@
-amended: 2026-09-25 (shared development-loop adoption under D-PEC-94)
+amended: 2026-09-25 (SCA-006 operational-reliance instruction tranche; earlier, shared development-loop adoption under D-PEC-94)
@@ -28 +28 @@
-loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.3 is the
+loop Step 0 and the deterministic parts of Step 1. `docs/PRD.md` v2.4 is the
@@ -32,2 +32,7 @@
-adopted through SCA-005 checkpoint group 2 under `D-PEC-92`). Implementation
-does not exist yet; nothing in the PRD is an implementation mandate.
+adopted through SCA-005 checkpoint group 2 under `D-PEC-92`; the v2.4
+successor, carrying the `D-PEC-90` operational-reliance direction, adopted
+through SCA-006 checkpoint group 2).
+Implementation so far consists of owner-ruled `v2/**` source slices
+(`D-PEC-74`, `D-PEC-75`, `D-PEC-77`, `D-PEC-84`, `D-PEC-85`, `D-PEC-87`,
+`D-PEC-89`, `D-PEC-91`); no consumer surface exists yet, and nothing in the
+PRD is an implementation mandate.
@@ -42,2 +47,8 @@
-  view, or verdict is labeled non-authoritative data, verified against its
-  cited source before reliance.
+  view, or verdict is labeled non-authoritative data in that authority sense.
+  Operational reliance on it (acting on a record-tier claim as true as of its
+  examined-through SHA, within the pin, coverage and tier the response
+  declares, with file fallback; PEC-K-03, `D-PEC-90`) applies only to a PEC
+  release whose PRD §12 reliance-advertisement gate has passed. Until then,
+  read the files directly. Operational reliance is distinct from the
+  reliance-hold control (§Active Reliance Holds) and from professional
+  reliance.
@@ -48,3 +59,6 @@
-  and never forced. An explicitly enabled consumer owns whether and when it
-  consumes and whether it injects labeled PEC data; no external cadence or
-  receiving-loop duty is inferred (`D-PEC-67`, `D-PEC-68`).
+  and never forced. An explicitly enabled consumer, whether a harness or an
+  agent querying through tool calls under the read-only `agent` access class,
+  owns whether and when it consumes and whether it injects labeled PEC data;
+  no external cadence or receiving-loop duty is inferred (`D-PEC-67`,
+  `D-PEC-68`, `D-PEC-90`). Injected or queried PEC data carries its reliance
+  envelope (PEC-ORI-007).
@@ -104 +118 @@
-| Agent | Type | Role in this project |
+| Role and method | Type | Role in this project |
@@ -106,3 +120,3 @@
-| `SOFTWARE_DECOMP` | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
-| `PROJECT_SETUP` | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
-| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the five `software-*` TASK skills (roster: root `AGENTS.md` agent index and `{REPO_ROOT}/skills/software-*`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
+| `WORKING_ITEMS` with `software-decomp` (formerly `SOFTWARE_DECOMP`) | 1 | Ran the decomposition over PRD v2, Gates 1–7 per `{REPO_ROOT}/docs/DECOMPOSITION_STANDARD.md` (session and acceptance state: `D-PEC-60` and `execution/_Decomposition/_LATEST.md` — this table asserts no gate state). The accepted package at `execution/_Decomposition/` is the authoritative downstream basis; no tranche is scoped from the PRD directly; post-acceptance amendment goes through the scope-change machinery, not direct edits. |
+| `WORKING_ITEMS` with `project-setup` (formerly `PROJECT_SETUP`) | 1 | Scaffolds packages/deliverables from the accepted decomposition, after acceptance and under its own packet. |
+| `WORKING_ITEMS` | 1 | Per-package activations and their work graph, using the `software-repository-reconnaissance` and `software-test-planning` workflows and the `software-code-review` and `software-defect-diagnosis` skills, with implementation commissioned as a bounded TASK assignment under the implementation-node requirements of `construct-local-work-graph` (catalog: `{REPO_ROOT}/workflows/index.json`), conforming to `{REPO_ROOT}/docs/SOFTWARE_WORKFLOW_PROFILE.md`; integrates results, validates, and prepares closeout. |
@@ -110,5 +124,5 @@
-| `CHANGE` | 1 | Performs scoped Git/file-state closeout for validated tranches. CHANGE owns Git state; PEC never will. |
-| `REVIEW` | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
-| `RECONCILIATION` | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
-| `RESEARCH` | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
-| `AUDIT_*` | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |
+| `WORKING_ITEMS` with the project `chirality-change` skill (formerly `CHANGE`, whose legacy mapping is the `change` workflow) | 1 | Performs scoped Git/file-state closeout for validated tranches. The agent performing it owns Git state; PEC never will. |
+| `WORKING_ITEMS` with `review` (formerly `REVIEW`) | 1 | Reviews outputs against scope, validation evidence, product invariants, and acceptance criteria. |
+| `WORKING_ITEMS` with `reconciliation` (formerly `RECONCILIATION`) | 1 | Detects cross-surface conflicts, stale assumptions, dependency issues, and inconsistent terminology. |
+| `WORKING_ITEMS` with `research-orchestration` (formerly `RESEARCH`) | 1 | Read-only inquiry over accepted docs, the frozen corpus, and retrieval indexes; returns cited findings without changing state. |
+| `TASK` with an `audit-*` workflow (formerly `AUDIT_*`) | 2 | Bounded checks for governance conformance, dependency closure, release-quality evidence, and epistemic integrity. |
@@ -115,0 +130,4 @@
+The roles are Root's four (`{REPO_ROOT}/agents/registry.json`). The former
+agent names map to these role and method pairs in
+`{REPO_ROOT}/workflows/index.json` (`legacy.retiredRoles`).
+
@@ -189 +207,3 @@
-  shared development-loop adoption)
+  shared development-loop adoption; `D-PEC-90` operational reliance on PEC
+  data (R-A); SCA-006 checkpoint group 2 — PRD v2.4 adopted
+  (`execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`))
@@ -409 +429 @@
-| Product release/reconciliation work | The packet's standing kill test and practitioner-harness parity diff, with rerunnable evidence; absent implementations are unmet gates, never fabricated passes |
+| Product release/reconciliation work | The packet's standing kill test and practitioner-harness parity diff, with rerunnable evidence; a release that advertises operational reliance also passes the PRD §12 reliance-advertisement gate (parity clean or explained, coverage statements under seeded feed failures, the reliance envelope, parser fixture suites, the kill test); absent implementations are unmet gates, never fabricated passes |
```

| Preimage lines | Candidate-with-I1 lines | Source |
|---|---|---|
| 6 | 6 | Seq 16 (front-matter `amended:`, revision 1) |
| 28 | 28 | Seq 16 |
| 32–33 | 32–38 | Seq 16 (32–34) + I1 (i) (35–38) |
| 42–43 | 47–54 | Seq 14 |
| 48–50 | 59–64 | Seq 15 |
| 104 | 118 | I1 (ii) header |
| 106–108 | 120–122 | I1 (ii) |
| 110–114 | 124–128 | I1 (ii) |
| (inserted after 115) | 130–133 (three note lines, blank) | I1 (ii) note |
| 189 | 207–209 | Seq 16 |
| 409 | 429 | Seq 17 |

Without-I1 candidate lines for the same SCA-006 hunks: 6; 28; 32–36; 45–52;
57–62; 201–203; 423.

## 6. Instruction-tranche manifest and notices (drafts)

### 6.1 Manifest draft

To be written at checkpoint 3 as
`docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml`.
The date part of the ID, the dates, the basis commit and the notice file
dates are slots (§9). `[SLOT CP2-ACT …]` and `[SLOT CP2-VARIANT …]` must be
replaced by the verbatim checkpoint-2 act and the accepted candidate before
the manifest is written.

```yaml
schema: instruction-tranche-manifest/v1
tranche_id: PEC-SCA006-OPERATIONAL-RELIANCE-20260925
title: PEC instruction tranche for SCA-006 (operational reliance on PEC data in projects/pec/AGENTS.md)
date: 2026-09-25
basis: 4d5f7b91102b7106ff74b98118b2bda2fe873f36
instruction_surface_paths:
  - projects/pec/AGENTS.md
  - docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml
  - execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
  - projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
  - projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
candidate_paths:
  - projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md
  - projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate_without_I1.md
  - projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/AGENTS_MD_CANDIDATE_DIFF.md
m2_gate:
  authorization: >-
    Ryan Tufts accepted PEC SCA-006 checkpoint 1 on 2026-09-25, verbatim:
    'SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded'
    (projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md).
    INS-a selected carrying the projects/pec/AGENTS.md change (accepted intake
    Amendment_Actions.csv Seq 14-17) as an instruction tranche applied at
    checkpoint 3. The owner then accepted the exact text at checkpoint 2,
    verbatim: '[SLOT CP2-ACT: the owner's checkpoint-2 act, transcribed
    verbatim from the group-2 DECISION.md]'
    (projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md).
    The accepted candidate is [SLOT CP2-VARIANT: AGENTS.candidate.md, which
    carries SCA-006 Seq 14-17 plus the work-graph node I1 corrections, or
    AGENTS.candidate_without_I1.md, which carries SCA-006 Seq 14-17 only], as
    fixed by that act at its recorded SHA-256. D-PEC-90 R-A grant item 3
    authorized preparing the amendment. HELP_HUMAN undertaking
    HELP-HUMAN-PEC-20260925-POST-SCA005, work-graph node R3 (with node I1 if
    the accepted candidate carries it), is this instruction change's
    authorized scope. This manifest records those acts and grants none.
  authorized_by: Ryan Tufts
  authorization_date: 2026-09-25
  integration_owner: >-
    WORKING_ITEMS manager for SCA-006 checkpoint 3 (work-graph node R3) under
    HELP_HUMAN undertaking HELP-HUMAN-PEC-20260925-POST-SCA005; roles
    instruction-asserted, not mechanically enforced. HELP_HUMAN owns the merge.
  merge_gate: owner-authorized-pr
  self_merge: true
m6_notice:
  disposition: routed
  routed_to:
    - execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
    - projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
    - projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md
  rationale: >-
    PEC changes only its own instruction file; Root AGENTS.md requires notice
    to each affected loop whose authority corpus or contract mirrors pin the
    changed instructions. Root and App: D-PEC-90 grant item 2 named them as the
    recipients of PEC's operational-reliance direction, and their 2026-09-25
    D-PEC-90 notices said the PEC text would change in a later scope change;
    these notices report the adopted text (SCA-006 Impact Assessment section
    8.2, work-graph node R4). Runtime: the DEL-02-06 Scope of Work
    (projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md,
    read scope item 5) names projects/pec/AGENTS.md,
    projects/pec/execution/_Decomposition/Deliverables.csv and
    ScopeLedger.csv as read-only sources, and its run record
    _run_records/DEL-02-06-RUNTIME-SPEC-001/clients/SOURCE_PINS.json pins them
    as S4, S5 and S6; SCA-006 changes all three. The D-PEC-94 tranche
    (PEC-DEVELOPMENT-LOOP-ADOPTION-20260925) is the precedent for notifying
    Runtime of a PEC instruction change. Piping is not notified: no Piping
    file references these paths or PEC's PRD. Each notice is non-binding,
    grants nothing and asks for no write.
supersession:
  D-PEC-67: >-
    The K03-A row (PEC PRD PEC-K-03, whose verify-before-rely clause D-PEC-67
    adopted) is superseded in PRD v2.4 under D-PEC-90 R-A through SCA-006; the
    K03-A bytes stay as historical exact input and PEC-K-11 stays
    byte-identical. In projects/pec/AGENTS.md the K-02 gloss's sentence "A PEC
    value, view, or verdict is labeled non-authoritative data, verified against
    its cited source before reliance." (present since the 2026-07-24 D-PEC-59
    follow-on commit 08fabff60) is replaced by the gated operational-reliance
    text; "PEC output is never citable as authority" and K-AUTH-1 stand
    unchanged.
  D-PEC-90: >-
    Not edited. Its ruling changed no PRD or AGENTS.md bytes; its grant item 3
    authorized preparing this amendment, which SCA-006 carries. The D-PEC-67
    L-A1 reliance-hold control, its register and its preflight are unchanged.
checks:
  - python3 tools/validation/validate_instruction_entrypoints.py .
  - python3 tools/validation/validate_instruction_tranche_manifest.py
  - python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only
  - python3 -m pytest -q tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py
  - python3 tools/validation/validate_pec_loop_receipts.py --repo-root .
  - PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check (compared with the recorded baseline)
  - git diff --check <basis>..HEAD
  - sha256 of projects/pec/AGENTS.md equals the candidate SHA-256 fixed by the checkpoint-2 act, after slot substitution per CANON section 5
  - python3 execution/_Scripts/pec_reliance_hold.py --operation exact-correction-preparation for projects/pec/AGENTS.md (run from projects/pec)
rollback: >-
  Revert this tranche's commits. projects/pec/AGENTS.md returns to its
  preimage (SHA-256 c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a);
  the three notices and this manifest are deleted. The PRD and decomposition
  changes of SCA-006 checkpoint 3 are reverted by their own records, not by
  this manifest. No lifecycle, source or data state changes.
scope_limits:
  - Only projects/pec/AGENTS.md, this manifest and the three notices change under this manifest.
  - The four SCA-006 loci are the K-02 gloss, the consumer-owned-use bullet, the lineage (the front-matter amended line, the Product Posture lineage and the Governance Pointers), and the "Product release/reconciliation work" checks row; the I1 corrections, if carried, are the Product Posture implementation sentence and the Primary Agents table, applied only if the owner's checkpoint-2 act accepts them.
  - PEC-K-01, PEC-K-02, PEC-K-06, PEC-K-11, K-AUTH-1, D-GOV-01 Option A and Root PRD N-1 stand unchanged; PEC output stays never citable as authority (D-PEC-90 R-C not selected).
  - Operational reliance is available only from a PEC release that has passed the PRD section 12 reliance-advertisement gate; this manifest makes nothing usable now.
  - F-PEC-1..4, Write Scopes And Fences, the frozen-corpus rules, the default-writable surfaces, the owner-ruled D-PEC packet rule and the reliance-hold control are unchanged.
  - The Session model convention section is unchanged.
  - The tier-0 profile _DomainEngines/profiles/pec.yaml needs its own tier-0 act before any PEC tool is declared or invoked; nothing here amends it.
  - Root, App, Piping and Runtime files other than the notices are unchanged.
  - No CHECKING, ISSUED, acceptance, release or operational-reliance act.
```

Precedent mapping to `PEC-DEVELOPMENT-LOOP-ADOPTION-20260925.yaml`: same
schema, key set and order (`schema`, `tranche_id`, `title`, `date`, `basis`,
`instruction_surface_paths`, `candidate_paths`, `m2_gate` with
`owner-authorized-pr` and `self_merge: true`, `m6_notice` `routed`,
`supersession`, `checks`, `rollback`, `scope_limits`).

Revision 1 changed one line of the draft: the second `scope_limits` item now
names the front-matter `amended:` line within the lineage locus and says the
I1 corrections are applied only if the owner's checkpoint-2 act accepts them
(pre-revision draft SHA-256 `b7a58cff4058af022e3f4c575c7ac05e59f6cd8297eeb6f3d9089f6af26beb44`).

### 6.2 Notice routing and the Runtime basis

Notice filenames follow the existing convention in all three folders,
`NOTICE_<YYYY-MM-DD>_<TOPIC>.md` (Root 22, App 55 and Runtime 19 notices use
it; none uses the compact `NOTICE_<YYYYMMDD>_` form), with PEC's existing
topic style `PEC_SCA-005_…`. The brief's
`NOTICE_20260925_PEC_SCA006_OPERATIONAL_RELIANCE.md` therefore becomes
`NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md`:

- Root: `execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md`
- App: `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md`
- Runtime: `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md`

None of the three exists at the basis.

Root and App: `D-PEC-90` grant item 2 named them for the direction notices,
which exist as `NOTICE_2026-09-25_D-PEC-90_OPERATIONAL_RELIANCE_ON_PEC_DATA.md`
in both folders and say "No PEC text changes yet"; Impact Assessment §8.2 says
"The R4 notices announce the adopted text".

Runtime (verified): `projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/ScopeOfWork.md`
L459–461, in "Accepted read basis and exact first-activation read scope" item
5, names `projects/pec/AGENTS.md`, `projects/pec/execution/_Decomposition/Deliverables.csv`
and `projects/pec/execution/_Decomposition/ScopeLedger.csv` "read-only, solely
to classify actual obligations or coordination effects". The run record
`_run_records/DEL-02-06-RUNTIME-SPEC-001/clients/SOURCE_PINS.json` pins them
as S4 (`46689c36…3846`), S5 (`49f90448…6b72`) and S6 (`2103afa2…e25`), and
`AFFECTED_CLIENT_CENSUS.md` L13 uses S4–S6 to classify PEC v2 as
`UNRESOLVED`. All three pins are already historical: the current files hash
to `c9d3b44d…197a`, `b8628fc4…d65a` and `83152a94…9df`. SCA-006 changes all
three (this tranche; decomposition revision 1.6, CANON §3 Seq 20–32). The
`D-PEC-94` tranche also notified Runtime.

Piping: `grep -rl` over `projects/chirality-piping` for these three paths and
`projects/pec/docs/PRD.md` finds nothing, so no Piping notice is drafted. The
same grep over App finds only a PRD-path string pin
(`frontend/src/__tests__/contract-pins.manifest.ts` L447, `contains`
`projects/pec/docs/PRD.md`) and a register citation, neither of which pins
`projects/pec/AGENTS.md` bytes.

### 6.3 Notice drafts

Each says what changed, that it grants nothing and asks for no write, and
that operational reliance begins only at a PEC release that passes the §12
gate. Each describes the checkpoint-2 adoption in the past tense because it
is sent at checkpoint 3, after that act; if the owner does not accept
checkpoint 2, no notice is sent.

Root:

```markdown
# Coordination Notice — PEC SCA-006: operational reliance on PEC data adopted in PEC's PRD and instructions

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Root
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`

PEC scope change SCA-006 carries the `D-PEC-90` R-A direction into PEC's
text. The owner adopted PEC PRD v2.4 by accepting SCA-006 checkpoint group 2
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`).
PEC-K-03 now describes operational reliance: an explicitly PEC-enabled
consumer may act on a record-tier claim as true as of its examined-through
SHA, within the pin, coverage and trust tier each response declares
(PEC-ORI-007), with file fallback. PEC-API-006 adds response-size budgets,
PEC-API-007 a read-only query surface for agent tool calls under a new
`agent` access class, and PRD §12 a standing reliance-advertisement gate.
`projects/pec/AGENTS.md` changes its K-02 gloss, consumer-owned-use bullet,
lineage and one checks row. Authority is unchanged: PEC output stays never
citable as authority (`D-PEC-90` R-C was not selected), and PEC-K-01,
PEC-K-02, K-AUTH-1, `D-GOV-01` Option A and Root PRD N-1 stand as written.

Changed paths and authority:
`docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml`.

For this loop: operational reliance begins only at a PEC release that passes
the PRD §12 reliance-advertisement gate. No PEC release has passed it, so
nothing here is usable now. The open reading question in PEC's earlier `D-PEC-90`
notice (Root `AGENTS.md` lines 54–55 and Root PRD N-1) is unchanged and stays
Root's to confirm, amend or decline.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
```

App:

```markdown
# Coordination Notice — PEC SCA-006: operational reliance on PEC data adopted in PEC's PRD and instructions

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality App (app-dev)
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`

PEC's earlier `D-PEC-90` notice said PEC would amend its PRD and
`projects/pec/AGENTS.md` in a later scope change. SCA-006 is that change. The
owner adopted PEC PRD v2.4 by accepting SCA-006 checkpoint group 2
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`).
PEC-K-03 now describes operational reliance: an explicitly PEC-enabled
consumer may act on a record-tier claim as true as of its examined-through
SHA, within the pin, coverage and trust tier each response declares
(PEC-ORI-007), with file fallback. The verify-before-rely precondition of the
`D-PEC-67` K03-A row is superseded under `D-PEC-90` R-A; the K03-A bytes stay
as historical exact input, and PEC-K-11 is byte-identical. PEC-API-006 adds
response-size budgets, PEC-API-007 a read-only query surface for agent tool
calls under a new `agent` access class, and PRD §12 a standing
reliance-advertisement gate. PEC output stays never citable as authority.

Changed paths and authority:
`docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml`.

For this loop: use stays consumer-owned (PEC-K-03, PEC-K-11). The App decides
whether and when its harness consumes or exposes PEC data, and whether any
agent tool-call surface is enabled; injection is not required. Operational
reliance begins only at a PEC release that passes the PRD §12
reliance-advertisement gate. No PEC release has passed it, so nothing here is
usable now.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
```

Runtime:

```markdown
# Coordination Notice — PEC SCA-006: operational reliance on PEC data adopted in PEC's PRD and instructions

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Runtime (`projects/chirality-runtime`)
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`

PEC scope change SCA-006 carries the `D-PEC-90` R-A direction into PEC's
text. The owner adopted PEC PRD v2.4 by accepting SCA-006 checkpoint group 2
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`).
PEC-K-03 now describes operational reliance on PEC record-tier claims within
the pin, coverage and trust tier each response declares (PEC-ORI-007), with
file fallback. PEC-API-007 adds a read-only query surface for agent tool
calls under a new PEC-local `agent` access class, and PRD §12 a standing
reliance-advertisement gate. PEC output stays never citable as authority.

Changed paths and authority:
`docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml`.

For this loop: the DEL-02-06 Scope of Work names `projects/pec/AGENTS.md`,
`projects/pec/execution/_Decomposition/Deliverables.csv` and
`projects/pec/execution/_Decomposition/ScopeLedger.csv` as read-only sources,
and run record `DEL-02-06-RUNTIME-SPEC-001` pins them as S4–S6
(`clients/SOURCE_PINS.json`). SCA-006 changes all three: this tranche changes
`AGENTS.md`, and decomposition revision 1.6 adds SOW-097..100 and
DEL-08-06 and DEL-10-13 to the two registers. The `agent` access class is
token-scoped and local to PEC. Its credentials remain part of PEC's open
token-mechanism decision (PRD §16.6, OI-006). Operational reliance begins only at a PEC release that
passes the PRD §12 reliance-advertisement gate. No PEC release has passed it.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
```

## 7. Validation (scratch copies; no repository state changed)

Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7; PyYAML 6.0.3. `SCR` =
`/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/B5/agents`
(session scratchpad; not in the repository). Validators were run from the
repository's own `tools/validation/` at the basis.

| # | Command | cwd | State | Exit | Result |
|---|---|---|---|---|---|
| V1 | `git archive --format=tar -o SCR/head.tar HEAD`, then `tar -xf … -C SCR/repo` | worktree | full copy of `4d5f7b911`; `projects/pec/AGENTS.md` hash `c9d3b44d…` | 0 | extracted |
| V2 | `python3 REPO/tools/validation/validate_instruction_entrypoints.py SCR/repo` | `SCR` | preimage (before) | 0 | `PASS: root instruction entrypoints are canonical` |
| V3 | same | `SCR` | pre-revision `AGENTS.candidate_without_I1.md` in place (`432d8d68…`) | 0 | PASS |
| V4 | same | `SCR` | pre-revision `AGENTS.candidate.md` in place (`ea6c62ed…`) | 0 | PASS |
| V5 | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py` | `SCR/repo` | candidate with I1 | 0 | 24 passed |
| V6 | `python3 REPO/tools/validation/validate_instruction_tranche_manifest.py` (CI mode) | `SCR/repo` (after `git init`, no commits) | existing corpus | 0 | `G4 PASS (CI mode): 114 tranche manifest(s)` |
| V7 | same | `SCR/repo` | + draft manifest + three notices at their paths | 0 | `G4 PASS (CI mode): 115 tranche manifest(s)`; INFO: `projects/pec/AGENTS.md` and the three notice paths "do not intersect the instruction surface (over-declaration; non-blocking)", as for the `D-PEC-94` precedent; INFO self-merge under the standing owner Git grant |
| V8 | same | `SCR/repo` | Runtime notice removed (negative control) | 1 | `G4 BLOCK (CI mode)`: "routed notice '…/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md' does not exist"; notice restored afterwards |
| V9 | `git init`; `git add -A`; `git commit -m base` (scratch identity) | `SCR/g4repo` | light repo: the 114-manifest corpus, the 139 routed notices that exist in the worktree, preimage `projects/pec/AGENTS.md` | 0 | base commit tagged `base` |
| V10 | `python3 REPO/tools/validation/validate_instruction_tranche_manifest.py` | `SCR/g4repo` | base | 0 | `G4 PASS (CI mode): 114` |
| V11 | commit adding the draft manifest, the three notices and `AGENTS.candidate.md` as `projects/pec/AGENTS.md` | `SCR/g4repo` | `git diff --name-status base HEAD`: 4 A + 1 M | 0 | — |
| V12 | `… validate_instruction_tranche_manifest.py` (CI) | `SCR/g4repo` | HEAD | 0 | `G4 PASS (CI mode): 115` |
| V13 | `… validate_instruction_tranche_manifest.py --base base --head HEAD --added-manifests-only` | `SCR/g4repo` | HEAD | 0 | `G4 PASS (diff mode)`; "diff base..HEAD: 5 changed path(s), 1 on the instruction surface, checked against 1 manifest(s)" |
| V14 | `git diff --check base HEAD` | `SCR/g4repo` | HEAD | 0 | no whitespace errors |
| V15 | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | `SCR/repo` | preimage, no drafts; then candidate with I1 plus drafts | 1 and 1 | outputs byte-identical (`diff` exit 0): BLOCK=2, INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124. Both BLOCKs are App/Piping receipt `COMMIT_NOT_FOUND`, because the scratch copy has no Git history; no finding names `projects/pec/AGENTS.md` or a draft file |
| V16 | `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | worktree (read-only) | unchanged | 0 | `VALID … frozen through Receipt-166; versioned receipt contract satisfied`. In `SCR/repo` it reports `COMMIT_NOT_FOUND` for lack of history, so it was run where history exists; it does not read `AGENTS.md` |
| V17 | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` | worktree (read-only) | unchanged | 0 | 33 passed. In `SCR/repo` 2 receipts tests fail for lack of Git history (31 passed) |
| V18 | `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target AGENTS.md --operation exact-correction-preparation` (and the same for `execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md`) | `projects/pec` | — | 0, 0 | `{"operation": "exact-correction-preparation", "status": "ALLOW"}` |

V1–V18 are the original run on the pre-revision candidates
(`ea6c62ed…` with I1, `432d8d68…` without) and the pre-revision manifest draft
(`b7a58cff…`). Revision 1 (manager decisions O-2 and O-3, and the resulting
`scope_limits` wording in the manifest draft) was rechecked as follows:

| # | Command | cwd | State | Exit | Result |
|---|---|---|---|---|---|
| R1 | `python3 build_candidates.py` (6 SCA-006 + 9 I1 replacements, each asserted to match once) | `SCR` | preimage `c9d3b44d…` | 0 | without I1 `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` (448 lines); with I1 `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` (454 lines) |
| R2 | `python3 REPO/tools/validation/validate_instruction_entrypoints.py SCR/repo` | `SCR` | preimage; then without I1 (`a8b8d906…`); then with I1 (`49ce993a…`) | 0, 0, 0 | PASS each time |
| R3 | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py` | `SCR/repo` | with I1 | 0 | 24 passed |
| R4 | `python3 REPO/tools/validation/validate_instruction_tranche_manifest.py` (CI) | `SCR/repo` | revised manifest draft (`852b1d5b…`) + three notices | 0 | `G4 PASS (CI mode): 115 tranche manifest(s)` |
| R5 | third scratch commit replacing the manifest draft and `projects/pec/AGENTS.md` (revised candidate with I1); `git diff --name-status base HEAD` | `SCR/g4repo` | 4 A + 1 M | 0 | — |
| R6 | `… validate_instruction_tranche_manifest.py` (CI) | `SCR/g4repo` | HEAD | 0 | `G4 PASS (CI mode): 115` |
| R7 | `… validate_instruction_tranche_manifest.py --base base --head HEAD --added-manifests-only` | `SCR/g4repo` | HEAD | 0 | `G4 PASS (diff mode)`; "diff base..HEAD: 5 changed path(s), 1 on the instruction surface, checked against 1 manifest(s)" |
| R8 | `git diff --check base HEAD` | `SCR/g4repo` | HEAD | 0 | no whitespace errors |
| R9 | `python3 term_check.py`; `python3 selfcheck.py` | `SCR` | both revised candidates, all drafts | 0, 0 | no trailing whitespace or tab in any added line of either candidate or in any draft; no bare "reliance"/"rely" beyond the line-wrap artifacts of §5; every heading kept in order, eleven invariants present, one checks row differs |

Not rerun after revision 1: V8 (negative control; the notice set is
unchanged), V15 (harness), V16–V17 (they read neither `AGENTS.md` nor the
drafts) and V18 (the preflight checks target paths, which are unchanged).
The notice drafts are byte-identical to the original run.

Revision 2 changed only I1 text in `AGENTS.candidate.md` (the `WORKING_ITEMS`
and `CHANGE` rows), after `origin/main` `7f33b4dd5` was merged into the
branch as HEAD `005a45445`. The without-I1 candidate, the manifest draft and
the notices are unchanged, so G4 was not rerun. Rechecks:

| # | Command | cwd | State | Exit | Result |
|---|---|---|---|---|---|
| R10 | `python3 build_candidates.py` | `SCR` | preimage `c9d3b44d…` (unchanged at HEAD `005a45445`) | 0 | all 6 SCA-006 replacements still match the preimage exactly once; without I1 `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` (unchanged from revision 1); with I1 `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d`; `diff -U0` without→with gives exactly the four I1 hunks |
| R11 | `git archive --format=tar -o SCR/light.tar HEAD AGENTS.md CLAUDE.md init tools/validation projects/{pec,chirality-app-dev,chirality-piping}/{AGENTS.md,init,loop,software-workflow.json}`; `tar -xf` into `SCR/light` | worktree | read-only | 0 | light copy of `005a45445`, 2.7 MB |
| R12 | `python3 SCR/light/tools/validation/validate_instruction_entrypoints.py SCR/light` | `SCR` | preimage; without I1; with I1 (`49ce993a…`) | 0, 0, 0 | PASS each time |
| R13 | `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/validation/test_validate_instruction_entrypoints.py` | `SCR/light` | with I1 | 0 | 24 passed |
| R14 | `python3 term_check.py`; `python3 selfcheck.py` | `SCR` | both candidates | 0, 0 | no trailing whitespace or tab; no new bare "reliance"/"rely"; headings and invariants as in R9 |

The light copy was deleted after these runs.

Fit notes. `validate_instruction_entrypoints.py` checks only that
`projects/pec/AGENTS.md` contains `software_workflow_profile.md` (kept at
candidate L122 and L433) plus launcher and LOOP_INIT rules; it does not
inspect meaning, so its PASS shows structural conformance only. The G4
validator does not treat `projects/pec/AGENTS.md` as instruction surface (its
surface is Root `AGENTS.md`, `CLAUDE.md`, `agents/`, `.agents/skills/`,
`skills/`, `workflows/`, `tools/`, `docs/`, `init/`, `.github/workflows/`),
so in diff mode only the manifest itself is a covered surface path. The brief
asked for a light repo holding only the manifest corpus and the three
placeholders; CI mode would then BLOCK on every other manifest's missing
routed notices, so the light repo also holds the 139 notices the corpus
routes that exist in the worktree, and V6–V8 used a full copy.

## 8. Observations not carried

- **O-1 Session model convention.** The "Session model convention" section
  still prescribes `opus` and `fable` model assignments. The M1 return (§7
  item 5) notes that App rescinded its equivalent under `D-GOV-17` M1-D.
  I1 does not name it, so both candidates leave it byte-identical.
- **O-2 "§12" inside `AGENTS.md` — disposed (revision 1).** CANON §4 writes
  "§12" in the K-02 gloss and "PRD §12" in the checks row; inside this file
  "§" also marks internal headings ("§Active Reliance Holds"). Manager
  decision: the K-02 gloss reads "whose PRD §12 reliance-advertisement gate
  has passed", recorded as a manager-directed fitting of the canon text
  (§3.1, §3.5). Applied in both candidates.
- **O-3 Front matter — disposed (revision 1).** Manager decision: the
  `amended:` line is lineage (Seq 16) and reads `amended: 2026-09-25 (SCA-006
  operational-reliance instruction tranche; earlier, shared development-loop
  adoption under D-PEC-94)`. It is its own Seq 16 hunk (§3.3), applied in both
  candidates, and its date is an application-date slot (§9).
- **O-4 Lineage wording.** Product Posture keeps "exact PEC-K-03/-11 rows
  adopted by `D-PEC-67`" as history; after v2.4 the PEC-K-03 row is no longer
  the `D-PEC-67` bytes (CANON C-S15). The lineage lists what each act adopted,
  so it stays true as history.
- **O-5 I1 node owner — disposed (revision 1).** The work graph assigns I1 to
  HELPS_HUMANS and R3 to WORKING_ITEMS. Manager decision: I1 rides only if the
  owner says so at checkpoint 2 (the checkpoint-2 plan asks it as an owner
  question). If it rides, the checkpoint-3 instruction tranche applies it
  under that acceptance, and the integration owner named in the manifest
  applies it. If it does not ride, `AGENTS.candidate_without_I1.md` is the
  accepted text and I1 stays a planned graph node.
- **O-6 Notice filename.** The brief's `NOTICE_20260925_PEC_SCA006_…` form
  was replaced by the observed convention (§6.2).
- **O-7 Stale pointers outside I1.** Other `AGENTS.md` text not named by I1
  was not reviewed for staleness beyond the loci; nothing else was changed.
- **O-8 Basis moving.** The repository also holds commit `57db67a0e` (a
  descendant of the basis that publishes the `D-PEC-96` proposal); it was not
  checked out here. It does not change `projects/pec/AGENTS.md` (hash matched
  the brief), and `D-PEC-96` is a proposal, so it is not in the I1 slice list.
- **O-9 Root profile wording (revision 2).** At `7f33b4dd5`,
  `docs/SOFTWARE_WORKFLOW_PROFILE.md` L22 still reads "software-* workflows
  executed by TASK", although two of those methods are now skills and
  `software-bounded-implementation` is retired. The profile is Root's file;
  the candidate keeps only its conformance clause and names the methods from
  `workflows/index.json`. Not carried.

## 9. Acceptance-bound slots (CANON §5)

Hashes in this file are computed with every slot at its default value. If the
owner acts on another date, substitute the actual values at exactly these
loci and recompute; no other byte changes.

| File | Locus | Token (default) |
|---|---|---|
| `CP2_CANDIDATE/AGENTS.candidate.md` | L6, front-matter `amended:` (application-date slot: the date the tranche is applied at checkpoint 3) | `2026-09-25` (the first token of the line only) |
| `CP2_CANDIDATE/AGENTS.candidate.md` | L209, Governance Pointers | `SCA-006_GROUP-2_2026-09-25` |
| `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` | L6, front-matter `amended:` (application-date slot, as above) | `2026-09-25` (the first token of the line only) |
| `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` | L203, Governance Pointers | `SCA-006_GROUP-2_2026-09-25` |
| Manifest draft (§6.1) | `tranche_id`, filename, `instruction_surface_paths` item 2 | date part `20260925` |
| Manifest draft | `date`; `m2_gate.authorization_date` | `2026-09-25` |
| Manifest draft | `basis` | `4d5f7b91102b7106ff74b98118b2bda2fe873f36` (replace with the checkpoint-3 basis commit) |
| Manifest draft | `m2_gate.authorization` | `[SLOT CP2-ACT: …]` (verbatim checkpoint-2 act); `[SLOT CP2-VARIANT: …]` (accepted candidate); group-2 folder token `SCA-006_GROUP-2_2026-09-25` in the `DECISION.md` path |
| Manifest draft | `instruction_surface_paths` items 3–5; `m6_notice.routed_to` (3) | notice date `2026-09-25` |
| Three notice drafts (§6.3) | group-2 folder path (Root L9, App L10, Runtime L9) | `SCA-006_GROUP-2_2026-09-25` |
| Three notice drafts | manifest path (Root L22, App L22, Runtime L17) | date part `20260925` |

Not slots (fixed facts): "owner direction of 2026-09-25" (`D-PEC-94`,
candidate L242, without-I1 L236); the rest of the `amended:` line, which
names the `D-PEC-94` adoption without a date; the undertaking ID
`HELP-HUMAN-PEC-20260925-POST-SCA005`; the snapshot folder
`SCA-006_2026-09-25_1912`; the checkpoint-1 date and folder
`SCA-006_GROUP-1_2026-09-25`; `PEC-DEVELOPMENT-LOOP-ADOPTION-20260925`.
