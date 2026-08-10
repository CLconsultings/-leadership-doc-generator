# Tools

## deck-generator.html

A self-contained, on-brand HTML deck generator in Eileen's LLOD / Leadership-Link
styles (Tahoma; Navy #0A1F44, Orange #F2541B, Gold #D4AF37, Lime #A6CE39). Open the
file in any browser — no build, no dependencies, no network.

- Pick a program (Managers / Teams / Senior Leaders / Leaders in Motion).
- Two presets per program: **Facilitation deck** (full workshop) and
  **Executive briefing** (lean).
- The repetitive slides (Mission, Ground Rules, Thank You / contact, footer, wordmark)
  are premade; the customizable parts (title, subtitle, Big Idea, section/module titles,
  a spotlight content slide) are editable fields with sensible defaults.
- A **Brand** toggle switches the wordmark and domain between Leadership-Link and
  Leadership-Link On-Demand (LLOD).
- **Print / Save as PDF** renders each slide to a full landscape page.

Fidelity: Managers, Teams, and Senior Leaders presets carry verified content; Leaders in
Motion ships as «placeholders» because its six-module curriculum is not yet verified —
fill those before delivering. Know2Grow is retired; the tool uses LLOD only.


## build_deck_from_spec.py

Turns the generator's exported settings into an **editable PowerPoint on the real
template**. In the generator, click **Download settings** to get `deck-settings.json`,
then:

```
python tools/build_deck_from_spec.py deck-settings.json out.pptx
```

It builds the deck by chrome inheritance on `Leadership-Link_Deck_Template.potx` (real
masters, logo, headshot, QR), packs it with the correct presentation content type, and
verifies it opens with python-pptx. Handles any number of overview items (4 blocks/moves
or 6 modules). This is the template-accurate export path — higher fidelity than an
in-browser rebuild, and verified before delivery.


## test_deck_generator.js

Interaction regression test for the generator's controls (requires jsdom: `npm install
jsdom`). Loads `deck-generator.html`, runs its script in a real DOM, and clicks every
control — program select, Design Option 1/2, per-slide A/B, Reset, Download settings,
Print — asserting each does what it should.

```
npm install jsdom && node tools/test_deck_generator.js
```
