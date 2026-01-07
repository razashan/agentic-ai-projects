# Competitive Market Analysis System - Agent Flow Diagram

## Complete System Architecture

```mermaid
flowchart TD
    USER["👤 User Input<br/>Company Name"]
    ROOT["🎯 root_report_builder<br/>Sequential Orchestrator"]
    
    subgraph PIPELINE ["4-Stage Analysis Pipeline"]
        direction LR
        CI["1️⃣ competitor_identifier<br/>Finds 5 Competitors"]
        
        subgraph PARALLEL ["⚡ 5-Agent Parallel Analysis"]
            direction TB
            CA1["competitor_analyzer_1<br/>Analyzes Competitor 1"]
            CA2["competitor_analyzer_2<br/>Analyzes Competitor 2"]
            CA3["competitor_analyzer_3<br/>Analyzes Competitor 3"]
            CA4["competitor_analyzer_4<br/>Analyzes Competitor 4"]
            CA5["competitor_analyzer_5<br/>Analyzes Competitor 5"]
        end
        
        SA["3️⃣ swot_analyzer<br/>Creates SWOT Matrices"]
        RG["4️⃣ report_generator<br/>Generates HTML Report"]
    end
    
    OUTPUT["📊 Final Output<br/>HTML Report"]
    
    USER --> ROOT
    ROOT --> PIPELINE
    CI --> CA1
    CI --> CA2
    CI --> CA3
    CI --> CA4
    CI --> CA5
    CA1 --> SA
    CA2 --> SA
    CA3 --> SA
    CA4 --> SA
    CA5 --> SA
    SA --> RG
    PIPELINE --> OUTPUT
    
    classDef userStyle fill:#e1f5fe,stroke:#01579b,stroke-width:3px,color:#000
    classDef orchestratorStyle fill:#f3e5f5,stroke:#4a148c,stroke-width:3px,color:#000
    classDef agentStyle fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px,color:#000
    classDef parallelStyle fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000
    classDef outputStyle fill:#fce4ec,stroke:#880e4f,stroke-width:3px,color:#000
    classDef pipelineStyle fill:#fff9c4,stroke:#f57f17,stroke-width:3px,color:#000
    
    class USER userStyle
    class ROOT orchestratorStyle
    class CI,SA,RG agentStyle
    class CA1,CA2,CA3,CA4,CA5 parallelStyle
    class OUTPUT outputStyle
    class PIPELINE pipelineStyle
```

## Data Flow

### Stage 1: Competitor Identification
```
User Input: "Apple"
    ↓
competitor_identifier
    ↓
Output: ["Samsung", "Microsoft", "Google", "Amazon", "Meta"]
State Key: competitor_identifier_output
```

### Stage 2: Parallel Competitor Analysis
```
Input: Each competitor name
    ↓
5 Parallel Agents (Simultaneous Analysis)
    ├→ competitor_analyzer_1 analyzes Samsung
    ├→ competitor_analyzer_2 analyzes Microsoft
    ├→ competitor_analyzer_3 analyzes Google
    ├→ competitor_analyzer_4 analyzes Amazon
    └→ competitor_analyzer_5 analyzes Meta
    ↓
Output: 5 Detailed competitor profiles
State Key: competitor_analyzer_output
```

### Stage 3: SWOT Synthesis
```
Input: All 5 competitor analyses
    ↓
swot_analyzer
    ↓
Output: 
  - Individual SWOT matrices
  - Comparative analysis
  - Market opportunities
  - Threat assessment
State Key: swot_analyzer_output
```

### Stage 4: Report Generation
```
Input: SWOT analysis + all competitive data
    ↓
report_generator
    ↓
Output: Professional HTML Report
File: output/[timestamp]_competitive_analysis_report.html
State Key: report_generator_output
```

## Key Features

### 🎯 Sequential Orchestration
- Root agent manages the 4-stage pipeline
- Each agent runs in sequence with data passing

### ⚡ Parallel Processing
- 5 competitor analysis agents run simultaneously
- Reduces total execution time by ~80%
- All results consolidated for SWOT analysis

### 📊 Data Synthesis
- Competitor data flows through state keys
- Each agent processes and enhances the data
- Final report integrates all intelligence

### 🔄 Workflow
```
Identify → Analyze → Synthesize → Report
```

## Agent Specifications

| Agent | Model | Role | Input | Output |
|-------|-------|------|-------|--------|
| competitor_identifier | Gemini 2.5 Flash | Finds 5 competitors | Company name | List of competitors |
| competitor_analyzer | Gemini 2.5 Flash | Deep analysis | Competitor name | Detailed profile |
| swot_analyzer | Gemini 2.5 Flash | Strategic analysis | 5 profiles | SWOT matrices |
| report_generator | Gemini 2.5 Flash | Report creation | SWOT data | HTML report |

## State Flow

```
State["competitor_identifier_output"]
    ↓ (passes to all 5 parallel agents)
State["competitor_analyzer_output"]
    ↓ (aggregated)
State["swot_analyzer_output"]
    ↓
State["report_generator_output"]
    ↓
Final HTML File
```

## Performance Characteristics

- **Sequential Agents:** competitor_identifier, swot_analyzer, report_generator
- **Parallel Agents:** 5x competitor_analyzer (simultaneous)
- **Total Processing:** ~60-90 seconds depending on analysis depth
- **Output:** Single HTML file (~2-5 MB)

---

## Usage in VS Code

1. Install **"Mermaid Preview"** extension
2. Open this file in VS Code
3. Use `Ctrl+Shift+P` → "Mermaid Preview: Open Preview to the Side"
4. The diagram will render beautifully with interactive elements
