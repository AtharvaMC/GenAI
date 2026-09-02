import os
import json
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Not found")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"



# structure it
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}

text="Hello My name is Ajay. I am raising this ticket because my iPhone has completely stopped working as of yesterday. It is entirely unresponsive, will not turn on, and does not respond to a charge. My address is delhi. My email is abc@gmail.com. My contact number is 82134"
prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)


answer=response.choices[0].message.content
print(answer)


raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

with open("response.json", "w", encoding="utf-8") as file:
    file.write(ticket.model_dump_json(indent=4))

print(ticket.name)
print(ticket.email)
print(ticket.issue)
