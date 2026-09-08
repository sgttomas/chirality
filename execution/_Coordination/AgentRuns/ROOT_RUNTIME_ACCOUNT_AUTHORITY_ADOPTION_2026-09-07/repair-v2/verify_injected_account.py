"""Disposable baseline composition must reject an injected account supplement."""
from pathlib import Path
import hashlib
import tempfile
from unittest.mock import patch

import root_runtime_successors as successors
from root_governance_state import GovernanceError

root = Path(tempfile.mkdtemp(prefix='root-account-baseline-negative-')).resolve()
baseline = {'projects/chirality-runtime/execution/_Decomposition/decomp.md':
            hashlib.sha256(b'baseline').hexdigest()}
target = root / next(iter(baseline))
target.parent.mkdir(parents=True, exist_ok=True)
target.write_bytes(b'baseline')
account = root / successors.ACCOUNT_SUPPLEMENT
account.parent.mkdir(parents=True, exist_ok=True)
account.write_bytes(b'unaccepted injected account authority')
with patch.object(successors, 'POLICY', 'missing/POLICY.json'):
    try:
        successors.recognize(root, baseline)
    except GovernanceError as exc:
        print('PASS: injected account supplement rejected:', exc)
    else:
        raise AssertionError('injected account supplement bypassed the successor policy')
