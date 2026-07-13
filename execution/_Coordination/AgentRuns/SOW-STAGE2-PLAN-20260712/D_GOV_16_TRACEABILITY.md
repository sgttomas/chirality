# D-GOV-16 Items 1–10 — Plan Traceability

Status: `COMPLETE — PLAN COVERAGE ONLY`
Basis: D-GOV-16 ruled items 1–10 exactly as proposed

| Item | Ruled obligation | Work-graph nodes | Acceptance gate / durable evidence |
|---:|---|---|---|
| 1 | Ratify and activate only the exact successor-standard bytes | `B0`, `C1`, `C1V`, `C1G` | G0 verifies ruled SHA; C1 exact-copies proposal over canonical standard; G1 requires SHA-256 `7f742901...85a6f`, proposal unchanged, dedicated canon commit, `P1_CANON` snapshot |
| 2 | Apply only the exact TYPES and SPEC patches in a controlled tranche | `B0`, `C1`, `C1V`, `C1G` | preflight `git apply --unidiff-zero --check`; patch SHA values verified; no consumer/project edits in tranche; EVALUATION diff/consistency PASS; P1 receipt binds before/after hashes |
| 3 | Deterministic checklist ownership; REVIEW exact consumption; judgment only at real review | `C2R`, `C2F`, every author/verifier pair, `P-F`, each `W-*`, `I0`, `X0` | G2 includes byte-identical checklist and one REVIEW compatibility calibration without re-extraction; every replacement emits deterministic checklist; verifier reproduces it; agentic semantic work occurs only for conflict or actual human-gated review |
| 4 | Single-format, lifecycle-neutral transition; new work SOW, legacy transitional | `C2R`, `C2A`, `C2F`, `B1`, `P-G`, all `W-*`, `I1`, `X0` | G2 proves INIT routes to SOW and compatibility states resolve/fail closed; every CHANGE commit adds SOW and deletes four docs atomically; control/status hashes unchanged; X0 requires 154 SOW and zero legacy/dual/invalid |
| 5 | Convert bounded remaining 144 after refreshed census and caller readiness | `B0`, `C2F`, `B1`, `W-A1`–`W-P4`, `I0`/`I1`, `X0` | G0/B1 require 154/10/144, digest `b6eca...`, one ISSUED, zero unclassified caller; seven ordinary waves cover 143 exactly; ISSUED node covers the 144th; per-wave manifests and RECON snapshots prove membership |
| 6 | Prepare ISSUED DEL-01-01 separately; require explicit administrative approval; no reissue | `W-P1`, `I0`, `H1`, `I1`, `X0` | W-P1 excludes named member; I0 binds source commit, four hashes, accepted basis, status and ISSUED state; H1 is separate human approval; I1 status must remain byte-identical/ISSUED; semantic difference is CONFLICT |
| 7 | Integrate ten pilots atomically; never merge dual-format branches as-is | `P-A`, `P-P`, `P-F`, `P-G` | current-base source/candidate hashes checked; only SOW blobs extracted from `fb83...` and `31c35...`; P-F reproduces 325/325 and 3,466/3,466; CHANGE makes ten serial replacement commits; no branch merge; P4 manifest and rollback binding |
| 8 | Enforce exact Stage-2 acceptance and wave-release gates | `C1V`, `C2F`, `B1`, `P-F`, every `W-*`, `I0`, `X0` | universal twelve-part per-deliverable gate; separate schema/content/preservation/substrate verdicts; independent verifier returns; RECON wave fan-in; applicable root/export/agent/skill/tool/project/runtime/practitioner checks; explicit single-format manifest |
| 9 | Fail closed; isolate failures; human-authorized non-rewriting rollback | all nodes, especially `P-F`, every `W-*`, `I0`, `X0` | failed members/dependants blocked while disjoint work may continue; FAILED/PARTIAL handoff persists; no failed candidate integrates; pre-integration deletion allowed; post-integration rollback requires human-authorized revert/replacement using preimage and manifest; receipts retained |
| 10 | Retain legacy through conversion/rollback; retirement only by later owner act | `C2R`, `C2F`, `X0`, `X1`, `R0`, `H2` | G2 requires four-documents/readers/checks retained; X1 stops at `LEGACY_RETIREMENT_RULING_REQUIRED`; R0 is proposal-only and exact; H2 is a later explicit human ruling; this plan contains no retirement implementation node |

## Cross-item acceptance closure

The graph has no path from H0 to conversion that bypasses exact canon,
consumer activation, caller fan-in, and the post-activation manifest freeze.
It has no path from ISSUED preparation to integration that bypasses H1. It has
no path from conversion closure to legacy deletion that bypasses a separately
prepared R0 proposal and later H2 ruling.

The plan therefore covers all ten ruled items without treating plan
presentation as implementation authority.
