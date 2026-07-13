# WORKING-A1-PKG03 Preserved Source Literal Inventory

Disposition: `PRESERVED_SOURCE_LITERAL — NON-PORTABILITY-DEFECT`.

The exact accepted control inputs contain machine-specific checkout strings.
Across this package instance there are exactly 13 occurrences in 13
byte-identical copied control files:

- author workspaces: DEL-03-01 `_REFERENCES.md` (1), DEL-03-02
  `_REFERENCES.md` (1), DEL-03-03 `_REFERENCES.md` (1) and
  `_DEPENDENCIES.md` (1), DEL-03-04 `_REFERENCES.md` (1);
- verifier workspaces: DEL-03-01 `_REFERENCES.md` plus its exact
  `legacy_state` copy (2), DEL-03-02 `_REFERENCES.md` (1), DEL-03-03
  `_REFERENCES.md` and `_DEPENDENCIES.md` plus their exact
  `legacy_state` copies (4), DEL-03-04 `_REFERENCES.md` (1).

Every occurrence is accepted source/control provenance. Candidates, rendered
derivatives, mapping/parity/checklist/verdict evidence, terminal generated
metadata, manager records, and project-check postimages contain zero
checkout-root, machine-temp, or local-file URI strings. Exact child-level
inventories bind member/file detail. Normalizing a copied source/control byte
would violate the frozen manifest and is not authorized.

