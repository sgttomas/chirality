# Separate supplier candidate — preparation and evidence

Status: baseline and one-rule patched builds passed (1,059.69 s and 717.74 s). Both report 0.149.0 and their local ad-hoc signatures verify. Four selected protected-pattern source-helper tests passed; parent actual conformance is separate. This is a candidate package, not accepted supply, source authority, production readiness, or vendor signing.

The authorized input is OpenAI Codex commit `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0` (annotated release tag `rust-v0.149.0`). `SOURCE_VERIFICATION.json` checks the seven pinned upstream inputs. Isolated Rust 1.95.0 and verified V8 150.4.0 artifacts build the arm64 App Server and code-mode host. `run.py` records the frozen, offline build command and limits parallel jobs to four; caches, source, binaries and temporary output stay in declared scratch. Existing HOME was not repurposed; no global tools, keys, accepted binaries or accepted pins were changed.

## Shared baseline preparation

The tagged workspace manifests say version 0.149.0 but its Cargo.lock has workspace-local version 0.0.0 entries. Frozen fetch initially failed. `release-lock-normalization.patch` records all 139 workspace version substitutions used identically by both builds. All 1,218 external package records and their dependency/checksum/source fields remain unchanged. `CRATE_CHECKSUMS.json` checks all 1,028 downloaded crate archives against the lock checksums. `GIT_DEPENDENCY_CHECKOUTS.json` records the five fetched git checkouts. This is documented release metadata normalization, not a byte-for-byte reproduction of the vendor binary. Native-tool availability and build-script review are recorded separately; the review is not a full dependency security audit.

## Single behavioral patch

`APPLIED.patch` adds only `(allow file-read-data (require-all (literal "/") (vnode-type DIRECTORY)))` to the exact source base policy, with a comment. `PATCH_IDENTITY.json` pins the patch and resulting policy. The draft patch had a missing blank context line and failed its dry check without modifying source; the applied patch was generated against exact source and reverse-check verified.

The local source-policy comparison is in `policy-regression.json`: baseline aborts before shell startup; patched source starts, allows a project write, denies sibling read/write, and rejects a loopback socket operation with `Operation not permitted`. The first diagnostic used silent netcat and failed an overly specific stderr assertion; both initial recipe/results are retained, followed by the verbose diagnostic that establishes socket denial. These are direct source-policy observations, not proof of actual App Server primary/descendant turn conformance.

## Build and acceptance limits

The baseline version inspection reports 0.149.0. Its linker-created ad-hoc signature verifies locally and has no vendor TeamIdentifier. No signing identity was requested. The patched artifact will have its own identity and tests; it must not be substituted for the accepted pin merely because its version string matches.

The owner-facing alternatives after actual conformance are: retain the original accepted pin with affected execution unavailable; accept this distinctly identified local patched supply with explicit provenance/signing/support implications; or seek an upstream fix and then repin/retest its release. Candidate preparation selects none. Parent owns final provider conformance and any operational credentials. No issue publication or upstream/source acceptance is authorized by this evidence package.

Attribution: OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent 2; role instruction-asserted and not mechanically enforced. Agent 0 role is not mechanically enforced.
