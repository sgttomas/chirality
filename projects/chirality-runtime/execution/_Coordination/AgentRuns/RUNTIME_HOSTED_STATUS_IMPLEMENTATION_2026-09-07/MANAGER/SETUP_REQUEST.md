# Proposed bounded validation setup exception

NOT GRANTED OR EXECUTED. Current Runtime node_modules is absent; authorized typecheck failed127 (tsc not found). Node v24.18.0 and npm11.16.0 are present; Node meets package engines >=22.19.0 and npm11 supports existing lockfileVersion3. No dependency version or package/lock edit is proposed.

Exact existing inputs: package.json SHA256 57c41cea4d4eab75c85af37ff55a31a1f3a2edbaf8fef6da97424e14d24a46ae; package-lock.json SHA256 b856eb9357becc7abb10cd0030a920e61afb7f5aaf24830c69261726a43c3acf. Lock resolved HTTP URLs use registry.npmjs.org. All Runtime workspace package manifests must be rehashed before/after setup, and unchanged package/lock bytes are required. No available cache is assumed.

Proposed one-time command from /private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime:

```sh
npm ci --ignore-scripts --no-audit --no-fund --registry=https://registry.npmjs.org --cache=./.custody-npm-cache
```

Permit network retrieval only for the existing lock's registry.npmjs.org packages/integrity-checked tarballs. Permit generated installation tree under this Runtime workspace (node_modules, its workspace links, any npm workspace-local node_modules) and .custody-npm-cache/logs only. npm ci may replace existing node_modules if one appears; therefore stop on unexpected preexisting installation rather than discard it. Do not alter manifests, lockfile, npm configuration or versions. --ignore-scripts disables dependency lifecycle scripts, including native postinstall; do not invoke them later as a workaround. --no-audit/--no-fund avoid unrelated requests. Stop on other registry/authentication, missing integrity, lock mismatch or unsafe install behavior; report instead of changing dependencies. No supplier/provider/keychain/login/protected operation or product release is granted.

This is a setup exception to the prior no-install exclusion, not a dependency upgrade. After exact setup receipt and unchanged-input checks, resume only the four already authorized validation commands. Existing scripts may still fail because ignored postinstall did not prepare an artifact; report that actual failure, do not run extra setup silently. Local generated cache/installation outputs are excluded from publication; retain command/result and exact inputs in evidence. Standing Git authority remains unchanged.

Proposed owner act: “I authorize this one bounded lockfile-preserving npm ci setup command and stated Runtime-local installation/cache effects, solely to enable the four already approved checks. No dependency change or lifecycle-script execution is authorized.”
