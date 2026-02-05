import os
import sys
from google.adk.agents import LlmAgent

# Add project root to path to import utils and tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils.file_loader import load_instructions_file
from tools.file_writer_tool import fetch_data_and_save_to_file

# Initialize the Data Extraction Agent
data_extraction_agent = LlmAgent(
    name="data_extraction_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/datafetch_agent/instructions.txt"),
    description=load_instructions_file("agents/datafetch_agent/description.txt"),
    tools=[fetch_data_and_save_to_file],
    output_key="data_extraction_output"
)
