from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions="You are a helpful assistant",
    markdown=True
)

agent.print_response("Hello, how are you?")

def main():
    print("Hello from hello-agno!")


if __name__ == "__main__":
    main()
