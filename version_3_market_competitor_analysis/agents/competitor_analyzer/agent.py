import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file

competitor_analyzer_agent = LlmAgent(
    name="competitor_analyzer_agent",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description=load_instructions_file("agents/competitor_analyzer/description.txt"),
    output_key="competitor_analyzer_output"
)
