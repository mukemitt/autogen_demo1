import os
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def main():
    # Configuration for the language model
    model_client = OpenAIChatCompletionClient(
        model="gpt-3.5-turbo",
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Create an AssistantAgent (AI assistant)
    assistant = AssistantAgent(
        name="Assistant",
        system_message="You are a helpful AI assistant. You can help with various tasks including writing code, answering questions, and providing explanations.",
        model_client=model_client,
    )

    # Start the conversation
    print("=== AutoGen Simple Chat Demo ===")
    print("This is a simple multi-agent chat application using AutoGen.")
    print("The assistant will help you with various tasks.")
    print("Type 'exit' to end the conversation.\n")

    # Run the assistant with a simple task
    result = await assistant.run(
        task="Hello! I'm ready to start our conversation. What would you like to work on today?"
    )
    print(result)

    # Close the model client
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())