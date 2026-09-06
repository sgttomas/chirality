# Pi SDK compaction, continuity, and bound callback return

Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent 2 role is instruction-asserted and not mechanically enforced. No child delegation. Authority: parent-released IMPLEMENTATION_AMENDMENT_9.json and IMPLEMENTATION_AMENDMENT_10.json; manager PI_IMPLEMENTATION/BRIEF.json and MANAGER_COMPOSITION/PLAN.md. This is implementation evidence, not owner acceptance or TM-ROOT-106 closure.

## Result

The actual installed Pi 0.82 SDK runs bounded automatic compaction. Its real compaction_start/compaction_end events map to the existing canonical context lifecycle with session/turn identity and metadata only. Summarization uses the same bounded loopback transport, requests no tools, and rejects tool calls in summary responses. Explicit idle/manual compaction is not exposed by this port. No durable resume is claimed.

Each Runtime session retains an in-memory SDK SessionManager across turns. Cache fingerprint binds root/model, credential hash, role/tool/turn budget, parentage, instruction/brief/context/write/approval/boot/runtime identity, host system prompt and protected paths, and exact callback registration. Changed identity/scope requires a fresh Runtime session. Count and TTL are bounded; active sessions are never evicted. Expired, failed, interrupted, and revoked session IDs cannot silently restart. Retired identity tombstones are capped by refusing new admissions, not forgetting denied history. Each turn still creates and disposes its isolated AgentSession exactly once; no SDK durable files are created. Cache survives only within this port instance.

PiRuntimePort exposes toolBindings.bind(sessionId, tools) and close(). The exact read_file empty-object coordinator schema binds one host-selected regular file. Model-supplied paths, alternative schema, root escape, symlink components, protected paths, and hardlinks are rejected. The bridge invokes the supplied Runtime callback and forwards its returned text to the SDK; it never constructs a read receipt. Callback invocation is abort bounded even when an injected callback ignores AbortSignal. A governed child requires a live binding; release invalidates its cache and active turn, without fallback to project-wide read. The trusted coordinator remains responsible for its callback implementation and receipt semantics; core metadata/descriptor revalidation is independently repaired by the managed_core child.

The observed real oMLX response shape with absent content plus nonempty valid tool_calls is accepted as no text. Other arbitrary content types remain rejected. reasoning_content is ignored and absent from replay and canonical output.

## Validation

21 real installed SDK tests pass using synthetic credential and injected fake provider transport. Tests cover actual read loops, ambient resource isolation, strict transport and model identity, malformed/oversized responses, path denial, interruption, hung-provider deadline, concurrent turn exclusion, actual automatic compaction and summary tool denial, compaction context reuse, account/scope changes, bounded count/TTL, active-session retention, actual bound callback execution, model path rejection, callback revocation, and no broad-read fallback. Runtime workspace typecheck passes. Tests do not contact the user's oMLX server or exercise actual credentials. Parent owns empirical live provider evidence and final integration validation.

## Handoff

Changed source is limited to owned Pi port/read tool/event mapper/export and dedicated tests. Historical PORT/ and COMPACTION/*.before.gz are preserved. Source hashes bind this return to current implementation; later manager changes require rerunning affected tests. Remaining work belongs to parent/sibling: standalone composition of toolBindings and shutdown close, coordinator receipt validation, overall suite and empirical live test, then owner review. No product surface or governance ruling selected here.
