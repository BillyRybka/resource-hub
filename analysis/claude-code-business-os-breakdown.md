# Claude Code Business Operating System - Complete Breakdown

## Source: Darren Viner (AAA Community by Liam Otley)

---

## Executive Summary

This system transforms Claude Code from a developer tool into a **complete AI-powered business operating system**. The key insight: Claude Code solves the fundamental limitations of ChatGPT, Gemini, and other AI tools (memory, context, orchestration) while requiring zero coding knowledge.

---

## Part 1: Problems This System Solves

### Traditional AI Tool Limitations

| Problem | Description |
|---------|-------------|
| **Context Window Management** | Models lose performance as context fills, forget details, hallucinate |
| **Siloed Sessions** | Cannot share context across chats, projects, or custom GPTs |
| **Manual Orchestration** | Must manually call teams/GPTs, copy-paste between sessions |
| **Limited External Connections** | Connectors are basic (can't write to Google Docs), clunky authentication |
| **Fragile Automation Stacks** | N8N, Make.com, Zapier = expensive, brittle, become obsolete fast |

### Why Claude Code is the Solution

- Anthropic is investing massively in Claude Code (evergreen tool)
- Built for coders BUT requires zero coding knowledge
- VS Code extension = chatbot-like experience
- Original use case: **business operations, not coding**

---

## Part 2: Core Architecture Components

### 2.1 CLAUDE.md Files (The Business Brain)

**What it is:** A markdown file that acts as a system prompt/permanent memory for each project folder.

**Key Characteristics:**
- Functions like custom instructions for ChatGPT projects
- Can exist in ANY folder (hierarchical structure)
- Automatically loaded when Claude Code opens in that folder
- Contains: project context, business context, mechanisms, instructions

**Advantages:**
- No need to re-explain project context
- Different instructions per project/folder
- Compound knowledge (update as you work)
- Can include executable mechanisms

**Structure Pattern:**
```
/Business-OS/
├── CLAUDE.md                    # Root business brain
├── /Department-A/
│   ├── CLAUDE.md               # Department-specific context
│   └── /Project-1/
│       └── CLAUDE.md           # Project-specific context
```

---

### 2.2 Sub-Agents (AI Worker Teams)

**What they are:** Specialized AI assistants with isolated context windows (200K tokens each).

**Key Features:**
- Isolated context = don't pollute main conversation
- Auto-invoked by Claude Code based on task matching
- Run in parallel OR sequentially (Claude orchestrates)
- Access files in working folder
- Can communicate via files or Claude-passed context

**Sub-Agent File Structure:**
```markdown
---
name: Agent Name
description: What the agent does (used for auto-invocation)
mission: The agent's purpose
color: (optional) For terminal visibility
tools: (optional) Specific tools access
---

[Agent instructions and processes]
```

**Availability Levels:**
- **Project level:** Available only in specific folder
- **Personal/Global level:** Available everywhere in Claude Code

**Creation Methods:**
1. `/agents` command → configure agents (terminal)
2. Custom "HR Team" system (recommended by creator)

---

### 2.3 Skills (Reusable Workflows/SOPs)

**What they are:** Standard Operating Procedures that Claude Code can trigger automatically.

**Key Features:**
- Auto-triggered based on context matching
- **Progressive Disclosure:** Claude reads only what it needs (context-friendly)
- Mix deterministic code (scripts) + LLM flexibility
- Shareable across teams, customers, projects
- Build once, use anywhere

**Skill File Structure:**
```
/skill-name/
├── SKILL.md                    # Main skill file with metadata
├── /references/                # Knowledge files
├── /scripts/                   # Python/JS scripts for deterministic tasks
└── /examples/                  # Example implementations
```

**SKILL.md Structure:**
```markdown
---
name: Skill Name
description: What the skill does (for auto-invocation)
---

# Extended Description

# Process Steps

# Troubleshooting

# Reference Documentation
(Progressive disclosure - Claude discovers these as needed)

# Example Skills

# Scripts

# Version History
```

**When to Create a Skill:**
- When you know how to do something well
- When you want it done the same way every time
- When it should be available across all projects

---

### 2.4 External Connections

#### APIs (Direct Integration)

**Concept:** APIs are interfaces that allow software to communicate.

**Process:**
1. Find the external tool's API documentation
2. Have Claude Code ingest the documentation
3. Get API keys/authentication
4. Claude Code writes the scripts to interact

**Use Cases:**
- Gmail integration
- Google Docs
- CRM (add/pull data)
- Social media posting
- Database operations
- Presentation tools (e.g., Gamma)

**Storage:** API keys stored in `.env` file

#### MCPs (Model Context Protocol)

**What it is:** Standardized protocol for AI agents to communicate with external tools.

**Analogy:** Power adapters for different countries - MCP is the standardized adapter.

**Benefits:**
- Pre-made toolboxes for external apps
- Auto-integration (Claude understands available tools)
- Standardized = easy to develop and use

**Reality Check (Creator's Warning):**
- New technology, needs maturity
- Many MCPs are poorly developed/unstable
- Only use official, well-documented MCPs
- Check: stars, recent updates, contributors

**When to Use What:**
| Scenario | Recommendation |
|----------|----------------|
| Proven official MCP exists | Use MCP |
| No MCP or only crappy open-source | Use API scripts |
| Need custom logic | Use API scripts |

**MCP Installation:**
```bash
# Check MCP status
/mcp

# Manage MCPs
/mcp manage
```

---

## Part 3: The Department/Team Structure

### Creator's Team Organization

```
CEO (You)
├── Operational Team (Business OS)
│   └── Multiple parallel sessions
├── HR Team (GPT Express Mastery)
│   └── Creates sub-agents and custom GPTs
└── Content Team (Magnetic Content OS)
    └── 14 sub-agents
    └── Multiple parallel sessions
```

### The "HR Team" Concept

A dedicated "department" for creating other agents:
- Sub-agent creation
- Custom GPT creation
- Uses "GPT Express Mastery Framework"

**Process Flow:**
1. Request: "I need an agent that can answer questions about X"
2. HR Team refines the purpose
3. Calls multiple sub-agents:
   - Purpose Refiner
   - Knowledge gatherer (parallel web searches)
   - System prompt crafter
   - Tool configuration
4. Output: Ready-to-use agent or GPT

---

## Part 4: Execution Patterns

### 4.1 Parallel Execution

**Two Approaches:**

1. **Multiple Sub-Agents in One Session**
   - Claude invokes multiple agents simultaneously
   - Each gets isolated context
   - Share info via files or Claude coordination

2. **Multiple Claude Code Sessions**
   - Open several windows in same/different folders
   - YOU orchestrate and check progress
   - True CEO delegation model

**Rules for Parallel Execution:**
- Tasks must have NO dependencies
- Agents must work on DIFFERENT files
- Avoid two agents on same file = messy

### 4.2 Plan Mode (Architect Mode)

**What it is:** Read-only planning mode before execution.

**Activation:**
- Shift+Tab
- Click right part of interface
- Natural language: "think harder", "sync harder"

**Process:**
1. Claude analyzes the request
2. Writes a detailed plan
3. You review and approve
4. Then execution begins

**When to Use:**
- Significant projects
- Complex implementations
- When you want to understand the approach first

**Benefits:**
- Safety and control
- Better thinking about the project
- Structured approach
- No surprises during implementation

---

## Part 5: Advanced Usage Patterns

### 5.1 Checkpoints and Recovery

**Auto-Checkpointing:**
- Claude Code automatically creates checkpoints
- Restore if something goes wrong
- Use `/checkpoints` command

### 5.2 Command Patterns

| Command | Purpose |
|---------|---------|
| `/login` | Re-authenticate |
| `/agents` | Manage sub-agents |
| `/mcp` | Check MCP status |
| `/mcp manage` | Configure MCPs |
| `/checkpoints` | View/restore checkpoints |
| Shift+Tab | Toggle plan mode |

### 5.3 Memory Hierarchy

```
Global Level (User folder/.claude/)
├── Global CLAUDE.md
├── Global Skills
├── Global Agents
└── Global MCPs

Project Level (Any folder)
├── Project CLAUDE.md
├── Project Skills
├── Project Agents
└── Project configurations
```

---

## Part 6: The Complete Business OS

### Folder Structure Philosophy

```
/Business-OS/
├── CLAUDE.md                           # Master business brain
├── /Operational-Team/                  # Day-to-day operations
│   ├── CLAUDE.md
│   └── [operational projects]
├── /HR-Team/                           # Agent/GPT creation
│   ├── CLAUDE.md
│   ├── /agents/                        # Sub-agent definitions
│   └── /GPT-projects/                  # Custom GPT builds
├── /Content-Team/                      # Content creation
│   ├── CLAUDE.md
│   └── /14-sub-agents/
├── /Skills-Library/                    # Reusable SOPs
│   ├── /project-creator/
│   ├── /skills-factory/
│   └── [other skills]
└── /Integrations/                      # API docs, MCP configs
    ├── gamma-api/
    └── [other integrations]
```

### The ACRA Framework

Creator's business philosophy embedded in the system:
- **A**ttract - Right customers
- **C**onvert - Right customers
- **R**etain - Customer satisfaction
- **A**scend - Upselling

Everything built around: focus, prioritization, solving bottlenecks.

---

## Part 7: Key Principles

### 1. CEO Mindset
- You distribute work among AI teams
- Teams work in parallel
- You check, give feedback, provide direction

### 2. Global vs Local
- Put frequently-used items globally
- Project-specific items stay local
- Hierarchy enables organization

### 3. Progressive Disclosure
- Skills load only what's needed
- Saves context window
- Better LLM performance

### 4. Compound Knowledge
- Update CLAUDE.md as you work
- Memory grows over time
- No repeated explanations

### 5. Self-Orchestration
- Claude Code invokes agents/skills automatically
- Matches task to capability
- You can enforce specific tools when needed

---

## Part 8: Implementation Checklist

### Phase 1: Foundation
- [ ] Install VS Code
- [ ] Install Claude Code extension
- [ ] Authenticate with Claude subscription (not API)
- [ ] Create root business folder
- [ ] Write master CLAUDE.md

### Phase 2: Structure
- [ ] Create department folders
- [ ] Write CLAUDE.md for each department
- [ ] Define folder hierarchy

### Phase 3: Agents
- [ ] Create HR Team (agent creator)
- [ ] Build core operational agents
- [ ] Build content team agents
- [ ] Test auto-invocation

### Phase 4: Skills
- [ ] Create Skills Factory skill (meta-skill)
- [ ] Build project creator skill
- [ ] Build department-specific skills
- [ ] Test progressive disclosure

### Phase 5: Integrations
- [ ] Identify needed external tools
- [ ] Find/evaluate APIs
- [ ] Install vetted MCPs
- [ ] Create integration scripts

### Phase 6: Workflow
- [ ] Practice parallel execution
- [ ] Use plan mode for big projects
- [ ] Establish checkpoint habits
- [ ] Iterate and improve

---

## Glossary

| Term | Definition |
|------|------------|
| CLAUDE.md | System prompt/memory file for a project |
| Sub-Agent | Specialized AI worker with isolated context |
| Skill | Reusable workflow/SOP package |
| Progressive Disclosure | Loading only needed parts of a skill |
| MCP | Model Context Protocol - standardized external tool connection |
| Plan Mode | Architect mode for planning before execution |
| Context Window | Token limit for conversation (200K per agent) |

---

## Notes for 1:1 Recreation

To build this system yourself:

1. **Start simple** - Master folder structure + CLAUDE.md first
2. **Build the HR Team** - This creates other agents
3. **Skills Factory** - Create a skill to create skills
4. **One department at a time** - Don't build everything at once
5. **Test auto-invocation** - Ensure Claude recognizes your components
6. **Iterate** - Update and improve based on real use

The creator emphasizes this is a **living system** - continuously updated based on actual business use.
