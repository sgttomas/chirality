# RETURN — additive guard v2 repair candidate

**GR-01/GR-02 repaired in source and pure tests; independent backcheck required.**
No compiler/model/guard/provider operation is admitted or performed by this
return. Original TASK `/root/delivery_manager/guard_implementation` returns to
DELIVERY `/root/delivery_manager`, under ROOT `/root`.

Continuation basis: coordination HEAD
`fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`; product basis remains
`3bddc2b05f6106e969c7cf43373b230845c7cc66`. Sealed uncommitted continuation brief
hash `e191e038879f9ae93a194d28d53b3170d33e088de96034c17c430928886dc7ff` and
independent REVIEW hash
`5b5ec41086242143cb24c14b6b0e30ad57fff04c001cd9e6fe1afb8cb25b7924` verified.
Root/project/TASK instruction hashes are unchanged from the original supplied
basis. Actual origins, hashes, parentage and commands are in `CONTEXT.json`.

## Exact changed-code scope

New `Run/tools/host_guard_v2.py` copies sealed v1 and changes only compilation
argv admission: one added pure `validate_compile_argv` helper and replacement
of `read_job`'s whole-argv token search with a call to that helper. The source
AST check confirms all other functions, classes and module-level statements
are identical. `host_guard_v1_to_v2.diff` is the complete source delta.
The original environment, executable/input hash, resource, provider, ownership,
control, logging, stop, latch and grant checks remain unchanged.

- **GR-01:** the helper parses Cargo's own segment before `--`, consuming option
  operands explicitly. Offline and locked flags must each occur there, along
  with exactly one jobs option whose value is exactly `1`. Workload/compiler
  arguments after `--` cannot supply those controls. All duplicate options,
  conflicting job values, malformed/missing operands, unknown controls and
  selected contradictory options refuse.
- **GR-02:** both cargo and rustc accept no explicit selector or one leading
  canonical `+1.97.1`. Other selectors, duplicates and ambiguous/misplaced
  selector-like controls refuse. This does not claim that argv proves a direct
  binary's version: executable hashes, isolated runtime identities and actual
  toolchain provenance remain separately required.

## Deliberately narrow grammar

Cargo subcommand immediately follows executable/optional selector and must be
`build`, `check`, `test`, `run` or `rustc`. Global flags placed before the
subcommand, Cargo aliases, --config/-Z and unknown options refuse. Supported
boolean/value options are the explicit small sets in the helper, not a claim of
full Cargo CLI compatibility. Separate `-j 1`, attached `-j1`, `--jobs 1` and
`--jobs=1` are equivalent admitted spellings; a second jobs option refuses even
if it also says 1. Duplicate option aliases normalize before comparison.
Value operands must be nonempty and not begin with `-` or `+`; use canonical
paths rather than ambiguous option-looking operands. `--offline=false` refuses.

Forwarding is supported only for Cargo `run`, `test` and `rustc`. Those trailing
arguments remain arguments of the program/test/compiler and are not interpreted
as Cargo controls or independently qualified workloads. A particular forwarded
command still needs its own complete reviewed grant; this grammar does not
promise the runtime behavior of arbitrary program arguments. Build/check
forwarding refuses. Rustc conservatively rejects any extra `+...` token; a
literal plus-prefixed filename can be written `./+filename.rs`.

Only exact `+1.97.1` is supported as an explicit selector; even a longer native
triple spelling is outside this narrow grammar and refuses. A real direct
compiler binary may reject the canonical proxy selector. No route or compiler
version is established from executable basename or these pure tests alone.

The future Cargo-rustc layout-IR command supplied by DELIVERY is one passing
syntax regression, including --manifest-path/--lib/--target and Cargo's own
--offline/--locked/-j 1 before the delimiter, then --cfg/--check-cfg/--emit/-C
arguments after it. No IR source, instrumentation, compiler call or runtime
claim was added here. ROOT retains the instrument review and compile grant.

## Verification and preservation

- **41 original behavioral tests pass against v2**, exit 0. The sealed original
  test module is loaded without byte edits and its `guard` global rebound to
  v2 in memory. Import and all tests retain the original live-capability fence.
- **70 additive tests pass**, exit 0: 67 exact argv cases (12 accepted valid
  forms, 55 refusals), plus original-review reproduction on unchanged v1,
  unchanged required environment validation and executable hash validation.
- The three bad argv examples from the independent review still reproduce as
  accepted on preserved v1 and are refused by v2. The valid reviewed build
  control passes v2. Exact inputs/outcomes are in `regression_inputs.json` and
  `regression_results.json`; no live toolchain was needed.
- **All 11 original v1/source/packet entries remain byte-identical**, including
  its original manifest. `PRESERVATION_BEFORE.json` and
  `PRESERVATION_AFTER.json` retain each hash and comparison. The old source,
  tests, logs, manifests, returns and context were not rewritten.

The source v2 SHA-256 is
`533a6f7506da4e031d8a824a27b4e9c496f374a3af8b7e98c72da55e8bbc26b5`.
`VALIDATION.json` lists exact source, harness, regression, test and log hashes;
`SHA256SUMS` seals this additive packet and v2 source, excluding itself.

Write scope was only `Run/tools/host_guard_v2.py` and this `continuation_01/**`
folder. No live provider/guard/signal/workload/compiler/model, network,
installation, setting change, Git/index mutation or delegation occurred.
Read-only repository-root/HEAD queries at entry were the only Git commands.
ROOT's separate read-only provider witness remains a different execution; it
was neither run nor interpreted here as a compile grant.

The original host/ABI/permissions/containment/latency/overshoot limitations,
K6/VR exclusion, separate DEC-025 qualification and protected criteria remain.
Return this exact candidate for independent GR-01/GR-02 backcheck. Compile
admission remains blocked pending that backcheck and relevant live qualification.
