#!/usr/bin/env python3
"""RV119 (ADDENDUM_01 copy: an optional last argument gives the rev to read the earlier form from) publication and host screen over the text PR #1114 adds (RV117's method and patterns, plus the
host-name screen of RR "RV117 passes #1111; ...", ruling 4, as widened by E-16).
Added files: every line (a .gz file is decompressed first). Modified files: '+' lines of `git diff M H`.
The machine's names are read at run time (hostname, scutil LocalHostName and ComputerName); the earlier
form named in RR and the strict pattern of B1_COMMON are assembled at run time, so this file carries none
of them literally. Output text is sanitized: host data is written <host>, <host-short>, <computer-name>,
<earlier-host> or <model-form> (the laptop-model form);
the dot-local suffix is written [.]local; home roots are written with a hyphen. The earlier form is read from
RR at H.
Usage: publication_scan.py <num_repo> <M> <H> <out_dir>"""
import re, subprocess, sys, os, collections, gzip
repo, M, H, out = sys.argv[1:5]
SRC = sys.argv[5] if len(sys.argv) > 5 else H   # RV119 ADDENDUM_01: the rev whose RR line names the earlier form (the reviewed head; E-18 reworded it at the new head)
def git(*a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, check=True).stdout
def sh(*a):
    r = subprocess.run(list(a), capture_output=True); return r.stdout.decode().strip() if r.returncode == 0 else ""
net = sh("hostname")                       # the network name
short = sh("scutil", "--get", "LocalHostName")
comp = sh("scutil", "--get", "ComputerName")
T3_ = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
# the earlier form, read from RR at H (E-16's "Screen widened" line names it), so this file does not carry it
earlier = re.search(r"beside `([^`]+)`", next(l for l in git("show", f"{SRC}:{T3_}ROOT_RULINGS_V1.md").decode().splitlines() if l.startswith("**Screen widened (E-16"))).group(1)
edom = earlier.split(".", 1)[1]
mb = bytes.fromhex("6d6163626f6f6b").decode()   # the laptop-model form, hex-encoded so this file does not carry it
ns = git("diff", "--no-renames", "--name-status", M, H).decode().splitlines()
units = []
for row in ns:
    st, path = row.split("\t", 1)
    if st == "A":
        raw = git("show", f"{H}:{path}")
        if path.endswith(".gz"): raw = gzip.decompress(raw)
        data = raw.decode("utf-8", "replace")
        for i, l in enumerate(data.splitlines(), 1): units.append((path, i, l))
    elif st == "M":
        d = git("diff", "-U0", M, H, "--", path).decode("utf-8", "replace")
        ln = 0
        for l in d.splitlines():
            m = re.match(r"@@ -\S+ \+(\d+)", l)
            if m: ln = int(m.group(1)); continue
            if l.startswith("+") and not l.startswith("+++"):
                units.append((path, ln, l[1:])); ln += 1
home = "/" + "Users" + "/"
pats = {
 # credentials
 "ghp_": r"ghp_", "gho_": r"gho_", "ghs_/ghu_/ghr_": r"gh[sur]_[A-Za-z0-9]{8,}", "github_pat_": r"github_pat_",
 "sk- (any)": r"sk-", "sk- token-shaped": r"\bsk-[A-Za-z0-9_-]{16,}", "AKIA": r"AKIA[0-9A-Z]{8,}|AKIA",
 "PRIVATE KEY": r"BEGIN .*PRIVATE KEY", "password": r"(?i)password", "secret": r"(?i)secret",
 "token=": r"(?i)token=", "Authorization:": r"(?i)Authorization:", "Bearer": r"Bearer [A-Za-z0-9._-]{12,}",
 "slack token": r"xox[abprs]-", "cred vars": r"GH_TOKEN|GITHUB_TOKEN|ANTHROPIC_API_KEY|OPENAI_API_KEY|AWS_SECRET|SSH_AUTH_SOCK|NPM_TOKEN",
 "api_key": r"(?i)api[_-]?key",
 # personal data
 "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "owner name": r"(?i)ryan|tufts",
 # whole-host data
 "Applications": "/" + "Applications" + "/", "apps": r"(?i)\b(Microsoft Teams|Parallels|ChatGPT|Claude\.app|Messages\.app|Mail\.app|Slack|Google Chrome|Safari|Spotify|Dropbox|Docker Desktop|Zoom\.us|1Password|Discord|WhatsApp|Firefox|Arc\.app|Cursor\.app|Visual Studio Code)\b",
 "session ids": r"--resume|--session-id|session_id|sessionId|user-data-dir|conversation[_-]?id",
 "uuid": r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
 "toolcall ids": r"\btoolu_[A-Za-z0-9]+|\bmsg_[A-Za-z0-9]{10,}|call_[A-Za-z0-9]{16,}",
 "transcripts": r"\.claude/projects/|\.jsonl\b.*transcript|/\.codex/sessions|rollout-",
 "system paths": r"/System/Library|/usr/libexec|launchd|" + "/" + "private/var/|" + "/" + "var/folders/",
 "ps headers": r"\bPID\s+(TTY|PPID|USER)|\bUSER\s+PID\b|%CPU|%MEM",
 "ps/pgrep/lsof": r"\bps (aux|-e|-ax|-A)|\bpgrep\b|\blsof\b|\btop -l",
 "home path": re.escape(home), "tilde home": "~" + "/" + r"(dev|Library|Documents|Desktop)",
 # the strict pattern of B1_COMMON, assembled at run time
 "strict": "~" + "/" + "|" + home + "|" + "/" + "private" + "/" + r"|\." + "claude" + "/" + "worktrees" + "|" + "swbpipe" + "-control-layer",
 # the host screen (ruling 4 and E-16)
 "host: network name": "(?i)" + re.escape(net) if net else r"(?!x)x",
 "host: local host name": "(?i)" + re.escape(short) if short else r"(?!x)x",
 "host: computer name": "(?i)" + re.escape(comp) if comp else r"(?!x)x",
 "host: model form": "(?i)" + mb,
 "host: earlier form": "(?i)" + re.escape(earlier) + "|" + re.escape(edom),
 "dot-local": r"\." + "lo" + r"cal\b",
 "junit hostname attr": r"hostname\s*=",
}
owner_emails = {git("log", "-1", "--format=%ae", H).decode().strip(), git("log", "-1", "--format=%ce", H).decode().strip()}
def sanitize(t):
    for e in owner_emails:
        if e: t = t.replace(e, "<owner-email>")
    for v, tag in ((net, "<host>"), (short, "<host-short>"), (comp, "<computer-name>")):
        if v: t = re.sub(re.escape(v), tag, t, flags=re.I)
    t = re.sub(re.escape(earlier), "<earlier-host>", t, flags=re.I)
    t = re.sub(re.escape(edom), "<earlier-domain>", t, flags=re.I)
    t = re.sub(mb + r"[\w -]*", "<model-form>", t, flags=re.I)
    t = re.sub(r"\." + "lo" + r"cal\b", "[.]local", t)
    # split host forms (quotes, brackets or joiners inside a name), the junit attribute and app roots
    J = r"[\W_]{0,6}"
    t = re.sub("(?i)" + J.join(mb[:3]) + J + mb[3:], "<model-form-split>", t)
    t = re.sub("(?i)" + J.join(re.escape(x) for x in earlier.split(".")), "<earlier-host-split>", t)
    t = re.sub("(?i)" + J.join(re.escape(x) for x in earlier.split(".")[1:]), "<earlier-domain-split>", t)
    t = re.sub("(?i)ry" + "ans", "<first-name-s>", t)
    t = t.replace("host" + "name=", "host-name=").replace("/" + "Applications" + "/", "/Appli-cations/")
    t = t.replace(home, "/U-sers/").replace("/" + "private" + "/", "/pri-vate/").replace("~" + "/", "~-/")
    t = t.replace("." + "claude" + "/" + "worktrees", ".claude/work-trees").replace("swbpipe" + "-control-layer", "swbpipe-c-l")
    return t
cre = {k: re.compile(v) for k, v in pats.items()}
hits = collections.defaultdict(list)
for path, ln, txt in units:
    for k, c in cre.items():
        if c.search(txt): hits[k].append((path, ln, txt.strip()[:240]))
os.makedirs(out, exist_ok=True)
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
def short_p(p): return p.replace(T3, "T3/").replace("projects/chirality-piping/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/", "WG-dir/")
with open(os.path.join(out, "publication_scan_summary.txt"), "w") as f:
    f.write(f"M={M}\nH={H}\nchanged paths: {len(ns)}\nlines scanned: {len(units)}\n")
    f.write(f"host names read at run time: network name {len(net)} chars, local host name {len(short)} chars, computer name {len(comp)} chars\n")
    for k in pats:
        h = hits.get(k, [])
        f.write(f"{k}\t{len(h)} hits\t{len({p for p, _, _ in h})} files\n")
with open(os.path.join(out, "publication_hits.tsv"), "w") as f:
    f.write("pattern\tpath\tline\ttext (sanitized)\n")
    for k in pats:
        for p, ln, t in hits.get(k, []):
            f.write(f"{k}\t{short_p(p)}\t{ln}\t{sanitize(t)}\n")
print(open(os.path.join(out, "publication_scan_summary.txt")).read())
