# Leadership-Link Claude system

A Claude-based production system for generating Leadership-Link work that reflects Dr.
Eileen Habelow's reasoning, preserves proprietary Leadership-Link frameworks exactly,
and produces practical, presentation-ready leadership content.

The system is a **foundational operating profile plus two composable operating-layer
Skills**. The profile is the authoritative source of Eileen's voice, brand, frameworks,
and non-negotiables. The two skills add the structured reasoning and production discipline
on top of it. They are kept separate on purpose; do not merge the two operating layers.

## Source of truth

### Eileen Operating Profile (`skills/eileen-operating-profile`)

Eileen's authoritative operating profile, verbatim. Voice and writing rules, brand
standards (Tahoma; Navy `#0A1F44` / Orange `#F2541B` / Gold `#D4AF37` / Lime `#A6CE39`;
the `Leadership-Link | Eileen Habelow, PhD` footer; the visual-first deck system and
standard workshop slides), the proprietary programs and models, confidentiality rules, and
the Corrections Log. Load it at the start of any Leadership-Link work. When anything in the
two skills below disagrees with this profile, the profile wins.

The approved template `Leadership-Link_Deck_Template.potx` ships with this profile and
lives in the Deck Builder's `assets/` (below).

## The two operating-layer Skills

### 1. Eileen Intelligence (`skills/eileen-intelligence`)

The reasoning and language layer. Judgment, coaching posture, voice, framework fidelity,
source hierarchy, and confidentiality. Use it for executive explanations, coaching
responses, workshop and facilitator language, public writing, private strategic analysis,
and any content destined for a Leadership-Link presentation.

- `SKILL.md`: operating sequence, reasoning posture, voice rules, output modes, framework
  fidelity, source hierarchy, governance, and the quality gate.
- `references/frameworks.md`: the framework catalog (flagship programs, Managers in Motion
  four-block sequence, proprietary models, external frameworks), preserved exactly.
- `references/output-modes.md`: detailed structure for each output mode.
- `references/governance.md`: confidentiality and fact-versus-inference rules.

### 2. Leadership-Link Deck Builder (`skills/leadership-link-deck-builder`)

The presentation production layer. Presentation architecture, the approved visual and brand
system, the approved PowerPoint template, production mechanics, validation, and export. Use
it whenever the deliverable is a deck, slides, workshop or facilitator deck, executive
briefing, learning material, or presentation export.

- `SKILL.md`: production workflow, brand summary, corrections handling, refusal and
  escalation behavior, and the pre-delivery check.
- `references/brand-system.md`: colors, typography, sizing, footer, layout system, and
  visual standards (mirrors the profile).
- `references/validation.md`: the pre-delivery validation checklist.
- `references/corrections-log.md`: the Corrections Log and the "What Great Looks Like"
  release standard.
- `assets/Leadership-Link_Deck_Template.potx`: the approved 23-layout template (present),
  with `assets/README.md` explaining chrome-inheritance use.

## How they compose

When the deliverable is a Leadership-Link deck, all three apply:

- **Eileen Operating Profile** is the authoritative standard for voice, brand, and
  frameworks.
- **Eileen Intelligence** controls the thinking, language, framework use, and coaching
  posture.
- **Leadership-Link Deck Builder** controls the presentation architecture, visual system,
  production mechanics, validation, and export, building from the approved template by
  chrome inheritance.

Get the content right first, then produce it. Production polish never substitutes for
correct reasoning or exact framework language.

## Operating principles

- Accuracy and fidelity outrank the appearance of completeness.
- Proprietary Leadership-Link frameworks are never invented, renamed, merged, simplified,
  reinterpreted, or extended.
- The brand standard is the operating profile and the approved template, not whatever deck
  is at hand; some circulating program decks are off-brand drafts.
- Verified fact, supported conclusion, inference, and speculation are kept distinguishable.
- Client confidentiality is preserved; information is never carried between engagements
  without authorization.
- An incomplete output that names its source gap is preferable to a complete-looking
  fabrication.

## Installing the Skills

Copy each skill directory into a location Claude loads Skills from, for example a project
`.claude/skills/` directory or a personal Skills directory:

```
.claude/skills/eileen-operating-profile
.claude/skills/eileen-intelligence
.claude/skills/leadership-link-deck-builder
```

The Deck Builder is fully operational: the approved `Leadership-Link_Deck_Template.potx` is
in `skills/leadership-link-deck-builder/assets/`.
