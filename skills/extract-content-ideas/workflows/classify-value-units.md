# Workflow: Classify Value Units

Categorize existing value units by type and temperature for content planning.

<required_reading>
1. references/temperature-classification.md
2. references/value-unit-criteria.md
</required_reading>

<process>
<!-- ============================================ -->
<!-- STEP 1: GATHER UNITS                         -->
<!-- ============================================ -->
<step name="gather">
Get the value units to classify:

**Accept:**
- List of value units from previous extraction
- Raw ideas that need classification
- Existing content pieces to categorize

For each unit, need at minimum:
- Title or description
- What problem it solves
- Brief summary of the content
</step>

<!-- ============================================ -->
<!-- STEP 2: CLASSIFY BY TYPE                     -->
<!-- ============================================ -->
<step name="classify_type">
For each value unit, determine its primary type:

| Type | Identifier | Example |
|------|------------|---------|
| **Quick tactic/tip** | Single actionable thing, small scope | "One question to ask before any meeting" |
| **Framework/mental model** | System for thinking about something | "The 4-filter extraction method" |
| **Story/case study** | Narrative with transformation | "How client X went from A to B" |
| **Contrarian take** | Against common belief | "Most content advice is wrong because..." |
| **Step-by-step process** | Sequential how-to | "How to extract value units in 4 steps" |
| **Mistake/warning** | What NOT to do | "The #1 reason repurposed content fails" |
| **Transformation proof** | Evidence of results | "Before/after of using this method" |

**Note**: Some units are hybrids. Pick the PRIMARY type, note secondary.
</step>

<!-- ============================================ -->
<!-- STEP 3: CLASSIFY BY TEMPERATURE              -->
<!-- ============================================ -->
<step name="classify_temperature">
For each value unit, determine temperature:

**Cold (Discovery)**
- Purpose: Attract new audiences
- Characteristics: Broad appeal, shareable, curiosity-driven
- Best for: Top of funnel, new viewer acquisition
- Formats: Shorts, viral tweets, LinkedIn posts

**Warm (Trust-Building)**
- Purpose: Deepen relationship with existing audience
- Characteristics: More depth, builds credibility, expertise display
- Best for: Middle of funnel, existing subscribers
- Formats: YouTube videos, email sequences, carousels

**Hot (Conversion)**
- Purpose: Move audience toward action
- Characteristics: Specific, actionable, tied to offer
- Best for: Bottom of funnel, engaged leads
- Formats: Deep dives, case studies, webinars

**Classification questions:**
1. Who would find this? (New people = cold, existing audience = warm/hot)
2. What action follows? (Share = cold, engage = warm, buy = hot)
3. How specific is it? (Broad = cold, niche = warm/hot)
</step>

<!-- ============================================ -->
<!-- STEP 4: MAP TYPE TO TEMPERATURE              -->
<!-- ============================================ -->
<step name="map">
Verify classification against typical patterns:

| Type | Typical Temperature | Notes |
|------|---------------------|-------|
| Quick tactic/tip | Cold | Easy to share, attracts new |
| Framework/mental model | Cold → Warm | Can be either depending on depth |
| Story/case study | Warm | Builds trust through narrative |
| Contrarian take | Cold | Controversy attracts attention |
| Step-by-step process | Warm → Hot | Depth signals expertise |
| Mistake/warning | Cold | Fear-based, shareable |
| Transformation proof | Warm → Hot | Credibility for conversion |

If classification differs from typical, note why - it may be correct or may need reconsideration.
</step>

<!-- ============================================ -->
<!-- STEP 5: ASSIGN BEST FORMATS                  -->
<!-- ============================================ -->
<step name="formats">
Based on type + temperature, identify best distribution formats:

**Cold Content Formats:**
- YouTube Shorts / TikTok / Reels
- Twitter/X posts
- LinkedIn posts
- Carousel graphics

**Warm Content Formats:**
- Long-form YouTube videos
- Email sequences
- Blog posts
- Podcast episodes
- LinkedIn articles

**Hot Content Formats:**
- Webinars
- Deep-dive videos
- Case study videos
- Sales emails
- Direct outreach content

Assign 2-3 best formats per unit.
</step>

<!-- ============================================ -->
<!-- STEP 6: OUTPUT CLASSIFICATION                -->
<!-- ============================================ -->
<step name="output">
Create classification summary:

```markdown
# Value Unit Classification

## Cold (Discovery) - [X] units
| Unit | Type | Best Formats |
|------|------|--------------|
| [Title] | [Type] | [Formats] |

## Warm (Trust-Building) - [X] units
| Unit | Type | Best Formats |
|------|------|--------------|
| [Title] | [Type] | [Formats] |

## Hot (Conversion) - [X] units
| Unit | Type | Best Formats |
|------|------|--------------|
| [Title] | [Type] | [Formats] |

## Content Mix Analysis
- Cold: [X]% of units
- Warm: [X]% of units
- Hot: [X]% of units

**Recommendation**: [Note if mix is balanced or if gaps exist]

## Priority Order
Based on current needs, recommend production order:
1. [Unit] - [Why first]
2. [Unit] - [Why second]
...
```
</step>
</process>

<success_criteria>
- [ ] All units received and understood
- [ ] Each unit assigned a primary type
- [ ] Each unit assigned temperature
- [ ] Type-temperature mapping verified
- [ ] Best formats identified for each
- [ ] Summary with content mix analysis created
- [ ] Priority order recommended
</success_criteria>
