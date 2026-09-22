"""D1 self-check of own packets against the r4_qa C4/C5 rules (read-only; does not write R4_QA.md)."""
import re, os, glob
R4 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CTX_PAT = re.compile(r"plans/|steers|SCA-APP-008|AgentRuns/APP_V3|APP_V3_|APPDEV_V3_NODE|CHIRALITY_V3_APP_ADOPTION|DONE_DECLARATION|done[- ]declaration|OWNER_DIRECTION|r2_r4q6_answer|owner'?s? (recorded )?answer", re.I)
HEAD = ["## What we found", "## Affected rows", "## Options", "## HELP_HUMAN recommendation (draft)", "## Who decides", "## On ruling", "## Risks, contested rows and dependencies"]
TAG = re.compile(r"\[(GOVERNING|CONTEXT|code|owner testimony|run finding)\]")
for p in ("P-01", "P-02", "P-03", "P-23", "P-24", "P-EX"):
    f = glob.glob(os.path.join(R4, "PACKETS", p + "_*.md"))[0]
    t = open(f, encoding="utf-8").read()
    probs = []
    for i, l in enumerate(t.splitlines(), 1):
        if "[GOVERNING]" in l and CTX_PAT.search(l): probs.append(f"ctx-on-gov:{i}")
        if len(TAG.findall(l)) > 1: probs.append(f"multitag:{i}")
    pos = [t.find(h) for h in HEAD]
    if any(x < 0 for x in pos) or pos != sorted(pos): probs.append("headings")
    m = re.search(r"## What we found\n(.*?)\n## ", t, re.S)
    for b in re.split(r"\n(?=- )", m.group(1).strip()):
        if b.startswith("- ") and not TAG.search(b): probs.append("untagged:" + b[:40])
    if re.search(r"/Users/|/private/tmp/|/tmp/claude", t): probs.append("abspath")
    if "<!-- COUNTS -->" not in t: probs.append("nocounts")
    body = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    print(p, os.path.basename(f), "words", len(body.split()), "problems", probs)
