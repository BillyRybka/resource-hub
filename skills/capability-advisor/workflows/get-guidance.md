# Workflow: Get Guidance

Explain the decision framework before asking for input.

<required_reading>
Read references/decision-framework.md for the full framework details.
</required_reading>

<process>

## Step 1: Explain the Framework

Present the decision framework clearly:

---

**Here's how I decide what to recommend:**

### The Four Capability Types

| Type | What It Is | Use When |
|------|------------|----------|
| **Skill** | Domain expertise with methodology | You need Claude to know HOW to do something correctly |
| **Subagent** | Autonomous specialist | You need a different persona or isolated analysis |
| **Command** | Prompt shortcut | You trigger the same action repeatedly |
| **claude.md** | Background reference | You need info always available |

### The Primary Decision Flow

I ask these questions in order and stop at the first "yes":

1. **Is it a shortcut?** Same action triggered repeatedly, no methodology?
   → **Command** (like a button)

2. **Does it need isolation?** Different persona, no user interaction, returns a report?
   → **Subagent** (like delegating to a specialist)

3. **Does it teach methodology?** Right/wrong way, requires expertise, trainable?
   → **Skill** (like domain knowledge)

4. **None of the above?**
   → **claude.md** (just reference info)

### The Splitting Tests

When something seems like "one big thing," I apply four tests:

| Test | Question |
|------|----------|
| **Boundary** | Can I finish section A without needing section B? |
| **Naming** | Can I name it without using "and"? |
| **Context** | Would someone ever need JUST this part? |
| **Expertise** | Does each section need different expertise? |

If 2+ tests suggest splitting → I recommend multiple components.

### What I Output

For every recommendation, I provide:
- **Type** - skill, subagent, command, or claude.md
- **Count** - how many of each
- **Names** - suggested names for each
- **Descriptions** - what each does
- **Rationale** - which test/principle led to this decision
- **Build order** - what to create first

---

## Step 2: Ask What They Have

After explaining, ask:

"Now, what would you like me to analyze?

1. **I have documentation/specs** - Files, notes, or written materials to review
2. **I want to describe a concept** - I'll explain what I need
3. **I have a specific question** - About the framework itself"

**Wait for response and route:**
- Documentation → workflows/analyze-documentation.md
- Concept → workflows/analyze-concept.md
- Question → Answer the question, then re-ask what they want to analyze

</process>

<success_criteria>
Guidance is complete when:
- [ ] Framework explained clearly
- [ ] User understands the four types
- [ ] User understands the decision flow
- [ ] User understands splitting tests
- [ ] User ready to share input for analysis
</success_criteria>
