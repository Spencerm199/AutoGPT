# AutoGPT Agents

This directory contains the custom agents for the AutoGPT platform.

## Structure

```
agents/
├── base/                  # Base agent classes and utilities
│   ├── __init__.py
│   ├── base_agent.py     # Base agent class
│   └── utils.py          # Utility functions
├── examples/             # Example agent implementations
│   ├── __init__.py
│   ├── qa_agent.py      # Question & Answer agent
│   └── calculator_agent.py # Calculator agent
├── blocks/              # Custom blocks for agent workflows
│   ├── __init__.py
│   └── custom_blocks.py # Custom block implementations
└── tests/              # Test files for agents
    ├── __init__.py
    └── test_agents.py  # Test cases for agents
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your API keys and configuration.

3. Start the agent server:
```bash
python -m agents.server
```

## Creating a New Agent

1. Create a new file in `agents/examples/` for your agent
2. Inherit from `BaseAgent` in `agents/base/base_agent.py`
3. Implement required methods
4. Register your agent in the platform

## Testing

Run tests using pytest:
```bash
pytest agents/tests/
```

## Examples

Check the `examples/` directory for sample agent implementations:
- QA Agent: Basic question-answering capability
- Calculator Agent: Numerical operations without AI 