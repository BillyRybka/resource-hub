<overview>
Skills can learn and improve over time by capturing successes and failures from working sessions. Instead of manually encoding every insight into the skill, the model extracts learnings at session end and writes them to persistent files. This creates a flywheel where knowledge compounds across sessions.
</overview>

<why_continual_learning>
**The problem:**
- Models don't retain session knowledge across conversations
- Manual encoding of insights is slow and incomplete
- Failures are valuable but rarely documented
- Each session's reasoning is discarded after the task

**The solution:**
- Store learnings outside the model's weights in readable files
- Capture both successes AND failures
- Let the model propose learnings, human approves
- Skills get better with every session

**Key insight from Robert Nishihara (Anyscale CEO):**
"The knowledge stored outside the model's weights in skills we can read, edit, and share. Every session's reasoning can compound into future skills."
</why_continual_learning>

<implementation>
## Adding Continual Learning to a Skill

### Step 1: Create Learning Files

Add two files to the skill directory:

```
your-skill/
├── SKILL.md
├── references/       # (if applicable)
├── workflows/        # (if applicable)
├── learnings.md      # NEW: Accumulated successes
└── failures.md       # NEW: Documented failures
```

### Step 2: Create Starter Templates

**learnings.md:**
```markdown
# Learnings

Accumulated knowledge from working sessions. Updated via /retrospective.

---

```

**failures.md:**
```markdown
# Failures & Dead Ends

Things that didn't work. Avoid repeating these patterns.

---

```

### Step 3: Reference in SKILL.md

Add a section to your skill that tells Claude to check these files:

```xml
<continual_learning>
Before starting work, check for accumulated knowledge:
- Read learnings.md for patterns that work
- Read failures.md for approaches to avoid

After significant work, suggest running /retrospective to capture new insights.
</continual_learning>
```

### Step 4: Use /retrospective

At the end of working sessions, run `/retrospective` to:
1. Review the conversation for learning moments
2. Extract successes and failures
3. Propose updates to the skill's learning files
4. Write updates after confirmation
</implementation>

<learning_entry_format>
Each learning entry follows this format:

```markdown
## Entry: [YYYY-MM-DD]

**Context:** [Brief description of what was being worked on]

**Learning:** [What was discovered - specific and actionable]

**Example:** [Concrete example if applicable]

**Tags:** [Optional: categorization for easier retrieval]
```

**Good entry example:**
```markdown
## Entry: 2025-01-15

**Context:** Building a webclass transformation for personal branding coaches

**Learning:** Transformations that focus on identity shift ("invisible expert → recognized authority") land better than capability claims ("learn to build your brand")

**Example:**
- Weak: "Learn how to grow your personal brand on LinkedIn"
- Strong: "Go from invisible expert to recognized authority in your field"

**Tags:** transformation, identity, webclass
```

**Bad entry example:**
```markdown
## Entry: 2025-01-15

**Learning:** The webclass went well.
```
(Too vague, no context, not actionable)
</learning_entry_format>

<retrospective_integration>
The `/retrospective` command is the primary way to capture learnings and improve skills.

**How it works:**
1. Scans conversation for skill invocations
2. Identifies which skills were active
3. Extracts successes, failures, AND skill gaps
4. Categorizes changes: learning files vs skill file modifications
5. Shows proposed updates with exact diffs
6. Gets explicit approval before any writes
7. Applies approved changes and provides summary

**Two types of changes:**
- **Learning file additions** - Append entries to learnings.md/failures.md
- **Skill file modifications** - Propose edits to SKILL.md or reference files (see `<skill_self_improvement>`)

**When to run it:**
- End of significant working sessions
- After breakthroughs or major insights
- After encountering and resolving problems
- When you notice patterns worth documenting
- When skill guidance was missing or unclear

**Skills should mention /retrospective** in their success_criteria or closing guidance to remind users.
</retrospective_integration>

<skill_self_improvement>
## Skills That Improve Themselves

Skills can evolve beyond just logging learnings - they can modify their own content based on session insights.

**Key insight:**
Claude can read AND write to skill files. When a session reveals missing guidance, outdated instructions, or new anti-patterns, `/retrospective` can propose changes to the actual SKILL.md file.

### Types of Self-Improvement

| Trigger | Action | Target |
|---------|--------|--------|
| New pattern discovered | Append entry | learnings.md |
| Dead end documented | Append entry | failures.md |
| Missing guidance | Propose addition | SKILL.md or reference file |
| Outdated instruction | Propose edit | SKILL.md or reference file |
| Unclear section | Propose rewrite | SKILL.md or reference file |
| New anti-pattern | Propose addition | anti_patterns section |

### The Approval Workflow

Skill file modifications always require explicit approval:

1. **Extract** - Claude identifies skill gaps from the session
2. **Propose** - Shows exact diff with CURRENT and PROPOSED content
3. **Explain** - Provides reason why this change improves the skill
4. **Confirm** - User chooses: apply all, learning files only, review individually, or skip
5. **Apply** - Makes approved changes and reports exactly what was modified

**Example modification proposal:**
```
🔧 SKILL FILE CHANGES

File: webclass-blueprint/SKILL.md
Location: Line 45 (inside <common_mistakes>)

CURRENT:
┌─────────────────────────────────
│ - Making the webclass too long (aim for 60-90 minutes)
│ - Starting with credentials instead of story
└─────────────────────────────────

PROPOSED:
┌─────────────────────────────────
│ - Making the webclass too long (aim for 60-90 minutes)
│ - Starting with credentials instead of story
│ - Revealing the mechanism too early (save for pitch)
└─────────────────────────────────

REASON: Session revealed that explaining the mechanism during content
undermines the pitch - save it for the offer reveal.
```

### When to Propose Skill Changes

**DO propose changes when:**
- Missing guidance caused confusion during the session
- Outdated instructions no longer work
- Anti-patterns discovered through failure
- New best practices validated through success
- Unclear wording led to misunderstanding

**DON'T propose changes for:**
- One-off edge cases (use learning files instead)
- User-specific preferences (not generalizable)
- Unvalidated ideas (need more sessions to confirm)
- Stylistic preferences (unless causing real problems)

### Safety Rules

- **NEVER** modify without showing exact diff first
- **NEVER** change YAML frontmatter without explicit request
- **ALWAYS** preserve existing structure and formatting
- **Prefer additions** over replacements when possible
- **Keep changes minimal** and focused

### The Flywheel Effect

```
Session → Learning → Skill Update → Better Session → Better Learning → ...
```

Over time, skills accumulate both:
1. **Learning files** - Session-specific insights, examples, edge cases
2. **Core skill content** - Patterns promoted from learning files, validated guidance

When a learning appears 3+ times in learnings.md, it's a candidate for promotion to SKILL.md itself.
</skill_self_improvement>

<best_practices>
**Keep entries concise and actionable**
- Focus on what to DO or AVOID, not abstract observations
- Include enough context to be useful later
- One learning per entry (don't bundle)

**Include concrete examples**
- Show before/after comparisons
- Include actual text, not descriptions of text
- Real examples are more useful than principles

**Document failures without judgment**
- Failures are valuable data, not mistakes
- Explain WHY something didn't work
- Note what was tried so it's not repeated

**Review and consolidate periodically**
- After ~20 entries, look for patterns
- Consolidate related learnings
- Promote repeated patterns to the main SKILL.md

**Tag entries for retrieval**
- Use consistent tag vocabulary
- Tags help Claude find relevant past learnings
- Keep tags simple and few

**Let the model propose, you approve**
- Claude extracts learnings from conversation
- You review and confirm before writing
- Edit if the model missed nuance
</best_practices>

<when_to_use>
**Good candidates for continual learning:**

| Type | Why |
|------|-----|
| Domain expertise skills | Accumulate field-specific knowledge |
| Creative/ideation skills | Learn what resonates vs. falls flat |
| Skills with subjective quality | Writing, design, communication |
| Frequently used skills | More sessions = more opportunities to learn |
| Skills for specific audiences | Learn what works for YOUR users |

**Less useful for:**

| Type | Why |
|------|-----|
| One-off utility skills | Used rarely, little to accumulate |
| Deterministic skills | Formatters, validators - clear right/wrong |
| Simple transformation skills | Convert X to Y - no judgment involved |
| Skills with external ground truth | API wrappers - the API defines correctness |

**Decision heuristic:**
If the skill involves judgment, creativity, or audience-specific effectiveness → add continual learning.
If the skill has clear right/wrong answers defined externally → skip it.
</when_to_use>

<maintenance>
**Periodic review (every ~20 entries):**
1. Read through learnings.md and failures.md
2. Look for patterns or repeated themes
3. Consolidate related entries
4. Promote important patterns to SKILL.md itself
5. Archive or remove outdated entries

**Promoting to SKILL.md:**
When a learning appears 3+ times or becomes foundational:
- Add it to the skill's core guidance
- Remove from learnings.md (it's now built-in)
- Note in the entry: "Promoted to SKILL.md on [date]"

**Archiving:**
For entries that are no longer relevant:
- Move to an `archive/` folder, or
- Delete with a note in git commit
</maintenance>
