# Values required to instantiate the composed source envelopes

The three source compositions are complete as parameterized sums. The
following are values or validation conditions, not unexplained heap terms.
FORMULAS.json gives their dependencies; SOURCE_ENVELOPES.md defines each
operator and allocation owner.

| Binding | Required exact record / substitution | Present status |
|---|---|---|
| Source/library identity | FK/H/VR/SD full source hashes, Rust library hashes, serde lock/features/archive identity, formula/script hash | Pinned in INPUTS and inherited sealed parent evidence; no compiled feature/layout claim |
| argv | Ordered strings, UTF-8 byte lengths, argc including executable, retained Args subset; command hash | Future admitted command must supply; source sum is E(argc,OsString)+sum bytes |
| paths | Input/output/archive path byte lengths, actual PathBuf join identities | Future run-specific values; durable records use aliases, not fabricated local paths |
| exact input files | SHA256, byte length F, stable file/metadata length during read | Family/expected-unresolved/committed H records available; large-model bytes still pending. Exact branch requires metadata=F, otherwise use the stated H-hint fallback |
| JSON descriptor | Array lengths, object key counts, key/string payload totals and longest decoded string; typed Case/Model field counts and string lengths | Compact histograms for 24 family records and expected-unresolved retained. RF large-model shape has the explicit source-schema template; actual byte/hash verification still required |
| H canonical model descriptor | N,m,l,restrained-node count, model/id/source/label byte totals, file F/hash | Parent finite-fixture bindings available; file-mode formula also accepts conservative payload≤F terms |
| runtime entry B0 | Requested allocator-live baseline at observation entry, with candidate/start boundary and metric named | Not measured here. Includes pre-entry runtime owners only; stdout/path/parser/output additions are separately derived. It is not spare heap used to cover omissions |
| sparse storage | n,f,m,z,zf,d_v,d_a,t_e,trow and numerical-zero skyline s64 | n/f/m and structural degrees from parent. For RF, z=36N+72m; zf=sum_a(d_a+1); t_e multiplicities are36 entries of degree(v) per node plus72m entries of multiplicity1; trow≤12max degree. Use s64≤f(f+1)/2 until a tighter candidate-bound count is supplied; never allocate a dense matrix to evaluate that expression |
| real layouts | All σ/α parameters, including consumer/helper/tree/error types below | Await separately scoped L1/consumer witness; no guessed mirror sizes |
| domain/runtime contracts | Original finite fixture/command/schema inputs, unique JSON keys, normal pinned stdlib/libc contracts, disabled mutation/arbitrary-precision/preserve-order features as specified | Source premises, to be rechecked with final candidate/runtime identity. Any changed premise reopens affected rows |

The RF multiplicity identity gives `sum_e t_e=144m` and
`sum_e(2t_e+1)=288m+z`, so the sparse expansion/report child sums need no
unknown numerical stiffness value. The numerical graph used by SD can be a
subgraph of the structural graph; its degree is bounded by d_a, but its RCM
skyline is not assumed equal to K4's ordering. This distinction is preserved.

Additional layout values made concrete by this finish, beyond the previously
listed K0 cells:

- std::ffi::OsString; the actual allocated `io::error::Custom` and StringError
  wrapper requests for the formatter-error path.
- H PrecisionWork, `(u64,u64)` digest tuple and borrowed string slice slots.
- FK FrameNode, `(usize,usize,Matrix12)`, structural::StiffnessContribution,
  structural::PivotEvidence, structural::ResidualRow, structural::ContributionRounding.
  These ordinary binary64 report types are distinct from retained Wide row types.
- SD SymmetricMatrixEntry; `(usize,usize)`, `(usize,f64,f64)`, `(usize,f64)`
  tuples and their Vec-header/primitive layout facts.
- Actual leaf/internal nodes for `BTreeMap<(usize,usize),(f64,usize)>` and
  `BTreeSet<usize>`, plus the already pending JSON/Case/Model/map layouts.

No witness code, overlay, build or invocation is supplied or activated by
this ledger. ROOT selects the exact added witness scope. Private layouts,
input values, independent checking, integration into the final full-phase
formula and final A1 impact remain separate from source-composition closure.
