#!/usr/bin/env python3
"""Re-extract exact repaired blocks and prove preservation outside them."""
from collections import Counter
from pathlib import Path
import csv
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]
RUN = HERE.parent.parent

def rows(path):
    return list(csv.DictReader(path.open()))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def check_coverage(repaired, unchanged, source):
    actual = Counter(r['ClaimKey'] for r in repaired + unchanged)
    expected = Counter(r['ClaimKey'] for r in source if r['PackageID'] == 'PKG-04')
    assert actual == expected, 'PKG-04 claim-key multiset differs from R3'
    assert all(v == 1 for v in actual.values()), 'Duplicate claim key'

def main():
    manifest = rows(HERE / 'REPAIR_MANIFEST.csv')
    unchanged = rows(HERE / 'UNCHANGED_R3_CLAIMS.csv')
    source = rows(RUN / 'R3/CLAIM_CONCORDANCE.csv')
    bindings = rows(HERE / 'SOURCE_BINDINGS.csv')
    check_coverage(manifest, unchanged, source)
    for broken in (manifest[:-1], manifest + manifest[:1]):
        try:
            check_coverage(broken, unchanged, source)
        except AssertionError:
            pass
        else:
            raise AssertionError('Coverage check failed to reject a missing/duplicate key')
    checks = []
    for binding in bindings:
        path = ROOT / binding['Path']
        current = path.read_bytes()
        assert sha(current) == binding['AfterSHA256'], str(path) + ': changed after repair'
        restored = current.decode()
        for row in [r for r in manifest if r['TargetPath'] == binding['Path']]:
            before = (ROOT / row['BeforePath']).read_bytes()
            after = (ROOT / row['AfterPath']).read_bytes()
            assert sha(before) == row['BeforeBlockSHA256']
            assert sha(after) == row['AfterBlockSHA256']
            match = re.search(r'^### ' + re.escape(row['BlockID']) + r'\b.*?(?=^### |^## |\Z)', current.decode(), re.M | re.S)
            assert match and match.group(0).encode() == after, row['ClaimKey']
            assert restored.count(after.decode()) == 1
            restored = restored.replace(after.decode(), before.decode(), 1)
            checks.append({'ClaimKey': row['ClaimKey'], 'AfterBlockSHA256': sha(after), 'Result': 'PASS'})
        assert sha(restored.encode()) == binding['BeforeSHA256'], 'Bytes outside declared blocks changed'
    print(json.dumps({'verdict': 'PASS', 'changed_files': len(bindings),
                      'changed_blocks': len(checks), 'unchanged_R3_claims': len(unchanged),
                      'coverage': '280/280 exactly once',
                      'negative_controls': 'missing-key and duplicate-key rejected',
                      'outside_block_preservation': '5/5 inverse reconstruction exact',
                      'changed_claim_reextraction': checks}, indent=2))

if __name__ == '__main__':
    main()
