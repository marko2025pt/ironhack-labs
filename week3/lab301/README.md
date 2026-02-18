# Lab301: NormalObjects - Creative Complaint Handler (LangChain) v1.01

Student: Marco Martins  
Module: LangChain Agents  
Project Type: Creative Tool-Calling Agent  

---

# 📌 Project Overview

This project implements a creative AI agent called **"Becma's Chaos Mode"**, designed to handle fictional complaints about inconsistencies in the Normal Objects universe.

The agent uses:

- LangChain's tool-calling framework  
- Custom creative tools  
- Flexible (freeform) reasoning  
- Dynamic tool chaining  
- Tool usage tracking for analysis  
- Streamlit web interface  

The objective of this lab is to demonstrate how freeform LangChain agents behave compared to structured workflows.

In addition to the lab requirements, a web interface was implemented to interact with the agent visually and generate downloadable logs.

---

# 🧠 Features Implemented

- Custom tools using the `@tool` decorator  
- Flexible tool chaining (LLM decides tool order)  
- Multiple tool calls per complaint  
- Creative responses generated dynamically  
- Tool usage tracking (counts + sequences)  
- Demonstration log included  
- Analysis document included  
- Streamlit GUI interface  
- Automatic log file generation  
- Downloadable complaint logs  

---

# 📂 Project Structure
lab301/
|
├── normalobjects_langchain.py   # Main agent implementation
├── demo_log.txt                 # Terminal output demonstration
├── analysis.html                # Analysis document (HTML format)
├── complaint_log_20260218_133012.txt # Generated GUI log file
├── complaint_log_20260218_133217.txt # Generated GUI log file
├── complaint_log_20260218_133422.txt # Generated GUI log file
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
- streamlit

## 🔑 OpenAI API Key Setup

Create a .env file in the project root folder and add:

OPENAI_API_KEY=your_actual_openai_key_here


⚠️ Do not include quotes.
⚠️ Do not commit the .env file.

# ▶️ Running the Project

## ▶️ Terminal Version

Run: python normalobjects_langchain.py

The program will:

- Load the OpenAI API key
- Create and register tools
- Initialize the LangChain agent
- Process three different complaints
- Display tool invocation logs
- Print tool usage statistics

## 🌐 Running the Web Interface (Streamlit GUI)

Run: streamlit run app.py

The web application will open at: http://localhost:8501

The GUI allows you to:

- Submit complaints interactively
- View the creative agent response
- See tool usage statistics
- Automatically generate a log file
- Download the generated log file

# 📊 Demonstration

The file demo_log.txt contains:

- Three different complaints handled
- Tool invocation logs
- Creative responses
- Tool usage statistics

You can regenerate it with:

python normalobjects_langchain.py > demo_log.txt

# 📝 Generated Log Files (GUI)

When using the Streamlit interface, each complaint generates a timestamped log file, such as:

- complaint_log_20260218_133012.txt
- complaint_log_20260218_133217.txt
- complaint_log_20260218_133422.txt

Each log file contains:
- Timestamp
- Complaint
- Agent response
- Tool usage statistics
- Tool call sequence

This extends the lab requirements by adding persistence and export capability.

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