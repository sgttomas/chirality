# Framework-Maintenance Pass — Handoff (apply FM-01..04 to Chirality canon)

> **This is the active `NEXT_INSTANCE_PROMPT` for the repo.** It supersedes the tier-0 bridge-prep coordination prompts (`NEXT_INSTANCE_PROMPT-piping.md`, `NEXT_INSTANCE_PROMPT-app-dev.md`), now archived under `{REPO_ROOT}/.archive/`. Point a fresh-session agent here: *"Read `{REPO_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT.md` and act on it."*

**For:** the next agent, in a **new session**. **Author:** DOMAIN_ENGINE (tier-0), 2026-06-21.

This brief hands off the **application** of the four gated canon diffs (`FM-01..04`) authored during the tier-0 OpenPipeStress bridge prep. The *direction* is owner-ruled; the *canon edits themselves* remain human-gated release-engineering changes. You draft the applied edits + a release note; the human approves; CHANGE publishes.

---

## 0. Posture & scope override (read first)

- **Act under the Type-0 standard `agents/AGENT_HELPS_HUMANS.md`** (instruction-governance / workflow-design authoring). The DOMAIN_ENGINE persona explicitly routes framework edits to a "HELPS_HUMANS / framework-maintenance pass" — **this is that pass.** `WORKING_ROOT = REPO_ROOT` (resolve via `git rev-parse --show-toplevel`).
- **You MAY edit release-managed canon:** `agents/AGENT_DOMAIN_ENGINE.md` and root `docs/CONTRACT.md` (and root `docs/TYPES.md` only if a diff explicitly requires it). This is framework maintenance, not project-runtime work.
- **You MUST NOT** edit `projects/**` (including app-dev's `docs/TYPES.md`/`docs/CONTRACT.md`) or anything under `_DomainEngines/**` except to mark the FM files APPLIED and add a release note.
- **Canon edits are release engineering** (`PROFESSIONAL_ENGINEERING.md` §6.2: material changes require review + a recorded release note; no silent behavior changes). **Human gate is mandatory** (K-AUTH-1): do not represent the applied canon as ratified; the human approves, CHANGE publishes, and approval binds to a SHA (K-AUTH-2).

## 1. Authorization (what the owner already ruled)

Recorded in `_DomainEngines/RULINGS_PUBLISHED.md` + `_DomainEngines/_DECISIONS/` (tier-0 records committed on `main`; latest tier-0 commit `6c2366fff`; the package/rulings commit is `6e70b5aac`):

- **`D-T0-01` = framework-root persona canonical, as NEW framework policy** → authorizes **FM-02** (promote K-DOMAIN to root) and **FM-04** (merge OperationProposal up).
- **`D-T0-02` = keep both `ProfileStatus` tokens (7-token enum)** → authorizes **FM-01**.
- **FM-03** is a **correctness fix** (the persona's OpenPipeStress example binding diverges from the real schema-driven layout), not tied to a numbered ruling — apply it as a factual correction, and flag it as correctness (not policy) for the human's approval.

## 2. The four edits

| Diff | Target canon | Change | Basis |
|---|---|---|---|
| `FM-01` | `agents/AGENT_DOMAIN_ENGINE.md` | `ProfileStatus` → 7-token enum `NONE\|DRAFT\|VALIDATED\|ADOPTED\|STALE\|INVALID\|UNKNOWN` at the Fn1 / SPEC / Integration-Record / Handoff-State sites | D-T0-02 |
| `FM-02` | root `docs/CONTRACT.md` | add **§1.12 K-DOMAIN-1..4** (new framework family) + index rows + update count "23 → 27 invariants / 11 → 12 subsections" | D-T0-01 |
| `FM-03` | `agents/AGENT_DOMAIN_ENGINE.md` | re-author the **OpenPipeStress Example Binding** to the verified schema-driven reality (no `project.ops.yaml`/`states/runs/comparisons` dir tree; `core/handoff/**` exists as export adapters) | correctness fix |
| `FM-04` | `agents/AGENT_DOMAIN_ENGINE.md` (SPEC "Valid Operation Proposal" + Minimal Profile Shape) | merge app-dev's richer `OperationProposal` fields + `draft\|ready_for_review\|accepted\|rejected\|applied` lifecycle up; add the generic `operation_risk_class` (engine-checkable vs engine-silent) + provenance-on-judgment-values | D-T0-01 flow (iii) |

The exact before/after text is in `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/framework_maintenance/FM-0{1..4}_*.md`.

## 3. Read order (cold — verify, don't trust)

1. The four diffs (above).
2. The rulings: `_DomainEngines/RULINGS_PUBLISHED.md`, `_DECISIONS/D-T0-01_precedence.md`, `_DECISIONS/D-T0-02_profilestatus_enum.md`.
3. The contract direction: `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/CONTRACT_DIRECTION.md` (esp. §4 **genericness verification** — app-dev's OperationProposal was verified piping-free; carry that forward for FM-04).
4. The current canon: `agents/AGENT_DOMAIN_ENGINE.md`, root `docs/CONTRACT.md`.
5. Governing: `agents/AGENT_HELPS_HUMANS.md`, `PROFESSIONAL_ENGINEERING.md` §6.2.

## 4. Critical pre-apply discipline — line drift

The diffs cite line anchors captured 2026-06-21 (e.g. persona `:197`, `:393-404`, `:657`, `:709-718`; CONTRACT index + count line). Commits have landed since (`d83e63b95`, `4930bd1de`, `9db0eef27`, `6c2366fff`) — they touched `projects/**` and `_DomainEngines/**`, **not** `agents/` or root `docs/`, so canon is likely undrifted, **but re-locate every anchor by CONTENT, not line number, before editing.** If any diff's "before" text no longer matches current canon, **STOP and reconcile** — do not force the edit.

## 5. Dependencies & notes

- `FM-01`, `FM-02` are independent and low-risk. `FM-04` carries the genericness verification (§4 above). Apply in any order; re-verify after each.
- Root `docs/CONTRACT.md` is itself **DRAFT pending ratification** — the `FM-02` K-DOMAIN addition rides that ratification; the K-* count update must stay consistent.
- **App-dev follow-on (NOT yours — flag it):** after `FM-02` lands, app-dev's working-root `K-DOMAIN-1..4` (`projects/chirality-app-dev/docs/CONTRACT.md:131-138`) should be annotated "specializes framework `docs/CONTRACT.md` §1.12; MUST NOT weaken." That is an **app-dev loop** edit — flag it, do not perform it.
- The owner's `_REFERENCES.md` SHA-pin of `AGENT_DOMAIN_ENGINE.md` into app-dev DEL-10-01/03 (`D-T0-01` sequencing) is likewise an app-dev-loop action — flag, don't perform.

## 6. Deliverables

1. **Applied edits** to `agents/AGENT_DOMAIN_ENGINE.md` and root `docs/CONTRACT.md` (after re-locating anchors).
2. A **release note** (what changed, why, ruling provenance `D-T0-01`/`D-T0-02` + FM IDs + the authorizing tier-0 SHAs) — per `PROFESSIONAL_ENGINEERING.md` §6.2.
3. **Post-apply verification:** `ProfileStatus` is the consistent 7-token enum at all sites; §1.12 K-DOMAIN present with index rows + corrected counts; example binding matches reality; OperationProposal merged with the generic risk-class field.
4. Mark `FM-01..04` **APPLIED** (with the applying SHA) in `_DomainEngines/bridge/.../framework_maintenance/` and update `_DomainEngines/RULINGS_PUBLISHED.md` "Next".
5. **Hand the file list + a PROPOSAL commit note to CHANGE** — you do not push; the human approves the applied canon first.
6. Flag the two app-dev follow-ons (§5) for the app-dev loop.

## 7. Closeout

Record what was applied, what was deferred (e.g. if an anchor drifted), and the next owner. The profile (`_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml`) stays **DRAFT / not ADOPTED** regardless — `VALIDATED` is gated on the profile-schema validator (TOOLMAKER brief: `_DomainEngines/bridge/.../TOOLMAKER_BRIEF-profile_schema_validator.md`), which is a separate handoff.
