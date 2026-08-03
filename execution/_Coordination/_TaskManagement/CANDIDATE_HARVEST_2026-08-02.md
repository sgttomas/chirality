# Root Task Management — Candidate Harvest Report (2026-08-02)

Status: **DECISION SUPPORT ONLY — NOT AUTHORITY — NO REGISTER ROWS WRITTEN**

Invoking loop: Root
Register home: `execution/_Coordination/_TaskManagement/`
Mode: Candidate harvest
Current basis: `main@cad3553bf530c2c8b00e2b058bbc9d0bba690266`
Delta boundary: the completed Stage-A scanner/closeout basis at
`main@9e6acfd7ded87b7b644057e6180a643c83e01656` (2026-07-31), with the
2026-07-31 seed and first owner triage treated as the prior root harvest.

This report presents observations and proposed dispositions only. Promotion,
priority, assignment, deferral, elevation, disposition, and closure remain
owner acts. `SourceSha` values below are SHA-256 digests of the current cited
source bytes, not hashes of this derivative report.

## 1. Mandatory federation preflight

Command:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register execution/_Coordination/_TaskManagement/REGISTER.csv
```

Verdict: **COMPLETE**.

- 4 canonical Git-tracked registers discovered, read, and validated: Root
  (103 rows), App (24), Piping (24), and PEC (6).
- 0 excluded lookalikes; 0 invalid, unreadable, or ambiguous inputs.
- 48 typed-field findings presented program-wide: 47
  `FOREIGN_LINK_TO_LOCAL` relationships and 1
  `REMOTE_CLOSED_LOCAL_OPEN` relationship.
- Zero-write proof: every readable register SHA-256 was unchanged;
  `register_writes: 0`.
- The sole divergent-closure relationship is `TM-PIP-023 CLOSED` →
  `TM-ROOT-053 OPEN`. It is an existing-row closure echo, not a promotion
  candidate; see §5.

The projection at
`execution/_Coordination/_TaskManagement/.candidates/federation.json` is
gitignored, rebuildable, and never authority.

## 2. Full §5.1 sweep coverage

The deterministic v0 scan completed first, then its expressly omitted source
classes were inspected manually.

| §5.1 source class | Sweep result | Root-harvest result |
|---|---|---|
| Decision registers — non-ruled rows | 0 current non-ruled rows found by the structured scan | No new candidate |
| Notice files vs. ledgers | 58 raw `TRACKED_OPEN` ledger observations and 29 raw notice-not-in-ledger observations; all 17 notices dated 2026-08-02 were manually inspected to defeat basename-family deduplication | Two inbound Root notices contain six explicit `TM-CANDIDATE:` markers; outbound notice families are screened in §4 |
| Evaluation `FINDINGS.csv` | 146 raw open-status observations; the only newly landed file is the Piping DAG-009 evaluation (8 validated/reconciled/ready rows and 1 Piping-local `OPEN_OWNER_GATES` row) | No new Root row; the open gate belongs to the Piping loop |
| `Review_Findings.csv` | All changed files inspected; one new open row, PEC DEL-01-06 `RF-001` (`DEFERRED`) | No Root row; PEC-local review residue for a future PEC invocation |
| HOLD registers | No newly changed open HOLD row; the App maturity survey confirms `APP_HOLD_REGISTER.csv` is header-only | No new candidate |
| Handoff blockers / coverage gaps | 34 raw blocker-language observations; all changed handoffs inspected | No unresolved Root blocker; surviving gates are owned by their App, Piping, PEC, bridge, or CHANGE instruments |
| Packet open-question/conflict/amendment fields | 64 raw observations | No new delta; prior packet residue is already registered or migrated |
| `*TBD_Register.csv` | 21 raw rows | No new delta; all were in the prior seed/migration set |
| New review reports | Three reports landed after the prior harvest: Piping maturity, App maturity, and five-investigation synthesis | Cross-cutting Root candidates are in §3; loop-local or already-registered observations are screened in §4 |
| Receipt parked lanes | Root Receipts 74–85 inspected | Receipt 77 expressly routes the recurring G4 manifest-discipline choice to the next harvest; included in §3 |
| Run-record markers | Exact-line scan for `TM-CANDIDATE:`, `NEEDS_HUMAN_RULING:`, and `MISSING:`; false `none` records and decomposition vocabulary tokens excluded | The six live new Root markers are exactly the five D-APP-84 markers and one D-APP-85 marker in §3/§4 |
| Slates / `## Remaining` / work graphs | Fenced as work-discovery surfaces per PRD §5.5 | Not harvested; no ordinary planned work was converted into a candidate |

Deterministic scan summary: 278 deduplicated observations, 74 canonical-copy
duplicates folded; 75 had coarse `SourceRef` overlap with the root register.
That projection is at
`execution/_Coordination/_TaskManagement/.candidates/scan_2026-08-02.json`
and is likewise gitignored and non-authoritative.

## 3. Promotion slate — Root rows recommended

### CH-20260802-01 — Product-delivery direction needs a Root product-basis disposition

- **SourceRef:**
  `execution/_Coordination/OWNER_INTENT_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`
  §§1–3 and “What this record does not do”
- **SourceSha:**
  `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03`
- **Concern:** The owner has made domain-specific applications the primary
  delivery vehicle and Piping the first target, but the coordination record
  deliberately performs no Root PRD, decomposition, activation, priority, or
  sequencing act, so Root must decide whether and how that direction changes
  its own product basis.
- **Domain lenses:** Prioritization; Deliverables; Planning; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — cite the eventual Root
  product-basis decision, including an explicit no-change decision if that is
  the ruling.
- **Route posture:** App and Piping already received the exact outbound
  coordination notices. No duplicate draft is warranted unless the Root
  decision adds or changes a requested local act.

### CH-20260802-02 — Generic per-run sandbox and native-tool primitive contract

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
  “Root-owned decisions and activation requested” items 1–2 and first
  `TM-CANDIDATE:` marker
- **SourceSha:**
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`
- **Concern:** The ruled App target depends on Root deciding generic
  role/run-specific sandbox identity and Chirality-owned native-tool
  authorization, audit, interruption, evidence, result-budget, and
  fail-closed semantics before any affected-client implementation can rely on
  them.
- **Domain lenses:** Deliverables; Work; Planning; Approval; Checking;
  Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — closure requires the
  exact Root contract/decision record; implementation evidence alone cannot
  substitute for the decision.
- **Likely owning instrument:** Root product decision followed, if selected,
  by the accepted DEL-02-06 activation lane.
- **Draft route after ruling:** consolidated Root response to the App loop;
  see §6.

### CH-20260802-03 — Root/App Pi version concordance

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
  item 3 and third `TM-CANDIDATE:` marker
- **SourceSha:**
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`
- **Concern:** Current executable/dependency surfaces and the Root engine
  descriptor use Pi `0.82.0` while the governed D-APP-72 basis remains
  `0.80.10`, so the accepted version and supply-chain concordance require an
  explicit ruling rather than treating present bytes as approval.
- **Domain lenses:** Deliverables; Approval; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — cite the exact accepted
  version/concordance record and its validation evidence.
- **Draft route after ruling:** consolidated Root response to the App loop;
  see §6.

### CH-20260802-04 — Root scope-change and runtime-package impact for the D-APP-84 target

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
  item 6, “Root should also determine…”, and fifth `TM-CANDIDATE:` marker
- **SourceSha:**
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`
- **Concern:** The selected App target may affect accepted Root decomposition,
  DEL-02-04, DEL-03-01, DEL-02-06, shared shell/tool contracts, runtime
  packages, validators, instruction mirrors, and affected clients, but no
  Root SCOPE_CHANGE assessment has accepted that impact.
- **Domain lenses:** Action Item; Deliverables; Work; Planning; Approval;
  Checking; Decisions.
- **Proposed disposition:** `SUPERSEDED_BY_SCOPE_CHANGE` — only after a ruled
  SCA is cited through `ScaRef`; until then the item would remain open or
  validly deferred.
- **Likely owning instrument:** SCOPE_CHANGE intake; TASK_MANAGEMENT must not
  draft decomposition amendments directly.
- **Draft route after ruling:** consolidated Root response to the App loop;
  see §6.

### CH-20260802-05 — Accepted-turn recovery across daemon restart

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-85_C06_DAEMON_RECOVERY_ROOT_ROUTE_2026-08-02.md`
  “Verified App finding” and its `TM-CANDIDATE:` marker
- **SourceSha:**
  `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41`
- **Concern:** The generic runtime persists `turn.accepted` before terminal
  evidence but does not reconcile accepted unterminated turns on daemon
  restart before admission or model activation, so drain accounting and the
  exactly-one-terminal-outcome claim can be lost across recovery.
- **Domain lenses:** Deliverables; Work; Planning; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_WITH_CHANGE` — cite the Root runtime
  repair plus restart/replay evidence proving idempotent reconciliation before
  admission and activation.
- **Likely owning instrument:** DEL-02-06 amendment/activation lane, not direct
  TASK_MANAGEMENT execution.
- **Draft route after ruling:** Root response to the App loop; see §6.

### CH-20260802-06 — Ruled comparison-basis requirement for “matches / conforms / compatible” claims

- **SourceRefs / SourceShas:**
  - `plans/chirality_five_investigations_2026-08-01.html`, “Cross-cutting
    synthesis” and “Candidate instruments discussed with the owner” —
    `9eda9bf68831714368d9d880a3a5dc66e80809e30a65b424d489c5740a8730b4`
  - `plans/chirality_app_dev_maturity_survey_2026-08-01.html` §§4–6 —
    `2826a26c12fa793857a6e42baae7f7a5513dea66b89ced43b3ae034ddf3d02e9`
  - `plans/chirality_piping_solver_maturity_survey_2026-07-31.html` §§4–6 —
    `afeb9e0ab445f5e81b122c6737ba5c16c0e8f538716f5b05ab5776b8bf4d7c28`
- **Concern:** Runtime compatibility identity, Piping tolerances, App parity,
  and ruling identity are four instances of the same missing comparison-basis
  object, leaving consequential “matches / conforms / compatible” claims
  without one ruled, versioned definition of equivalence.
- **Domain lenses:** Deliverables; Approval; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — cite a ruled generic
  comparison-basis contract or an explicit decision to keep the definitions
  local.
- **Draft route after ruling:** if a generic rule is selected, prepare
  separate App and Piping notices carrying the Root row and decision evidence;
  see §6.

### CH-20260802-07 — Recurrent G4 manifest-gap handling

- **SourceRef:** `execution/_Coordination/LOOP_RECEIPTS.md`, Receipt 77,
  “Standing observation (not a ruling request)”
- **SourceSha:**
  `abd0f89081cc7bb426a7a8d6c687128cc6d94a42d46ffc72cb1a2b42d059510d`
- **Concern:** Five disclosed instruction-surface tranches have lacked G4
  manifests because CI exercises schema-only validation while the existing
  diff-mode check is unwired, leaving the owner to choose between wiring it,
  amending the discipline, or continuing disclose-as-found.
- **Domain lenses:** Work; Planning; Approval; Checking; Decisions.
- **Proposed disposition:** `RESOLVED_BY_DECISION` — cite the ruling that
  chooses the standing handling and any resulting change evidence.
- **Route posture:** Root-only unless the selected rule changes a shared
  instruction or loop contract, in which case ordinary affected-loop notices
  follow the governing change-notice rule.

## 4. Screened candidates — no new Root row recommended

### CH-20260802-08 — Four-pillar coherence heuristic

- **SourceRef:** `plans/chirality_five_investigations_2026-08-01.html`,
  “Candidate instruments discussed with the owner”
- **SourceSha:**
  `9eda9bf68831714368d9d880a3a5dc66e80809e30a65b424d489c5740a8730b4`
- **Concern:** The report records an unruled ontology / epistemology /
  praxeology / axiology coherence heuristic, but no current HOLD, missing
  approval, or session-unresolvable concern depends on adopting it.
- **Domain lenses:** Checking; Decisions.
- **Proposed disposition:** `INFORMATIONAL_NO_ACTION`.
- **Screening rationale:** Fails the PRD §7.1 promotion gate today; retain as
  evidence until a concrete decision surface needs it.

### CH-20260802-09 — Governance-economics telemetry gap

- **SourceRef:** `plans/chirality_five_investigations_2026-08-01.html`, T4
  “Governance economics: the first quantitative pass”
- **SourceSha:**
  `9eda9bf68831714368d9d880a3a5dc66e80809e30a65b424d489c5740a8730b4`
- **Concern:** Governance benefit/cost remains undecidable because no durable
  record carries comparable time/token telemetry, defect blast radius,
  retained CI evidence, or a control period.
- **Domain lenses:** Planning; Checking; Decisions.
- **Proposed disposition:** `INFORMATIONAL_NO_ACTION`.
- **Screening rationale:** This is a measurement limitation, not a present
  HOLD or owner-requested evaluation program; promote only if the owner
  initiates that evaluation.

### CH-20260802-10 — D-APP-84 Root doctrine-successor marker

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
  item 6 and second `TM-CANDIDATE:` marker
- **SourceSha:**
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`
- **Concern:** The marker asks Root to replace a project-root/serialized-owner
  rule that the owner subsequently removed from shared Root doctrine while
  expressly preserving the App-owned managed-child policy.
- **Domain lenses:** Work; Decisions.
- **Proposed disposition:** `OBE`.
- **EvidenceRef:**
  `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_HARNESS_SCOPE_CORRECTION.md`
  (`f6923e7335f76fc413dd56d5735f0299c31bbf83187bce1b660bfb23ae007a11`)
  and Root Receipt 80/81 scope-correction record.
- **Screening rationale:** No new Root row is needed for the superseded
  premise; the still-live App sandbox question is CH-20260802-02.

### CH-20260802-11 — D-APP-84 DEL-02-06 activation marker

- **SourceRef:**
  `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md`
  item 5 and fourth `TM-CANDIDATE:` marker
- **SourceSha:**
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`
- **Concern:** Compatibility identity, affected-client conformance, and the
  DEL-02-06 activation trigger are already represented by
  `TM-ROOT-035`, `TM-ROOT-043`, and `TM-ROOT-046`, so a fourth Root row would
  duplicate the same activation residue.
- **Domain lenses:** Planning; Deliverables; Checking; Decisions.
- **Proposed disposition:** `DUPLICATE` — surviving rows
  `TM-ROOT-035` / `TM-ROOT-043` / `TM-ROOT-046`.
- **Screening rationale:** Review the existing rows if the new product
  direction changes their triggers; do not mint a duplicate.

### CH-20260802-12 — AUDIT_GOVERNANCE stale-DBM repair notice family

- **SourceRefs / SourceShas:**
  - `domains/chirality/_Coordination/NOTICE_2026-08-02_AUDIT_GOVERNANCE_STALE_DBM_REFERENCE_REPAIR.md`
    — `4cc98bbbecd9e195cf28337d4018589276a8eb498a910d47408384ca767a1c4c`
  - `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_AUDIT_GOVERNANCE_STALE_DBM_REFERENCE_REPAIR.md`
    — `28222953e38ebafbdb6aef85229a4823e7bba3e034c4c5bd5f0afc852cb7dfa0`
- **Concern:** The shared audit instruction repair is complete and the Root
  notice duty is discharged; only optional/current-corpus reconciliation
  remains within the receiving domain/App loops' own instruments.
- **Domain lenses:** Checking; Decisions.
- **Proposed disposition:** `INFORMATIONAL_NO_ACTION` in the Root register.
- **Screening rationale:** Existing notices already route the follow-on; a
  Root row must not create a foreign-loop duty (K-TM-3/K-TM-4).

### CH-20260802-13 — Root governance-document simplification notice family

- **SourceRefs / SourceShas:**
  - `domains/chirality/_Coordination/NOTICE_2026-08-02_ROOT_GOVERNANCE_DOC_SIMPLIFICATION.md`
    — `940806f7960100b87236affb0cfe5f7051b8e48ecf251a1925d31e5544464f89`
  - `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_GOVERNANCE_DOC_SIMPLIFICATION.md`
    — `d1500dd428f42431dd19b638f3f0bbc0e75834ce7d721b6d9ba9ca8cb6424525`
- **Concern:** Root relocation/removal and the App packaging pin repair are
  complete; the domain source-catalog repin/retirement choice remains owned by
  that domain's corpus-currency process.
- **Domain lenses:** Deliverables; Checking; Decisions.
- **Proposed disposition:** `INFORMATIONAL_NO_ACTION` in the Root register.
- **Screening rationale:** The routed notices are already the correct
  cross-loop mechanism; no second notice or Root row is needed.

### CH-20260802-14 — Shared instruction repair/federation notice families

- **SourceRefs / SourceShas (representative App copies; equivalent Piping/PEC
  notices were also inspected):**
  - `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_INSTRUCTION_SCHEMA_REPAIR.md`
    — `6f6bd502dc11bb9f365afa585b837f6fadc0eb34fde78725157cedcf5cac2422`
  - `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_FEDERATION_PREFLIGHT.md`
    — `b82bb366f15007369bb5fa0ffaf31c05e3c8822b42b2f7576eb93bee2c94ef99`
- **Concern:** Both shared instruction changes are now effective, validated,
  and routed; the federation notices' pre-publication wording is historical
  provenance, not a live receiving-loop obligation.
- **Domain lenses:** Checking; Decisions.
- **Proposed disposition:** `INFORMATIONAL_NO_ACTION`.
- **Screening rationale:** D-GOV-33 and PR #478/Receipt 85 already carry the
  effective decision/change evidence; no new row or replacement notice is
  warranted.

## 5. Existing-row maintenance observations — not promotion candidates

No edit is authorized by this report.

| Existing row(s) | Observation | Proposed disposition if separately ruled | Evidence |
|---|---|---|---|
| `TM-ROOT-098` | App Task Management adoption is effective, but the Root adoption-echo row remains OPEN | `RESOLVED_BY_DECISION` | `execution/_Coordination/NOTICE_D-APP-83_APP_TASK_MANAGEMENT_ADOPTION_2026-08-01.md`, SHA-256 `09ed242875b083b1a6f5626d00d2a72a95cac1c6c3464d5b175d0b1900f4c838`; D-APP-83; App register SHA-256 `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |
| `TM-ROOT-053` ↔ `TM-PIP-023` | Federation reports remote CLOSED / local OPEN | `RESOLVED_BY_DECISION` if the Root owner accepts the Piping decision as closure evidence | Root register SHA-256 `79bb9b166b63e1faa6364e33bf141512eed0fad2b3bb700fe26c90bdccfe98b5`; Piping register SHA-256 `bdfef05ec04d8a64fd8c86bdddc679a48e5317c4557613dd5c8762c9de5b68ce` |
| `TM-ROOT-103` ↔ `TM-APP-024` | Both rows still say the Pi/oMLX packet is pending/deferred, while D-APP-84 has now been ruled and its Root-owned residuals arrived through the inbound notice | `RESOLVED_BY_DECISION` for the migrated packet-opening concern, leaving CH-20260802-02/03/04 as distinct Root residuals if promoted | D-APP-84 inbound notice SHA-256 `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`; App register SHA-256 `e6a3de4c96e4471c1bf4157e1e65f8e9b607534c3a61e395abf87a61ae9bfd64` |

## 6. Routed-response draft preparation and gate

No routed draft file is written in this tranche because no candidate has yet
been promoted or ruled and therefore no receiving notice can truthfully carry
the required Root `ActionItemID`. Inventing or reserving an ID outside the
register would violate K-TM-3 and the user's reciprocal-citation requirement.

The closeout tranche is preplanned as follows; drafts remain gated on the
owner's promotion/ruling and will be written only inside the Root closeout
tranche, never directly into another loop's surface:

| Triggering candidate/ruling | Draft addressee and intended destination | Required reciprocal citations |
|---|---|---|
| CH-20260802-02/03/04 | Chirality App Dev loop; draft target named for `projects/chirality-app-dev/execution/_Coordination/` | inbound D-APP-84 notice SHA-256 `2d6123…e6a`; promoted `TM-ROOT-*` row ID(s); Root decision/SCA/DEL-02-06 evidence refs and SHAs |
| CH-20260802-05 | Chirality App Dev loop; draft target named for `projects/chirality-app-dev/execution/_Coordination/` | inbound D-APP-85 notice SHA-256 `0b34ce…c41`; promoted `TM-ROOT-*` row ID; accepted repair/check evidence refs and SHAs |
| CH-20260802-06, if a generic rule is selected | Separate Chirality App Dev and Chirality Piping notices | source report SHA-256 values above; promoted `TM-ROOT-*` row ID; Root decision/contract evidence refs and SHAs |
| CH-20260802-01, only if the product-basis ruling changes the already-routed request | App and/or Piping, as affected | owner-intent SHA-256 `9bbb67…e03`; promoted `TM-ROOT-*` row ID; product-basis decision evidence refs and SHAs |

The existing product-direction, AUDIT_GOVERNANCE repair,
governance-simplification, scope-correction, instruction-schema, and
federation-preflight notices are already routed artifacts. This report does
not duplicate, amend, or treat them as authority.

## 7. Owner ruling requested

Please rule only on the explicit slate:

1. Promote or decline CH-20260802-01 through CH-20260802-07.
2. Accept or amend the no-new-row recommendations for CH-20260802-08 through
   CH-20260802-14.
3. Separately authorize any maintenance disposition for `TM-ROOT-098`,
   `TM-ROOT-053`, and/or `TM-ROOT-103`; none is implied by a promotion ruling.
4. If a promotion/ruling requires another loop's action, authorize the exact
   closeout draft(s) after the new Root row IDs exist. Shipping remains under
   the user's closeout gate.
