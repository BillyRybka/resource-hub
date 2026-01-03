---
name: extract-content-ideas
description: Mine existing content (videos, courses, transcripts) for standalone value units that solve specific viewer problems. Use when repurposing long-form content, planning content series, or identifying high-potential clips.
---

<essential_principles>
## Content is Not Monolithic

A 30-minute video isn't one piece of content - it's 5-15 problem-solution units stacked together. Each unit solves ONE specific problem and can potentially stand alone.

**The Extraction Mindset:**
- Content = collection of value units, not a single thing
- Each value unit has its own problem-solution arc
- Some units are better than the whole
- Extraction is discovery, not creation

**What Makes a Value Unit:**
- Solves ONE specific problem
- Can stand alone without surrounding context
- Has clear transformation (before → after)
- Viewer can act immediately after consuming

**The 4 Filters (Sequential):**
1. **Problem Identification** - What specific problem does this segment solve?
2. **Standalone Test** - Can this make sense without the surrounding content?
3. **Iceberg Alignment** - Does this fit our positioning (niche tip of broader expertise)?
4. **Demand Signal** - Is there evidence people want this solved?
</essential_principles>

<intake>
What would you like to do?

1. **Extract from source** - Analyze content and identify value units
2. **Classify value units** - Categorize existing units by type and temperature
3. **Audit extraction** - Check extracted units against criteria

**Wait for response before proceeding.**
</intake>

<routing>
| Response | Next Action |
|----------|-------------|
| 1, "extract", "analyze", "source", "find" | → workflows/extract-from-source.md |
| 2, "classify", "categorize", "type", "temperature" | → workflows/classify-value-units.md |
| 3, "audit", "check", "review" | → workflows/audit-extraction.md |
</routing>

<value_unit_types>
## Value Unit Types & Temperature

| Type | Temperature | Best Formats | Example |
|------|-------------|--------------|---------|
| Quick tactic/tip | Cold (discovery) | Short, LinkedIn, Twitter | "One question to ask before any meeting" |
| Framework/mental model | Cold → Warm | YouTube video, carousel, email | "The 4-filter extraction method" |
| Story/case study | Warm (trust) | YouTube, long-form, podcast clip | "How client X went from A to B" |
| Contrarian take | Cold (discovery) | Short, tweet, hook | "Most content advice is wrong because..." |
| Step-by-step process | Warm → Hot | YouTube, email sequence, guide | "How to extract value units in 4 steps" |
| Mistake/warning | Cold (discovery) | Short, carousel | "The #1 reason repurposed content fails" |
| Transformation proof | Warm → Hot | YouTube, testimonial, case study | "Before/after of using this method" |

**Temperature Guide:**
- **Cold**: Discovery content for new audiences (broad appeal, shareable)
- **Warm**: Trust-building for known audiences (depth, credibility)
- **Hot**: Conversion content for engaged audiences (specific, actionable)
</value_unit_types>

<output_format>
## Value Unit Output Spec

For each extracted value unit, capture:

```markdown
## Value Unit: [Working Title]

**Problem Statement**: [What specific problem does this solve?]
**Solution Summary**: [2-3 sentence core insight]
**Transformation**: [Before → After for the viewer]
**Standalone?**: [Yes/No + why]
**Iceberg Fit**: [How does this relate to core expertise?]
**Demand Evidence**: [Search volume, comments, questions that validate demand]
**Type**: [From value unit types table]
**Temperature**: [Cold/Warm/Hot]
**Best Formats**: [Where this would work best]
**Source**: [Original content + timestamp/section]
**Hook Potential**: [Possible opening line or hook]
```
</output_format>

<reference_index>
## Domain Knowledge

All in `references/`:

| File | Content |
|------|---------|
| content-extraction-framework.md | Full 4-filter process, examples |
| value-unit-criteria.md | What makes a valid value unit |
| temperature-classification.md | Cold/Warm/Hot mapping |
</reference_index>

<templates_index>
## Output Templates

All in `templates/`:

| File | Purpose |
|------|---------|
| extraction-analysis.md | Full source analysis output |
| value-unit-card.md | Individual value unit spec |
</templates_index>

<workflows_index>
## Workflows

All in `workflows/`:

| Workflow | Purpose |
|----------|---------|
| extract-from-source.md | Analyze content, apply 4 filters, output units |
| classify-value-units.md | Categorize units by type and temperature |
| audit-extraction.md | Check units against quality criteria |
</workflows_index>

<success_criteria>
A complete extraction has:
- [ ] Source content fully analyzed
- [ ] Each potential value unit identified
- [ ] 4 filters applied to each unit
- [ ] Units that pass filters fully documented
- [ ] Type and temperature classified
- [ ] Best formats identified
- [ ] Hook potential noted
- [ ] Units that fail filters noted with reason
</success_criteria>

<continual_learning>
Before starting work, check for accumulated knowledge:
- Read learnings.md for patterns that work
- Read failures.md for approaches to avoid

After completing an extraction, suggest running /retrospective to capture new insights.
</continual_learning>
