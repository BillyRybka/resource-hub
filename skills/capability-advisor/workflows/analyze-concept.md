# Workflow: Analyze Concept

<required_reading>
**Read these reference files NOW before analyzing:**
1. references/decision-framework.md
2. references/component-boundaries.md
</required_reading>

<process>

## Step 1: Initial Description

If user hasn't already described their concept, ask:

"Describe what you want Claude to be able to do. Include as much detail as helpful - what triggers it, what it produces, who uses it."

**Listen for:**
- **Actions (verbs)** - What Claude should DO
- **Context (when)** - When this gets triggered
- **Inputs (what)** - What Claude receives to work with
- **Outputs (artifacts)** - What Claude produces
- **Frequency** - How often this happens

---

## Step 2: Structured Discovery Questions

Based on initial description, ask targeted questions using AskUserQuestion.

**Only ask questions where the answer is genuinely unclear.** Skip questions the user already answered.

<question_bank>

### Scope Questions

"How often will this be used?"
1. **Once or rarely** - Specific to this situation
2. **This project only** - Repeatedly, but project-specific
3. **All my projects** - Want this everywhere I work
4. **Shareable** - Others should have this too

"Who else might use this?"
1. **Just me** - Personal workflow
2. **My team** - Shared within project
3. **Anyone** - General utility

### Complexity Questions

"Walk me through what happens. What's the first step? Then what?"

"Are there decisions along the way, or is it always the same process?"
1. **Always the same** - Deterministic steps
2. **Depends on context** - Judgment calls needed
3. **Multiple paths** - Different approaches for different cases

### Boundary Questions

"You mentioned [X] and [Y]. Could someone need just [X] without [Y]?"
1. **Yes, often** - They're independent
2. **Sometimes** - Usually together, occasionally separate
3. **No, always together** - One can't work without the other

"Does [X] require different expertise than [Y]?"
1. **Yes, very different** - Different mental models
2. **Somewhat different** - Related but distinct
3. **Same expertise** - One skill set covers both

### Interaction Questions

"During this task, should Claude ask you questions or just work autonomously?"
1. **Ask questions** - Want to guide the process
2. **Work autonomously** - Just give me the result
3. **Depends** - Sometimes one, sometimes the other

"Do you want to see Claude's thinking, or just the final output?"
1. **See everything** - Want visibility into process
2. **Just the result** - Don't need to see the work
3. **Summary + result** - High-level progress, then output

### Existing Context Questions

"Is there already something similar you want to build on?"
1. **Yes** - [Ask what]
2. **No** - Starting fresh
3. **Not sure** - Might overlap with something

</question_bank>

**Ask 2-4 questions maximum.** Focus on genuine gaps, not comprehensive coverage.

---

## Step 3: Apply Decision Framework

After gathering enough context, apply:

**Primary Decision Flow:**
1. Is it a shortcut to a repeated action? → Command
2. Does it need a different persona or isolation? → Subagent
3. Does it teach methodology with expertise? → Skill
4. None of above? → claude.md

**Splitting Tests (if something seems too big):**
- Boundary: Can complete A without B?
- Naming: Can name without "and"?
- Context: Would someone need just this part?
- Expertise: Different expertise required?

---

## Step 4: Validate Understanding

Before producing recommendations, confirm understanding:

"Let me confirm I understand correctly:

**What this is for:** [summary]
**How often it's used:** [frequency]
**What it produces:** [outputs]
**Key constraints:** [any mentioned limitations]

Is this accurate, or should I adjust?"

**Wait for user confirmation or corrections.**

---

## Step 5: Generate Recommendation

Read templates/recommendation-output.md and use that exact format.

For each component, include:
- **Type:** skill / subagent / command / claude.md
- **Name:** Suggested name (lowercase-with-hyphens)
- **Description:** 1-2 sentences
- **Rationale:** Which decision/test led here
- **Complexity:** Simple or complex (for skills)

Include dependencies, build order, and next steps.

---

## Step 6: Offer Next Steps

1. **Proceed with building** - Start with first component
2. **Adjust recommendations** - Modify based on feedback
3. **Get more details** - Explain specific recommendation
4. **Ask more questions** - I want to clarify further

**Wait for user choice.**

</process>

<success_criteria>
Concept analysis is complete when:
- [ ] User's intent is fully understood
- [ ] Frequency and scope are clear
- [ ] Components are categorized
- [ ] Splitting tests applied where relevant
- [ ] User confirms understanding is accurate
- [ ] Quantified recommendation produced using template
- [ ] User has clear next steps
</success_criteria>
