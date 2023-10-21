from flask import Flask, jsonify, request
from heyoo import WhatsApp

from bot_functions import send_message

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

mensagem = "Bem-vindo ao AVE - Seu Assistente Virtual Educacional!"

app = Flask(__name__)

@app.route("/")
def teste():

    #messenger = WhatsApp(token=TOKEN, phone_number_id=PHONE_NUMBER_ID)
    #messenger.send_message(mensagem, "numero")

    send_message(mensagem, "5584987880923")

    return "<p>TESTE4</p>"

#webhook para receber mensagens
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"

if __name__ == "__main__":
    app.run(debug=True)


