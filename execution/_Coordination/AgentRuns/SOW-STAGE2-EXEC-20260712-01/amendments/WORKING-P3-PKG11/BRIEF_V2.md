# WORKING-P3-PKG11 Brief Amendment v2 — Stale Manifest Binding Repair

Disposition: `NON-CONSEQUENTIAL OWNED-EVIDENCE REPAIR`
Parent: `HELP_HUMAN`
Basis: `main@4d153302c3c4cd42578936db160c2bac1270225a`

Direct RECON-P3 found that the accepted PKG-11 author manifest still binds
`children/AUTHOR-B1/__pycache__/finalize_author_pkg11.cpython-313.pyc`, although
the package manager intentionally removed that generated residue before its
final package freeze. The absent ignored file is not candidate, project,
source, control, lifecycle, dependency, or semantic evidence. The defect is a
stale row in package-owned derivative evidence.

Resume the same `WORKING-P3-PKG11` manager. Preserve its prior PASS return,
attempts, manifests, and RECON notice. Within existing package evidence scope:

1. audit every AUTHOR-B1 and VERIFY-B1 manifest row for existence,
   containment, byte count, hash, uniqueness, self-exclusion, and ignored
   generated residue;
2. remove stale ignored-residue bindings without recreating the residue;
3. rebuild the affected child manifest(s), acceptance binding(s), package
   manifest, status/return/handoff citations, and any aggregate digest;
4. rerun all package fan-in, candidate immutability, project non-write,
   replacement/inverse/simulation, focused-check, and manifest-validation
   gates;
5. return `PASS_REBOUND` with old/new hashes and exact changed evidence paths.

Do not alter candidate or live project bytes, accepted semantic evidence,
member counts, mappings, source-line coverage, acceptance criteria, authority,
or any lifecycle/dependency/Git/release/reliance/rollback/retirement/H2 state.
This amendment authorizes no new author or verifier instance. Any additional
upstream defect reported by RECON must be included if it is within the same
owned mechanical binding class; otherwise return it to HELP_HUMAN.
