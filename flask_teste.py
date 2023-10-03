from flask import Flask, jsonify, request

from heyoo import WhatsApp

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def teste():

    token = ''

    id_numero = ''

    numero_receptor = ''

    mensagem = ""

    msg_W = WhatsApp(token, id_numero)

    msg_W.send_message(mensagem, numero_receptor)

    return "<p>TESTE</p>"

if __name__ == "__main__":
    app.run(debug=True)