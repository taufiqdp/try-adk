from datetime import datetime

import pytz
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

AGENT_MODEL = "azure/gpt-4o-mini"


def get_time(timezone: str) -> dict:
    """Retrieves the current local time for a specified timezone.

    Args:
        timezone (str): The name of the timezone (e.g., 'US/Pacific', 'Europe/London', 'Asia/Tokyo').

    Returns:
        dict: A dictionary containing the time information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'time' key with the local time as a string.
              If 'error', includes an 'error_message' key.
    """

    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return {
            "status": "success",
            "time": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
        }
    except:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have time information for '{timezone}'.",
        }


root_agent = Agent(
    name="time_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="Provides current time for specified timezone",
    instruction="You are a helpful time assistant. Your primary goal is to provide the current time for given timezones or cities. "
    "When the user asks for the time in a specific city or time zone "
    "you MUST use the 'get_time' tool to find the information. "
    "Analyze the tool's response: if the status is 'error', inform the user politely about the error message. "
    "If the status is 'success', present the information clearly and concisely to the user. "
    "Only use the tools when appropriate for a time-related request.",
    tools=[get_time],
)
