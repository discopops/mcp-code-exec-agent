from agency_swarm import Agent
from agency_swarm.tools import PersistentShellTool, IPythonInterpreter
from openai.types.shared import Reasoning
from agents import ModelSettings

sales_ops = Agent(
    name="SalesOps",
    description="Sales operations agent equipped with Python interpreter and shell tools for automating operational tasks using Notion and Google Drive MCP tools.",
    instructions="./instructions.md",
    tools_folder="./tools",
    files_folder="./files",
    tools=[PersistentShellTool, IPythonInterpreter],
    model="gpt-5",
    model_settings=ModelSettings(
        reasoning=Reasoning(
            effort="medium",
            summary="auto",
        ),
    ),
)

