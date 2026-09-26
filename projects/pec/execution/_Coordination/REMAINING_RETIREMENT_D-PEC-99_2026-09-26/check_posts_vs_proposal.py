#!/usr/bin/env python3
"""Compare generator POST lines with the D-PEC-99 proposal's tabled postimages (read-only).
Usage: python3 check_posts_vs_proposal.py <generator output> <proposal.md>"""
import re, sys
gen, prop = sys.argv[1], sys.argv[2]
posts = [l.split()[1:3] for l in open(gen, encoding='utf-8') if l.startswith('POST ')]
text = open(prop, encoding='utf-8').read()
rows = {}
for line in text.splitlines():
    m = re.match(r'\| (DEL-\d\d-\d\d) \|.*\| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|$', line)
    if m:
        rows[m.group(1)] = m.group(3)
    m = re.match(r'\| `([^`]+)` \| (?:modify|create).*\| `([0-9a-f]{64})` \|$', line)
    if m:
        rows[m.group(1)] = m.group(2)
bad = 0
for h, rel in posts:
    key = None
    m = re.search(r'/(DEL-\d\d-\d\d)_[^/]*/_STATUS\.md$', rel)
    if m:
        key = m.group(1)
    else:
        for k in rows:
            if not k.startswith('DEL-'):
                pat = re.escape(k).replace(re.escape('{N}'), 'D-PEC-99').replace(re.escape('{DC}'), r'\d{8}').replace(re.escape('{D}'), r'\d{4}-\d{2}-\d{2}')
                if re.fullmatch(r'(?:projects/pec/)?' + pat, rel) or re.fullmatch(pat, rel):
                    key = k
    exp = rows.get(key)
    ok = exp == h
    bad += not ok
    print('%s %s %s' % ('MATCH' if ok else 'MISMATCH', rel, h if ok else '%s expected %s' % (h, exp)))
print('posts=%d tabled=%d mismatches=%d' % (len(posts), len(rows), bad))
sys.exit(1 if bad or len(posts) != 62 else 0)
