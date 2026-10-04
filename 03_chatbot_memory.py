import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END

# 改动 1：文件顶部多一行 import
from langgraph.checkpoint.memory import MemorySaver

llm = ChatOpenAI(
    model="glm-4.5-flash",  # 免费档，学习够用
    api_key=os.environ["ZHIPU_API_KEY"],
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)


def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}


g = StateGraph(MessagesState)
g.add_node("chatbot", chatbot)
g.add_edge(START, "chatbot")
g.add_edge("chatbot", END)
# app = g.compile()
# 改动 2：compile 时挂上存档器
app = g.compile(checkpointer=MemorySaver())


# while True:
#     user = input("你: ")
#     if user in ("q", "exit", "quit"):
#         break
#     result = app.invoke({"messages": [("user", user)]})
#     print("AI:", result["messages"][-1].content)
# 改动 3：invoke 时带上会话槽位
config = {"configurable": {"thread_id": "t1"}}
while True:
    user = input("你: ")
    if user in ("q", "exit", "quit"):
        break
    result = app.invoke({"messages": [("user", user)]}, config)
    print("AI:", result["messages"][-1].content)
