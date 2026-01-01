---
description: Capture session learnings and propose skill improvements
argument-hint: [optional: specific skill path]
---

<objective>
Review the current conversation, capture learnings, and propose improvements to skill files themselves.
Skills can evolve and improve with every session - not just through learning logs, but through actual content updates.
</objective>

<process>
## Phase 1: Identify Active Skills

If argument provided:
- Focus on that specific skill path

Otherwise, scan for skills that were likely used:
```bash
ls ~/.claude/skills/
ls ~/.claude/skills/expertise/
```

Look for skill invocations in the conversation:
- Direct skill mentions
- Slash commands that invoke skills
- Domain-specific work that would use expertise skills

Ask user to confirm which skill(s) to update if unclear.

## Phase 2: Extract Learning Moments

Review the conversation for:

**SUCCESSES:**
- What worked well
- Breakthroughs or insights
- Effective patterns discovered
- Approaches that should be repeated

**FAILURES:**
- What didn't work
- Dead ends encountered
- Counterproductive approaches
- Things to avoid in the future

**SKILL GAPS:**
- Missing guidance that would have helped
- Outdated instructions that caused problems
- Unclear sections that led to confusion
- Anti-patterns not yet documented

Focus on learnings that are:
- Specific and actionable
- Likely to recur in future sessions
- Not already documented in the skill

## Phase 3: Categorize Proposed Changes

For each insight, determine the appropriate action:

| Type | Action | Target |
|------|--------|--------|
| New pattern discovered | Append entry | learnings.md |
| Dead end documented | Append entry | failures.md |
| Missing guidance | Propose addition | SKILL.md or reference file |
| Outdated instruction | Propose edit | SKILL.md or reference file |
| Unclear section | Propose rewrite | SKILL.md or reference file |
| New anti-pattern | Propose addition | anti_patterns section |

## Phase 4: Present Proposed Changes

### Format for learning file additions:

```
📝 LEARNING FILE UPDATES

For [skill-name]/learnings.md:
────────────────────────────────────
+ ## Entry: [YYYY-MM-DD]
+
+ **Context:** [description]
+
+ **Learning:** [what was discovered]
+
+ **Example:** [concrete example]
────────────────────────────────────

For [skill-name]/failures.md:
────────────────────────────────────
+ ## Entry: [YYYY-MM-DD]
+
+ **Context:** [description]
+
+ **Failure:** [what didn't work]
+
+ **Why:** [why it failed]
────────────────────────────────────
```

### Format for skill file modifications:

```
🔧 SKILL FILE CHANGES

File: [skill-name]/SKILL.md
Location: Line [X] (inside <section_name>)

CURRENT:
┌─────────────────────────────────
│ [existing content]
└─────────────────────────────────

PROPOSED:
┌─────────────────────────────────
│ [new content]
└─────────────────────────────────

REASON: [Why this change improves the skill]
```

**Show ALL proposed changes before any modifications.**

## Phase 5: Get Explicit Approval

Present options using AskUserQuestion:

**Question:** "How would you like to apply these changes?"

**Options:**
1. **Apply all changes** - Update learning files and skill files
2. **Learning files only** - Only append to learnings.md/failures.md (safer)
3. **Review individually** - Approve each change one by one
4. **Skip all** - Don't make any changes

For skill file changes, ALWAYS show the exact diff before applying.

## Phase 6: Apply Approved Changes

**For learning files:**
- Read existing learnings.md and failures.md (if they exist)
- Append new entries to the appropriate file
- Create files if they don't exist (with header template)

**For skill files:**
- Make the approved edits to SKILL.md or reference files
- Preserve existing structure and formatting
- Report exactly what was changed and where

**Starter templates for new learning files:**

learnings.md:
```markdown
# Learnings

Accumulated knowledge from working sessions. Updated via /retrospective.

---

```

failures.md:
```markdown
# Failures & Dead Ends

Things that didn't work. Avoid repeating these patterns.

---

```

## Phase 7: Summary

Report:
- What was added to learning files
- What was changed in skill files (with file paths and line numbers)
- Suggest: "Run `/audit-skill [path]` to verify changes"
</process>

<skill_modification_guidelines>
**When to propose SKILL.md changes:**
- Missing guidance that caused confusion during the session (add it)
- Outdated instructions that no longer work (update them)
- Anti-patterns discovered through failure (add to anti_patterns section)
- New best practices validated through success (add to guidance)
- Unclear wording that led to misunderstanding (clarify it)

**When NOT to modify SKILL.md:**
- One-off edge cases (use learning files instead)
- User-specific preferences (not generalizable)
- Unvalidated ideas (need more sessions to confirm)
- Stylistic preferences (unless causing real problems)

**Safety rules:**
- NEVER modify without showing exact diff first
- NEVER change YAML frontmatter without explicit request
- ALWAYS preserve existing structure and formatting
- Prefer ADDITIONS over replacements when possible
- Keep changes minimal and focused
</skill_modification_guidelines>

<edge_cases>
**No clear learnings found:**
Report: "No significant learning moments identified in this session. This is fine - not every session produces documentable insights."

**Skill doesn't support continual learning:**
If the skill has no learnings.md or failures.md, ask:
"This skill doesn't have learning files yet. Create them? [Y/n]"

**Multiple skills used:**
Present learnings grouped by skill, let user confirm each skill separately.

**User provides specific skill path:**
Skip the identification step, go directly to extraction for that skill.

**Proposed skill change is risky:**
Flag with ⚠️ and explain why extra caution is warranted.
</edge_cases>

<success_criteria>
- Relevant skills identified (or user-specified skill used)
- Learnings categorized appropriately (learning files vs skill changes)
- Exact diffs shown for any skill file changes
- User explicitly approved before any writes
- Changes applied cleanly
- Summary provided with file paths
</success_criteria>
