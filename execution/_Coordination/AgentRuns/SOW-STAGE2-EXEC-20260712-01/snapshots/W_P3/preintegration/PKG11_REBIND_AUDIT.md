# PKG-11 Rebind Audit

Verdict: `PASS_REBOUND`.

RECON attempt 1 found two stale ignored `.pyc` bindings. Under `BRIEF_V2.md`, the owning manager removed only those two absent-residue rows, retained their exact old hashes in `REBINDING_V2.md`, and rebuilt all transitive bindings. The active author manifest contains 972 valid self-excluding rows at SHA-256 `a943cc42d4e5090a10bc03e1a3b80f90f924d329442051f7f4f597499b3a673d`; the verifier remains unchanged at 493 rows; the rebuilt package manifest contains 1,530 valid rows at SHA-256 `4dc1714c70c38fe4469af9e4d680f3f32a8d050f7d3c53c20ebafeff97608ee7`. Fresh RECON attempt 3 rehashed and validated the rebound state before reconstructing all members.
