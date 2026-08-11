# Sealed N1 no-shell packet-author brief

- RequestedBy: WORKING_ITEMS
- RunID: `APPDEV_DAPP93_TWELFTH_PACKET_AUTHORING_2026-08-10`
- ParentInstanceID: twelfth-lineage WORKING_ITEMS
- ChildInstanceID: `N1-TWELFTH-FRESH-AUTHOR`
- PackageID: D-APP-93 packet preparation
- Objective: fill the six pre-materialized packet stubs and return a disk-consistent self-census and terminal return
- AcceptedBasis: M0 validation in `validation/M0_PRE_DISPATCH.md`
- Dependencies: M0 accepted only
- Exclusions: every historical root; Git; network; shell; command execution; file creation/deletion/rename; product/runtime/system state; packet execution; verifier work; receipt work; any thirteenth lineage
- DeclaredReads: the complete hash-pinned capsule and six SPEC contents embedded verbatim in the dispatch message
- AllowedTools: `apply_patch` only
- AllowedWriteTargets: exactly the eight paths in `allowlists/N1_WRITE_TARGETS.txt`
- ExpectedOutputs: six filled packet files, `returns/N1_SELF_CENSUS.md`, `returns/N1_TERMINAL_RETURN.md`
- AcceptanceCriteria: exact sentinel replacement; no sentinel remains; all SPEC hashes unchanged; nonempty files; census equals disk; full-pattern per-stub scan has zero hits; five-component content contract complete; no execution claim
- Escalation: any inability to replace an exact sentinel or satisfy a SPEC returns BLOCK without improvisation

Pacing: runbook 8 minutes; scripts 8; evidence/citation 6; approval/census/return 6; total 28 minutes. The first checkpoint is at 10 minutes. Later checkpoints are 10 minutes apart. Durable filled-stub count and byte growth define progress. Native context occupancy is unavailable.

The child receives no path outside the eight write targets and no prior-lineage content. The dispatch message contains the capsule and SPEC text in full, so no rule is circularly hidden behind a prohibited read.

Sealed input identities:

- capsule: `a39cca483c803ee9928cc0372214abbf84143f0e9dd253bdf411868c8c2c88aa`
- N1 read allowlist: `c9c99ed9c05d48add940b1004d723212e7151938921d36371b1eb2a4c404f059`
- N1 write targets: `028f4223275b7c33edffda3667832b116c0dc74185a5b0f0825073b52383730b`
- SPEC identity manifest: content rows in `specs/SPEC_IDENTITIES.sha256`
- work graph: `7da865d7f8dbfc344fd2b1f9e37a76d25af245fc6e3155284ca3a5416081ca75`

Initial output identities are recorded in `validation/M0_PRE_DISPATCH.md`; each is a one-line sentinel and must change by exact replacement.
