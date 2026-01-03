# Workflow: Extract From Source

Analyze content and identify value units using the 4-filter process.

<required_reading>
1. references/content-extraction-framework.md
2. references/value-unit-criteria.md
3. templates/value-unit-card.md
</required_reading>

<process>
<!-- ============================================ -->
<!-- STEP 1: GATHER SOURCE                        -->
<!-- ============================================ -->
<step name="gather_source">
Get the source content from user:

**Ask for:**
- Source type (video transcript, course module, blog post, podcast)
- The actual content (pasted or file path)
- Original title/topic
- Target audience context (if known)

**If video**: Request transcript with timestamps if available.
**If course**: Identify which module/lesson.
**If multiple sources**: Process one at a time.
</step>

<!-- ============================================ -->
<!-- STEP 2: INITIAL SCAN                         -->
<!-- ============================================ -->
<step name="initial_scan">
Read through the entire source and identify:

1. **Topic shifts** - Where does the subject change?
2. **Problem mentions** - Every time a problem is stated or implied
3. **Solution reveals** - Every time a solution, tactic, or insight is given
4. **Story starts** - Every narrative or example that begins
5. **Framework introductions** - Any mental models or systems explained

Create a rough map:
```
[Timestamp/Section] - [What happens here]
00:00 - Hook about common mistake
02:15 - Story about client failure
05:30 - Framework introduction (3 steps)
08:00 - Step 1 deep dive
...
```
</step>

<!-- ============================================ -->
<!-- STEP 3: SEGMENT INTO CANDIDATES              -->
<!-- ============================================ -->
<step name="segment">
Group the map into potential value unit candidates.

**A candidate is a segment that:**
- Has a clear problem it addresses
- Contains some form of solution/insight
- Could potentially stand alone

Don't filter yet - just identify all candidates.

Output format:
```
## Candidate 1: [Working title]
- Section: [timestamp range or section]
- Problem hint: [what problem seems to be addressed]
- Content: [brief summary of what's covered]

## Candidate 2: [Working title]
...
```
</step>

<!-- ============================================ -->
<!-- STEP 4: APPLY FILTER 1 - Problem Identification -->
<!-- ============================================ -->
<step name="filter_1">
For each candidate, answer:

**"What SPECIFIC problem does this segment solve?"**

Requirements:
- Must be a real problem people have (not theoretical)
- Must be specific (not vague like "improve your life")
- Must be completable (viewer knows when problem is solved)

**Pass**: Clear, specific problem statement possible
**Fail**: Problem is vague, theoretical, or unclear

Mark candidates as PASS-F1 or FAIL-F1 with reason.
</step>

<!-- ============================================ -->
<!-- STEP 5: APPLY FILTER 2 - Standalone Test     -->
<!-- ============================================ -->
<step name="filter_2">
For candidates that passed Filter 1:

**"Can this make sense WITHOUT the surrounding content?"**

Check:
- Does it require context from earlier in the video?
- Does it reference things not explained in this segment?
- Would a new viewer understand the value immediately?

**Pass**: Self-contained, new viewer would get it
**Fail**: Requires too much context to make sense

Mark as PASS-F2 or FAIL-F2 with reason.

**Note**: Some fails here can be rescued by adding brief context. Note this possibility.
</step>

<!-- ============================================ -->
<!-- STEP 6: APPLY FILTER 3 - Iceberg Alignment   -->
<!-- ============================================ -->
<step name="filter_3">
For candidates that passed Filter 2:

**"Does this fit our positioning (niche tip of broader expertise)?"**

The "iceberg" concept: You show specific tactical content (tip of iceberg) that implies deeper expertise (underwater).

Check:
- Does this demonstrate expertise in your core domain?
- Would this attract the right audience?
- Does it connect to what you sell/offer?

**Pass**: Clearly aligned with core expertise and positioning
**Fail**: Off-topic or attracts wrong audience

Mark as PASS-F3 or FAIL-F3 with reason.
</step>

<!-- ============================================ -->
<!-- STEP 7: APPLY FILTER 4 - Demand Signal       -->
<!-- ============================================ -->
<step name="filter_4">
For candidates that passed Filter 3:

**"Is there evidence people WANT this solved?"**

Look for demand signals:
- Comments asking about this topic
- Search volume for related queries
- Questions in communities/forums
- Competitor content on this topic performing well
- DMs/emails asking about this

**Pass**: Clear evidence of demand exists
**Fail**: No evidence people care about this problem
**Unknown**: No evidence either way (still viable, lower priority)

Mark as PASS-F4, FAIL-F4, or UNKNOWN-F4 with evidence.
</step>

<!-- ============================================ -->
<!-- STEP 8: DOCUMENT PASSING UNITS               -->
<!-- ============================================ -->
<step name="document">
For each candidate that passed all 4 filters:

Use templates/value-unit-card.md to create full documentation:

```markdown
## Value Unit: [Working Title]

**Problem Statement**: [From Filter 1]
**Solution Summary**: [2-3 sentence core insight]
**Transformation**: [Before → After for the viewer]
**Standalone?**: Yes - [brief note on why]
**Iceberg Fit**: [From Filter 3 - how it connects to expertise]
**Demand Evidence**: [From Filter 4]
**Type**: [Classify using value unit types]
**Temperature**: [Cold/Warm/Hot]
**Best Formats**: [Where this would work best]
**Source**: [Original content + timestamp/section]
**Hook Potential**: [Possible opening line or hook]
```
</step>

<!-- ============================================ -->
<!-- STEP 9: SUMMARIZE EXTRACTION                 -->
<!-- ============================================ -->
<step name="summarize">
Create extraction summary:

```markdown
# Extraction Summary: [Source Title]

**Source**: [Original content details]
**Analyzed**: [Date]

## Results
- Total candidates identified: [X]
- Passed all filters: [Y]
- Failed at Filter 1 (Problem): [Z]
- Failed at Filter 2 (Standalone): [Z]
- Failed at Filter 3 (Iceberg): [Z]
- Failed at Filter 4 (Demand): [Z]
- Unknown demand (still viable): [Z]

## Extracted Value Units
1. [Title] - [Type] - [Temperature]
2. [Title] - [Type] - [Temperature]
...

## Highest Potential
[Which 1-2 units have strongest combination of clear problem, high demand, and good format fit]

## Failed But Rescuable
[Any candidates that failed but could work with modifications]

## Notes for Future
[Any patterns noticed, insights about the source content]
```
</step>
</process>

<success_criteria>
- [ ] Source content fully received and understood
- [ ] Initial scan completed with topic map
- [ ] All candidates identified before filtering
- [ ] Filter 1 applied to all candidates
- [ ] Filter 2 applied to passing candidates
- [ ] Filter 3 applied to passing candidates
- [ ] Filter 4 applied to passing candidates
- [ ] Full documentation for all passing units
- [ ] Summary created with actionable insights
</success_criteria>
