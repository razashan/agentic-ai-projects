# 📁 Project File Structure

```
version_3_market_competitor_analysis/
│
├── 📄 README.md                          # Complete system documentation
├── 📄 SETUP_COMPLETE.md                  # Setup verification & instructions
├── 📄 agent_flow_diagram.md              # Visual architecture diagram
├── 📄 main.py                            # Entry point script
├── 📄 pyproject.toml                     # Project dependencies
│
├── 📁 agents/
│   ├── __init__.py
│   │
│   ├── 📁 competitor_identifier/         # Agent 1: Identifies competitors
│   │   ├── __init__.py
│   │   ├── agent.py                      # Agent definition
│   │   ├── instructions.txt              # Agent instructions
│   │   └── description.txt               # Agent description
│   │
│   ├── 📁 competitor_analyzer/           # Agent 2: Analyzes competitors (x5 parallel)
│   │   ├── __init__.py
│   │   ├── agent.py                      # Agent definition
│   │   ├── instructions.txt              # Agent instructions
│   │   └── description.txt               # Agent description
│   │
│   ├── 📁 swot_analyzer/                 # Agent 3: Creates SWOT analysis
│   │   ├── __init__.py
│   │   ├── agent.py                      # Agent definition
│   │   ├── instructions.txt              # Agent instructions
│   │   └── description.txt               # Agent description
│   │
│   ├── 📁 report_generator/              # Agent 4: Generates HTML report
│   │   ├── __init__.py
│   │   ├── agent.py                      # Agent definition
│   │   ├── instructions.txt              # Agent instructions
│   │   └── description.txt               # Agent description
│   │
│   └── 📁 root_report_builder/           # Orchestrator agent
│       ├── __init__.py
│       ├── agent.py                      # Sequential orchestration logic
│       └── description.txt               # Root description
│
├── 📁 tools/
│   ├── __init__.py
│   └── file_writer_tool.py               # Tool: Writes HTML reports to file
│
├── 📁 utils/
│   ├── __init__.py
│   └── file_loader.py                    # Utility: Loads instruction files
│
└── 📁 output/                            # Generated reports (created at runtime)
    └── [timestamp]_competitive_analysis_report.html
```

## 📊 Agent Responsibilities

```
user_input (Company Name)
    ↓
┌─────────────────────────────────────────┐
│ competitor_identifier_agent             │
│ • Analyzes company information          │
│ • Identifies 5 major competitors        │
│ Output: List of competitors             │
└────────┬────────────────────────────────┘
         ↓
    ┌────────────────────────────────────────┐
    │ 5x competitor_analyzer_agent (parallel)│
    ├────────────────────────────────────────┤
    │ Agent 1: Analyzes Competitor 1         │
    │ Agent 2: Analyzes Competitor 2         │
    │ Agent 3: Analyzes Competitor 3         │
    │ Agent 4: Analyzes Competitor 4         │
    │ Agent 5: Analyzes Competitor 5         │
    │                                         │
    │ Each generates:                        │
    │ • Market position                      │
    │ • Strengths & weaknesses               │
    │ • Product strategy                     │
    │ • Target audience                      │
    │ • Competitive advantages               │
    └────────┬─────────────────────────────┘
             ↓
┌─────────────────────────────────────────┐
│ swot_analyzer_agent                     │
│ • Aggregates all competitor data        │
│ • Creates SWOT matrices                 │
│ • Identifies market opportunities       │
│ Output: Strategic SWOT analysis         │
└────────┬────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ report_generator_agent                  │
│ • Synthesizes all intelligence          │
│ • Creates professional HTML             │
│ • Generates visualizations              │
│ • Formats for stakeholders              │
│ Output: HTML report file                │
└────────┬────────────────────────────────┘
         ↓
    Final Report (HTML)
```

## 🔄 Data Flow Through State Keys

```
┌──────────────────────────────────┐
│ State: competitor_identifier_    │
│        output                    │
│                                  │
│ ["Samsung", "Microsoft",         │
│  "Google", "Amazon", "Meta"]     │
└────────────┬─────────────────────┘
             │
             ├─────┬─────┬─────┬─────┐
             ↓     ↓     ↓     ↓     ↓
        ┌────────────────────────────┐
        │ competitor_analyzer_output │
        │                            │
        │ [                          │
        │   {name: Samsung,          │
        │    analysis: {...}},       │
        │   {name: Microsoft,        │
        │    analysis: {...}},       │
        │   ... (5 total)            │
        │ ]                          │
        └────────┬───────────────────┘
                 │
         ┌───────▼─────────┐
         │ swot_analyzer_  │
         │ output          │
         │                 │
         │ {               │
         │   swot_matrix,  │
         │   comparative,  │
         │   opportunities │
         │ }               │
         └────────┬────────┘
                  │
         ┌────────▼──────────┐
         │ report_generator_ │
         │ output            │
         │                   │
         │ <HTML Report>     │
         └───────────────────┘
```

## 📝 Key Files Explained

| File | Purpose |
|------|---------|
| `agent.py` | Defines LlmAgent with model, instructions, tools, output_key |
| `instructions.txt` | Detailed prompt for the agent's behavior |
| `description.txt` | Brief description of agent's role |
| `file_writer_tool.py` | Saves HTML files with timestamps |
| `file_loader.py` | Loads .txt instruction files |
| `root_report_builder/agent.py` | SequentialAgent + ParallelAgent orchestration |

## 🎯 Execution Flow

1. **User provides company name**
2. **root_agent starts SequentialAgent**
3. **Stage 1:** competitor_identifier finds competitors
4. **Stage 2:** ParallelAgent launches 5 analyzers simultaneously
5. **Stage 3:** swot_analyzer synthesizes all data
6. **Stage 4:** report_generator creates HTML
7. **Output:** File saved to `output/[timestamp]_competitive_analysis_report.html`

---

## ⚡ Performance Metrics

- **Sequential agents:** 3 (identifier, swot, report)
- **Parallel agents:** 5 (concurrent analysis)
- **Total execution time:** ~60-90 seconds
- **Output file size:** ~2-5 MB
- **API calls:** ~6-7 per run
