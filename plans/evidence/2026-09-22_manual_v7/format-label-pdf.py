"""Add viewer labels to the retained tagged export without altering its page content."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
EV = Path(__file__).resolve().parent
SOURCE = Path('/tmp/manual-v7-20260922/final/Project_Management_for_Human_Agent_Teams_Consolidated_v7.pdf')
OUT = ROOT / 'docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v7.pdf'
r = PdfReader(SOURCE)
assert len(r.pages) == 166
folios = [re.findall(r'^PROJECT MANAGEMENT\s+([ivxlcdm]+|\d+)\s*$', p.extract_text(), re.M) for p in r.pages]
assert folios == [[]] + [[v] for v in ['i', 'ii', 'iii']] + [[str(i)] for i in range(1, 163)]
w = PdfWriter()
w.clone_document_from_reader(r)
w.set_page_label(0, 0, prefix='Cover')
w.set_page_label(1, 3, style=NameObject('/r'), start=1)
w.set_page_label(4, 165, style=NameObject('/D'), start=1)
with OUT.open('wb') as f:
    w.write(f)
final = PdfReader(OUT)
assert final.page_labels == ['Cover', 'i', 'ii', 'iii'] + [str(i) for i in range(1, 163)]
assert dict(r.metadata) == dict(final.metadata)
assert set(final.trailer['/Root']) == set(r.trailer['/Root']) | {'/PageLabels'}
assert final.trailer['/Root']['/Lang'] == r.trailer['/Root']['/Lang']
assert final.trailer['/Root']['/Metadata'].get_data() == r.trailer['/Root']['/Metadata'].get_data()
def outlines(reader, sequence):
    result = []
    for item in sequence:
        if isinstance(item, list):
            result.append(outlines(reader, item))
        else:
            result.append([item.title, reader.get_destination_page_number(item), str(item.left), str(item.top)])
    return result
assert outlines(r, r.outline) == outlines(final, final.outline)
for before, after in zip(r.pages, final.pages):
    assert before.get_contents().get_data() == after.get_contents().get_data()
    assert before.extract_text() == after.extract_text()
    assert list(before.mediabox) == list(after.mediabox)
    assert len(before.get('/Annots', [])) == len(after.get('/Annots', []))
report = {
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'pdf_sha256': hashlib.sha256(OUT.read_bytes()).hexdigest(),
    'page_count': len(final.pages),
    'viewer_labels': final.page_labels,
    'preservation_checks': ['all decoded page content streams', 'all extracted page text', 'page geometry', 'annotation counts', 'outline destinations and hierarchy', 'document metadata', 'XMP', 'language', 'catalog keys retained; only PageLabels added'],
    'render_comparison': 'Separate full-page comparison required after this metadata-only patch.'
}
(EV / 'pdf-label-check.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'pdf_sha256': report['pdf_sha256'], 'pages': len(final.pages), 'labels': final.page_labels[:6]}))
