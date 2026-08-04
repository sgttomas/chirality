# Candidate and acceptance validation plan

Status: `BLUEPRINT — POSITIVE CANDIDATE CASE HELD FOR POST-S2 BYTES`

## Deterministic validators

### Candidate packet

Command after instantiation:

```text
python3 packet_blueprint/validate_candidate_packet.py packet_candidate/
```

Required result: exit `0`, JSON `valid: true`, exact five content hashes, and
non-empty manifest SHA-256. Run twice and require byte-identical JSON after
normalizing only the invocation path if the path differs.

The validator checks exact membership, regular-file type, UTF-8/LF/terminal
newline, whitespace, placeholder absence, machine-path absence, fresh/not-
accepted markers, accepted Scope-of-Work and ruling bindings, compatibility
requirements, ten failure conditions, recovery invariants, exact sixteen-row
open-item mapping, gate boundary, sorted manifest format, and all file hashes.

`--content-only` validates the five frozen content files before manifest
creation. It does not produce or mutate a hash manifest.

### Owner acceptance

Command only after an owner token is recorded:

```text
python3 packet_blueprint/validate_owner_acceptance.py packet_candidate/ packet_acceptance/PACKET_OWNER_ACCEPTANCE.md
```

Required result: exit `0`, JSON `valid: true`, exactly one acceptance token,
and token manifest SHA-256 equal to the exact candidate manifest SHA-256.

## Required negative cases

Before presentation, run isolated copies of the post-S2 candidate and prove
each case fails without mutating the canonical candidate:

1. remove one file;
2. add an extra file;
3. rename one file;
4. alter one content byte without updating manifest;
5. change manifest digest to uppercase or use one space;
6. add manifest self-entry;
7. leave one `{{S2_*}}` placeholder;
8. introduce CRLF, trailing whitespace, surplus EOF blank line, symlink, or
   machine-absolute path;
9. delete/duplicate/reorder an OPEN_ITEMS row or alter its source hash;
10. remove fresh/non-reconstruction/not-accepted language;
11. insert an owner token into `OWNER_GATE.md`;
12. record an external acceptance token for another manifest SHA;
13. record zero or two owner acceptance tokens;
14. edit a candidate file after owner acceptance;
15. copy a non-byte-identical candidate into live `accepted_inputs/`.

Each must return nonzero with a specific issue. Negative fixtures remain under
temporary test storage and are not accepted inputs or run evidence unless the
later candidate activation explicitly records them.

## Blueprint-time validation

Before S2, only the following are lawful:

- Python syntax compilation of both validators;
- JSON/CSV/Markdown structural inspection of blueprint files;
- candidate-whitespace validation over the blueprint directory;
- exact template-name and placeholder-vocabulary inspection; and
- verification that neither live nor candidate packet directories exist.

A positive candidate validation cannot occur before S2 because the allowed
S2 values do not yet exist. Claiming a positive result now would be false.
