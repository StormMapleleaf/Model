from state_save import chat
from langchain_core.messages import HumanMessage

def main():
    # 配置保持不变，可以动态设置
    config = {"configurable": {"thread_id": "abc123"}}
    
    # 循环获取用户输入
    while True:
        query = input("用户: ")

        if query.lower() == 'exit':
            print("对话已结束。")
            break

        # 创建消息并发送给模型
        input_messages = [HumanMessage(query)]
        output = chat.invoke({"messages": input_messages}, config)

        # 打印模型的最新回复
        last_message = output["messages"][-1]   #从 output 对象中提取模型生成的最后一条消息
        print("小机器人: ", end="")
        print(last_message.content)                #打印消息的文本
        print()

if __name__ == "__main__":
    main()
