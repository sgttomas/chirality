# Comparative Measurements

State: `DERIVATIVE STATIC PROOF — NOT IMPLEMENTATION EFFORT`

These measures compare the frozen maps. They do not report actual migrated
code, build duration, package size, or runtime performance because no product
prototype or build was authorized.

## Definitions

### Target leakage (`TL`) and exposure (`TA`)

`TL = count(unique target-aware source files outside the variant allowlist)`.
Every variant must achieve `TL=0`. `TA` separately counts allowlisted shared
files that remain target-aware, so a design cannot hide exposure merely by
declaring a larger allowlist. The present tree has zero exact matches for
`CHIRALITY_PRODUCT_TARGET`, `productProfile`, `product_profile`,
`targetProfile`, or `target_profile`; that proves only that no current target
contract exists.

### Duplicate composition (`DC`)

`DC = count(target-owned route/shell files whose normalized component/import
tree is equivalent across both targets)`. Thin wrappers count only when their
bodies are equivalent. The current one-target baseline is zero. A/C intend
zero through one shared shell. B's naive fork risk set is 11 exact current
route/full-shell composition files; a valid extraction must also return zero
by retaining equivalent bodies in shared packages.

### Build matrix (`BM`)

One target-specific cell is one required logical stage: TypeScript/source
contract, renderer production build, Electron compile/package, or packaged
launch/smoke. Therefore `BM = 2 targets × 4 stages = 8` for every variant.
Common and architecture-specific checks are additional and cannot replace a
target cell.

### Migration-cost vector and index

Use `(E,N,Pkg,DeltaBM)`, where `E` is the existing lower-bound seam set, `N`
is new conceptual schema/profile/config nodes, `Pkg` is new package roots, and
`DeltaBM=4` is the target-specific build-cell increase from today's one-target
four-cell baseline. For transparent structural sorting only:

`MCI = E + N + 3*Pkg + DeltaBM`.

The package factor represents a manifest, public boundary, and independent
consumer validation; it is not an hours estimate. `U` is the exact additional
surface contributed by the held first-domain delta.

## Results

| Variant | TL target | TA design target | DC intended / risk set | BM | `(E,N,Pkg,DeltaBM)` | MCI lower bound |
|---|---:|---|---|---:|---|---:|
| A — light skin | 0 | measured within ruled profile boundary; lower-bound audit `P=9` | `0 / 0` | 8 | `(9,5,0,4)` | `18 + U` |
| B — shared core + shells | 0 | `0` in shared packages | `0 / 11` naive-fork sites | 8 | `(20,4,3,4)` | `37 + U` |
| C — build profiles + slots | 0 | one generated shared binding; adapters target-owned | `0 / 0` | 8 | `(9,9,0,4)` | `22 + U` |

## Reproduction and traceability

- `E=9` for A/C is the product/profile seam set `P`. B adds an 11-file
  route/full-shell composition set `R`, so `E=20`.
- B's broader extraction-review population is the sum
  `9+23+4+1+1+6+8+6+1+2=61`, reproduced with immediate-directory `find`
  counts recorded in `ARCHITECTURE_DEPENDENCY_MAPS.md`; it is not the lower-
  bound `E` value and does not claim that all 61 files move.
- `N` is enumerated as A: schema + two profiles + two packaging overrides;
  B: workspace/config change + three roots; C: schema + two manifests +
  generated binding + slot contract + two adapters + two packaging overrides.
- A additionally requires a conditional-spread check; B requires shared-to-
  target edge and cross-shell common-behavior checks; C requires manifest and
  adapter import/resource exclusion checks.

## Interpretation limits

- Lower numbers are not automatically better. A's smaller structural index
  may trade against greater future target-awareness exposure.
- The measures are projected from exact maps, not observed build telemetry.
- The held first-domain delta prevents measuring slot occupancy, adapter size,
  domain-only route count, or actual shell divergence. Therefore the measures
  cannot select A, B, or C in this run.
