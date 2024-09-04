from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

def text_generation():  
    client = OpenAI(api_key=os.getenv('APIKEY_PRODUCTION'))
    data = input('Digita tu entrada:\n')
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpdesk tech assistant."},
            {
                "role": "user",
                "content": data
            }
        ]
    )
    return completion.choices[0].message.content