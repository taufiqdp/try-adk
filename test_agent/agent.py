from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

AGENT_MODEL = "azure/gpt-4o-mini"

root_agent = Agent(
    name="pirate_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="Act like pirate",
    instruction="You are a pirate.  Answer all questions like a pirate.",
)
