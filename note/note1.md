StateGraph / node / edge / checkpointer

Q1｜LangGraph 的 StateGraph 是什么？
- 01-03.py 里哪几行在建图？MessagesState 里装的是什么？
g = StateGraph(MessagesState)
g.add_node("chatbot", chatbot)
g.add_edge(START, "chatbot")
g.add_edge("chatbot", END)
这些是在建图，就是建一个链路，定义起点终点，如果有分支看分支怎么走。MessagesState 装的是当前状态，可以理解为指针走到这里时携带的状态。


- 为什么叫「状态图」——每一步之间流动的到底是什么？
因为流动的就是状态，每一个状态怎么处理不关心，因为处理在钩子函数里，但是关心的是每一步的状态。

Q2｜node 是什么？
- 我们的 node 函数叫什么、干什么的？
我理解就是指针的指的当前的状态。它包含了所有携带的状态的集合。
- 它的输入和输出分别是什么（state 进、state 出）？
状态进，状态出。中间被函数处理了。

Q3｜edge 是什么？
- START→chatbot→END 两行在定义什么？
定义一条链路的起点和终点，还有中间环节经过了哪。
- 如果再加一个 node，要改哪几行？（这就是 W3 工具调用的伏笔，先想一眼）
看加在哪里，如果是加在chatbots前面，那就是改START后面接node，node后面接chatbot，如果改END，同理，END前是node，chatbot后面接node。

Q4｜checkpointer 是什么？
- 02 里它忘了你叫什么（无状态现形）；03 加了哪三行修好的？
checkpointer是检查点。1.加了导入memorySaver 2.编译的时候加了checkpointer=memorySaver 挂载了记忆器。3.加了config，invoke的时候带上了config。我的理解就是有个专门的线程去处理记忆，这个处理的线程在config里配好了。
- thread_id 换掉 / 进程重启，各发生什么？
tread_id换掉，应该会把内容做备份放到新的thread中。但是进程重启，应该会记忆清零。