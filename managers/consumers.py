import json
from random import randint
from time import sleep


from channels.generic.websocket import AsyncWebsocketConsumer

class GraphConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()

        for i in range(1000):
            self.send(json.dumps({'value':randint(-20,20)}))
            await sleep(1)
