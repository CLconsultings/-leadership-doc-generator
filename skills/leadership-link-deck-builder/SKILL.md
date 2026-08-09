---
name: leadership-link-deck-builder
description: >-
  Presentation production layer for Leadership-Link. Use this whenever the deliverable
  is a Leadership-Link presentation, deck, slide, workshop or facilitator deck, executive
  briefing, learning material, or a presentation export, even if the user just says
  "deck," "slides," or "presentation" without naming Leadership-Link. It controls
  presentation architecture, the approved visual and brand system, the approved
  PowerPoint template, production mechanics, validation, and export. Pair it with the
  eileen-intelligence skill on every Leadership-Link deck: that skill controls the
  thinking, language, framework fidelity, and coaching posture; this skill controls how
  that content is structured and produced as slides.
---

# Leadership-Link Deck Builder

The production layer for Leadership-Link presentations. It turns approved content into
editable, on-brand, presentation-ready slides. It does not decide what the content
should say; that is the job of `eileen-intelligence`.

The authoritative brand, voice, and framework source is Eileen's operating profile
(`skills/eileen-operating-profile/SKILL.md`). Load it too. Where any detail here disagrees
with the profile, the profile wins.

## When this skill applies

Use it for Leadership-Link presentations, workshops, facilitator decks, executive
briefings, learning materials, and presentation exports.

On every Leadership-Link deck, also load `eileen-intelligence` and
`eileen-operating-profile`. Those own the thinking, language, framework use, voice, and
coaching posture. This skill owns presentation architecture, the visual system, production
mechanics, validation, and export. Get the content right first, then produce it; do not
let production polish paper over a framework or reasoning error.

The mechanics of building `.pptx`/`.potx` files (opening the template, editing slides,
speaker notes, export) are handled by the `pptx` skill. Load it for the file-level work
and use this skill for the Leadership-Link brief, narrative, brand system, and
validation on top of it.

## Required production workflow

### 1. Establish the brief

Determine the audience, the purpose, the presentation setting, the expected decision or
behavior, the required length, the source materials, and whether the deck is
participant-facing, facilitator-facing, executive-facing, or internal. These decisions
change nearly everything downstream, so settle them first.

### 2. Inspect approved sources

Locate the relevant approved program materials. Identify framework names and required
wording. Identify anything missing. Distinguish approved curriculum from reinforcement
materials, working drafts, and inference. Do not begin framework-specific slide
production with unresolved foundational gaps; resolve them or flag them first (see
Refusal and escalation).

### 3. Open the approved template

Use `assets/Leadership-Link_Deck_Template.potx` (present in this skill). It carries the
Leadership-Link layout system (23 layouts, including the standard workshop slides), the
logo variants, Eileen's headshot, the LinkedIn QR, and the icon-in-circle motif. Do not
recreate the brand from memory when the template is available. Build by **chrome
inheritance**: duplicate an existing branded template slide and replace only its text, so
the header, footer, colors, and layout are preserved. Never rebuild a branded slide from
scratch when the chrome exists (Corrections Log). If the template were ever missing, stop
before producing branded slides rather than reconstructing the brand yourself.

### 4. Build the narrative

Workshop decks follow the standard skeleton (see the operating profile): Mission → Ground
Rules → Big Idea → Three Keys → (key section breaks and content) → Action Commitment →
Thank You. For programs whose architecture is not three keys (for example Managers in
Motion, a four-block system), adapt the skeleton to the program's real structure using the
template's numbered section dividers, and say what you adapted.

Within that skeleton, sequence content as: context or tension; why it matters; framework
or concept; practical application; participant or leader action; reinforcement or next
step. Give each slide one primary job (one idea per slide). If a slide is doing two jobs,
split it.

### 5. Produce editable slides

Use native editable PowerPoint objects only. Never flatten a slide into a single image;
every element must be individually selectable, movable, and retypeable. Preserve editable
text, editable shapes, usable speaker notes, template layouts, and consistent masters.
Keep visuals-first: few words on the slide face, the presenter carries the words.

### 6. Write speaker notes

Every slide ships with speaker notes, without being asked; a deck with empty notes is a
defect. The slide face stays sparse and the notes carry what the presenter would actually
say to that slide: the narration, the point being made, and the transition into the next
slide. Add value beyond the slide, never repeat it verbatim. Include, where relevant,
facilitator intent, transition language, discussion prompts, an explanation of the model,
timing guidance, likely participant reactions, application instructions, and caution
points. Bracketed asides mark presenter guidance not read aloud.

### 7. Validate the deck

Run the validation checklist in `references/validation.md` before delivery. Revise any
failure before delivering; do not ship a known failure with a note.

### 8. Export

Provide the requested native and presentation formats. Keep the editable PowerPoint as
the primary source file.

The template is a `.potx`, so a deck built from it inherits the template content type. Pack
the finished deck with `scripts/pack_pptx.py`, which rewrites the `/ppt/presentation.xml`
Override from `...presentationml.template.main+xml` to
`...presentationml.presentation.main+xml` and verifies the result opens with python-pptx:

```
python scripts/pack_pptx.py <unpacked_dir> <output.pptx>
```

Do not hand-zip a template-derived deck. A `.pptx` that keeps the template content type
opens in LibreOffice and passes the XSD but PowerPoint refuses it ("PowerPoint can't read").
Always confirm the deck opens with a PowerPoint-like parser (python-pptx) before delivery,
not only the XSD validator.

## Brand and visual system

Use the approved Leadership-Link visual system. The full specification (colors,
typography, sizing, footer, layout system, and visual standards) is in
`references/brand-system.md`, which mirrors the operating profile. Load it whenever you
make a visual decision. Key points:

- Core colors: Navy `#0A1F44` (dominant, 60-70% of visual weight), Orange `#F2541B`
  (accent), Gold `#D4AF37` (secondary accent), Lime `#A6CE39` (sparingly). Never give the
  four equal weight. Prefer the template's own values over hand-substituting.
- Typography: **Tahoma** across all deliverables, sentence case. Not Merriweather, not a
  decorative or generic technology font.
- PowerPoint has an 18 pt floor: nothing below 18 pt except a footnote or source citation.
  If text will not fit at 18 pt, cut words, do not shrink type. Elsewhere (Word, PDF,
  footers) the floor is 10 pt. The 11 pt exception is only for muted, non-substantive
  structural labels, never for body copy, instructions, evidence, model definitions, or
  participant actions.
- Footer: `Leadership-Link | Eileen Habelow, PhD`. Preserve the approved logo and
  capitalization treatments; use the white-knockout logo on navy, the full-color logo on
  light.
- Dark/light sandwich, cards not bars (never edge stripes or under-title rules), and the
  icon-in-circle motif on every content slide.

One central message per slide, real whitespace, clear hierarchy, restrained emphasis,
and diagrams only when they teach something. Avoid generic corporate AI imagery,
decorative icons, dense text walls, unapproved fonts, excessive gradients, clutter, and
layouts that read like a report.

## Corrections and calibration

Maintain both the Corrections Log and the "What Great Looks Like" release standard in
`references/corrections-log.md`. Apply the log internally on every deck to prevent
repeating a past failure, and check the release standard before delivery. Never expose
the internal Corrections Log in client-facing work. Calibration examples support
judgment but do not replace explicit corrections or release criteria.

## Refusal and escalation behavior

Stop or narrow the work when a proprietary framework detail cannot be verified, the user
requests unapproved claims or fabricated evidence, the deck would expose confidential
client information, the template or a required source is unavailable, a formal
curriculum deliverable is being inferred from reinforcement content, or current approved
materials cannot be distinguished from older drafts.

When you stop, state: what is verified; what remains unknown; which source is required;
and what can safely be produced now. Do not treat an information gap as permission to
improvise. A polished deck that violates framework fidelity is not acceptable, and an
incomplete deck that clearly names a source gap is preferable to a complete-looking
fabrication.

## Final pre-delivery check

Confirm the correct skills were applied (this one plus `eileen-intelligence` and
`eileen-operating-profile`), the output mode was identified, only relevant references were
loaded, Eileen's judgment appears before stylistic imitation, framework names and
structures are exact, no proprietary content was invented, fact and inference are
distinguishable, confidentiality is preserved, the approved template was used via chrome
inheritance, slides remain editable native objects, the deck is Tahoma on the real palette
with the `Leadership-Link | Eileen Habelow, PhD` footer, body text meets the 18 pt floor,
the 11 pt exception was used only for muted structural labels, every slide has speaker
notes, the Corrections Log was applied internally, and the output meets the "What Great
Looks Like" standard. Revise before delivery if any item fails.
