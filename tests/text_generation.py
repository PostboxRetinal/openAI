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
            {"role": "system", "content": "Eres un asistente de helpdesk general."},
            {
                "role": "user",
                "content": data
            }
        ],
        max_tokens=100,
        temperature=0.5
    )
    return completion.choices[0].message.content