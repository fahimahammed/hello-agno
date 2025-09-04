# Level 2: Agents with knowledge and storage

from agno.agent import Agent
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv
import os

# Load environment variables first
load_dotenv()

# Load Agno documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/llms.txt"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=SentenceTransformerEmbedder(),  # Changed to local embedder
    )
)

storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/level_2_agent.db")

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),  # Using Anthropic Claude
    instructions=[
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    agent.knowledge.load(recreate=False)
    agent.print_response("What is Agno? Give me a short answer.", stream=True)