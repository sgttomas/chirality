#!/usr/bin/env python3
"""Fixtures and expected decisions for the App amendment-reopen parity test.

The App checker `src/lib/lifecycle/amendment-reopen.ts` ports the Root checker
`tools/validation/check_amendment_reopen.py`. This script writes the shared
inputs and the Root checker's decisions on them:

- `cases.json`: fixture trees (files, symlinks, empty folders) with the
  queries run against each. The trees mirror
  `tools/validation/test_check_amendment_reopen.py` and add cases for CSV,
  heading and path handling.
- `expected.json`: `check_reopen()`'s decision for every fixture query, and for
  the real amendment records in this checkout (PEC, Piping, Runtime and App
  scope-change roots) read in place. A real case whose records are absent is
  written as `null`, and the test skips it.

`src/__tests__/lib/amendment-reopen-parity.test.ts` materializes each tree in
a temporary folder, runs the TypeScript checker with the same arguments and
compares the decisions field by field, including the reason text. Absolute
temporary or repository paths in reasons are written as `<ROOT>`.

Usage, from the repository root:

    python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/amendment-reopen/generate_expected.py
    python3 projects/chirality-app-dev/frontend/src/__tests__/fixtures/amendment-reopen/generate_expected.py --check

`--check` writes nothing and exits 1 when a committed file differs from what
this script and the Root checker now produce.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[6]
CHECKER = REPO_ROOT / "tools" / "validation" / "check_amendment_reopen.py"

_spec = importlib.util.spec_from_file_location("check_amendment_reopen", CHECKER)
assert _spec and _spec.loader
checker = importlib.util.module_from_spec(_spec)
sys.modules["check_amendment_reopen"] = checker
_spec.loader.exec_module(checker)

BASE_COLUMNS = [
    "AmendmentID",
    "ActionSeq",
    "ActionType",
    "EntityType",
    "EntityID",
    "Description",
    "AffectedFiles",
    "DownstreamReruns",
    "SupersessionBindingPresent",
]
DEL_REL = "projects/fixture/execution/PKG-01_Fixture/1_Working/DEL-01-01_Fixture"
SC_REL = "projects/fixture/execution/_ScopeChange"
SNAPSHOT_REL = f"{SC_REL}/SCA-001_2026-09-26_1200"
GROUP_REL = f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-{{group}}_2026-09-26"


def csv_text(columns: list[str], rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({c: row.get(c, "") for c in columns})
    return buffer.getvalue()


def row(action, entity="DEL-01-01", seq="1", entity_type="DELIVERABLE", scope=None, amendment="SCA-001"):
    data = {
        "AmendmentID": amendment,
        "ActionSeq": seq,
        "ActionType": action,
        "EntityType": entity_type,
        "EntityID": entity,
        "Description": "fixture",
        "SupersessionBindingPresent": "NO",
    }
    if scope is not None:
        data["ScopeChanging"] = scope
    return data


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def tree(
    rows,
    *,
    prefix="",
    amendment="SCA-001",
    scope_column=True,
    groups=("1", "2", "3"),
    group3_heading=None,
    register_name="Amendment_Actions.csv",
    register_text=None,
    bound_sha=None,
    extra_manifest_rows=(),
    manifest_path_override=None,
    manifest_header="Path,SHA256,Role,AcceptanceBoundary",
) -> dict:
    """One deliverable folder and one amendment's scope-change records (as test_check_amendment_reopen.build)."""
    files: dict[str, str] = {}
    snapshot = f"{prefix}{SC_REL}/{amendment}_2026-09-26_1200"
    files[f"{prefix}{DEL_REL}/_STATUS.md"] = "# Status: DEL-01-01\n\n**Current State:** ISSUED\n"
    columns = BASE_COLUMNS + (["ScopeChanging"] if scope_column else [])
    register = f"{snapshot}/{register_name}"
    text = register_text if register_text is not None else csv_text(columns, rows)
    files[register] = text
    bound = bound_sha or sha(text)
    register_rel = manifest_path_override or register[len(prefix):]
    for group in groups:
        folder = f"{prefix}{SC_REL}/checkpoint_snapshots/{amendment}_GROUP-{group}_2026-09-26"
        heading = f"{amendment} checkpoint group {group} — accepted fixture"
        if group == "3" and group3_heading is not None:
            heading = group3_heading
        files[f"{folder}/DECISION.md"] = f"# {heading}\n\nFixture decision.\n"
        manifest_rows = [f"{snapshot[len(prefix):]}/Propagation_Plan.md,{'0' * 64},plan,Accepted"]
        if group == "2":
            manifest_rows.append(f"{register_rel},{bound},exact final action register,Accepted")
            manifest_rows.extend(extra_manifest_rows)
        files[f"{folder}/ACCEPTED_MANIFEST.csv"] = manifest_header + "\n" + "\n".join(manifest_rows) + "\n"
    return {"files": files, "symlinks": {}, "dirs": []}


def merge(*trees: dict) -> dict:
    out = {"files": {}, "symlinks": {}, "dirs": []}
    for item in trees:
        out["files"].update(item["files"])
        out["symlinks"].update(item["symlinks"])
        out["dirs"].extend(item["dirs"])
    return out


def q(deliverable=DEL_REL, amendment="SCA-001", *, deliverable_is_path=True, amendment_is_path=False,
      scope_change_root=None, project_root=".", cwd=".") -> dict:
    return {
        "deliverable": deliverable,
        "deliverableIsPath": deliverable_is_path,
        "amendment": amendment,
        "amendmentIsPath": amendment_is_path,
        "scopeChangeRoot": scope_change_root,
        "projectRoot": project_root,
        "cwd": cwd,
    }


def fixture_cases() -> list[dict]:
    cases: list[dict] = []

    def add(name: str, spec: dict, *queries: dict) -> None:
        cases.append({"name": name, "tree": spec, "queries": list(queries) or [q()]})

    # Admitted paths
    add("modify-admitted", tree([row("ADD", entity="DEL-01-02"), row("MODIFY", seq="2", scope="NO")]))
    add("legacy-modify-admitted", tree([row("MODIFY")], scope_column=False))
    add("reclassify-yes-admitted", tree([row("RECLASSIFY", scope="YES")]))
    add(
        "labelled-entity-id",
        tree([row("MODIFY", entity="DEL-01-01_Fixture", scope="YES")]),
        q("DEL-01-01", deliverable_is_path=False, scope_change_root=SC_REL),
        q(),
    )
    add("similar-deliverable-id-not-matched", tree([row("MODIFY", entity="DEL-01-011", scope="NO")]))
    group3 = GROUP_REL.format(group="3")
    add(
        "group3-and-snapshot-paths",
        tree([row("MODIFY", scope="NO")]),
        q(amendment=group3, amendment_is_path=True),
        q(amendment=f"{group3}/DECISION.md"),
        q(amendment=SNAPSHOT_REL, amendment_is_path=True),
        q(amendment=f"{SNAPSHOT_REL}/Amendment_Actions.csv"),
    )
    add(
        "project-qualified-amendment-id",
        tree([row("MODIFY", scope="NO", amendment="SCA-APP-003")], amendment="SCA-APP-003"),
        q(amendment="SCA-APP-003"),
    )
    cp2 = tree([row("MODIFY", scope="NO")], register_name="Amendment_Actions_CP2.csv")
    cp2["files"][f"{SNAPSHOT_REL}/Amendment_Actions.csv"] = csv_text(BASE_COLUMNS, [row("ADD")])
    add("cp2-register-name-bound", cp2)
    add(
        "manifest-path-relative-to-project-folder",
        tree(
            [row("MODIFY", scope="NO")],
            manifest_path_override="execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv",
        ),
    )
    intake = f"{SNAPSHOT_REL}/Amendment_Actions.csv"
    role = tree(
        [row("MODIFY", scope="NO")],
        register_name="Amendment_Actions_CP2.csv",
        extra_manifest_rows=[f"{intake},{'1' * 64},intake context,Context"],
    )
    role["files"][intake] = "x\n"
    add("role-disambiguates-registers", role)
    add("uppercase-bound-sha", tree([row("MODIFY", scope="NO")], bound_sha=sha(csv_text(BASE_COLUMNS + ["ScopeChanging"], [row("MODIFY", scope="NO")])).upper()))
    add(
        "lowercase-manifest-header",
        tree([row("MODIFY", scope="NO")], manifest_header="path,sha-256,role,acceptanceboundary"),
    )

    # Acceptance stage
    add(
        "group2-only",
        tree([row("MODIFY", scope="NO")], groups=("1", "2")),
        q(),
        q(amendment=SNAPSHOT_REL, amendment_is_path=True),
    )
    add("group1-only", tree([row("MODIFY", scope="NO")], groups=("1",)))
    add("no-group-folders", tree([row("MODIFY", scope="NO")], groups=()))
    add(
        "group2-decision-path",
        tree([row("MODIFY", scope="NO")]),
        q(amendment=GROUP_REL.format(group="2"), amendment_is_path=True),
        q(amendment=f"{GROUP_REL.format(group='1')}/DECISION.md"),
    )
    for index, heading in enumerate(
        [
            "SCA-001 checkpoint group 3 — returned to checkpoint 2",
            "SCA-001 checkpoint group 3 — not accepted",
            "SCA-002 checkpoint group 3 — accepted audited poststate",
            "Checkpoint group 3 notes",
            "SCA-001 checkpoint group 3 — withdrawn after review, accepted text retracted",
            "SCA-001 checkpoint group 30 — accepted",
            "SCA-001 checkpoint group 3 — preaccepted",
            "sca-001   CHECKPOINT GROUP 3: ACCEPTED",
            "SCA-001\tcheckpoint group 3 (owner 'accepted' it)",
        ]
    ):
        add(f"group3-heading-{index}", tree([row("MODIFY", scope="NO")], group3_heading=heading))
    bom = tree([row("MODIFY", scope="NO")])
    bom["files"][f"{group3}/DECISION.md"] = "﻿\r\n# SCA-001 checkpoint group 3 — accepted\r\nbody\r\n"
    add("group3-heading-bom-crlf", bom)
    late = tree([row("MODIFY", scope="NO")])
    late["files"][f"{group3}/DECISION.md"] = "Preamble line\n#Not a heading\n# SCA-001 checkpoint group 3 — accepted\n"
    add("group3-heading-after-preamble", late)
    two = tree([row("MODIFY", scope="NO")], group3_heading="SCA-001 checkpoint group 3 — returned")
    second = f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-27"
    two["files"][f"{second}/DECISION.md"] = "# SCA-001 checkpoint group 3 — accepted on retry\n"
    two["files"][f"{second}/ACCEPTED_MANIFEST.csv"] = "Path,SHA256\n"
    add("two-group3-folders-second-accepted", two)
    both = tree([row("MODIFY", scope="NO")], group3_heading="SCA-001 checkpoint group 3 — returned")
    both["files"][f"{second}/DECISION.md"] = "# SCA-001 checkpoint group 3 — 'rejected'\n"
    add("two-group3-folders-refused", both)
    no_manifest = tree([row("MODIFY", scope="NO")])
    del no_manifest["files"][f"{group3}/ACCEPTED_MANIFEST.csv"]
    add("group3-without-manifest", no_manifest)
    no_g2 = tree([row("MODIFY", scope="NO")])
    del no_g2["files"][f"{GROUP_REL.format(group='2')}/ACCEPTED_MANIFEST.csv"]
    add("group2-manifest-missing", no_g2)

    # Register binding
    mismatch = tree([row("MODIFY", scope="NO")])
    mismatch["files"][f"{SNAPSHOT_REL}/Amendment_Actions.csv"] += "SCA-001,9,MODIFY,DELIVERABLE,DEL-09-09,late edit,,,NO,NO\n"
    add("register-hash-mismatch", mismatch)
    add("register-not-bound", tree([row("MODIFY", scope="NO")], register_name="Actions_Final.csv"))
    other = f"{SNAPSHOT_REL}/Amendment_Actions_B.csv"
    add(
        "register-ambiguous",
        tree(
            [row("MODIFY", scope="NO")],
            extra_manifest_rows=[f"{other},{'1' * 64},exact final action register,Accepted"],
        ),
    )
    missing = tree([row("MODIFY", scope="NO")])
    del missing["files"][f"{SNAPSHOT_REL}/Amendment_Actions.csv"]
    add("register-missing", missing)
    add("manifest-schema", tree([row("MODIFY", scope="NO")], manifest_header="Path,Digest,Role,AcceptanceBoundary"))
    absolute = tree([row("MODIFY", scope="NO")], manifest_path_override="/etc/Amendment_Actions.csv")
    add("manifest-absolute-register-path", absolute)

    # Action rows
    for action in ("ADD", "REMOVE", "MERGE", "SPLIT"):
        add(f"action-{action.lower()}-refused", tree([row(action, scope="YES")]))
    add("reclassify-no-refused", tree([row("RECLASSIFY", scope="NO")]))
    add("reclassify-blank-refused", tree([row("RECLASSIFY", scope="")]))
    add("reclassify-legacy-refused", tree([row("RECLASSIFY")], scope_column=False))
    add("non-deliverable-entity", tree([row("MODIFY", entity_type="OTHER", scope="NO")]))
    add("row-of-another-amendment", tree([row("MODIFY", scope="NO", amendment="SCA-009")]))
    add(
        "mixed-case-and-padded-cells",
        tree(
            [row("modify", seq=" 7 ", entity_type="deliverable", entity=" DEL-01-01 ", scope=" no ")],
        ),
    )
    add(
        "register-schema",
        tree([], register_text="AmendmentID,ActionSeq,ActionType,EntityID\nSCA-001,1,MODIFY,DEL-01-01\n"),
    )
    quirky = (
        "﻿AmendmentID,ActionSeq,ActionType,EntityType,EntityID,Description,ScopeChanging\r\n"
        "\r\n"
        'SCA-001,1,ADD,DELIVERABLE,DEL-01-01,"multi\nline, ""quoted"" description",YES,extra,cells\r\n'
        "SCA-001,2,RECLASSIFY,DELIVERABLE,DEL-01-01\r\n"
        'SCA-001,3,RECLASSIFY,DELIVERABLE,DEL-01-01,"x"tail,"Y\'s"\r'
    )
    add("csv-quirks-refused", tree([], register_text=quirky))
    quirky_ok = quirky + 'SCA-001,4,"RECLASSIFY",DELIVERABLE,DEL-01-01_Fixture,,YES'
    add("csv-quirks-admitted", tree([], register_text=quirky_ok))
    unterminated = (
        "AmendmentID,ActionSeq,ActionType,EntityType,EntityID,ScopeChanging\n"
        'SCA-001,5,MODIFY,DELIVERABLE,DEL-01-01,"unterminated\n'
    )
    add("csv-unterminated-quote", tree([], register_text=unterminated))
    duplicate = (
        "AmendmentID,ActionType,EntityType,EntityID,ActionType\n"
        "SCA-001,MODIFY,DELIVERABLE,DEL-01-01,ADD\n"
        "SCA-001,ADD,DELIVERABLE,DEL-01-01\n"
    )
    add("csv-duplicate-header", tree([], register_text=duplicate))
    add("csv-blank-first-line", tree([], register_text="\nActionType,EntityType,EntityID\nMODIFY,DELIVERABLE,DEL-01-01\n"))

    # Containment
    outside = merge(
        tree([row("MODIFY", scope="NO")], prefix="project/", manifest_path_override="../outside/Amendment_Actions.csv"),
        {"files": {"outside/Amendment_Actions.csv": csv_text(BASE_COLUMNS, [row("MODIFY")])}, "symlinks": {}, "dirs": []},
    )
    add("manifest-path-escape", outside, q(f"project/{DEL_REL}", project_root="project", cwd="project"))
    other_root = tree([row("MODIFY", scope="NO")], manifest_path_override="projects/other/Amendment_Actions.csv")
    other_root["files"]["projects/other/Amendment_Actions.csv"] = csv_text(BASE_COLUMNS + ["ScopeChanging"], [row("MODIFY", scope="YES")])
    add("manifest-path-outside-scope-change-root", other_root)
    link_register = tree([row("MODIFY", scope="NO")], prefix="project/")
    text = link_register["files"].pop(f"project/{SNAPSHOT_REL}/Amendment_Actions.csv")
    link_register["files"]["outside.csv"] = text
    link_register["symlinks"][f"project/{SNAPSHOT_REL}/Amendment_Actions.csv"] = "../../../../../../outside.csv"
    add("symlinked-register-escape", link_register, q(f"project/{DEL_REL}", project_root="project", cwd="project"))
    inside_link = tree([row("MODIFY", scope="NO")])
    text = inside_link["files"].pop(f"{SNAPSHOT_REL}/Amendment_Actions.csv")
    inside_link["files"][f"{SC_REL}/registers/actions.csv"] = text
    inside_link["symlinks"][f"{SNAPSHOT_REL}/Amendment_Actions.csv"] = "../registers/actions.csv"
    add("symlinked-register-inside", inside_link)
    moved = tree([row("MODIFY", scope="NO")], prefix="project/")
    for key in list(moved["files"]):
        marker = f"project/{SC_REL}/checkpoint_snapshots/"
        if key.startswith(marker):
            moved["files"][f"moved_snapshots/{key[len(marker):]}"] = moved["files"].pop(key)
    moved["symlinks"][f"project/{SC_REL}/checkpoint_snapshots"] = "../../../../../moved_snapshots"
    add("symlinked-checkpoint-snapshots-escape", moved, q(f"project/{DEL_REL}", project_root="project", cwd="project"))
    elsewhere = merge(tree([row("MODIFY", scope="NO")], prefix="project/"), tree([row("MODIFY", scope="NO")], prefix="elsewhere/"))
    add(
        "amendment-path-outside-project",
        elsewhere,
        q(f"project/{DEL_REL}", f"elsewhere/{SNAPSHOT_REL}", amendment_is_path=True, project_root="project", cwd="project"),
    )
    another = tree([row("MODIFY", scope="NO")])
    another["dirs"].append("projects/other/execution/_ScopeChange")
    add(
        "amendment-of-another-execution-root",
        another,
        q(scope_change_root="projects/other/execution/_ScopeChange"),
    )
    add(
        "scope-change-root-not-a-directory",
        tree([row("MODIFY", scope="NO")]),
        q(scope_change_root="projects/fixture/execution/missing_ScopeChange"),
    )
    add(
        "amendment-path-not-under-given-root",
        merge(tree([row("MODIFY", scope="NO")]), {"files": {}, "symlinks": {}, "dirs": ["projects/fixture/execution/PKG-01_Fixture/_ScopeChange"]}),
        q(amendment=SNAPSHOT_REL, amendment_is_path=True, scope_change_root="projects/fixture/execution/PKG-01_Fixture/_ScopeChange"),
    )
    add(
        "unresolvable-and-unusable-amendments",
        tree([row("MODIFY", scope="NO")]),
        q(amendment="no/such/path"),
        q(amendment=f"{SNAPSHOT_REL}/Amendment_Actions.csv", amendment_is_path=True),
        q(amendment="projects/fixture", amendment_is_path=False),
        q(amendment="  SCA-001  "),
        q(amendment="SCA-001x"),
    )
    add(
        "deliverable-id-without-root",
        tree([row("MODIFY", scope="NO")]),
        q("DEL-01-01", deliverable_is_path=False),
    )
    add(
        "usage-errors",
        tree([row("MODIFY", scope="NO")]),
        q("not-a-deliverable", deliverable_is_path=False),
        q(project_root="no-such-project-root"),
    )
    linked_deliverable = tree([row("MODIFY", scope="NO")])
    linked_deliverable["symlinks"]["projects/fixture/execution/PKG-01_Fixture/1_Working/DEL-01-01_Link"] = "DEL-01-01_Fixture"
    linked_deliverable["files"]["outside/DEL-01-01_Out/_STATUS.md"] = "# Status\n"
    linked_deliverable["symlinks"]["project-link/DEL-01-01_Escape"] = "../outside/DEL-01-01_Out"
    add(
        "symlinked-deliverable-folders",
        linked_deliverable,
        q("projects/fixture/execution/PKG-01_Fixture/1_Working/DEL-01-01_Link"),
        q("outside/DEL-01-01_Out", project_root="projects"),
        q("project-link/DEL-01-01_Escape", project_root="project-link"),
    )
    return cases


# Real amendment records in this checkout, read in place (project root = repository).
PEC_DEL = "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access"
PEC_SC = "projects/pec/execution/_ScopeChange"
PIPING_SC = "projects/chirality-piping/execution/_ScopeChange"
RUNTIME_SC = "projects/chirality-runtime/execution/_ScopeChange"
APP_SC = "projects/chirality-app-dev/execution/_ScopeChange"


def real_cases() -> list[dict]:
    return [
        {
            "name": "pec-sca-006",
            "requires": [f"{PEC_SC}/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26", PEC_DEL],
            "queries": [
                q(PEC_DEL, "SCA-006"),
                q("DEL-08-06", f"{PEC_SC}/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26", deliverable_is_path=False),
                q("DEL-04-03", "SCA-006", deliverable_is_path=False, scope_change_root=PEC_SC),
                q("DEL-09-09", "SCA-006", deliverable_is_path=False, scope_change_root=PEC_SC),
            ],
        },
        {
            "name": "pec-sca-005",
            "requires": [f"{PEC_SC}/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25"],
            "queries": [
                q("DEL-01-01", "SCA-005", deliverable_is_path=False, scope_change_root=PEC_SC),
                q("DEL-07-04", "SCA-005", deliverable_is_path=False, scope_change_root=PEC_SC),
                q("DEL-02-08", f"{PEC_SC}/SCA-005_2026-09-23_2139", deliverable_is_path=False),
            ],
        },
        {
            "name": "piping-sca-011",
            "requires": [f"{PIPING_SC}/checkpoint_snapshots"],
            "queries": [q("DEL-04-07", "SCA-011", deliverable_is_path=False, scope_change_root=PIPING_SC)],
        },
        {
            "name": "runtime-sca-003",
            "requires": [RUNTIME_SC],
            "queries": [q("DEL-01-01", "SCA-003", deliverable_is_path=False, scope_change_root=RUNTIME_SC)],
        },
        {
            "name": "app-sca-app-010",
            "requires": [APP_SC],
            "queries": [q("DEL-02-05", "SCA-APP-010", deliverable_is_path=False, scope_change_root=APP_SC)],
        },
    ]


def materialize(spec: dict, root: Path) -> None:
    for rel in spec["dirs"]:
        (root / rel).mkdir(parents=True, exist_ok=True)
    for rel, text in spec["files"].items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    for rel, link_target in spec["symlinks"].items():
        link = root / rel
        link.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(link_target, link)


def run(query: dict, root: Path) -> dict:
    deliverable = str(root / query["deliverable"]) if query["deliverableIsPath"] else query["deliverable"]
    amendment = str(root / query["amendment"]) if query["amendmentIsPath"] else query["amendment"]
    scope_root = str(root / query["scopeChangeRoot"]) if query["scopeChangeRoot"] is not None else None
    try:
        decision = checker.check_reopen(
            deliverable,
            amendment,
            scope_change_root=scope_root,
            project_root=str(root / query["projectRoot"]),
            cwd=str(root / query["cwd"]),
        )
    except checker.UsageError:
        return {"usageError": True}
    data = decision.to_json()
    reason = data["reason"]
    for prefix in sorted({str(root), os.path.realpath(root)}, key=len, reverse=True):
        reason = reason.replace(prefix, "<ROOT>")
    return {
        "admitted": data["admitted"],
        "code": data["code"],
        "reason": reason,
        "deliverableId": data["deliverable_id"],
        "amendmentId": data["amendment_id"],
        "scopeChangeRoot": data["scope_change_root"],
        "group3Snapshot": data["group3_snapshot"],
        "group3Decision": data["group3_decision"],
        "group2Manifest": data["group2_manifest"],
        "registerPath": data["register_path"],
        "registerSha256": data["register_sha256"],
        "actionSeq": data["action_seq"],
        "actionType": data["action_type"],
        "scopeChanging": data["scope_changing"],
        "notes": data["notes"],
    }


def build() -> tuple[str, str]:
    cases = fixture_cases()
    expected: dict[str, object] = {"fixtures": {}, "real": {}}
    for case in cases:
        with tempfile.TemporaryDirectory(prefix="amendment-reopen-parity-") as tmp:
            root = Path(tmp)
            materialize(case["tree"], root)
            expected["fixtures"][case["name"]] = [run(query, root) for query in case["queries"]]
    reals = real_cases()
    for case in reals:
        present = all((REPO_ROOT / rel).exists() for rel in case["requires"])
        expected["real"][case["name"]] = [run(query, REPO_ROOT) for query in case["queries"]] if present else None
    cases_text = json.dumps({"fixtures": cases, "real": reals}, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    expected_text = json.dumps(expected, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    return cases_text, expected_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="compare with the committed files; write nothing")
    args = parser.parse_args(argv)
    outputs = dict(zip(("cases.json", "expected.json"), build()))
    drift = []
    for name, text in outputs.items():
        target = HERE / name
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != text:
                drift.append(name)
            continue
        target.write_text(text, encoding="utf-8")
    if drift:
        print("committed files differ from the Root checker's results: " + ", ".join(drift), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
