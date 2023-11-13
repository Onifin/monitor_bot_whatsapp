import requests
from dotenv import load_dotenv
import os

#Carregando variáveis de ambiente
load_dotenv()

# Variáveis necessárias

access_token = os.environ["TOKEN"]
bot_number_id = os.environ['NUMBER_ID']

url = f"https://graph.facebook.com/v17.0/{bot_number_id}/messages"

def send_message(message, number):
  # Cria o cabeçalho da requisição
  headers = {
    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json",
  }

  # Cria o corpo da requisição
  data = {
    "messaging_product": "whatsapp",
    "to": number,
    "text": {"body": message}
  }

  # Faz a requisição
  response = requests.post(url, headers=headers, json=data)

  # Processa a resposta da requisição
  if response.status_code == 200:
    print("Mensagem enviada com sucesso.")
  else:
    print("Erro ao enviar mensagem: {}".format(response.status_code))

  return response.status_code