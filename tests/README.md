# Tests

## e2e_test.py

An end-to-end check for the Leadership-Link Claude system. Run it after editing a skill or
producing a deck.

```bash
python tests/e2e_test.py                    # skills + template only
python tests/e2e_test.py path/to/deck.pptx  # also check a produced deck
```

**System checks:** each skill has valid frontmatter whose `name` matches its directory;
every referenced file resolves; no off-brand tokens (Merriweather, the #1C1E43 draft
palette, etc.) leak into the guidance; the approved template is present, Tahoma, and
on-palette.

**Deck checks** (read straight from the `.pptx`/`.potx` zip): Tahoma only; colors within
the template palette; the `Leadership-Link | Eileen Habelow, PhD` footer on every slide;
speaker notes on every slide; no leftover template placeholders; the 18pt PowerPoint floor
(allowing 11pt muted labels and the template's QR caption); and, for a Managers in Motion
deck, the four block titles verbatim.

Exits non-zero on any error.

### Limitation

This does not render slides, so it cannot catch purely visual defects (text overflow,
wrapping, overlap). Where a working renderer is available, also convert the deck to images
and inspect them. See the `pptx` skill for `office/validate.py` (OOXML structural
validation) and the render commands.
