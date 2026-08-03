# WORKING_ITEMS return — DEL-01-05 RF-002 locality repair

**RunID:** `PEC-DPEC77-78-20260802`  
**InstanceID:** `working-items-del0105-rf002`  
**DeliverableID:** `DEL-01-05`  
**Finding disposition implemented:** `RF-002 REVISE`  
**Result:** `COMPLETE — candidate repair; independent REVIEW rerun required`

## Bounded writes

Only the two authorized product files were changed:

| File | Pre-repair SHA-256 | Post-repair SHA-256 |
|---|---|---|
| `projects/pec/v2/tools/check_service_core_posture.py` | `59ced09020cb228b1e6ecf9c3c213287a03b2bcd3da822fddaa5b3cbe10ed112` | `3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643` |
| `projects/pec/v2/tests/enforcement/test_locality_assertion.py` | `2f670b723e8c5948f3ff2b074ae476a39963bcb9df3d38bd20581fb9e66e63f0` | `69051b4c127009c821886c4cc6aea70222f57c3ad51013bdebe53a6211d92d20` |

The only other writes were this instance's `RETURN.md` and `STATUS.json`.
No fixture path, evidence, manifest, decision, lifecycle, SOW, decomposition,
source-core, workflow, or foreign-loop surface was written. `RF-001` remains
reserved for the final manifest reseal after later evidence/review updates.

## Method repair

The locality checker now builds deterministic canonical bindings from
`ast.Import` and absolute `ast.ImportFrom` nodes, propagates callable/class and
instance aliases to a fixed point, and resolves call receivers through the
AST. It recognizes:

- aliased modules and imported symbols;
- aliases assigned from canonical network callables or `socket.socket`;
- assigned and re-aliased socket instances;
- aliased bound socket methods;
- inline `socket.socket().connect(...)` receivers; and
- unbound socket-class calls with the correct endpoint argument position.

Resolution begins only from import-derived bindings; arbitrary similarly
named locals are not assumed to be standard-library modules. Existing Unix,
loopback, endpoint-configuration, and OI-009-independent classification is
preserved.

## Owner-bound regression evidence

Each exact source was embedded in the existing test module, materialized only
under a temporary directory, hashed before evaluation, and produced an
`EXTERNAL_NETWORK_CALL` finding at `core/app.py:2`:

| Source SHA-256 | Overall | Locality | Located endpoint |
|---|---|---|---|
| `303b635b082646ef9b62979f779960a5a513ed8d9cafb489a431af9742095eaa` | BLOCK | BLOCK | `198.51.100.10` |
| `ad74e807c6ffcb555cc84fe342bb131717423ad4bb3ec4f1c510564ae0627d4a` | BLOCK | BLOCK | `198.51.100.10` |
| `5c765f1daa1b8989dabf39c54658625a0f107aebbc5808847b49ad8f7b68de4a` | BLOCK | BLOCK | `https://example.invalid` |

## Novel producer probes

Fresh sources distinct from the three review cases produced:

| Probe | Expected/result |
|---|---|
| `from http import client as hc`; assigned `HTTPConnection` factory alias; external keyword `host` | BLOCK, located at line 3 |
| aliased `socket` module; assigned socket-class, instance, and bound-method aliases; external tuple | BLOCK, located at line 5 |
| imported socket-class plus instance alias; Unix-domain literal | PASS, no locality finding |
| aliased module plus inline socket constructor; IPv6 loopback literal | PASS, no locality finding |

## Verification

- Locality module: **9/9 PASS**.
- Entire enforcement suite: **19/19 PASS**.
- Live posture check: overall **PASS**; dependency/locality/registration all
  **PASS**; zero findings; `PEC_RELEASE_BLOCKING` retained.
- Live bound hashes: config
  `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed`,
  core tree
  `2c830d1fe9bc7f550c47d5f22223f330a3a95118360e61bb6d9c785b47c151ca`,
  workflow
  `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b`.
- `git diff --check`: **PASS**.

## Remaining gates

DEL-01-05 remains `INITIALIZED` under the standing `HOLD`. This return accepts
no artifact and satisfies no AC. The independent formal REVIEW must rerun
against the revised candidate with fresh novel-form probes. After every other
revision and evidence update lands, `RF-001` requires the D-PEC-77 manifest to
be repaired and resealed as the final act.
