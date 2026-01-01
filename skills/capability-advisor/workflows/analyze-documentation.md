# Workflow: Analyze Documentation

<required_reading>
**Read these reference files NOW before analyzing:**
1. references/decision-framework.md
2. references/component-boundaries.md
</required_reading>

<process>

## Step 1: Receive Documentation

Ask user to share documentation if not already provided.

**Accept:**
- File paths (use Read tool to access)
- Pasted content in the message
- URLs (use WebFetch to retrieve)
- Multiple sources combined

**Say:** "Share your documentation. You can provide file paths, paste content directly, or share URLs."

Read ALL provided content before proceeding to analysis.

---

## Step 2: Extract Capabilities

From the documentation, identify:

1. **Distinct capabilities** - What separate things does this describe?
2. **Boundaries** - Where does one capability end and another begin?
3. **Types of content:**
   - Procedures (how-to) → Potential skills or commands
   - Reference info (what-is) → Potential claude.md
   - Analysis tasks → Potential subagents
   - Repeated actions → Potential commands

Create a working list of identified capabilities.

---

## Step 3: Apply Primary Decision Flow

For EACH identified capability, ask these questions in order:

**Question 1: Is this a shortcut?**
- Same prompt used repeatedly?
- No methodology, just triggering?
→ If YES: Mark as **Command**

**Question 2: Does it need isolation?**
- Different persona needed?
- Should run without user interaction?
- Returns a report/artifact?
→ If YES: Mark as **Subagent**

**Question 3: Does it teach methodology?**
- Has right/wrong way to do it?
- Requires expertise?
- Trainable skill?
→ If YES: Mark as **Skill**

**Question 4: None of above?**
→ Mark as **claude.md** or project docs

---

## Step 4: Apply Splitting Tests

For anything that seems like "one big thing," apply ALL FOUR tests:

| Test | Question | Split if... |
|------|----------|-------------|
| Boundary | Can section A complete without section B? | YES |
| Naming | Can name without "and"? | NO (needs "and") |
| Context | Would someone need JUST this part? | YES |
| Expertise | Different expertise for each section? | YES |

**If 2+ tests suggest splitting:** Break into multiple components and re-apply Step 3 to each.

---

## Step 5: Check for Ambiguity

Route to workflows/clarify-ambiguity.md if any of these are unclear:

- Purpose of a section (trigger vs methodology vs reference)
- Whether something is reused or one-time
- Scope boundaries (where one thing ends, another begins)
- Level of isolation needed

Use AskUserQuestion with specific options from the clarification workflow.

---

## Step 6: Generate Recommendation

Read templates/recommendation-output.md and use that exact format.

For each component, include:
- **Type:** skill / subagent / command / claude.md
- **Name:** Suggested name (lowercase-with-hyphens)
- **Description:** 1-2 sentences, what it does and when to use it
- **Rationale:** Which decision/test led to this classification
- **Complexity:** Simple or complex (for skills)

Include:
- Dependencies between components
- Suggested build order
- Next steps options

---

## Step 7: Offer Next Steps

After presenting recommendations:

1. **Proceed with building** - Start with first component using appropriate create-* skill
2. **Adjust recommendations** - Modify scope, split/combine, change types
3. **Get more details** - Deep dive on specific recommendation
4. **See decision rationale** - Explain the reasoning in more depth

**Wait for user choice before taking action.**

</process>

<success_criteria>
Documentation analysis is complete when:
- [ ] All documentation has been read
- [ ] Each capability is categorized (skill/subagent/command/claude.md)
- [ ] Multi-part items tested with all 4 splitting tests
- [ ] Ambiguities resolved through clarification
- [ ] Quantified recommendation produced using template format
- [ ] User has clear next steps
</success_criteria>
