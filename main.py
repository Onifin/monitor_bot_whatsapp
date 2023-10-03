import logging

from heyoo import WhatsApp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

TOKEN = "TOKEN DO WHATSAPP BUSINESS"
PHONE_NUMBER_ID = "ID NÚMERO DO WHATSAPP BUSINESS"

messenger = WhatsApp(token=TOKEN, phone_number_id=PHONE_NUMBER_ID)
messenger.send_message("TESTE", "NÚMERO PARA O QUAL A MENSAGEM SERÁ ENVIADA")
