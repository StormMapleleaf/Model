import requests

url = 'http://127.0.0.1:8000/chat'
user_input = "你好，聊天机器人！"

response = requests.post(url, json={"query": user_input})

if response.status_code == 200:
    print("小机器人: ", response.json().get('response'))
else:
    print("请求失败，状态码:", response.status_code)
