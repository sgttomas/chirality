# DELIVERY — guard implementation integration checkpoint

**Ready for ROOT to freeze and send for independent review. The guard is
implemented and pure-tested, inactive and not live-qualified.** I21's separate
source-only checkpoint is complete, with full K0 acceptance still open.

Manager `/root/delivery_manager` (WORKING_ITEMS / Agent 1) returns to ROOT
`/root`. Continuation basis is `b2acd4023557eeff2416d99aaed1f03abf7a2404`;
product/source basis remains `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
Manager writes are confined to this new folder. The initial DELIVERY/ENV
packets committed at the continuation basis remain unchanged; all 27 initial
manifest entries reverify. ROOT owns Git/index and shared writes.

## Actual execution and checked return

ROOT explicitly granted the TASK slot released by ENV. DELIVERY launched
`/root/delivery_manager/guard_implementation` through native
`collaboration.spawn_agent`, fresh context, no model override. The committed
brief SHA256 is
`09079fc3441de766ef4abbe463d6731741b8c0df8cbadb4ee3c13d147e66ee68`.
`GUARD_LAUNCH.json` records parentage, basis and the prompt-only write fence.
The TASK has now completed; no additional child was launched by DELIVERY.

The author wrote only `Run/tools/host_guard.py` and
`Run/instances/GUARD-IMPLEMENTATION/**`. All **10 guard manifest entries**
verify. The author log records **41 pure tests passing**. Manager checked
packet integrity, read the return/provider/limits/live-plan records, and
inspected the source interfaces and fake-only test fence; this integration
check is not the required independent review and did not rerun the guard.

| Artifact | SHA256 |
|---|---|
| host_guard.py | `feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db` |
| test_host_guard.py | `5e72b5d9589b345d1ef45171227b7b6a56281b7b2984e97625291112fb62b5b1` |
| pure-tests.log | `976d0b3ee9ed9856bb78236e553a7b8963d7762020f78528a81d38874da557c8` |
| GUARD-IMPLEMENTATION/RETURN.md | `79ab19582efa382537db30b35c1baf5f5d9dc58692821d49ee299a35c4cebaba` |
| GUARD-IMPLEMENTATION/SHA256SUMS | `bea430634d4e3c597f77a33c031d58b7f2fd41379b62684df8b7e7bcf4b497d3` |

The guard uses explicit job parameters and one runtime flock; an independently
running supervisor owns its session/group and private nonce/sequence channel.
Only that continuously live owner sends group TERM/KILL. Worker signal handlers
are reset before exec. Monitoring failure/heartbeat loss routes through the
owner; unresolved termination leaves a latch blocking retries. Fixed provider
commands and ctypes bindings are source-derived from the installed SDK. Group
RSS, physical footprint, available percentage, pressure, swap and disk are
separate quantities. The existing binary heap backstop is preserved.

Manager feedback tightened the pure test capability fence around import and
session/exit paths, and added executable-hash regression coverage. The author
also replaced in-group ps completion sampling with native group enumeration,
then fake-tested sizes/denial/identity races/draining. Real native calls, fork,
flock, signals, provider sampling, workload and guard activation have not run.

## Boundaries for independent review and live qualification

The first scope is direct cargo/rustc and tiny probes with descendants remaining
in the owned group. K6/VR runners create separate sessions and remain unsupported;
a later explicit registration adapter needs its own review and qualification.
The serial DEC-025 driver is proposed separately and is not implemented here.

`../GUARD-IMPLEMENTATION/PROVIDERS.md`, `LIMITS.md` and
`LIVE_QUALIFICATION.md` supply the precise review/qualification package. Open
items include actual ABI/provider permissions, socket/fork/flock behavior,
signal defaults and TERM-ignore escalation, monitoring cadence/stop latency,
peak overshoot and useful direct-cargo operation under conservative race stops.
Userspace polling cannot guarantee catching an unseen double-fork/reparent
escape. External supervisor SIGKILL defeats this single-owner containment;
the guard retains the latch and does not signal an old group. These are explicit
limits, not live-tested safety claims.

The future qualification plan uses a read-only provider witness, low-memory
owned fixture, unrelated sentinel, ordinary completion, 16-MiB allocation,
TERM-ignore escalation, 64-MiB cap crossing, monitor loss, visible escape and
lock/latch refusal cases. None is executed here. ROOT's reviewed operating
choices and actual host boundary govern each later invocation. A source/tool
existence check or 41 passing fake tests does not supply a heavy slot.

## I21 parallel return

I21 `/root/delivery_manager/i21_k6c` completed its source-only assignment while
the guard was authored. All **13 I21 manifest entries** verify. RETURN hash:
`6e882dd527d0c2e35e6befe4879406a28badb9ab0af2061e74d4107f9871aafa`;
manifest hash:
`6a40dfe26ce2752844db4f0f8fad0f96da26a4d8174ac1fae0bc75aadff6f952`.
`I21_RETURN_INTEGRITY.json` records this manager check.

It closes the two nl_pass lifetime corrections, reproduces 36 original admission
dictionaries and evaluates a provisional normalization against 204 selected
historical heap comparisons. It does **not** establish final E_max or admit A.
Next work is narrowly identified: K0-S1 original fixture/preparation capacities;
K0-S2 finish/report/control/binary closure; K0-L1 exact private-layout/liballoc
witness in a separately authorized disposable archive; K0-V1 complete formula
review. Final A1 change impact still governs final estimate/evidence. Additional
VR Cargo.lock and possibly H main/capacity reporting paths need explicit write
grants before editing. The provisional roughly 3-GiB 10,000-member estimates
are not suitable for the current <=2-GiB half-cap backstop.

## New owner direction and next safe action

ROOT's central decision `Run/decisions/03_OWNER_EVIDENCE_AND_A0_PREPARATION.md`
records the owner-approved safe continuation while M5 originals are unavailable
for now. `OWNER_DIRECTION_RECEIPT.json` binds that record and distinguishes the
initial native relay from the centrally recorded human wording. Preserve old
summaries/hashes. Recreated inputs and new M3 checks carry their own identities,
candidates, commands and environments; they never impersonate originals.
Original recovery is low priority unless a concrete discrepancy makes it
necessary. No protected criterion, required gate or acceptance hold is waived.

Next, ROOT should freeze the actual guard source/test/record candidate and assign
a fresh independent reviewer. After repairs/backcheck and an explicit bounded
live-qualification grant, execute the planned low-memory qualification. Only
then grant a separately budgeted direct compile/probe. DESIGN's A0 preparation
and the named K0 source work can proceed under their own scopes while runtime
qualification remains open. No new DELIVERY child starts without ROOT's grant.

No live monitoring/guard/workload, process signal, compiler/model run, install,
download, system-setting change, Git/index mutation or old-packet edit was
performed by DELIVERY or this guard TASK. This return makes no engineering,
release, whole-deliverable readiness or dependency-satisfaction claim.
