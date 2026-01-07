import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file

competitor_identifier_agent = LlmAgent(
    name="competitor_identifier_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_identifier/instructions.txt"),
    description=load_instructions_file("agents/competitor_identifier/description.txt"),
    output_key="competitor_identifier_output"
)