#!/usr/bin/env python3
"""Debug script to understand why agent doesn't call tools."""

import os
import asyncio
import nest_asyncio
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

nest_asyncio.apply()

# Get API key from environment
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print("ERROR: OPENAI_API_KEY not set")
    exit(1)

OPENAI_MODEL = "gpt-5-nano"

# Define tools
def lookup_ticket(ticket_id: str) -> dict:
    """Look up details for a support ticket."""
    mock_tickets = {
        "5678": {
            "ticket_id": "5678",
            "status": "In Progress",
            "priority": "High",
            "user": "Alice Johnson",
            "issue": "Cannot access email"
        }
    }
    return mock_tickets.get(ticket_id, {"error": f"Ticket {ticket_id} not found"})


def search_knowledge_base(query: str) -> dict:
    """Search the IT knowledge base for help articles."""
    return {"query": query, "results": [], "count": 0}


def check_system_status(service_name: str) -> dict:
    """Check the operational status of a service."""
    return {"service": service_name, "status": "operational", "uptime": "99.9%"}


# Create agent
llm_model = LiteLlm(model=f"openai/{OPENAI_MODEL}", api_key=OPENAI_API_KEY)
agent = LlmAgent(
    name="it_support_agent",
    model=llm_model,
    description="An IT support agent",
    instruction="You are an IT support agent. Use the tools to help users.",
    tools=[lookup_ticket, search_knowledge_base, check_system_status]
)

print(f"✅ Agent created with {len(agent.tools)} tools")


async def test_agent(user_message: str):
    """Test the agent with debug output."""
    print(f"\n{'='*60}")
    print(f"Testing: {user_message}")
    print(f"{'='*60}")

    session_service = InMemorySessionService()
    session_id = "debug_session"
    user_id = "debug_user"

    await session_service.create_session(
        app_name="it_support_test",
        user_id=user_id,
        session_id=session_id,
        state={}
    )

    runner = Runner(
        app_name="it_support_test",
        agent=agent,
        session_service=session_service
    )

    content = types.Content(role='user', parts=[types.Part(text=user_message)])
    events = runner.run_async(user_id=user_id, session_id=session_id, new_message=content)

    print("\n📊 Events:")
    event_count = 0
    tool_count = 0

    async for event in events:
        event_count += 1
        print(f"\nEvent {event_count}: {type(event).__name__}")

        # Print all attributes
        print(f"  Attributes: {dir(event)}")

        # Check for tool_use
        if hasattr(event, 'tool_use'):
            print(f"  tool_use: {event.tool_use}")
            if event.tool_use:
                tool_count += len(event.tool_use)
                for tool in event.tool_use:
                    print(f"    Tool: {tool}")

        # Check for content
        if hasattr(event, 'content'):
            print(f"  content: {event.content}")

        # Check if final
        if hasattr(event, 'is_final_response'):
            print(f"  is_final: {event.is_final_response()}")

    print(f"\n📈 Summary: {event_count} events, {tool_count} tools called")


# Run test
asyncio.run(test_agent("What's the status of ticket 5678?"))
