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
    "role": "system",
    "content": """You are a non-technical business user.
You don't understand programming or system architecture.
Explain the answer using simple real-world concepts.
Do not use technical jargon."""
}
message2 = {
    "role": "user",
    "content": "What is java and where it is used" 
}
# messages = [message,message2,message3,message4] 
messages = [message,message2] 

response = client.chat.completions.create(
    model=model,
    messages=messages
)
print("----------------Reply as normal user----------------")
print(response.choices[0].message.content)
message3 = {
    "role": "system",
    "content": "You are a senior backend software engineer." 
}
message4 = {
    "role": "user",
    "content": "What is java and where it is used" 
}
messages = [message3,message4] 

print("----------------Reply as software engineer----------------")
response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
with open("response.txt", "w", encoding="utf-8") as file:
    file.write("---------------- Reply as normal user ----------------\n")
    file.write(response.choices[0].message.content)
    file.write("\n\n")

    file.write("---------------- Reply as software engineer ----------------\n")
    file.write(response.choices[0].message.content)