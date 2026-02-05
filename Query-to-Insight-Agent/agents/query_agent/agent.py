import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_sql_to_file

query_writer_agent = LlmAgent(
    name = "query_writer_agent",
    model = "gemini-2.5-flash",
    instruction=load_instructions_file("agents/query_agent/instructions.txt"),
    description=load_instructions_file("agents/query_agent/description.txt"),
    tools=[write_sql_to_file],
    output_key="query_writer_output"
)