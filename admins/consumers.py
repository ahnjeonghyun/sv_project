import json
import my_settings

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db                import database_sync_to_async

class Admin(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'all'

        #그룹생성
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, event):

        await self.send({
            'message':'disconnect_websocket'
        })

    async def receive(self,text_data):
        data = json.loads(text_data)
        print(data)
        status = data.get('status', None)

        if status == "입장허용":
            #group_message 함수로 event 생성
            await self.channel_layer.group_send(
                self.group_name,{
                "type" : "accept_message",     #type 값이 전송할 함수이름과 동일해야함
                "status" : status 
                }
            )
        
        if status == "보상확인":
            quiz_num = data["quiz_num"]
            #group_message 함수로 event 생성
            await self.channel_layer.group_send(
                self.group_name,{
                    "type"     : "reward_message",     
                    "status"   : status,
                    "quiz_num" : quiz_num
                }
            )

        if status == "퀴즈시작":
            quiz_num = data["quiz_num"]
            await self.channel_layer.group_send(
                self.group_name,{
                    "type"     : "quiz_message",    
                    "status"   : status,
                    "quiz_num" : quiz_num
                }
            )
        
        if status == "정답확인":
            await self.channel_layer.group_send(
                self.group_name,{
                    "type"     : "user_answer_message",    
                    "status"   : status,
                }
            )

        if status == "결과확인":
            await self.channel_layer.group_send(
                self.group_name,{
                    "type"     : "result_message",    
                    "status"   : status,
                }
            )

    async def accept_message(self, event):
        text = event["status"]
        #그룹으로 실제로 메세지를 보내는곳
        await self.send( json.dumps({
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
        }, ensure_ascii = False))

    async def quiz_message(self, event):
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

    async def result_message(self, event):
        text = event["status"]

        await self.send(json.dumps({
            "type"   : "result_message",
            "status" : text
        }, ensure_ascii = False))

    # @database_sync_to_async
    # def get_chart(self,language,language_id):
    #     pass
        