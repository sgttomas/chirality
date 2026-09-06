from pathlib import Path
import csv,collections
p=Path(__file__).parent
rows=list(csv.DictReader((p/"PACKAGE_RESIDUALS.csv").open()))
evidence={"DEL-03-01":[1,2],"DEL-03-02":list(range(1,15)),"DEL-03-03":[1,2],"DEL-03-04":[1],"DEL-03-05":[1],"DEL-03-06":[1]}
doc={"DEL-03-02":[16],"DEL-03-03":[4],"DEL-03-06":[4]}
output=[]
for r in rows:
 n=int(r["ResidualID"].rsplit("-",1)[1]);did=r["DeliverableID"]
 if n in evidence.get(did,[]):category="RECOMMENDED_EVIDENCE_CANDIDATE_CONDITIONAL_PRODUCTION";why="Accepted obligation has bounded UNKNOWN implementation/verification evidence; establish exact current evidence before any separately ruled missing-scope production. No absence finding."
 elif n in doc.get(did,[]):category="RECOMMENDED_NARROW_DOCUMENTARY_CANDIDATE";why="Independently substantiated current dependency-register paraphrase discrepancy; preserve historical authoring, D65 change lineage, frozen DAG evidence and PENDING statuses."
 else:category="HELD_OWNER_REVIEW_SCOPE_OR_CONTRACT_ROUTING";why="Owner/REVIEW/source interpretation or missing-contract boundary; not automatically executable Remaining and not an administrative mirror."
 output.append({"ResidualID":r["ResidualID"],"DeliverableID":did,"Classification":category,"Rationale":why,"ClaimIDs":r["ClaimIDs"],"Depends":r["Depends"],"ExactGate":r["ExactGate"],"Selectability":r["Selectability"]})
with (p/"RESIDUAL_RECOMMENDATIONS.csv").open("w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=output[0].keys(),lineterminator="\n");w.writeheader();w.writerows(output)
counts=collections.Counter(r["Classification"] for r in output)
text="# PKG-03 R4 decision candidates\n\nDerivative proposals only under D82; no exact Remaining application, production, lifecycle, source or authority repair is authorized. Base2be412ccea62bdc4bd96deb082c46d7a792076ea. Accepted D81 conventions and fresh independent verification govern selected rows. Raw proposals are not accepted obligations or work selection.\n\n"
text+="Selected raw proposals: "+str(len(rows))+"; classification counts: "+str(dict(counts))+". Every member ASSESSED_UNKNOWN; no warranted NONE. These counts reflect raw atomic groupings, not an authorization to create that number of product tasks.\n\n"
text+="Evidence candidates establish implementation and verification truth first. Conditional production is considered only after a positively established gap and an exact owner-ruled packet. Full-rebuild, delta, drift, parity, recovery and timing evidence remain distinct. Standing test obligations do not claim a test ran; finite evidence never proves an all-input or release guarantee.\n\n"
text+="Narrow documentary candidates concern only current-register evidence-field paraphrases independently contradicted by D65-repaired local Dependencies.csv. Dated OPEN/authoring and historical decomposition-basis paragraphs are preserved as provenance through fresh02/03 corrections. Ordinary currency is complete; no pointer sweep, source acceptance reversal, graph edit or status flip follows.\n\n"
text+="Held routes retain exact authority: full-rebuild coverage meaning; loop/feed and snapshot/baseline/producer interpretation; parity release-gating and explanation/closure; missing DEL03-05 contract boundary; owner timing-bound confirmation and declared REVIEW criteria. Options are locate exact already-accepted evidence, rule the narrow unresolved question, amend via the owning scope workflow, or explicitly defer. An agent cannot choose these by implementation. Dependency artifacts can be observed on the branch, while new owner acts must be shared-main observable.\n\n"
text+="Preserve D79/PRDv2.3 adopted-not-applied, TM022 deferred, TM023 dedicated held mapping without blanket downstream gate, source/Root/product fences and all current lifecycle states. No TM mirrors. R4 successor application packet must name exact carrier/status path, final text/gate/Depends, source/pre/post hashes, authorization and rollback, with post-repair backcheck; this report applies none.\n\n"
text+="## Exact selected proposal index\n\n"
for o,r in zip(output,rows):text+="- "+r["ResidualID"]+" — "+o["Classification"]+". "+r["ProposedText"]+" Depends: "+r["Depends"]+". Gate: "+r["ExactGate"]+"\n"
(p/"R4_DECISION_CANDIDATES.md").write_text(text)
