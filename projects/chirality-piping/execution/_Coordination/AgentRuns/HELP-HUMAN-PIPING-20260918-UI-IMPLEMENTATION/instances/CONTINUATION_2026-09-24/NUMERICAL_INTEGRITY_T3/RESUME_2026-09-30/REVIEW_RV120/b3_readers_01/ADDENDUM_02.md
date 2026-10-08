# RV120 (RV-R2) ADDENDUM_02: (A) the B3a drop, readers' side — CONFIRMED; (B) repair 02 — clean, verdict held for repair 03

TASK (Type 2), RV120. Requested by WORKING_ITEMS for T3 (Agent 1), my return path. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **(A):** `b2` `0ef9a8ace9`, I113's one commit on `51f339a11e`. Record `R/I113/b3a_drop_01/RETURN.md` (`a2847713…`; SHA256SUMS 83 of 83).
- **(B), repair 02:** RS `b2-r` `7873884fb4`, TS `b2-t` `d933514312`, PY `b2-p` `101ebcff76`. Record `R/I101/b3_readers_01/REPAIR_02.md` (`00254505…`; SHA256SUMS.repair_02 verified).
- **Basis of the B3a drop:** RR's U3 rulings, as relayed (B3a dropped, B3D-10's tightenings kept).
- **What `51f339a11e` carries:** it merges my confirmed lanes (`65c04cd0c7` and `6d3d4cdca6`) and lane A's merge `583fc758ee`. Its nine reader sources are byte-equal to my confirmed heads, and RE, the desktop app and the schemas are unchanged from `65c04cd0c7`. So my ADDENDUM_01 runs serve as the RE, vitest and census baseline. PY's seven files were rerun at `51f339a11e` (copy `m0`).
- **Candidate under test, `m1`:** the dry-merge equivalent. It is `git archive` of `0ef9a8ace9` with repair 02 applied by `patch`: `65c04cd0c7..d933514312` (RS transport check plus RS and TS tests) and `6d3d4cdca6..101ebcff76` (PY tests and fixture), both clean with offsets. In `m1`, `physics_evidence.rs` equals `d933514312`'s and the fixture equals `101ebcff76`'s. The diffs are in `addendum_02/harness/`.
- **Scope:** the readers only. The B3a drop's producer side (`core/product_physics`, 6 files) is not reviewed here.

## (A) The B3a drop, readers' side — CONFIRMED

- **Code:** the three readers' `legacy_namespace` are now one predicate, model 0.1.0 or 0.2.0 with `pressure_contract` absent or JSON null, and anything else is G8 `INVOCATION_MISMATCH`. They are RS `retained_precision.rs` `legacy_namespace`, PY `_legacy_namespace` (`LEGACY_PRESSURE_CONTRACT` removed) and TS `legacyNamespace`. They stay type-strict (B3D-10 and N-4 kept). The exact route is unchanged.
- **Tests:** RS, TS and PY pin one 29-entry table entry for entry. The five "L3 on …" entries and the two N-11 entries now read INV. In PY, m3l is a refusal witness.
- **What moved since ADDENDUM_01:** I compared 6,039 readings; 34 moved, on 12 inputs. All are intended and identical in all three readers:
  - **3 of my probes** (0.3.0 with the legacy contract; the same with keys reordered; the same with `pressure_regions` `[]`): eligible → G8 `INVOCATION_MISMATCH`.
  - **I100's 8 m3l shapes:** both m3l must-pass bases go from eligible to INV. The 6 load-refusal shapes go from G8 `PREPARATION_MISMATCH` to INV: they are refused at the namespace, before any load is read.
  - **1:** N2's RS transport code, now deterministic (below).
  - The unbound and transport readings of every L3 shape are unchanged, because G8 does not run there.

## (B) Repair 02 — clean; verdict held for repair 03, as asked

- **Code:** RS `physics_evidence.rs` `validate_transport_metadata` now iterates the cases, materials, sections, extrema and region members in array order. Its maps and sets serve only duplicate detection and lookups, and `assembly` was already array-ordered.
- **Determinism:** on N2's probe the RS transport code is `SOURCE_PHYSICS_TRANSPORT_MAXIMUM_RESULT` in 5 of 5 fresh processes, on both bases. Before the repair it alternated.
- **Pins:** the N2 probe is pinned in all three readers; RS's pin runs 64 times and its digests match my index. F1's four probes are now pinned in RS and TS as well (175 shapes). I101 reports N2H killed (one of its 64 runs read the other code).
- **Open:** N2b, the same hash-order dependence in RS's `validate_physics_evidence` (raw reads), which I101 traced. It goes to repair 03 together with the class inventory. My verdict on (B) waits for those heads.

## Counts

- **Three-reader agreement** at `m1`, on identical bytes:
  - my 128 probes and 4 forgeries: 0 differences outside G7. The only missed expectations are the 3 B3a admissions above, now INV in all three.
  - I101's 175 shapes, I100's 52 and I100's 318: 0 differences outside G7.
- **Census:** 0 changes and 0 misses against the base census, in RS, TS and PY, for 07m (339 entries) and 07n (638).
- **Suites, test by test:**
  - **RE:** 208 → **212**. That is +1 N2 pin and +3 of my no-op harness tests, so 207 without them.
  - **vitest:** 3,680 → **3,684**. That is +1 N2 pin, the shape pin's title renamed from 169 to 175 shapes, and +3 harness tests, so 3,679 without them.
  - **tsc:** rc 0.
  - **PY's seven files** at `51f339a11e` vs `m1`: 1,704 → **1,736**. Added: 34 (the 29-entry table and its count test, 2 m3l-refused tests and 2 N2 pins). Removed: 2 (m3l-admitted, replaced by m3l-refused).
  - No outcome was changed or failed.

## Findings

| # | Status | Line |
|---|---|---|
| A | **Confirmed** | The B3a drop is correct and identical in all three readers. The moves are exactly the L3 and m3l shapes, refused at G8's namespace |
| N2 | **Closed for the transport check** | RS's transport code is array-ordered and stable (5 of 5), and pinned in all three readers |
| F1 | Pin completed | The order probe is now pinned in RS and TS too |
| N2b | **Open, routed to repair 03** | `validate_physics_evidence` iterates hashed collections. (B)'s verdict is held |

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` (target `WT/targets/rv120b3-m1`).
  - Every other heavy job went through `WT/tools/t3_slot.sh`, one heavy job of mine at a time.
  - My jobs queued for about 90 minutes behind another session's exclusive DEC-025 job (20:23–21:52Z).
  - No Git writes, no DEC-025, no installs and no measurements. The dry-merge equivalent was built by `patch` in my archive copy; no Git object was written.
- **Disclosed:** I stopped one duplicate waiter of my own.
- **Record:** `addendum_02/host/job_stamps.txt`. Placeholders as before.
