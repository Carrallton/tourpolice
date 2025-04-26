import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger('chatbot')

class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connection established.")
        await self.accept()

    async def disconnect(self, close_code):
        logger.info("WebSocket connection closed.")

    async def receive(self, text_data):
        logger.debug(f"Received message: {text_data}")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response = self.process_message(message)
        await self.send(text_data=json.dumps({'response': response}))
        logger.debug(f"Sent response: {response}")

    def process_message(self, message):
        return f"Вы сказали: {message}"