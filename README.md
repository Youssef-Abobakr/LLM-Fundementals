# LLM-Fundementals

This project is set up to practice LLM fundamentals using clean code practices and Azure AI Foundry. The README documents each step of the learning process as the system evolves from basic model connection to more advanced LLM workflows.

---

## Step 1: Setup and Connect to an LLM Model

**Output File:** `Connection_Check.py`

**Goal:** Establish a secure connection to a deployed LLM using Azure AI Foundry and verify that responses can be generated successfully.

### Steps:
1. Create an Azure subscription  
2. Set up a project in Microsoft Azure AI Foundry  
3. Deploy a model inside the Foundry project (e.g., GPT-5 Mini or equivalent)  
4. Configure authentication for secure access  
5. Write a Python script to connect to the deployed model  
6. Send a test prompt and verify the response  

---

### Model Connection

To interact with the model, users must authenticate using Azure’s identity system.

This project uses:

- `DefaultAzureCredential` from `azure.identity`
- `.env` file for environment configuration
- `AIProjectClient` from `azure.ai.projects`

Authentication is handled automatically through Azure-supported methods such as:

- Azure CLI login (`az login`)
- Visual Studio Code Azure account
- Managed Identity (for deployed environments)

---

### Environment Configuration

Create a `.env` file in the root directory:

```env
FOUNDRY_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-name>