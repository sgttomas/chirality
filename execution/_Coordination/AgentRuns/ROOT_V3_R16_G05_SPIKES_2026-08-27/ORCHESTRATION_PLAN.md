# Orchestration Plan — Root R16 G0.5 Disposition and Feasibility — 2026-08-27

- **Version:** 1 (frozen before N0 execution)
- **Selection authority:** HUMAN — R16-A through R16-F and the companion steer
- **Basis:** `origin/main@b0d975a9139eddebf5c1e728cf724b55c8a97cad`
- **Posture:** ordered N0/N1/N2 followed by independent bounded N3 limbs and N4 fan-in
- **Supervisor:** HELP_HUMAN (Agent 0)
- **Standing workplan:** remains idle; no workplan target was selected

## Work graph

| Node | Objective | Dependencies | Write ownership | Expected return | Fan-in gate |
| --- | --- | --- | --- | --- | --- |
| N0 | Transcribe R16-A/B into immutable Root successor state and Receipt 131 | Exact main and all pinned-input gates PASS | DEL-02-06 successor packet; this run folder; Receipt 131 append | Ten-row routing, Tier-0 record, preservation proof, pushed immutable commit | Only Tier-0 substantively disposed; nine other holds preserved; owner act verbatim |
| N1 | Freshly acquire only the minimum accepted 0.149.0 artifact set if later nodes require it | Pushed N0 commit | Untracked quarantine and disposable state; evidence records only | Official metadata, asset and payload identity, teardown proof | Exact accepted identity or fail closed |
| N2 | Attempt OUT-002 exact endpoint-policy completion | Pushed N0; accepted empirical evidence; N1 only if binary required | DEL-02-08 new R16 evidence subtree | Row-by-row policy with exact evidence and calibrated unavailable rows | No inferred account/model/turn endpoint; no network authority |
| N3.1 | G-SBX feasibility | Pushed N0; N1 if binary required | DEL-02-07 primary evidence; citations elsewhere | One calibrated verdict and implementation implication | No packaged/signed-bundle overclaim |
| N3.2 | G-PROT feasibility | Pushed N0 | DEL-02-07 primary evidence; citations elsewhere | Deterministic protected-path round-trip result | Inexpressible rule is blocking evidence |
| N3.3 | G-ENV feasibility | Pushed N0; N1 if binary required | DEL-02-07 or DEL-02-09 primary evidence; citations elsewhere | Disposable environment-boundary result | No launchd/plist/host mutation |
| N3.4 | G-ROLE feasibility | Pushed N0; N1 if binary required | DEL-02-09 or DEL-02-10 primary evidence; citations elsewhere | Mechanism/configuration/instruction calibration | No mechanical non-delegation overclaim |
| N3.5 | Deterministic G-APPR feasibility | Pushed N0 | DEL-02-10 primary evidence; exact-pin citations from DEL-02-08 | Three-posture and routing fixtures | No network request, approval, or live grouping claim |
| N3.6 | Deterministic G-SENT feasibility | Pushed N0 | DEL-02-09 primary evidence; citations elsewhere | No-account preflight and denied-attempt fixtures | No authentication or live turn sentinel |
| N3.7 | Deterministic G-WIRE feasibility | Pushed N0 | DEL-02-10 primary evidence; citations elsewhere | Synthetic closed-event/redaction/multi-sink fixtures | No real secret or generated-schema claim |
| N4 | Fan in exact evidence and return one PR | Completed or calibrated unavailable N2/N3 results | DEL-02-12 fan-in; run records; Receipt 131 continuation | Claim matrix, manifests, cleanup/ancestry/input proofs, validations, PR | N0 ancestor preserved; all negative grants intact |

The N3 limbs may execute concurrently only when their writes and disposable
state are disjoint. A stopped limb does not stop an independent sibling. N0,
N1 when needed, and N2 retain their required order. No node may mutate product,
runtime, tool, App, Piping, Tier-0, workplan, pin, production configuration,
host launchd, credentials, or accepted immutable evidence.
