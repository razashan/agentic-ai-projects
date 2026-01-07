import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_to_file

report_generator_agent = LlmAgent(
    name="report_generator_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/report_generator/instructions.txt"),
    description=load_instructions_file("agents/report_generator/description.txt"),
    tools=[write_to_file],
    output_key="report_generator_output"
)