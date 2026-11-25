from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.calculator import calculator
from tools.file_lookup import file_lookup


def create_agent_instance():

    # Initialize Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    # Register tools
    tools = [calculator, file_lookup]

    # Create AI Agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""
        You are a helpful AI agent.

        Understand the user's request and choose the correct tool.

        Use calculator for mathematical calculations.
        Use file_lookup to search information in sample_data.txt.

        If no tool is needed, answer normally.
        Explain results clearly and simply.
        """
    )

    return agent
