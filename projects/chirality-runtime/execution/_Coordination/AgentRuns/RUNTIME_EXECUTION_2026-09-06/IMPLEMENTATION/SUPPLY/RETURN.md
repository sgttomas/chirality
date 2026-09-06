# Exact supply verifier return

Executor: OpenAI GPT-6, exact serving model ID unavailable; bounded Agent 2 role instruction-asserted, not mechanically enforced. No delegation, downloads, executable invocation, accounts or operational state.

Implemented fixed production `verifyExactSupply({executablePath, expectedSha256?, expectedVersion?})`, `revalidateExactSupply(descriptor)`, immutable `ACCEPTED_SUPPLY`, and distinct explicit `createControlledSupplyVerifierForTests(profile)` seam. Production overrides must match the accepted SHA256/version and cannot replace them. Payload size is also fixed at 179721344 bytes. Paths must be canonical absolute regular files with no symlink traversal. Hashing uses an O_NOFOLLOW descriptor; path and descriptor identities are checked before and after reading. Descriptor and nested file identity are frozen; a process-local WeakSet issuance seal rejects forgery, deserialization and fixture substitution. Each new process must verify again.

Version 0.149.0 is mapped from the accepted exact payload hash, not claimed as an executed --version observation. `OPEN_G5_FINDING_INVALID_VENDOR_SIGNATURE` remains explicit. Verification supplies no signature approval, launch grant, production acceptance or release authority.

`revalidateExactSupply` rehashes and checks dev/inode/size/mtime/ctime immediately before a caller's launch. Path-based OS execution still has a residual race after the check; this is a reduction of TOCTOU exposure, not an atomic verify-and-exec guarantee. Parent must integrate revalidation at launch and preserve that limit.

Validation: `npm run build` PASS; `npx vitest run tests/exact-supply.test.ts` PASS, 9 tests. Actual disposable-file tests cover unknown production overrides, missing supply, immutable controlled descriptors, byte/size drift, identical-byte inode replacement, forged/cross-instance/fixture production descriptors, symlinks and parent aliases, nonregular/relative paths, and post-verification symlink replacement. The accepted binary was not supplied to this specialist; no accepted-payload positive verification is claimed. Parent's separate exact-artifact probe can supply that evidence without changing this test claim.

Code writes remain exactly the two assigned files. Parent owns exports, broker integration and full test fan-in. No remaining known local defect. This packet is derivative implementation evidence, not authority or an accepted deliverable completion.
