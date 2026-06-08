from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

import os
from dotenv import load_dotenv

load_dotenv()

FOUNDRY_PROJECT_ENDPOINT=os.getenv('FOUNDRY_PROJECT_ENDPOINT')
AGENT_NAME = os.getenv("AGENT_NAME")

project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

openai = project.get_openai_client()

conversation = openai.conversations.create()

response = openai.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
    input="What is the size of Egypt in square miles?",
)
print(response.output_text)

response = openai.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
    input="What is its capital city?",
)
print(response.output_text)
