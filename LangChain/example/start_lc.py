from langchain_community.chat_models import ChatOllama

# 导入输出解释器   字符串输出
from langchain_core.output_parsers import StrOutputParser

#导入模版相关的库
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model = "llama3.1:8b",base_url = "http://94.191.48.110:6399")
ans = llm.invoke('你好')
print(ans)

# #使用输出解释器格式化数据
# strparse = StrOutputParser()
# anstr = strparse.invoke(ans)
# print(anstr)





# #模版


# llm =  ChatOllama(model = "llama3.1:latest")
# strparse = StrOutputParser()



# #模版字符串
# system_template = "你现在要将用户说的话翻译成为 {language} "

# #将模版作为信息传递给提示词模版
# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template), ("user", "{text}")]
# )

# #调用模版传入数据
# result = prompt_template.invoke({"language": "英语", "text": "你好啊，哥哥"})

# print(result)


# chain = prompt_template | llm | strparse


# #执行操作练
# ans = chain.invoke({"language": "德语", "text": "你好啊，哥哥"})

# print(ans)
