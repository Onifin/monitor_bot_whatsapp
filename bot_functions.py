import requests

# Variáveis necessárias

access_token = "access_token"
bot_number_id = "bot_number_id"

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