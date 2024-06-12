from flask import Flask, session, jsonify, request
from dotenv import load_dotenv

import os
import logging
import json

from bot_functions import send_message
from history import *

import google.generativeai as genai

#GEMINI 

gemini_token = os.environ['GEMINI_TOKEN']
genai.configure(api_key=gemini_token)

model = genai.GenerativeModel('gemini-pro')

#message history

bot_memory = history_handler()

#init Flask
app = Flask(__name__)
app.secret_key = 'senha'

#authentication route
@app.route("/", methods=['GET'])
def get():

  args = request.args
  args = args.to_dict()

  return(args['hub.challenge'])

#webhook for whatsapp api
@app.route("/", methods=['POST'])
def post():  
  
  request_json = request.json

  """
  Recebemos diversos tipos de informação da api do whatsapp business.
  Caso a informação requerida no try for satisfeita, então uma mensagem foi recebida pelo bot. 
  Caso contrário foi alguma informação não necessária, tais como, status de mensagem enviada, status de mensagem recebida, status de mensagem lida ou outros.
  """
  
  try:
    number = request_json['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
    user_message = request_json['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
  except:
    return(request.json) 

  h = bot_memory.get_history(number) 
  add = h.append_message(user_message, "user")

  if(not add):
    return(request.json)
  
  messages = h.get_chat()
  response = model.generate_content(messages)

  #Verifica se a mensagem foi devolvida pela api do Gemini e retorna o feedback
  if(not response.candidates):
    h.pop_message()
    send_message(number, "Não entendi o que você falou")
    return(request.json)
  
  #Responde a mensagem, caso a requisição não fira nenhuma regra da do Gemini
  try: 
    send_message(number, response.text)
    h.append_message(response.text, "model")
  except:
    h.pop_message()
    send_message(number, "Não consigo responder esse tipo de pergunta")
    return(request.json) 


  if(h.check_pendding_messages()):
    for i in range(len(h.queue)):
      print("entrou")
      msg = h.get_pendding_message()
      h.append_message(msg, "user")
      messages = h.get_chat()
      print("MESSAGES:")
      print(messages)
      response = model.generate_content(messages)
      send_message(number, response.text)
      h.append_message(response.text, "model")

  #bot_memory.change_history(h, number)
  return(request.json)
    

if __name__ == "__main__":
  app.run(debug=True)
