---
name: extract
description: Extract value units from existing content using the 4-filter framework
argument-hint: "[source-type] [source-path-or-paste]"
---

# /extract Command

Mine existing content for standalone value units that solve specific problems.

## Usage

```
/extract video transcript.txt
/extract course module-3
/extract podcast [paste transcript]
/extract [paste content directly]
```

## What This Does

1. Analyzes the source content
2. Identifies potential value units (problem-solution segments)
3. Runs each through 4 filters:
   - Problem Identification
   - Standalone Test
   - Iceberg Alignment
   - Demand Signal
4. Documents passing units with full specs
5. Classifies by type and temperature
6. Recommends best formats and priorities

## Process

Invoke the `extract-content-ideas` skill with workflow: extract-from-source

Then offer to classify results if user wants.

## Output

- Extraction analysis with all identified units
- Value unit cards for each passing unit
- Priority recommendations
- Content mix analysis

## Quick Options

After extraction, offer:
- `/extract classify` - Classify units by type/temperature
- `/extract audit` - Audit quality of extracted units
