import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_database_file

sql_writer_agent = LlmAgent(
    name = "sql_writer_agent",
    model = "gemini-2.5-flash",
    instruction=load_instructions_file("agents/sql_writer/instructions.txt"),
    description=load_instructions_file("agents/sql_writer/description.txt"),
    tools=[write_database_file],
    output_key="sql_writer_output"
)