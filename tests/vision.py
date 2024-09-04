from dotenv import load_dotenv
from openai import OpenAI
import os

def vision():

  client = OpenAI(api_key=os.getenv('APIKEY_PRODUCTION'))
  data = input('Digita tu entrada:\n')

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What’s in this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
              "detail": "low"
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )

  return response.choices[0].message.content