---
name: plan-extensions
description: Analyzes documentation or concepts and recommends what Claude Code extensions to build (skills, subagents, commands, claude.md). Use when planning what extensions you need before invoking create-* skills.
---

<essential_principles>

<principle name="user_intent">
Before recommending components, understand what the user wants to achieve:

| Intent | Description | Implications |
|--------|-------------|--------------|
| **Equip yourself** | Tools that make YOU better at doing the work | Favor skills (teach methodology), user stays in the loop, interactive |
| **Delegate to agent** | Autonomous worker that does the work and returns results | Favor subagents (isolated execution), minimal user interaction |
| **Hybrid** | Agent does work but uses your methodology | Subagent + skills (agent invokes skills you've defined) |

This intent shapes every recommendation. Same documentation could become:
- A skill (user learns, stays involved)
- A subagent (user delegates, gets results)
- Both (agent uses skill for quality)
</principle>

<principle name="capability_types">
Claude Code has four capability types:

| Type | Purpose | One-Line Definition |
|------|---------|---------------------|
| **Skill** | Domain expertise with methodology | Teaches Claude HOW to do something |
| **Subagent** | Specialized autonomous worker | A team member with a persona, runs isolated |
| **Command** | Prompt shortcut | A trigger button for repeated actions |
| **claude.md** | Background context | Reference info always available |
</principle>

<principle name="primary_decision_flow">
Ask these questions in order. Stop at the first "yes."

1. **Is this a shortcut to something asked repeatedly?**
   - Same prompt used over and over
   - No methodology, just triggering an action
   → **YES = Command**

2. **Does this need a different persona or isolated context?**
   - Should think as a different "person" (critic, security expert)
   - Should NOT interact with user during execution
   - Returns a report/artifact autonomously
   → **YES = Subagent**

3. **Does this teach HOW to do something with real methodology?**
   - Has a "right way" and "wrong way"
   - Requires domain expertise
   - A junior would need training
   → **YES = Skill**

4. **None of the above?**
   → Put in **claude.md** or project documentation
</principle>

<principle name="one_vs_many_tests">
When something seems like "one big thing," apply these tests:

**Boundary Test:** "Can I complete section A's job without needing section B?"
**Naming Test:** "Can I name it without using 'and'?"
**Context Test:** "Would someone ever need JUST this part?"
**Expertise Test:** "Does each section require a DIFFERENT type of expertise?"

If 2+ tests suggest splitting → split into multiple components.
</principle>

<principle name="not_a_skill">
These are NOT skills (common mistakes):

| This | Is Actually |
|------|-------------|
| Simple checklists | Command |
| One-time project instructions | Project docs |
| Static reference info | claude.md |
| Just a trigger for a process | Command |
| Isolated task with no reuse | Just do it, don't create anything |
</principle>

<principle name="quantify_recommendations">
Always output:
- **What TYPE** of component (skill, subagent, command, claude.md)
- **HOW MANY** of each type
- **NAME** for each component
- **BRIEF description** of each
- **RATIONALE** for each decision (which test/principle applied)

Use templates/recommendation-output.md format.
</principle>

</essential_principles>

<intake>
**First, what's your goal?**

A. **Equip yourself** - Build tools that make YOU better at doing the work (you stay in the loop)
B. **Delegate to an agent** - Build an autonomous worker that does the work and comes back with results
C. **Hybrid** - Agent does the work but uses methodologies/skills you've defined
D. **Not sure yet** - Help me figure it out

**Wait for response, then ask:**

What do you have to share?

1. **Documentation** - I have docs, notes, specs, or files to analyze
2. **Concept explanation** - I want to describe what I need
3. **Both** - I have docs and want to add context
4. **Audit existing** - I have existing extensions I want to evaluate/restructure
5. **Get guidance** - Explain the decision framework first

**Wait for response before proceeding.**
</intake>

<routing>
| Response | Workflow |
|----------|----------|
| 1, "documentation", "docs", "specs", "files" | workflows/analyze-documentation.md |
| 2, "concept", "describe", "explain", "idea" | workflows/analyze-concept.md |
| 3, "both" | Start with workflows/analyze-documentation.md, then ask for additions |
| 4, "audit", "existing", "evaluate", "restructure" | workflows/audit-existing.md |
| 5, "guidance", "help", "framework", "explain" | workflows/get-guidance.md |

**After reading the workflow, follow it exactly.**
</routing>

<reference_index>
All in `references/`:

| Reference | Purpose |
|-----------|---------|
| decision-framework.md | Deep dive on when to use what, edge cases, examples |
| component-boundaries.md | How to split one vs many, counting rules |
</reference_index>

<workflows_index>
All in `workflows/`:

| Workflow | Purpose |
|----------|---------|
| analyze-documentation.md | Analyze provided docs/specs systematically |
| analyze-concept.md | Guided discovery when describing a concept |
| audit-existing.md | Evaluate existing extensions for restructuring |
| clarify-ambiguity.md | Structured questions for unclear cases |
| get-guidance.md | Explain the framework before asking for input |
</workflows_index>

<templates_index>
All in `templates/`:

| Template | Purpose |
|----------|---------|
| recommendation-output.md | Consistent format for presenting recommendations |
</templates_index>

<success_criteria>
Capability analysis is complete when:
- [ ] All input has been received and read
- [ ] Each capability is categorized (skill/subagent/command/claude.md)
- [ ] Multi-part items tested for splitting (4 tests applied)
- [ ] Ambiguities resolved through clarification
- [ ] Quantified recommendation produced (type + count + names + rationale)
- [ ] Output uses templates/recommendation-output.md format
- [ ] User has actionable next steps
</success_criteria>
