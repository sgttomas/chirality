# Deployed dependency integrity — bounded implementation return

OpenAI GPT-6; exact serving model ID unavailable. Agent 2 is instruction-asserted, not mechanically enforced. Derivative implementation/evidence package, not accepted source truth. Parent AM11 ordinary implementation release; no owner acceptance, hold lift, live account/provider call, package installation or network action.

## Accepted-source mapping and scope

DEL-02-12 ScopeOfWork.md OUT-002 lines63–65 binds source_identity to exact accepted implementation bytes. Release execution plan AT-039 line852 binds source/dependency lock/resolved supply/config identity; line881 says dependency drift invalidates tested exact-byte evidence. These support identifying deployed dependencies as part of conformance identity. They do not mandate re-reading every installed byte on every admission, nor authorize this child to accept a release.

The new helper traverses dependencies and optionalDependencies from the Runtime workspace root manifest and every immediate Runtime package manifest, plus declared installed peer edges. Missing optional/peer edges are recorded; missing required production edges fail. Dev-only edges are excluded. Node's actual lookup-directory precedence is confined to the Runtime root. Known workspace links must have exactly the expected relative target; external/unknown links, aliases, unsafe files and resolved require entrypoints outside their selected package fail. A disagreement between fresh lookup and Node's cached require resolution also fails closed. No user-global package search is inspected.

All files in each selected external package are inventoried, including conditional exports and resources; nested node_modules are traversed through declared edges. Canonical paths, versions, selected lookup roots, link targets, require entries where available and resolution identity metadata bind the package digest. Import-only/type-only packages may lack a require entry; whole-package bytes remain bound. Runtime root package.json and lockfile, all Runtime package manifests and dist files remain included.

## Generation and cache behavior

Production inventory roots are derived from the core module location, never from caller-selected harmless paths. The generic verifier must match the mandatory process inventory digests before issuing any branded admission. Controlled test inventories cannot replace the production singleton.

The module-evaluation generation guard remains mandatory and irreversible. Every check re-enumerates deployed package trees and actual resolution edges. Cached content hashes are reused only after canonical-path and dev/ino/size/mtimeNs/ctimeNs/mode/uid checks against an open file and current path; changed metadata causes a byte rehash. Generation fingerprints still permanently reject observed metadata, file-set, byte or resolution changes, including byte restoration or new verifier construction. Private acceptance records are reread without the content cache and external acceptance is reconsulted. File reads are bounded and batched at64 concurrent operations.

Bounds:1024 package roots,16,384 dependency edges,50,000 external package files/directories,64 tree depth,512MiB per file and2GiB aggregate external package bytes. Every exceeded bound fails closed; no automatic partial inventory. Root manifest and dist inventory are additionally subject to existing file-read bounds.

## Calibration and operational cost

This extends the earlier GENERATION_FREEZE calibration addendum: installed declared production dependency bytes and their observed resolution bindings are now covered. It remains a disk/deployment-generation check, not complete proof of executed bytes. Node's loaded module cache, imports racing startup capture, arbitrary undeclared or computed dynamic imports, custom loaders and subsequent OS changes are not comprehensively measured. Whole-package hashing is not a complete SBOM/license audit or supply-chain signature attestation. Host stat identities are assumed trustworthy; this does not defend against a privileged filesystem adversary that can forge them.

The complete selected closure has233 external packages plus seven Runtime packages and the workspace root manifest. It includes35,598 external files and210,099,611 bytes. Node24.18.0 measured startup plus first check8.42s, unchanged check3.80s and inventory-only traversal2.90s; exact local observations are recorded in benchmark.json. An unchanged check costs several seconds and a successful admission performs checks before and after acceptance. Expensive canaries are not rerun automatically for unchanged evidence. Broad isolated test runs may incur repeated startup-inventory work. A changed deployment requires a new process and separately accepted matching conformance evidence.

## Validation and handoff

Workspace TypeScript build passed. Existing44 conformance tests and12 new dependency tests pass (tests-verified.log). New coverage includes transitive and installed-peer inclusion/dev-only exclusion, optional absence/presence, nested lookup precedence/cache disagreement, exact workspace symlink binding and replacement, external/symlink rejection, escaped main entry, content mutation with restored mtime, same-byte inode replacement, new package file, new optional package, resolution-parent replacement and permanent poison after restoration/new verifier.

Historical failed logs also preserve a test-only stale Pi package-name expectation, subsequently corrected to the installed @earendil-works package name. Earlier failed test log preserves the discovery of Node's cached resolution behavior; final tests exercise the corrected fail-closed expectation. No test fixture establishes owner acceptance or a production canary result. Supervisor/standalone sources were not changed. Independent review of this extension remains parent fan-in work; the prior C1 repair review remains valid only at its own historical pins.
