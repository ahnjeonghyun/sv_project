import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db                import database_sync_to_async

from users.models               import Language,User

class User(AsyncWebsocketConsumer):
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
        data          = json.loads(text_data)
        # language_data = data.get('language',None)
        # movie_url     = await self.get_movie_url(language_data)

        # await self.send(json.dumps({'movie_url' : movie_url}))

    # 그룹으로 실제로 메세지를 보내는곳
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
        # print(event,"users")
        text     = event["status"]
        quiz_num = event["quiz_num"]

        await self.send(json.dumps({
            "type"     : "quiz_message",
            "status"   : text,
            "quiz_num" : quiz_num
        }, ensure_ascii = False))

    async def user_answer_message(self, event):
        text = event["status"]

        await self.send(json.dumps({
            "type"   : "user_answer_message",
            "status" : text
        }, ensure_ascii = False))
    
    # async def result_message(self, event):
    #     text = event["status"]

    #     await self.send(json.dumps({
    #         "type"   : "result_message",
    #         "status" : text
    #     }, ensure_ascii = False))


    # @database_sync_to_async
    # def get_movie_url(self,language_data):
    #     return Language.objects.get(language_type = language_data).movie_url