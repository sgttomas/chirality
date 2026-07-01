# Tier-0 Bridge — ADOPTED (closeout & remaining work)

> The previous handoff here (build the profile-schema validator) is **fulfilled** — validator built + committed (`dd73d7fe8`), profile **VALIDATED → ADOPTED** (owner Gate 2, 2026-06-21). **There is no active tier-0 build task**; the bridge prep + adoption arc is complete. This doc orients the next session.

**Author:** DOMAIN_ENGINE (tier-0), 2026-06-21.

## Status — tier-0 adoption COMPLETE

- Contract reconciled into canon (`agents/AGENT_DOMAIN_ENGINE.md` + root `docs/CONTRACT.md` §1.12 K-DOMAIN) — `77a327727`.
- Profile-schema validator built (`tools/validation/validate_domain_engine_profile.py`, 8/8 tests) — `dd73d7fe8`.
- OpenPipeStress profile conformed → **VALIDATED → ADOPTED** (owner Gate 2, 2026-06-21). The integration boundary in `_DomainEngines/profiles/open_pipe_stress.yaml` is **governed-authoritative**.
- **Tier-0 adoption is 1 of the 4 live-build conditions — now cleared.** (Residency also cleared via RES-RECONCILE.)

## Remaining work (owned by other loops / human-gated — NOT a root build task)

- **app-dev loop** (launch from the app-dev project init, `WORKING_ITEMS`): annotate app-dev `K-DOMAIN-1..4` as specializing root `docs/CONTRACT.md` §1.12; SHA-pin `agents/AGENT_DOMAIN_ENGINE.md` @ `77a327727` into DEL-10-01/03 `_REFERENCES.md`; PKG-10 re-draft to ruled canon (D-T0-01); flow-A versioning (D-T0-07); ProfileStatus/OperationProposal conformance.
- **piping loop** (DEC-042 prep only; `D-21` held): validate-only trust-probe spike, headless CLI entrypoint, surface reconciliation.
- **Live-build conditions still gating L2/L3:** **app-dev F3 · piping D-21 · DEC-041.**

## Open refinements (minor, non-urgent — recorded, not authorized)

- **FM-05 candidate:** the FM-04 canon requires `apply_result_schema` on *every* declared tool incl. `read_only` ones (recorded `TBD`); consider requiring it only on `proposal_*`-mode tools.
- **Result-schema TBDs:** declare the `operation_applier` / `rule_check_runner` result shapes (piping DEL-10-03 conformance).
- **Profile filename:** retains the historical `.DRAFT` suffix; `profile_status: ADOPTED` in the field is authoritative. Rename deferred — it touches 10 references including the validator tool; churn outweighs the cosmetic benefit. [rename executed 2026-07-01 per D-GOV-06]

## To resume root (tier-0) work

A future root session resumes when a live-build condition opens, or to action the FM-05 refinement. Launch as **DOMAIN_ENGINE** at `WORKING_ROOT = {REPO_ROOT}`:
```
Resolve REPO_ROOT with git rev-parse --show-toplevel.
Set WORKING_ROOT to {REPO_ROOT}.
Read {REPO_ROOT}/agents/AGENT_DOMAIN_ENGINE.md.
Read {WORKING_ROOT}/AGENTS.md.
Act in the DOMAIN_ENGINE persona for {WORKING_ROOT}.
Then read {WORKING_ROOT}/execution/_Coordination/NEXT_INSTANCE_PROMPT.md and follow the instructions.
```
The app-dev / piping follow-ons launch from their **own** project inits (`WORKING_ITEMS`), not this one.
