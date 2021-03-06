from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

#  Example from the walkthrough
# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)

def ws_message(message):
    Group("chat").send({
        "text": message.content['text'],
    })

# Connected to websocket.connect
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
