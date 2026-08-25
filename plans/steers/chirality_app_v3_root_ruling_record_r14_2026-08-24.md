# ROOT RULING RECORD R14 — supply-tranche egress-inventory amendment and ancillary-executable grant — owner ruling of 2026-08-24

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: disposition of the second compliant supply-tranche stop (N3 egress attempt) and authorization to resume with an amended containment rule and a bounded ancillary-executable grant. Target workspace: Root loop under its own instruments. Companion instrument: the second resume steer (`chirality_app_v3_supply_resume2_steer_root_2026-08-24.md`; SHA-256 recorded in the PR that published this record — the files merged together). Prior instruments, all remaining in force except as amended: R12 (`2ee282fc1330c466e17ce2791cb7cb8c66f2a7e13f455c2ab1750c42719321fd`), the supply-pinning steer (`1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`), R13 (`0ba74959dac38f49f81f6ba8aff4020df520fd418bed2a3aa6617b19f3aa4960`), and the first resume steer (`248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session minder chat on
2026-08-24. "[click]" marks the option the owner selected.

## The stop, and what it established

The resumed tranche passed N2b — both alternate packagings digest-exact,
both embedded app-server binaries byte-identical to
`b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`, all
signatures matching only the R13-admitted defect class — then stopped
compliantly in N3 when the executing binary's startup attempted
curated-plugin synchronization to `https://api.github.com/repos/openai/plugins`
and the OS sandbox denied it. The original steer made any attempted egress a
stop condition, and the loop honored it without loosening containment.

The preserved evidence additionally establishes: the kernel admits the
binary despite the vendor-signature defect; it identifies as exactly
`codex-app-server 0.149.0`; the egress attempt occurred with
`check_for_update_on_startup = false`, `web_search = "disabled"`, and
analytics/feedback disabled, so none of those switches governs the plugin
sync; remote-control startup reached an unauthenticated waiting state with
no credential prompt, login flow, or `auth.json`; all writes stayed inside
the disposable tree; and the dedicated app-server binary exposes no
schema-generation subcommand, so schema/types evidence requires ancillary
executables from the pinned package variant. Rollback and teardown were
verified; main is untouched and the ledger still ends at Receipt 128.

R14-A — Egress-inventory amendment: [click] "Authorize".
  The containment rule is amended: an egress **attempt that the OS sandbox
  denies** is recorded inventory, not a stop. For every such attempt the
  evidence must record the full trace, the exact destination, and the
  triggering operation, and every attempted destination must be carried into
  the OUT-002 endpoint-enumeration policy and the N4 G2 candidate.
  `https://api.github.com/repos/openai/plugins` is admitted as an observed
  destination of this artifact. Any egress the sandbox **fails to deny** —
  any completed connection — remains an immediate fail-closed stop, as do
  credential prompts and writes outside the disposable tree. The tranche
  must additionally probe for the exact 0.149.0 configuration switch, if
  any, that governs curated-plugin synchronization, and record its exact
  name, default, and readback — or record that no such switch exists.

R14-B — Bounded ancillary-executable grant: [click] "Authorize".
  Solely to produce the missing schema/types and readback evidence, the
  tranche may execute ancillary executables **contained within the three
  already-pinned, digest-verified 0.149.0 assets** — nothing downloaded or
  obtained from anywhere else — under the identical containment terms, with
  each executed file's SHA-256 recorded before execution. If the evidence
  still cannot be produced from those files, the gap is recorded as
  `UNAVAILABLE_UNDER_BOUNDS` and the candidate returns with it documented;
  the owner rules at G2 with the gap in view.

## Boundary of this authorization

Everything previously withheld remains withheld: no pin amendment, no G2
acceptance, no implementation, cutover, release, publication, or reliance
authority, and no blocker lift. The amended egress rule admits only
sandbox-denied attempts as inventory; containment is otherwise unchanged.
The R13-B G5 finding requirement stands. TM-ROOT-106/122 and every other
blocker remain as they are.

Not ruled here: G2 supply-unit acceptance; the App-side treatment of the
observed plugin-sync destination (an App OUT-002/G-ENV concern consumed
downstream); any upstream communication; any later gate.
