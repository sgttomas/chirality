# DEL-07-01-V3-01 boundary candidate — not authorized implementation

Status: CANDIDATE_FOR_PARENT_REVIEW. No product bytes changed. No owner ruling or acceptance claimed.

## Basis and exact boundary

The live DEL-07-01 `_STATUS.md` Remaining item requires a SHA-256 per asset pin verified at boot and two-layer write/root/proposal-path protection. Its write locus names `frontend/src/lib/harness/instruction-root.ts` and path-policy helpers, tests, and `frontend/electron/daemon-instruction-root.ts` only if daemon enforcement is necessary. It does not name `frontend/electron/main.ts`.

The controlling SCA-APP-010 ScopeOfWork current contract requires the organisation layer to be hash-pinned, read-only during ordinary execution, packaging-checked, separate from the working root, and never a working root/proposal path (SOW-084, decomposition L254/L357/L487). Packaging checks belong to DEL-08-01; instruction composition belongs to DEL-04-04. Those responsibilities are not absorbed here.

Current App readability checks call `assertInstructionRootReadable`, but daemon startup bypasses them. `main.ts:initializeDaemon` calls `resolvePackagedDaemonInstructionRoot` only when packaged; the development branch directly sets CHIRALITY_INSTRUCTION_ROOT. Both paths then call startRuntimeHost. Putting verification solely into the named resolver misses development boot; putting it solely in readability helpers does not prove either live boot path.

## Minimal additional locus

`MAIN_BOOT_SEAM_CANDIDATE.diff` is an exact patch against the SHA in SOURCE_IDENTITIES.sha256. It adds one import and one awaited call after both root-resolution branches and before startRuntimeHost. No root selection, credentials, runtime tool registration, provider, or process policy changes. The proposed new export is implemented in the already-named `electron/daemon-instruction-root.ts` and invokes a pure/local verifier in the App harness helper. It returns immediately when no organisation layer is configured; when configured it resolves the already-registered project roots, checks canonical separation, and verifies pins. Invalid configuration, unavailable registration, overlap, unsafe assets, and hash mismatch throw before runtime boot. The call is outside the existing fallback catch, so integrity failure cannot downgrade to packaged resources.

This is the narrow candidate the parent must either accept as an ordinary owned caller integration or route for owner scope clarification. This proposal does not resolve that authority classification itself.

## Explicit local configuration candidate

The sources require pinning but do not define a file format or configuration carrier. Proposed ordinary implementation choices, requiring parent freeze:

- CHIRALITY_ORGANISATION_ROOT: absolute local directory. Absence together with absent pin digest means the existing bundled-only configuration.
- CHIRALITY_ORGANISATION_PINS_SHA256: exactly 64 lowercase hexadecimal characters, SHA-256 of the exact manifest bytes. Both variables must be present together; partial/blank/relative configuration fails closed.
- Fixed manifest at `<organisationRoot>/organisation-pins.json`:

```json
{"schema":"chirality-organisation-pins/v1","assets":[{"path":"agents/AGENT_EXAMPLE.md","sha256":"<64 lowercase hex>"}]}
```

No path or host configuration is written into project truth. The verifier reads only; it never creates/updates a manifest or changes modes. Expected manifest digest comes from explicit deployment configuration rather than trusting a replaceable manifest to authenticate itself. Pinning checks integrity against configured expected bytes, not signer identity or professional acceptance.

Strict manifest contract: exact keys, nonempty unique sorted asset paths, exact digest shape, relative POSIX paths, no empty/dot/dotdot segments, no backslashes/absolute paths; manifest cannot list itself. Reject symlinks in the root resolution chain and every asset path, special files, missing files, duplicate entries, extra keys, unreadable bytes, unlisted files, and digest mismatch. Compare every regular asset under the root except the fixed manifest to the inventory. Canonical organisation root must be disjoint (neither ancestor nor descendant) from working root and bundled base. Verify per boot and App instruction-read entry, not a stale process cache.

## Remaining implementation loci if candidate accepted

- `frontend/src/lib/harness/organisation-layer.ts`: config parsing, manifest/asset verification, canonical overlap/protected-target helpers.
- `frontend/src/lib/harness/instruction-root.ts`: invoke verifier in readability path; expose two-layer protected-root predicate without changing bundled-only behavior.
- `frontend/src/lib/harness/tool-path-policy.ts`: reject org targets for writes even where managed targets allow them; preserve symlink rejection and working-root containment.
- `frontend/src/lib/harness/session-manager.ts`: only working-root validation call integration, rejecting org overlap/canonical aliases.
- `frontend/electron/daemon-instruction-root.ts`: export assertDaemonOrganisationLayerReady with explicit typed args `{ instructionRoot, projectId, resolveProjectRoots }`; use registered working root, no fallback if configured verification fails.
- `frontend/electron/main.ts`: only attached seam.
- Dedicated tests `src/__tests__/lib/organisation-layer.test.ts`, existing `harness-instruction-root.test.ts`, and `src/__tests__/electron/daemon-instruction-root.test.ts`; path-policy fixtures may use new `organisation-layer-path-policy.test.ts` to avoid unrelated test writers.

## Acceptance and limitations to preserve

Fixtures must prove absent config compatibility; every malformed/partial config; pin/asset mutation; manifest inventory attacks; traversal and symlink cases; disjoint roots; both-layer write denials; organisation rejected as project/proposal path; and boot rejection before runtime invocation. Fresh read-only TASK software-code-review must review all frozen product/test bytes. Parent owns final registered gates and A1 re-stage record.

Root runtime ProjectRegistry currently returns only `{workingRoot, instructionRoot}` (`runtime/packages/core/src/project-registry.ts`). This proposal changes neither that schema nor daemon/CLI universal path enforcement. If the accepted return is interpreted to require newly configured organisation roots in all Root-owned tool/CLI flows, that is an additional Root-owned integration dependency and cannot be certified from the App helper fixtures or this startup seam. Surface it; never claim a helper proves untested downstream enforcement.

## Handoff

Derivative proposal based on the live carrier, D-APP-108 selectability and Q14 cited by the carrier, accepted SCA-010 decomposition, accepted DepClosure snapshot CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034. Closure NOT_IMPLEMENTED. No derivative acceptance/pointer changes. Rerun patch applicability and preflight after any source change. Next owner HELP_HUMAN: disposition exact main.ts scope and configuration carrier, then freeze brief or route owner question. DEL-07-03 remains independent.

Attribution: OpenAI GPT-6 per parent context; exact serving ID unavailable; delegated-harness-native; WORKING_ITEMS role instruction-asserted. No child dispatched.
