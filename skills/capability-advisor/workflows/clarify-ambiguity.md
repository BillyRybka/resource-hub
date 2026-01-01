# Workflow: Clarify Ambiguity

Use these structured clarification patterns when ambiguity is detected during analysis.

<process>

## When to Use This Workflow

Route here from analyze-documentation.md or analyze-concept.md when:
- Purpose of a section is unclear
- Scope boundaries are ambiguous
- Reuse frequency is unknown
- Overlap between sections is uncertain

---

## Pattern 1: Purpose Unclear

**When to use:** Can't determine if something is a trigger, methodology, reference, or isolated task.

**Ask using AskUserQuestion:**

"I see [component name] but I'm not sure of its purpose. Which best describes it?"

| Option | Description |
|--------|-------------|
| **Trigger for repeated action** | "Run this when I say X" - same every time |
| **Methodology/expertise** | "How to do this correctly" - requires judgment |
| **Reference information** | "Just need this info available" - look up as needed |
| **Isolated analysis** | "Analyze and report back" - autonomous work |

**Mapping:**
- Trigger → Command
- Methodology → Skill
- Reference → claude.md
- Isolated analysis → Subagent

---

## Pattern 2: Scope Unclear

**When to use:** Something could be one unified thing or multiple separate things.

**Ask using AskUserQuestion:**

"[Component name] could be structured different ways. Which matches your intent?"

| Option | Description |
|--------|-------------|
| **One unified thing** | Always used together, inseparable |
| **Two separate things** | [A] and [B] could be used independently |
| **Layered** | [Base] that [Extension] builds on |
| **Actually multiple** | More than two distinct things here |

**Follow-up if "Two separate" or "Layered" or "Multiple":**
Ask user to name or describe each part. Re-analyze each independently.

---

## Pattern 3: Reuse Unclear

**When to use:** Don't know if this is one-time, project-specific, or universal.

**Ask using AskUserQuestion:**

"How often and where will this be used?"

| Option | Description |
|--------|-------------|
| **Once** | Just this project, this time - then done |
| **This project only** | Repeatedly, but specific to this project |
| **All my projects** | Want this everywhere I work |
| **Shareable** | Others should have this too |

**Mapping:**
- Once → Don't create a capability; just do it
- This project → .claude/ directory (project-level)
- All projects → ~/.claude/ directory (user-level)
- Shareable → Consider plugin/repo distribution

---

## Pattern 4: Expertise Overlap

**When to use:** Two things seem related but unsure if they're same skill or different skills.

**Ask using AskUserQuestion:**

"[A] and [B] seem related. Are they:"

| Option | Description |
|--------|-------------|
| **Same expertise, different actions** | One skill with multiple workflows |
| **Different expertise, related topic** | Multiple skills that work together |
| **Actually the same thing** | Consolidate into one |
| **Unrelated** | I was wrong to group them |

**Mapping:**
- Same expertise, different actions → One skill with workflows/ directory
- Different expertise → Multiple separate skills
- Same thing → One skill
- Unrelated → Analyze separately

---

## Pattern 5: Interaction Model Unclear

**When to use:** Unsure if user wants to be involved during execution.

**Ask using AskUserQuestion:**

"During [task], should Claude:"

| Option | Description |
|--------|-------------|
| **Ask questions along the way** | Interactive, guided process |
| **Work autonomously** | Do it all, just give me the result |
| **Quick check-ins only** | Mostly autonomous, occasional confirmation |
| **Depends on the situation** | Sometimes interactive, sometimes not |

**Mapping:**
- Ask questions → Skill (can use AskUserQuestion)
- Work autonomously → Subagent (no user interaction)
- Quick check-ins → Skill with optional prompts
- Depends → Consider both: Skill for interactive, Subagent for autonomous

---

## Pattern 6: Output Type Unclear

**When to use:** Don't know what the deliverable should be.

**Ask using AskUserQuestion:**

"What should the output of [task] be?"

| Option | Description |
|--------|-------------|
| **A report/analysis** | Structured findings to review |
| **Code/files** | Generated artifacts to use |
| **Guidance/advice** | Recommendations to follow |
| **Just do the thing** | No separate output, just complete the task |

**Implications:**
- Report/analysis → Often subagent (returns structured output)
- Code/files → Could be skill or subagent depending on interaction
- Guidance → Usually skill (expertise-based)
- Just do it → Command (trigger action) or skill (if complex)

---

## After Clarification

1. Return to the calling workflow (analyze-documentation or analyze-concept)
2. Apply the clarified understanding to the decision framework
3. Continue with recommendation generation

</process>

<success_criteria>
Clarification is complete when:
- [ ] Specific ambiguity identified
- [ ] Appropriate pattern selected
- [ ] User provided clear answer via AskUserQuestion
- [ ] Answer mapped to component type
- [ ] Ready to return to main workflow
</success_criteria>
