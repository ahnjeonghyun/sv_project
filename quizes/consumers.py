import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db                import database_sync_to_async

from users.models               import Language
from quizes.models              import Quiz,Reward

class QuizLoad(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'all'

        #그룹생성
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, event):
        await self.send({'message':'disconnect_websocket'})

    async def receive(self,text_data):
        data       = json.loads(text_data)
        status     = data.get('status',None)

    async def accept_message(self, event):
        text = event["status"]

        await self.send( json.dumps(
        {
            "type" : "websocket.send",
            "status" : text
        }, ensure_ascii = False))
    
    async def reward_message(self, event):
        text     = event["status"]
        quiz_num = event["quiz_num"]

        await self.send(json.dumps({
            "type"     : "reward_message",
            "status"   : text,
            "quiz_num" : quiz_num
        }, ensure_ascii=False))    
    
    async def quiz_message(self, event):
        text     = event["status"]
        quiz_num = event["quiz_num"]

        await self.send(json.dumps({
            "type"     : "quiz_message",
            "status"   : text,
            "quiz_num" : quiz_num
        }, ensure_ascii=False))
    
    async def user_answer_message(self, event):
        text = event["status"]

        await self.send(json.dumps({
            "type"   : "user_answer_message",
            "status" : text
        }, ensure_ascii = False))
    
    async def result_message(self, event):
        text = event["status"]

        await self.send(json.dumps({
            "type"   : "result_message",
            "status" : text
        }, ensure_ascii = False))