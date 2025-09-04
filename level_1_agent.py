# Level 1: Agents with tools and instructions
# This agent uses the OpenRouter model and DuckDuckGo tools to provide information.
# It is instructed to use tables for displaying data. It streams the response. 

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables
load_dotenv()

agent = Agent(
    model=OpenAIChat(
        id="z-ai/glm-4.5-air:free",   # OpenRouter model ID
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_API_KEY")
    ),
    tools=[DuckDuckGoTools()],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)

agent.print_response("I want to learn python. give me a roadmap with video content.", stream=True)