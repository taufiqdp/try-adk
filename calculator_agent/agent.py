import os

import docker
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

base_url = os.getenv("DOCKER_BASE_URL")


def code_execution_tool(code: str) -> str:
    """
    Execute ONLY python code and return the result.

    Args:
        code (str): The code to execute.
        eg. '''
        import math

        def calculate_square_root(number):
            return math.sqrt(number)

        print(calculate_square_root(16))
        '''

    Returns:
        str: The result of the code execution or None if the code is not valid.
    """

    if not code.strip():
        return None

    lines = code.strip().splitlines()
    if lines:
        last_line = lines[-1]
        if (
            not last_line.strip().startswith("print")
            and "=" not in last_line
            and last_line.strip()
        ):
            lines[-1] = f"print({last_line.strip()})"
        elif last_line.strip().startswith("result ="):
            lines.append("print(result)")
        code = "\n".join(lines)

    print("Executing code:", code)

    try:
        client = docker.DockerClient(base_url=base_url)
        container = client.containers.run(
            # image="python-math:latest",
            image="python:3.13.3-slim",
            command=["python", "-c", code],
            mem_limit="128m",
            cpu_quota=100000,
            network_disabled=True,
            stderr=True,
            stdout=True,
            detach=False,
            remove=True,
        )
        output = container.decode()
        print("Code execution output:", output)

        return output.strip()

    except Exception as e:
        print("Error executing code:", e)
        return None


root_agent = Agent(
    name="calculator_agent",
    model=LiteLlm(model="azure/gpt-4o-mini"),
    tools=[code_execution_tool],
    instruction="""You are a calculator agent.
    When given any mathematical expression, write a Python code snippet to calculate the result and assign it to a variable named 'result'!.
    Always end the code with 'print(result)' to print the result.
    Use the 'code_execution_tool' to execute the code and print the result.
    If the code execution fails, return an error message and provide a suggestion for debugging.
    """,
    description="Executes Python code to perform calculations.",
)
