import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

myApiKey = os.getenv("GROQ_API_KEY")

if not myApiKey:
    print("API key not found")
    exit()

client = Groq(api_key=myApiKey)

model = "openai/gpt-oss-120b"

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Give me a creative name for a coffee shop."
    }
]

# Temperature = 0
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.0
)

print("Temperature 0:")
print(response.choices[0].message.content)


# Temperature = 1
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1.0
)

print("\nTemperature 1:")
print(response.choices[0].message.content)


# Temperature = 2
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2.0
)

print("\nTemperature 2:")
print(response.choices[0].message.content)