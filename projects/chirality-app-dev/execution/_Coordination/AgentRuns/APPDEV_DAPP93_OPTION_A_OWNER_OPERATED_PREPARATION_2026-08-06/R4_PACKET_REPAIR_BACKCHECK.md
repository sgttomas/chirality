# R4 packet-repair exhaustive backcheck

Status: `MANAGER BACKCHECK COMPLETE — READY FOR R4 FREEZE`

Accepted audit basis:

- EVALUATION report SHA-256
  `9b4992a285e18040e2ef9ae2d6af4d34fabdb392277d606a587f82efe8d4f2a5`;
- EVALUATION handoff SHA-256
  `0b5607afa53151a1f730a3c53a899fa85d321270e820bf97d81435656c2849ff`;
- report coverage: 31/31 steps, 15/15 terminal-path classes, all 81 R3
  ledger rows, and 40/40 grouped evidence requirements;
- accepted findings: six class-A rows representing two root defects and 37
  incomplete class-B groups.

No runtime or dynamic fact was tested. This backcheck is static derivative
evidence only.

## Matrix A fan-in — every accepted branch/precondition row

| Accepted row(s) | R4 disposition | Result |
|---|---|---|
| A01-A04 | C1146 markers begin before C1067; C1149 form materializes after a valid C1070 or directly in returned after C1147. Pre-C1070, partial-C1070, and incomplete-baseline routes are distinct. | CLOSED |
| A05-A18 | Normal command prerequisites unchanged. Every post-first-C1079/pre-C196 failure routes C1147→C1146→C1148/C1149, applicable revalidated C1128/C1129, C1131-C1143, C1150-C1151. Neither C1144 nor C1130 is invoked. | CLOSED |
| A19-A22 | C196/C197 rows and exact bytes are untouched. Post-C196 same-PTY, one-signal, and absolute-bound rules remain unchanged. | CLOSED |
| A23-A25 | C1067 now preflights the returned path. Ordinary path remains literal C1145→C1144→C1130. A failed C1145 produces only a retained failure disposition; no alternate destination or illegal copy. | CLOSED |
| A26-A27 | C1128/C1129 require applicable evidence preservation and exact-PID revalidation on either legal pre-C196 or post-C196 path. | CLOSED |
| A28-A31 | C1131-C1141 remain mandatory only after a reconstruction write; C1142-C1143 also allow a recorded no-write/partial-root path. C1146/C1149 finalize, C1150 manifests, C1151 checks, and step 31 has one literal disposition. | CLOSED |
| A32 | The former step-5 jump to steps 25-28 is deleted. The literal replacement invokes C1147/C1146/C1148-C1149 and never C1144/C1130. | CLOSED |
| A33, A35, A36 | All other post-reconstruction/pre-C196 failures use the same legal alternative, with conditional exact-PID cleanup only after evidence preservation. | CLOSED |
| A34a | Before C1070, C1147 creates only returned; no fixed temp root is created/reused and C1131-C1143 are not invoked. | CLOSED |
| A34b | Partial C1070 uses preservation plus C1142-C1143 only after explicit no-write/partial-root disposition; C1131-C1141 are prohibited. | CLOSED |
| A34c | C1071-C1078 incomplete/mismatch is explicitly no reconstruction write; C1131-C1141 are prohibited. | CLOSED |
| A37-A39 | Existing post-C196 C197 and transcript paths remain legal; invalid runtime results are captured, never narratively repaired. | CLOSED |
| A40-A42 | C1145 occupancy, prohibited content, or preservation failure retains state and emits an explicit incomplete/no-return disposition; destructive cleanup and alternate destinations remain forbidden. | CLOSED |
| A43-A44 | PID cleanup remains conditional on live exact identity; rollback/proof failure still prohibits C1142 and complete handoff. | CLOSED |

Matrix-A count: every accepted A01-A44 row, including A34a-A34c, is
dispositioned above. No command is newly invoked where its stated prerequisite
cannot hold.

## Matrix B fan-in — every accepted evidence row

| Accepted row(s) | Enumerated R4 capture and return/inclusion | Result |
|---|---|---|
| B01-B08 | C1146 captures CONTROL bytes; C1149 materializes, completes, screens, returns, and hashes the writable derivative form. | CLOSED |
| B09-B13 | C1146 step/C-ID ranges preserve baseline, candidate, projection, archive, and overlay outputs; C1149 cites their ranges/hashes; C1150-C1151 manifest and verify inclusion. | CLOSED |
| B14-B17 | C1146 separately brackets C1105, C1106, C1107, and C1108 and preserves complete combined output plus exit disposition, including failures. C1151 requires each complete range/hash and forbids rerun. | CLOSED |
| B18-B21 | C1146 captures package hashes, plist identity, topology, and comparison output/exit; C1149/C1150/C1151 return and verify them. | CLOSED |
| B22 | The blank schema now contains 31 literal rows, numbered 1 through 31 exactly once; aggregate `1-30` is removed. | CLOSED |
| B23-B25 | Skips/deviations, helper/GUI identity, process bytes, and owner contact are captured in C1146 and finalized in C1149; raw conditional files use C1130 post-C196 or C1148 pre-C196. | CLOSED |
| B26, B29 | Existing C1144 LLDB transcript/hash remains unchanged on the ordinary post-C196 path; C1149 records `MISSING`/invalid on terminal exceptions. | CLOSED |
| B27-B28 | C1146 captures signal/time/exit and bounded process/socket/owner/GUI observations; C1149-C1151 return and bind them. | CLOSED |
| B30 | C1114/C1117 raw files return through unchanged post-C196 C1130 or mutually exclusive pre-C196 C1148; C1150 adds per-file size/hash/provenance/screen/inclusion. | CLOSED |
| B31-B35 | C1146 captures cleanup, rollback hashes, Git-status bytes, and absence results; C1149 records phase-specific dispositions; C1150-C1151 bind the returned proof. | CLOSED |
| B36 | C1150 enumerates every returned file with path, size, SHA-256, provenance, credential screen, and inclusion disposition, then hashes the manifest. | CLOSED |
| B37-B38 | C1149 requires retained-state reason, missing bytes, uncertainty, deviations, redactions, unsupported inferences, and owner attestation; `TBD` fails C1151. | CLOSED |
| B39 | Runtime propositions remain validly `UNKNOWN`; C1151 closes the upstream inclusion chain without creating a causal claim. | CLOSED |
| B40 | C1149 returns/hashes the completed form; C1150 manifests the exact directory; C1151 emits/hashes `PASS_COMPLETE` or `STOP_INCOMPLETE` before handoff. | CLOSED |

Matrix-B count: all 40 accepted grouped evidence rows are dispositioned; no
required byte/object lacks an enumerated capture plus return/inclusion or
explicit `MISSING`/retained-state failure disposition.

## Mechanical checks

- command table: 87 unique rows — C196, C197, and every C1067-C1151 row
  exactly once; no gap, duplicate, or extra row;
- new allocation: C1146-C1151 exactly six sequential rows;
- evidence schema: exactly 31 unique literal step rows, 1 through 31;
- forbidden old route: no `skip to steps 25-28` remains;
- pre-C196 route: C1147-C1148 explicitly invoke neither C1144 nor C1130;
- ordinary post-C196 order: C1145→C1144→C1130 remains explicit;
- unaffected prepared identities: reconstruction manifest, LLDB script, and
  static revalidation match R3 exactly;
- C196/C197: their ledger rows were outside every edit hunk and their command/
  input text remains the exact R3 text;
- no prepared object outside the six owner-authorized affected files changed;
- no runtime/evidence target was created and no command in the packet was
  executed.

Backcheck verdict: `PASS_STATIC_R4_REPAIR_CLOSED`.
