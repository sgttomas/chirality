# Literal root feasibility closure and supplier amendment candidate

Decision support only. OpenAI GPT-6, exact serving ID unavailable; ephemeral Agent2 role instruction-asserted. No binary execution, binary modification or production policy change in this subtask.

## Finding

No verified native configuration expression was found for a nonrecursive root-directory read. The inspected current OpenAI compiler accepts read/write exact paths and trailing /** by removing that suffix; other read/write glob patterns are rejected. Those readable paths then lower to Seatbelt Subpath. Therefore /** is recursive root access, and glob syntax is not an established narrow-root workaround. Deny glob support does not imply read-glob support. This is based on actual fetched current source, corroborated by the exact binary's diagnostic vocabulary; current source is not asserted to be the exact supply source tree.

Primary sources: https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/config/permissions.rs, compile_read_write_glob_path lines642–655; https://raw.githubusercontent.com/openai/codex/main/codex-rs/sandboxing/src/seatbelt.rs, read-root lowering lines475–478. The accepted no-platform-default requirement rules out treating :minimal as an interchangeable narrow permission.

Parent's paired host diagnostic was read from literal-root-diagnostic/RESULTS.json. Without the added rule the controlled process exited by SIGABRT (-6). Literal directory file-read-data alone and the variant also granting metadata both exited0 and emitted STARTEDCANARY_DENIED. Remaining /private/var/select/sh and getcwd warnings are retained: this demonstrates the startup/canary differential, not complete production compatibility or G-SBX closure.

## Smallest supplier/base-policy candidate

Add only this rule to the native macOS restricted base policy, where it applies to command and filesystem-helper startup as appropriate:

```scheme
(allow file-read-data (require-all (literal "/") (vnode-type DIRECTORY)))
```

No recursive root grant, platform bundle, command network change or write grant is included. Existing identity, private-account/control, protected-path and tool-process checks remain mandatory. The candidate is a narrowly evidenced compatibility repair, not a selected supply change. Supplier should add an automated startup test on the affected macOS/dyld build and negative unrelated-canary reads/writes, plus exact primary/descendant action tests. Verify the emitted policy diff and root-directory-only semantics in the actual rebuilt artifact.

## Authority and reconciliation implications

Changing or replacing the accepted executable changes its exact supply identity. Do not overwrite the existing artifact, label a local rebuild as the unchanged vendor release, reuse its digest, or treat G2's old acceptance as acceptance of new bytes. Prepare the new candidate's provenance/source revision, reproducible build details, dependency inventory, digest, version/build identity, license and signature assessment under DEL-02-08. Existing R13-B invalid-signature finding is not disposed merely by creating another build; any local/supplier signing and downstream packaged release basis need their actual accepted dispositions.

The changed candidate requires exact supply acceptance and any named pin amendment before production reliance. Re-run affected protocol/config/feature readback, named-profile isolation, primary/descendant G-SBX/G-PROT/G-ENV/G-SENT evidence and conformance identity fan-in. Update only authorized source-identity bindings and consumer references after acceptance; other held compatibility acts, account permission, activation and release remain separate. Root's D-GOV-20 boundary authority and runtime's product/supply ownership retain their existing division.

## Optional safe parser probe

If exact-pin parsing evidence is still required, use only a disposable project-local read glob such as <canonical disposable root>/probe/[a] = read, in a bounded config-read diagnostic with no turn. Current-source expectation is rejection of nontrailing read globs. It tests parser grammar without ever requesting recursive root reads. It is not a proposed literal-root solution. No safe working root-literal selector is claimed or invented here.

Recommendation: prepare the supplier repair/pin-impact package rather than broaden the runtime policy. The parent can complete unaffected implementation and evidence while the precise supply disposition is decided. This assessment does not select the supplier patch or create an owner ruling.
