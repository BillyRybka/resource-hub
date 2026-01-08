<objective>
Create the **definitive Business Documentary Script-Writing Guide** - a single source of truth.

Purpose: Consolidate patterns from 3 example scripts + existing guides into one comprehensive reference document that a Claude Code skill can use to write scripts.

Input:
- Three example scripts showing the target style with different hook archetypes:
  - example1.md (Disney/Togo): Personal grievance → corporate injustice
  - example2.md (Arizona Tea): Business mystery → impossible economics
  - example3.md (Colonel Sanders): Character reveal → escalating absurdity biography
- Existing guides to consolidate/replace:
  - faceless-writing-guide.md
  - script-writing-guide.md

Output: `faceless/business-documentary-guide.md` - the single source of truth for writing these scripts
</objective>

<context>
Example scripts to analyze:
@faceless/example1.md
@faceless/example2.md
@faceless/example3.md

Existing guides:
@faceless/faceless-writing-guide.md
@faceless/script-writing-guide.md

The examples share a distinct DNA but with important structural variations:

**Shared DNA:**
- **Humanizing subjects**: Making business people feel like real characters with flaws and motivations
- **Witty interjections**: Conversational tangents, absurd comparisons, self-aware humor
- **Moral extraction**: Every story distills to a lesson about business/life/values
- **Adaptive structure**: Hooks vary, pacing varies, segment count varies

**Key Structural Differences to Capture:**

| Aspect | Example 1 (Togo) | Example 2 (Arizona) | Example 3 (Sanders) |
|--------|------------------|---------------------|---------------------|
| **Hook type** | Personal grievance | Business mystery | Character reveal |
| **Structure** | Thematic jumping | Chronological business | Chronological biography |
| **Central question** | "Why did Disney delete this?" | "How do they stay at 99¢?" | "Was this guy even real?" |
| **Conflict source** | Corporate vs history | Economics vs expectations | Karma vs protagonist |
| **Humor style** | Rant + sarcasm | Comparison + absurdity | Running gags + fake-outs |

**Hook Archetypes Identified:**
1. **Personal Grievance** - "I wanted X, but [entity] made it impossible"
2. **Business Mystery** - "This doesn't make economic sense, they must be up to something"
3. **Character Reveal** - "You're not prepared for how crazy this person was" + rapid-fire shocking facts
</context>

<planning_requirements>
The system must:

1. **Capture the specific style** of these business documentaries (not generic YouTube scripts)
   - The investigative "wait, that doesn't make sense" hook pattern
   - Character-building for business figures ("complete gangster", "badass")
   - The humor style (absurd comparisons, tangents that circle back)
   - Value-based conclusions that emerge naturally from the story

2. **Support two modes**:
   - **Autonomous mode**: Take research/notes → produce complete draft script
   - **Guided mode**: Walk through hook → structure → segments → ending interactively

3. **Be adaptable, not formulaic**:
   - Multiple hook archetypes (not one template)
   - Flexible segment structures
   - Varied pacing based on content
   - Different ending patterns

4. **Attempt humor** in the drafts (knowing the user will refine)
   - Learn the wit patterns from examples
   - Generate attempts at witty commentary
   - Not placeholder markers - actual attempts

5. **Integrate with existing knowledge**:
   - Reference useful concepts from script-writing-guide.md (setup-tension-payoff, retention, etc.)
   - But filter through the specific lens of this documentary style

Deliverables the plan should produce:
- `SKILL.md` for a Claude Code skill
- Core style guide document (distilled principles)
- Hook pattern library (multiple archetypes with examples)
- Structure pattern library (flexible frameworks)
- Reference breakdowns of the examples (annotated analysis)
</planning_requirements>

<analysis_instructions>
Before planning phases, deeply analyze all THREE example scripts to extract:

1. **Hook patterns used** - What makes each work? What's the formula underneath each archetype?
   - Personal Grievance (ex1): How does personal stake create investment?
   - Business Mystery (ex2): How does "impossible economics" create curiosity?
   - Character Reveal (ex3): How does rapid-fire shocking facts build anticipation?

2. **Structural patterns** - How do they organize content differently?
   - Thematic jumping (ex1) vs chronological business (ex2) vs biography timeline (ex3)
   - When does each structure work best?

3. **Segment transition techniques** - How do they move between topics?

4. **Humor patterns** - Types, triggers, and timing:
   - Rant + sarcasm (ex1)
   - Absurd comparisons (ex2): "Your local convenience store is scalping tea"
   - Running gags + fake-outs (ex3): "Medulla oblongata", "vampire hunter - no I'm just kidding"
   - Self-aware narrative commentary: "foreshadowing at its finest"

5. **Character-building techniques** - How do they make business people compelling?
   - Flaws that humanize (ex3: Sanders' anger issues, adultery)
   - Decisions that define character (ex2: Don choosing family over billions)
   - Underdog framing (ex1: Togo vs Balto)

6. **Framing devices** - Recurring narrative structures:
   - "Karma vs protagonist" (ex3)
   - "Complete gangster" characterization (all three)
   - The "badass moment" technique

7. **Moral/lesson extraction** - How do they get to the conclusion naturally?

8. **Pacing patterns** - When do they slow down vs speed up?

9. **Myth-busting/tangent handling** - How ex3 handles the racist myths section (serious but brief, returns to tone)

Use this analysis to inform the system design. The system must be able to recognize which archetype fits a given topic and adapt accordingly.
</analysis_instructions>

<output_structure>
Save to: `faceless/business-documentary-guide.md`

Structure the guide for skill consumption - it should be:
1. **Comprehensive but scannable** - Claude can find what it needs quickly
2. **Pattern-focused** - Not theory, but "here's how to do X" with examples
3. **Adaptable** - Multiple archetypes, not one rigid formula

```markdown
# Business Documentary Script-Writing Guide

> The definitive reference for writing compelling business documentary scripts in the investigative, witty style.

## Quick Reference

### When to Use Which Hook Archetype
{Decision tree or table for selecting hook type based on content}

### Core DNA (Non-Negotiable Elements)
{The 4-5 things every script MUST have}

---

## Part 1: Hook Archetypes

### Archetype 1: Personal Grievance
**Use when**: You have a personal connection or the audience can relate to being wronged
**Formula**: {Step by step}
**Example breakdown**: {From example1}
**Variations**: {How to adapt}

### Archetype 2: Business Mystery
**Use when**: The economics/business model seems impossible or counterintuitive
**Formula**: {Step by step}
**Example breakdown**: {From example2}
**Variations**: {How to adapt}

### Archetype 3: Character Reveal
**Use when**: The subject is a person with a wild/unknown backstory
**Formula**: {Step by step}
**Example breakdown**: {From example3}
**Variations**: {How to adapt}

---

## Part 2: Structure Patterns

### Pattern A: Thematic Investigation
**Best for**: Corporate/systemic stories
**Flow**: {How segments connect}

### Pattern B: Chronological Business Journey
**Best for**: Company origin stories
**Flow**: {How segments connect}

### Pattern C: Biography Timeline
**Best for**: Founder/figure profiles
**Flow**: {How segments connect}

---

## Part 3: Humor & Voice

### Humor Types (with examples)
{Each type with 2-3 examples pulled from scripts}

### Voice Patterns
{Specific phrases, cadences, techniques}

### When to Get Serious
{How to handle sensitive topics - see example3 myth-busting}

---

## Part 4: Character Building

### Making Business People Compelling
{Techniques with examples}

### The "Complete Gangster" Characterization
{How and when to use it}

### Showing Flaws That Humanize
{Examples from all 3 scripts}

---

## Part 5: Conclusions & Morals

### Extracting the Lesson Naturally
{How each example does it}

### Ending Patterns
{Different ways to close}

---

## Part 6: Segment Transitions

### Transition Techniques
{With examples}

### Pacing Guidelines
{When to speed up/slow down}

---

## Appendix: Example Breakdowns

### Example 1 (Togo/Disney) - Annotated
{Key moments with commentary}

### Example 2 (Arizona Tea) - Annotated
{Key moments with commentary}

### Example 3 (Colonel Sanders) - Annotated
{Key moments with commentary}
```
</output_structure>

<summary_requirements>
Create `.prompts/001-faceless-documentary-system-plan/SUMMARY.md`

Include:
- **One-liner**: What was produced
- **Key Patterns Extracted**: 3-5 most important discoveries from analysis
- **Guide Structure**: Overview of sections created
- **Next Step**: Create skill using `/create-agent-skill` that references this guide
</summary_requirements>

<success_criteria>
- Deep analysis of all 3 example scripts completed (not surface-level)
- Patterns are specific and actionable (not vague principles)
- Each hook archetype has clear "use when" + formula + example
- Humor patterns captured with actual examples from scripts
- Guide is structured for Claude to quickly find relevant sections
- Adaptability built in (multiple archetypes, not one formula)
- Guide saved to `faceless/business-documentary-guide.md`
- SUMMARY.md confirms guide is ready for skill creation
</success_criteria>
