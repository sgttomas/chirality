#!/usr/bin/env python3
"""Independent, read-only reproduction for D-GOV-15 Stage-1 pilot fan-in."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent / "evidence"
BASE = "2770fda4c63c98ee9f18cffbafd14c9aa59f497f"
VARIANCE = "D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674"
LEGACY = ("Datasheet.md", "Specification.md", "Procedure.md", "Guidance.md")

PILOTS = (
    {
        "project": "APP",
        "repo": Path("/Users/ryan/ai-env/projects/chirality-sow-app-pilot"),
        "commit": "fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26",
        "calibration": "9f219099eddc1e17aee643bcef040706de8f8f01",
        "package": Path("projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working"),
        "record": "SOW_FROZEN_WAVE_2026-07-12",
        "stored_map": "claim-map.csv",
        "stored_parity": "parity.json",
    },
    {
        "project": "PIP",
        "repo": Path("/Users/ryan/ai-env/projects/chirality-sow-piping-pilot"),
        "commit": "31c35ea9798c29cd0af16b7089186f3942dcfcb1",
        "calibration": "64aceb781bd26b148648922a4e103aa49096c4d1",
        "package": Path("projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working"),
        "record": "SOW_STAGE1_FROZEN_WAVE_2026-07-12",
        "stored_map": "CLAIM_MAP.csv",
        "stored_parity": "PARITY_REPORT.json",
    },
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(*args: object, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run([str(arg) for arg in args], cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(str(a) for a in args)}\n{result.stderr.decode(errors='replace')}")
    return result


def git_blob(repo: Path, rev: str, rel: Path) -> bytes:
    return run("git", "show", f"{rev}:{rel.as_posix()}", cwd=repo).stdout


def definitions(text: str, prefix: str) -> list[tuple[str, str]]:
    pattern = re.compile(rf"^(?:[-*]\s+\*\*|#{{3,6}}\s+)(?P<id>{prefix}-\d{{3}})(?:\*\*)?\s+[—-]\s+(?P<body>.+)$", re.MULTILINE)
    return [(m.group("id"), m.group("body").strip()) for m in pattern.finditer(text)]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    inventory: list[dict[str, object]] = []
    checklist: list[dict[str, object]] = []
    containment: list[dict[str, object]] = []
    failures: list[str] = []

    for pilot in PILOTS:
        repo = pilot["repo"]
        assert isinstance(repo, Path)
        package_rel = pilot["package"]
        assert isinstance(package_rel, Path)
        package = repo / package_rel
        candidates = sorted(package.glob("DEL-*/ScopeOfWork.md"))
        expected = 6 if pilot["project"] == "APP" else 4
        if len(candidates) != expected:
            failures.append(f"{pilot['project']}: expected {expected} candidates, found {len(candidates)}")

        diff = run("git", "diff", "--name-status", f"{BASE}..{pilot['commit']}", cwd=repo).stdout.decode().splitlines()
        diff_cal = run("git", "diff", "--name-status", f"{pilot['calibration']}..{pilot['commit']}", cwd=repo).stdout.decode().splitlines()
        bad = []
        for line in diff:
            status, rel = line.split("\t", 1)
            allowed_package_prefix = package_rel.as_posix().removesuffix("/1_Working")
            allowed = (
                rel.startswith(allowed_package_prefix + "/")
                or (pilot["project"] == "APP" and rel == "projects/chirality-app-dev/loop/LOOP_RECEIPTS.md")
                or (pilot["project"] == "PIP" and rel == "projects/chirality-piping/loop/LOOP_RECEIPTS.md")
            )
            if not allowed:
                bad.append(line)
        loop_receipt = Path(
            "projects/chirality-app-dev/loop/LOOP_RECEIPTS.md"
            if pilot["project"] == "APP" else "projects/chirality-piping/loop/LOOP_RECEIPTS.md"
        )
        base_receipt = git_blob(repo, BASE, loop_receipt)
        final_receipt = (repo / loop_receipt).read_bytes()
        containment.append({
            "project": pilot["project"], "base_to_final_changed_paths": len(diff),
            "calibration_to_final_changed_paths": len(diff_cal), "unauthorized_changes": bad,
            "domain_or_kty_changes": [line for line in diff if re.search(r"(^|/)(domains|_DomainEngines|KTY)(/|$)", line, re.I)],
            "loop_receipt_append_only": final_receipt.startswith(base_receipt),
            "calibration_evidence_modified_in_frozen_wave": [
                line for line in diff_cal if line.startswith("M\t") and "SOW_STAGE1_CALIBRATION" in line or
                line.startswith("M\t") and "SOW_CALIBRATION" in line
            ],
        })
        if bad:
            failures.append(f"{pilot['project']}: unauthorized changed paths: {bad}")

        for sow in candidates:
            deliverable = sow.parent
            rel_del = deliverable.relative_to(repo)
            del_id = deliverable.name.split("_", 1)[0]
            rec = deliverable / "_run_records" / str(pilot["record"])
            map_name = str(pilot["stored_map"])
            parity_name = str(pilot["stored_parity"])
            dst = OUT / del_id
            dst.mkdir(exist_ok=True)

            validate = run(sys.executable, ROOT / "tools/scope_of_work/validate_scope_of_work.py", deliverable,
                           "--pilot-variance", "--variance-ref", VARIANCE, "--json")
            validation = json.loads(validate.stdout)
            (dst / "validation.json").write_bytes(validate.stdout)
            if not validation.get("valid") or validation.get("format") != "PILOT_DUAL":
                failures.append(f"{del_id}: candidate validation failed: {validation}")

            map_out = dst / "claim-map.csv"
            parity_out = dst / "parity.json"
            run(sys.executable, ROOT / "tools/scope_of_work/map_scope_of_work_claims.py", "--scope-of-work", sow,
                "--source-dir", deliverable, "--output-csv", map_out)
            run(sys.executable, ROOT / "tools/scope_of_work/report_scope_of_work_parity.py", "--scope-of-work", sow,
                "--source-dir", deliverable, "--output-json", parity_out)
            rows = list(csv.DictReader(map_out.open(encoding="utf-8")))
            parity = json.loads(parity_out.read_text(encoding="utf-8"))
            mapped_source_lines = sum(
                int(check["line_end"]) - int(check["line_start"]) + 1
                for check in parity.get("checks", [])
            )
            stored_map_equal = rec.joinpath(map_name).read_bytes() == map_out.read_bytes()
            # Stored parity encodes a worktree-specific absolute path. Compare semantic content after normalizing that field.
            stored_parity = json.loads(rec.joinpath(parity_name).read_text(encoding="utf-8"))
            parity_cmp = dict(parity); stored_cmp = dict(stored_parity)
            parity_cmp.pop("scope_of_work", None); stored_cmp.pop("scope_of_work", None)
            stored_parity_equal = parity_cmp == stored_cmp

            html1, html2 = dst / "render-1.html", dst / "render-2.html"
            run(sys.executable, ROOT / "tools/scope_of_work/render_scope_of_work.py", sow, "--output", html1)
            run(sys.executable, ROOT / "tools/scope_of_work/render_scope_of_work.py", sow, "--output", html2)
            html = html1.read_bytes(); lower = html.lower()
            html_ok = html == html2.read_bytes() and sha(sow.read_bytes()).encode() in html and b"<script" not in lower \
                and b"<form" not in lower and not re.search(rb"(?:src|href|action)\s*=", lower)

            base_sources = {}
            source_equal = True
            for name in LEGACY:
                current = (deliverable / name).read_bytes()
                base = git_blob(repo, BASE, rel_del / name)
                base_sources[name] = sha(current)
                source_equal &= current == base
            status = (deliverable / "_STATUS.md").read_bytes()
            base_status = git_blob(repo, BASE, rel_del / "_STATUS.md")
            lifecycle_match = re.search(rb"(?:Current State|State):\*\*?\s*`?([A-Z_]+)", status)
            lifecycle = lifecycle_match.group(1).decode() if lifecycle_match else "UNKNOWN"

            text = sow.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1]
            def fm_list(key: str) -> list[str]:
                match = re.search(rf"(?m)^{key}:\s*\[([^]]*)\]\s*$", frontmatter)
                return [part.strip().strip("\"'") for part in match.group(1).split(",") if part.strip()] if match else []
            ac_first = definitions(text, "AC")
            ac_second = definitions(text, "AC")
            review_bytes_1 = json.dumps(ac_first, ensure_ascii=False, separators=(",", ":")).encode()
            review_bytes_2 = json.dumps(ac_second, ensure_ascii=False, separators=(",", ":")).encode()
            checklist.append({"deliverable_id": del_id, "source": "ScopeOfWork.md AC-* definitions",
                              "items": [{"id": i, "criterion": body} for i, body in ac_first],
                              "derivation_1_sha256": sha(review_bytes_1), "derivation_2_sha256": sha(review_bytes_2),
                              "byte_identical": review_bytes_1 == review_bytes_2})

            dispositions = sorted({r["Disposition"] for r in rows})
            item = {
                "project": pilot["project"], "deliverable_id": del_id,
                "relative_path": rel_del.as_posix(), "candidate_sha256": sha(sow.read_bytes()),
                "source_sha256": base_sources, "status_sha256": sha(status),
                "status_matches_frozen_base": status == base_status, "lifecycle": lifecycle,
                "source_files_match_frozen_base": source_equal, "mapping_rows": len(rows),
                "dispositions": dispositions, "parity_pass": parity.get("pass"),
                "source_line_checks": len(parity.get("checks", [])), "mapped_source_lines": mapped_source_lines,
                "stored_map_byte_equal": stored_map_equal,
                "stored_parity_semantically_equal": stored_parity_equal, "html_pass": html_ok,
                "ac_count": len(ac_first), "out_count": len(definitions(text, "OUT")),
                "ver_count": len(definitions(text, "VER")),
                "project_scope_refs": fm_list("project_scope_refs"),
                "package_objective_refs": fm_list("package_objective_refs"),
                "independent_verifier_return_present": (rec / "INDEPENDENT_VERIFIER_RETURN.md").is_file(),
            }
            inventory.append(item)
            if not all((source_equal, status == base_status, lifecycle == "IN_PROGRESS", parity.get("pass"),
                        stored_map_equal, stored_parity_equal, html_ok, dispositions == ["PRESERVED"],
                        item["independent_verifier_return_present"])):
                failures.append(f"{del_id}: one or more preservation/reproduction gates failed: {item}")

    (OUT / "DELIVERABLE_INVENTORY.json").write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "REVIEW_CHECKLIST_REPRODUCTION.json").write_text(json.dumps(checklist, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (OUT / "CONTAINMENT.json").write_text(json.dumps(containment, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "verdict": "PASS" if not failures else "FAIL", "basis": BASE,
        "app_commit": PILOTS[0]["commit"], "piping_commit": PILOTS[1]["commit"],
        "deliverables": len(inventory), "mapping_rows": sum(int(i["mapping_rows"]) for i in inventory),
        "source_line_checks": sum(int(i["source_line_checks"]) for i in inventory),
        "mapped_source_lines": sum(int(i["mapped_source_lines"]) for i in inventory),
        "all_checklist_derivations_repeat": all(bool(i["byte_identical"]) for i in checklist),
        "failures": failures,
    }
    (OUT / "REPRODUCTION_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
