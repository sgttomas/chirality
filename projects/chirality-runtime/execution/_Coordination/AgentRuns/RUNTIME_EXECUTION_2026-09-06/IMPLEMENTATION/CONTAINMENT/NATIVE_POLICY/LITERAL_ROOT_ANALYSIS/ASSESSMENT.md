# Literal root-directory access: source-grounded candidate

Read-only analysis; no vendor or system differential execution in this subtask. Parent owns the proposed isolated differential. Existing early offline containment tests already found literal root-directory access fixes a dyld startup abort in our custom profile; that is evidence about that profile, not proof of the current native App Server profile.

## Findings

Current official OpenAI seatbelt.rs, build_seatbelt_access_policy, maps read roots to Subpath; the Literal alternative is used for writable non-directory roots. Thus ordinary permissions filesystem '/'='read' grants recursive access and must not be used as the literal-directory fix. Current named policy types inspected earlier expose path/glob/special plus access; no verified nonrecursive read selector was found. This is a bounded source finding, not a proof that every exact-pin interface lacks such a selector.

`:minimal` selects a platform-default policy bundle, not just a directory handle. Current official policy source includes broad system/preferences/database roots and additional special-file/device grants. It cannot be represented as equivalent to the narrowly needed literal root read. Do not add it by assuming its name proves minimality. Current upstream source is not asserted to match the accepted executable byte-for-byte.

Apple's published DyldProcessConfig.cpp CacheFinder enters libignition through ignite, corroborating the owned crash frames. That source does not expose the full private ignition implementation or establish the specific failing open in this exact OS build. The parent's local dyld string 'failed to open canonical root' is suggestive, and the controlled differential can test it directly.

Primary sources:
- https://raw.githubusercontent.com/openai/codex/main/codex-rs/sandboxing/src/seatbelt.rs (read-root lowering around lines475–478).
- https://raw.githubusercontent.com/openai/codex/main/codex-rs/sandboxing/src/seatbelt_read_only_platform_defaults.sbpl (bundle contents).
- https://raw.githubusercontent.com/apple-oss-distributions/dyld/main/dyld/DyldProcessConfig.cpp (CacheFinder ignition call around lines1089–1112).

## Concrete safe diagnostic candidate

Keep the same explicit command/system read roots, all deny controls and command-network-off policy. Compare otherwise identical isolated Seatbelt profiles with and without:

```scheme
(allow file-read-data (require-all (literal "/") (vnode-type DIRECTORY)))
```

Run only the controlled system printf/sh sentinel under the parent's authorized diagnostic. Pair positive startup with actual unrelated canary reads still denied. If metadata is independently necessary, test it as a separate exact literal-directory allowance, not a recursive root grant. Capture final emitted SBPL and exact differences.

A passing differential would isolate a base-policy resource gap. It would not itself supply a supported native configuration expression. Next inspect exact generated native policy/API for a literal-directory facility; if none exists, prepare the smallest base-policy patch or supply-resolution proposal, rather than weaken restricted reads. No claimed automatic waiver, broad default admission, or immediate owner decision follows solely from this diagnosis.
