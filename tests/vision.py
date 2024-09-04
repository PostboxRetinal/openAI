from dotenv import load_dotenv
from openai import OpenAI
import os

def vision():

  client = OpenAI(api_key=os.getenv('APIKEY_PRODUCTION'))
  prompt = input('Pregunta al modelo:\n')
  link = input('Ingresa el link de la imagen:\n')
  detail  = input('Ingresa la fidelidad de la imagen\n\n- 1. low res\n- 2. high res\n- 3. auto\n\n')
  if detail == '1':
    detail = 'low'
  elif detail == '2':
    detail = 'high'
  else:
    detail = 'auto'

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": prompt},
          {
            "type": "image_url",
            "image_url": {
              "url": link,
              "detail": detail
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )

  return response.choices[0].message.content