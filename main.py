
from agent.main_agent import create_agent_instance


def format_response(content):
    if isinstance(content, list):
        return "\n".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("type") == "text"
        )

    return str(content)


def main():
    print("\n🤖 AI Agent with Tool Calling")
    print("Ask me to calculate or search project information.")
    print("Type 'exit' to stop.\n")

    try:
        agent = create_agent_instance()

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("AI Agent: Goodbye!")
                break

            if not user_input:
                continue

            try:
                response = agent.invoke({
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                })

                for message in response["messages"]:
                    if message.type == "tool":
                        print(f"[Tool Used: {message.name}]")

                answer = response["messages"][-1].content

                print("\nAI Agent:", format_response(answer), "\n")

            except Exception as error:
                print("\nAI Agent: Sorry, something went wrong.")
                print("Error:", str(error), "\n")

    except Exception as error:
        print("Could not start the AI Agent.")
        print("Error:", str(error))


if __name__ == "__main__":
    main()
