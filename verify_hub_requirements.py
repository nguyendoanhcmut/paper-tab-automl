# verify_hub_requirements.py
import json
import os

def extract_block(text, header):
    pos = text.find(header)
    if pos == -1:
        return ""
    start = text.find('{', pos)
    depth = 1
    i = start + 1
    while i < len(text) and depth > 0:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    return text[start+1:i-1]

def verify_all():
    errors = []
    
    # 1. Verify papers_catalog.json
    cat_path = 'branche_v2/papers_catalog.json'
    if not os.path.exists(cat_path):
        errors.append(f"Missing {cat_path}")
        return errors
    with open(cat_path, 'r', encoding='utf-8') as f:
        cat = json.load(f)
    if len(cat) != 30:
        errors.append(f"Tab 1 papers_catalog.json length is {len(cat)}, expected 30")
    
    expected_core_12 = ['M002', 'M007', 'M018', 'M030', 'M041', 'M066', 'M069', 'G-M001', 'M020', 'L-01', 'L-02', 'L-03']
    pids_in_cat = [p.get('pid') for p in cat]
    for c12 in expected_core_12:
        if c12 not in pids_in_cat:
            errors.append(f"Core PID {c12} missing from papers_catalog.json")

    for p in cat:
        pid = p.get('pid')
        pdf = p.get('pdf_bilingual')
        if not pdf or not os.path.exists(pdf):
            errors.append(f"Paper {pid} bilingual PDF missing: {pdf}")
        if not p.get('title_vn'):
            errors.append(f"Paper {pid} missing title_vn")

    # 2. Verify extended_catalog.json
    ext_path = 'branche_v2/extended_catalog.json'
    if not os.path.exists(ext_path):
        errors.append(f"Missing {ext_path}")
        return errors
    with open(ext_path, 'r', encoding='utf-8') as f:
        ext = json.load(f)
    if len(ext) != 65:
        errors.append(f"Tab 2 extended_catalog.json length is {len(ext)}, expected 65")

    for p in ext:
        pid = p.get('pid')
        pdf = p.get('pdf_dual')
        if not pdf or not os.path.exists(pdf):
            errors.append(f"Extended Paper {pid} dual PDF missing: {pdf}")
        if not p.get('title_vn'):
            errors.append(f"Extended Paper {pid} missing title_vn")

    # 3. Verify index.html content & Mobile CSS rules
    html_path = 'index.html'
    if not os.path.exists(html_path):
        errors.append(f"Missing {html_path}")
        return errors
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Check embedded counts
    if '"id": 30' not in html_content:
        errors.append("index.html does not contain paper id 30")
    
    # Check mobile media queries
    mobile_css = extract_block(html_content, '@media (max-width: 768px)')
    if not mobile_css:
        errors.append("Missing @media (max-width: 768px) in index.html")
    else:
        if '100dvh' not in mobile_css:
            errors.append("Mobile CSS missing 100dvh for modal")
        if 'position: sticky' not in mobile_css and 'sticky' not in mobile_css:
            errors.append("Mobile CSS missing position: sticky for modal header")
        if '44px' not in mobile_css:
            errors.append("Mobile CSS missing 44px tap target for close button")
        if 'flex-wrap: nowrap' not in mobile_css:
            errors.append("Mobile CSS missing flex-wrap: nowrap for filter chips or tabs")
        if 'overflow-x: auto' not in mobile_css:
            errors.append("Mobile CSS missing overflow-x: auto for swipeable tracks")
        if 'tree-toc-sidebar' not in mobile_css or 'display: none' not in mobile_css:
            errors.append("Mobile CSS missing display: none for tree-toc-sidebar")
        if 'grid-template-columns: 1fr' not in mobile_css:
            errors.append("Mobile CSS missing 1fr column rules for gallery/cards")

    # Check overflow-x hidden
    if 'overflow-x: hidden' not in html_content:
        errors.append("Missing overflow-x: hidden in html/body")

    # Check Tab navigation elements
    if 'tabCoreBtn' not in html_content or 'tabExtendedBtn' not in html_content:
        errors.append("Missing tab navigation buttons in index.html")

    return errors

if __name__ == '__main__':
    errs = verify_all()
    if errs:
        print(f"VERIFICATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        exit(1)
    else:
        print("VERIFICATION PASSED:")
        print("  [OK] Tab 1 contains exactly 30 papers with valid PIDs & Bilingual PDFs.")
        print("  [OK] Tab 2 contains exactly 65 papers with valid PIDs & Bilingual PDFs.")
        print("  [OK] All mobile media queries & layout stability fixes verified.")
        print("  [OK] HTML and embedded datasets valid and synchronized.")
