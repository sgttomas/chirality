#!/usr/bin/env python3
"""Adapt the accepted PKG-16 terminal binder to frozen PKG-17 B1."""
from pathlib import Path

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG16/children/AUTHOR-B1/finalize_author_pkg16.py"
source = template.read_text(encoding="utf-8")
source = source.replace(
    '\nfor forbidden in ("WORKING-P4-PKG15"',
    '\nsource = source.replace(\'pkg00[0]["active_edges_to_pkg00"] == "28"\', \'pkg00[0]["active_edges_to_pkg00"] == "66"\')\nsource = source.replace(\'if row["package"] == "PKG-17":\\n            deps.append\', \'if row["deliverable_id"] in {"DEL-17-01", "DEL-17-02", "DEL-17-03", "DEL-17-04", "DEL-17-05"}:\\n            deps.append\')\nsource = source.replace(\'if row["package"] == "PKG-17"]\\nassert len(validator) == 4\', \'if row["deliverable_id"] in {"DEL-17-01", "DEL-17-02", "DEL-17-03", "DEL-17-04", "DEL-17-05"}]\\nassert len(validator) == 5\')\nfor forbidden in ("WORKING-P4-PKG15"',
)
replacements = {
    "WORKING-P4-PKG16": "WORKING-P4-PKG17",
    "candidates/W_P4/PIP-PKG16": "candidates/W_P4/PIP-PKG17",
    "W_P4/PIP-PKG16": "W_P4/PIP-PKG17",
    "DEL-16-": "DEL-17-",
    "PKG-16": "PKG-17",
    "1097": "1528",
    "1,097": "1,528",
    "106": "166",
}
for old, new in replacements.items():
    source = source.replace(old, new)

# PKG-17 B1 returns to the accepted five-member batch shape while retaining
# the P4 no-HTML posture inherited from PKG-16.
source = source.replace("range(1,5)", "range(1,6)")
source = source.replace('"members_complete":4', '"members_complete":5')
source = source.replace('"members_expected":4', '"members_expected":5')
source = source.replace('"replacement_rows":20', '"replacement_rows":25')
source = source.replace('"inverse_rows":20', '"inverse_rows":25')
source = source.replace('"simulations_passed":4', '"simulations_passed":5')
source = source.replace('"negative_probes_passed":28', '"negative_probes_passed":35')
source = source.replace("Four evidence", "Five evidence")
source = source.replace("four distinct", "five distinct")
source = source.replace("four clean", "five clean")
source = source.replace("four external", "five external")
source = source.replace("`4/4`", "`5/5`")
source = source.replace("4/4 members", "5/5 members")
source = source.replace("4/4 terminal", "5/5 terminal")
source = source.replace("exact `20` replacement and `20` inverse", "exact `25` replacement and `25` inverse")
source = source.replace("20 replacement rows", "25 replacement rows")
source = source.replace("20 inverse rows", "25 inverse rows")
source = source.replace("four apply/target/rollback", "five apply/target/rollback")
source = source.replace("four successful apply/target/rollback", "five successful apply/target/rollback")
source = source.replace("and four simulations", "and five simulations")
source = source.replace("each of four members", "each of five members")
source = source.replace("for each of four members", "for each of five members")
source = source.replace("12/12 expected files", "15/15 expected files")
source = source.replace("assert len(cent)==12", "assert len(cent)==15")
source = source.replace("28 fail-closed negative probes", "35 fail-closed negative probes")
source = source.replace('"five members"):', '"four members"):')

for forbidden in ("WORKING-P4-PKG16", "PIP-PKG16", "DEL-16-", "PKG-16", "1097", "1,097", "106 mappings", "four members", "4/4", "20 replacement", "20 inverse", "12/12"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
