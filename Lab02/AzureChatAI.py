
import os
import base64
from openai import AzureOpenAI
from googlesearch import search

endpoint = os.getenv("ENDPOINT_URL", "https://sw-openai-lab02.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "Your Azure OpenAI API Key")

#使用金鑰型驗證，將 Azure OpenAI 服務用戶端初始化
client = AzureOpenAI(
    azure_endpoint = endpoint,
    api_key = subscription_key,
    api_version = "2024-05-01-preview"
)

# 對話函式
def get_reply(messages):
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages
        )
        reply = response.choices[0].message.content
    except Exception as err:
        reply = f"發生 {err.error.type} 錯誤\n{err.error.message}"
    return reply

# 簡易對話程式
# while True:
#     msg = input("你說：")
#     if not msg.strip():
#         break
#     messages = [
#         {"role": "system", "content": [{ "type": "text", "text": "您是協助人員找資訊的 AI 助理"
#                 }]},
#         {"role": "user", "content": [{ "type": "text", "text": msg }]}
#     ]
#     reply = get_reply(messages)
#     print(f"AI 說：{reply}")

# hist = []       # 歷史對話紀錄
# backtrace = 2   # 記錄幾組對話

# # 記憶對話紀錄的函式
# def chat(sys_msg, user_msg):
#     hist.append({"role": "user", "content": user_msg})
#     reply = get_reply(hist + [{"role": "system", "content": sys_msg}])

#     while len(hist) >= 2 * backtrace:   # 超過記錄限制
#         hist.pop(0)                     # 移除最舊紀錄
    
#     hist.append({"role": "assistant", "content": reply})
#     return reply



# 能接續對話的 AI 程式
# sys_msg = input("你希望 AI 扮演：")
# if not sys_msg.strip(): sys_msg = '小助理'
# print()
# while True:
#     msg = input("你說：")
#     if not msg.strip(): break
#     reply = chat(sys_msg, msg)
#     print(f"{sys_msg}: {reply}\n")
# hist = []

# 加入搜尋功能
hist=[]
backtrace = 2

def chat_w(sys_msg, user_msg, search_google=True):
    web_res=[]
    if search_google == True :
        content = "以下為已發生的事實：\n"
        for res in search(user_msg, advanced=True,
                          num_results=5, lang="zh-TW"):
            content += f"標題：{res.title}\n" \
                        f"摘要：{res.description}\n\n"
            content += "請依照上述事實回答問題。\n"
            web_res = [{"role": "user", "content": content}]
        web_res.append({"role": "user", "content": user_msg})
    
    while len(hist) >= 2 * backtrace:
        hist.pop(0)

    reply_full = ""
    for reply in get_reply(
        hist + web_res + [{"role": "system", "content": sys_msg}]):
        reply_full += reply
        yield reply
    hist.append({"role": "user", "content": user_msg})
    while len(hist) >= 2 * backtrace:
        hist.pop(0)
    hist.append({"role": "assistant", "content": reply_full})

sys_msg = '小助理'

while True:
    msg = input("你說：")
    if not msg.strip(): break
    print(f"{sys_msg}: ", end="")

    for reply in chat_w(sys_msg, msg, search_google=True):
        print(reply, end="")
    print("\n")
hist = []