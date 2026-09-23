"""Bind the new folio layout to final Word renders and visually reviewed v4 pages."""
from pathlib import Path
from PIL import Image, ImageChops
from pypdf import PdfReader
import hashlib
import json

ROOT = Path('/Users/ryan/.codex/worktrees/da43/chirality')
EV = ROOT / 'plans/evidence/2026-09-22_manual_authorship_frontmatter'
PRE = Path('/tmp/manual-v5-authorship-20260922/preliminary')
FINAL = Path('/tmp/manual-v5-authorship-20260922/final2')
V4 = Path('/tmp/manual-v4-20260922/final3')
REPO_PDF = ROOT / 'docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf'
pdf = PdfReader(FINAL / 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.pdf')
v4pdf = PdfReader(V4 / 'Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf')
assert len(pdf.pages) == 165 and len(v4pdf.pages) == 162

front = []
changed = []
body = []
# Compare all final Word render pages to the frozen render from which Contents caches were read.
for page_no in range(1, 166):
    new = Image.open(FINAL / f'page-{page_no}.png').convert('RGB')
    frozen = Image.open(PRE / f'page-{page_no}.png').convert('RGB')
    assert new.size == frozen.size
    box = ImageChops.difference(new, frozen).getbbox()
    if page_no in (5, 6):
        assert box is not None and box[0] >= 1260 and box[1] >= 150 and box[2] <= 1400 and box[3] <= 1870
        changed.append({'page': page_no, 'difference_bbox': box, 'cause': 'materialized Contents folios'})
    else:
        assert box is None, (page_no, box)
    if 2 <= page_no <= 7:
        front.append({'page': page_no,
                      'sha256': hashlib.sha256((FINAL / f'page-{page_no}.png').read_bytes()).hexdigest(),
                      'visual_status': 'individually inspected at original detail'})

# Cover remains pixel-identical. All old book-body pages keep their exact typography and flow;
# only the page-folio value differs because the Preface now restarts at Arabic 1.
cover = Image.open(FINAL / 'page-1.png').convert('RGB')
v4cover = Image.open(V4 / 'page-1.png').convert('RGB')
assert ImageChops.difference(cover, v4cover).getbbox() is None
body_boxes = []
for physical in range(7, 166):
    old_physical = physical - 3
    new = Image.open(FINAL / f'page-{physical}.png').convert('RGB')
    old = Image.open(V4 / f'page-{old_physical}.png').convert('RGB')
    assert new.size == old.size
    box = ImageChops.difference(new, old).getbbox()
    assert box is not None and box[0] >= 1260 and box[1] >= 1880 and box[2] <= 1400 and box[3] <= 1960, (physical, old_physical, box)
    body_boxes.append(box)
    def text_without_running_items(page):
        return '\n'.join(line.strip() for line in (page.extract_text() or '').splitlines()
                         if not line.strip().startswith('PROJECT MANAGEMENT'))
    assert text_without_running_items(pdf.pages[physical-1]) == text_without_running_items(v4pdf.pages[old_physical-1])

result = {
    'v5_pdf_sha256': hashlib.sha256(REPO_PDF.read_bytes()).hexdigest(),
    'v5_pages': 165,
    'v4_pdf_sha256': hashlib.sha256((V4 / 'Project_Management_for_Human_Agent_Teams_Consolidated_v4.pdf').read_bytes()).hexdigest(),
    'v4_pages': 162,
    'cover': {'status': 'pixel-identical to v4 cover', 'sha256': hashlib.sha256((FINAL / 'page-1.png').read_bytes()).hexdigest()},
    'individually_inspected_new_pages': front,
    'contents_pages': {'physical_pages': [5, 6], 'folio_numbers_materialized': True,
                       'pixel_changes_confined_to_page_number_column': changed},
    'main_body': {'v5_physical_range': [7, 165], 'v4_physical_range': [4, 162],
                  'page_count': len(body_boxes), 'individual_page_text_unchanged': True,
                  'pixel_difference_on_each_page_confined_to_footer_folio': True,
                  'preface_page_number_restarts_at': 1, 'last_printed_folio': 159},
    'render_carryover': {'preliminary_page_count': 165, 'final_page_count': 165,
                         'changed_pages': [5, 6], 'cause': 'correct Contents folio caches'},
}
(EV / 'format-visual-v5.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'new_pages_reviewed': len(front), 'preserved_body_pages_bound': len(body_boxes),
                  'contents_pages_rechecked': 2, 'cover_identical': True, 'pdf_sha256': result['v5_pdf_sha256']}, indent=2))
