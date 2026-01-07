import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_design_to_file

designer_agent = LlmAgent(
    name = "designer_agent",
    model = "gemini-2.5-flash",
    instruction=load_instructions_file("agents/designer/instructions.txt"),
    description=load_instructions_file("agents/designer/description.txt"),
    tools=[write_design_to_file],
    output_key="designer_output"
)