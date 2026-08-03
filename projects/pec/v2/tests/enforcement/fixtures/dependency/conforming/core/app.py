from __future__ import annotations

import json
from pathlib import Path


def encode_path(path: Path) -> str:
    return json.dumps({"path": str(path)})
