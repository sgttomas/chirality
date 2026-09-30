# Guard review disposition and read-only provider witness

ROOT accepts the fresh independent review at
`instances/GUARD-REVIEW/REVIEW.md`, SHA256
`5b5ec41086242143cb24c14b6b0e30ad57fff04c001cd9e6fe1afb8cb25b7924`,
covering candidate `fe6ca966259d29d8d6ed2f05460400f6cb5d5de0` against main
`292e123db9117e097c2dfbbecaf7a93de86c3c6b`. No live qualification is inferred.

GR-01 and GR-02 block compile admission. DELIVERY may resume the original
guard TASK in the slot released by the reviewer, writing only the additive
`tools/host_guard_v2.py` and `instances/GUARD-IMPLEMENTATION/continuation_01/**`.
Preserve all v1 bytes. Minimal argument validation repair and pure tests only;
independent backcheck precedes compilation. A0 preparation holds the other slot.

The reviewer finds the exact low-memory provider/fixture qualification suitable
for ROOT's next bounded invocation. ROOT grants its own read-only provider
witness first, using reviewed v1 SHA256
`feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db` and
`instances/ROOT-GUARD-QUALIFICATION/provider_witness.py`. It performs three
serialized samples, validates self identity, queries own RSS/footprint and
compares own RSS coarsely with ps. It runs no workload or compiler, creates
no workload session/group, and sends no workload signal. Provider command
cleanup retains its direct-child ownership. Preserve raw outputs locally and
sanitized evidence with hashes. Only the response-owned runtime/guard/log
directories may be changed to private mode as required by the reviewed plan.

This is the first stage of qualification, not general heavy-work admission.
Any failed/unknown provider observation stops advancement. Subsequent fixture
runs retain the reviewed 64-MiB maximum explicit allocation and their separate
ROOT command grants; all compiler/numerical work remains ungranted.
