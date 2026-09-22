#!/usr/bin/env python3
"""Compare rendered manual content with the parser baseline and check local links.

Run from the repository root after rendering. This is run evidence, not a new
repository-wide test suite. The JSON output records the exact inspected bytes.
"""

from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "docs/alignment-manual/CHIRALITY_AGENT_USER_MANUAL_v1.md"
HTML = SOURCE.with_suffix(".html")
MD = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])


class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.counts = Counter()
        self.text = []
        self.links = []
        self.ids = []
        self.active = []
        self.parts = {tag: [] for tag in ["p", "table", "pre", "h1", "h2", "h3", "h4", "h5", "h6"]}
        self.assets = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.counts[tag] += 1
        if tag in self.parts:
            self.active.append([tag, []])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("name") and attrs.get("name") != attrs.get("id"):
            self.ids.append(attrs["name"])
        for attr in ("src", "srcset", "poster"):
            if attrs.get(attr) and not attrs[attr].startswith("data:"):
                self.assets.append([tag, attr, attrs[attr]])
        if tag == "link" and attrs.get("href"):
            self.assets.append([tag, "href", attrs["href"]])

    def handle_endtag(self, tag):
        if self.active and self.active[-1][0] == tag:
            name, text = self.active.pop()
            self.parts[name].append("".join(text))

    def handle_data(self, data):
        self.text.append(data)
        for _, text in self.active:
            text.append(data)


def normalize(text):
    return " ".join(text.split())


def markdown_targets(path):
    tokens = MD.parse(path.read_text(encoding="utf-8"))
    parsed = Audit()
    parsed.feed(MD.renderer.render(tokens, MD.options, {}))
    targets = set(parsed.ids)
    slugs = Counter()
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        inline = Audit()
        inline.feed(MD.renderer.renderInline(tokens[index + 1].children or [], MD.options, {}))
        heading = unicodedata.normalize("NFC", "".join(inline.text)).lower()
        base = re.sub(r"[^\w\-\s]", "", heading, flags=re.UNICODE).strip()
        base = re.sub(r"\s", "-", base)
        count = slugs[base]
        slugs[base] += 1
        targets.add(f"{base}-{count}" if count else base)
    return targets


def main():
    html = HTML.read_text(encoding="utf-8")
    start, end = "<!-- BEGIN MARKDOWN CONTENT -->\n", "<!-- END MARKDOWN CONTENT -->"
    assert html.count(start) == 1 and html.count(end) == 1, "Missing or ambiguous source-content markers"
    body = html.split(start, 1)[1].split(end, 1)[0]
    expected, actual, page = Audit(), Audit(), Audit()
    expected.feed(MD.render(SOURCE.read_text(encoding="utf-8")))
    actual.feed(body)
    page.feed(html)
    checks = {
        "visible_text_parity": normalize("".join(expected.text)) == normalize("".join(actual.text)),
        "paragraph_parity": expected.parts["p"] == actual.parts["p"],
        "table_content_parity": expected.parts["table"] == actual.parts["table"],
        "code_block_exact_text_parity": expected.parts["pre"] == actual.parts["pre"],
        "heading_content_parity": all(expected.parts[tag] == actual.parts[tag] for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]),
        "source_link_sequence_parity": expected.links == actual.links,
        "source_element_count_parity": all(actual.counts[tag] == count for tag, count in expected.counts.items() if tag != "div"),
        "source_div_count_plus_table_wrappers": actual.counts["div"] == expected.counts["div"] + expected.counts["table"],
        "no_duplicate_page_ids": len(page.ids) == len(set(page.ids)),
        "all_in_page_targets_exist": all(unquote(link[1:]) in page.ids or link == "#" for link in page.links if link.startswith("#")),
        "no_non_embedded_assets": not page.assets,
        "source_sha256_visible": hashlib.sha256(SOURCE.read_bytes()).hexdigest() in html,
    }
    local_links, failures, cache = [], [], {}
    for link in sorted(set(page.links)):
        parts = urlsplit(link)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        path = (HTML.parent / unquote(parts.path)).resolve()
        exists = path.exists()
        item = {"href": link, "exists": exists}
        if not exists:
            failures.append(item)
        elif parts.fragment and path.suffix.lower() in {".md", ".html"}:
            if path not in cache:
                if path.suffix.lower() == ".md":
                    cache[path] = markdown_targets(path)
                else:
                    target = Audit()
                    target.feed(path.read_text(encoding="utf-8"))
                    cache[path] = set(target.ids)
            item["fragment_exists"] = unquote(parts.fragment) in cache[path]
            if not item["fragment_exists"]:
                failures.append(item)
        local_links.append(item)
    checks["all_local_link_files_and_fragments_exist"] = not failures
    result = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "html": str(HTML.relative_to(ROOT)),
        "html_sha256": hashlib.sha256(HTML.read_bytes()).hexdigest(),
        "checks": checks,
        "source_counts": dict(expected.counts),
        "page_ids": len(page.ids),
        "local_links": local_links,
        "failures": failures,
        "visual_inspection": "Assigned to the parent; not established by these structural checks.",
    }
    destination = Path(__file__).with_name("html-publisher-production-checks.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": checks, "failures": failures, "source_counts": result["source_counts"], "evidence": str(destination.relative_to(ROOT))}, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
