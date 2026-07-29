# Deck Builder assets

## Required: Leadership-Link_Deck_Template.potx

The Deck Builder workflow opens the approved PowerPoint template at:

```
assets/Leadership-Link_Deck_Template.potx
```

This template is the source of the Leadership-Link layout system, logo variants, visual
assets, headshot, QR assets, and presentation structure.

**This file is intentionally not committed here and must be supplied by
Leadership-Link.** It is a proprietary brand asset and is not reconstructed from memory.
Recreating the brand by hand would violate the fidelity rules the Skill exists to
enforce, so the template is treated as a required, authoritative input rather than
something the Skill generates.

### To make the Deck Builder fully operational

Place the approved `Leadership-Link_Deck_Template.potx` in this `assets/` directory.

### When the template is absent

If the template is not present, the Deck Builder must stop before producing branded
slides and report, per its refusal and escalation behavior:

1. what is verified;
2. what remains unknown;
3. which source is required (this template);
4. what can safely be produced now (for example, an outline, narrative structure, and
   speaker-note drafting that do not depend on the brand assets).
