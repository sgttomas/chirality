# Provider host versus action containment

Read-only assessment by OpenAI GPT-6 ephemeral Agent 2; exact serving model ID unavailable, role instruction-asserted. No vendor execution, account action or code changes. Repository-relative line anchors below identify sources inspected live.

## Conclusion

The inspected accepted sources do not require our newly introduced sandbox-exec wrapper around the entire trusted App Server process. They expressly assign enforcement to the exact App Server/Seatbelt policy for primary and descendant actions. A trusted, daemon-owned exact App Server with native kernel-enforced action boundaries is a supportable ordinary implementation topology, subject to proving those actual boundaries. Removing our experimental wrapper is not by itself an amendment of a prescribed production topology.

However, per-command sandboxing plus private HOME and protocol allowlisting is not sufficient evidence: all primary and descendant read/file-change/shell actions, protected paths, root/profile/account identity, process lifetime and provider-service endpoints remain constrained. An unsandboxed provider host that exposes uncontained in-process file tools or unrestricted client RPCs would weaken the accepted boundary. That is not authorized by calling the binary trusted.

## Exact sources

- `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html:542`: “the exact packaged App Server enforces the policy for primary and descendant actions inside a root-specific worker.” The same line says “RC does not adopt Apple App Sandbox” and requires G-SBX proof of “the App Server/Seatbelt policy and enclosing process posture in that exact bundle.” Apple App Sandbox and our ad hoc sandbox-exec wrapper are distinct mechanisms; the quoted exclusion alone would not decide the wrapper question, but the explicit enforcement assignment does.
- Same file:552 requires every turn's root-specific `workspaceWrite.readOnlyAccess`, or restricted `readOnly.access`, with no platform defaults; canonical-root-only writes, excluded `/tmp` and actual TMPDIR, root-local private scratch, login shells off and command network disabled.
- Same file:831: “Under the exact turn/start policy used by production” primary/descendant probes must reject sibling/home canary reads and outside/temp writes. It explicitly says the probe is not substituted with `command/exec`, and client shell/process methods must be unreachable.
- Same file:833 distinguishes “OpenAI adapter service traffic” restricted to the governed endpoint set from command/tool network explicitly false. Thus provider transport and command network are separate authority surfaces.
- `plans/steers/chirality_app_v3_r16_g05_and_spikes_steer_root_2026-08-27.md:267–279` grounds G-SBX in exact App Server restricted policy properties and G-PROT in read, file-change and shell-write representations for primary and descendant actions. It calls any inexpressible/untestable protected rule blocking, not an accepted subset.
- `plans/steers/chirality_app_v3_root_ruling_record_r12_2026-08-24.md:41–53` expressly scopes disposable-home/no-account/no-outside-write execution to G2 supply evidence. That diagnostic grant does not itself prescribe every production provider-process wrapper.
- `plans/steers/chirality_app_v3_root_ruling_record_r15_2026-08-25.md:28–33` accepts only exact supply and explicitly does not authorize implementation/activation/release/reliance or lift bindings. It provides no independent production topology waiver.
- `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md:57–69` puts native descendants inside the hard outer envelope and says lack of native topology limits does not relax filesystem/network/process/canonical-root/account/policy boundaries. It does not name a required whole-provider wrapper.
- `AGENTS.md:87–90` retains the same hard outer envelope for native descendant facility, without prescribing an OS wrapper around the trusted provider host.
- Live DEL-02-07 ScopeOfWork.md:22–34 and REQ-005/008 require the daemon/supervisor topology, single broker and unchanged hard containment; AX-004 says unchanged outer containment. DEL-02-09:21–29 and REQ-001/004 require root-private app-owned CODEX_HOME, ambient ~/.codex exclusion and command network default off. DEL-02-10 CLM-004 and DEL-02-12 AC-004 retain claim calibration and unchanged hard containment. These contracts preserve outcomes, not the specific new wrapper implementation.

## Decision boundary

Proceed with a design amendment and controlled evidence for native restricted App Server/Seatbelt enforcement under the existing authorized implementation scope if the parent confirms that scope includes the experiment. Do not claim production readiness until actual primary/descendant action sentinels and the complete private broker/control boundary pass. A new owner decision is necessary only to weaken those accepted properties, select a separately gated fallback, release a held binding, authorize account/provider use, or release/adopt—not merely to replace an unnecessary experimental outer wrapper with the architecture already described by the accepted plan.

This assessment does not authorize unsandboxed vendor execution; the parent must reconcile the current experiment-specific authority before any new run. No such execution occurred here.
