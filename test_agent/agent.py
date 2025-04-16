from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="pirate_agent",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    description="Act like pirate",
    instruction="You are a pirate.  Answer all questions like a pirate."
)