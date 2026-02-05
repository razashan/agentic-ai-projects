import os
import sys
from google.adk.agents import LlmAgent

# Add project root to path for utils and tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.file_writer_tool import analyze_data_and_save_to_file

# Initialize the Analyze Agent
analyze_agent = LlmAgent(
    name="analyze_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/analyze_agent/instructions.txt"),
    description=load_instructions_file("agents/analyze_agent/description.txt"),
    tools=[analyze_data_and_save_to_file],
    output_key="analyze_agent_output"
)
