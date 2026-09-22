"""Independent read-only publication audit. Uses final Markdown, OOXML, and PDF.

No publication writes. Outputs go to the caller's scratch JSON path. It checks
ordered content, separately preserves table cell/specimen boundaries, and records
navigation/metadata facts for human examination. Not a layout validator.
"""
from pathlib import Path
from collections import Counter
from lxml import etree as E
from pypdf import PdfReader
import argparse, hashlib, html, json, re, unicodedata, zipfile

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
N = {'w': W, 'r': R}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def normalized(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()

def compact(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFC', s).replace('\xad', ''))

def visible(s):
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)
    s = s.replace('**', '').replace('*', '').replace('`', '')
    return html.unescape(s)

def ptext(p):
    return ''.join((el.text or '') if el.tag == '{'+W+'}t' else '\n' if el.tag == '{'+W+'}br' else '\t'
                   for el in p.xpath('.//w:t | .//w:br | .//w:tab[not(ancestor::w:pPr)]', namespaces=N))

def source_units(md):
    # Per-source-line parser independent of the publication builder. Source
    # paragraphs occupy single logical lines. Fenced specimens form one unit.
    lines = md.splitlines()
    start = lines.index('# Preface')
    units, headings, tables, codes, images, links = [], [], [], [], [], []
    code, current_table = None, None
    for i, raw in enumerate(lines[start:], start + 1):
        s = raw.strip()
        if s.startswith('```'):
            if code is None:
                code = {'line': i, 'kind': 'code', 'text': ''}
                code_lines = []
            else:
                code['text'] = '\n'.join(code_lines)
                units.append(code); codes.append(code); code = None
            continue
        if code is not None:
            code_lines.append(raw)
            continue
        if not s or s.startswith('<a '):
            current_table = None if not s else current_table
            continue
        if s.startswith('!['):
            a = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', s)
            images.append({'line': i, 'alt': a[1], 'source': a[2]})
            continue
        for label, url in re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', s):
            links.append({'line': i, 'label': label, 'target': url})
        if s.startswith('|'):
            if re.fullmatch(r'\|[\s|:\-]+\|', s):
                continue
            cells = [visible(c.strip()) for c in re.split(r'(?<!\\)\|', s)[1:-1]]
            if current_table is None:
                current_table = {'line': i, 'rows': []}; tables.append(current_table)
            current_table['rows'].append(cells)
            units.extend({'line': i, 'kind': 'cell', 'text': c} for c in cells)
            continue
        current_table = None
        h = re.fullmatch(r'(#{1,6})\s+(.+)', s)
        if h:
            u = {'line': i, 'kind': 'heading', 'level': len(h[1]), 'text': visible(h[2])}
            headings.append(u)
        else:
            u = {'line': i, 'kind': 'paragraph', 'text': visible(s)}
        units.append(u)
    assert code is None, 'Unclosed source fence'
    return units, headings, tables, codes, images, links

def audit(mdpath, docxpath, pdfpath):
    md = Path(mdpath).read_text()
    units, headings, tables, codes, images, links = source_units(md)
    z = zipfile.ZipFile(docxpath)
    x = E.fromstring(z.read('word/document.xml'))
    rels = {a.get('Id'): dict(a.attrib) for a in E.fromstring(z.read('word/_rels/document.xml.rels'))}
    paragraphs = x.xpath('/w:document/w:body//w:p', namespaces=N)
    begin = next(i for i,p in enumerate(paragraphs) if ptext(p) == 'Preface' and p.xpath('./w:pPr/w:pStyle/@w:val', namespaces=N)==['Heading1'])
    bodyps = paragraphs[begin:]
    word_units = [ptext(p) for p in bodyps if ptext(p).strip()]
    content_mismatches = []
    for i, (a,b) in enumerate(zip(units, word_units)):
        if normalized(a['text']) != normalized(b):
            content_mismatches.append({'index':i, 'md_line':a['line'], 'kind':a['kind'], 'expected':a['text'], 'actual':b})
    word_heads = [{'text':ptext(p),'level':int(p.xpath('./w:pPr/w:pStyle/@w:val',namespaces=N)[0][-1])}
                  for p in bodyps if p.xpath('./w:pPr/w:pStyle[starts-with(@w:val,"Heading")]', namespaces=N)]
    head_mismatch = [{'i':i,'expected':a,'actual':b} for i,(a,b) in enumerate(zip(headings,word_heads)) if (a['text'],a['level'])!=(b['text'],b['level'])]
    word_codes = [ptext(p) for p in bodyps if p.xpath('./w:pPr/w:pStyle[@w:val="PMSpecimen"]',namespaces=N)]
    code_mismatch = [{'i':i,'line':a['line'],'expected':a['text'],'actual':b} for i,(a,b) in enumerate(zip(codes,word_codes)) if a['text']!=b]
    word_tables = []
    table_header_rows=[]
    for t in x.xpath('/w:document/w:body/w:tbl',namespaces=N):
        if t.xpath('.//w:tbl',namespaces=N):
            continue
        rows = [['\n'.join(ptext(p) for p in c.xpath('.//w:p',namespaces=N)) for c in r.xpath('./w:tc',namespaces=N)] for r in t.xpath('./w:tr',namespaces=N)]
        word_tables.append(rows)
        table_header_rows.append(len(t.xpath('./w:tr[1]/w:trPr/w:tblHeader',namespaces=N)))
    table_mismatch = [{'i':i,'line':a['line'],'expected':a['rows'],'actual':b} for i,(a,b) in enumerate(zip(tables,word_tables)) if a['rows']!=b]
    anchors = re.findall(r'<a id="([^"]+)"></a>',md)
    bookmarks = x.xpath('//w:bookmarkStart/@w:name',namespaces=N)
    hyperlink_records = []
    for h in x.xpath('//w:hyperlink',namespaces=N):
        rid=h.get('{'+R+'}id'); target=rels[rid]['Target'] if rid else '#'+str(h.get('{'+W+'}anchor'))
        hyperlink_records.append({'text':ptext(h), 'target':target, 'rid':rid})
    active_rids = {a['rid'] for a in hyperlink_records if a['rid']}
    inactive_rels = [r for rid,r in rels.items() if r['Type'].endswith('/hyperlink') and rid not in active_rids]
    toc = []
    bookmark_paragraph = {b.get('{'+W+'}name'): ptext(b.getparent()) for b in x.xpath('//w:bookmarkStart',namespaces=N)}
    for p in paragraphs[:begin]:
        if p.xpath('./w:pPr/w:pStyle[starts-with(@w:val,"PMContents")]',namespaces=N):
            title = ''.join(p.xpath('.//w:hyperlink//w:t/text()',namespaces=N))
            anchors2 = p.xpath('.//w:hyperlink/@w:anchor',namespaces=N)
            toc.append({'text':ptext(p),'title':title,'cached_folio':''.join(p.xpath('./w:r/w:t/text()',namespaces=N)),'anchors':anchors2,'target_text':[bookmark_paragraph[a] for a in anchors2],'fields':p.xpath('.//w:fldSimple/@w:instr',namespaces=N)})
    forbidden_tags = ['ins','del','moveFrom','moveTo','commentRangeStart','commentRangeEnd','commentReference','pPrChange','rPrChange','sectPrChange','tblPrChange','trPrChange','tcPrChange']
    tracked = {}
    history_attributes=[]
    history_elements=[]
    for name in z.namelist():
        if name.endswith('.xml'):
            e = E.fromstring(z.read(name))
            c = {t:len(e.findall('.//{'+W+'}'+t)) for t in forbidden_tags}
            c = {k:v for k,v in c.items() if v}
            if c:tracked[name]=c
            history_attributes.extend({'part':name,'element':E.QName(a).localname,'attribute':E.QName(k).localname,'value':v} for a in e.iter() for k,v in a.attrib.items() if E.QName(k).localname.lower().startswith('rsid'))
            history_elements.extend({'part':name,'element':E.QName(a).localname} for a in e.iter() if E.QName(a).localname.lower().startswith('rsid') or E.QName(a).localname=='docId')
    reader = PdfReader(pdfpath)
    page_text = [p.extract_text() or '' for p in reader.pages]
    pdfbody = []
    folios = []
    for i,s in enumerate(page_text):
        nums = re.findall(r'^PROJECT MANAGEMENT (\d+)\s*$',s,re.M)
        folios.append({'physical_page':i+1,'printed_folios':nums})
        s = re.sub(r'^PROJECT MANAGEMENT FOR HUMAN–AGENT TEAMS\s*\n','',s,flags=re.M)
        s = re.sub(r'^PROJECT MANAGEMENT \d+\s*\n','',s,flags=re.M)
        pdfbody.append(s)
    pdfstart = next(i for i,s in enumerate(pdfbody) if s.startswith('Preface\n'))
    pdfstream = compact('\n'.join(pdfbody[pdfstart:]))
    # Locate complete logical paragraphs/cells/specimens consecutively in the
    # extraction. Whitespace is discarded because PDF stores visual line wraps.
    cursor=0; pdfmissing=[]; pdfextras=[]
    for u in units:
        t=compact(u['text']); pos=pdfstream.find(t,cursor)
        if pos<0:
            pdfmissing.append({'md_line':u['line'],'kind':u['kind'],'text':u['text']})
            continue
        if pos>cursor:
            pdfextras.append({'before_md_line':u['line'],'text':pdfstream[cursor:pos]})
        cursor=pos+len(t)
    if cursor<len(pdfstream):pdfextras.append({'trailing':pdfstream[cursor:]})
    pdf_annots=[]
    for i,p in enumerate(reader.pages):
        for ref in p.get('/Annots',[]):
            a=ref.get_object(); item={'physical_page':i+1,'subtype':str(a.get('/Subtype')),'rect':list(a.get('/Rect',[]))}
            if '/A' in a: item['action'] = {str(k):str(v) for k,v in a['/A'].items()}
            if '/Dest' in a:
                d=a['/Dest']; item['destination']=str(d)
                if isinstance(d,list):item['destination_coordinates']=[str(v) for v in d[1:]]
                if isinstance(d,list) and d and hasattr(d[0],'idnum'):
                    item['target_physical_page']=next((j+1 for j,p2 in enumerate(reader.pages) if p2.indirect_reference.idnum==d[0].idnum),None)
            pdf_annots.append(item)
    def outlines(seq,depth=1):
        result=[]
        for a in seq:
            if isinstance(a,list):result.extend(outlines(a,depth+1))
            else:result.append({'depth':depth,'title':a.title,'physical_page':reader.get_destination_page_number(a)+1,'left':str(a.left),'top':str(a.top)})
        return result
    captions=[ptext(p) for p in bodyps if p.xpath('./w:pPr/w:pStyle[@w:val="PMFigureCaption"]',namespaces=N)]
    caption_pages=[{'caption':c,'physical_pages':[i+1 for i,s in enumerate(page_text) if compact(c) in compact(s)]} for c in captions]
    code_pages=[{'source_line':c['line'],'physical_pages':[i+1 for i,s in enumerate(page_text) if compact(c['text']) in compact(s)]} for c in codes]
    toc_pdf_annotations=sorted([a for a in pdf_annots if a['physical_page']<pdfstart+1 and 'target_physical_page' in a],key=lambda a:(a['physical_page'],-a['rect'][3]))
    toc_pdf_checks=[]
    outline_rows=outlines(reader.outline)
    outline_by_title={a['title']:a for a in outline_rows}
    for t,a in zip(toc,toc_pdf_annotations):
        target=a['target_physical_page']
        od=outline_by_title.get(t['title'])
        target_matches_outline=bool(od and target==od['physical_page'] and a.get('destination_coordinates',[None]*3)[1:3]==[od['left'],od['top']])
        toc_pdf_checks.append({'title':t['title'],'cached_folio':t['cached_folio'],'target_physical_page':target,'target_printed_folio':folios[target-1]['printed_folios'],'target_contains_title':compact(t['title']) in compact(pdfbody[target-1]),'source_physical_page':a['physical_page'],'word_anchor_matches_title':t['target_text']==[t['title']],'target_matches_outline_position':target_matches_outline})
    source_image_hashes=[{'source':a['source'],'sha256':sha(Path(mdpath).parent/a['source']) if (Path(mdpath).parent/a['source']).exists() else None} for a in images]
    return {
        'files':{str(p):{'sha256':sha(p),'bytes':Path(p).stat().st_size} for p in [mdpath,docxpath,pdfpath]},
        'comparison_policy':{'source_start':'# Preface','cover_and_contents':'Separately examined; expanded Contents intentionally added in Word.','body':'All ordered source paragraphs, headings, cells, captions and whole fenced specimens compared against OOXML. Whitespace collapsed only.','specimens_and_tables':'Exact text and table row/cell boundary comparisons.','pdf':'Complete ordered unit search after discarding extraction whitespace and page furniture; all gaps and missing units reported for investigation.'},
        'word_content':{'source_units':len(units),'word_units':len(word_units),'mismatches':content_mismatches},
        'headings':{'source':len(headings),'word':len(word_heads),'mismatches':head_mismatch,'word_outline':word_heads},
        'tables':{'source':len(tables),'word':len(word_tables),'mismatches':table_mismatch,'source_row_counts':[len(a['rows']) for a in tables],'repeating_first_header_row_counts':table_header_rows},
        'specimens':{'source':len(codes),'word':len(word_codes),'exact_mismatches':code_mismatch},
        'figures':{'image_source':images,'source_image_hashes':source_image_hashes,'embedded_media':[{'part':a,'sha256':hashlib.sha256(z.read(a)).hexdigest()} for a in z.namelist() if a.startswith('word/media/')], 'caption_count':len(captions),'captions':captions,'caption_pages':caption_pages,'specimen_pages':code_pages},
        'word_navigation':{'source_anchors':len(anchors),'bookmarks':len(bookmarks),'missing_source_anchors':sorted(set(anchors)-set(bookmarks)),'duplicate_bookmarks':[k for k,v in Counter(bookmarks).items() if v>1],'bookmark_names_over_40':[b for b in bookmarks if len(b)>40],'bookmark_id_pairs_match':Counter(x.xpath('//w:bookmarkStart/@w:id',namespaces=N))==Counter(x.xpath('//w:bookmarkEnd/@w:id',namespaces=N)), 'missing_link_targets':sorted({a['target'][1:] for a in hyperlink_records if a['target'].startswith('#')}-set(bookmarks)),'source_links':links,'links':hyperlink_records,'inactive_hyperlink_relationships':inactive_rels,'contents':toc},
        'word_metadata':{'core_xml':z.read('docProps/core.xml').decode(),'app_xml':z.read('docProps/app.xml').decode(),'comment_parts':[n for n in z.namelist() if 'comment' in n.lower()],'tracked_change_elements':tracked,'history_attributes':history_attributes,'history_elements':history_elements,'package_parts':{n:hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist()}},
        'pdf_content':{'pages':len(reader.pages),'first_body_physical_page':pdfstart+1,'missing_units':pdfmissing,'interstitial_extras':pdfextras},
        'pdf_navigation':{'folios':folios,'annotations':pdf_annots,'outline':outline_rows,'metadata':dict(reader.metadata),'contents_checks':toc_pdf_checks,'contents_annotation_count':len(toc_pdf_annotations)}
    }

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('markdown');p.add_argument('docx');p.add_argument('pdf');p.add_argument('output');a=p.parse_args()
    result=audit(a.markdown,a.docx,a.pdf);Path(a.output).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'word_content':{k:v for k,v in result['word_content'].items() if k!='mismatches'},'word_mismatches':len(result['word_content']['mismatches']),'heading_counts':[result['headings']['source'],result['headings']['word']],'heading_mismatches':len(result['headings']['mismatches']),'table_counts':[result['tables']['source'],result['tables']['word']],'table_mismatches':len(result['tables']['mismatches']),'specimen_counts':[result['specimens']['source'],result['specimens']['word']],'specimen_mismatches':len(result['specimens']['exact_mismatches']),'pdf_missing_units':len(result['pdf_content']['missing_units']),'pdf_extras':len(result['pdf_content']['interstitial_extras']),'result':a.output},indent=2))
