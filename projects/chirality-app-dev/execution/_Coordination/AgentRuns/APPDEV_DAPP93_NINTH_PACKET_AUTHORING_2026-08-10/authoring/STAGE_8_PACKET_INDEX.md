# Stage 8 — assembled packet index and author checks

Status: `AUTHOR CANDIDATE COMPLETE — MANAGER VALIDATION AND FREEZE REQUIRED`

## Five-file packet

| Exact packet file | SHA-256 |
|---|---|
| `DAPP93_NINTH_EXACT_EXECUTION_PACKET.md` | `ffab8340831f1993958a78330accc6f9b2c0edf05cf198a52fd60b80a355374b` |
| `DAPP93_NINTH_LLDB_COMMAND_SCRIPT.txt` | `af95e5eef8c9eaaa9a61e08143b9ae905dbf482307827bb9b278c84932e10344` |
| `DAPP93_NINTH_EVIDENCE_RETURN_TEMPLATE.md` | `527a484288cb1bb10173222477fd8df260512d07b2bc92acd0256c81d940c153` |
| `TWO_TIER_PROBE_LEDGER.csv` | `b006318e9f055f10d8e6ff0aa11ca590b01fe19bf3b6640d01b0749aef4af363` |
| `PACKET_INDEX.md` | `73cc3b5dbc48a34446da00cddebbe585c2b0bf267d46dbc63803dd44e1544582` |

The packet root identity candidate is the `PACKET_INDEX.md` SHA-256
`73cc3b5dbc48a34446da00cddebbe585c2b0bf267d46dbc63803dd44e1544582`.
That file binds the other four exact payload identities. The manager must
independently re-hash all five and freeze all bytes before this identity can be
presented as the final packet identity.

## Author checks

- Cleared semantic ledger identity:
  `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.
- Fresh alignment: exactly 80 data rows labelled contiguously `R001` through
  `R080`; every row has a nonempty packet disposition and no row is uncovered.
- Minimal tool surface: fifteen retained candidates and two explicit removals;
  npm/node and the full build/overlay/dependency chain are absent.
- Restricted tool-chain probes: all neutral forms passed with exit `0` except
  `/bin/ps`.
- `/bin/ps` restricted probe: exact form denied by sandbox with exit `127`,
  stderr `operation not permitted`, no process row; binary is readable and
  pinned; trace necessity is explicit; tier is `OWNER_PREFLIGHT`.
- Step 0: exact owner command pin expected exit/output shape evidence fields
  and stop-unexecuted route are the first runbook stage.
- Exact awk content and timing programs: neutral scratch inputs returned exit
  `0`; the elapsed program printed `20`.
- Debugger chain: pinned `/usr/bin/xcrun` to exact Xcode LLDB; neutral version
  invocation exit `0`; operative attach and internal target forms are
  `REVIEWED_NOT_EXECUTED`.
- Subject launch: operative and not run; separately prepared subject is an
  exact pre-run hard gate at SHA-256
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
- Historical-identity scan: F03 returned exit `1` and zero stdout on every
  authoring stage packet file and scratch record present before Stage 8.
- Packet hashes: F02 returned exit `0` with one digest row for each of the five
  packet files.
- Probe scratch disclosure: the exact restricted F09 invocation created
  contained transient tool cache bytes beneath the frozen scratch HOME. They
  are preserved untouched for manager fan-in and are not packet bytes.
- No packet command helper runtime LLDB attach signal Security mutation GUI
  action product mutation Git receipt lifecycle or later lineage action ran.

## Required manager continuation

Independently validate the 80-row mapping every command form and tier all
chains/pins the Step-0 owner surface exact packet hashes and zero historical
identities. Re-execute every safe probe in the same restricted environment.
If accepted freeze every packet byte dispatch one fresh read-only verifier over
both tiers and stop at the exact packet-hash approval gate. The author grants no
execution authority.
