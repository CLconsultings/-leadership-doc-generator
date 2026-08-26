---
name: red-flag-run
description: >-
  Authorship-preserving writing audit and editing layer for public, executive, client,
  social, and professional prose. Use when the user asks for a Red Flag Run, /human,
  an AI-pattern scan, less generic or less AI-sounding writing, authorship fidelity,
  final copy QA, or a rewrite that must remain recognizably theirs. Detect named writing
  patterns without claiming who wrote the text; preserve known human-authored language;
  make only necessary edits; test generic sentences for portability; protect specific
  facts and uncertainty; and compose after any domain, brand, evidence, or framework skill.
---

# Red Flag Run

Use this as a final authorship and writing-quality layer. Improve the prose without
quietly replacing the writer.

Do not optimize for AI-detector scores or help misrepresent authorship. Style is not
proof of authorship. The job is to preserve authentic contribution, remove formulaic
writing patterns, and make the smallest change that materially improves the piece.

## Operating priority

Apply these rules in order:

1. Preserve meaning, factual integrity, and authorized framework language.
2. Preserve known human-authored wording and the writer's recognizable voice.
3. Remove or repair named formulaic patterns that reduce clarity or authorship fidelity.
4. Improve specificity, readability, and cadence only where the draft needs it.
5. Stop editing when further polish would mostly make the piece smoother rather than better.

When another skill governs domain reasoning, proprietary frameworks, brand language,
legal constraints, evidence, or confidentiality, that skill wins on those matters.
Run Red Flag Run after the governing content is correct.

For Leadership-Link work, pair with `eileen-intelligence`. Eileen Intelligence controls
judgment, framework fidelity, coaching posture, and approved voice. Red Flag Run controls
authorship preservation and formulaic writing patterns where doing so does not conflict
with Eileen Intelligence.

## Choose the mode

Use the user's requested mode. If none is stated, infer the least destructive one.

**Detect.** Audit without rewriting. Name the pattern, quote only the shortest useful
excerpt, explain why it is a problem in this draft, and give a concise correction direction.
Do not score the text, guess whether AI wrote it, or rewrite the full piece.

**Edit.** Return a revised draft. Make the minimum effective edit. Preserve strong original
sentences, useful roughness, asymmetry, bluntness, uncertainty, humor, and natural changes
in pace when they belong to the writer.

**Final audit.** Review a near-final piece after other edits. Change only clear failures:
unsupported claims, displaced authorship, generic filler, repeated formulaic structures,
or wording that materially weakens the intended voice.

If the user asks for copy-paste-ready text, return only the finished artifact unless they
also request an audit record.

## Authorship and provenance gate

Before editing, identify what can reasonably be preserved as author-originated.

- Treat the user as the author of the ideas and intended message unless there is clear
  evidence that a specific passage came from another source or was model-added.
- Preserve known human-authored phrases rather than replacing them with cleaner synonyms.
- Use conversation history, supplied drafts, tracked revisions, or explicit attribution
  when available. Do not invent provenance.
- When provenance is uncertain, preserve the wording if it works and describe attribution
  as uncertain if attribution matters to the task.
- Do not introduce fake imperfections to make writing look human.
- Do not claim that a stylistic pattern proves AI authorship.

A change to distinctive wording should earn its cost through accuracy, clarity, removal
of repetition, audience fit, or repair of a named pattern.

## Voice-preservation pass

Read the whole draft before changing it. Identify internally:

- the actual point
- the intended reader and destination when known
- characteristic vocabulary
- sentence length and cadence
- degree of bluntness or restraint
- uncertainty and qualification
- humor, asides, fragments, or unevenness that carry character

Do not normalize all of these into polished corporate prose.

## Pattern scan

Load `references/pattern-library.md` when editing or auditing substantive prose.

Flag patterns by evidence in the actual draft, not because a word appears on a blacklist.
A word is a problem only when its use is generic, inflated, unnecessary, imprecise, or
inconsistent with the writer's established voice.

Pay special attention to clusters. One ordinary transition may be harmless; several
formulaic transitions, binary contrasts, symmetrical paragraphs, and dramatic kickers in
the same short piece are stronger evidence that the prose has become templated.

## Portability test

Test any sentence that feels generic:

> Could this sentence move unchanged to another person, company, product, industry, or
> topic and still sound plausible?

If yes, it is probably not doing enough work. Prefer one of four repairs:

1. cut it
2. replace it with a specific fact already supported by the material
3. state the mechanism or consequence
4. state the writer's actual judgment in plain language

Do not invent a fact merely to make a sentence more specific.

## Protect the specific fact

Do not smooth an operational detail, number, date, mechanism, limitation, or concrete
example into abstract importance. Specific evidence usually carries more authority than
an adjective saying the point is important.

Likewise, preserve real uncertainty. Do not turn "may," "I think," "based on what we know,"
or similar bounded language into certainty unless the evidence supports the stronger claim.

## Minimum-effective-edit rule

Make the smallest set of changes that solves the actual writing problem.

Leave a sentence alone when it is clear, accurate, specific, in voice, and not part of a
harmful repeated pattern. Do not rewrite it for consistency alone.

Do not automatically:

- shorten every sentence
- front-load every paragraph
- convert every paragraph to bullets
- remove every fragment
- remove every personal aside
- replace repeated clear terms with synonyms
- remove every colon or dash
- force a polished opening and concluding takeaway

Editing should not erase evidence of the writer's own thinking process.

## Evidence and claim check

Writing quality cannot repair weak evidence.

- Do not add statistics, examples, quotations, sources, outcomes, or causal claims that are
  not supported by the supplied material or an authorized source.
- Preserve the distinction between observed fact, evidence-supported conclusion, inference,
  and speculation when the distinction matters.
- Replace vague source claims such as unnamed experts or studies with a named source when
  available; otherwise flag the unsupported attribution rather than fabricating support.
- Do not strengthen a claim merely because the stronger version reads better.

## Evaluation

Load `references/evaluation.md` after an edit or final audit. Run it internally before
returning the result. If a check fails, fix only the failed issue and run the relevant
checks again.

## Output discipline

For **Detect**, use a compact findings format:

- pattern
- shortest useful excerpt
- why it weakens this draft
- correction direction

For **Edit**, follow the requested destination and formatting. Do not add a generic
"What changed" section when the user asked for only the final copy. Provide change notes
only when requested or when a material meaning/structure change needs disclosure.

For **Final audit**, return the final artifact plus only the unresolved evidence,
provenance, or authorization issue that could still change the decision to publish.
