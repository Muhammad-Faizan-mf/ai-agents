├── mcp_leave_management/       # Model Context Protocol (MCP) implementations
│   └── mcp-server/
│       ├── main.py             # FastMCP Leave Management Server
│       └── pyproject.toml      # Project dependencies managed via uv
│
└── phidata_finance_agent/      # Multi-Agent orchestrations using Phidata
    ├── 1_financial_agent.py    # Basic financial agent implementation
    ├── 2_finance_agent_groq.py # Free-tier financial processing utilizing Groq & Llama
    ├── 3_agent_teams_openai.py # Live financial analyst & web research agent team via OpenAI
    ├── 4_agent_playground.py   # Phidata UI Playground dashboard integration
    └── .env.example            # Environment variables configuration template