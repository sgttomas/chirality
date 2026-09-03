# Orchestration Plan — Root Notice Ingestion and TM-ROOT-122 Disposition — 2026-09-03

- **Plan version:** 1
- **Selection authority:** HUMAN — R18 (`plans/steers/chirality_app_v3_root_ruling_record_r18_2026-09-03.md`) and its companion steer (`plans/steers/chirality_app_v3_r18_notice_ingestion_steer_root_2026-09-03.md`)
- **Basis:** `origin/main@8140daec7ab7165f8972451dbdd3a67b8bb2fd38` (the PR #680 merge commit)
- **Posture:** `TERMINAL_FAN_OUT_IN` (three write-disjoint nodes executed sequentially by one instance; no child agent)
- **Objective:** record the routed App Electron-authority disposition notice on the Root coordination surface with its final merge identity, apply the owner's R18-B ruling that `TM-ROOT-122` closes `RESOLVED_BY_DECISION`, and publish the R18 instrument pair — without adopting the notice as authority, touching `TM-ROOT-106`, or passing G1.

## Work graph

| Node | Executor | Depends on | Write ownership | Expected return | Fan-in gate |
|---|---|---|---|---|---|
| N1 notice ingestion | Root ordinary session (Claude Fable 5.1, `claude-fable-5-1`), single instance, no delegation | verified basis gate; Root G0–G4 | destination notice plus this node's instance records | header-plus-body copy with body byte-identical to source; claim-by-claim drift verdict; changed-path inventory | body identity equals source; every asserted identity matches live bytes; no out-of-scope write |
| N2 register act | Root `TASK_MANAGEMENT` (same instance) | N1 (the ingested notice SHA-256 is closure evidence); mandatory federation preflight | `REGISTER.csv`, `REGISTER_CLOSED.csv`, `RULING_2026-09-03_ROOT_TM-ROOT-122_DISPOSITION.md` | pre/post row and file identities; validate/archive/validate results; final federation counts | only `TM-ROOT-122` changed; `TM-ROOT-106` byte-identical; both registers valid; federation `COMPLETE` with zero writes |
| N3 R18 pair | Root ordinary session (same instance) | N1, N2 (cites their identities) | the two new `plans/steers/` files | R18 record in R16/R17 structure; companion steer in R11-steer shape | receipt pins both SHA-256 values |

N2 and N3 leave their evidence at their governed paths (the `RULING` file
and the `plans/steers/` pair); only N1 carries an instance folder here, per
the owner's direction. The Task Management federation projection under
`_TaskManagement/.candidates/` is gitignored and never authority.

## Human gates and stops

- Any exact mismatch between an App-notice claim and live bytes at the basis stops the tranche for owner routing; nothing is repaired.
- Any identity disagreement in the basis gate, any row other than `TM-ROOT-122` changing, or any write outside the steer's write set stops the tranche.
- The owner's R18-B disposition is the only disposition applied; no other row is proposed, ruled, or touched.
- G1, `TM-ROOT-106`, the ten held DEL-02-06 bindings, every pin/supply/implementation/lifecycle/release/publication/reliance act, and the PR merge remain owner acts outside this run.

## Validation owner

The same Root session validates its own returns (no child to fan in), reruns every check the steer names, appends the next free main-line receipt (Receipt 131), and performs Git closeout without merging.
