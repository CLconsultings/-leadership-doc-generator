#!/usr/bin/env python3
"""Pack an unpacked, template-derived deck into a PowerPoint-openable .pptx.

A deck built by chrome inheritance from Leadership-Link_Deck_Template.potx inherits the
template content type for ppt/presentation.xml
(...presentationml.template.main+xml). A file named .pptx that keeps that content type
opens in LibreOffice and passes the XSD, but PowerPoint refuses it
("PowerPoint can't read ..."). This packer rewrites that Override to the presentation
content type and zips the package so PowerPoint accepts it. It also verifies the result
opens with python-pptx (a PowerPoint-faithful parser) when that library is available.

Usage:
    python pack_pptx.py <unpacked_dir> <output.pptx>

Exit status is non-zero if the packed file cannot be opened by python-pptx.
"""
import os, sys, zipfile

TEMPLATE_CT = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
PRES_CT = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"


def pack(unpacked_dir, out_path):
    ct_path = os.path.join(unpacked_dir, "[Content_Types].xml")
    ct = open(ct_path, encoding="utf-8").read()
    if TEMPLATE_CT in ct:
        ct = ct.replace(TEMPLATE_CT, PRES_CT)
        open(ct_path, "w", encoding="utf-8").write(ct)
        print("  content type set to presentation (was template)")
    elif PRES_CT in ct:
        print("  content type already presentation")
    else:
        print("  warning: no presentation content-type Override found", file=sys.stderr)

    # Collect files; write [Content_Types].xml first, which some readers require.
    files = []
    for root, _, names in os.walk(unpacked_dir):
        for n in names:
            full = os.path.join(root, n)
            arc = os.path.relpath(full, unpacked_dir)
            files.append((full, arc))
    files.sort(key=lambda fa: (fa[1] != "[Content_Types].xml", fa[1]))

    if os.path.exists(out_path):
        os.remove(out_path)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for full, arc in files:
            z.write(full, arc)
    print(f"  wrote {out_path} ({len(files)} parts)")


def verify(out_path):
    try:
        import importlib
        Presentation = importlib.import_module("pptx").Presentation
    except ImportError:
        print("  (python-pptx not installed; skipping open-check)")
        return True
    try:
        Presentation(out_path)
        print("  verified: opens with python-pptx")
        return True
    except Exception as e:  # noqa: BLE001
        print(f"  ERROR: python-pptx cannot open the file: {e}", file=sys.stderr)
        return False


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    unpacked_dir, out_path = argv[1], argv[2]
    if not os.path.isdir(unpacked_dir):
        print(f"not a directory: {unpacked_dir}", file=sys.stderr)
        return 2
    pack(unpacked_dir, out_path)
    return 0 if verify(out_path) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
