# Independent dependency integrity initial review

OpenAI GPT-6; exact serving ID unavailable. Actual Agent2 instruction-asserted/not mechanically enforced. No vendor/provider/account/package execution, installation, credentials, Git, product writes or delegation. Evidence-local controlled tests only.

## Changes required: D1 outside dependency mistaken for absence

When a declared optional/peer edge has no candidate inside runtimeRoot, runtime-dependencies.ts skips every ancestor/global lookup location and records absence before actual require resolution is checked. Node may resolve that same declared dependency from an ancestor node_modules outside the inventoried runtime. That dependency can execute outside the byte binding while the inventory succeeds. This is an integrity gap, not a request to enforce all peer semantic requirements.

Two controlled reproductions pass, demonstrating the flaw for both peerDependencies and optionalDependencies: temporary parent/runtime/packages/app declares escaped-dep, whose actual package is parent/node_modules/escaped-dep; createRequire(app/package.json).resolve returns the outside index.js while inventory reports packageCount1 and files[]. No package entrypoint executes. Repro source retained byte-identically as ancestor-resolution-repro.test.ts.source with mapping. Parent and implementation child accepted D1 and are repairing it. Outside ancestor package presence must not be represented as genuine absence; import-only exports need coverage too because require.resolve may throw for an ESM package that import would load.

## Other reviewed boundaries

Mandatory production inventory derives from core module location and includes first-party dist/manifests/lock plus whole files of declared selected production dependencies. The generic verifier compares supplied digests against the process generation before issuing admission, so a harmless subset cannot obtain a branded result. Existing canonical/link checks reject package file aliases, arbitrary workspace links and require entrypoints outside a selected package. Nested dependencies follow fresh lookup precedence; disagreement with Node's cached require resolution rejects.

Every generation check re-enumerates file/resolution identity; changed bytes, metadata, inode, file set, optional presence and observed resolution invalidate and permanently poison the process. Hash reuse is conditioned on dev/ino/size/mtimeNs/ctimeNs/mode/uid plus canonical path observation; private acceptance is uncached. The cache relies on trustworthy host metadata and does not prove actual loaded modules or atomic future execution. Package/edge/file/depth/byte bounds fail closed; observed per-check costs are seconds, not a cheap constant-time preflight.

Parent explicitly confirmed the intended boundary is installed declared closure, not package-manager validity or semver proof. All absent peers are recorded even if peerDependenciesMeta does not mark them optional. This does not assert required peers are satisfied and does not automatically install anything. D1 differs because the allegedly absent edge actually resolves outside the binding.

## Validation and limits

Existing conformance44 + dependency12 =56 PASS (38.97s), plus2 controlled reproductions PASS demonstrating D1. Reviewed source drift is recorded separately. No genuine conformance acceptance or live vendor activity occurred. Whole-package disk identity is not arbitrary dynamic-import, custom-loader or loaded-module proof; standalone/supervisor changes are outside this review. Await a separate immutable D1 repair backcheck before closing this slice.
