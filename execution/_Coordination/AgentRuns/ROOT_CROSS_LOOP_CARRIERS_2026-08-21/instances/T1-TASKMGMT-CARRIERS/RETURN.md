# TASK_MANAGEMENT return — Root cross-loop carrier decision preparation

- RunID: `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- Instance: `T1-TASKMGMT-CARRIERS`
- Invoking loop: Root
- Parent: `HELP_HUMAN`
- Verdict: `DECISION_SLATES_READY / PRODUCTION HELD AT HUMAN GATE`
- Write effect: this return and companion `STATUS.json` only; zero register,
  receipt, notice, decision, deliverable, package, runtime, foreign-loop, or
  Git writes.

## 1. Mandatory federation preflight

The deterministic command was run before decision preparation:

```text
python3 tools/taskmgmt/taskmgmt.py federation \
  --register execution/_Coordination/_TaskManagement/REGISTER.csv \
  --out /tmp/t1-federation.json
```

Result: `COMPLETE`; four canonical registers discovered, read, and validated;
zero register writes; no excluded tracked lookalikes.

| Loop | Live rows | Live status | Archived | Validation |
|---|---:|---|---:|---|
| Root | 23 | OPEN 13 / DEFERRED 10 | 102 | PASS / PASS |
| App | 13 | OPEN 9 / DEFERRED 3 / CLOSED 1 | 31 | PASS / PASS |
| Piping | 34 | OPEN 11 / DEFERRED 23 | 8 | PASS / PASS |
| PEC | 18 | OPEN 16 / DEFERRED 1 / CLOSED 1 | 7 | PASS / PASS |

Program-wide typed findings: 49 `FOREIGN_LINK_TO_LOCAL`, 2
`LOCAL_LINK_TO_FOREIGN`, 3 `REMOTE_CLOSED_LOCAL_OPEN`, 21
`LOCAL_CLOSED_REMOTE_OPEN`, and 4 `MISSING_NOTICE`. There are zero invalid or
unreadable registers, ambiguous references, duplicate global IDs, orphaned
links, inbound elevations, or outbound-awaiting-ack findings. The relevant
typed relation is `TM-ROOT-117` -> `TM-APP-032` through `SourceRef`
(`LOCAL_LINK_TO_FOREIGN`). No typed federation relation presently makes
`TM-APP-027` or `TM-APP-028` a Root register row; their Root carrier is the
routed coordination notice and the independently owned DEL-02-06 lifecycle.

The projection was written only to `/tmp`; it is derived, rebuildable, and
not authority. Authoritative register SHA-256 identities at inspection:

- Root live: `6955ae0b1a606e7053e78ccf33258f3247eee6d4ef8133720a0dbeb939dc9978`;
  archive: `0c3dfc3cf60d86a623a2b171540e10f6a1977d83175c190305b61dc57b25a9a0`.
- App live: `ff84a9ace7722532374aa73d474ac99d34a605c30e951468076904e474a0497f`;
  archive: `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6`.
- Piping live: `5bad460d18782fbf7f3b370e2eca2d3518a178dfb485aa1d9386b2e9d85a064c`;
  archive: `c110c052fa2735b31c6889b8fdd7f2898d7a0194fc5bf5fbf703bc9024472192`.
- PEC live: `6f7eb2a528a8a38ee01b94f5a028632d95297c82f4fa197f4c62f7102fef9264`;
  archive: `bf0d5537686d3dba23ad2e3c1b91d989850cda04e98e92dc545516829c9242b6`.

The sealed brief's accepted worktree basis is present at
`HEAD=e3e18d27740018efd12e73193c02395a9eca93c2`. During the run, the local
tracking ref `origin/main` was `7d5a3f558dfa2e8e902df25fc9a3e813a9ab7048` and contained HEAD. A scoped
`HEAD..origin/main` diff found no change to the four register homes or any
required TM-ROOT-117 / DEL-02-06 / App decision and carrier source used in
this return. This is disclosed basis drift, not a semantic-input change.

## 2. Authority classification

### Authoritative facts

1. Root `TM-ROOT-117` is `OPEN` and was owner-promoted with closure class
   `RESOLVED_BY_DECISION`. Its allowed resolution is either an owner ruling
   naming an accepted D-APP-48 successor identity or an owner direction that
   App re-scope `TM-APP-032`; either outcome requires a routed App notice.
2. App `TM-APP-032` is `DEFERRED`. Its exact current trigger requires
   `TM-ROOT-117` to close `RESOLVED_BY_DECISION` and a routed Root notice to
   name an exact accepted successor plus a separate human-acceptance record,
   or direct App to re-scope the trigger. Preparation, DEL activation, draft
   production, or identification without human acceptance does not fire it.
3. D-APP-48 historically selected an App-era private intra-repo SHA-pinned
   pull mechanism. D-APP-73 prospectively rehomed generic runtime contracts
   to Root while preserving an App compatibility re-export. D-APP-76 E1
   selected only preparation of a Root-owned successor route and expressly
   created no identity, version, commit, compatibility boundary, repin, or
   implementation. D-APP-89 Option B authorized the App direct-import
   migration to `@chirality/runtime-contracts` but expressly did not resolve
   D-APP-48 successor identity.
4. DEL-02-06 `_STATUS.md` remains `INITIALIZED`; it says the first
   WORKING_ITEMS production activation is unauthorized. The later accepted
   semantic snapshot has no lifecycle-pointer effect and does not change that
   status.
5. The human-accepted DEL-02-06 semantic snapshot
   `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`
   accepts the six exact V2 semantic members. Its compatibility member
   `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1`
   accepts the grammar `root-runtime-<positive-decimal-epoch>`, exact
   two-sided per-operation equality, distinct
   `RUNTIME_COMPATIBILITY_MISMATCH`, no range negotiation/downgrade/
   multi-version inference, epoch-change criteria, and one immutable binding
   manifest shape. It explicitly mints no numeric epoch or identity.
6. The accepted handoff
   `acf64d0518e4a589650bea6885bd5b3c2ada7dfd0f01880f05150e9017ffe2d6`
   and manager return
   `65bc77f02759b8a58b3a811b6a79d5fbbf1001636b84db576a7a780a0cab1e22`
   name the next gate: an owner-supplied positive-decimal epoch plus a
   complete immutable compatibility binding manifest, returned as exact
   bytes for accountable-human acceptance. Implementation and every later
   lifecycle/release/reliance gate remain held.
7. The App notice for `TM-APP-027` and `TM-APP-028`, SHA-256
   `17f269567c3a5795799e5be92a9ac75281dc8ff553afa11376a055d3e78924ed`,
   is coordination only. Its requested Root response matches the live
   DEL-02-06 handoff: epoch, complete binding manifest, exact-byte human
   acceptance, then reciprocal notice.

### Derivative or observational support

- The D-APP-89 WORKING_ITEMS manager return is derivative execution evidence.
  It proves App migrated ordinary imports to `@chirality/runtime-contracts`
  and retained the facade; it expressly disclaims a D-APP-48 successor act.
- Current `runtime/packages/contracts/package.json` identifies the package as
  `@chirality/runtime-contracts` version `0.1.0`. A package name/version and
  implementation location are not the Root compatibility identity under the
  accepted semantics.
- A tracked search found no concrete `root-runtime-<digits>` value. That is
  collision evidence for a future candidate, not authority to mint one.
- Task Management registers are authoritative only for Action Item existence
  and disposition. The App notice and federation projection create no Root
  duty, acceptance, or lifecycle effect.

## 3. TM-ROOT-117 decision slate

### Current conclusion

No exact **accepted** D-APP-48 successor identity exists in the inspected
basis. The only exact candidate supportable from accepted semantics is
`root-runtime-1`: `1` is the smallest positive decimal, the accepted contract
calls this the initial epoch, and no concrete `root-runtime-<digits>` value
exists in the tracked tree. It remains non-binding decision support. It must
not be cited as accepted until an accountable-human record binds exact
completion-package bytes and their SHA-256 identity.

### Option R — direct App to re-scope now (recommended)

Exact owner token:

```text
TM-ROOT-117 — APPROVE OPTION R (RE-SCOPE). CLOSE TM-ROOT-117 RESOLVED_BY_DECISION. ROUTE A RECIPROCAL NOTICE DIRECTING APP TO REPLACE TM-APP-032'S TRIGGER WITH THE EXACT TEXT IN THE T1 RETURN; NO SUCCESSOR IDENTITY IS ACCEPTED BY THIS RULING.
```

Exact proposed App trigger text:

```text
Root DEL-02-06 records accountable-human acceptance of an exact compatibility-completion package that supplies a positive-decimal Root compatibility epoch and the complete immutable compatibility binding manifest required by accepted semantic snapshot SHA-256 `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`; then a routed Root notice lands in the App loop citing the exact accepted bytes, their SHA-256 identity, and the separate human-acceptance record. Semantic-byte acceptance alone, epoch selection without accepted package bytes, draft production, implementation behavior, or TM-ROOT-117 closure alone does not fire this re-scoped trigger.
```

Tradeoff: this closes the orphaned Root carrier immediately and aligns
`TM-APP-032` with the same checkable Root gate already used by
`TM-APP-027`/`028`, but App remains deferred until its own instruments adopt
the replacement and the compatibility-completion gate later fires.

### Option I — wait for an exact accepted successor

This option is not currently selectable as an immediate closure because the
required exact acceptance record does not exist. The future closure token,
only after exact bytes are prepared and accepted, is:

```text
TM-ROOT-117 — APPROVE OPTION I. ACCEPT D-APP-48 SUCCESSOR IDENTITY `<EXACT_ROOT_COMPATIBILITY_IDENTITY>` UNDER `<HUMAN_ACCEPTANCE_RECORD>` AT SHA-256 `<EXACT_SHA256>`. CLOSE TM-ROOT-117 RESOLVED_BY_DECISION AND ROUTE THE ACCEPTED IDENTITY, RECORD, AND HASH TO APP.
```

Using `root-runtime-1` in this token before the acceptance record exists
would invent acceptance and violate K-AUTH-1, K-AUTH-2, K-INVENT-1, the
accepted compatibility member, and the explicit App trigger.

Tradeoff: Option I preserves a direct successor-identity trigger but keeps
`TM-ROOT-117` and `TM-APP-032` open through at least one production gate and
one later human exact-byte acceptance gate.

### Closure and routing plan after Option R ruling

Do not execute before the owner rules. After the ruling:

1. Record the exact human decision in a Root-owned decision-support/ruling
   record and compute its SHA-256.
2. Update only Root `TM-ROOT-117`: `Status=CLOSED`,
   `Disposition=RESOLVED_BY_DECISION`, `EvidenceRef` to that record,
   `EvidenceSha` to its exact bytes, `EvidenceQuote` to the ruling token, and
   current `LastReviewed`/`Closed`; then archive under the normal Root
   register procedure.
3. Validate live/archive registers and run a final federation pass.
4. Through Root's ordinary closeout, route one reciprocal coordination notice
   to App citing `TM-ROOT-117`, `TM-APP-032`, the ruling path/hash, this
   trigger text, D-APP-76, the accepted semantic snapshot, and the accepted
   handoff. The notice grants no App disposition authority.
5. App decides whether and how to adopt the re-scope and maintain or close its
   row under App instruments. Root performs no App register write.

## 4. DEL-02-06 / TM-APP-027 / TM-APP-028 assessment

### Current classification

The App rows remain `ACTIVATABLE` in the App deferral-review sense: a named
Root instrument plus later human acceptance can fire them. Actual Root
production is nevertheless **held now at a human gate**. The live status does
not authorize a new production activation, and the exact package cannot be
prepared without inventing the owner-supplied epoch. No planning shell or
placeholder manifest should be written to simulate progress.

The accepted compatibility member also requires the single manifest to carry
the exact identity; all six accepted semantic-member hashes and their sorted
package-manifest identity; source/release, affected-client, conformance,
Root-evidence, census/Tier-0/PEC/notice/finding, cutover/rollback/replay, and
human-act fields. A later WORKING_ITEMS run must populate each field from
accepted evidence or return it honestly as blocking; it may not infer a pass,
acceptance, implementation, release, or foreign-loop disposition.

### Exact owner fields needed now

1. `epoch`: one positive decimal integer. Non-binding recommendation: `1`.
2. `preparation_authorization`: authorize or decline one new sealed
   DEL-02-06 WORKING_ITEMS activation limited to compatibility-completion
   package preparation and validation.
3. `effect_boundary`: package preparation only; no implementation, source or
   test edits, client conformance, lifecycle transition, release,
   publication, reliance, or foreign-loop act.

Recommended exact owner token:

```text
DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `1`, YIELDING CANDIDATE IDENTITY `root-runtime-1`, AND AUTHORIZE ONE SEALED WORKING_ITEMS ACTIVATION TO PREPARE AND VALIDATE THE EXACT COMPATIBILITY-COMPLETION PACKAGE AGAINST ACCEPTED SNAPSHOT `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`. PREPARATION ONLY: DO NOT ACCEPT THE RESULTING BYTES BY INFERENCE; DO NOT IMPLEMENT, CHANGE LIFECYCLE, RELEASE, PUBLISH, ASSERT RELIANCE, OR WRITE A FOREIGN LOOP.
```

Alternative exact token:

```text
DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `<POSITIVE_DECIMAL>` AND AUTHORIZE THE SAME PREPARATION-ONLY ACTIVATION AND EFFECT BOUNDARY STATED IN THE T1 RETURN.
```

Tradeoff: epoch `1` is the minimal initial value and is deliberately unrelated
to npm version `0.1.0`, Flow-A `flow-a.contract.v0.1.0`, source/release commit,
runtime fingerprint, route namespace, session identity, or residency epoch.
Another positive decimal is lawful but needs an explicit owner value and the
same collision/reserved-value validation.

### Largest bounded lawful slice after the owner token

Dispatch Root `WORKING_ITEMS` against DEL-02-06 with one new immutable
deliverable-local run root. Limit it to:

1. reproduce the accepted snapshot, six member hashes, package-manifest hash,
   live lifecycle, and no-drift basis;
2. apply the owner-supplied epoch to a new exact compatibility-completion
   candidate without altering the accepted historical semantic members;
3. assemble the one immutable binding manifest required by the accepted
   compatibility member, preserving explicit held/unavailable states and
   returning any field that cannot be populated without invention;
4. run deterministic completeness/hash/collision checks plus a fresh
   read-only semantic and authority refutation;
5. emit an exact candidate manifest, validation, manager return, and handoff
   for a **later** accountable-human exact-byte acceptance gate.

No implementation brief may be released from that slice. If any required
manifest field needs unavailable acceptance or evidence rather than an exact
honest disposition, the run must stop and return that field; it must not
weaken `complete` or fabricate evidence.

After the later human accepts the exact completion bytes, Root may route one
reciprocal notice to App citing `TM-APP-027` and `TM-APP-028`, the accepted
record and hashes, and stating whether range negotiation/downgrade/
multi-version inference remain unsupported and whether the accepted
ten-condition degraded-mode contract remains current. App then dispositions
its rows under App instruments.

## 5. Recommendation and blockers

Non-binding recommendation:

1. Rule TM-ROOT-117 **Option R** now and route the exact re-scope. This is the
   only presented option that permits truthful immediate
   `RESOLVED_BY_DECISION` closure.
2. Separately supply DEL-02-06 epoch `1` and authorize the preparation-only
   completion activation. Treat `root-runtime-1` as a candidate until the
   later exact-byte acceptance record exists.

Current blockers:

- human ruling on TM-ROOT-117 Option R versus waiting for a future accepted
  identity;
- owner-supplied positive-decimal compatibility epoch and explicit sealed
  preparation activation;
- later WORKING_ITEMS production, completeness validation, and fresh
  refutation;
- later accountable-human acceptance of exact completion-package bytes;
- App-owned adoption/disposition after reciprocal notices.

No blocker above authorizes this instance to write a register, notice,
decision, deliverable, package, runtime, receipt, or foreign-loop surface.
