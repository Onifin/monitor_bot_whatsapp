import requests
from dotenv import load_dotenv
import os
import json

#Carregando variáveis de ambiente
load_dotenv()

# Variáveis necessárias

access_token = os.environ['TOKEN_WPP']
bot_number_id = os.environ['NUMBER_ID']

url = f"https://graph.facebook.com/v18.0/{bot_number_id}/messages"

def send_message(number, message):
  headers = {
      "Authorization": "Bearer " + access_token,
      "Content-Type": "application/json"
  }

  data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": number,
    "type": "text",
    
    "text": {
      "preview_url": False,
      "body": message
    }
  }

  response = requests.post(url, headers=headers, data=json.dumps(data))

  return response