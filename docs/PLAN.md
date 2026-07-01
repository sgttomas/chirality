# PLAN — Active Roadmap

> **Status: ACTIVE — maintainer-adopted 2026-07-01** (supersedes the
> 2026-06-15 DRAFT skeleton). §2–§4 record ruled direction and measured
> findings only, prepared at the owner's explicit request following the
> D-GOV-01..07 rulings of 2026-07-01 (ruled and SHA-bound at commit
> `82a35c545`; see `docs/governance_harness/_DECISIONS/_REGISTER.md`); per
> K-INVENT-1 nothing is invented. §1 and the Control-Plane Boundary are
> unchanged from the 2026-06-15 restoration.

## Control-Plane Boundary

This document is the active **framework roadmap**. It is strategic and
non-governing: `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, and `TYPES.md` govern;
this file records direction and intended work, not binding requirements.
Tactical sequencing, blocker policy, and completed-work detail live in
issue/branch/release records — not here. Working roots (`projects/*`,
`domains/*`) maintain their own `docs/PLAN.md` for project-level roadmaps; this
file does not supersede them. `docs/governance_harness/PLAN_INDEX.md`
classifies planning artifacts and their standing; it is an index, not a
competing roadmap surface.

---

## 1. Current Architectural Direction

The established direction (reflected in `AGENTS.md` and the agent suite):

- **`TASK` is the canonical Type 2 execution shell.** It hydrates reusable
  methods via `TaskSkill: <name>`. A new bespoke task agent is not added when
  role, write scope, and interaction surface are unchanged and only the method
  differs — that is a skill.
- **Method logic lives in `skills/`; deterministic operations live in
  `tools/`; Type 1 personas handle human-facing orchestration.** `ORCHESTRATOR`
  is the grandfathered orchestration persona.
- **Governance is two-layered.** The framework root (`AGENTS.md`, root `docs/`,
  `agents/`, `skills/`, `tools/`) defines Chirality-wide rules; working roots
  specialize them without weakening framework invariants (`CONTRACT.md`
  K-AGENTS-1).
- **One shared instruction root serves many working roots** under `projects/*`
  and `domains/*`; path anchoring and task write-scope containment make
  per-working-root and git-worktree isolation safe (`SPEC.md` §0.2;
  `CONTRACT.md` K-WRITE-2).

Details of in-flight work live in issue/branch/release records, not in this
planning surface.

---

## 2. Active Roadmap Themes

| Theme | Status |
|---|---|
| Governance harness (practitioner bench tool) | RULED — D-GOV-01..07 ruled 2026-07-01 (SHA-bound at publication commit 82a35c545); plan of record: `governance_harness_plan_v3_2026-07-01`; next slice is the first PR |
| Root governance ratification | ACTIVE — sequenced per D-GOV-05 (minimal harness basis first; full DIRECTIVE/SPEC/TYPES/CONTRACT ratification on its own track) |
| Tier-0 domain-engine integration (OpenPipeStress) | ACTIVE — profile ADOPTED (affirmed by D-GOV-06); surface-cleanup slice directed; live-build conditions per `_DomainEngines/` records |

Unsplit backlog: History trailer grammar (rides D-GOV-05); domain-shape
verifier + D-GOV-07 re-binding (deferred per D-GOV-03); obligations /
applicability register (deferred).

---

## 3. Roadmap Detail

### Architecture and Governance

- **Root governance restoration + path anchoring.** Ratify the root `docs/`
  governance set (DIRECTIVE/SPEC/TYPES/CONTRACT/PLAN); wire the `K-WRITE-2`
  ScopePath-containment rule (`SCOPE_OUTSIDE_WORKTREE`) into `AGENT_TASK.md`;
  derive `REPO_ROOT` in `init/init-prompt.md` and de-absolutize
  coordination/handoff files. Basis:
  `plans/monorepo_root_governance_and_path_anchoring_2026-06-15.md`.
  **Amended 2026-07-01 per D-GOV-05:** ratification is sequenced — the minimal
  harness basis (source-of-truth, human authority, generated-output rule, path
  containment, approval-SHA binding, provenance, status canonicity, verifier
  severities) ratifies first; the full root set proceeds on its own track; the
  append-only History trailer grammar (SPEC §3.1) rides that ruling.

- **Governance harness build.** Read/report bench tool over
  `projects/chirality-app-dev`, `projects/chirality-piping`, and
  `_DomainEngines/` (D-GOV-03 scope): adapters + manifests, `status`,
  `drift`/`self-check` against the 92/154 status-history baseline (verified
  2026-07-01, all in piping), source-cited candidate briefs with human
  adoption (D-GOV-04), tool-run validations under the mutation contract, and
  the `write_status.sh` precondition guard (canonical copy + export source;
  the staging copy is a gitignored regenerated artifact). Basis:
  `governance_harness_plan_v3_2026-07-01` + `PLAN_INDEX.md`; authority:
  D-GOV-01..07 (ruled 2026-07-01, SHA 82a35c545). Planning is closed
  (terminal-artifact rule); the next artifact is the first pull request.

- **D-GOV-06 cleanup slice.** CHANGE-published correction of the six
  contradicting `open_pipe_stress` current-truth surfaces
  (`RULINGS_PUBLISHED.md` stale closing paragraph; both halves of the
  `DOMAIN_ENGINE_INDEX.md` banner — "No profile is ADOPTED" and "No decision
  is ruled"; the profile YAML header comments plus the open_issues "Profile
  stays DRAFT" entry; the `.DRAFT` filename; D-T0-06's stale HumanRuling
  line; the `_DomainEngines/_LATEST.md` "PROPOSAL, not yet owner-accepted"
  framing); the diff becomes the harness's first live self-check fixture.

### Workflow Normalization

- **Drift reduction as a standing objective.** Framework-wide target: the
  status/history mismatch count trends down from the 92/154 baseline as
  measured by the harness `drift` command; restated-state surfaces (pointers,
  banners, index tables, header comments, filenames) are audited on the same
  cadence.

---

## 4. Known Risks

- **State drift.** 92/154 deliverable status files disagree with their own
  histories (verified 2026-07-01; all 92 in chirality-piping, app-dev 0/53
  clean); control-area surfaces have contradicted each other about single
  facts. Mitigation: harness drift metric with run-over-run trend; D-GOV-06
  cleanup; consistency checks over every restated-state surface.
- **Plan resurrection.** Settled architectural forks re-derived by fresh
  sessions (the SQLite control plane was independently re-proposed twice).
  Mitigation: ruled decision records with supersession clauses (D-GOV-01);
  `PLAN_INDEX.md` standing markers; terminal-artifact rule.
- **Planning outproducing execution.** The 2026-06 archive shows heavy
  meta-work against 92/101 piping deliverables IN_PROGRESS and 53/53 app-dev
  deliverables in CHECKING. Mitigation: PR-first sequencing; success defined
  as tranches closing and drift falling, not documents produced.

---

## 5. Historical Record

Completed roadmap slices are historical and are not tracked as active surface
here; they live in git history, release records, and per-project completion
logs.
