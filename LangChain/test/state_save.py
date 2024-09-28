from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from model_init import model,ans_format

# 定义一个新的状态图
# workflow：创建了一个 StateGraph 对象，用来管理这个工作流的状态。
# state_schema=MessagesState 指定了工作流中使用的状态结构是 MessagesState
workflow = StateGraph(state_schema=MessagesState)


# 定义调用模型的函数，写入状态。
def call_model(state: MessagesState):           #这个函数接收一个 MessagesState 对象作为输入，调用模型，并返回处理后的消息。
    response = model.invoke(state["messages"])  #调用模型方法 invoke，传入当前状态中的消息（state["messages"]），获取模型的响应。
    return {"messages": response}               #用于将模型响应的消息存入状态中。


#  定义状态图的节点和边
workflow.add_edge(START, "model")               # 将状态图中的 START 节点与名为 "model" 的节点连接起来。这个边定义了状态图中的执行顺序，从起点开始执行。
workflow.add_node("model", call_model)          # 将 "model" 节点添加到图中，并关联调用模型的函数 call_model。当工作流到达这个节点时，会执行 call_model 函数写入状态。

# 添加内存检查点
memory = MemorySaver()                          #创建一个 MemorySaver 对象，负责在工作流执行过程中保存状态到内存中。
chat = workflow.compile(checkpointer=memory)     #将工作流编译为一个应用（app），并使用 MemorySaver 作为检查点系统。这样，工作流的状态可以在不同步骤间保存和恢复

