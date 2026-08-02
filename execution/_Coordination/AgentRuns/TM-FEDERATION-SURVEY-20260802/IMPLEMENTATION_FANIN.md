# Implementation Fan-In — HELPS_HUMANS

RunID: `TM-FEDERATION-SURVEY-20260802`
Node: `A2-IMPLEMENT`
Disposition: `ACCEPTED WITH MANAGER CORRECTION`
Date: 2026-08-02

## Accepted child return

`instances/A2-IMPLEMENT-R2/RETURN.md` returned `SUCCESS` with writes confined
to the two authorized tool/test files plus its managed records. Its initial
focused evidence was 29 passing tests, Root `COMPLETE` with 48/48 findings
presented, App `COMPLETE` with 48 complete/24 presented findings, and all four
register hashes unchanged.

The child consumed `INVENTORY_FANIN.md`; its sealed status retained the
original graph label `A2-INVENTORY-R2`, whose child run was interrupted. The
manager fan-in record is the accepted substitute dependency and is the basis
actually named by the launch brief.

## Manager inspection and correction

HELPS_HUMANS inspected the implementation rather than accepting the return by
assertion. One bounded context-labeling defect was found: in a non-Root
invocation's complete JSON, a resolved link between two foreign registers was
labeled `LOCAL_LINK_TO_FOREIGN`, although neither endpoint belonged to the
invoking loop. The presented subset filtered the row, so user-facing App
output was unaffected, but the complete evidence graph's class was inaccurate.

Manager correction:

- emit `INBOUND_ELEVATION` only when a foreign row targets the invoking
  namespace;
- emit `OUTBOUND_AWAITING_ACK` only for an invoking-register source row;
- emit `FOREIGN_LINK_TO_LOCAL` only when the target is the invoking register;
- emit `LOCAL_LINK_TO_FOREIGN` only when the source is the invoking register;
- add a regression fixture proving unrelated foreign relationships receive no
  invoking-relative directional label; and
- correct the module documentation from two to three subcommands.

A second manager safety inspection found that explicit `--out` could name or
resolve through a symlink to a canonical `REGISTER.csv`. Because the original
hash proof was assembled before output write, that target could have been
overwritten after the proof. The integrated correction fails operationally
before writing whenever the resolved output aliases any discovered canonical
register or any register-shaped surface. Direct-path and symlink regression
fixtures prove the register bytes remain unchanged.

Fresh verification then identified a same-namespace elevation edge case:
`OUTBOUND_AWAITING_ACK` was gated on cross-namespace targeting even though the
frozen contract applies it to every invoking-loop `ELEVATED` row whose exact
target is absent. The integrated correction keeps the cross-namespace
condition only for `SourceRef` and adds a same-namespace missing-target
regression.

The global graph still retains program-level orphan, duplicate, ambiguity,
notice, validation, and closure observations. Only the invoking-relative
directional labels were narrowed.

## Reproduced evidence after correction

- `python3 -m pytest tools/taskmgmt/test_taskmgmt.py -q` — PASS, 33 tests.
- `python3 -m py_compile tools/taskmgmt/taskmgmt.py tools/taskmgmt/test_taskmgmt.py`
  — PASS.
- `git diff --check -- tools/taskmgmt/taskmgmt.py tools/taskmgmt/test_taskmgmt.py`
  — PASS.
- Root live survey — `COMPLETE`, four registers, 48 findings, 48 presented,
  47 `FOREIGN_LINK_TO_LOCAL`, one `REMOTE_CLOSED_LOCAL_OPEN`, zero writes.
- App live survey — `COMPLETE`, four registers, 25 complete findings, 24
  presented, 24 `LOCAL_LINK_TO_FOREIGN`, one unrelated program closure echo,
  zero writes.
- All four post-survey SHA-256 values exactly match `BASELINE.md`.

## Fan-in conclusion

The tool/test implementation is accepted for fresh adversarial verification.
No H1 expansion is required. This fan-in is structural and behavioral
acceptance by the component manager, not publication or semantic approval.
