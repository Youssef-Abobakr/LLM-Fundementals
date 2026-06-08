from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")

# Create project and openai clients to call Foundry API
project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

# Run a responses API call
response = openai.responses.create(
    model="gpt-5-mini",
    input="What is the size of France in square miles?",
)

print(f"Response output: {response.output_text}")