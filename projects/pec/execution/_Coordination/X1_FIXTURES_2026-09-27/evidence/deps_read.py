import csv, glob, sys
rows = []
for f in sorted(glob.glob("projects/pec/execution/PKG-*/1_Working/DEL-*/Dependencies.csv")):
    for r in csv.DictReader(open(f, newline="", encoding="utf-8")):
        r["_file"] = f; rows.append(r)
X1 = {"DEL-02-03", "DEL-02-08", "DEL-02-09"}
named = {"DEP-02-03-003","DEP-02-08-003","DEP-02-09-003","DEP-03-01-010","DEP-03-01-015","DEP-03-01-016","DEP-04-05-003","DEP-10-13-009","DEP-10-13-013","DEP-10-13-014"}
print("## Named rows (proposal add-on L / row 1)")
for r in rows:
    if r["DependencyID"] in named:
        print(f'{r["DependencyID"]} from={r["FromDeliverableID"]} type={r["DependencyType"]} target={r["TargetDeliverableID"]} req={r["RequiredMaturity"]} sat={r["SatisfactionStatus"]} status={r["Status"]}')
print("found", sum(r["DependencyID"] in named for r in rows), "of", len(named))
print("## Every ACTIVE PREREQUISITE row FROM the three X1 deliverables")
for r in rows:
    if r["FromDeliverableID"] in X1 and r["Status"] == "ACTIVE" and r["DependencyType"] == "PREREQUISITE":
        print(f'{r["DependencyID"]} target={r["TargetDeliverableID"] or r["TargetRefID"]} ({r["TargetName"][:50]}) sat={r["SatisfactionStatus"]} req={r["RequiredMaturity"]}')
print("## Every ACTIVE PREREQUISITE row TARGETING the three X1 deliverables")
for r in rows:
    if r["TargetDeliverableID"] in X1 and r["Status"] == "ACTIVE" and r["DependencyType"] == "PREREQUISITE":
        print(f'{r["DependencyID"]} from={r["FromDeliverableID"]} target={r["TargetDeliverableID"]} req={r["RequiredMaturity"]} sat={r["SatisfactionStatus"]}')
