# model初始化
from langchain_community.chat_models import ChatOllama
model = ChatOllama(model = "llama3.1:8b",base_url = "http://139.186.222.157:6399")

# 输出格式化
from langchain_core.output_parsers import StrOutputParser
ans_format = StrOutputParser()