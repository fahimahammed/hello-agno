Hello Agno:

# Create new project
mkdir my-agno-project && cd my-agno-project

# Initialize UV project
uv init

# Add Agno
uv add agno

# Activate virtual environment
source .venv/bin/activate  # Mac/Linux
# or
.venv\Scripts\activate     # Windows


# Add web search tools
uv add duckduckgo-search

# Add local models
uv add ollama

# Add other providers
uv add anthropic google-generativeai

# Add web framework for apps
uv add "uvicorn[standard]"


# Create project
uv init research-agent && cd research-agent
uv add agno duckduckgo-search