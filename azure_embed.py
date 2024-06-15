import os
import langchain
#from openai import AzureChatOpenAI

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://vlb-tst-openai01.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "2c8083b8cef04c958c9f2a88894fcf3f"

os.environ["AZURE_OPENAI_API_VERSION"] = "2023-06-01-preview"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "testtest"

from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI

model = AzureChatOpenAI(
        azure_deployment="testtest",
        openai_api_version="2023-05-15"
)
message = HumanMessage(
    content="Translate this sentence from English to French. I love programming."
)
model.invoke([message])

# EMBEDDERS
client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-01",
  azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT") 
)

response = client.embeddings.create(
    input = "Your text string goes here",
    model= "text-embedding-ada-002"
)

text = "This is a test query."
print(response.model_dump_json(indent=2))

ChatOpenAI(openai_api_key=api_key, temperature=0, max_tokens=max_tokens, model_name=model)