# Workflow: Audit Existing Extensions

<required_reading>
**Read these reference files NOW before auditing:**
1. references/decision-framework.md
2. references/component-boundaries.md (especially keep_together_tests and balanced_decision sections)
</required_reading>

<process>

## Step 1: Receive Extension to Audit

Ask user to identify what they want audited.

**Accept:**
- File paths to skill, subagent, or command files
- Folder paths to extension directories
- Names of extensions to locate
- Multiple extensions to compare

**Say:** "What extension(s) do you want me to audit? Provide file paths, folder paths, or names and I'll locate them."

Read ALL provided extension files before proceeding to analysis.

---

## Step 2: Understand Current Structure

For each extension, document:

1. **Type:** What is it currently? (skill / subagent / command / claude.md)
2. **Scope:** What does it cover? List all capabilities/sections
3. **Purpose:** What problem does it solve?
4. **Usage pattern:** How is it typically invoked?

Create a summary table:

| Extension | Current Type | Capabilities Covered | Stated Purpose |
|-----------|--------------|---------------------|----------------|
| ... | ... | ... | ... |

---

## Step 3: Apply "Is This the Right Type?" Test

For each extension, re-run the primary decision flow:

**Question 1: Is this actually just a shortcut?**
- Does it have real methodology, or is it just triggering an action?
- If no methodology → should be **Command**, not Skill

**Question 2: Does it actually need isolation?**
- Does it need a different persona?
- Does it need to run without user interaction?
- If no → might be **Skill**, not Subagent

**Question 3: Does it actually teach methodology?**
- Is there a right/wrong way, or just steps?
- Does it require expertise, or just execution?
- If just steps → might be **Command**, not Skill

**Flag mismatches:** Note where current type doesn't match what the content suggests.

---

## Step 4: Apply Balanced Boundary Tests

For each extension, apply BOTH splitting AND keep-together tests:

### Splitting Tests (reasons to break apart)

| Test | Question | Result |
|------|----------|--------|
| Boundary | Can section A complete without section B? | |
| Naming | Can name without "and"? | |
| Context | Would someone need JUST this part? | |
| Expertise | Different expertise for each section? | |

**Splitting score:** Count YES responses (for Boundary, Context, Expertise) and NO responses (for Naming)

### Keep-Together Tests (reasons to keep as one)

| Test | Question | Result |
|------|----------|--------|
| Integration | Does A without B produce nothing useful? | |
| Overhead | Would splitting create painful coordination friction? | |
| Context Dependency | Does each part need the other's context to function? | |
| Workflow | Would users ALWAYS invoke these together, never separately? | |

**Keep-together score:** Count YES responses

### Decision Matrix

| Splitting Score | Keep-Together Score | Recommendation |
|-----------------|---------------------|----------------|
| 0-1 | Any | KEEP AS IS |
| 2+ | 0-1 | SPLIT |
| 2+ | 2+ | CONFLICT - investigate further |

---

## Step 5: Investigate Conflicts

If both scores are 2+, dig deeper:

1. **Weight by severity** - Which signals are strongest?
2. **Consider user intent** - Are they building tools for themselves or autonomous agents?
3. **Prototype test** - If split, would the user invoke them separately? How often?
4. **Default to fewer** - When truly ambiguous, recommend keeping together

Ask clarifying questions using workflows/clarify-ambiguity.md if needed.

---

## Step 6: Generate Audit Report

Present findings in this format:

### Extension: [name]

**Current state:**
- Type: [current type]
- Scope: [what it covers]

**Type assessment:**
- Current type appropriate: YES / NO
- If NO, should be: [recommended type]
- Rationale: [why]

**Boundary assessment:**
- Splitting score: X/4
- Keep-together score: X/4
- Recommendation: KEEP AS IS / SPLIT / INVESTIGATE

**If SPLIT recommended:**
- Proposed components:
  1. [name] - [type] - [what it covers]
  2. [name] - [type] - [what it covers]
- Migration path: [how to transition]

**If KEEP AS IS:**
- Confirmation: [why current structure is correct]
- Optional improvements: [any refinements within current structure]

---

## Step 7: Offer Next Steps

After presenting audit results:

1. **Accept recommendations** - Proceed with restructuring using appropriate create-* skills
2. **Challenge findings** - Discuss specific recommendations you disagree with
3. **Audit another** - Evaluate a different extension
4. **See test details** - Walk through specific tests in more depth

**Wait for user choice before taking action.**

</process>

<success_criteria>
Audit is complete when:
- [ ] All specified extensions have been read
- [ ] Type appropriateness evaluated for each
- [ ] Both splitting AND keep-together tests applied
- [ ] Conflicts investigated and resolved
- [ ] Clear recommendation provided (keep / split / change type)
- [ ] User has actionable next steps
</success_criteria>

<anti_patterns>
Avoid these audit mistakes:

**Split-happy:** Don't recommend splitting just because you CAN split. The keep-together tests exist to prevent unnecessary fragmentation.

**Type-forcing:** Don't recommend changing type unless there's a clear mismatch. "Could be a subagent" is not the same as "should be a subagent."

**Ignoring usage:** Consider how the extension is actually used, not just how it's structured. A slightly messy structure that works well in practice may be better than a "clean" restructure that adds friction.

**Premature optimization:** Don't recommend restructuring for extensions that work fine. "Could be better" is not sufficient justification - there should be a real problem to solve.
</anti_patterns>
