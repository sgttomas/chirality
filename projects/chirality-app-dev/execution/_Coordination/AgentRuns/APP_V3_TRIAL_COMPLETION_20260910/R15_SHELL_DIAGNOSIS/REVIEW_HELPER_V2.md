# Independent preparation helper v2 review

**PASS for the narrow helper v2 correction against the frozen inputs.** Parent may release within the already approved supplier scope. This is not build or qualification success.

Reviewed `/private/tmp/chirality-supplier-root-directory-fix-20260911-01/prepare-and-build-v2.py`, SHA256 `a703b41d0c7a00022d6f110a23960e7fcc3356ce5e81a9325aada1f6b02d3883`, against prior helper, FIRST_FAILURE.json, source-correspondence-failure-details.json and approved BUILD_RECIPE manifest `cf52b048015cfab86f377760f657191ac94ca4912bb08defebe1cc839c09d8f0`. Independent TASK / Type 2; no delegation, helper/supplier execution, source changes, live/account reads or downloads. Only read-only source/cache/target inventory checks and this report write performed.

The v2 diff corrects regular-file inventory semantics with lstat, compares the complete baseline first, then explicitly records and removes only `.git/` administrative entries for the copied source. It also uses a fresh failure-evidence filename. It does not remove arbitrary differences or alter cloning, candidate application or build execution.

Independent read-only hashing found **6,443 / 6,443 regular entries match exactly**, with no differences. The 24 `.git/` regular entries match before their deliberate exclusion; 6,419 regular source entries remain. Baseline manifest SHA256 matches approved `4e5250720d8a947e815602fb38352726b9e2c7f16d5d219ef5d450d2ea129d16`. The prior 6,420 observation omitted .git and erroneously followed the bubblewrap LICENSE symlink as an additional regular file. Thus the change restores the pinned schema rather than weakening source correspondence.

Actual internal links inspected without following directory links:

- Source `codex-rs/vendor/bubblewrap/LICENSE -> COPYING`.
- Cargo git `checkouts/nucleo-425d994cd74b3654/4253de9/matcher/LICENSE -> ../LICENSE`.
- Registry and retained target contain no symlinks.

Both link targets are contained regular files copied before their links by the helper's sorted traversal. Link text is preserved, external/absolute links fail closed, and these copied links resolve inside their corresponding copied trees. The immediate destination is_file check is not a general directory-link/order-independent copier, but it is valid for these frozen inputs; generalizing it is not required for this release.

COW cloning uses exclusive clonefile destinations, verifies equal bytes/modes and distinct device/inode pairs, and checks source identity/size/timestamps after copying. No hardlinks or writes to retained inputs are introduced. New directories fail if already present. The exact candidate patch and target before/after hashes remain enforced; the candidate regular-file inventory must differ at exactly the one Seatbelt base-policy path.

The actual isolated build-invocation.json SHA256 `b2473c41ea47872635622b00a743bbb0dc069d1087ab97206d518095604ded7d` and build-enclosure.sb SHA256 `6f8fada36a25bc332db157f9d31d9afbab4efa11749a83ba57243e206d2a2dfb` match the approved recipe. The mapped isolated cwd/target/cache, sanitized environment, locked/offline build and network-denied sandbox remain unchanged. No expanded supplier capability or new owner decision is introduced by normalization.

Remaining execution evidence: the helper checks candidate source after build but does not itself implement the recipe's complete post-build retained source/cache/target inventory comparison. Parent must collect that preserved-input comparison, Mach-O/artifact identity and approved qualification evidence before closeout. This obligation does not block the narrow helper fix. No copying, compilation, native tool qualification or retirement result is claimed by this review.
