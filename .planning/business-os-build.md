# Plan: Build HR Department for Business Operating System

## Summary

Create `~/projects/business-os/` with the HR Department as the first team. HR can then create all other departments, agents, skills, and commands.

**VERIFIED BEHAVIOR:** Claude Code does NOT traverse parent directories. It only looks at:
1. `.claude/` in current working directory (project scope)
2. `~/.claude/` in home directory (user scope - globally available)

**HYBRID APPROACH:** Put shared skills in `~/.claude/` (globally available everywhere). Each department gets its own `.claude/` for department-specific items.

---

## Phase 1: Foundation Structure

### 1.1 Directory Structure

```
~/.claude/                        # USER SCOPE - Available EVERYWHERE
├── skills/                       # Shared skills (create-*, debug-*, etc.)
│   ├── create-subagents/
│   ├── create-agent-skills/
│   ├── create-slash-commands/
│   ├── create-hooks/
│   ├── create-plans/
│   ├── create-meta-prompts/
│   └── debug-like-expert/
├── agents/                       # Shared auditor agents
│   ├── skill-auditor.md
│   ├── subagent-auditor.md
│   └── slash-command-auditor.md
└── commands/                     # (optional shared commands)

~/projects/business-os/           # PROJECT ROOT
├── .claude/                      # Root orchestration
│   └── CLAUDE.md                 # Master brain - routes to departments
├── .planning/                    # Project plans
│   └── hr-department-build.md    # This implementation plan
├── docs/                         # Guidance documents
│   ├── context-handoff.md
│   ├── todo-management.md
│   └── meta-prompting.md
├── failures.md                   # Org-wide failures
├── learnings.md                  # Org-wide insights
│
└── hr-department/                # HR DEPARTMENT (open separate window here)
    ├── .claude/                  # HR-specific items
    │   ├── skills/
    │   │   └── hr-operations/    # Main HR skill
    │   ├── agents/
    │   │   ├── knowledge-researcher.md
    │   │   └── department-auditor.md
    │   ├── commands/
    │   │   ├── hire.md
    │   │   ├── interview.md
    │   │   └── ... (other HR commands)
    │   └── CLAUDE.md             # HR department context
    ├── failures.md
    └── learnings.md
```

### 1.2 How This Works

**When working from `~/projects/business-os/`:**
- Claude sees: root `.claude/` + `~/.claude/` (shared skills)
- Use for: high-level orchestration, cross-department work

**When working from `~/projects/business-os/hr-department/`:**
- Claude sees: hr-department's `.claude/` + `~/.claude/` (shared skills)
- Does NOT see: business-os root `.claude/`
- Use for: focused HR work with HR-specific agents/commands

**Benefits:**
- Shared skills (create-*, audit-*) available everywhere via `~/.claude/`
- Department-specific context only loads when in that folder
- No context pollution between departments
- Can open multiple Claude windows for parallel work (like Darren does)

### 1.3 Files to Create

| Location | File | Purpose |
|----------|------|---------|
| `~/.claude/` | skills/, agents/ | Copy shared skills from taches-cc-resources |
| `business-os/` | `.claude/CLAUDE.md` | Root orchestration brain |
| `business-os/` | `failures.md`, `learnings.md` | Org-wide learning |
| `business-os/` | `docs/*.md` | Copy guidance docs from taches-cc-resources |
| `hr-department/` | `.claude/CLAUDE.md` | HR department context |
| `hr-department/` | `.claude/skills/hr-operations/` | Main HR skill |
| `hr-department/` | `.claude/agents/*.md` | HR-specific agents |
| `hr-department/` | `.claude/commands/*.md` | HR-specific commands |
| `hr-department/` | `failures.md`, `learnings.md` | HR learning |

---

## Phase 2: Copy Shared Skills to ~/.claude/ (Global)

### Skills to Copy to `~/.claude/skills/` (7)

These go in HOME so they're available in ALL projects:

| Source (taches-cc-resources) | Destination |
|------------------------------|-------------|
| `skills/create-subagents/` | `~/.claude/skills/create-subagents/` |
| `skills/create-agent-skills/` | `~/.claude/skills/create-agent-skills/` |
| `skills/create-slash-commands/` | `~/.claude/skills/create-slash-commands/` |
| `skills/create-hooks/` | `~/.claude/skills/create-hooks/` |
| `skills/create-plans/` | `~/.claude/skills/create-plans/` |
| `skills/create-meta-prompts/` | `~/.claude/skills/create-meta-prompts/` |
| `skills/debug-like-expert/` | `~/.claude/skills/debug-like-expert/` |

### Agents to Copy to `~/.claude/agents/` (3)

| Source (taches-cc-resources) | Destination |
|------------------------------|-------------|
| `agents/skill-auditor.md` | `~/.claude/agents/skill-auditor.md` |
| `agents/subagent-auditor.md` | `~/.claude/agents/subagent-auditor.md` |
| `agents/slash-command-auditor.md` | `~/.claude/agents/slash-command-auditor.md` |

### Docs to Copy to business-os/docs/ (3)

| Source (taches-cc-resources) | Destination |
|------------------------------|-------------|
| `docs/context-handoff.md` | `business-os/docs/context-handoff.md` |
| `docs/todo-management.md` | `business-os/docs/todo-management.md` |
| `docs/meta-prompting.md` | `business-os/docs/meta-prompting.md` |

---

## Phase 3: Create HR Operations Skill (Main Router)

### 3.1 Structure

Lives in HR's `.claude/` so it's HR-specific (only visible when working in hr-department/):

```
~/projects/business-os/hr-department/.claude/skills/hr-operations/
├── SKILL.md                      # Router + essential principles
├── workflows/
│   ├── conduct-interview.md      # Requirements gathering via AskUserQuestion
│   ├── onboard-knowledge.md      # Capture user expertise
│   ├── create-department.md      # Full department with agents/skills
│   ├── create-agent.md           # Individual agent
│   ├── create-skill.md           # Skill for agent
│   ├── create-command.md         # Slash command
│   └── improve-component.md      # Heal/refine existing component
├── references/
│   ├── interview-questions.md    # Question templates by type
│   ├── department-templates.md   # Department patterns
│   ├── agent-archetypes.md       # Common agent types
│   └── knowledge-gathering.md    # How to capture expertise
└── templates/
    ├── department-claude-md.md   # Template for new dept CLAUDE.md
    ├── agent-job-description.md  # Template for agent specs
    └── failures-learnings.md     # Template for learning files
```

### 3.2 Key Design: Interview Flow

The core differentiator - structured requirements gathering:

1. **Type Selection** (AskUserQuestion - multiple choice)
   - Department / Agent / Skill / Command

2. **Purpose Gathering** (AskUserQuestion)
   - What should it do? What's the mission?

3. **Knowledge Assessment** (AskUserQuestion - multiple choice)
   - "I'm the expert" / "I have docs" / "Just ideas" / "Starting fresh"

4. **Knowledge Capture** (based on assessment)
   - Expert: Walk me through your process
   - Has docs: Share them, I'll structure
   - Ideas: Describe success, I'll research
   - Fresh: I'll research best practices

5. **Research Decision** (AskUserQuestion - with judgment)
   - Yes comprehensive / Yes targeted / No, enough / Decide for me
   - If "Decide for me" → HR applies judgment based on knowledge volume

6. **Plan Proposal** → User approval → Build

---

## Phase 4: Create HR Subagents

### 4.1 New Agents to Create (in `hr-department/.claude/agents/`)

| Agent | Purpose |
|-------|---------|
| `knowledge-researcher.md` | Research online to extend user knowledge (WebSearch, WebFetch) |
| `department-auditor.md` | Audit department health (structure, CLAUDE.md, learning infra) |

### 4.2 Agent Patterns

Follow existing auditor pattern from `subagent-auditor.md`:
- Pure XML structure
- Clear `<role>`, `<constraints>`, `<workflow>`, `<output_format>`
- Minimal tool access (least privilege)
- Structured output format

---

## Phase 5: Create HR Commands (in `hr-department/.claude/commands/`)

| Command | Purpose | Invokes |
|---------|---------|---------|
| `/hire` | Main entry point: `/hire [agent/department/skill]` | hr-operations skill |
| `/interview` | Start requirements gathering | conduct-interview workflow |
| `/audit-department` | Check department health | department-auditor agent |
| `/improve` | Enhance existing component | improve-component workflow |
| `/heal-component` | Fix issues from execution | (pattern from heal-skill) |
| `/org-chart` | View organization structure | Bash ls + tree |

---

## Phase 6: Learning Infrastructure

### failures.md Template
```markdown
# Failures Log

## Entry Format
### [Date] - [Title]
**What Happened**:
**Root Cause**:
**Resolution**:
**Prevention**:
```

### learnings.md Template
```markdown
# Learnings Log

## Entry Format
### [Date] - [Insight]
**Discovery**:
**Context**:
**Application**:
**Components Updated**:
```

Each department AND each skill gets its own failures.md + learnings.md.

---

## Implementation Order

### Step 0: Save plan to working directory
- [x] Copy this plan to `taches-cc-resources/.planning/business-os-build.md`
- [x] This becomes the authoritative plan we work from

### Step 1: Copy shared skills/agents to ~/.claude/ (global)
- [x] Create `~/.claude/skills/` if doesn't exist
- [x] Copy 7 skills from taches-cc-resources to `~/.claude/skills/`
- [x] Create `~/.claude/agents/` if doesn't exist
- [x] Copy 3 auditor agents to `~/.claude/agents/`
- [x] Verify skills work from any directory

### Step 2: Create business-os directory structure
- [x] Create `~/projects/business-os/`
- [x] Create `.claude/` with CLAUDE.md
- [x] Create `.planning/` and copy this plan there
- [x] Create `docs/` and copy 3 docs from taches-cc-resources
- [x] Write root `failures.md` and `learnings.md`

### Step 3: Create HR department structure
- [x] Create `hr-department/`
- [x] Create `hr-department/.claude/` with skills/, agents/, commands/
- [x] Write `hr-department/.claude/CLAUDE.md` (HR context)
- [x] Write `hr-department/failures.md` and `learnings.md`

### Step 4: Create hr-operations skill
- [x] Write SKILL.md (router)
- [x] Write references (4 files)
- [x] Write templates (3 files)
- [x] Write workflows (7 files) - conduct-interview FIRST

### Step 5: Create HR agents
- [x] Write `hr-department/.claude/agents/knowledge-researcher.md`
- [x] Write `hr-department/.claude/agents/department-auditor.md`

### Step 6: Create HR commands
- [x] Write `hr-department/.claude/commands/hire.md`
- [x] Write `hr-department/.claude/commands/interview.md`
- [x] Write `hr-department/.claude/commands/audit-department.md`
- [x] Write `hr-department/.claude/commands/improve.md`
- [x] Write `hr-department/.claude/commands/heal-component.md`
- [x] Write `hr-department/.claude/commands/org-chart.md`

### Step 7: Test the system
- [ ] Open Claude in hr-department/, verify HR skills + global skills work
- [ ] Test /hire command to create a sample department
- [ ] Capture any failures/learnings
- [ ] Refine based on experience

---

## Critical Files Reference

**Patterns to follow:**
- Router pattern: `taches-cc-resources/skills/create-agent-skills/SKILL.md`
- Heal pattern: `taches-cc-resources/commands/heal-skill.md`
- Auditor pattern: `taches-cc-resources/agents/subagent-auditor.md`
- Interview flow: `taches-cc-resources/skills/create-meta-prompts/SKILL.md`

---

## Key Decisions Made

1. **Location**: `~/projects/business-os/` (separate from taches-cc-resources)
2. **Verified behavior**: Claude does NOT traverse parent directories
3. **Hybrid approach**: Shared skills in `~/.claude/` (global), department-specific in each dept's `.claude/`
4. **Shared globally**: 7 create-* skills + 3 auditor agents in `~/.claude/`
5. **HR-specific**: HR operations skill, agents, commands in `hr-department/.claude/`
6. **Learning location**: Both per-department AND per-skill failures.md/learnings.md
7. **HR capabilities**: Full departments, agents, skills, and commands
8. **Interview approach**: AskUserQuestion with multiple choice for speed
9. **Research integration**: Optional, with HR judgment when user says "decide for me"
10. **Docs copied**: context-handoff, todo-management, meta-prompting to business-os/docs/
11. **Usage pattern**: Open separate Claude windows per department (like Darren does)

## Sources

- [Claude Code Subagents Docs](https://code.claude.com/docs/en/sub-agents)
- [Using CLAUDE.MD files](https://claude.com/blog/using-claude-md-files)
- [Claude Code Setup Guide](https://keonarmin.com/blog/claude-code-configs)
