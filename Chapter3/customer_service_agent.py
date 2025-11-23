# Required imports
import os
from dotenv import load_dotenv
from agents import Agent, Runner
# Load environment variables from the .env file
load_dotenv()
# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
# Define an agent
agent = Agent(name="Customer service agent",
              instructions="You are an AI Agent that helps respond to customer queries for a local paper company",
              model="gpt-4o")
# Run the Control Logic Framework
result = Runner.run_sync(agent, "How do I cancel my order?")
# Print the result
print(result.final_output)