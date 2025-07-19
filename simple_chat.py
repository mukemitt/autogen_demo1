import os
import autogen
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for the language model
config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
]

# Configuration for the agents
llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
}

def main():
    # Create a UserProxyAgent (represents the human user)
    user_proxy = autogen.UserProxyAgent(
        name="UserProxy",
        system_message="A human admin who will provide the task and manage the conversation.",
        code_execution_config={"last_n_messages": 2, "work_dir": "coding"},
        human_input_mode="TERMINATE",
    )

    # Create an AssistantAgent (AI assistant)
    assistant = autogen.AssistantAgent(
        name="Assistant",
        system_message="You are a helpful AI assistant. You can help with various tasks including writing code, answering questions, and providing explanations.",
        llm_config=llm_config,
    )

    # Create a ChatManager for group chat
    groupchat = autogen.GroupChat(
        agents=[user_proxy, assistant],
        messages=[],
        max_round=10,
    )

    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
    )

    # Start the conversation
    print("=== AutoGen Simple Chat Demo ===")
    print("This is a simple multi-agent chat application using AutoGen.")
    print("The assistant will help you with various tasks.")
    print("Type 'exit' to end the conversation.\n")

    # Initiate chat
    user_proxy.initiate_chat(
        manager,
        message="Hello! I'm ready to start our conversation. What would you like to work on today?",
    )

if __name__ == "__main__":
    main()