# ==============================
# IMPORTS
# ==============================

# Standard Python library to access environment variables
import os

# Loads variables from a .env file into the system environment
from dotenv import load_dotenv

# LangChain OpenAI chat model
from langchain_openai import ChatOpenAI

# Agent utilities to create and run tool-calling agents
from langchain.agents import AgentExecutor, create_openai_tools_agent

# Decorator used to turn a normal Python function into a LangChain tool
from langchain.tools import tool

# Used to create structured prompts for the agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


# ==============================
# LOAD ENVIRONMENT VARIABLES
# ==============================

# Load variables from .env file
# override=True ensures the .env value replaces any system variable
load_dotenv(override=True)

# Debug: show first characters of API key (to confirm it loaded correctly)
print("API KEY LOADED:",
      os.getenv("OPENAI_API_KEY")[:10] if os.getenv("OPENAI_API_KEY") else "NOT FOUND")


# ==============================
# INITIALIZE LLM
# ==============================

# Create the OpenAI chat model
# temperature=0.7 makes responses more creative
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

print("Environment loaded successfully.")


# ==============================
# TOOL USAGE TRACKER
# ==============================

class ToolUsageTracker:
    """
    This class tracks:
    - How many times each tool is used
    - The order in which tools are called
    """

    def __init__(self):
        # Dictionary: {tool_name: usage_count}
        self.usage_count = {}

        # List storing the order of tool calls
        self.tool_sequences = []

    def register_tools(self, tools):
        """Initialize usage counter for each tool"""
        self.usage_count = {tool.name: 0 for tool in tools}

    def track_usage(self, tool_name: str):
        """Increment counter when a tool is used"""
        if tool_name in self.usage_count:
            self.usage_count[tool_name] += 1
            self.tool_sequences.append(tool_name)

    def get_statistics(self):
        """Return statistics for analysis"""
        return {
            "total_tool_calls": sum(self.usage_count.values()),
            "tool_counts": self.usage_count,
            "most_used": max(self.usage_count.items(), key=lambda x: x[1])[0]
            if self.usage_count else None,
            "tool_sequences": self.tool_sequences
        }


# Create tracker instance
tracker = ToolUsageTracker()


# ==============================
# TOOL DEFINITIONS
# ==============================

# Each function below becomes a tool that the agent can call.
# The @tool decorator registers it inside LangChain.


@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint."""
    
    # Track usage
    tracker.track_usage("consult_demogorgon")

    # Pre-written creative responses
    responses = [
        f"The Demogorgon tilts its head at '{complaint}'. Maybe you're thinking in three dimensions?",
        f"It growls softly. Perhaps time flows differently in the Upside Down.",
        f"It seems confused. Maybe consistency is not important there?"
    ]

    # Randomly choose one response
    import random
    return random.choice(responses)


@tool
def check_hawkins_records(query: str) -> str:
    """Search Hawkins historical records for clues."""
    
    tracker.track_usage("check_hawkins_records")

    # Fake database of known issues
    records = {
        "portal": "Portals open unpredictably due to weather and electromagnetic changes.",
        "monsters": "Creatures behave differently depending on environment.",
        "psychics": "Psychic abilities vary from person to person.",
        "electricity": "Electrical systems are affected by Upside Down interference."
    }

    # Search for keyword match
    for key, value in records.items():
        if key in query.lower():
            return value

    return "No specific record found, but Hawkins has a history of strange events."


@tool
def cast_interdimensional_spell(problem: str, creativity_level: str = "medium") -> str:
    """Suggest a creative magical solution."""
    
    tracker.track_usage("cast_interdimensional_spell")

    # Decide how many spells to return
    creativity_multiplier = {"low": 1, "medium": 2, "high": 3}[creativity_level]

    spells = [
        f"Chant 'Becma Becma Becma' while focusing on: {problem}",
        f"Create a salt circle to stabilize: {problem}",
        f"Play music backwards near the issue: {problem}",
        f"Arrange symbolic objects in a triangle for: {problem}"
    ]

    import random
    selected = random.sample(spells, min(creativity_multiplier, len(spells)))
    return "\n".join(selected)


@tool
def gather_party_wisdom(question: str) -> str:
    """Ask the D&D party for their opinion."""
    
    tracker.track_usage("gather_party_wisdom")

    party_responses = {
        "portal": "Portals open near emotional events.",
        "monsters": "Demogorgons sense fear.",
        "psychics": "Powers depend on emotional state.",
        "electricity": "The Upside Down disrupts power lines."
    }

    for key, response in party_responses.items():
        if key in question.lower():
            return response

    return "The party agrees more investigation is needed."


# ==============================
# REGISTER TOOLS
# ==============================

tools = [
    consult_demogorgon,
    check_hawkins_records,
    cast_interdimensional_spell,
    gather_party_wisdom
]

# Initialize tracker counters
tracker.register_tools(tools)

print(f"Created {len(tools)} creative tools:")
for tool in tools:
    print(f"  - {tool.name}")


# ==============================
# AGENT SETUP
# ==============================

# Define system + user prompt structure
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are Becma's Chaos Mode. Solve complaints creatively using tools."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Create tool-calling agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Create executor to run the agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,          # Shows tool calls in terminal
    max_iterations=5,      # Prevents infinite loops
    handle_parsing_errors=True
)

print("Agent created successfully.")


# ==============================
# TESTING THE AGENT
# ==============================

# Sample complaints
complaints = [
    "Why do demogorgons sometimes eat people and sometimes don't?",
    "The portal opens on different days—is there a schedule?",
    "Why can some psychics see the Downside Up and others can't?"
]


def handle_complaint(complaint: str) -> str:
    """Send complaint to agent and return response"""
    
    print(f"\n{'='*60}")
    print(f"COMPLAINT: {complaint}")
    print(f"{'='*60}\n")

    result = agent_executor.invoke({"input": complaint})
    return result["output"]


print("Testing agent...\n")

# Run all complaints
for complaint in complaints:
    response = handle_complaint(complaint)
    print(f"\nRESPONSE:\n{response}\n")


# ==============================
# TOOL USAGE ANALYSIS
# ==============================

print("\n=== Tool Usage Analysis ===")

stats = tracker.get_statistics()

print(f"Total tool calls: {stats['total_tool_calls']}")
print(f"Tool usage counts: {stats['tool_counts']}")
print(f"Most used tool: {stats['most_used']}")
print(f"Tool sequence: {stats['tool_sequences']}")
