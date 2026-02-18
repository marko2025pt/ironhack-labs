# ✅ README.md
Lab301: NormalObjects - Creative Complaint Handler (LangChain)

Student: Marco Martins
Module: LangChain Agents
Project Type: Creative Tool-Calling Agent

# 📌 Project Overview

This project implements a creative AI agent called "Becma's Chaos Mode", designed to handle fictional complaints about inconsistencies in the Normal Objects universe.

The agent uses:

- LangChain's tool-calling framework
- Custom creative tools
- Flexible (freeform) reasoning
- Dynamic tool chaining
- Tool usage tracking for analysis

The objective of this lab is to demonstrate how freeform LangChain agents behave compared to structured workflows.

# 🧠 Features Implemented

- Custom tools using the @tool decorator
- Flexible tool chaining (LLM decides tool order)
- Multiple tool calls per complaint
- Creative responses generated dynamically
- Tool usage tracking (counts + sequences)
- Demonstration log included
- Analysis document included

# 📂 Project Structure
lab301/
|
├── normalobjects_langchain.py   # Main agent implementation
├── demo_log.txt                 # Terminal output demonstration
├── analysis.html                # Analysis document (HTML format)
├── requirements.txt             # Required Python packages
├── .env                         # OpenAI API key (not committed)
└── README.md                    # Project documentation

# ⚙️ Installation
## 1️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows (PowerShell): venv\Scripts\activate

## 2️⃣ Install Required Packages
pip install -r requirements.txt

This installs:
- langchain==0.1.20
- langchain-openai==0.1.6
- openai
- python-dotenv

## 🔑 OpenAI API Key Setup

Create a .env file in the project root folder and add:

OPENAI_API_KEY=your_actual_openai_key_here


⚠️ Do not include quotes.
⚠️ Do not commit the .env file.

# ▶️ Running the Project

Run: python normalobjects_langchain.py

The program will:

- Load the OpenAI API key
- Create and register tools
- Initialize the LangChain agent
- Process three different complaints
- Display tool invocation logs
- Print tool usage statistics

# 📊 Demonstration

The file demo_log.txt contains:

- Three different complaints handled
- Tool invocation logs
- Creative responses
- Tool usage statistics

You can regenerate it with:

python normalobjects_langchain.py > demo_log.txt

# 📄 Analysis

The full analysis report for this lab is provided in:

analysis.html

The document includes:
- Creative tool usage behavior
- Comparison between freeform and structured approaches
- Recommendations for when to use each architecture

You can open analysis.html in a browser or export it as PDF for submission.

-------

Lab301 – NormalObjects Creative Complaint Handler (LangChain)
Marco Martins