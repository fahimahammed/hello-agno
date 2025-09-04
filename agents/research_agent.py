from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    name="Research Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="You are a research assistant. Use the tools to gather information and answer the user's questions.",
    markdown=True,
    show_tool_calls=True,
)

if __name__ == "__main__":
    agent.print_response("What is the latest news on AI?")