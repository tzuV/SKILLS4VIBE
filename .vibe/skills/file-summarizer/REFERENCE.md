# File Summarizer - Reference Guide

## Template Syntax

### Basic Structure

Custom templates use a simple placeholder syntax with double curly braces:

```markdown
# Summary: {{name}}

Generated: {{timestamp}}
Source: {{path}}
Total Files: {{file_count}}
Total Size: {{total_size}}

## Structure
{{structure_tree}}

## File Details
{{file_details}}

## Statistics
{{statistics}}
```

### Available Placeholders

#### Metadata
- `{{name}}` - Name of the summarized item (filename or folder name)
- `{{timestamp}}` - Generation timestamp (ISO format)
- `{{path}}` - Source path
- `{{file_count}}` - Total number of files
- `{{total_size}}` - Total size in human-readable format
- `{{elapsed_time}}` - Time taken to generate summary

#### Structure
- `{{structure_tree}}` - ASCII tree representation of folder structure
- `{{structure_depth}}` - Maximum depth of the structure

#### File Details
- `{{file_details}}` - Complete file details section
- `{{file_list}}` - Simple list of all files
- `{{file_table}}` - Markdown table of files with metadata

#### Statistics
- `{{statistics}}` - Complete statistics section
- `{{loc}}` - Total lines of code
- `{{code_lines}}` - Lines of actual code (excluding comments/blanks)
- `{{comment_lines}}` - Lines of comments
- `{{blank_lines}}` - Blank lines
- `{{file_type_distribution}}` - Breakdown by file type

#### Code Analysis (for codebases)
- `{{dependencies}}` - List of dependencies
- `{{imports}}` - Import statements found
- `{{exports}}` - Export statements found
- `{{functions}}` - Functions defined
- `{{classes}}` - Classes defined
- `{{code_complexity}}` - Complexity metrics

#### Relationships
- `{{dependency_graph}}` - ASCII representation of file dependencies
- `{{import_map}}` - Map of which files import from which

### Conditional Sections

Use `{{#if condition}}...{{/if}}` for conditional content:

```markdown
{{#if is_codebase}}
## Code Analysis
- Functions: {{functions}}
- Classes: {{classes}}
{{/if}}

{{#if has_dependencies}}
## Dependencies
{{dependencies}}
{{/if}}
```

Available conditions:
- `is_codebase` - True if source contains code files
- `has_dependencies` - True if dependencies were detected
- `is_folder` - True if summarizing a folder
- `is_single_file` - True if summarizing a single file
- `has_errors` - True if any files couldn't be read

### Looping

Use `{{#each items}}...{{/each}}` for iterating over collections:

```markdown
## Key Files
{{#each key_files}}
### {{name}}
- Size: {{size}}
- Lines: {{lines}}
- Description: {{description}}
{{/each}}
```

### Formatting Helpers

- `{{format_size bytes}}` - Convert bytes to human-readable (KB, MB, GB)
- `{{format_number num}}` - Format number with commas
- `{{truncate text 50}}` - Truncate text to 50 characters
- `{{uppercase text}}` - Convert to uppercase
- `{{lowercase text}}` - Convert to lowercase
- `{{date format}}` - Format timestamp (use `YYYY-MM-DD`, `HH:mm:ss`, etc.)

## Command Line Options

### Filtering Files

| Option | Description | Example |
|--------|-------------|---------|
| `--include` | File patterns to include | `--include=*.py,*.js` |
| `--exclude` | File patterns to exclude | `--exclude=*.log,*.tmp` |
| `--max-size` | Maximum file size to process | `--max-size=1MB` |
| `--min-size` | Minimum file size to process | `--min-size=1KB` |
| `--depth` | Maximum folder depth to scan | `--depth=3` |

### Output Control

| Option | Description | Example |
|--------|-------------|---------|
| `--output` | Output file path | `--output=custom.md` |
| `--no-save` | Don't save to file, only display | `--no-save` |
| `--template` | Custom template file | `--template=my_template.md` |
| `--append` | Append to existing summary | `--append` |

### Analysis Options

| Option | Description | Example |
|--------|-------------|---------|
| `--code-analysis` | Perform code analysis | `--code-analysis` |
| `--dependency-map` | Generate dependency map | `--dependency-map` |
| `--ignore-gitignore` | Don't respect .gitignore | `--ignore-gitignore` |
| `--follow-symlinks` | Follow symbolic links | `--follow-symlinks` |

### Display Options

| Option | Description | Example |
|--------|-------------|---------|
| `--verbose` | Show detailed progress | `--verbose` |
| `--quiet` | Minimal output | `--quiet` |
| `--no-visuals` | Skip visual elements | `--no-visuals` |
| `--no-stats` | Skip statistics | `--no-stats` |

## File Type Detection

The skill automatically detects and handles these file types:

### Code Files
- **Python**: `.py`, `.pyw`, `.pyx`, `.pyd`
- **JavaScript**: `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs`
- **Java**: `.java`
- **C/C++**: `.c`, `.cpp`, `.cc`, `.cxx`, `.h`, `.hpp`
- **C#**: `.cs`
- **Ruby**: `.rb`, `.rbw`
- **PHP**: `.php`, `.php5`, `.phtml`
- **Go**: `.go`
- **Rust**: `.rs`
- **Swift**: `.swift`
- **Kotlin**: `.kt`, `.kts`
- **Shell**: `.sh`, `.bash`, `.zsh`
- **SQL**: `.sql`

### Markup/Documentation
- **Markdown**: `.md`, `.markdown`
- **HTML**: `.html`, `.htm`, `.xhtml`
- **XML**: `.xml`
- **JSON**: `.json`
- **YAML**: `.yaml`, `.yml`
- **TOML**: `.toml`

### Configuration
- **INI**: `.ini`, `.cfg`, `.conf`
- **Properties**: `.properties`
- **Docker**: `Dockerfile`, `.dockerignore`, `docker-compose.yml`
- **Git**: `.gitignore`, `.gitattributes`, `.gitmodules`
- **EditorConfig**: `.editorconfig`
- **ESLint**: `.eslintrc`, `.eslintignore`
- **Prettier**: `.prettierrc`

### Data Files
- **CSV**: `.csv`
- **TSV**: `.tsv`
- **TOML**: `.toml`
- **INI**: `.ini`

### Binary Files (excluded by default)
- Images: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`, `.ico`
- Archives: `.zip`, `.tar`, `.gz`, `.rar`, `.7z`
- Executables: `.exe`, `.dll`, `.so`, `.dylib`
- Databases: `.db`, `.sqlite`, `.sqlite3`

## ASCII Art Styles

The skill supports different styles for visual representations.

### Tree Styles

**Default (Unicode):**
```
project/
├── src/
│   ├── index.js
│   └── utils/
│       └── helper.js
└── README.md
```

**ASCII-only:**
```
project/
+-- src/
|   +-- index.js
|   +-- utils/
|       +-- helper.js
+-- README.md
```

**Compact:**
```
project/src/index.js
project/src/utils/helper.js
project/README.md
```

**Indented:**
```
project/
  src/
    index.js
    utils/
      helper.js
  README.md
```

### Progress Bar Styles

**Block:** `▰▰▰▰▰▰▰▰▱▱▱▱▱▱ 70%`

**Simple:** `[==========          ] 50%`

**Detailed:** `[▓▓▓▓▓▓▓▓▓▓░░░░░░░░] 45% (9/20 files)`

### Chart Styles

**Bar Chart:**
```
.py    ████████████████ 12 files (40%)
.js    ████████████        8 files (27%)
.md    ████████            5 files (17%)
.json  ████                3 files (10%)
.other ██                  2 files (6%)
```

**Histogram:**
```
12 | ██
10 | ██
 8 | ████
 6 | ██████
 4 | ████████
 2 | ██████████
  0 +------------------
     .py  .js  .md .json
```

## Incremental Updates

For previously summarized folders, the skill can perform incremental analysis:

### Change Detection
- Compares file modification timestamps
- Detects new, modified, and deleted files
- Calculates change percentage

### Update Modes

**Full Update:**
- Re-analyze all files
- Generate complete new summary
- Mark changes from previous summary

**Partial Update:**
- Only analyze changed files
- Update relevant sections
- Preserve unchanged content

**Diff Mode:**
- Generate a diff-style summary
- Show only what changed
- Highlight additions and removals

### Version Tracking

Each summary includes:
- `Previous Summary`: Link to last summary (if exists)
- `Changes Since`: Timestamp of last summary
- `Files Changed`: Count of modified files
- `New Files`: Count of new files
- `Deleted Files`: Count of deleted files

## Error Handling

### File Access Errors
- Permission denied: Skip and log warning
- File not found: Skip and notify user
- Encoding issues: Attempt fallback encodings

### Size Limits
- Default max file size: 10MB
- Default max total size: 1GB
- Configurable via command line options

### Timeout
- Default timeout: 30 seconds per file
- Configurable via `--timeout` option

### Recovery
- Partial summaries are saved on error
- Error details included in summary
- User can retry with adjusted options

## Performance Optimization

### Caching
- File content cached by path + modification time
- Metadata cached separately
- Cache invalidated on file change

### Parallel Processing
- Files processed in parallel (default: 4 workers)
- Configurable via `--workers` option
- Automatic throttling based on system resources

### Memory Management
- Large files processed in chunks
- Streaming for files > 100MB
- Garbage collection between files

## Security Considerations

### Safe Paths
- Resolves paths relative to project root
- Prevents directory traversal attacks
- Validates all paths before access

### Sensitive Data
- Skips files matching patterns:
  - `*.env`
  - `*.secret`
  - `*.key`
  - `*.pem`
  - `.git/` (by default)
  - `.vibe/` (by default)
- Configurable via `--exclude` option

### Output Sanitization
- Escapes special characters in output
- Prevents markdown injection
- Validates filenames for output

## Integration with Other Skills

The file-summarizer skill can be combined with other skills:

### With `clean-lean-coder`
- Summarize codebase structure before refactoring
- Identify code smells in summary
- Track refactoring progress

### With `improve-codebase`
- Generate baseline summary for improvement analysis
- Compare before/after states
- Visualize architectural changes

### With `diagnosis`
- Summarize files related to a bug
- Include error locations in summary
- Track debugging progress

### With `prototype`
- Summarize prototype files
- Document prototype structure
- Generate prototype documentation

## Examples

### Basic Usage
```bash
# Summarize current folder
skill:file-summarizer

# Summarize specific folder
skill:file-summarizer --path=src/

# Summarize specific files
skill:file-summarizer --files=index.js,main.py
```

### Advanced Usage
```bash
# Summarize with code analysis and dependency map
skill:file-summarizer --path=src/ --code-analysis --dependency-map

# Summarize only Python and JavaScript files
skill:file-summarizer --path=. --include=*.py,*.js

# Summarize excluding test files
skill:file-summarizer --path=. --exclude=*test*,*spec*

# Use custom template
skill:file-summarizer --path=. --template=my_template.md

# Generate ASCII-only output
skill:file-summarizer --path=. --no-visuals --tree-style=ascii
```

### With Custom Template

Create `my_template.md`:
```markdown
# Project Analysis: {{name}}

## Quick Stats
- Files: {{file_count}}
- Size: {{total_size}}
- LOC: {{loc}}

## Breakdown
{{file_type_distribution}}

## Key Files
{{#each key_files}}
### {{name}}
- Lines: {{lines}}
- Complexity: {{complexity}}
{{/each}}
```

Then run:
```bash
skill:file-summarizer --template=my_template.md
```
