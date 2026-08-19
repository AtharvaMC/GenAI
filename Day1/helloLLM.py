import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
myApiKey=os.getenv("GROQ_API_KEY")

if not myApiKey:
    print("key not found")

client = Groq(api_key=myApiKey)

model = "openai/gpt-oss-120b"

message = {
    "role": "user",
    "content": "What is capital of india"
}
message2 = {
    "role": "user",
    "content": "give the proper schedule week wise to explore capital" 
}

messages = [message,message2]

response = client.chat.completions.create(
    model=model,
    messages=messages
)
# print(response)
print(response.choices[0].message.content)
# answer=response.choices[0].messege.content
