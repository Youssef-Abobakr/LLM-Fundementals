from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition # This defines which model the agent uses and how it should behave. 

import os
from dotenv import load_dotenv

load_dotenv()

FOUNDRY_PROJECT_ENDPOINT=os.getenv('FOUNDRY_PROJECT_ENDPOINT')
AGENT_NAME = os.getenv("AGENT_NAME")

project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

agent = project.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="You are a helpful assistant that answers general questions."
    )
)
print(f"Agent Created (id: {agent.id}, name: {agent.name}, version: {agent.version})")