---
name: file-summarizer
description: Scan files or folders and generate comprehensive markdown summaries with visual representations. Use when user wants to summarize codebases, documentation, or file collections, or mentions "summarize files", "folder summary", or "scan and explain".
---

# File Summarizer

## Quick start

Activate this skill when you need to understand the content and structure of files or folders. It will:
1. Ask you which files or folders to analyze
2. Scan the specified location(s)
3. Generate a comprehensive summary with visual hierarchy
4. Save the result as `summary_[timestamp].md` in `/Summarizer/`

**Example invocation:**
- "summarize this folder"
- "can you scan these files and explain them?"
- "create a summary of the project structure"

## Workflows

### Single File Summary
1. User activates skill or requests file summary
2. Skill asks: "Which file(s) should I summarize?"
3. User provides file path(s)
4. Skill reads and analyzes the file(s)
5. Skill generates summary with:
   - File metadata (size, type, last modified)
   - Content overview
   - Key sections with visual hierarchy
   - Code structure (if applicable)
   - Dependency map (if applicable)
6. Saves to `/Summarizer/summary_[filename]_[timestamp].md`

### Folder Summary
1. User activates skill or requests folder summary
2. Skill asks: "Which folder should I scan?"
3. User provides folder path
4. Skill recursively scans the folder (respecting .gitignore)
5. Skill generates summary with:
   - Folder structure tree
   - File count and types breakdown
   - Total lines of code (if codebase)
   - Key files identified
   - Visual hierarchy diagram (ASCII tree)
   - Content summaries of significant files
6. Saves to `/Summarizer/summary_[foldname]_[timestamp].md`

### Multi-File Summary
1. User activates skill with multiple files
2. Skill asks: "Which files should I include?" (accepts glob patterns)
3. User provides list or pattern (e.g., `*.py`, `src/**/*.js`)
4. Skill analyzes all matching files
5. Skill generates unified summary with:
   - Common patterns across files
   - Shared dependencies
   - File relationship map
   - Aggregated statistics
6. Saves to `/Summarizer/summary_[pattern]_[timestamp].md`

## Summary Format

All summaries follow this structure:

```markdown
# Summary: [Name]

**Generated:** [Timestamp]  
**Source:** [Path]  
**Total Files:** [Count]  
**Total Size:** [Size]

## 📊 Overview
[Brief description of what was analyzed]

## 🗂️ Structure
```
[ASCII tree representation]
```

## 📄 File Details
### [File 1]
- **Path:** [relative path]
- **Type:** [file type]
- **Size:** [size]
- **Key Contents:**
  [Bullet points of important sections]

### [File 2]
... 

## 🔗 Relationships
[Visual representation of file dependencies/relationships]

## 📈 Statistics
- Total lines: [count]
- Code lines: [count]
- Comment lines: [count]
- [Other relevant metrics]

## 🎯 Key Findings
[3-5 bullet points highlighting most important aspects]
```

## Visual Elements

The skill incorporates these visual representations:

### ASCII Trees
```
project/
├── src/
│   ├── index.js
│   └── utils/
│       └── helper.js
├── tests/
│   └── index.test.js
└── README.md
```

### Progress Indicators
- `▰▰▰▰▰▰▰▰▱▱▱▱▱▱ 70%` for scanning progress
- `✓` for completed files
- `✗` for errors

### Statistics Bars
```
File Types:
▰▰▰▰▰▰▰▰▰▰▰▰ .py    12 files (40%)
▰▰▰▰▰▰▰▰▱▱▱▱▱ .js     8 files (27%)
▰▰▰▰▰▱▱▱▱▱▱▱▱ .md     5 files (17%)
▰▰▱▱▱▱▱▱▱▱▱▱▱ .json   3 files (10%)
▱▱▱▱▱▱▱▱▱▱▱▱ .other   2 files (6%)
```

## Output Location

All summaries are saved to:
```
[project-root]/Summarizer/summary_[name]_[YYYYMMDD_HHMMSS].md
```

The `Summarizer` folder is created automatically if it doesn't exist.

## Advanced Features

### Filtering
Users can specify:
- File extensions to include (`--include=*.py,*.js`)
- File extensions to exclude (`--exclude=*.log,*.tmp`)
- Maximum file size (`--max-size=1MB`)
- Maximum depth for folder scanning (`--depth=3`)

### Custom Templates
Users can provide a custom summary template file. The skill will use the template structure and populate it with the analyzed data.

### Incremental Updates
For previously summarized folders, the skill can:
- Identify changed files
- Update only modified sections
- Highlight new additions

See [REFERENCE.md](REFERENCE.md) for template syntax and advanced options.
