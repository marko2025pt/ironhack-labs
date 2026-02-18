# ==============================
# IMPORTS
# ==============================

# Streamlit is used to create the web interface
import streamlit as st

# Used to generate timestamps for log files
from datetime import datetime

# Import the agent and tracker from our main backend file
# agent_executor = runs the AI agent
# tracker = tracks tool usage
from normalobjects_langchain import agent_executor, tracker


# ==============================
# PAGE CONFIGURATION
# ==============================

# Configure basic page settings
st.set_page_config(
    page_title="Becma's Chaos Mode",  # Browser tab title
    page_icon="🌌",                   # Icon in browser tab
    layout="centered"                 # Center content on page
)

# Main page title
st.title("🌌 Becma's Chaos Mode")

# Subtitle
st.subheader("NormalObjects - Creative Complaint Handler (LangChain)")

# Short explanation for the user
st.write(
    "Submit a complaint about the Normal Objects universe. "
    "The agent will consult different sources and respond creatively."
)


# ==============================
# USER INPUT AREA
# ==============================

# Text area where the user writes their complaint
complaint = st.text_area(
    "Enter your complaint:",
    height=120,
    placeholder="Example: Why do portals open randomly?"
)


# ==============================
# BUTTON ACTION
# ==============================

# When the button is clicked, this block runs
if st.button("Generate Response"):

    # Prevent empty submissions
    if complaint.strip() == "":
        st.warning("Please enter a complaint before submitting.")

    else:

        # ==============================
        # RESET TOOL TRACKER
        # ==============================

        # We reset tool usage statistics so each request starts clean
        tracker.tool_sequences = []
        for key in tracker.usage_count:
            tracker.usage_count[key] = 0

        # ==============================
        # CALL THE AGENT
        # ==============================

        # Show a loading spinner while the AI is thinking
        with st.spinner("Consulting the Upside Down..."):

            # Send the complaint to the agent
            result = agent_executor.invoke({"input": complaint})

            # Extract the text output from the result
            response = result["output"]

        # Get tool usage statistics after agent finishes
        stats = tracker.get_statistics()

        # Show success message
        st.success("Response Generated!")

        # ==============================
        # DISPLAY AGENT RESPONSE
        # ==============================

        st.markdown("### 📝 Agent Response")
        st.write(response)

        # ==============================
        # DISPLAY TOOL USAGE STATISTICS
        # ==============================

        st.markdown("### 🔧 Tool Usage Statistics")

        st.write(f"**Total tool calls:** {stats['total_tool_calls']}")
        st.write(f"**Most used tool:** {stats['most_used']}")

        # Show usage count as JSON (clean structured view)
        st.json(stats["tool_counts"])

        # Show the order in which tools were called
        if stats["tool_sequences"]:
            st.write("**Tool call sequence:**")
            st.write(" → ".join(stats["tool_sequences"]))

        # ==============================
        # GENERATE LOG FILE
        # ==============================

        # Create readable timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create formatted log content
        log_content = f"""
=== NORMALOBJECTS CHAOS MODE LOG ===
Timestamp: {timestamp}

COMPLAINT:
{complaint}

RESPONSE:
{response}

=== TOOL USAGE ===
Total tool calls: {stats['total_tool_calls']}
Most used tool: {stats['most_used']}
Tool usage counts: {stats['tool_counts']}
Tool call sequence: {stats['tool_sequences']}
"""

        # Create a unique filename using timestamp
        filename = f"complaint_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        # Save the log file locally in the project folder
        with open(filename, "w", encoding="utf-8") as f:
            f.write(log_content)

        st.success(f"Log file saved as {filename}")

        # ==============================
        # DOWNLOAD BUTTON
        # ==============================

        # Allow user to download the log directly
        st.download_button(
            label="⬇️ Download Log File",
            data=log_content,
            file_name=filename,
            mime="text/plain"
        )

