# 🚀 Quick Start Guide - Competitive Market Analysis System

## ⚡ 5-Minute Setup

### Step 1: Get API Key (1 min)
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

### Step 2: Create .env File (1 min)
```bash
# In project root directory, create .env
echo "GOOGLE_API_KEY=your-copied-key" > .env
echo "GOOGLE_GENAI_USE_VERTEXAI=FALSE" >> .env
```

### Step 3: Install Dependencies (2 min)
```bash
# From project root
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv sync
```

### Step 4: Run the System (1 min)
```bash
adk web ./agents
```

---

## 💻 Using the System

### Via Web Interface
1. Open the ADK web interface (typically `http://localhost:8000`)
2. Select **root_report_builder_agent**
3. Enter company name (e.g., "Apple", "Tesla", "Netflix")
4. Click **Run**
5. Wait for analysis to complete (~60-90 seconds)
6. Download the generated HTML report

### Example Inputs
- Apple
- Tesla
- Netflix
- Spotify
- Airbnb
- Uber
- Amazon
- Google

---

## 📊 What You Get

### Report Includes
✅ Top 5 Competitors identified  
✅ Individual competitor analysis  
✅ SWOT matrices for each  
✅ Comparative analysis  
✅ Market opportunities  
✅ Strategic recommendations  
✅ Professional HTML format  

### Report Location
```
output/[DATE]_[TIME]_competitive_analysis_report.html
Example: output/260108_143022_competitive_analysis_report.html
```

---

## 🔍 Understanding the Flow

```
You enter: "Apple"
    ↓ (10s)
System finds: Samsung, Microsoft, Google, Amazon, Meta
    ↓ (40s - parallel processing)
Each competitor analyzed for:
  • Market position
  • Products/Services
  • Strengths/Weaknesses
  • Strategy
  • Growth trends
    ↓ (15s)
SWOT analysis created
    ↓ (20s)
Professional HTML report generated
    ↓
Report ready in output/ folder!
```

---

## 🛠️ Troubleshooting

### "Module not found" Error
```bash
# Reinstall dependencies
uv sync --all-groups
```

### "API Key Invalid" Error
1. Verify API key in .env file
2. Check key hasn't expired
3. Regenerate at [Google AI Studio](https://makersuite.google.com/app/apikey)

### "Connection Error"
1. Check internet connection
2. Verify Google API is accessible
3. Check firewall settings

### Report Generation Takes Long
- First run may cache models (normal)
- Large reports may take 90+ seconds
- Check internet speed

---

## 📚 Understanding Agents

### competitor_identifier_agent
- **Input:** Company name
- **Output:** 5 competitor names
- **Time:** ~10 seconds

### competitor_analyzer_agent (x5, parallel)
- **Input:** Competitor name
- **Output:** Detailed analysis
- **Time:** ~40 seconds (all 5 simultaneous)

### swot_analyzer_agent
- **Input:** 5 competitor analyses
- **Output:** SWOT matrices
- **Time:** ~15 seconds

### report_generator_agent
- **Input:** SWOT analysis
- **Output:** HTML report
- **Time:** ~20 seconds

---

## 💡 Pro Tips

1. **Try different companies** to see varying competitor landscapes
2. **Compare results** across different industries
3. **Export reports** as PDF from browser for presentations
4. **Share reports** with stakeholders for strategic planning
5. **Customize analysis** by modifying agent instructions

---

## 📝 Customization Quick Tips

### Change Number of Competitors
Edit `root_report_builder/agent.py`:
```python
parallel_competitor_analysis = ParallelAgent(
    name="parallel_competitor_analysis",
    sub_agents=[competitor_analyzer_agent] * 3,  # Change from 5 to 3
    description="Analyzes 3 competitors in parallel"
)
```

### Modify Analysis Focus
Edit `competitor_analyzer/instructions.txt` to emphasize:
- Financial metrics
- Innovation capabilities
- Customer satisfaction
- Supply chain strength
- Etc.

### Change Report Styling
Edit `report_generator/instructions.txt` for different:
- Color schemes
- Layout options
- Visualization types
- Font styles

---

## 🎯 Example Workflows

### Workflow 1: Startup Market Research
1. Enter your startup idea category
2. Get 5 main competitors
3. Analyze each competitor
4. Identify market gaps
5. Use report for investor pitch

### Workflow 2: Market Entry Strategy
1. Enter target market company
2. Analyze all competitors
3. Identify your positioning
4. Find unmet customer needs
5. Plan differentiation

### Workflow 3: Product Strategy
1. Enter competitor to benchmark against
2. Analyze competitor portfolio
3. Identify product gaps
4. Plan feature differentiation
5. Define market positioning

---

## 📞 Need Help?

1. **Check README.md** - Comprehensive documentation
2. **Review agent instructions** - See exact prompts
3. **Check PROJECT_STRUCTURE.md** - Understand architecture
4. **View agent_flow_diagram.md** - Visual guide

---

## ✨ Key Advantages

✅ **Automated** - No manual competitor research  
✅ **Comprehensive** - 4-stage in-depth analysis  
✅ **Fast** - Parallel processing (80% time saved)  
✅ **Professional** - Stakeholder-ready HTML reports  
✅ **Data-driven** - Based on real market intelligence  
✅ **Scalable** - Easy to add more competitors  

---

## 🎉 Ready to Go!

You now have a powerful competitive analysis system. Start by running:

```bash
adk web ./agents
```

Then enter any company name to analyze its competitive landscape!

**Happy analyzing! 🚀**
