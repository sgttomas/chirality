# D-APP-87 — Dual-Target Product-Direction Adoption and Re-plan

**Status:** `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

**Prepared:** 2026-08-02 by `HELPS_HUMANS`, managed by App `HELP_HUMAN`

**Task Management link:** `TM-APP-025`

## 1. Decision requested

Should the App loop adopt, amend, defer, or decline the recorded product
direction as an App planning input: one codebase serving both the standalone
Chirality Desktop app and a lightly skinned per-domain control-plane UI, with
domain-specific applications as the primary delivery vehicle for the agents?

If adopted or amended, should the owner authorize a bounded App re-plan across
UI, packaging, and runtime-contract planning, returned for a later owner gate
before any implementation or scope effect?

## 2. Authority and evidence boundary

| Evidence | SHA-256 | Effect |
|---|---|---|
| `execution/_Coordination/OWNER_INTENT_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md` | `9bbb67556765c6c83d6a35a1ace297e4d693d5169281c620dc9b2673229c7e03` | Records owner intent for loop consumption; explicitly not PRD, scope, decomposition, or reliance authority. |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md` | `3231f46463e5a9d2b93793ae39b3b78a041878220932b369d76a976601090cb3` | Routes the direction to App and requires App to act through its own instruments. |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_ROOT_RESPONSE_DAPP84_DAPP85.md` | `b4c6e9a67437618de517616ab411bb411bb099f543663ab14362c745e901b328` | Reports that generic runtime/sandbox work remains Root-gated; H1 grants no Bash now. |

This packet is the App instrument. The notices alone adopt nothing. A ruling
on this packet may establish an App planning input and authorize planning; it
does not amend the PRD, decomposition, deliverables, or runtime contract.

## 3. Root-gated exclusion

No option authorizes selection or implementation of generic runtime-contract,
sandbox, identity, version, resume, or Bash work while:

- Root `TM-ROOT-105` waits for the Piping loop's recorded runtime-surface
  response;
- Root `TM-ROOT-107` awaits a ruled SCOPE_CHANGE reference;
- Root `TM-ROOT-109` shares the `TM-ROOT-105` trigger; and
- the Piping response gate named by those rows remains unresolved.

App may inventory affected-client needs and mark a runtime-contract lane
`BLOCKED_BY_ROOT`, but may not define the generic contract, grant Agent-2
Bash, or select implementation that depends on it.

## 4. Options

### Option A — Adopt the direction as App planning input (recommended)

Adopt all of the following for planning only:

- Chirality App remains a standalone Desktop target;
- the same App codebase also supports a lightly skinned per-domain
  control-plane target;
- domain applications are the primary delivery vehicle for the agents; and
- the per-domain UI focuses users into typed agent interactions, structured
  information, workflows, and decision gates toward outcomes.

Authorize one bounded re-plan that inventories current accepted App scope and
returns a later proposal covering UI, packaging, and affected-client runtime
needs. The re-plan may recommend later scope/PRD/decomposition acts but cannot
perform them.

### Option B — Amend before adoption

Adopt the two-target requirement (standalone Desktop plus per-domain skin),
but treat one or both of these statements as hypotheses pending the re-plan:

1. domain-specific apps are the primary delivery vehicle; and
2. the targets must remain one lightly skinned codebase rather than a shared
   package/core with target-specific shells.

The owner must name the amendment. The same bounded re-plan then tests the
amended posture without silently restoring the omitted premise.

### Option C — Defer

Adopt nothing yet. Re-present after a named trigger, such as the Piping
runtime-surface response or Root's opening of the generic-contract workstream.
Current App planning remains governed by existing accepted sources.

### Option D — Decline

Decline the routed direction as an App planning input. The standalone App
continues under existing accepted scope; any future domain control-plane skin
requires a new App product/scope proposal.

## 5. Bounded re-plan contract for A or B

The re-plan is a derivative planning package, not decomposition truth. It must
be built from live PRD, accepted decomposition/SCOPE_CHANGE state, deliverable
Remaining items, current source/package topology, validation strategy, and the
selected D-APP-87 ruling.

It must return:

| Lane | Required planning output |
|---|---|
| UI | shared versus target-specific surfaces; skin/configuration boundary; typed-agent, structured-information, workflow, and decision-gate mappings; accessibility and D-APP-36 visual-evidence implications |
| Packaging | standalone app and domain-skin artifact topology; identity/config/resource boundaries; unsigned local validation matrix; no signing/publication commitment |
| Runtime contract | App affected-client requirements and blocked interfaces only; explicit `BLOCKED_BY_ROOT` markers for generic contract, sandbox, identity, version, resume, and Bash concerns |
| Deliverables | exact existing deliverables affected, candidate amendments, dependencies, and work-order implications; no new deliverable or scope adoption |
| Validation | target-by-target source, UI, packaged, and runtime-client evidence matrix with common and target-specific checks |
| Decisions | every later owner gate required for PRD, decomposition, SCOPE_CHANGE, public contract, packaging identity, release posture, or cross-loop action |

The package must live under a frozen App AgentRuns root and fan in to a new
`PROPOSAL` in `_DECISIONS/` using the then-next live D-APP ID. It must not
create a new standing plan, queue, register, or status surface.

## 6. Validation implications

Planning validation is static: source/path/hash verification, exact
deliverable inventory, current package/import topology, register-ID
uniqueness, reference integrity, `git diff --check`, corpus/receipt checks as
applicable, and an independent adversarial review of the later proposal's
authority boundaries.

If later implementation is separately ruled, its evidence matrix must cover
both targets and prevent a standalone-only check from proving a domain-skin
claim or vice versa.

## 7. Risks and non-effects

- A risks prematurely treating “same codebase/light skin” as an architecture
  constraint; the later re-plan must test, not assume, its implementation
  form.
- B preserves design latitude but may weaken the owner's recorded delivery
  emphasis if the amendment is vague.
- C delays useful UI/packaging planning even though those lanes do not require
  the generic Root contract.
- D may force a later product/scope restart if domain delivery proceeds.

No option in this packet edits PRD, decomposition, SCOPE_CHANGE, deliverables,
runtime/frontend source, Root/Piping/PEC surfaces, or Task Management rows. No
option authorizes release, lifecycle advancement, provider/network expansion,
generic runtime work, or Agent-2 Bash. The six D-APP-81 unknown historical
relations remain untouched.

## 8. Non-binding recommendation

Select **Option A**. It most faithfully consumes the owner's direction while
keeping every product-basis and implementation act behind a later App gate.
Begin UI and packaging re-plan work now; record runtime-contract needs only as
affected-client requirements blocked on the named Root/Piping gates.

## 9. Owner return tokens

- `APPROVE D-APP-87 OPTION A`
- `APPROVE D-APP-87 OPTION B — AMENDMENT: <exact amendment>`
- `APPROVE D-APP-87 OPTION C — TRIGGER: <trigger>`
- `APPROVE D-APP-87 OPTION D`
