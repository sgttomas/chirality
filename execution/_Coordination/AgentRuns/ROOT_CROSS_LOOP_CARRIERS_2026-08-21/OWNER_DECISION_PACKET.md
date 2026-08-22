# Owner decision packet — Root carrier decisions

Status: `DECISION SUPPORT ONLY — NO OPTION SELECTED`

Prepared by: `HELP_HUMAN` from validated `TASK_MANAGEMENT` return
`instances/T1-TASKMGMT-CARRIERS/RETURN.md` at SHA-256
`95bba875c86b967e8374a3f6affadf951407886113218cc028118feab14216e3`

Accepted inspection basis: `e3e18d27740018efd12e73193c02395a9eca93c2`.
The later observed `origin/main@7d5a3f558dfa2e8e902df25fc9a3e813a9ab7048`
changes no cited carrier, register, decision, or DEL-02-06 input.

This packet presents two independent owner decisions. Selecting one does not
select the other. No text below is a ruling until returned by the owner.

## Decision 1 — TM-ROOT-117 / App TM-APP-032

### R — direct App to re-scope (non-binding recommendation)

```text
TM-ROOT-117 — APPROVE OPTION R (RE-SCOPE). CLOSE TM-ROOT-117 RESOLVED_BY_DECISION. ROUTE A RECIPROCAL NOTICE DIRECTING APP TO REPLACE TM-APP-032'S TRIGGER WITH THE EXACT TEXT IN THE T1 RETURN; NO SUCCESSOR IDENTITY IS ACCEPTED BY THIS RULING.
```

Effect: Root closes the orphaned carrier by decision and routes the exact
replacement trigger from the T1 return. App remains free to adopt, amend, or
decline under its own instruments. The replacement points to the same
DEL-02-06 compatibility-completion acceptance gate already awaited by
`TM-APP-027` and `TM-APP-028`.

Reason for recommendation: no exact accepted D-APP-48 successor exists.
D-APP-76 is preparation-only; D-APP-89 expressly disclaims a successor act;
and package name/version `@chirality/runtime-contracts@0.1.0` is not the
Root compatibility identity under the accepted DEL-02-06 semantics. Re-scope
avoids inventing a second or prematurely accepted identity.

### I — retain the carrier until a future accepted successor exists

```text
TM-ROOT-117 — SELECT OPTION I (WAIT FOR AN EXACT ACCEPTED SUCCESSOR). RETAIN TM-ROOT-117 OPEN AND TM-APP-032 DEFERRED; NO SUCCESSOR IDENTITY IS ACCEPTED BY THIS RULING.
```

Effect: no row closes and no App trigger changes. A later closure would require
an exact Root compatibility identity, exact accepted bytes, a separate human
acceptance record and SHA-256, and a reciprocal App notice.

## Decision 2 — DEL-02-06 compatibility-completion preparation

### E1 — supply epoch 1 and authorize preparation (non-binding recommendation)

```text
DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `1`, YIELDING CANDIDATE IDENTITY `root-runtime-1`, AND AUTHORIZE ONE SEALED WORKING_ITEMS ACTIVATION TO PREPARE AND VALIDATE THE EXACT COMPATIBILITY-COMPLETION PACKAGE AGAINST ACCEPTED SNAPSHOT `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`. PREPARATION ONLY: DO NOT ACCEPT THE RESULTING BYTES BY INFERENCE; DO NOT IMPLEMENT, CHANGE LIFECYCLE, RELEASE, PUBLISH, ASSERT RELIANCE, OR WRITE A FOREIGN LOOP.
```

Effect: supplies the missing owner field and releases one new immutable,
deliverable-local preparation run. The run must reproduce the six accepted
member hashes and package manifest, assemble the single required binding
manifest with honest held/unavailable dispositions, validate and refute it,
and return exact candidate bytes for a later human acceptance gate. It cannot
release implementation.

Reason for recommendation: `1` is the smallest lawful initial positive
decimal, and no tracked concrete `root-runtime-<digits>` value exists. It is
deliberately unrelated to npm `0.1.0`, Flow-A
`flow-a.contract.v0.1.0`, source/release commits, runtime fingerprints,
routes, sessions, or residency epochs.

### E-other — supply another positive decimal

```text
DEL-02-06 — SUPPLY INITIAL ROOT COMPATIBILITY EPOCH `<POSITIVE_DECIMAL>` AND AUTHORIZE THE SAME PREPARATION-ONLY ACTIVATION AND EFFECT BOUNDARY STATED IN OWNER_DECISION_PACKET.md.
```

Effect: same as E1, with mandatory collision and reserved-value validation.

### E-defer — retain the gate

```text
DEL-02-06 — DEFER COMPATIBILITY-COMPLETION PREPARATION. SUPPLY NO EPOCH AND AUTHORIZE NO NEW ACTIVATION.
```

Effect: `DEL-02-06` stays `INITIALIZED`; no package is produced;
`TM-APP-027` and `TM-APP-028` remain deferred.

## Preserved gates

- Any decision on TM-ROOT-117 is independent of epoch/preparation selection.
- `root-runtime-1` is only a future candidate until the owner supplies it.
- Preparation is not exact-byte acceptance, implementation, lifecycle,
  release, publication, reliance, or a foreign-loop act.
- After exact completion bytes are prepared, their accountable-human
  acceptance is a separate decision.
- App adoption and App register dispositions remain App-loop acts.
- PR review and merge remain owner acts.
