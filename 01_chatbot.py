import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END

llm = ChatOpenAI(
    model="glm-4.5-flash",   # 免费档，学习够用
    api_key=os.environ["ZHIPU_API_KEY"],
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("chatbot", chatbot)
g.add_edge(START, "chatbot")
g.add_edge("chatbot", END)
app = g.compile()

result = app.invoke({"messages": [("user", "你好，一句话介绍你自己")]})
print(result["messages"][-1].content)
