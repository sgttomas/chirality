"""I105 (B2-P): what physics-1's PY retained reader does today with each combination successor document
({source, invocation}): validate_retained_precision's refusal (gate, code) or acceptance.
Usage: readers_today_py.py <P root> <document.json>..."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
from core.analysis_runs.retained_precision import RetainedPrecisionError, validate_retained_precision
for path in sys.argv[2:]:
    doc = json.loads(Path(path).read_text())
    try:
        validate_retained_precision(doc['source'], doc['invocation'])
        print(f"READER_PY {Path(path).name} accepted")
    except RetainedPrecisionError as error:
        print(f"READER_PY {Path(path).name} refused gate={getattr(error, 'gate', None)} code={error.code}")
