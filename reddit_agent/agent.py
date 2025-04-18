import os

import praw
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")


def get_reddit_hot_posts_tool(subreddit_name: str, limit: int = 5) -> dict:
    """
    Fetch the hot posts from a specified subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to fetch posts from.
        limit (int, optional): The number of posts to fetch. Default is 5.

    Returns:
        dict: A dictionary with:
            - status (str): "success" if posts are fetched, "error" otherwise.
            - content (list or str):
                If status is "success": a list of dictionaries, each with:
                    - title (str): The post's title.
                    - url (str): The post's URL.
                    - created_utc (float): The post's creation time (UTC timestamp).
                    - author (str): The post author's username.
                    - selftext (str): The post's text content.
                If status is "error": a string describing the error.
    """
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )
        subreddit = reddit.subreddit(subreddit_name.lower())
        if not subreddit:
            return {"status": "error", "content": "Subreddit not found."}

        hot_posts = subreddit.hot(limit=limit)
        posts = []
        for post in hot_posts:
            posts.append(
                {
                    "title": post.title,
                    "url": post.url,
                    "created_utc": post.created_utc,
                    "author": str(post.author),
                    "selftext": post.selftext,
                }
            )

        return {"status": "success", "content": posts}
    except Exception as e:
        return {"status": "error", "content": str(e)}


root_agent = Agent(
    name="reddit_agent",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    tools=[get_reddit_hot_posts_tool],
    description="A Reddit agent that searches for the most relevant posts in a given subreddit",
    instruction="""You are a Reddit agent. Your primary task is to fetch and summarize the hot posts from a specified subreddit.
    You can use the 'get_reddit_hot_posts_tool' to fetch the hot posts from a subreddit.
    Present the information as a concise, bulleted list. Clearly state which subreddit(s) the information came from. 
    If the tool indicates an error or an unknown subreddit, report that message directly.
    """,
)
