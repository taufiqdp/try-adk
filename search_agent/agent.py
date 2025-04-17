from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

load_dotenv()

tavily_tool_instance = TavilySearchResults(
    max_results=1,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=False,
)

adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)

root_agent = Agent(
    name="search_agent",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    description="Agent to answer questions using TavilySearch.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[adk_tavily_tool],
)
