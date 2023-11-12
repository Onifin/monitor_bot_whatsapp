from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

#carregando dados do dotenv
load_dotenv()

from bot_functions import send_message

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

mensagem = "Bem-vindo ao AVE - Seu Assistente Virtual Educacional!"

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def teste():

    #send_message(mensagem, os.environ['MY_NUMBER'])

    if request.method == 'GET':
        args = request.args
        args = args.to_dict()
        print("GET")
        return(args['hub.challenge'])
    
    print("dfhdsfhdsfh")
    
    



#webhook para receber mensagens
@app.route('/webhook', methods=['GET'])
def webhook():
    if request.method == 'GET':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"

if __name__ == "__main__":
    app.run(debug=True)
