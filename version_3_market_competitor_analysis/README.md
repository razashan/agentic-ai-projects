# Competitive Market Analysis System

## Overview

A sophisticated multi-agent system that generates comprehensive competitive analysis reports. Users input a company name, and the system automatically:

1. **Identifies 5 Major Competitors** - Uses market analysis to find direct competitors
2. **Analyzes Each Competitor** - Conducts in-depth research in parallel (5 agents simultaneously)
3. **Creates SWOT Analysis** - Synthesizes findings into strategic SWOT matrices
4. **Generates HTML Report** - Produces a professional, interactive HTML report

## Architecture

### Agent Pipeline (Sequential + Parallel)

```
User Input (Company Name)
    ↓
competitor_identifier_agent (Finds 5 competitors)
    ↓
5x Parallel competitor_analyzer_agents (Each analyzes one competitor)
    ↓
swot_analyzer_agent (Synthesizes SWOT analysis)
    ↓
report_generator_agent (Creates HTML report)
    ↓
Output: Professional HTML Report
```

## Agents

### 1. competitor_identifier_agent
- **Input:** Company name from user
- **Task:** Identify top 5 direct competitors
- **Output:** List of 5 competitor names with market positioning

### 2. competitor_analyzer_agent (x5, runs in parallel)
- **Input:** Individual competitor name from identifier
- **Task:** Deep competitive analysis
- **Output:** Detailed competitor profile including strengths, weaknesses, strategies

### 3. swot_analyzer_agent
- **Input:** All 5 competitor analyses
- **Task:** Create SWOT matrices and comparative analysis
- **Output:** Strategic SWOT analysis and market opportunity identification

### 4. report_generator_agent
- **Input:** SWOT analysis and all competitive data
- **Task:** Generate professional HTML report
- **Output:** Interactive HTML competitive analysis report

## Data Flow

Each agent receives relevant data from previous agents via state keys:
- `competitor_identifier_output` → List of competitors
- `competitor_analyzer_output` → Individual competitor analyses
- `swot_analyzer_output` → Strategic SWOT analysis
- `report_generator_output` → Final HTML report

## Setup

### Prerequisites
- Python 3.11+
- Google ADK framework
- Google API key

### Installation

```bash
# Clone the repository
git clone https://github.com/theailanguage/adk_samples.git
cd version_3_market_competitor_analysis

# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Set up API key
# Create .env file in project root
echo "GOOGLE_API_KEY=your-api-key" > .env
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> .env
```

## Running the System

```bash
# Start the ADK web interface
adk web ./agents

# Or run programmatically
python main.py
```

## Example Usage

Input:
```
Company: Apple
```

The system will:
1. Identify competitors: Samsung, Microsoft, Google, Amazon, Meta
2. Analyze each competitor's market position, products, strategy
3. Create SWOT matrices comparing all competitors
4. Generate a comprehensive HTML report with visualizations

Output:
```
output/260108_143022_competitive_analysis_report.html
```

## Output Features

The generated HTML report includes:
- Executive Summary
- Competitive Landscape Overview
- Individual Competitor Profiles
- Comparative Analysis Tables
- Color-coded SWOT Matrices
- Market Positioning Analysis
- Strategic Recommendations
- Interactive Elements

## Key Technologies

- **Google ADK Framework:** Agent orchestration
- **Gemini 2.5 Flash:** LLM for all analysis
- **Sequential + Parallel Agents:** Efficient processing
- **HTML/CSS:** Professional report generation

## Future Enhancements

- Real-time market data integration
- Financial metrics comparison
- Social media sentiment analysis
- Patent and innovation tracking
- Revenue and growth analysis
- Customer review analysis

## License

MIT

## Support

For issues and questions, visit the repository or contact the maintainers.
