import os
import sys
from google.adk.agents import SequentialAgent

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file

# Import all sub-agents
from agents.intent.agent import intent_agent
from agents.query_agent.agent import query_writer_agent
from agents.datafetch_agent.agent import data_extraction_agent
from agents.analyze_agent.agent import analyze_agent
from agents.insight_agent.agent import insight_agent

# Initialize the Root Agent for Query-to-Insight pipeline
root_agent = SequentialAgent(
    name="root_query_to_insight_agent",
    sub_agents=[
        intent_agent,
        query_writer_agent,
        data_extraction_agent,
        analyze_agent,
        insight_agent
    ],
    description=load_instructions_file("agents/root_agent/description.txt")
)
