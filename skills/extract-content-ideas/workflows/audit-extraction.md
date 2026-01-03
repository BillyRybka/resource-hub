# Workflow: Audit Extraction

Check extracted value units against quality criteria and identify gaps.

<required_reading>
1. references/value-unit-criteria.md
2. references/content-extraction-framework.md
</required_reading>

<process>
<!-- ============================================ -->
<!-- STEP 1: GATHER EXTRACTION                    -->
<!-- ============================================ -->
<step name="gather">
Get the extraction to audit:

**Accept:**
- Previous extraction summary
- List of value units with documentation
- Or file path to extraction output

Need the full value unit cards to audit properly.
</step>

<!-- ============================================ -->
<!-- STEP 2: AUDIT EACH UNIT                      -->
<!-- ============================================ -->
<step name="audit_units">
For each value unit, score against criteria:

**Problem Clarity (1-5)**
- 5: Crystal clear, specific, completable problem
- 3: Problem is clear but could be more specific
- 1: Vague or unclear what problem is solved

**Standalone Quality (1-5)**
- 5: Completely self-contained, no context needed
- 3: Mostly standalone, minor context helps
- 1: Requires significant external context

**Iceberg Alignment (1-5)**
- 5: Perfectly aligned with core expertise/positioning
- 3: Related but not directly in wheelhouse
- 1: Off-topic or attracts wrong audience

**Demand Evidence (1-5)**
- 5: Strong evidence (search volume, comments, competitor success)
- 3: Some signals but not definitive
- 1: No evidence or negative signals

**Hook Potential (1-5)**
- 5: Obvious viral hook, stops the scroll
- 3: Good hook but not exceptional
- 1: No clear hook, hard to capture attention

**Total Score**: Sum of all criteria (max 25)
</step>

<!-- ============================================ -->
<!-- STEP 3: IDENTIFY WEAK POINTS                 -->
<!-- ============================================ -->
<step name="weak_points">
For units scoring below 4 in any category, note:

```markdown
## [Unit Title] - Weak Points

**Score**: [X/25]

**Issues:**
- [Category]: [Score] - [What's wrong]
- [Category]: [Score] - [What's wrong]

**Improvement Suggestions:**
- [Specific suggestion to improve weak area]
- [Specific suggestion to improve weak area]

**Verdict**: [Keep as-is / Improve / Discard / Merge with another]
```
</step>

<!-- ============================================ -->
<!-- STEP 4: CHECK COVERAGE                       -->
<!-- ============================================ -->
<step name="coverage">
Analyze the extraction for gaps:

**Type Coverage:**
- [ ] Quick tactic/tip present?
- [ ] Framework/mental model present?
- [ ] Story/case study present?
- [ ] Contrarian take present?
- [ ] Step-by-step process present?
- [ ] Mistake/warning present?
- [ ] Transformation proof present?

**Temperature Coverage:**
- Cold (discovery): [X] units
- Warm (trust): [X] units
- Hot (conversion): [X] units

**Gaps Identified:**
- Missing types: [List]
- Temperature imbalance: [Description]
</step>

<!-- ============================================ -->
<!-- STEP 5: CHECK SOURCE UTILIZATION             -->
<!-- ============================================ -->
<step name="utilization">
Assess how well the source was mined:

**Questions:**
- Were there obvious value units missed?
- Could any failed candidates be rescued?
- Is there unrealized potential in the source?

**Utilization Score:**
- High: Most valuable content extracted
- Medium: Good extraction but opportunities remain
- Low: Significant value left on the table

If utilization is Medium or Low, note specific missed opportunities.
</step>

<!-- ============================================ -->
<!-- STEP 6: OUTPUT AUDIT REPORT                  -->
<!-- ============================================ -->
<step name="output">
Create audit report:

```markdown
# Extraction Audit Report

**Source**: [Original content]
**Date Audited**: [Date]

## Quality Scores

| Unit | Problem | Standalone | Iceberg | Demand | Hook | Total |
|------|---------|------------|---------|--------|------|-------|
| [Title] | [1-5] | [1-5] | [1-5] | [1-5] | [1-5] | [X/25] |

**Average Score**: [X/25]
**Highest Scoring**: [Unit name] ([Score])
**Lowest Scoring**: [Unit name] ([Score])

## Units Needing Improvement
[List units with specific issues and suggestions]

## Coverage Analysis
**Types Present**: [List]
**Types Missing**: [List]
**Temperature Balance**: [Cold X% / Warm Y% / Hot Z%]

## Utilization Assessment
**Score**: [High/Medium/Low]
**Missed Opportunities**: [If any]

## Recommendations

### High Priority
1. [Most important action]
2. [Second priority]

### Nice to Have
1. [Lower priority improvement]
2. [Lower priority improvement]

## Overall Verdict
[Summary assessment of extraction quality and what to do next]
```
</step>
</process>

<success_criteria>
- [ ] All units scored against criteria
- [ ] Weak points identified with improvement suggestions
- [ ] Coverage gaps analyzed
- [ ] Source utilization assessed
- [ ] Clear recommendations provided
- [ ] Overall verdict given
</success_criteria>
