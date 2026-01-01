# Component Boundaries Reference

Guidelines for determining when to split into multiple components vs keep as one.

---

<splitting_tests>

## The Four Splitting Tests

When something seems like "one big thing," apply these tests. If 2+ suggest splitting, split.

### 1. Boundary Test

**Question:** "Can I complete section A's job without needing section B?"

**How to apply:**
- List the major sections/phases of the workflow
- For each pair of adjacent sections, ask if A can be "done" independently
- If yes, they can be separate components

**Example: YouTube workflow**
| Section A | Section B | Can A complete without B? |
|-----------|-----------|---------------------------|
| Ideation | Scripting | YES - ideas can be validated before scripting |
| Scripting | Production | YES - script is complete before filming |
| Production | Editing | NO - raw footage needs editing |
| Editing | Publishing | YES - edited video is complete |

**Result:** Ideation, Scripting could be separate. Production+Editing might stay together.

---

### 2. Naming Test

**Question:** "Can I name it without using 'and'?"

**How to apply:**
- Try to name the capability
- If you need "and" or "or" to describe it, it's probably multiple things

**Examples:**
| Attempted Name | Analysis |
|----------------|----------|
| "user-management" | Clean - one skill |
| "user-and-notification-system" | Split into two |
| "youtube-ideation" | Clean - one skill |
| "ideation-and-scripting" | Split into two |
| "api-client" | Clean - one skill |
| "api-client-with-error-handling" | Keep together (error handling is part of client) |

**Nuance:** "with" is different from "and." X-with-Y often means Y is part of X. X-and-Y means two things.

---

### 3. Context Test

**Question:** "Would someone ever need JUST this part?"

**How to apply:**
- Imagine different users/scenarios
- Would anyone invoke just section A without section B?

**Example: YouTube workflow**
| Section | Would someone need JUST this? |
|---------|-------------------------------|
| Ideation | YES - might just want ideas, not script yet |
| Scripting | YES - might have idea already, just need script |
| Packaging | YES - might have video, just need title/thumbnail |
| Publishing | YES - just need the checklist |

**Result:** Each section could be standalone because different contexts need just that part.

---

### 4. Expertise Test

**Question:** "Does each section require a DIFFERENT type of expertise?"

**How to apply:**
- Identify the core expertise for each section
- If expertise differs significantly, they're probably different skills

**Example: YouTube workflow**
| Section | Core Expertise |
|---------|----------------|
| Ideation | Pattern recognition, audience psychology, trend analysis |
| Scripting | Storytelling, pacing, structure, hooks |
| Packaging | CTR psychology, visual hierarchy, copywriting |
| Editing | Rhythm, retention, technical proficiency |

**Result:** All different expertise → All separate skills.

**Counter-example: API Client**
| Section | Core Expertise |
|---------|----------------|
| Request building | HTTP, REST patterns |
| Error handling | HTTP, REST patterns |
| Response parsing | HTTP, REST patterns |

**Result:** Same expertise throughout → One skill.

</splitting_tests>

---

<counting_skills>

## Rules for Counting Skills

### Principle: One Skill = One Domain of Expertise

A skill should encapsulate ONE cohesive body of knowledge that:
- Could be taught as a standalone workshop
- Has clear inputs and outputs
- Doesn't require constant context-switching

### Signs You Have ONE Skill

- All parts use the same mental model
- Knowledge from part A helps with part B
- You'd teach them together in the same session
- Examples naturally span all parts

### Signs You Have MULTIPLE Skills

- Parts require shifting mental models
- An expert in part A isn't necessarily expert in part B
- You'd teach them in separate sessions
- Examples are isolated to specific parts

### Counting Heuristic

1. List all major capabilities in the workflow
2. Group by expertise type
3. Each expertise group = potential skill
4. Apply splitting tests to confirm

</counting_skills>

---

<counting_subagents>

## Rules for Counting Subagents

### Principle: One Subagent = One Persona/Focus

Create a subagent when you need:
- A distinct persona (harsh critic, security expert)
- Isolated execution (shouldn't interact with user)
- Limited tool access (safety/focus)
- Fresh context (avoid main thread pollution)

### Signs You Need ONE Subagent

- Single focused analysis task
- One type of output
- Consistent persona throughout

### Signs You Need MULTIPLE Subagents

- Different personas for different phases
- Different tool requirements
- Would never run together

### Example: YouTube Workflow

| Need | Subagent? | Why |
|------|-----------|-----|
| Idea evaluation | YES - "harsh critic" persona | Needs critical mindset main Claude won't adopt |
| Trend research | MAYBE - depends on isolation need | Fresh context might help, but could be skill |
| Script review | MAYBE - if want specific focus | Could be skill with review workflow instead |
| Security review | YES - security expert persona | Needs isolation and limited tools |

### Subagent vs Skill Decision

| Factor | Favor Subagent | Favor Skill |
|--------|----------------|-------------|
| User interaction | None needed | Questions/iteration needed |
| Persona | Different from main Claude | Same as main Claude |
| Output | Single report/artifact | Guided process |
| Learning | Not needed | Want to learn the approach |

</counting_subagents>

---

<counting_commands>

## Rules for Counting Commands

### Principle: One Command = One Trigger Point

Commands are shortcuts. Count them by counting distinct trigger moments.

### Signs You Need ONE Command

- Single action triggered
- Same context every time
- No branching paths

### Signs You Need MULTIPLE Commands

- Different triggers for different scenarios
- Significantly different inputs
- Different tool restrictions needed

### Example: Git Operations

| Trigger | Command |
|---------|---------|
| "Create commit" | `/commit` |
| "Review PR" | `/review-pr [number]` |
| "Check diff" | `/diff` |

Three distinct triggers = three commands.

### Don't Over-Command

❌ Don't create:
- `/commit-feature`
- `/commit-fix`
- `/commit-docs`

✅ Create:
- `/commit [type]` - One command with optional argument

</counting_commands>

---

<workflow_to_skill>

## Mapping Workflows to Skills

When analyzing a comprehensive workflow document:

### Step 1: Identify Natural Boundaries

Look for:
- Phase transitions ("ideation → scripting → production")
- Deliverable handoffs ("idea doc → script → video")
- Context switches ("creative mode → technical mode")

### Step 2: Apply Expertise Test

For each identified section:
- What expertise does this require?
- Is it the same as adjacent sections?

### Step 3: Apply Remaining Tests

For sections with same expertise:
- Boundary test: Can A complete without B?
- Naming test: Can name without "and"?
- Context test: Would anyone need just this?

### Step 4: Map to Components

| Section Analysis | Maps To |
|------------------|---------|
| Distinct expertise, reusable | Skill |
| Needs different persona | Subagent |
| Just a trigger | Command |
| Static reference | claude.md |
| One-time/project-specific | Project docs |

### Example Mapping

**Input:** YouTube content creation workflow doc

**Analysis:**
1. Ideation (pattern recognition) → Skill: youtube-ideation
2. Scripting (storytelling) → Skill: youtube-scripting
3. Packaging (CTR psychology) → Skill: youtube-packaging
4. Harsh critic (different persona) → Subagent: video-critic
5. Trend research (isolated context) → Subagent: trend-researcher (optional)
6. Publish checklist (just steps) → Command: /youtube-publish
7. Production notes (reference) → claude.md
8. Editing guidelines (reference) → claude.md

**Output:** 3 skills, 1-2 subagents, 1 command, 2 claude.md sections

</workflow_to_skill>

---

<anti_patterns>

## Anti-Patterns to Avoid

### Mega-Skill

**Problem:** One file with 5+ methodologies crammed together
**Solution:** Split by expertise boundaries

### Micro-Skill

**Problem:** Skill for a simple checklist
**Solution:** Make it a command instead

### Agent Overuse

**Problem:** Subagent for everything
**Solution:** Only when persona/isolation actually needed

### Blurry Boundaries

**Problem:** Skills that overlap significantly
**Solution:** Each skill owns one domain exclusively

### Premature Abstraction

**Problem:** Creating capabilities for one-time needs
**Solution:** Only create when pattern repeats 2-3+ times

</anti_patterns>
