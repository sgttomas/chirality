# Coordination Notice 001 — Preserved Source Literals

Status: RECORD AND ROUTE TO HELP_HUMAN / RECONCILIATION

Claim status: FACT. DEL-01-01, DEL-01-03, and DEL-01-04 contain an accepted
legacy Datasheet reference with a checkout-root literal. The deterministic
converter preserves each inside a source-marker range. DEL-01-02 contains the
literal only in exact control inputs. Normalizing production content would
break source parity and is not authorized.

Parent disposition: PRESERVED_SOURCE_LITERAL. Exact source/hash/line and
candidate marker bindings are frozen in PRESERVED_SOURCE_LITERAL_INVENTORY.md.
Generated evidence remains portable. No candidate, source, status, lifecycle,
scope, authority, risk, or acceptance change is requested.

Affected downstream owner: RECONCILIATION must retain the inventory during
fan-in and distinguish marker-bound legacy text from generated path authority.
Blocking posture: non-blocking when the inventory and zero-generated-prefix
gates pass.

## RECON-A1-F R2 disposition

RECON-A1-F found one unclassified generated workspace_root in each accepted
project-check JSON. A1-PKG01-CHECK-EVIDENCE-PORT-R2-001 routed exact repair to
this manager. CHECK_NORMALIZATION_R2_MANIFEST.tsv and
CHECK_NORMALIZATION_R2_CHECKS.md prove one field-only substitution per JSON,
exact reverse hashes, semantic equivalence, and all-six-PASS preservation.
The historical R1 normalization record remains immutable intermediate chain
evidence. RECON-A1-F must rerun against the updated package bindings.
