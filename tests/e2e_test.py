#!/usr/bin/env python3
"""End-to-end check for the Leadership-Link Claude system.

Validates the skills and brand assets, and (optionally) a produced deck.

Usage:
    python tests/e2e_test.py                 # check skills + template only
    python tests/e2e_test.py path/to/deck.pptx   # also check a produced deck

System checks: each skill has valid frontmatter whose name matches its directory;
every referenced file resolves; no off-brand tokens leak into guidance; the approved
template is present, Tahoma, and on-palette.

Deck checks (self-contained, read straight from the .pptx/.potx zip): Tahoma only;
colors within the template palette; the approved footer on every slide; speaker notes on
every slide; no leftover template placeholders; the 18pt PowerPoint floor (allowing 11pt
muted labels and the template's QR caption); and the four Managers in Motion block titles
verbatim when the deck is a Managers in Motion deck.

Exits non-zero if any error is found. Note: this does not render slides, so it cannot
catch purely visual defects (overflow, wrapping). Pair it with a visual pass where a
renderer is available.
"""
import re, os, sys, glob, zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(REPO, "skills/leadership-link-deck-builder/assets/Leadership-Link_Deck_Template.potx")
FOOTER = "Leadership-Link  |  Eileen Habelow, PhD"
STALE = ["Merriweather", "1C1E43", "ED8344", "BAD3E9", "5D386C", "9BBB59", "know2grow"]
PLACEHOLDERS = ["Part One", "Deck Title Here", "First segment", "Second segment",
                "Third segment", "Fourth segment", "OPTIONAL MUTED LABEL",
                "One Idea, Stated Short", "Visual anchor", "One short support phrase",
                "The point.", "Lorem", "ipsum"]
BLOCKS = ["Know Yourself and Others", "Motivate Your People and Manage the Work",
          "Give Feedback That Drives Performance and Growth", "Manage Up and Out"]

errors, oks = [], []
def err(m): errors.append(m)
def ok(m): oks.append(m)

def palette_from(path):
    z = zipfile.ZipFile(path)
    allx = "".join(z.read(n).decode("utf8", "ignore") for n in z.namelist() if n.endswith(".xml"))
    return {c.upper() for c in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', allx)}

def check_system():
    print("## System: skills, references, brand")
    for sk in sorted(glob.glob(f"{REPO}/skills/*/SKILL.md")):
        base = os.path.dirname(sk); d = os.path.basename(base)
        txt = open(sk, encoding="utf-8").read()
        fm = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
        if not fm: err(f"{d}: missing frontmatter"); continue
        nm = re.search(r'^name:\s*(.+)$', fm.group(1), re.M)
        if not nm or nm.group(1).strip() != d: err(f"{d}: frontmatter name != dir")
        else: ok(f"{d}: frontmatter OK")
        if 'description:' not in fm.group(1): err(f"{d}: no description")
        for ref in set(re.findall(r'`(references/[\w./-]+\.md|assets/[\w._-]+)`', txt)):
            if not os.path.exists(os.path.join(base, ref)): err(f"{d}: missing {ref}")
        for ref in set(re.findall(r'`(skills/[\w./-]+\.md)`', txt)):
            if not os.path.exists(os.path.join(REPO, ref)): err(f"{d}: missing {ref}")
    # stale-brand leak, paragraph-aware so wrapped negations are honored. An off-brand
    # token is fine when its paragraph frames it as a draft/mistake to avoid; it is an
    # error when it reads as prescriptive brand guidance.
    markers = ["draft", "off-brand", "circulating", "substitute", "not merriweather",
               "not tahoma", "failed behavior", "do not copy", "navy palette", "mistake"]
    for f in glob.glob(f"{REPO}/skills/**/*.md", recursive=True) + [f"{REPO}/README.md"]:
        if "eileen-operating-profile" in f: continue  # verbatim source of truth
        for para in re.split(r'\n\s*\n', open(f, encoding="utf-8").read()):
            low = para.lower()
            if any(w in low for w in markers):
                continue
            for tok in STALE:
                if tok in para:
                    err(f"{os.path.relpath(f, REPO)}: off-brand token '{tok}' in prescriptive context")
    if not os.path.exists(TPL): err("approved template missing"); return
    tpal = palette_from(TPL)
    z = zipfile.ZipFile(TPL)
    sfonts = set(re.findall(r'typeface="([^"]*)"',
                 "".join(z.read(n).decode("utf8", "ignore") for n in z.namelist()
                         if re.search(r'slides/slide\d+\.xml$', n))))
    if sfonts - {"Tahoma"}: err(f"template slides use non-Tahoma: {sfonts-{'Tahoma'}}")
    else: ok("template is Tahoma")
    ok(f"template present, {len(tpal)}-color palette")
    return tpal

def check_deck(path, tpal):
    print(f"## Deck: {os.path.basename(path)}")
    z = zipfile.ZipFile(path)
    slide_names = sorted([n for n in z.namelist() if re.search(r'ppt/slides/slide\d+\.xml$', n)])
    slides = {n: z.read(n).decode("utf8", "ignore") for n in slide_names}
    allx = "".join(slides.values())
    # fonts
    bad = set(re.findall(r'typeface="([^"]*)"', allx)) - {"Tahoma"}
    if bad: err(f"deck non-Tahoma fonts: {bad}")
    else: ok("deck font = Tahoma only")
    # colors
    off = {c.upper() for c in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', allx)} - tpal
    if off: err(f"deck colors outside template palette: {off}")
    else: ok("deck colors within template palette")
    # per-slide: footer, notes, placeholders, 18pt floor
    rels_map = {}
    for n in z.namelist():
        if n.endswith(".rels") and "slides/_rels/slide" in n:
            rels_map[n] = z.read(n).decode("utf8", "ignore")
    no_footer, no_notes, viol = [], [], []
    for sn, sx in slides.items():
        num = re.search(r'slide(\d+)\.xml', sn).group(1)
        if FOOTER not in sx: no_footer.append(num)
        relp = f"ppt/slides/_rels/slide{num}.xml.rels"
        rx = rels_map.get(relp, "")
        nm = re.search(r'(notesSlide\d+\.xml)', rx)
        if not nm: no_notes.append(num)
        else:
            nx = z.read(f"ppt/notesSlides/{nm.group(1)}").decode("utf8", "ignore")
            i = nx.find('type="body"'); j = nx.find('<a:t>', i); k = nx.find('</a:t>', j)
            if not (i > -1 and j > -1 and k - j > 15): no_notes.append(num + "(empty)")
        for t in re.findall(r'<a:t>(.*?)</a:t>', sx, re.S):
            if any(p in t for p in PLACEHOLDERS): err(f"slide{num} leftover placeholder: {t!r}")
        for r in re.findall(r'<a:r>.*?</a:r>', sx, re.S):
            szm = re.search(r'<a:rPr[^>]*\bsz="(\d+)"', r); tm = re.search(r'<a:t>(.*?)</a:t>', r, re.S)
            if not (szm and tm): continue
            sz = int(szm.group(1)); t = tm.group(1).strip()
            if sz >= 1800 or len(t) <= 2 or t.isdigit() or "Eileen Habelow" in t: continue
            is_label = sz <= 1100 and (t.isupper() or t.startswith("BLOCK"))
            if not (is_label or t == "Connect on LinkedIn"):
                viol.append(f"slide{num} {sz//100}pt '{t[:36]}'")
    if no_footer: err(f"slides missing footer: {no_footer}")
    else: ok(f"footer on all {len(slides)} slides")
    if no_notes: err(f"slides missing/empty notes: {no_notes}")
    else: ok(f"notes on all {len(slides)} slides")
    if viol: err(f"18pt-floor violations: {viol}")
    else: ok("18pt floor holds (11pt muted labels + QR caption allowed)")
    if any(b in allx for b in BLOCKS):  # Managers in Motion deck
        for b in BLOCKS:
            if b not in allx: err(f"missing block title verbatim: {b!r}")
        if not [b for b in BLOCKS if b not in allx]: ok("four block titles verbatim")

def main():
    tpal = check_system()
    if len(sys.argv) > 1 and tpal:
        deck = sys.argv[1]
        if not os.path.exists(deck): err(f"deck not found: {deck}")
        else: check_deck(deck, tpal)
    print("\n" + "=" * 58)
    for m in oks: print("  [OK] ", m)
    for m in errors: print("  [ERR]", m)
    print("=" * 58)
    print(f"VERDICT: {'PASS - 0 errors' if not errors else str(len(errors)) + ' ERROR(S)'}")
    print("(structural/brand only; no visual render - pair with a visual pass)")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
