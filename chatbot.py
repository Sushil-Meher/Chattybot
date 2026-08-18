from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatOllama(model = "qwen3:4b")

chat_history = [
    SystemMessage(content="You are Chattybot, a friendly and talkative AI assistant")
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(chat_history)

    chat_history.append(
        AIMessage(content=response.content)
    )

    print("AI: ",response.content)


    