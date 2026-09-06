# Manager audit notes

Original five worker ledgers were structurally valid and source unchanged but not semantically ready: independent verifier sealed F001 evidence-proposal dependency defect and F002 coverage-accounting defect. Original rows/manifests remain immutable. Fresh correction chains and independent backcheck determine selected reports.

Manager initially stated all five evidence residual Depends were NONE without row-by-row corroboration. This was wrong for DEL07-03; the manager corrected the statement to HELP_HUMAN immediately on F001 and will publish full item-by-item classification/Depends evidence at final fan-in. Structural checks alone were insufficient for the semantic conclusion.

A manager parser initially did not strip spaces around semicolon-separated claim backlinks and reported false reciprocity errors in DEL07-02. Parser was corrected to normalize separator whitespace; original CSV bytes were unchanged and passed. One manager import produced validator bytecode under this permitted evidence root; the exact manager-generated cache file was removed immediately. No worker, source, frozen or foreign file changed; subsequent module runs use PYTHONDONTWRITEBYTECODE=1.
