# Owner Ruling — App Parked-Decision Slate Dispositions

Date: `2026-08-21`

Status: OWNER RULING OF RECORD

Provenance: the owner (Ryan Tufts) ruled in-session and directed HELP_HUMAN
to relay the ruling to the App loop's TASK_MANAGEMENT instance. K-AUTH-1 is
satisfied by the owner's explicit statement that the owner ruled and carries
the text below. This record transcribes the four-part ruling verbatim. It
authorizes only the effects stated by the owner; it creates no unstated
promotion, disposition taxonomy value, proof, launcher action, foreign-loop
write, lifecycle effect, or release claim.

## Owner ruling — verbatim

```text
1. D-APP-86 launcher post-state TM candidate: DISPOSITIONED — ACCEPT the recorded launcher state as baseline, with provenance evidence. An owner-directed read-only host inspection (Agent 0, 2026-08-21) found: live /Users/ryan/.local/bin/chirality still hashes SHA-256 f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a, unchanged since 2026-08-20 15:26; content is byte-structurally the exact renderCliLauncher output (frontend/electron/cli-launcher.ts) — product-generated, no tampering; its pins identify the D-APP-86 parity invocation as author (worktree dist executable path, LaunchAgent label com.chirality.runtime.d86pkg02, userdata default /private/tmp/chirality-d86pkg02.VWKLGL which no longer exists); the operator LaunchAgent com.chirality.runtime is loaded and unaffected. Record the acceptance noting the launcher is functionally stale drill output and that the next authorized packaged operator launch is expected to rewrite it idempotently. No launcher action is authorized now.

2. TM-APP-036 distinct-helper parity-rerun trigger: RETIRED. Remove the trigger from the register: no distinct helper .app exists or is planned; the current package uses the main executable plus --runtime-daemon. If a D-APP-88 distinct-helper implementation is ever accepted, establishing a new rerun trigger requires a fresh owner ruling — do not treat this retirement as pre-authorizing one.

3. TM-APP-044: REHOME AUTHORIZED. Add the remaining runtime-delegation work to DEL-08-04's ## Remaining surface so it is selectable as an engineering product target. Name the root-side metadata/validator alignment there explicitly as a dependency owned by the root loop — the App loop implements only its own side and does not reach into root surfaces.

4. DEL-09-04 LaunchAgent auto-start proof: PREPARE-THEN-OWNER. Next iteration may prepare the proof harness and a minimal owner procedure (install steps, the logout/login act, one capture command, evidence packaging). The logout/login itself remains an owner act on the owner's schedule; do not treat preparation as the proof.
```

## Applied register meaning

### 1. D-APP-86 launcher post-state candidate

The source is a harvested `TM-CANDIDATE:` marker, not a promoted Action Item
row. The owner did not direct promotion. The lawful treatment is therefore
**no new register row**: this ruling record preserves the owner's exact
`DISPOSITIONED — ACCEPT` treatment and screens the marker as already ruled.
No PRD disposition-taxonomy token is fabricated for a row that does not
exist.

Provenance reviewed for this application:

| Evidence | SHA-256 / observation |
|---|---|
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/TM_CANDIDATES.md` | `88652f8aea5ec12c65ddf7a6f71be9c1d2a69b99ccc8f17fbff5e2be8557fac0` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/instances/A2-PKG02-PARITY-EXECUTOR-01/evidence/runtime/desktop-main.log` | `4b0b310ec20ed294a2e986dab76fe1cdd65fb620ed357cf57ca93b515b37d702`; records `desktop.cli_launcher.install` as `written` at `2026-08-20T21:26:36.929Z` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/PACKAGED_UI_SMOKE.md` | `2149fa1fabf6c0e7ce655be77222d0d21a27cd2f124c8efade2776b4abed8fab` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20/instances/A2-PKG02-PARITY-EXECUTOR-01/RETURN.md` | `408eae1a1e14baafd93228f07222aebe62d78823d7ec18ac8b09c7771aa6904c`; records the same launcher post-write hash and no trustworthy before-state |
| `projects/chirality-app-dev/frontend/electron/cli-launcher.ts` | `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`; contains `renderCliLauncher` and content-idempotent installation |
| Owner-directed read-only host inspection relayed 2026-08-21 | live launcher SHA-256 `f16bc2ba9228b5321deb9c66ba9526aa60fbe3bb02179d32fd66ce1de208384a`; mtime `2026-08-20 15:26:36 -0600`; byte-structural renderer match; stale D-APP-86 pins; disposable root absent; operator job `com.chirality.runtime` loaded separately with operator user-data |

The accepted baseline is functionally stale drill output. The next authorized
packaged operator launch is expected to rewrite it idempotently. No launcher
action is authorized by this record.

### 2. TM-APP-036

Mechanical row maintenance is authorized: remove the retired second residue
from the live row's title, concern, associations, and notes. Preserve its
historical source and candidate citation. The row remains `OPEN`, with blank
`Disposition`, `EvidenceRef`, `EvidenceSha`, and `Closed`, because the
three-deliverable pointer/status review survives. Historical evidence remains
in the immutable 2026-08-03 source, harvest report, promotion ruling, and this
superseding owner ruling.

### 3. TM-APP-044

The owner authorizes a deliverable-amendment package routed to PKG-08
WORKING_ITEMS for DEL-08-04. Existing evidence establishes that the App-side
product code and tests already landed in commit
`ac2cd801a06a0679bc86830c627218ccca78b658` and were integrated under
Receipt 172. No duplicate App implementation is proposed. The only residual
App work to place on `## Remaining` is post-root cross-surface validation and
integration after the root loop completes its separately owned `TM-ROOT-125`
metadata/validator alignment.

TM-APP-044 remains `OPEN`. TASK_MANAGEMENT does not edit DEL-08-04 and does
not close the row before the owning amendment lands and its evidence is
hash-bound.

### 4. DEL-09-04

The PREPARE-THEN-OWNER ruling is preserved exactly above for Agent 0 and the
owning production lane. TASK_MANAGEMENT does not manage DEL-09-04, does not
prepare the harness in this register-maintenance run, and does not claim that
preparation or this record constitutes the logout/login proof.

## Effect boundary

This ruling record is an App Task Management coordination artifact. It does
not itself amend a deliverable, execute validation, alter a launcher or
LaunchAgent, write a Root surface, close TM-APP-044, prove DEL-09-04, or
authorize any later distinct-helper trigger.
