import os
import sys
from google.adk.agents import SequentialAgent, ParallelAgent, LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))
from utils.file_loader import load_instructions_file
from agents.competitor_identifier.agent import competitor_identifier_agent
from agents.swot_analyzer.agent import swot_analyzer_agent
from agents.report_generator.agent import report_generator_agent

# Create 5 separate instances of competitor analyzer agents for parallel execution
# Each instance is independent and can run simultaneously
competitor_analyzer_1 = LlmAgent(
    name="competitor_analyzer_1",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description="Analyzes competitor 1",
    output_key="competitor_analyzer_output_1"
)

competitor_analyzer_2 = LlmAgent(
    name="competitor_analyzer_2",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description="Analyzes competitor 2",
    output_key="competitor_analyzer_output_2"
)

competitor_analyzer_3 = LlmAgent(
    name="competitor_analyzer_3",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description="Analyzes competitor 3",
    output_key="competitor_analyzer_output_3"
)

competitor_analyzer_4 = LlmAgent(
    name="competitor_analyzer_4",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description="Analyzes competitor 4",
    output_key="competitor_analyzer_output_4"
)

competitor_analyzer_5 = LlmAgent(
    name="competitor_analyzer_5",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("agents/competitor_analyzer/instructions.txt"),
    description="Analyzes competitor 5",
    output_key="competitor_analyzer_output_5"
)

# Create parallel agent for analyzing 5 competitors simultaneously
parallel_competitor_analysis = ParallelAgent(
    name="parallel_competitor_analysis",
    sub_agents=[
        competitor_analyzer_1,
        competitor_analyzer_2,
        competitor_analyzer_3,
        competitor_analyzer_4,
        competitor_analyzer_5
    ],
    description="Analyzes all 5 competitors in parallel"
)

# Create the main sequential orchestration
root_agent = SequentialAgent(
    name="root_report_builder_agent",
    sub_agents=[
        competitor_identifier_agent,
        parallel_competitor_analysis,
        swot_analyzer_agent,
        report_generator_agent
    ],
    description=load_instructions_file("agents/root_report_builder/description.txt")
)