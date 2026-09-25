# Decisive scientific JSON cases

These are prospective controls. `probe_numeric_domains.py` uses only Python standard-library Decimal/float/struct/json for independent domain examples; it does not implement production canonicalization or establish Rust/JS/WASM parity.

| Input/value | Scientific real under new profile | Exact-integer field under new text rule |
|---|---|---|
| `1e160` | Finite binary64; canonical exponent form `1e+160`; must not fail merely because its fractional part is zero | Reject exponent token and range |
| `100000000000000000000`, `1e20`, `1.0e20` | Same bits and canonical `100000000000000000000` across serde number variants | Reject |
| `9007199254740991` | Exactly representable | Accept if field bound permits |
| `9007199254740992` | Exactly representable real, canonical same digits | Reject safe-integer bound |
| `9007199254740993`, `9007199254740993.0`, `9.007199254740993e15` | All round to9007199254740992 and hash identically under declared real semantics | Reject before rounding |
| `18446744073709551615` | Rounds to18446744073709551616; canonical rendering must follow binary64, not preserve u64 digits | Reject |
| `1`, `1.0`, `1e0` | Same real value and canonical `1` | Only integer token`1` accepted |
| `1.0000000000000000001` | Rounds to1 | Reject fractional token; JS object Number1 can only authenticate actual received1, not this lost spelling |
| `0.1` | Accepted approximate binary64 real | Reject |
| `-0`, `-0.0`, `-0e3` | Reject new input before canonicalization; historical renderer still emits0 | Reject |
| `5e-324` / bitpattern0000000000000001 | Accept smallest positive subnormal | Reject |
| `1e-324` / `-1e-324` | Reject nonzero input underflow to zero | Reject |
| `1.7976931348623157e308` | Accept maximal finite binary64 | Reject |
| `1e309`, NaN, Infinity | Reject; never emit null | Reject |
| `"9007199254740993"` | String preserved; no automatic numeric conversion | Not an integer field |

Expected canonical spellings above are standards-derived targets, not observed new Rust outputs. Freeze actual golden results using the Rust authority and independently check ECMAScript/V8/native/Python transport. Include adjacent values around2^53, exponent formatting boundaries1e-6/1e-7 and1e20/1e21, maximal finite, smallest normal/subnormal, decimal midpoint ties and scientific lexemes just below/above underflow/overflow boundaries. Compare bits as well as canonical bytes. Fix a bounded seed/sample count for randomized parity rather than an open-ended benchmark.

Required negative controls:

1. Duplicate decoded names, including `{"a":1,"\u0061":2}` with an actual JSON Unicode escape in the second key, must fail before a map overwrites the first. Invalid trailing text and nested duplicates must fail too.
2. Lone high/low surrogates and noncharacters in keys, values and top-level strings fail. A valid supplementary character and a BMP key verify UTF-16 ordering; NFC/NFD spellings remain different strings. Escaping-equivalent valid strings produce identical semantic content.
3. A count changed from1 to`1.0000000000000000001` must fail raw integer admission even though ordinary float parsing returns1. Exponent spelling cannot bypass count bounds. Negative counts, booleans, strings and oversized integer host types fail their field contracts. Unknown/new numeric fields cannot silently become counters by naming convention.
4. Programmatic -0, NaN, Infinity, Decimal/Fraction/BigInt, accessors, symbols, undefined, sparse arrays, cycles and nonplain objects fail the strict adapter. Deliberately converted scientific integers use the explicit real-domain path. Record what a JS Number already is, not its unknowable earlier decimal source.
5. Computational -0 stays available in exact source-bit evidence; the successor public-zero projection produces +0 before row binding. Removing or applying that projection after signing must fail binding. All old negative-zero hashes remain unchanged.
6. A new raw1e160 model reaches the genuine producer, retains actual invocation/mode, and returns its real numerical verdict; it does not merely hash an inserted fixture. Repeat through native/headless, new semantic readers, save/reopen and exports. A current-method range refusal remains a truthful refusal after serialization succeeds.
7. New-profile payload with v1 checksum label, new source receipt under old source-blocks semantic ID, changed input mode/model, parsed DTO substituted for full invocation, forged public-zero projection, and unknown future profile all fail qualification. No fallback from v1 refusal to new profile.
8. Existing unrestricted large-integer rendering, checked_v1 unsafe-integral rejection, frozen raw/AnalysisRun/canonical/history hashes and all existing profile dispatch tests retain their original behavior. New success is stored under a new identity beside the original failure.

9. Scientific stress unit control: force binary64`1e-306`N / area binary64`596902.6041820607`m². Compare against exact rational division of those represented inputs. Direct Pa value`1.67531519044e-312` has relative error about6.64575e-13; dividing to binary64 MPa gives`1.675317e-318` with about1.269450175e-6 error. Preserve1e-9. New raw rows, maxima, canonical output and machine exports retain Pa; display MPa only through an explicit checked display path or show its limitation. A larger JSON range alone must not qualify the inaccurate MPa projection.

Scale qualification to the actual candidate; no protected numerical tolerance changes follow from admitting a wider finite input range. The scientific profile only establishes unambiguous transport and canonical semantic identity.
