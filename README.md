# Leadership-Link Claude system

A Claude-based production system for generating Leadership-Link work that reflects Dr.
Eileen Habelow's reasoning, preserves proprietary Leadership-Link frameworks exactly,
and produces practical, presentation-ready leadership content.

The system is built as **two separate, composable Claude Skills**. They are kept
separate on purpose: one governs judgment and language, the other governs presentation
and production. Do not merge them.

## The two Skills

### 1. Eileen Intelligence (`skills/eileen-intelligence`)

The reasoning and language layer. It controls judgment, coaching posture, voice,
framework fidelity, source hierarchy, and confidentiality. Use it for executive
explanations, coaching responses, workshop and facilitator language, public writing,
private strategic analysis, and any content destined for a Leadership-Link
presentation.

- `SKILL.md`: operating sequence, reasoning posture, voice rules, output modes,
  framework fidelity, source hierarchy, governance, and the quality gate.
- `references/frameworks.md`: the framework catalog (Managers in Motion and every
  registered framework), preserved exactly.
- `references/output-modes.md`: detailed structure for each output mode.
- `references/governance.md`: confidentiality and fact-versus-inference rules.

### 2. Leadership-Link Deck Builder (`skills/leadership-link-deck-builder`)

The presentation production layer. It controls presentation architecture, the approved
visual and brand system, the approved PowerPoint template, production mechanics,
validation, and export. Use it whenever the deliverable is a deck, slides, workshop or
facilitator deck, executive briefing, learning material, or presentation export.

- `SKILL.md`: production workflow, brand summary, corrections handling, refusal and
  escalation behavior, and the pre-delivery check.
- `references/brand-system.md`: colors, typography, sizing, footer, and visual
  standards.
- `references/validation.md`: the pre-delivery validation checklist.
- `references/corrections-log.md`: the Corrections Log and the "What Great Looks Like"
  release standard.
- `assets/README.md`: how to supply the required, proprietary
  `Leadership-Link_Deck_Template.potx` (not committed; must come from Leadership-Link).

## How they compose

When the deliverable is a Leadership-Link deck, both Skills apply:

- **Eileen Intelligence** controls the thinking, language, framework use, and coaching
  posture.
- **Leadership-Link Deck Builder** controls the presentation architecture, visual
  system, production mechanics, validation, and export.

Get the content right first, then produce it. Production polish never substitutes for
correct reasoning or exact framework language.

## Operating principles

- Accuracy and fidelity outrank the appearance of completeness.
- Proprietary Leadership-Link frameworks are never invented, renamed, merged,
  simplified, reinterpreted, or extended.
- Verified fact, supported conclusion, inference, and speculation are kept
  distinguishable.
- Client confidentiality is preserved; information is never carried between engagements
  without authorization.
- An incomplete output that names its source gap is preferable to a complete-looking
  fabrication.

## Installing the Skills

Copy (or symlink) each skill directory into a location Claude loads Skills from, for
example a project `.claude/skills/` directory or a personal Skills directory:

```
.claude/skills/eileen-intelligence
.claude/skills/leadership-link-deck-builder
```

To make the Deck Builder fully operational, place the approved
`Leadership-Link_Deck_Template.potx` in
`skills/leadership-link-deck-builder/assets/` (see that folder's `README.md`).
