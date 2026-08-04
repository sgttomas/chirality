# N4 terminal return — recovery specification integration

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Runtime identity: `/root/w1_del0206/n4_w6`
- Parent runtime identity: `/root/w1_del0206`
- Form: fresh bounded ephemeral Agent 2 generalist; sole integration writer
- Date: `2026-08-03`
- Attempt: `3`, governed by `BRIEF_AMENDMENT_2.md` SHA-256 `3f58f9d7c741a3ba4abf08e7822963acbc8c17d35af5b8150c7979c6bac4587e`
- Verdict: `ADMIT_FOR_FRESH_N5_RECHECK`

## Result

Accepted N0-N3 fan-in and the accepted Scope of Work were integrated into an
exact planning-only recovery specification, an explicit compatibility
no-change-or-delta disposition candidate, a degraded-mode delta candidate, a
complete open-item/finding map, and a bounded later implementation sequence.
Attempt 2 disposes only N5-F01: the degraded-mode delta now binds accepted base
candidate SHA-256 `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917`
and contains exactly ten independent required-condition rows with all required
columns. The accepted base bytes were not read, reproduced, weakened, or
replaced. Attempt 3 disposes only N5-R2-F01 through the exact correction to
`D1/D6/TBD-016`; it makes no other semantic or matrix change.
The result preserves fact/candidate separation and makes no present-byte,
execution, evidence-pass, semantic-adoption, implementation, lifecycle,
release, closure, or reliance claim.

## Output identities

| Output | SHA-256 |
|---|---|
| `integration/RECOVERY_SPEC_CANDIDATE.md` | `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7` |
| `integration/COMPATIBILITY_DISPOSITION_CANDIDATE.md` | `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1` |
| `integration/DEGRADED_MODE_DELTA_CANDIDATE.md` | `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b` |
| `integration/OPEN_ITEM_MAP.md` | `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf` |
| `integration/IMPLEMENTATION_PLAN_CANDIDATE.md` | `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9` |
| `integration/N4_SELF_CHECK.md` | `92cfd5b00f463056cfa05df614df55ec31ea4395a849c005656753498ace3179` |

The SHA-256 of this return is intentionally reported externally after the file
is closed, avoiding a self-referential manifest.

## Source coverage

- Governing N4 brief and sealed wrapper: `2/2`, read in full and hash-checked.
- Accepted N0 outputs: `2/2`, read in full; JSON parsed.
- Accepted N1 outputs: `2/2`, read in full.
- Accepted N2 outputs: `2/2`, read in full.
- Accepted N3 outputs: `2/2`, read in full.
- Accepted Scope of Work: `1/1`, read in full and hash-checked.
- Attempt-2 amendment and manager-relayed N5 finding: `2/2`, read in full and
  hash-checked.
- Attempt-3 amendment carrying manager-relayed N5-R2-F01: `1/1`, read in full
  and hash-checked.
- Total declared inputs across three attempts: `14/14`; additional read
  request: none. The accepted base candidate bytes and N5-R2 capture were not
  read in attempt 3.

Exact input identities are recorded in `N4_SELF_CHECK.md`.

## Findings and held decisions

New N4 finding: none. Accepted N5-F01 is remediated within the existing N4
scope and returned for fresh N5 recheck; N4 does not purport to close or accept
the finding on N5's behalf. Accepted N5-R2-F01 received the exact bounded token
correction. Exhaustive scanning of all seven outputs finds zero decision
identifiers numerically greater than D9; only D1-D9 are used as decisions and
TBD-016 remains an open item.

Carried findings remain intact: N1-F01 through N1-F08, N2-F-001, and N3-F01
through N3-F07. D1 through D9 and all sixteen TBD/OD6 items remain unresolved.
N4 proposes `DELTA_REQUIRED_IF_RECOVERY_SPEC_IS_ADOPTED` but does not choose or
apply an identity. Root CLI and App remain `AFFECTED`; Piping and Tier-0 remain
`NOT_AFFECTED`; PEC remains `UNRESOLVED` with no work, dependency, or closure
veto. All N3 executable evidence remains `DESIGNED_NOT_EXECUTED`.

## Self-check

`PASS_ATTEMPT_3`: exact requirements, affected surfaces, P0-P9 change sequence,
fact/candidate separation, D1-D9 preservation, all accepted findings, PEC
boundary, REQ-027/035/052, text hygiene, hard stops, tool containment, and
write containment were checked. The amended matrix has exactly ten rows and
nine columns: condition, boundary, candidate required behavior, recovery,
exact class/open item, retry, redaction/evidence, positive verification, and
negative/adversarial verification. N4 recommends fresh read-only N5
adversarial recheck; the recommendation does not release or dispatch N5.

## Tool-use statement

- Used non-shell Node file reads, SHA-256 hashing, text inspection, and JSON
  parsing through the Node REPL tool.
- Attempt 2 read only the amendment, manager-relayed N5 finding, and existing
  N4 outputs, and used `apply_patch` only for the three exact amended targets.
- Attempt 3 read only `BRIEF_AMENDMENT_2.md` and existing N4 outputs, and used
  `apply_patch` only for the same three exact amended targets.
- Bash/shell, network, executable checks/tests, runtime execution,
  implementation tools, delegation, Git, and foreign writes: not used.

## Write containment

The original seven-file membership remains exact. Attempt-3 allowed and actual
writes are identical:

1. `integration/DEGRADED_MODE_DELTA_CANDIDATE.md`
2. `integration/N4_SELF_CHECK.md`
3. `integration/N4_RETURN.md`

The following four files remain byte-identical to attempt 1:

| Preserved file | Pre/post SHA-256 |
|---|---|
| `integration/RECOVERY_SPEC_CANDIDATE.md` | `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7` |
| `integration/COMPATIBILITY_DISPOSITION_CANDIDATE.md` | `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1` |
| `integration/OPEN_ITEM_MAP.md` | `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf` |
| `integration/IMPLEMENTATION_PLAN_CANDIDATE.md` | `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9` |

Attempt-3 changed-file identities before and after correction are:

| Changed file | Pre SHA-256 | Post SHA-256 |
|---|---|---|
| `integration/DEGRADED_MODE_DELTA_CANDIDATE.md` | `ac7a3e50406ca7a46ca5a8b91af145f1c5ff95028fe7a9d8ff23d7ed5847a1cd` | `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b` |
| `integration/N4_SELF_CHECK.md` | `3587c2f2e5ff9579ae8c3ae42469d68df3c61041d388db721c0d9146c4bd0cf6` | `92cfd5b00f463056cfa05df614df55ec31ea4395a849c005656753498ace3179` |
| `integration/N4_RETURN.md` | `d16e409b41577113d38f4bcae630618730fcd1cbfbef5cec800dc3b6d031892b` | reported externally after file closure |

No runtime, client, project, profile/check, dependency, S1,
SCA/decomposition/PRD, lifecycle, release, reliance, Task Management, Git, or
foreign-loop write or act was performed.

## Next owner

WORKING_ITEMS must validate and accept this attempt-3 return before any fresh
N5 dispatch or graph transition. N5, if released by the manager, must be fresh
and read-only; it may report findings but must not repair these outputs.
