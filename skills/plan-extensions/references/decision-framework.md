# Decision Framework Reference

Deep reference for the capability decision framework. Read this when analyzing documentation or concepts.

---

<user_intent>

## Start with Intent

Before applying the decision cascade, understand what the user wants to achieve. This shapes all recommendations.

### The Intent Question

**"What are you trying to build?"**

| Intent | Description | Component Bias |
|--------|-------------|----------------|
| **Equip yourself** | Tools that make YOU better at doing the work | Favor skills (interactive, teaches methodology) |
| **Delegate to agent** | Autonomous worker that does work and returns results | Favor subagents (isolated, hands-off) |
| **Hybrid** | Agent does work using your methodologies | Subagents that invoke skills |

### How Intent Changes Recommendations

**Same input, different intent:**

Example: "I have documentation on how to write great YouTube scripts"

| Intent | Recommendation | Rationale |
|--------|----------------|-----------|
| Equip yourself | Skill: youtube-scripting | You want to learn the methodology, stay involved in writing |
| Delegate to agent | Subagent: script-writer | You want to hand off a topic, get a script back |
| Hybrid | Both: skill + subagent | Agent writes scripts using your methodology skill |

### When Intent is Unclear

If user picks "not sure yet":

1. Ask about their typical workflow - do they want to be involved or get results?
2. Ask about learning goals - do they want to internalize the expertise?
3. Ask about volume - one-off deep work or repeated delegation?

High involvement + learning + one-off → Equip yourself
Low involvement + no learning + repeated → Delegate
Mix → Hybrid

</user_intent>

---

<decision_cascade>

## The Primary Decision Flow

Ask these questions in order. Stop at the first "yes."

### Question 1: Is this a shortcut to something asked repeatedly?

**Indicators of YES:**
- User says "I always do X" or "every time I need to Y"
- Same prompt used repeatedly with minor variations
- No contextual variation in how it's done
- No methodology involved - just triggering an action
- Could be replaced with a button

**Examples that ARE shortcuts (→ Command):**
- `/commit` - Create a git commit with context
- `/optimize [file]` - Analyze file for performance
- `/review-pr [number]` - Review a specific PR
- `/check-todos` - Show outstanding todos
- `/first-principles` - Apply a thinking framework

**Examples that are NOT shortcuts:**
- How to write good commits (methodology) → Skill
- When to optimize vs refactor (expertise) → Skill
- PR review with specific persona → Subagent

**Test:** "Would a simple 'do X now' button work?" If yes → Command.

---

### Question 2: Does this need a different persona or isolated context?

**Indicators of YES:**
- Needs to think as a different "person" (critic, security expert, etc.)
- Should NOT interact with user during execution
- Needs limited tool access for safety
- Returns a report/artifact after autonomous work
- Context would pollute main conversation

**Examples that need isolation (→ Subagent):**
- Security auditor - Reviews code, returns vulnerability report
- Harsh critic - Evaluates ideas without user pushback
- Documentation generator - Researches API, returns complete docs
- Test writer - Analyzes code, generates comprehensive tests
- Code reviewer - Reviews changes, returns structured feedback

**Examples that DON'T need isolation:**
- Security guidance you apply yourself → Skill
- Critique with back-and-forth discussion → Skill
- Writing docs iteratively with user → Skill

**Test:** "Should this run autonomously and return a result without asking me questions?" If yes → Subagent.

---

### Question 3: Does this teach HOW to do something with real methodology?

**Indicators of YES:**
- Has a "right way" and "wrong way" to do it
- Requires domain expertise to do well
- A junior would need training to do this correctly
- Multiple workflows for the same domain
- Reusable across projects

**Examples that teach methodology (→ Skill):**
- Create React components (patterns, hooks, testing approaches)
- Design database schemas (normalization, indices, constraints)
- Write Claude skills (structure, principles, validation)
- Debug complex issues (systematic investigation)
- Plan software projects (briefs, roadmaps, phases)

**Examples that DON'T teach methodology:**
- List of React component names → claude.md
- Database connection string → claude.md
- One specific debugging session → Just do it
- Single project plan → Project docs

**Test:** "Could this be taught as a workshop or course module?" If yes → Skill.

---

### Question 4: None of the above?

If it's not a shortcut, doesn't need isolation, and doesn't teach methodology:

**Where it goes:**
- Project-specific reference info → `.claude/CLAUDE.md` or README
- Personal preferences → `~/.claude/CLAUDE.md`
- One-time instructions → Just tell Claude directly
- Static reference (API keys, paths, conventions) → claude.md

</decision_cascade>

---

<common_mistakes>

## What's NOT a Skill (Common Mistakes)

### Mistake 1: Simple checklists

"Deploy checklist: 1. Run tests, 2. Build, 3. Deploy, 4. Verify"

This is a Command, not a Skill. No methodology, just steps.

### Mistake 2: One-time project instructions

"For this project, always use TypeScript strict mode"

This goes in claude.md or project README. Not reusable.

### Mistake 3: Static reference info

"Our API base URL is https://api.example.com"

This is claude.md content. No expertise needed.

### Mistake 4: Just a trigger

"When I say 'analyze', run security checks"

This is a Command. No teaching, just triggering.

### Mistake 5: Isolated task with no reuse

"Help me debug this specific error"

Don't create anything. Just do it. Only create capabilities for reusable patterns.

</common_mistakes>

---

<edge_cases>

## Edge Cases and Resolution

### Edge Case 1: Could be Skill OR Command

**Situation:** "Create a code review process"

**Resolution questions:**
- Is there ONE way to do it, or does it require judgment? → Judgment = Skill
- Will the approach vary by context? → Varies = Skill
- Is it just triggering a pre-defined review? → Pre-defined = Command

**Likely answer:** Skill (review requires expertise), but could also have a `/review` command that invokes a code-reviewer subagent.

---

### Edge Case 2: Could be Skill OR Subagent

**Situation:** "Security analysis capability"

**Resolution questions:**
- Do you need to interact during analysis? → Interactive = Skill
- Should it just return findings? → Report = Subagent
- Do you want to learn security patterns? → Learning = Skill

**Common pattern:** Both. Skill teaches security methodology, Subagent runs automated analysis.

---

### Edge Case 3: Could be Command OR Subagent

**Situation:** "PR review automation"

**Resolution questions:**
- Is this a quick trigger or deep analysis? → Deep = Subagent
- Do you need specific persona/focus? → Persona = Subagent
- Is it just "review this PR now"? → Trigger = Command invoking Subagent

**Common pattern:** Command that invokes Subagent. `/review-pr 123` triggers security-reviewer subagent.

---

### Edge Case 4: Multiple things combined

**Situation:** "YouTube content creation workflow"

**Resolution:** Apply BOTH splitting AND keep-together tests (see component-boundaries.md):

**Step 1: Apply splitting tests**
- Ideation (different expertise) → Maybe split
- Scripting (different expertise) → Maybe split
- Packaging (different expertise) → Maybe split

**Step 2: Apply keep-together tests**
- Integration: Does ideation alone produce value? → YES (validated ideas are useful)
- Overhead: Would splitting create friction? → NO (clean handoffs)
- Context dependency: Need each other's context? → NO (minimal)
- Workflow: Always used together? → NO (often just need one part)

**Step 3: Apply decision matrix**
- Splitting score: 3+ (different expertise, can complete separately, would need just one)
- Keep-together score: 0 (all tests say split is fine)
- Decision: SPLIT

**Result:**
- Ideation → Skill
- Scripting → Skill
- Packaging → Skill
- Harsh critic (different persona) → Subagent
- Publish checklist (just steps) → Command

---

### Edge Case 5: Audit says split, but feels wrong

**Situation:** Tests suggest splitting, but something feels off

**Resolution questions:**
1. Would users actually invoke these separately? (If rarely → keep together)
2. Does splitting create more overhead than value? (If yes → keep together)
3. Is the "split" creating micro-components that don't stand alone? (If yes → keep together)

**Remember:** The balanced decision framework defaults to fewer components when truly ambiguous. Don't split just because you can.

</edge_cases>

---

<capability_characteristics>

## Capability Type Characteristics

### Skills

**What they are:** Domain expertise with methodology
**When loaded:** On invocation, entire SKILL.md + selected workflows
**User interaction:** Full - can ask questions, wait for answers
**Tool access:** All tools available
**Context:** Runs in main conversation
**Typical size:** 100-500 lines, can grow with references

### Subagents

**What they are:** Specialized autonomous workers
**When loaded:** On Task tool invocation
**User interaction:** None - black box, returns result only
**Tool access:** Configurable, should be restricted
**Context:** Isolated, doesn't pollute main conversation
**Typical size:** 50-200 lines

### Commands

**What they are:** Prompt shortcuts
**When loaded:** On /command invocation, expands in place
**User interaction:** Full - runs in main conversation
**Tool access:** Configurable via allowed-tools
**Context:** Runs in main conversation
**Typical size:** 20-100 lines

### claude.md

**What it is:** Background context always loaded
**When loaded:** Always, at conversation start
**User interaction:** N/A - just reference info
**Tool access:** N/A
**Context:** Informs all conversations
**Typical size:** 50-300 lines recommended

</capability_characteristics>
