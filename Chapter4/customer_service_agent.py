import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, ModelSettings

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create a tool
@function_tool
def get_order_status(orderID: int) -> str:
    """Returns the order status given an order ID"""
    if orderID in (100, 101):
        return "Delivered"
    elif orderID in (200, 201):
        return "Delayed"
    elif orderID in (300, 301):
        return "Cancelled"

# Define an agent
agent = Agent(
    name="Customer service agent",
    instructions="You are a customer service agent that must always use the backend system to check order status. Do not guess.",
    model="gpt-4o",
    tools=[get_order_status],
    model_settings=ModelSettings(tool_choice="required")
)

# Run the Control Logic Framework
result = Runner.run_sync(agent, "Can you check the status of Order ID 101?")
# Print the result
print(result.final_output)