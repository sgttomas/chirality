# DRAFT / UNROUTED — App handoff for Pi 0.82.0 Option A evidence hold

Status: `DRAFT ONLY — ROOT EVALUATION QUARANTINE — NOT ROUTED`
From: Root EVALUATION / E2
Prospective recipient: Chirality App Dev loop
Effect: none

## Why this draft exists

The Root owner selected Pi Option A under evidence hold. The selection keeps Pi
`0.82.0` as the preferred candidate only. It does not approve it, supersede
D-APP-72/SCA-APP-002 `0.80.10`, authorize App work, or write any App surface.

If the App loop elects to take up this request under its own authority, Root
asks it to consider the App-owned work units `PIA-U20` through `PIA-U25` in
`OPTION_A_WORK_UNITS.csv`. App may accept, amend, decline, split, or defer them.

## Frozen inbound references

- Root owner continuation ruling SHA-256:
  `9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`.
- D-APP-84 REV2 Root route SHA-256:
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- E1 report SHA-256:
  `e5253fbb40dfa1159981d87073d415e6156adb338f51316be0a97ac1c7f620c1`.
- E1 findings SHA-256:
  `10c9e70b1db6e456d287c46e02578087958c89da763e829919823ddc3d0917d0`.
- Provisional identity basis: `OPTION_A_IDENTITY_BASIS.json` (hash to be
  supplied by the E2 closeout return).

## Requested App-owned evidence, subject to App acceptance

1. repair the packaged-Pi proof entrypoint and test that both direct asset and
   production-route children execute and fail closed;
2. perform exact-lock clean-install, dependency, SRI, lifecycle, and realized
   module-topology validation;
3. build the exact macOS package and preserve ASAR/unpacked/native/WASM
   inventories, hashes, load results, and both packaged Pi proofs;
4. rerun full and focused source regression/conformance on the final candidate;
5. repeat the opt-in live oMLX proof at the candidate version only after exact
   owner authorization for model/credential use; and
6. prepare complete packaged-closure notice provenance as a release-only hold.

Every bundle should follow the immutable evidence contract in
`OPTION_A_CONTINUATION_PROTOCOL.md`. Root requests returned hashes and evidence
references, not an App authority change.

## Questions App must retain for its own later gate

- Whether App will retain `PiAgentEngineAdapter` as an explicitly named
  affected-client implementation or consume a Root-canonical implementation.
- Whether Electron `43.2.0` is proposed as a successor to D-APP-72's `43.1.1`
  prerequisite fact.
- Whether and how App product/decomposition/SCA surfaces change after a Root
  version/identity acceptance.
- Whether any proof work requires an App SCOPE_CHANGE before implementation.

## Preserved holds

- D-APP-72/SCA-APP-002 `0.80.10` remains operative.
- No dependency, lockfile, adapter, package, notice, authority, decomposition,
  lifecycle, release, or reliance write is authorized by this draft.
- No Pi native tool, Bash, sandbox, delegation, remote provider, fallback, or
  durable-resume capability is requested here.
- No App decision or receipt is presumed.

## Draft disposition

Retain inside the Root EVALUATION package until HELP_HUMAN and the human owner
decide whether to route it. If routed later, bind the final E2 artifact hashes
and preserve this draft's unrouted provenance rather than rewriting history.
