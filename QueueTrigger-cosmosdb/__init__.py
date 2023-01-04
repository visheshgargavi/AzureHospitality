import datetime
from email import message
import json
import logging
from xml.dom.minidom import Document

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def main(msg: func.ServiceBusMessage,documents: func.Out[func.Document]) -> None:
   logging.info('Python ServiceBus queue trigger processed message: %s',
               msg.get_body().decode('utf-8'))
   result = json.dumps({
        'body': msg.get_body().decode('utf-8')
    })
   message = msg.get_body().decode('utf-8')
   logging.info(message)
   logging.info(type(message))
   logging.info(type(result))
   documents.set(func.Document.from_json(result))
