from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=50,
    n=1,
    temperature=0,
    messages=[
        {"role":"user","content":"hello"}
    ]

)
for choice in response.choices:
    print(choice.message.content)
