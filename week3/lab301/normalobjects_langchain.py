# ==============================
# IMPORTS
# ==============================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


# ==============================
# LOAD ENVIRONMENT VARIABLES
# ==============================

load_dotenv(override=True)

print("API KEY LOADED:",
      os.getenv("OPENAI_API_KEY")[:10] if os.getenv("OPENAI_API_KEY") else "NOT FOUND")


# ==============================
# INITIALIZE LLM
# ==============================

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

print("Environment loaded successfully.")


# ==============================
# TOOL USAGE TRACKER
# ==============================

class ToolUsageTracker:
    """
    Tracks:
    - Tool usage count
    - Tool call sequence
    """

    def __init__(self):
        self.usage_count = {}
        self.tool_sequences = []

    def register_tools(self, tools):
        self.usage_count = {tool.name: 0 for tool in tools}

    def track_usage(self, tool_name: str):
        if tool_name in self.usage_count:
            self.usage_count[tool_name] += 1
            self.tool_sequences.append(tool_name)

    def get_statistics(self):
        return {
            "total_tool_calls": sum(self.usage_count.values()),
            "tool_counts": self.usage_count,
            "most_used": max(self.usage_count.items(), key=lambda x: x[1])[0]
            if self.usage_count else None,
            "tool_sequences": self.tool_sequences
        }


tracker = ToolUsageTracker()


# ==============================
# TOOL DEFINITIONS
# ==============================

@tool
def consult_demogorgon(complaint: str) -> str:
    """Get the Demogorgon's perspective on a complaint."""
    
    tracker.track_usage("consult_demogorgon")

    responses = [
        f"The Demogorgon tilts its head at '{complaint}'. Maybe you're thinking in three dimensions?",
        f"It growls softly. Perhaps time flows differently in the Upside Down.",
        f"It seems confused. Maybe consistency is not important there?"
    ]

    import random
    return random.choice(responses)


@tool
def check_hawkins_records(query: str) -> str:
    """Search Hawkins historical records for clues."""
    
    tracker.track_usage("check_hawkins_records")

    records = {
        "portal": "Portals open unpredictably due to weather and electromagnetic changes.",
        "monsters": "Creatures behave differently depending on environment.",
        "psychics": "Psychic abilities vary from person to person.",
        "electricity": "Electrical systems are affected by Upside Down interference."
    }

    for key, value in records.items():
        if key in query.lower():
            return value

    return "No specific record found, but Hawkins has a history of strange events."


@tool
def cast_interdimensional_spell(problem: str, creativity_level: str = "medium") -> str:
    """Suggest a creative magical solution."""
    
    tracker.track_usage("cast_interdimensional_spell")

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

tracker.register_tools(tools)

print(f"Created {len(tools)} creative tools:")
for tool_obj in tools:
    print(f"  - {tool_obj.name}")


# ==============================
# AGENT SETUP
# ==============================

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are Becma's Chaos Mode. Solve complaints creatively using tools."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    max_iterations=5,
    handle_parsing_errors=True
)

print("Agent created successfully.")


# ==============================
# RUN TESTS ONLY IF EXECUTED DIRECTLY
# ==============================

if __name__ == "__main__":

    complaints = [
        "Why do demogorgons sometimes eat people and sometimes don't?",
        "The portal opens on different days—is there a schedule?",
        "Why can some psychics see the Downside Up and others can't?"
    ]

    def handle_complaint(complaint: str) -> str:
        print(f"\n{'='*60}")
        print(f"COMPLAINT: {complaint}")
        print(f"{'='*60}\n")

        result = agent_executor.invoke({"input": complaint})
        return result["output"]

    print("Testing agent...\n")

    for complaint in complaints:
        response = handle_complaint(complaint)
        print(f"\nRESPONSE:\n{response}\n")

    print("\n=== Tool Usage Analysis ===")

    stats = tracker.get_statistics()

    print(f"Total tool calls: {stats['total_tool_calls']}")
    print(f"Tool usage counts: {stats['tool_counts']}")
    print(f"Most used tool: {stats['most_used']}")
    print(f"Tool sequence: {stats['tool_sequences']}")
