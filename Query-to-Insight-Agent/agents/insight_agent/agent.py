import os
import sys
from google.adk.agents import LlmAgent

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.file_writer_tool import generate_insights_and_save_to_file

# Initialize Insight Generator Agent
insight_agent = LlmAgent(
    name="insight_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/insight_agent/instructions.txt"),
    description=load_instructions_file("agents/insight_agent/description.txt"),
    tools=[generate_insights_and_save_to_file],
    output_key="insight_agent_output"
)
