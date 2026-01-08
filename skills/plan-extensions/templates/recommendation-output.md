# Recommendation Output Template

Use this format when presenting capability recommendations to users.

---

## Capability Recommendation

### Summary

**Total components recommended:** [N]

| Type | Count |
|------|-------|
| Skills | [X] |
| Subagents | [Y] |
| Commands | [Z] |
| claude.md additions | [W] |

---

### Skills ([X] total)

#### 1. [skill-name]

| Field | Value |
|-------|-------|
| **Description** | [What it does and when to use it - third person] |
| **Rationale** | [Which decision/test led here] |
| **Complexity** | [Simple (single file) / Complex (router pattern)] |

**Suggested structure:**
[If complex, list expected workflows. If simple, note "single SKILL.md file"]

---

#### 2. [skill-name]
[Repeat format]

---

### Subagents ([Y] total)

#### 1. [subagent-name]

| Field | Value |
|-------|-------|
| **Description** | [What it does - when to invoke it] |
| **Rationale** | [Why isolation/persona is needed] |
| **Suggested tools** | [Limited tool list or "inherit all"] |
| **Model** | [sonnet/haiku/opus/inherit] |

---

### Commands ([Z] total)

#### 1. /[command-name]

| Field | Value |
|-------|-------|
| **Description** | [What it triggers] |
| **Arguments** | [Expected arguments or "none"] |
| **Rationale** | [Why command vs skill] |

---

### claude.md Additions ([W] total)

#### 1. [Section name]

| Field | Value |
|-------|-------|
| **Content summary** | [Brief description of what to add] |
| **Location** | [Project `.claude/` or user `~/.claude/`] |
| **Rationale** | [Why claude.md vs skill/command] |

---

### Dependencies

[Describe relationships between components, if any]

- [Component A] requires [Component B] to exist first
- [Component C] and [Component D] are independent

---

### Suggested Build Order

1. **[First component]** - [Why first: foundation, dependency, etc.]
2. **[Second component]** - [Relationship to first]
3. **[Third component]** - [Relationship to previous]
...

---

### Next Steps

Ready to proceed? Options:

1. **Start building [first component]** - Invoke the appropriate create-* skill
2. **Adjust recommendations** - Modify scope, split/combine, or change types
3. **Get more details** - Deep dive on a specific recommendation
4. **See the decision rationale** - Explain why each recommendation was made
