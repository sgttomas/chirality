# PKG-01 Preserved Source Literal Inventory

Disposition: PRESERVED_SOURCE_LITERAL.

These checkout-root strings already exist in accepted source/control bytes.
They are not new path authority. Exact copied inputs and marker-bound verbatim
candidate/render text must not be normalized because doing so breaks source
identity or conversion parity. Generated metadata, run records, returns,
statuses, checks, and manifests are portable.

| Member | Source binding | Marker binding | Candidate/render occurrence | Control-only occurrences |
|---|---|---|---:|---:|
| DEL-01-01 | Datasheet.md line 63, SHA-256 0cf37c2b83e3d2295390a6f89d0e0b54e653499c28e4d88dd1a1dedfc34cf870 | CLM-006, Datasheet lines 53–64 | 4 across author workspace candidate, package candidate, and two author renders; verifier reproduces the same marker-bound class | 4 across _REFERENCES.md, _DEPENDENCIES.md twice, and Dependencies.csv |
| DEL-01-02 | no production-source literal; exact control bytes only | not applicable | 0 | 2 across _DEPENDENCIES.md and Dependencies.csv |
| DEL-01-03 | Datasheet.md line 69, SHA-256 ff00ec279937b42d6a86999dca8968c6488d019b67f63ec1ca1bbda0c9b813dd | CLM-006, Datasheet lines 59–69 | 4 across author workspace candidate, package candidate, and two author renders; verifier reproduces the same marker-bound class | 3 across _REFERENCES.md and _DEPENDENCIES.md twice |
| DEL-01-04 | Datasheet.md line 80, SHA-256 c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd | CLM-007, Datasheet lines 70–80 | 4 across author workspace candidate, package candidate, and two author renders; verifier reproduces the same marker-bound class | 1 in _REFERENCES.md |

The inventory is carried to RECONCILIATION. It does not waive portability for
generated evidence and does not itself block format migration.
