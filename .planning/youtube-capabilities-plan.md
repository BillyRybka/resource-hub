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

---

## Alternative Analysis (More Comprehensive)

A second analysis suggested 5 skills covering the full process:

### 1. video-strategy-classifier
**Covers:** Phase 0 (Strategic Purpose)
- Classifies video role (discovery, trust-building, list-building, deep dive, direct promo)
- Maps the problem chain automatically
- Outputs viewer pathway and CTA strategy
- Determines curiosity hook placement for conversion content

**Why critical:** Without this, every other phase lacks strategic direction.

### 2. pattern-bank-analyzer
**Covers:** Phase 1 (Research & Validation)
- Takes outlier data (titles, thumbnails, topics) and extracts patterns
- Identifies repeating power words, structures, thumbnail styles
- Validates topic ideas against iceberg positioning
- Outputs "building blocks" for title/thumbnail creation

**Integration:** Could connect to Get_YouTube_Transcript tool to analyze competitor content.

### 3. youtube-title-thumbnail-generator
**Covers:** Phase 2 + 3 (Title & Thumbnail Strategy)
- Generates 5-7 title options using outlier structures + BENS
- Runs each through checklist automatically
- Generates 3 thumbnail strategy concepts (from 6 proven styles)
- Creates 2 variations of each = 9 concepts with rationale

**Why combined:** Titles and thumbnails are one packaging system.

### 4. video-script-architect
**Covers:** Phase 4 (Content Planning)
- Takes title/thumbnail promise and video purpose
- Builds structure (Hook → Setup → Framework → Implementation → Bridge)
- Scripts opening 15 seconds to validate promise
- Places retention hooks every 2-3 minutes
- Integrates curiosity loops for conversion content

**Integration:** Pulls from brand-voice, audience-avatar.

### 5. video-launch-analyzer
**Covers:** Phase 5 + 6 (Pre-Launch & Post-Launch)
- Generates optimized description with strategic CTA placement
- Maps distribution (playlists, end screens, cross-promotion)
- Provides 3-hour and 7-day check frameworks
- Documents learnings in pattern bank format
- Triggers sequel strategy when performance exceeds benchmarks

---

## Comparison: Minimal vs Comprehensive

| Phase | Minimal Approach | Comprehensive Approach |
|-------|------------------|------------------------|
| Strategy | Reference doc (youtube-monetization-strategy.md) | **Skill:** video-strategy-classifier |
| Research | Manual + reference | **Skill:** pattern-bank-analyzer |
| Packaging | **Skill:** create-video-packaging | **Skill:** youtube-title-thumbnail-generator |
| Scripting | **Skill:** create-video-script (exists) | **Skill:** video-script-architect |
| Launch | **Command:** /launch-video | **Skill:** video-launch-analyzer |
| Analysis | **Skill:** analyze-video-performance | Part of video-launch-analyzer |

**Key Differences:**
1. Comprehensive adds **video-strategy-classifier** (Phase 0) - determines video purpose before anything
2. Comprehensive adds **pattern-bank-analyzer** - Claude helps analyze provided outlier data
3. Comprehensive combines launch + analysis into one skill
4. Minimal treats more as reference docs; Comprehensive makes more skills

**Recommendation:** Start minimal, add strategy-classifier and pattern-bank-analyzer if you find yourself repeatedly needing those steps.

---

## Existing Skills to Leverage

| Skill | What It Covers | Gaps |
|-------|----------------|------|
| audience-avatar | Mike's profile, pain points, desires | Complete |
| brand-voice | Voice identity, writing rules | Complete |
| create-video-script | Script structure, tension-release | Could integrate with video-script-architect ideas |
