# WORKING_ITEMS launch brief — DEL-01-05 RF-002 locality repair

RequestedBy: HELP_HUMAN
RunID: PEC-DPEC77-78-20260802
InstanceID: working-items-del0105-rf002
PackageID: PKG-01
DeliverableID: DEL-01-05

## Owner disposition and authority

Ryan Tufts, in-session, 2026-08-03:

> RF-002: REVISE — repair the locality checker's detection method itself:
> replace exact-spelling matching with import-binding/AST-based resolution so
> aliased and inline standard-library egress forms are detected generally; add
> the three evidenced scratch forms (SHA-256 303b635b…, ad74e807…,
> 5c765f1d…) as blocking regression fixtures. Bounded WORKING_ITEMS authority
> within the D-PEC-77 §3.2 path fence only. Rerun the independent review
> against the revised candidate, including fresh novel-form probes.
> DEL-01-05 remains INITIALIZED under the standing HOLD.

RF-001 is separately `REVISE`; its manifest reseal is reserved as the final
act after every other revision and evidence update lands. Do not edit the
D-PEC-77 manifest in this lane.

## Objective

Repair the locality assertion's method, not merely the three examples. Replace
exact local spelling assumptions with deterministic import-binding and
AST-based call resolution that recognizes canonical standard-library egress
operations through aliases, imported symbols, assigned socket instances, and
inline socket constructors while preserving Unix-domain and loopback-only
classification.

The exact regression sources are:

```python
import socket as s
s.create_connection(("198.51.100.10",443))
```

SHA-256 `303b635b082646ef9b62979f779960a5a513ed8d9cafb489a431af9742095eaa`.

```python
import socket
socket.socket().connect(("198.51.100.10",443))
```

SHA-256 `ad74e807c6ffcb555cc84fe342bb131717423ad4bb3ec4f1c510564ae0627d4a`.

```python
import urllib.request as req
req.urlopen("https://example.invalid")
```

SHA-256 `5c765f1daa1b8989dabf39c54658625a0f107aebbc5808847b49ad8f7b68de4a`.

Because D-PEC-77 §3.2 enumerates exact fixture paths, encode these exact-source
regression fixtures inside the already authorized
`test_locality_assertion.py` and materialize them only in temporary test
directories. Create no new repository fixture path.

## Allowed writes

Only:

- `projects/pec/v2/tools/check_service_core_posture.py`;
- `projects/pec/v2/tests/enforcement/test_locality_assertion.py`;
- this instance's `RETURN.md` and `STATUS.json`.

Do not edit other tests or fixtures, candidate configuration, posture note,
workflow, activation/registered evidence, execution handoff, manifest,
decision/register/receipt, lifecycle, SOW, decomposition, Task Management,
source core, or foreign-loop surfaces.

## Required verification and return

1. Prove the three exact regression sources hash to the owner-cited values and
   each returns overall/locality BLOCK with a located finding.
2. Add method-focused tests for import bindings and inline receiver
   resolution; preserve existing external, Unix-domain, loopback, and OI-009
   tests.
3. Run the entire enforcement suite and live posture check.
4. Run independent producer-side novel forms not identical to the three
   review cases, including at least a `http.client` alias and a socket-class or
   socket-instance alias form.
5. Prove no false block for Unix-domain and loopback-only forms.
6. Prove exact two-file product-write containment and `git diff --check`.

Return exact pre/post hashes, algorithms changed, regression and novel-probe
outcomes, all test counts, and remaining gates. Candidate work only; do not
change lifecycle or claim AC/artifact acceptance.
