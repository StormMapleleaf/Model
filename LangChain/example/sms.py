#api key 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

from langchain_community.chat_models import ChatOllama

# 导入输出解释器   字符串输出
from langchain_core.output_parsers import StrOutputParser

#导入模版相关的库
from langchain_core.prompts import ChatPromptTemplate


import os

os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = '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'
os.environ['LANGCHAIN_ENDPOINT'] = "https://api.smith.langchain.com"
os.environ['LANGCHAIN_PROJECT'] = "pr-mundane-witness-28"


#模版


llm =  ChatOllama(model = "llama3.1:latest")
strparse = StrOutputParser()



#模版字符串
system_template = "你现在要将用户说的话翻译成为 {language} "

#将模版作为信息传递给提示词模版
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

#调用模版传入数据
result = prompt_template.invoke({"language": "英语", "text": "你好啊，你大爷的！"})

print(result)


chain = prompt_template | llm | strparse


#执行操作练
ans = chain.invoke({"language": "德语", "text": "你好啊，哥哥"})

print(ans)
