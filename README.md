# 🤖 Advanced AI Agents Integration Workspace

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Phidata-orange?style=for-the-badge" alt="Phidata">
  <img src="https://img.shields.io/badge/Protocol-MCP-green?style=for-the-badge" alt="MCP">
  <img src="https://img.shields.io/badge/Package%20Manager-uv-purple?style=for-the-badge" alt="uv">
</p>

---

## 📂 System Architecture Overview

This repository serves as a centralized development environment for building, evaluating, and orchestrating advanced Large Language Model (LLM) agent architectures. The workspace is split into two core modern engineering paradigms:

1. **Multi-Agent Teams & Tool Routing** via the Phidata framework.
2. **Model Context Protocol (MCP) Infrastructures** via the FastMCP engine to expose local tools directly to LLM clients (like Claude Desktop and Cursor).

---

## 📁 Repository Blueprint

```text
├── 🔌 mcp_leave_management/       # Model Context Protocol Framework
│   └── mcp-server/
│       ├── main.py             # FastMCP Leave Management Engine
│       └── pyproject.toml      # Virtual environment configuration via uv
│
└── 📈 phidata_finance_agent/      # Multi-Agent Financial Ecosystem
    ├── 1_financial_agent.py    # Baseline Market Data Tracker
    ├── 2_finance_agent_groq.py # High-Speed Zero-Cost Processing Pipeline
    ├── 3_agent_teams_openai.py # Parallel Autonomous Research Team
    ├── 4_agent_playground.py   # Phidata Web UI Dashboard Interface
    └── .env.example            # Environment variables credential configuration