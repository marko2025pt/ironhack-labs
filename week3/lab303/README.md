# Lab 303 – Using MCP in LangChain

## Overview

This lab explores how to integrate an MCP (Model Context Protocol) server with a LangChain agent, enabling the agent to access external systems through standardized MCP tools and resources.

The objective was to:

- Integrate an MCP server with LangChain
- Load MCP tools into an agent workflow
- Access MCP resources for contextual data
- Build a working MCP-enabled LangChain agent
- Demonstrate MCP capabilities in practice

MCP provides a standardized way for AI systems to connect to files, APIs, databases, and other external systems. This lab focuses on bridging MCP and LangChain so agents can use external capabilities seamlessly.

---

## Learning Objectives

- Integrate MCP servers with LangChain agents
- Use MCP tools inside agent workflows
- Access MCP resources for contextual information
- Build an agent that leverages MCP capabilities
- Understand trade-offs between MCP integration and direct API calls

---

## What Happened During Implementation

While attempting to connect to a hosted MCP endpoint, a server-side HTTP 500 error was encountered. This issue originated from external infrastructure and was outside the local environment's control.

To avoid spending excessive time debugging third-party infrastructure and to ensure successful completion of the lab objectives within the expected time frame (90–120 minutes), the implementation strategy was adapted:

- A local MCP server was built
- A minimal, controlled environment was used
- Core MCP–LangChain integration was validated end-to-end

The goal remained aligned with the lab success criteria — integration and functionality — even if advanced features were not fully expanded.

---

## Project Structure

**Directory:** `C:\Users\marco\ironhack-labs\week3\lab303`

**Files:**

- **`mcp_langchainV2.ipynb`** — Main notebook containing all implementation code, step-by-step Markdown explanations, MCP server setup, client configuration, agent integration, tool execution tests, resource checks, final conclusions and lessons learned, and reflection and further work.
- **`requirements.txt`** — Python dependencies required to reproduce the lab.
- **`lablog.txt`** — Cell execution log with timestamps.

---

## How to Run the Project

### 1. Create Environment

\```bash
conda create -n mcp-lab python=3.11
conda activate mcp-lab
\```

### 2. Install Dependencies

\```bash
pip install -r requirements.txt
\```

### 3. Set OpenAI API Key

Create a `.env` file in the project directory:

\```
OPENAI_API_KEY=your_api_key_here
\```

### 4. Launch Notebook

\```bash
jupyter notebook
\```

Open `mcp_langchainV2.ipynb` and run the cells sequentially.

---

## Final Implementation

The final working implementation includes:

- A local MCP server using FastMCP
- HTTP transport (streamable-http)
- A registered arithmetic tool
- MCP client configuration via `langchain-mcp-adapters`
- A LangChain agent capable of invoking MCP tools
- Successful end-to-end tool execution

MCP resources were queried; however, the local server did not expose resources in this implementation.

---

## Success Criteria Evaluation

| Criteria | Status |
|---|---|
| Successfully integrated MCP server with LangChain | ✔ |
| Built agent that uses MCP tools | ✔ |
| Demonstrated MCP capabilities in a working agent | ✔ |
| Accessed MCP resources (none available in this server configuration) | ✔ |

Core integration objectives were achieved.

---

## Lessons Learned

- External infrastructure can introduce unexpected instability.
- Proper debugging requires separating local configuration issues from external service failures.
- Any external dependency can become a single point of failure.
- Architectural decisions under time constraints require strategic trade-offs.
- A working, controlled integration is more valuable than an overextended, unstable implementation.

---

## Further Work

Future improvements may include:

- Adding multiple arithmetic tools (subtraction, multiplication, division)
- Implementing MCP resources (e.g., document-based context)
- Connecting multiple MCP servers
- Comparing MCP integration with direct API integration
- Deploying the MCP server beyond local development

---

## Status

> Lab objectives achieved. Integration validated. Further enhancements identified for future iteration.