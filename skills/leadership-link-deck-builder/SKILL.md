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

## When this skill applies

Use it for Leadership-Link presentations, workshops, facilitator decks, executive
briefings, learning materials, and presentation exports.

On every Leadership-Link deck, also load `eileen-intelligence`. That skill owns the
thinking, language, framework use, and coaching posture. This skill owns presentation
architecture, the visual system, production mechanics, validation, and export. Get the
content right first, then produce it; do not let production polish paper over a
framework or reasoning error.

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

Use `assets/Leadership-Link_Deck_Template.potx`. The approved template carries the
Leadership-Link layout system, logo variants, visual assets, headshot, QR assets, and
presentation structure. Do not recreate the brand from memory when the template is
available. If the template file is not present in `assets/`, see
`assets/README.md` and stop before producing branded slides rather than reconstructing
the brand yourself.

### 4. Build the narrative

Use a presentation sequence, not a document split into pages:

1. context or tension
2. why it matters
3. framework or concept
4. practical application
5. participant or leader action
6. reinforcement or next step

Give each slide one primary job. If a slide is doing two jobs, split it.

### 5. Produce editable slides

Use native editable PowerPoint objects wherever possible. Do not flatten complete
slides into images. Preserve editable text, editable shapes, usable speaker notes,
template layouts, consistent masters, and export compatibility. An editable deck is the
deliverable; a picture of a deck is not.

### 6. Write speaker notes

Speaker notes must add value beyond the slide, never repeat it verbatim. Include, where
relevant, facilitator intent, transition language, discussion prompts, an explanation of
the model, timing guidance, likely participant reactions, application instructions, and
caution points.

### 7. Validate the deck

Run the validation checklist in `references/validation.md` before delivery. Revise any
failure before delivering; do not ship a known failure with a note.

### 8. Export

Provide the requested native and presentation formats. Keep the editable PowerPoint as
the primary source file.

## Brand and visual system

Use the approved Leadership-Link visual system. The full specification (colors,
typography, sizing, footer, and visual standards) is in `references/brand-system.md`.
Load it whenever you make a visual decision. Key points:

- Core colors include Navy `#1C1E43`, Orange `#ED8344`, Grey `#999999`, Light blue
  `#BAD3E9`, Purple `#5D386C`, Green `#9BBB59`. Where the current approved template uses
  later signal colors, preserve the template rather than substituting values by hand.
- Typography: Merriweather where the template and brand standards require it, sentence
  case, no decorative or generic technology fonts.
- Body content is minimum 18 pt. The 11 pt exception is only for muted, non-substantive
  structural labels, never for body copy, instructions, evidence, model definitions, or
  participant actions.
- Footer: `Leadership-Link | Ask AI-Leen`, and where required, `powered by
  know2grow.com`. Preserve approved logo and capitalization treatments.

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

Confirm the correct skills were applied (this one plus `eileen-intelligence`), the
output mode was identified, only relevant references were loaded, Eileen's judgment
appears before stylistic imitation, framework names and structures are exact, no
proprietary content was invented, fact and inference are distinguishable,
confidentiality is preserved, the approved template was used, slides remain editable,
body text meets minimum sizing, the 11 pt exception was used only for muted structural
labels, speaker notes add value, the Corrections Log was applied internally, and the
output meets the "What Great Looks Like" standard. Revise before delivery if any item
fails.
