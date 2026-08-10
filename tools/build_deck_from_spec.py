#!/usr/bin/env python3
"""Build an editable Leadership-Link .pptx from a deck-settings JSON spec.

The HTML deck generator (tools/deck-generator.html) exports its settings via
"Download settings". This script turns that spec into an editable PowerPoint built on
the approved template by chrome inheritance (duplicate branded slides, replace text),
then packs it with the correct presentation content type and verifies it opens.

Usage:
    python build_deck_from_spec.py <spec.json> <output.pptx> [template.potx]

Spec shape (produced by the generator):
    {"name","kind","unit","subtitle","bigIdea","items":[...],
     "spot":{"label","headline","point","support"}}
Mission and ground rules are standard and filled automatically.
"""
import json, os, re, sys, subprocess, zipfile, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TPL = os.path.join(HERE, "..", "skills", "leadership-link-deck-builder",
                           "assets", "Leadership-Link_Deck_Template.potx")
PACK = os.path.join(HERE, "..", "skills", "leadership-link-deck-builder", "scripts", "pack_pptx.py")

MISSION = "We help teams of experts become expert teams."
GROUND = [("Be present", "phones down, fully here"),
          ("Participate", "the room is the content"),
          ("Real examples", "use situations you actually face"),
          ("Leave with one move", "pick one behavior to change this week")]

MER = ('<a:latin typeface="Tahoma" pitchFamily="34" charset="0"/>'
       '<a:ea typeface="Tahoma" pitchFamily="34" charset="-122"/>'
       '<a:cs typeface="Tahoma" pitchFamily="34" charset="-120"/>')

# template slide file -> relationship id (stable in the shipped template)
ORDER = ["rId2", "rId16", "rId17", "rId18", "rId3", "rId5", "rId6", "rId23", "rId24"]
#         cover   mission  ground  bigidea  over-  divid  cont-  commit  thanks
#                                            view    er     ent


def rt(x): return open(x, encoding="utf-8").read()
def wt(x, s): open(x, "w", encoding="utf-8").write(s)
def esc(s): return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def replace_in(path, pairs):
    x = rt(path)
    for a, b in pairs:
        if a not in x:
            raise SystemExit(f"pattern missing in {os.path.basename(path)}: {a!r}")
        x = x.replace(a, b, 1)
    wt(path, x)


def rebuild_rows(slide_path, items):
    """Rebuild the agenda-style overview rows to exactly len(items) rows."""
    xml = rt(slide_path)
    sps = list(re.finditer(r"<p:sp>.*?</p:sp>", xml, re.S))
    def txt(sp): return re.findall(r"<a:t>(.*?)</a:t>", sp.group(0), re.S)
    first = next(i for i, m in enumerate(sps) if txt(m) == ["1"])
    last = next(i for i, m in enumerate(sps) if txt(m) == ["Fourth segment"])
    n = len(items)
    top, bottom, rowh = 1737360, 6858000, 685800          # EMU
    step = (bottom - top) // n
    cid = 400
    parts = []
    for k, it in enumerate(items):
        ty = top + k * step + max(0, (step - rowh) // 2)
        ny = ty + 123444
        parts.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{cid}" name="N{cid}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="1143000" y="{ny}"/><a:ext cx="438912" cy="438912"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln/></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" rtlCol="0" anchor="ctr"/><a:lstStyle/>'
            f'<a:p><a:pPr algn="ctr" indent="0" marL="0"><a:buNone/></a:pPr>'
            f'<a:r><a:rPr lang="en-US" sz="1900" b="1" dirty="0"><a:solidFill><a:srgbClr val="D4AF37"/></a:solidFill>'
            f'{MER}</a:rPr><a:t>{k+1}</a:t></a:r></a:p></p:txBody></p:sp>')
        cid += 1
        parts.append(
            f'<p:sp><p:nvSpPr><p:cNvPr id="{cid}" name="R{cid}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="1828800" y="{ty}"/><a:ext cx="9326880" cy="{rowh}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln/></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" rtlCol="0" anchor="ctr"/><a:lstStyle/>'
            f'<a:p><a:pPr indent="0" marL="0"><a:buNone/></a:pPr>'
            f'<a:r><a:rPr lang="en-US" sz="2000" b="1" dirty="0"><a:solidFill><a:srgbClr val="1A2238"/></a:solidFill>'
            f'{MER}</a:rPr><a:t>{esc(it)}</a:t></a:r></a:p></p:txBody></p:sp>')
        cid += 1
    new = xml[:sps[first].start()] + "".join(parts) + xml[sps[last].end():]
    wt(slide_path, new)


def build(spec, out_path, tpl):
    tmp = tempfile.mkdtemp(prefix="llbuild_")
    try:
        up = os.path.join(tmp, "unpacked")
        with zipfile.ZipFile(tpl) as z:
            z.extractall(up)
        S = os.path.join(up, "ppt", "slides")
        # 1. select + order the 9 slides
        pres = os.path.join(up, "ppt", "presentation.xml")
        x = rt(pres)
        items = "".join(f'<p:sldId id="{256+i}" r:id="{r}"/>' for i, r in enumerate(ORDER))
        x = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>", f"<p:sldIdLst>{items}</p:sldIdLst>", x, flags=re.S)
        wt(pres, x)
        # remove orphaned slide parts (rels, content-types) now out of the deck
        _clean(up)

        name, kind, unit = spec["name"], spec.get("kind", ""), spec.get("unit", "Section")
        it = spec["items"]; spot = spec["spot"]
        # 2. cover
        replace_in(f"{S}/slide1.xml", [
            ("<a:t>Deck Title Here</a:t>", f"<a:t>{esc(name)}</a:t>"),
            ("<a:t>Subtitle  ·  Client  ·  Date</a:t>", f"<a:t>{esc(spec.get('subtitle',''))}</a:t>")])
        # 3. mission
        replace_in(f"{S}/slide15.xml", [
            ("<a:t>We help technical experts become expert communicators.</a:t>",
             f"<a:t>{esc(MISSION)}</a:t>")])
        # 4. ground rules
        gpairs = []
        tmpl = [("Be present   ", "phones down, fully here"),
                ("Participate   ", "the room is the content"),
                ("Confidentiality   ", "what&apos;s shared here stays here"),
                ("Respect the room   ", "one voice at a time, assume good intent")]
        for (tl, tsub), (nl, nsub) in zip(tmpl, GROUND):
            gpairs.append((f"<a:t>{tl}</a:t>", f"<a:t>{esc(nl)}   </a:t>"))
            gpairs.append((f"<a:t>{tsub}</a:t>", f"<a:t>{esc(nsub)}</a:t>"))
        replace_in(f"{S}/slide16.xml", gpairs)
        # 5. big idea
        replace_in(f"{S}/slide17.xml", [
            ("<a:t>State the workshop&apos;s single Big Idea here, in one bold sentence.</a:t>",
             f"<a:t>{esc(spec['bigIdea'])}</a:t>")])
        # 6. overview
        replace_in(f"{S}/slide2.xml", [("<a:t>Agenda</a:t>", "<a:t>Overview</a:t>")])
        rebuild_rows(f"{S}/slide2.xml", it)
        # 7. divider (item 0)
        replace_in(f"{S}/slide4.xml", [("<a:t>Part One</a:t>", f"<a:t>{esc(it[0])}</a:t>"),
                                       ('sz="4000"', 'sz="2800"')])
        # 8. content (spotlight)
        replace_in(f"{S}/slide5.xml", [
            ("<a:t>OPTIONAL MUTED LABEL</a:t>", f"<a:t>{esc(spot['label'])}</a:t>"),
            ("<a:t>One Idea, Stated Short</a:t>", f"<a:t>{esc(spot['headline'])}</a:t>"),
            ("<a:t>Visual anchor</a:t>", f"<a:t>{esc(unit)}</a:t>"),
            ("<a:t>The point.</a:t>", f"<a:t>{esc(spot['point'])}</a:t>"),
            ("<a:t>One short support phrase.</a:t>", f"<a:t>{esc(spot['support'])}</a:t>")])
        # 9. commitment
        replace_in(f"{S}/slide22.xml", [
            ("Pick one real conversation coming up in the next two weeks. Apply the framework to it now, "
             "and commit to the specific language and intent you&apos;ll use.",
             "Pick one real situation coming up soon. Apply what you learned, and commit to the specific "
             "behavior you&apos;ll use."),
            ("The conversation:", "The situation:")])
        # thanks (slide23) left as-is: headshot, QR, logo, contact.

        # 10. pack with correct content type + verify
        r = subprocess.run([sys.executable, PACK, up, out_path], capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0:
            print(r.stderr.strip(), file=sys.stderr); return False
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _clean(up):
    """Remove slide parts not referenced by <p:sldIdLst>, and their rels/notes/content-types."""
    pres = rt(os.path.join(up, "ppt", "presentation.xml"))
    keep_rids = set(re.findall(r'r:id="(rId\d+)"', re.search(r"<p:sldIdLst>.*?</p:sldIdLst>", pres, re.S).group(0)))
    rels_p = os.path.join(up, "ppt", "_rels", "presentation.xml.rels")
    rels = rt(rels_p)
    keep_slides = set()
    for rid, tgt in re.findall(r'Id="(rId\d+)"[^>]*Target="slides/(slide\d+\.xml)"', rels):
        if rid in keep_rids:
            keep_slides.add(tgt)
    slides_dir = os.path.join(up, "ppt", "slides")
    ct_p = os.path.join(up, "[Content_Types].xml")
    ct = rt(ct_p)
    for f in os.listdir(slides_dir):
        if f.endswith(".xml") and f not in keep_slides:
            # remove slide, its rels, notes references stay orphaned but harmless; drop content-type + pres rel
            os.remove(os.path.join(slides_dir, f))
            relf = os.path.join(slides_dir, "_rels", f + ".rels")
            if os.path.exists(relf):
                os.remove(relf)
            ct = ct.replace(f'<Override PartName="/ppt/slides/{f}" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>', "")
            rels = re.sub(rf'<Relationship Id="rId\d+"[^>]*Target="slides/{re.escape(f)}"[^>]*/>', "", rels)
    wt(ct_p, ct)
    wt(rels_p, rels)


def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    spec = json.load(open(argv[1]))
    tpl = argv[3] if len(argv) > 3 else DEFAULT_TPL
    ok = build(spec, argv[2], tpl)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
