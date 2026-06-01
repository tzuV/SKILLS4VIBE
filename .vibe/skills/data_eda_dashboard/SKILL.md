---
name: data_eda_dashboard
description: A skill to scan folders for data files (CSV, JSON, etc.), detect relationships, merge or combine datasets, and generate a comprehensive EDA dashboard with visualizations tailored to data types.
---

# Data EDA Dashboard Vibe Skill

## Instructions
This skill guides **you** to:
- **Scan** a specified folder and its subfolders for data files (CSV, JSON, etc.).
- **Load** all detected data files into memory.
- **Detect relationships** among the datasets by comparing column names and indices.
- **Merge datasets** on a common index or a user-specified column if relationships exist.
- **Combine datasets** into a single dataset if no relationships are found.
- **Generate a comprehensive EDA dashboard** with visualizations and summary statistics tailored to the data types:
  - **Numeric**: Histograms, box plots, scatter plots, summary statistics (mean, median, std, etc.).
  - **String/Categorical**: Word counts, word clouds, bar plots of top terms, unique value counts.
  - **Date/Time**: Time series plots, distribution of events over time.
- **Output** Python scripts for loading, merging, and visualizing the data, as well as a dashboard script to display the EDA results.

The agent ensures the process is interactive, transparent, and results in clean, reusable Python code.

---

## Agent Behavior
1. **Interactive Clarity:** The agent asks follow-up questions to clarify the folder structure, data types, and user preferences for merging or visualizations.
2. **Reasoning Transparency:** For every step (e.g., merging, visualization choice), the agent explains its logic (e.g., "Merging on 'user_id' because it is the only common column").
3. **Code Quality:** The generated Python files are modular, well-commented, and use best practices (e.g., `pandas` for data handling, `matplotlib/seaborn` for visualizations).
4. **Dashboard Focus:** The final dashboard is a standalone HTML file (using `plotly` or `streamlit`) for easy sharing and interactivity.

---

## Q&A Flow

### Phase 1: Folder and Data Discovery
**Agent:** *"What is the root folder path to scan for data files? (e.g., './data')"*
**Agent Reasoning:** *"The root folder path determines where the agent will look for subfolders and data files. Ensure the path is correct and accessible."*
**Your Answer:**

**Agent:** *"What data file types should be included? (Default: CSV, JSON. Add others if needed, e.g., Excel, Parquet)"*
**Agent Reasoning:** *"Specifying file types ensures the agent only loads relevant data. For example, excluding log files or temporary files."*
**Your Answer:**

---

### Phase 2: Data Loading and Inspection
**Agent:** *"Should the agent preview the first few rows of each loaded dataset for your review? (Y/N)"*
**Agent Reasoning:** *"Previewing the data helps you confirm that the correct files are loaded and the structure is as expected."*
**Your Answer:**

**Agent:** *"Are there any files or folders to exclude from the scan? (e.g., 'temp/', 'backup_*')"*
**Agent Reasoning:** *"Excluding irrelevant files/folders speeds up the process and avoids errors."*
**Your Answer:**

---

### Phase 3: Relationship Detection and Merging
**Agent:** *"The agent has detected the following datasets: [List of file names and their columns]. Do you want to check for relationships between them? (Y/N)"*
**Agent Reasoning:** *"Checking for relationships (e.g., common columns like 'id' or 'timestamp') allows the agent to merge datasets meaningfully."*
**Your Answer:**

**Agent:** *"The following common columns were found: [List of columns]. Should the agent merge the datasets on one of these columns? If yes, specify which one (or 'index' for merging on index). If no, the datasets will be combined into a single dataset."*
**Agent Reasoning:** *"Merging on a common column (e.g., 'user_id') preserves relationships between datasets. Combining without merging is useful for unrelated but complementary data."*
**Your Answer:**

---

### Phase 4: EDA and Visualization Preferences
**Agent:** *"For numeric columns, which visualizations should be included? (Default: histograms, box plots, summary statistics. Add/remove as needed)"*
**Agent Reasoning:** *"Numeric data benefits from distribution visualizations (histograms, box plots) and summary statistics to understand central tendency and spread."*
**Your Answer:**

**Agent:** *"For string/categorical columns, which visualizations should be included? (Default: word counts, word clouds, bar plots of top terms, unique value counts)"*
**Agent Reasoning:** *"String data is best explored with frequency-based visualizations (e.g., word clouds for open-ended text, bar plots for categories)."*
**Your Answer:**

**Agent:** *"For date/time columns, which visualizations should be included? (Default: time series plots, event distributions)"*
**Agent Reasoning:** *"Date/time data is ideal for trend analysis and event distribution over time."*
**Your Answer:**

**Agent:** *"Should the dashboard include interactive visualizations (using `plotly`) or static images (using `matplotlib/seaborn`)? (Default: interactive)"*
**Agent Reasoning:** *"Interactive visualizations allow users to hover for details and zoom, while static images are simpler to embed in reports."*
**Your Answer:**

---
### Phase 5: Dashboard Generation
**Agent:** *"What should be the output format for the dashboard? (Default: Standalone HTML file. Alternatives: Streamlit app, Jupyter Notebook)"*
**Agent Reasoning:** *"Standalone HTML is portable and easy to share. Streamlit apps are interactive but require running a server. Notebooks are useful for further exploration."*
**Your Answer:**

**Agent:** *"Should the dashboard include a summary report (e.g., data quality issues, missing values, outliers)? (Y/N)"*
**Agent Reasoning:** *"A summary report provides actionable insights, such as missing values or outliers, to guide data cleaning or analysis."*
**Your Answer:**

---
### Phase 6: Code Output
**Agent:** *"The agent will now generate the following Python files:
1. `data_loader.py`: Scans folders, loads data files, and returns a list of DataFrames.
2. `data_merger.py`: Detects relationships and merges/combines datasets as specified.
3. `eda_visualizer.py`: Generates visualizations and summary statistics for each data type.
4. `dashboard.py`: Creates a dashboard (HTML/Streamlit) to display the EDA results.

Should the agent proceed with generating these files? (Y/N)"*
**Agent Reasoning:** *"These files are modular and reusable. Each file has a single responsibility, making the code easy to maintain and extend."*
**Your Answer:**

---
## Example Workflow
1. User specifies `./data` as the root folder.
2. Agent scans and loads all CSV/JSON files in `./data` and subfolders.
3. Agent detects that `users.csv` and `orders.csv` both have a `user_id` column.
4. User chooses to merge on `user_id`.
5. Agent generates visualizations:
   - Histograms and box plots for numeric columns (`age`, `order_amount`).
   - Word clouds and bar plots for string columns (`product_name`, `user_feedback`).
   - Time series plots for date columns (`order_date`).
6. Agent creates a standalone HTML dashboard with all visualizations and summary statistics.
7. Agent outputs the Python files for reuse.

---
## Example Compressed Output
The agent will create the following files in the specified folder:

### `data_loader.py`
```python
import os
import pandas as pd
from pathlib import Path

def load_data_files(root_folder, file_types=['.csv', '.json']):
    """Load all data files of specified types from root_folder and subfolders."""
    data_frames = {}
    for root, _, files in os.walk(root_folder):
        for file in files:
            if Path(file).suffix.lower() in file_types:
                file_path = os.path.join(root, file)
                try:
                    if file.endswith('.csv'):
                        df = pd.read_csv(file_path)
                    elif file.endswith('.json'):
                        df = pd.read_json(file_path, lines=True)
                    data_frames[file] = df
                    print(f"Loaded: {file_path}")
                except Exception as e:
                    print(f"Failed to load {file_path}: {e}")
    return data_frames

if __name__ == "__main__":
    root_folder = input("Enter root folder path: ")
    file_types = input("Enter file types (comma-separated, e.g., .csv,.json): ").split(",")
    data = load_data_files(root_folder, file_types)
    print(f"Loaded {len(data)} files.")