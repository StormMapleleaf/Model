from flask import Flask, request, jsonify
from state_save import chat
from flask_cors import CORS
from langchain_core.messages import HumanMessage

app = Flask(__name__)
CORS(app)
# 配置保持不变，可以动态设置
config = {"configurable": {"thread_id": "abc123"}}

@app.route('/chat', methods=['POST'])
def chat_api():
    user_query = request.json.get('query')
    
    if user_query.lower() == 'exit':
        return jsonify({"message": "对话已结束。"})

    # 创建消息并发送给模型
    input_messages = [HumanMessage(user_query)]
    output = chat.invoke({"messages": input_messages}, config)

    # 提取模型生成的最后一条消息
    last_message = output["messages"][-1]
    return jsonify({"response": last_message.content})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  # 使其可通过网络访问
