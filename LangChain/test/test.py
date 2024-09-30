import streamlit as st
from state_save import chat
from langchain_core.messages import HumanMessage

def main():
    st.title("聊天机器人")
    
    # 配置保持不变，可以动态设置
    config = {"configurable": {"thread_id": "abc123"}}
    
    # 初始化会话状态
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # 用户输入框
    user_input = st.text_input("用户输入:", "")
    
    if st.button("发送"):
        if user_input:
            # 存储用户消息
            st.session_state.messages.append({"role": "user", "content": user_input})

            # 创建消息并发送给模型
            input_messages = [HumanMessage(user_input)]
            output = chat.invoke({"messages": input_messages}, config)

            # 打印模型的最新回复
            last_message = output["messages"][-1]
            st.session_state.messages.append({"role": "bot", "content": last_message.content})

    # 显示对话历史
    for msg in st.session_state.messages:
        role = "用户" if msg["role"] == "user" else "小机器人"
        st.write(f"{role}: {msg['content']}")

if __name__ == "__main__":
    main()
