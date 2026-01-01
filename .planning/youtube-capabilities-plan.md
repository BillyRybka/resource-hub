# YouTube Capabilities Plan

**Created:** 2025-12-31
**Status:** Ready for implementation

---

## Context

Refined the 41k-token `all-youtube-knowledge.md` into three focused documents:
- `youtube-foundations.md` - Algorithm, metrics, positioning fundamentals
- `youtube-workflow.md` - Repeatable production process (research → refinement)
- `youtube-monetization-strategy.md` - Deep dives, list-building, videos that sell

Ran capability advisor analysis to identify what skills/agents/commands are needed.

---

## Documents Created

| Document | Tokens (est.) | Purpose |
|----------|---------------|---------|
| youtube-foundations.md | ~3k | Strategic reference (algorithm, temperature, positioning) |
| youtube-workflow.md | ~4k | Production process overview |
| youtube-monetization-strategy.md | ~3k | Content strategy for monetization |

---

## Capability Recommendations

### Skills to Build

| Skill | Priority | Purpose | Notes |
|-------|----------|---------|-------|
| **create-video-packaging** | HIGH | Title + Thumbnail creation | BENS framework, 6 thumbnail styles, design principles, 9-thumbnail process |
| **create-video-script** | EXISTS | Script writing | Already built, uses Tension-Release framework |
| **analyze-video-performance** | LOW | Metrics analysis + refinement | Temperature framework, metrics interpretation, sequel strategy |

### Commands to Build

| Command | Priority | Purpose | Notes |
|---------|----------|---------|-------|
| **/launch-video** | MEDIUM | Pre-publish checklist | Split test setup, description optimization, timing |

### Subagents (Optional)

| Subagent | Priority | Purpose | Notes |
|----------|----------|---------|-------|
| **idea-critic** | LOW | Harsh idea evaluation | Different persona, returns verdict. Could be skill workflow instead. |

### Reference Documentation

| Document | Status | Notes |
|----------|--------|-------|
| youtube-foundations.md | DONE | Could add to claude.md or keep standalone |
| youtube-workflow.md | DONE | Coordinates the skills |
| youtube-monetization-strategy.md | DONE | Strategic reference |

---

## The Full Workflow with Capabilities

```
Research (manual + youtube-foundations.md reference)
    ↓
Ideation (use pattern bank → rough topic)
    ↓
create-video-packaging skill (title + thumbnail FIRST)
    ↓
create-video-script skill (script the video)
    ↓
Production (manual, reference youtube-workflow.md)
    ↓
/launch-video command (checklist + publish)
    ↓
Refinement (manual or analyze-video-performance skill)
    ↓
REPEAT
```

---

## Minimum Viable Implementation

**Phase 1 (Start here):**
1. Build `create-video-packaging` skill
2. Build `/launch-video` command
3. Existing `create-video-script` skill already works

**Phase 2 (Later):**
4. Build `analyze-video-performance` skill
5. Consider `idea-critic` subagent

---

## Implementation Notes

### create-video-packaging skill should include:

**Workflows:**
- create-title (BENS framework, pattern-based, checklist)
- create-thumbnail-concepts (6 styles, 3 strategies + variations)
- refine-thumbnail (design principles, feedback integration)

**References:**
- BENS copywriting system
- 6 thumbnail styles
- 8 design guidelines
- 9 common mistakes
- Title checklist
- Thumbnail checklist

**Templates:**
- Title options output
- Thumbnail concept brief
- Split test setup

### /launch-video command should include:

- Title finalization check
- 3 thumbnails ready for split test
- Description template (lead magnet link first)
- End screens configured
- Publish timing guidance
- Split test activation steps

---

## Resume Instructions

To continue this work:
1. Review this plan
2. Read `youtube-workflow.md` for context on the production process
3. Start with `create-video-packaging` skill using `/create-agent-skill`
4. Reference the BENS system and thumbnail sections from `youtube-workflow.md`

---

## Source Material

Original knowledge document: `all-youtube-knowledge.md` (41k tokens)
Existing script skill: `skills/create-video-script/`
