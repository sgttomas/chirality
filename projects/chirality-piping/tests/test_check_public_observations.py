#!/usr/bin/env python3
"""Tests for the lane-local public-observation check (tools/caepipe_correlation/check_public_observations.py).

Every term here is invented: "Acmepipe" stands for a product name, "Acme Labs" for a vendor, "9.99" for a
version, and the tokens for distinctive strings from private evaluation notes. "Crashing" stands in for any
defect or limit language about the target.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.caepipe_correlation import check_public_observations as check  # noqa: E402

TERMS = """# invented
[names]
Acmepipe
Acme Labs
9.99
[tokens]
Widget overflow at
Acmepipe Demo
Loads on Gadgets
"""


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


def repo_with(tmp_path: Path, files: dict[str, str]) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True)
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "invented@example.invalid")
    git(repo, "config", "user.name", "Invented")
    (repo / "README.md").write_text("base\n", encoding="utf-8")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    git(repo, "checkout", "-q", "-b", "topic")
    for name, text in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "topic change")
    return repo


def run(tmp_path: Path, files: dict[str, str]) -> list[str]:
    repo = repo_with(tmp_path, files)
    terms = check.load_terms(write_terms(tmp_path))
    return check.check_range(repo, "main", "topic", terms)


def write_terms(tmp_path: Path) -> Path:
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = tmp_path / "terms.txt"
    path.write_text(TERMS, encoding="utf-8")
    return path


def test_named_observation_in_prose_is_blocked_and_terms_are_not_printed(tmp_path):
    findings = run(tmp_path, {"doc/design.md": "Intro.\nAcmepipe 9.99 was crashing to stop early.\n"})
    assert findings and all("Acmepipe" not in item and "crashing" not in item for item in findings)
    assert any(item.startswith("doc/design.md:2:") for item in findings)


def test_generic_wording_about_the_target_is_still_screened(tmp_path):
    assert run(tmp_path, {"doc/design.md": "The target tool stops early (private notes).\n"}) == [
        "doc/design.md:1: defect or limit about the target tool"]


def test_name_without_observation_marker_passes(tmp_path):
    assert run(tmp_path, {"doc/design.md": "The Acmepipe manual documents batch runs.\n"}) == []


def test_observed_token_is_blocked_anywhere_in_prose(tmp_path):
    findings = run(tmp_path, {"doc/notes.md": "It reported Widget overflow at startup.\n"})
    assert findings == ["doc/notes.md:1: private token #1"]


def test_code_literals_pass_but_comments_and_test_names_are_prose(tmp_path):
    code = ('TITLE = "Loads on Gadgets"\n'
            "# Acmepipe trial build quirk\n"
            "X = 1\n"
            "def test_acmepipe_trial_quirk():\n"
            "    pass\n")
    findings = run(tmp_path, {"pkg/mod.py": code})
    assert {item.split(":")[1] for item in findings} == {"2", "4"}
    findings = run(tmp_path / "t", {"tests/test_mod.py": "def test_widget_overflow_at_start():\n    pass\n"})
    assert any("private token #1" in item for item in findings)


def test_identifier_and_path_forms_of_a_name_do_not_match(tmp_path):
    findings = run(tmp_path, {"core/acmepipe_mbf/notes.md": "See core/acmepipe_mbf/ and acmepipe_export; trial.\n"})
    assert findings == []


def test_private_tokens_are_blocked_on_every_fixture_line_but_the_product_name_is_not(tmp_path):
    findings = run(tmp_path, {"fixtures/x/invented/data.csv": "Acmepipe Demo,MODEL,\nLoads on Gadgets: case,\nAcmepipe,9.99,\n"})
    assert findings == ["fixtures/x/invented/data.csv:1: private token #2", "fixtures/x/invented/data.csv:2: private token #3"]


def test_owner_words_are_not_screened(tmp_path):
    text = ("<!-- owner-words -->\n- Owner: \"I installed a trial version of Acmepipe.\"\n<!-- /owner-words -->\n"
            "Acmepipe trial limits were crashing.\n")
    findings = run(tmp_path, {"doc/design.md": text})
    assert findings and all(item.startswith("doc/design.md:4:") for item in findings)


def test_commit_messages_are_screened(tmp_path):
    repo = repo_with(tmp_path, {"doc/a.md": "generic\n"})
    (repo / "doc/b.md").write_text("generic\n", encoding="utf-8")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "Acmepipe 9.99 crashing limit")
    findings = check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path)))
    assert any(item.startswith("commit ") for item in findings)


def test_whole_file_mode_and_exit_codes(tmp_path):
    terms = write_terms(tmp_path)
    clean = tmp_path / "clean.md"
    clean.write_text("Generic text.\n", encoding="utf-8")
    dirty = tmp_path / "dirty.md"
    dirty.write_text("Acmepipe was crashing.\n", encoding="utf-8")
    assert check.main(["--terms-file", str(terms), "--file", str(clean)]) == 0
    assert check.main(["--terms-file", str(terms), "--file", str(dirty)]) == 1
    assert check.main(["--terms-file", str(tmp_path / "missing.txt"), "--file", str(clean)]) == 2


def test_names_match_in_any_case(tmp_path):
    findings = run(tmp_path, {"doc/a.md": "ACMEPIPE was crashing.\n\nacme labs trial notes.\n"})
    assert {item.split(":")[1] for item in findings} == {"1", "3"}


def test_added_line_is_screened_against_unchanged_context(tmp_path):
    repo = repo_with(tmp_path, {"doc/a.md": "The Acmepipe manual documents batch runs.\n"})
    git(repo, "branch", "-f", "main", "topic")
    (repo / "doc/a.md").write_text("The Acmepipe manual documents batch runs.\nIt was crashing to stop.\n",
                                   encoding="utf-8")
    git(repo, "commit", "-q", "-am", "more")
    findings = check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path)))
    assert findings == ["doc/a.md:1: defect or limit about the target tool"]


def test_unchanged_findings_are_not_reported(tmp_path):
    repo = repo_with(tmp_path, {"doc/a.md": "Acmepipe was crashing.\n\n\nGeneric.\n"})
    git(repo, "branch", "-f", "main", "topic")
    (repo / "doc/a.md").write_text("Acmepipe was crashing.\n\n\nGeneric.\nMore generic text.\n", encoding="utf-8")
    git(repo, "commit", "-q", "-am", "more")
    assert check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path))) == []


def test_tokens_and_names_wrapped_across_lines_match(tmp_path):
    findings = run(tmp_path, {"doc/a.md": "It printed Widget\n  overflow at startup.\nThe Acme\nLabs build was crashing.\n"})
    assert "doc/a.md:1: private token #1" in findings
    assert "doc/a.md:3: defect or limit about the target tool" in findings


def test_non_ascii_and_quoted_file_names_are_screened(tmp_path):
    findings = run(tmp_path, {"doc/na\u00efve \"notes\".md": "Acmepipe was crashing.\n"})
    assert findings and all(item.startswith('doc/na\u00efve "notes".md:1:') for item in findings)


def test_one_line_single_quoted_docstring_is_prose(tmp_path):
    code = "def helper():\n    'Acmepipe trial quirk.'\n    return 1\n"
    findings = run(tmp_path, {"pkg/mod.py": code})
    assert {item.split(":")[1] for item in findings} == {"2"}


def test_owner_words_keep_text_outside_the_span_and_reject_unpaired_markers(tmp_path):
    text = '<!-- owner-words -->"Acmepipe trial."<!-- /owner-words --> Acmepipe was crashing.\n'
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: defect or limit about the target tool"]
    with pytest.raises(ValueError):
        run(tmp_path / "u", {"doc/a.md": "<!-- owner-words -->\nAcmepipe was crashing.\n"})
    with pytest.raises(ValueError):
        run(tmp_path / "c", {"doc/a.md": "Acmepipe was crashing.\n<!-- /owner-words -->\n"})


def test_path_and_file_name_forms_are_masked_but_hyphenated_prose_is_not(tmp_path):
    text = "See `Design/acmepipe-notes.md`, acmepipe-pilot.md and core/acmepipe-x/; the check screens trial text.\n"
    assert run(tmp_path, {"doc/a.md": text}) == []
    findings = run(tmp_path / "h", {"doc/a.md": "Acmepipe-compatible output was crashing.\n"})
    assert findings == ["doc/a.md:1: defect or limit about the target tool"]
    findings = run(tmp_path / "s", {"doc/a.md": "The Acmepipe/Other comparison was crashing.\n"})
    assert findings == ["doc/a.md:1: defect or limit about the target tool"]

    for index, text in enumerate(("Acmepipe/9.99 was crashing.\n", "It was crashing in Acmepipe/Other.\n")):
        assert "doc/a.md:1: defect or limit about the target tool" in run(tmp_path / f"p{index}", {"doc/a.md": text})


@pytest.mark.parametrize("name, text", [
    ("pkg/mod.py", "x = 1  # Widget\n# overflow at startup.\n"),
    ("src/lib.rs", "let x = 1; // Widget\n/// overflow at startup.\n"),
    ("tools/a.ps1", "$x = 1 # Widget\n# overflow at startup.\n"),
    ("src/a.ts", "/* Widget\n * overflow at startup. */\n"),
    ("tools/b.ps1", "<# Widget\n#>\n# overflow at startup.\n"),
    ("src/b.rs", "fn f<'a>(x: &'a str) -> &'a str { x } // Widget overflow at startup.\n"),
    ("src/c.rs", "/* outer\n/* inner */\nWidget overflow at startup.\n*/\n"),
    ("src/b.ts", "const r = /\"/g; // Widget overflow at startup.\n"),
    ("tools/c.ps1", "$p = \"C:\\\" # Widget overflow at startup.\n"),
])
def test_wrapped_comments_join_without_comment_syntax(tmp_path, name, text):
    line = 1 + text.split("Widget")[0].count("\n")
    assert run(tmp_path, {name: text}) == [f"{name}:{line}: private token #1"]


def test_single_quoted_docstring_beside_a_comment_is_prose_but_code_literals_are_not(tmp_path):
    code = ("def helper():\n    'Acmepipe trial quirk.'  # note\n    return 1\n\n\n"
            "def test_values(): 'Acmepipe trial quirk.'\n\n\nTITLE = 'Acmepipe trial'  # generic note\n")
    findings = run(tmp_path, {"pkg/mod.py": code})
    assert {item.split(":")[1] for item in findings} == {"2", "6"}


def test_concatenated_and_non_ascii_docstrings_are_prose(tmp_path):
    code = "def helper(): 'generic ' 'Widget overflow at startup.'\n\n\ndef caf\u00e9(): 'Widget overflow at startup.'\n"
    assert run(tmp_path, {"pkg/mod.py": code}) == ["pkg/mod.py:1: private token #1", "pkg/mod.py:4: private token #1"]


def test_markdown_link_destinations_are_masked(tmp_path):
    assert run(tmp_path, {"doc/a.md": "See [details](Design/acmepipe-notes.md); trial notes.\n"}) == []
    findings = run(tmp_path / "t", {"doc/a.md": "See [Acmepipe](Design/notes.md); it was crashing.\n"})
    assert findings == ["doc/a.md:1: defect or limit about the target tool"]


def test_concatenated_docstring_fragments_join(tmp_path):
    code = "def helper():\n    'Widget ' 'overflow at startup.'\n"
    assert run(tmp_path, {"pkg/mod.py": code}) == ["pkg/mod.py:2: private token #1"]


@pytest.mark.parametrize("text", ["Widget **overflow** at startup.\n", "> Widget\n> overflow at startup.\n",
                                  "Widget `overflow` _at_ startup.\n"])
def test_markdown_formatting_does_not_hide_a_phrase(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]


@pytest.mark.parametrize("name, text", [
    ("doc/a.md", "Widget [overflow](errors.md) at startup.\n"),
    ("doc/b.md", "Widget [overflow][ref] at startup.\n"),
    ("src/lib.rs", "/// Widget **overflow** at startup.\nfn f() {}\n"),
    ("pkg/mod.py", "def helper():\n    \"\"\"Widget `overflow` at startup.\"\"\"\n"),
    ("pkg/two.py", "x = 1  # Widget [overflow](notes.md) at startup.\n"),
])
def test_links_and_formatting_do_not_hide_a_phrase_in_any_prose(tmp_path, name, text):
    line = 1 + text.split("Widget")[0].count("\n")
    assert run(tmp_path, {name: text}) == [f"{name}:{line}: private token #1"]



@pytest.mark.parametrize("text", [
    "Widget [overflow] at startup.\n\n[overflow]: notes.md\n",
    "Widget [overflow][ref] at startup.\n\n[ref]: notes.md\n",
    "Widget ![overflow](figure.png \"title\") at startup.\n",
    "Widget [overflow](https://example.invalid/a_(b)) at startup.\n",
    "Widget <em>overflow</em> at startup.\n",
    "Widget&nbsp;overflow&#32;at startup.\n",
])
def test_markdown_is_read_as_visible_text(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]


def test_a_link_wrapped_across_lines_keeps_its_label(tmp_path):
    findings = run(tmp_path, {"doc/a.md": "It printed Widget [overflow\nat](notes.md) startup.\n"})
    assert findings == ["doc/a.md:1: private token #1"]


@pytest.mark.parametrize("name, text", [
    ("doc/a.md", "The Acmepipe run on the\ninvented model, with its default settings,\nwas crashing to stop.\n"),
    ("pkg/mod.py", "# The Acmepipe run on the\n# invented model, with its default settings,\n# was crashing to stop.\n"),
    ("src/lib.rs", "// The Acmepipe run on the\n// invented model, with its default settings,\n// was crashing to stop.\n"),
    ("src/a.ts", "/* The Acmepipe run on the\n * invented model, with its default settings,\n * was crashing to stop. */\n"),
    ("tools/a.ps1", "# The Acmepipe run on the\n# invented model, with its default settings,\n# was crashing to stop.\n"),
])
def test_a_name_and_a_marker_in_one_sentence_match_across_lines(tmp_path, name, text):
    assert run(tmp_path, {name: text}) == [f"{name}:1: defect or limit about the target tool"]


def test_separate_sentences_and_paragraphs_more_than_a_line_apart_do_not_match(tmp_path):
    text = ("The Acmepipe manual documents batch runs. It has\nmany chapters on\ninputs. A run was crashing.\n\n"
            "The Acmepipe manual is public.\n\nA run was crashing.\n")
    assert run(tmp_path, {"doc/a.md": text}) == []


def test_escaped_continuations_in_docstrings_join(tmp_path):
    code = 'def helper():\n    """Widget \\\n    overflow at startup."""\n'
    assert run(tmp_path, {"pkg/mod.py": code}) == ["pkg/mod.py:2: private token #1"]



def test_table_rows_and_code_block_lines_are_separate_sentences(tmp_path):
    text = ("| Item | Value |\n|---|---|\n| Target | Acmepipe |\n| Notes | none |\n| Run | crashing |\n\n"
            "```\nacmepipe_out/   Acmepipe files\nx/\nparsed/   crashing\n```\n")
    assert run(tmp_path, {"doc/a.md": text}) == []
    text = "| Target | Acmepipe |\n| Run | crashing |\n"
    assert run(tmp_path / "w", {"doc/a.md": text}) == ["doc/a.md:1: defect or limit about the target tool"]



@pytest.mark.parametrize("text", [
    "Widget <!-- note -->overflow at startup.\n",
    "Widget<br>overflow at startup.\n",
    "Widget<p>overflow at startup.</p>\n",
    "Widget [overflow](https://example.invalid/a_(b_(c))) at startup.\n",
])
def test_html_comments_breaks_and_nested_destinations_do_not_hide_a_phrase(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]


def test_html_comment_bodies_are_screened(tmp_path):
    assert run(tmp_path, {"doc/a.md": "Generic text <!-- Widget overflow at startup --> here.\n"}) == [
        "doc/a.md:1: private token #1"]


def test_a_continuation_that_splits_a_word_reads_it_whole(tmp_path):
    code = 'def helper():\n    """The Acme\\\npipe run was crashing."""\n'
    assert run(tmp_path, {"pkg/mod.py": code}) == ["pkg/mod.py:2: defect or limit about the target tool"]
    code = 'def helper():\n    """Two\\\n    words stay apart."""\n'
    assert check.python_prose_lines(code)[3].lstrip("\x00").startswith("    words")



@pytest.mark.parametrize("text", [
    'Widget [overflow](notes.md "1) Details") at startup.\n',
    "Widget [overflow](notes.md '(a) b') at startup.\n",
    "Widget [overflow](notes\\).md) at startup.\n",
    "Widget [overflow](<notes (1).md>) at startup.\n",
    'Widget <span title="usage > capacity">overflow</span> at startup.\n',
    "Widget<br class='a > b'>overflow at startup.\n",
])
def test_link_titles_escapes_and_quoted_attributes_do_not_hide_a_phrase(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]


def test_whitespace_before_a_continuation_still_separates_words(tmp_path):
    code = '"""Acmepipe \\\nwas crashing."""\n'
    assert run(tmp_path, {"pkg/mod.py": code}) == ["pkg/mod.py:1: defect or limit about the target tool"]



@pytest.mark.parametrize("name, text", [
    ("doc/a.md", "The Acmepipe run used default settings, i.e.\nunchanged tolerances and limits,\nand was crashing to stop early.\n"),
    ("pkg/mod.py", "# The Acmepipe run used defaults, e.g.\n# unchanged tolerances and limits,\n# and was crashing to stop.\n"),
    ("src/lib.rs", "// The Acmepipe run (cf. the notes, etc.)\n// with unchanged tolerances and limits\n// was crashing to stop.\n"),
])
def test_abbreviations_do_not_end_a_sentence(tmp_path, name, text):
    assert run(tmp_path, {name: text}) == [f"{name}:1: defect or limit about the target tool"]


def test_real_sentence_ends_still_separate(tmp_path):
    text = "The Acmepipe manual is public. It has\nmany chapters on\ninputs. A run was crashing.\n"
    assert run(tmp_path, {"doc/a.md": text}) == []


def test_a_markdown_hard_break_does_not_hide_a_phrase(tmp_path):
    assert run(tmp_path, {"doc/a.md": "It printed Widget\\\noverflow at startup.\n"}) == ["doc/a.md:1: private token #1"]


@pytest.mark.parametrize("text", [
    "Acmepipe 9.99 writes displacements to 0.001 mm and forces to 1 N in its CSV.\n",
    "The record states whether the Acmepipe and SWBPIPE values match.\n",
    "Acmepipe results are compared per DEL-17-05 §7.1 (2026-10-26, REQ-018) and matched by node id.\n",
    "Acmepipe's MBF import does not accept FIXR records, so the writer refuses partial rotational restraints.\n",
    "SWBPIPE fails to converge when the model has 3 free nodes.\n",
    "The comparison record carries three values and three pairwise checks, so Acmepipe differs per quantity.\n",
    "Public material about Acmepipe is limited to invented models and the 3 m and 12 m spans.\n",
    "Acme Labs documents the batch route in its public manual.\n",
])
def test_interoperability_facts_and_the_bare_name_pass(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == []


@pytest.mark.parametrize("text", [
    "Acmepipe matched SWBPIPE in 20 of 35 quantities.\n",
    "The external prover's tip deflection differs from SWBPIPE by 0.04 mm.\n",
    "SWBPIPE matches the target tool within 0.5 % on every case.\n",
    "Acmepipe agreed with the hand calculation in 8 of 8 cases.\n",
    "The prover's 12 m residual was\na few ppm, 3 parts per million.\n",
])
def test_results_about_the_target_are_blocked(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: result about the target tool"]


@pytest.mark.parametrize("text", [
    "The batch route of Acmepipe crashes with a gadget fault.\n",
    "The external prover's evaluation build limits models to a small size.\n",
    "Acmepipe solves are slow on large models.\n",
    "Outputs of the target tool carry an evaluation stamp.\n",
    "Acmepipe 9.99 needs a workaround for its batch CSV.\n",
])
def test_defects_and_limits_of_the_target_are_blocked(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: defect or limit about the target tool"]


def test_screenshot_references_about_the_target_or_survey_are_blocked(tmp_path):
    assert run(tmp_path, {"doc/a.md": "See the Acmepipe screenshot of the results dialog.\n"}) == ["doc/a.md:1: screenshot reference"]
    assert run(tmp_path / "c", {"pkg/mod.py": "# from the survey's screen capture\nX = 1\n"}) == ["pkg/mod.py:1: screenshot reference"]
    assert run(tmp_path / "g", {"doc/a.md": "Keep generated reports and screenshots private by default.\n"}) == []


def test_a_neighbouring_line_counts_as_the_same_context(tmp_path):
    text = "Acmepipe 9.99 was run on the pilot cases.\nIts batch route crashed on every model.\n"
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: defect or limit about the target tool"]



def test_policy_text_is_not_screened_and_must_be_paired(tmp_path):
    text = ("<!-- policy-text -->Acmepipe defects, trial limits and screenshots stay private.<!-- /policy-text -->\n"
            "The Acmepipe trial crashed.\n")
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:2: defect or limit about the target tool"]
    with pytest.raises(ValueError):
        run(tmp_path / "u", {"doc/a.md": "<!-- policy-text -->\nAcmepipe crashed.\n"})


def test_the_check_does_not_screen_its_own_source(tmp_path):
    files = {"tools/caepipe_correlation/check_public_observations.py": "# Acmepipe crashes are screened here.\n",
             "tests/test_check_public_observations.py": "# Acmepipe crashed.\n"}
    assert run(tmp_path, files) == []


def test_a_unit_ratio_is_not_a_result(tmp_path):
    assert run(tmp_path, {"doc/a.md": "An Acmepipe difference uses standard gravity 9.80665 m/s2 as assumed.\n"}) == []



@pytest.mark.parametrize("text", [
    "Acmepipe differs from SWBPIPE by 3 mm at the tip.\n",
    "Acmepipe matched all 12 quantities.\n",
])
def test_integer_results_and_counts_are_blocked(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: result about the target tool"]


@pytest.mark.parametrize("text", [
    "Acmepipe CSV sections have 2 rows of headers.\n",
    "The importer converts Acmepipe inch lengths at 25.4 mm per inch, so values match exactly.\n",
    "Acmepipe weights in kgf convert at 9.80665 N/kgf, and the writer differs only in units.\n",
    "Survey proposals describe a trial feature in the project's own words.\n",
    "The Acmepipe user's manual gives no default for the gravitational acceleration.\n",
])
def test_format_facts_conversions_and_survey_context_pass(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == []


def test_a_row_limit_is_blocked(tmp_path):
    assert run(tmp_path, {"doc/a.md": "Acmepipe imports at most 20 rows.\n"}) == [
        "doc/a.md:1: defect or limit about the target tool"]


def test_private_tokens_are_screened_inside_exempt_spans_and_the_checks_own_files(tmp_path):
    text = "<!-- policy-text -->Rule text: Widget overflow at start.<!-- /policy-text -->\n"
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]
    text = "<!-- owner-words -->\"Widget overflow at start\"<!-- /owner-words -->\n"
    assert run(tmp_path / "o", {"doc/a.md": text}) == ["doc/a.md:1: private token #1"]
    files = {"tools/caepipe_correlation/check_public_observations.py": "# Widget overflow at start\n"}
    assert run(tmp_path / "s", files) == ["tools/caepipe_correlation/check_public_observations.py:1: private token #1"]



def test_signed_results_are_blocked(tmp_path):
    assert run(tmp_path, {"doc/a.md": "The Acmepipe residual is -3 mm against SWBPIPE.\n"}) == [
        "doc/a.md:1: result about the target tool"]


@pytest.mark.parametrize("text", [
    "The Acmepipe importer matches 3 values to X/Y/Z.\n",
    "Acmepipe units differ: 1 in = 25.4 mm.\n",
    "Acmepipe writes no delimiter after the final field.\n",
    "See [REQ-018](notes.md): Acmepipe records match per DEL-17-04.\n",
])
def test_mapping_counts_equations_and_format_omissions_pass(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == []


def test_image_links_of_the_target_are_screenshot_references(tmp_path):
    assert run(tmp_path, {"doc/a.md": "![Acmepipe dialog](screenshots/result.png)\n"}) == [
        "doc/a.md:1: screenshot reference"]
    assert run(tmp_path / "d", {"doc/a.md": "![Load path diagram](diagram.png)\n"}) == []



def test_a_result_equality_is_not_a_unit_conversion(tmp_path):
    assert run(tmp_path, {"doc/a.md": "Acmepipe agreement: 12/12 = 100%.\n"}) == ["doc/a.md:1: result about the target tool"]


def test_mapping_with_a_scope_word_passes(tmp_path):
    assert run(tmp_path, {"doc/a.md": "The Acmepipe importer matches all 3 values to X/Y/Z.\n"}) == []


def test_reference_style_images_of_the_target_are_screenshot_references(tmp_path):
    text = "![Acmepipe dialog][shot]\n\n[shot]: result.png\n"
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: screenshot reference"]
    assert run(tmp_path / "s", {"doc/a.md": "![Acmepipe dialog]\n"}) == ["doc/a.md:1: screenshot reference"]


def test_original_format_diagrams_pass(tmp_path):
    assert run(tmp_path, {"doc/a.md": "![Acmepipe MBF record layout](layout.svg)\n"}) == []
    assert run(tmp_path / "r", {"doc/a.md": "![Acmepipe record diagram][d]\n\n[d]: d.png\n"}) == []



@pytest.mark.parametrize("text", [
    "Acmepipe and SWBPIPE agree: 3 mm = 3 mm.\n",
    "Acmepipe matched all 12 values to 3 decimal places.\n",
])
def test_same_unit_equalities_and_precision_matches_are_results(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: result about the target tool"]


def test_screenshot_cues_beat_generic_diagram_words(tmp_path):
    assert run(tmp_path, {"doc/a.md": "![Acmepipe layout window](screenshots/run.png)\n"}) == [
        "doc/a.md:1: screenshot reference"]


def test_reference_image_destinations_are_resolved(tmp_path):
    assert run(tmp_path, {"doc/a.md": "![Acmepipe MBF][d]\n\n[d]: layout.svg\n"}) == []
    assert run(tmp_path / "s", {"doc/a.md": "![Acmepipe MBF][d]\n\n[d]: shots/run.png\n"}) == [
        "doc/a.md:1: screenshot reference"]



def test_a_changed_image_definition_alone_is_screened(tmp_path):
    repo = repo_with(tmp_path, {"doc/a.md": "![Acmepipe MBF][d]\n\n[d]: layout.svg\n"})
    git(repo, "branch", "-f", "main", "topic")
    (repo / "doc/a.md").write_text("![Acmepipe MBF][d]\n\n[d]: shots/run.png\n", encoding="utf-8")
    git(repo, "commit", "-q", "-am", "swap")
    assert check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path))) == [
        "doc/a.md:1: screenshot reference"]


def test_equations_reporting_agreement_are_results(tmp_path):
    assert run(tmp_path, {"doc/a.md": "Acmepipe and Otherpipe agree: 3 mm = 0.3 cm.\n"}) == [
        "doc/a.md:1: result about the target tool"]


def test_a_mapping_to_listed_fields_passes(tmp_path):
    assert run(tmp_path, {"doc/a.md": "The Acmepipe importer matches all 3 values to `x`, `y`, and `z` fields.\n"}) == []



def test_a_reference_image_keeps_its_own_line_context(tmp_path):
    assert run(tmp_path, {"doc/a.md": "Acmepipe output.\n![View][d]\n\n[d]: run.png\n"}) == [
        "doc/a.md:1: screenshot reference"]


def test_a_precision_clause_is_not_a_mapping(tmp_path):
    text = "Acmepipe matches all 12 values to 3 decimal places in the output fields.\n"
    assert run(tmp_path, {"doc/a.md": text}) == ["doc/a.md:1: result about the target tool"]


def test_an_equation_stated_as_cross_tool_agreement_is_a_result(tmp_path):
    # Invented sentences: a unit definition used as an agreement statement is screened; one beside a difference
    # word stays a format fact.
    assert run(tmp_path / "a", {"doc/a.md": "Acmepipe and Otherpipe agree: 1 mm = 0.1 cm.\n"}) == [
        "doc/a.md:1: result about the target tool"]
    for index, word in enumerate(("agrees", "agreed", "agreement", "match", "matches", "matched")):
        findings = run(tmp_path / f"w{index}", {"doc/a.md": f"Acmepipe {word} here: 1 mm = 0.1 cm.\n"})
        assert findings == ["doc/a.md:1: result about the target tool"], word
    assert run(tmp_path / "d", {"doc/a.md": "Acmepipe units differ: 1 in = 25.4 mm.\n"}) == []



# Benchmark agreement is published only in the designated surface, as a summary rendered from data, once the owner's
# ruling record exists, validates and quotes the owner's words (owner, 2026-10-28). Every sentence, identifier,
# value and ruling below is invented.
SURFACE = check.PUBLISHED_SURFACE
LOOP = check.GATE_RECORD
REPORT_PATH = SURFACE + "report.md"
TOLERANCE_WORDS = "Class TC-1: 0.5 % on displacements and 1 N on forces."
LICENCE_WORDS = "I have read the full licence and the download terms."
LOOP_TEXT = ("# Loop\n\n## Rulings\n\n"
             f"Owner, 2026-11-02: <!-- owner-words -->\"{TOLERANCE_WORDS}\"<!-- /owner-words -->\n"
             f"Owner, 2026-11-01: <!-- owner-words -->{LICENCE_WORDS}<!-- /owner-words -->\n")
RULING = {"document_kind": "swbpipe.caepipe_benchmark_ruling", "ruled_on": "2026-11-02", "tolerance_class": "TC-1",
          "families": [{"id": "displacements", "threshold": 0.5, "unit": "%"},
                       {"id": "forces", "threshold": 1, "unit": "N"}],
          "licence_terms_checked": True, "licence_terms_checked_on": "2026-11-01",
          "owner_words": [TOLERANCE_WORDS, LICENCE_WORDS]}
SUMMARY = {"document_kind": "swbpipe.caepipe_benchmark_summary", "benchmark_set": {"id": "BS-1", "version": "3"},
           "caepipe_version": "9.99", "models": 12, "cases": 35,
           "families": [{"id": "forces", "agreed": 34, "total": 35, "max_difference": 1.2, "unit": "N"},
                        {"id": "displacements", "agreed": 35, "total": 35, "max_difference": 0.12, "unit": "%"}]}
AGREEMENT_TEXT = "SWBPIPE and Acmepipe 9.99 agree within 0.5 % on 35 of 35 quantities.\n"
RELIANCE = ("<!-- reliance -->\n" + check.RELIANCE_STATEMENT + "\n<!-- /reliance -->\n")
SUMMARY_KINDS = {"benchmark summary without the owner's ruling record", "benchmark summary does not validate against its schema",
                 "benchmark summary families differ from the owner's ruling", "benchmark summary unit differs from the owner's ruling",
                 "benchmark summary agreement count exceeds its total", "benchmark summary Markdown differs from its rendering",
                 "benchmark summary missing or not a regular file", "benchmark summary is not well-formed JSON"}


def dump(document) -> str:
    return check.json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def rendered(summary=SUMMARY, ruling=RULING) -> str:
    return check.render_summary(summary, ruling)


def published(ruling=RULING, summary=SUMMARY, loop: str = LOOP_TEXT, text: str | None = None, **files: str) -> dict:
    out = {LOOP: loop, check.SUMMARY_DATA: dump(summary),
           check.SUMMARY_TEXT: rendered(summary, RULING) if text is None else text, **files}
    if ruling is not None:
        out[check.RULING_RECORD] = dump(ruling)
    return out


def kinds(findings: list[str]) -> set[str]:
    return {item.split(": ", 1)[1] for item in findings}


def commit_links(repo: Path, links: dict[str, str]) -> None:
    for name, target in links.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.symlink_to(target)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "links")


def run_links(tmp_path: Path, files: dict[str, str], links: dict[str, str]) -> list[str]:
    repo = repo_with(tmp_path, files)
    commit_links(repo, links)
    return check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path)))


def test_a_rendered_summary_passes_with_a_valid_ruling_record(tmp_path):
    assert run(tmp_path, published(**{SURFACE + "README.md": "# Folder\n\n" + RELIANCE})) == []
    text = rendered()
    # Families follow the ruling's order; thresholds and units come from the ruling, differences from the data.
    assert "| Displacements | 35 of 35 | 0.12 % | 0.5 % |\n| Forces | 34 of 35 | 1.2 N | 1 N |" in text
    assert "Tolerance class: TC-1, ruled by the owner on 2026-11-02" in text and check.RELIANCE_STATEMENT in text


def blank_after_version(text: str) -> str:
    return text.replace("- CAEPIPE version: 9.99\n", "- CAEPIPE version: 9.99\n\n")


def fenced(text: str) -> str:
    return "```\n" + text + "```\n"


# Round 2, P1: with the gate unset, a summary passed after a blank line after the version or inside a code fence.
@pytest.mark.parametrize("variant", [lambda text: text, blank_after_version, fenced])
def test_without_a_ruling_record_any_summary_file_is_refused_whatever_its_formatting(tmp_path, variant):
    files = published(ruling=None, text=variant(rendered()))
    findings = run(tmp_path, files)
    assert {f"{check.SUMMARY_DATA}:1: benchmark summary without the owner's ruling record",
            f"{check.SUMMARY_TEXT}:1: benchmark summary without the owner's ruling record"} <= set(findings)
    only_text = {key: value for key, value in files.items() if key != check.SUMMARY_DATA}
    assert f"{check.SUMMARY_TEXT}:1: benchmark summary without the owner's ruling record" in run(tmp_path / "t", only_text)


@pytest.mark.parametrize("variant", [lambda text: text, blank_after_version, fenced])
@pytest.mark.parametrize("ruled", [True, False])
def test_a_summary_elsewhere_in_the_surface_is_refused_whatever_its_formatting(tmp_path, variant, ruled):
    files = published(ruling=RULING if ruled else None, **{REPORT_PATH: variant(rendered())})
    files.pop(check.SUMMARY_DATA), files.pop(check.SUMMARY_TEXT)
    assert "result number in the published surface outside the rendered summary" in kinds(run(tmp_path, files))


@pytest.mark.parametrize("path", ["doc/report.md", "projects/chirality-piping/validation/caepipe_benchmark/report.md",
                                  "projects/chirality-piping/validation/caepipe_benchmark/published-draft/summary.md"])
def test_a_summary_outside_the_surface_is_refused_with_the_ruling_recorded(tmp_path, path):
    assert "result about the target tool" in kinds(run(tmp_path, published(**{path: AGREEMENT_TEXT})))


def test_agreement_in_the_surface_outside_the_rendered_summary_is_refused(tmp_path):
    findings = kinds(run(tmp_path, published(**{SURFACE + "notes.md": "Displacements: 35/35.\n\nForces: 0.3 N.\n"})))
    assert findings == {"result number in the published surface outside the rendered summary"}


@pytest.mark.parametrize("edit", [
    lambda text: text.replace("| 0.5 % |", "| 0.6 % |"),  # a threshold that is not the ruling's
    lambda text: text.replace("0.12 %", "0.12 mm"),
    lambda text: text + "\nThe n1 displacement was 1.234 mm in both.\n",  # a raw value
    lambda text: text.replace("\n\n|", "\n|", 1),
    lambda text: text.rstrip("\n"),
])
def test_summary_markdown_must_equal_its_rendering_exactly(tmp_path, edit):
    findings = run(tmp_path, published(text=edit(rendered())))
    assert f"{check.SUMMARY_TEXT}:1: benchmark summary Markdown differs from its rendering" in findings


def family(**changes) -> dict:
    return {**SUMMARY, "families": [{**SUMMARY["families"][0], **changes}, SUMMARY["families"][1]]}


# Round 2, P1: thresholds are bound to explicit, family-specific owner rulings with exact units.
@pytest.mark.parametrize("summary, kind", [
    (family(unit="kN"), "benchmark summary unit differs from the owner's ruling"),  # a unit prefix
    ({**SUMMARY, "families": [SUMMARY["families"][1], {**SUMMARY["families"][1], "unit": "mm"}]},
     "benchmark summary families differ from the owner's ruling"),  # one family twice
    (family(id="moments", unit="N·m"), "benchmark summary families differ from the owner's ruling"),  # not ruled
    ({**SUMMARY, "families": SUMMARY["families"][1:]}, "benchmark summary families differ from the owner's ruling"),
    (family(threshold=1), "benchmark summary does not validate against its schema"),  # thresholds are the ruling's
    (family(max_difference="1.2 N"), "benchmark summary does not validate against its schema"),
    (family(max_difference=-0.1), "benchmark summary does not validate against its schema"),
    (family(agreed=36), "benchmark summary agreement count exceeds its total"),
    (family(unit="mm"), "benchmark summary does not validate against its schema"),  # a displacement unit on forces
    ({**SUMMARY, "models": 0}, "benchmark summary does not validate against its schema"),
    ({**SUMMARY, "notes": "per-model listing"}, "benchmark summary does not validate against its schema"),
    ({**SUMMARY, "caepipe_version": "9.99 (evaluation)"}, "benchmark summary does not validate against its schema"),
])
def test_summary_data_must_match_the_ruling_and_its_schema(tmp_path, summary, kind):
    files = published(summary=summary, text=rendered())  # the valid rendering, so only the data is wrong
    findings = run(tmp_path, files)
    assert f"{check.SUMMARY_DATA}:1: {kind}" in findings


def test_malformed_or_missing_summary_files_are_refused(tmp_path):
    files = published()
    files[check.SUMMARY_DATA] = '{"models": 1, "models": 2}\n'
    assert kinds(run(tmp_path / "d", files)) >= {"benchmark summary is not well-formed JSON"}
    files = published()
    files[check.SUMMARY_DATA] = dump(SUMMARY).replace("0.12", "NaN")
    assert "benchmark summary is not well-formed JSON" in kinds(run(tmp_path / "n", files))
    files = published()
    files.pop(check.SUMMARY_TEXT)
    assert f"{check.SUMMARY_TEXT}:1: benchmark summary missing or not a regular file" in run(tmp_path / "m", files)


def test_a_symlinked_summary_is_refused(tmp_path):
    files = published(**{SURFACE + "real.md": rendered()})
    files.pop(check.SUMMARY_TEXT)
    findings = run_links(tmp_path, files, {check.SUMMARY_TEXT: "real.md"})
    assert f"{check.SUMMARY_TEXT}:1: benchmark summary missing or not a regular file" in findings


def ruling(**changes) -> dict:
    return {**RULING, **changes}


@pytest.mark.parametrize("record", [
    ruling(ruled_on="2026-02-30"), ruling(licence_terms_checked_on="2026-13-01"), ruling(ruled_on="2 Nov 2026"),
    ruling(licence_terms_checked=False), ruling(licence_terms_checked="yes"),
    {key: value for key, value in RULING.items() if key != "owner_words"}, ruling(owner_words=[]),
    ruling(owner_words=["0.5 %"]),  # too short to be the owner's ruling words
    ruling(owner_words=["Class TC-1: 0.5 % on displacements and 2 N on forces."]),  # not the owner's words
    ruling(families=[]), ruling(families=RULING["families"] + [RULING["families"][0]]),  # a family twice
    ruling(families=[{"id": "displacements", "threshold": 0.5, "unit": "N"}]),  # a force unit on displacements
    ruling(families=[{"id": "displacements", "threshold": 0.5, "unit": "inch"}]),  # outside the closed list
    ruling(families=[{"id": "displacements", "threshold": "0.5 %", "unit": "%"}]),
    ruling(families=[{"id": "displacements", "threshold": 0, "unit": "%"}]),
    ruling(families=[{"id": "stresses", "threshold": 1, "unit": "%"}]),
    ruling(tolerance_class="TC 1"), ruling(document_kind="swbpipe.other"), ruling(extra="x"),
])
def test_an_invalid_ruling_record_is_an_operational_error(tmp_path, record):
    files = published(ruling=record)
    with pytest.raises(ValueError):
        run(tmp_path, files)
    assert check.main(["--terms-file", str(write_terms(tmp_path)), "--repo", str(tmp_path / "repo"), "--base", "main",
                       "--head", "topic"]) == 2


def test_a_ruling_record_with_a_duplicate_key_or_a_symlink_is_an_operational_error(tmp_path):
    files = published()
    files[check.RULING_RECORD] = dump(RULING).replace('"ruled_on": "2026-11-02"',
                                                      '"ruled_on": "2026-11-02", "ruled_on": "2026-11-03"')
    with pytest.raises(ValueError):
        run(tmp_path / "k", files)
    files = published(**{"projects/chirality-piping/loop/rulings/real.json": dump(RULING)})
    files.pop(check.RULING_RECORD)
    with pytest.raises(ValueError):
        run_links(tmp_path / "s", files, {check.RULING_RECORD: "real.json"})
    files = published(**{"projects/chirality-piping/loop/real.md": LOOP_TEXT})
    files.pop(LOOP)
    with pytest.raises(ValueError):
        run_links(tmp_path / "l", files, {LOOP: "real.md"})


def quoted(words: str) -> str:
    return "<!-- owner-words -->" + words + "<!-- /owner-words -->"


# Round 2, P1: owner markers inside fenced or HTML-commented examples activated the gate.
@pytest.mark.parametrize("loop", [
    "# Loop\n\n```markdown\n" + quoted(TOLERANCE_WORDS) + "\n```\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\n~~~~\n" + quoted(TOLERANCE_WORDS) + "\n~~~~\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\n<!--\nExample: " + quoted(TOLERANCE_WORDS) + "\n-->\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\n<!-- " + TOLERANCE_WORDS + " -->\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\n" + quoted("<!-- " + TOLERANCE_WORDS + " -->") + "\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\nWrite `" + quoted(TOLERANCE_WORDS) + "` for a ruling.\n\n" + quoted(LICENCE_WORDS) + "\n",
    "# Loop\n\n    " + quoted(TOLERANCE_WORDS) + "\n\n" + quoted(LICENCE_WORDS) + "\n",  # indented code
    "# Loop\n\n" + TOLERANCE_WORDS + "\n\n" + quoted(LICENCE_WORDS) + "\n",  # words without the span
    "# Loop\n\n" + quoted(TOLERANCE_WORDS) + "\n\n<!-- owner-words -->" + LICENCE_WORDS + "\n",  # unpaired
])
def test_ruling_words_count_only_in_live_owner_words_spans(tmp_path, loop):
    with pytest.raises(ValueError):
        run(tmp_path, published(loop=loop))


def test_ruling_words_wrapped_across_lines_in_a_live_span_count(tmp_path):
    loop = ("# Loop\n\n```text\nan example\n```\n\nOwner: <!-- owner-words -->Class TC-1: 0.5 % on\ndisplacements and "
            "1 N on forces.<!-- note --><!-- /owner-words --> and " + quoted(LICENCE_WORDS) + "\n")
    assert run(tmp_path, published(loop=loop)) == []


def test_the_render_command_writes_the_rendering_of_the_working_tree(tmp_path, capsys):
    repo = repo_with(tmp_path, published())
    assert check.main(["--render-summary", "--repo", str(repo)]) == 0
    assert capsys.readouterr().out == rendered()
    (repo / check.SUMMARY_DATA).write_text(dump(family(unit="kN")), encoding="utf-8")
    assert check.main(["--render-summary", "--repo", str(repo)]) == 2


@pytest.mark.parametrize("links", [
    {SURFACE + "alias.md": "../../../../doc/a.md"},  # in the surface
    {"doc/alias": "../projects/chirality-piping/validation/caepipe_benchmark/published"},  # into it
    {"doc/deep": "../projects/chirality-piping/validation"},  # above it
    {"projects/chirality-piping/validation/caepipe_benchmark": "../../../doc"},  # on its path
    {"doc/absolute": "/elsewhere/projects/chirality-piping/validation/caepipe_benchmark/published/x.md"},
])
def test_a_symlink_in_or_into_the_surface_is_refused(tmp_path, links):
    findings = run_links(tmp_path, {"doc/a.md": "generic\n"}, links)
    assert "symlink in or into the published surface" in kinds(findings)


def repo_with_base_links(tmp_path: Path, links: dict[str, str]) -> Path:
    """A repository whose main already holds `links` and a surface file."""

    repo = tmp_path / "repo"
    repo.mkdir(parents=True)
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "invented@example.invalid")
    git(repo, "config", "user.name", "Invented")
    (repo / SURFACE).mkdir(parents=True)
    (repo / SURFACE / "README.md").write_text("generic\n", encoding="utf-8")
    commit_links(repo, links)
    git(repo, "checkout", "-q", "-b", "topic")
    return repo


# Round 2, P3: an alias through an existing intermediate symlink passed.
@pytest.mark.parametrize("base_links, alias", [
    ({"doc/v": "../projects/chirality-piping/validation"}, "v/caepipe_benchmark/published"),
    ({"doc/v": "../projects/chirality-piping/validation", "doc/w": "v"}, "w/caepipe_benchmark"),
    ({"doc/up": "../projects/chirality-piping"}, "up/validation/./caepipe_benchmark/published/../published/README.md"),
    ({"doc/v": "../projects/chirality-piping/validation/caepipe_benchmark/published"}, "v/../../../../../doc"),
])
def test_a_symlink_chain_through_existing_links_into_or_through_the_surface_is_refused(tmp_path, base_links, alias):
    repo = repo_with_base_links(tmp_path, base_links)
    commit_links(repo, {"doc/alias": alias})
    findings = check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path)))
    assert findings == ["doc/alias:1: symlink in or into the published surface"]


def test_an_unrelated_symlink_or_chain_passes(tmp_path):
    assert run_links(tmp_path / "a", {"doc/a.md": "generic\n"}, {"doc/alias.md": "a.md"}) == []
    repo = repo_with_base_links(tmp_path / "c", {"doc/v": "../projects/chirality-piping/tools"})
    commit_links(repo, {"doc/alias": "v/x.py"})
    assert check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path))) == []


def test_policy_text_and_owner_words_exempt_nothing_in_the_surface(tmp_path):
    text = "<!-- policy-text -->\nAcmepipe 9.99 crashed.\n<!-- /policy-text -->\n"
    assert kinds(run(tmp_path / "s", published(**{SURFACE + "notes.md": text}))) == {"defect or limit about the target tool"}
    assert run(tmp_path / "o", published(**{"doc/notes.md": text})) == []


def test_agreement_in_a_commit_message_is_refused_with_a_summary_published(tmp_path):
    repo = repo_with(tmp_path, published())
    (repo / "doc").mkdir()
    (repo / "doc/b.md").write_text("generic\n", encoding="utf-8")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", AGREEMENT_TEXT)
    findings = check.check_range(repo, "main", "topic", check.load_terms(write_terms(tmp_path)))
    assert findings and all(item.startswith("commit ") for item in findings)
    assert kinds(findings) == {"result about the target tool"}


@pytest.mark.parametrize("ruled", [True, False])
@pytest.mark.parametrize("text", [
    "The benchmark agreement validates the design.\n",
    "This benchmark marks the release of SWBPIPE.\n",
    "SWBPIPE is production-ready.\n",
    check.RELIANCE_STATEMENT + "\n",  # the canonical sentence without its marker
])
def test_framing_as_acceptance_compliance_or_release_is_refused_in_the_surface(tmp_path, ruled, text):
    files = published(ruling=RULING if ruled else None, **{SURFACE + "notes.md": text})
    if not ruled:
        files.pop(check.SUMMARY_DATA), files.pop(check.SUMMARY_TEXT)
    assert "acceptance or compliance framing in the published surface" in kinds(run(tmp_path, files))


def test_framing_words_outside_the_surface_are_not_screened(tmp_path):
    assert run(tmp_path, published(**{"doc/a.md": "The checks validate the parser before the release.\n"})) == []


def test_only_the_canonical_reliance_sentence_is_exempt(tmp_path):
    assert run(tmp_path / "c", {SURFACE + "README.md": "# Folder\n\n" + RELIANCE}) == []
    altered = RELIANCE.replace("stays with the user", "stays with the user; the design is validated")
    findings = run(tmp_path / "a", {SURFACE + "README.md": "# Folder\n\n" + altered})
    assert "reliance statement differs from the canonical sentence" in kinds(findings)
    assert "acceptance or compliance framing in the published surface" in kinds(findings)


@pytest.mark.parametrize("text", [
    "Acmepipe and SWBPIPE agree closely.\n",
    "Acmepipe 9.99 shows no significant differences from SWBPIPE.\n",
    "The results are identical in Acmepipe.\n",
    "SWBPIPE stays within tolerance of Acmepipe.\n",
    "Acmepipe gives the same displacements as SWBPIPE.\n",
    # Round 2, P3: bare agreement assertions, without numbers or adverbs.
    "Acmepipe agrees with SWBPIPE.\n",
    "The Acmepipe results match SWBPIPE.\n",
    "SWBPIPE is in agreement with Acmepipe.\n",
    "Acmepipe corroborates the SWBPIPE model.\n",
    "Acmepipe reproduces the SWBPIPE results.\n",
    "The target tool and SWBPIPE agreed.\n",
])
@pytest.mark.parametrize("path", ["doc/a.md", SURFACE + "notes.md"])
def test_qualitative_agreement_is_refused_in_and_outside_the_surface(tmp_path, text, path):
    assert kinds(run(tmp_path, {path: text})) == {"qualitative result about the target tool"}


# Round 2, P2: interface facts about formats are not results.
@pytest.mark.parametrize("text", [
    "The Acmepipe importer uses the same displacement sign convention as SWBPIPE.\n",
    "Acmepipe and SWBPIPE use identical force labels.\n",
    "Acmepipe writes the same moment units as the MBF records.\n",
    "The Acmepipe CSV keeps the same reaction column order as SWBPIPE.\n",
    "The Acmepipe importer uses the same sign convention as SWBPIPE.\n",
    "The Acmepipe batch dialog writes the CSV.\n",
    "The record states whether the Acmepipe and SWBPIPE values agree.\n",
    "Acmepipe agrees to the licence prompt only through the dialog.\n",
])
def test_format_facts_near_the_result_classes_pass(tmp_path, text):
    assert run(tmp_path, {"doc/a.md": text}) == []


# Round 2, P3: neutral survey notes passed.
@pytest.mark.parametrize("text", [
    "Survey note: the editor keeps two undo stacks.\n",
    "Survey notes — loads are grouped by case.\n",
    "From the survey, the editor groups loads by case.\n",
    "According to our survey notes the results view has tabs.\n",
    "The survey notes record a tabbed results view.\n",
    "The survey found a tree of load cases.\n",
])
@pytest.mark.parametrize("path", ["doc/a.md", SURFACE + "notes.md"])
def test_survey_note_text_is_refused(tmp_path, text, path):
    assert kinds(run(tmp_path, {path: text})) == {"survey-note text"}


@pytest.mark.parametrize("text", [
    "The Acmepipe load dialog is clunky.\n",
    "Acmepipe has a steep learning curve.\n",
    "Survey note: the results window is hard to navigate.\n",
])
@pytest.mark.parametrize("path", ["doc/a.md", SURFACE + "notes.md"])
def test_user_interface_critique_is_refused_in_and_outside_the_surface(tmp_path, text, path):
    assert "user-interface critique of the target tool" in kinds(run(tmp_path, {path: text}))


@pytest.mark.parametrize("text", [
    '[manual](https://example.invalid/m "Acmepipe crashed here")\n',
    '<span title="Acmepipe crashed">note</span>\n',
    "<abbr title='Acmepipe trial build'>TB</abbr>\n",
    '<td title="Acmepipe crashed">x</td>\n',
])
def test_link_titles_and_tag_attributes_are_screened(tmp_path, text):
    assert kinds(run(tmp_path, {"doc/a.md": text})) == {"defect or limit about the target tool"}


def test_whole_file_mode_has_no_surface(tmp_path):
    report = tmp_path / "report.md"
    report.write_text("Acmepipe 9.99 agrees within 0.5 % on 35 of 35 quantities.\n", encoding="utf-8")
    assert check.main(["--terms-file", str(write_terms(tmp_path)), "--file", str(report)]) == 1


def test_nothing_is_published_at_the_checked_in_state():
    # Nothing is published before the owner rules the tolerance class and checks the licence terms (Design §8.1).
    root = ROOT.parents[1]
    assert not (root / check.RULING_RECORD).exists()
    assert not (root / check.SUMMARY_DATA).exists() and not (root / check.SUMMARY_TEXT).exists()


def test_the_schemas_list_the_checks_families_and_units():
    for name in (check.RULING_SCHEMA, check.SUMMARY_SCHEMA):
        schema = check.json.loads((check.SCHEMAS / name).read_text(encoding="utf-8"))
        assert schema["$defs"]["family_id"]["enum"] == list(check.FAMILIES)
        assert schema["$defs"]["unit"]["enum"] == list(check.UNITS)
    assert check._valid(RULING, check.RULING_SCHEMA) and check._valid(SUMMARY, check.SUMMARY_SCHEMA)
