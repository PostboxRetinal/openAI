from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

client = OpenAI(api_key=os.getenv('APIKEY_TESTING'))
data = input('Digita tu entrada:\n')
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": data
        }
    ]
)
print(f"Salida:\n{completion.choices[0].message.content}")