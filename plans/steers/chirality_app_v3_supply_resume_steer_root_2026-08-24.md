# ROOT LOOP STEER — v3 supply resumption: equivalence check and amended signature gate — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (DEL-02-08 lane). Authorizing ruling: R13
> (`chirality_app_v3_root_ruling_record_r13_2026-08-24.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together). This
> steer amends and resumes the supply-pinning steer
> (`plans/steers/chirality_app_v3_supply_pinning_steer_root_2026-08-24.md`,
> SHA-256
> `1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`),
> which remains the contract except as amended here. Read both in full
> before any write.

## Basis gate (in addition to the original steer's basis gate)

1. Work on a fresh branch `codex/root-supply-resume-2026-08-<DD>` from
   current `origin/main`. Record the exact basis commit.
2. Verify R12 and the original supply steer at the SHA-256 values R13 cites,
   and incorporate this steer and R13 by immutable path and SHA-256 from the
   PR that published them.
3. Confirm the prior run left no residue: no quarantine contents, no
   `ROOT_SUPPLY_PINNING_*` additions on any branch, and the receipts ledger
   still ends at Receipt 128.
4. If any check fails, stop and report.

## Amendments to the original steer

1. **N2 signature gate.** A strict-codesign failure on digest-exact bytes
   matching the documented defect class — Team ID `2DC432GLL2`,
   `invalid signature (code or signature have been modified)`, invalid
   entitlements blob, `spctl` failure — is recorded as supply inventory with
   citation to `openai/codex#37725` and does not stop the tranche. Every
   other signature, identity, version, or license disagreement remains
   fail-closed.
2. **N2b (new) — equivalence check before any execution.** Under the R12-A
   download terms, additionally download, digest-verify, and extract in
   quarantine:
   - `codex-app-server-aarch64-apple-darwin.zst` — size `50359498`, SHA-256
     `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677`;
   - `codex-app-server-package-aarch64-apple-darwin.tar.gz` — size
     `93775517`, SHA-256
     `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2`.
   Compare each contained arm64 app-server Mach-O byte-for-byte against
   `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2` and
   record equality plus each packaging's own signature-verification result.
   If any contained app-server binary differs from that identity, stop and
   report. Ancillary files in the package variant (launchers, licenses,
   notices) are inventoried, not executed.
3. **N3.** Proceeds only after N2 (re-verified on the re-downloaded primary
   asset) and N2b complete clean under the amended gate. Containment terms
   are unchanged from the original steer. If macOS refuses to execute the
   binary, stop and report — that outcome is compliant.
4. **N4.** The supply-unit candidate additionally records, as a named open
   finding for the preparation lane, the R13-B G5 implication: the plan
   fails G5 on an invalid nested signature, and the 0.149.0 app-server
   vendor signature is invalid as published (`openai/codex#37725`); G5
   planning requires either a corrected upstream artifact or a later owner
   ruling.

Everything else in the original steer — write set, quarantine discipline,
validators, Receipt 129, run evidence location (use
`ROOT_SUPPLY_PINNING_2026-08-<DD>/` for this resumed run), PR-without-merge,
sync rule, rollback, and discipline — applies unchanged. The prior stop
consumed no receipt number; this resumed run closes Receipt 129.

## Rollback note

The original steer's rollback rule extends to the two additional assets:
any failure deletes all quarantine contents (all three assets), tears down
disposable state, reverts branch additions, and stops with a report.
