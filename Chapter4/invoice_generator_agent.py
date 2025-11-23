import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, StopAtTools

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

@function_tool
def create_invoice(orderID: int) -> str:
    return f"Invoice for Order {orderID}: $123.45 (Generated on 2025-11-23)"

agent = Agent(
    name="Invoice generator agent",
    instructions="Generate and return an invoice when requested.",
    model="gpt-4o",
    tools=[create_invoice],
    stop=StopAtTools.stop_at_tool_names(["create_invoice"])
)

# Run the Control Logic Framework
result = Runner.run_sync(agent, "Please create an invoice for Order 300")
# Print the result
print(result.final_output)