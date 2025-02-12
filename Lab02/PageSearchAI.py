
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

for item in search("NBA 2024 冠軍隊", advanced=True, num_results=3):
    print(item.title)
    print(item.description)
    print(item.url)
    print()