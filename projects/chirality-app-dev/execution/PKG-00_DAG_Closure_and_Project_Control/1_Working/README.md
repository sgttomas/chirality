# PKG-00 Working Records

This folder holds mutable project-control records for DAG closure.

`DEL-00-*` folders here are control deliverables for SCC closure. They do not participate in the product deliverable dependency graph unless a future human ruling explicitly adds `Dependencies.csv` registers and promotes them into graph scope.

## Current Control Deliverables

- `DEL-00-01_SCC-002_PKG-10_Policy_Proposal_Closure` is `SEMANTIC_READY` with TASK run-record provenance for lifecycle repair, four-documents P1/P2, semantic matrix build, lens-register, and four-documents P3.
- `DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure` is `SEMANTIC_READY` with TASK run-record provenance for lifecycle repair, four-documents P1/P2, semantic matrix build, lens-register, and four-documents P3.

Both folders remain control-plane artifacts. Their readiness prepares SCC closure work; it is not itself a DepClosure ruling.

## SCC Resolution Cases

Each `scc-cases/CASE-SCC-*` folder is a living TASK-updated receptacle for SCC resolution work. Cases collect deliverable-local findings, evidence, open human questions, candidate remedies, rulings, and owner-workflow handoffs. They are intentionally local to PKG-00 and do not mutate product deliverables or dependency rows.

- `DEL-00-01/.../scc-cases/CASE-SCC-002_PKG-10_Policy_Proposal`
- `DEL-00-02/.../scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling`

The existing `scope-change-packets/PKG00-SCA-PACKET-*` folders remain as prior TASK outputs and are copied into each case under `case-seeds/`. The packets are seed evidence only. A human may later choose to initiate SCOPE_CHANGE from a case handoff, but neither packet readiness nor case readiness starts SCOPE_CHANGE or bypasses SCOPE_CHANGE gates.
