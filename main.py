import asyncio
import aiosqlite
import json
import ast
from random import getrandbits, randint
from aiovk.longpoll import BotsLongPoll
from aiovk.sessions import TokenSession
from aiovk.api import API

from vars import Variables
from commands import Games


class Bot:
    def __init__(self, token, group_id, donationapp_id=None, debug=True):
        self.token = token
        self.group_id = group_id
        self.loop = asyncio.get_event_loop()
        self.empty_keyboard = Variables().empty_keyboard
        self.keyboard = {"one_time": False, "inline": False, "buttons": Variables(app_id=donationapp_id, owner_id=-group_id, hash=getrandbits(32)).keyboard}
        self.pics_beer = Variables().pics_beer
        self.dice_var = Variables().dice_var
        self.notifications = Variables().notifications
    

    def handler(self):
         return self.loop.run_until_complete(self.__async_handler())
    

    async def create_tables(self):
        async with aiosqlite.connect('db.db') as db:
            await db.execute('CREATE TABLE IF NOT EXISTS penis(vk_id INTEGER, value INTEGER, day INTEGER, UNIQUE(vk_id));')
            await db.execute('CREATE TABLE IF NOT EXISTS gaytest(vk_id INTEGER, value INTEGER, day INTEGER);')
            await db.execute('CREATE TABLE IF NOT EXISTS gachitest(vk_id INTEGER, value INTEGER, day INTEGER);')
            await db.commit()

    async def __async_handler(self):
        await self.create_tables()
        async with TokenSession(self.token) as session:
            self.api = API(session)
            self.longpoll = BotsLongPoll(self.api, group_id=self.group_id)
            async for event in self.longpoll.iter():
                    # print(event)
                    match event["type"]:
                        case "message_new":
                            message = event["object"]["message"]
                            await self.msg_handler(msg_obj=message)
                            print(f"From: {message['from_id']}\tPeer: {message['peer_id']}\tText: {message['text']}")
                        case _:
                            print(f"Type: {event['type']}\tObject: {event['object']}")


    async def msg_handler(self, msg_obj):
        text = msg_obj['text']
        from_id = msg_obj['from_id']
        peer_id = msg_obj['peer_id']
        if any(elem in text for elem in self.notifications):
            resp_text = 'Иди нахуй со своими all\'ами'
            await self.send_msg(resp_text,
                                peer_id,
                                keyboard=self.keyboard)
            return
        command = ""
        if 'payload' in msg_obj.keys():
            payload = ast.literal_eval(msg_obj['payload'])
            command = payload['command']
        match command:
            case 'beer':
                resp_text = "🍺🍺🍺Брат, держи пивко🍺🍺🍺"
                await self.send_msg(resp_text,
                                peer_id,
                                attachment=self.pics_beer[randint(0, 5)],
                                keyboard=self.keyboard)
            case 'dice':
                resp_text, attach = await Games.rnd_dice()
                await self.send_msg(resp_text,
                                peer_id,
                                attachment=attach,
                                keyboard=self.keyboard)
            case 'coin':
                resp_text, attach = await Games.rnd_coin()
                await self.send_msg(resp_text,
                                peer_id,
                                attachment=attach,
                                keyboard=self.keyboard)
            case 'penis':
                resp_text = await Games.get_penis(from_id, self.api)
                await self.send_msg(resp_text,
                                peer_id,
                                keyboard=self.keyboard)
            case 'gaytest':
                resp_text = await Games.gay_test(from_id, self.api)
                await self.send_msg(resp_text,
                                peer_id,
                                keyboard=self.keyboard)
            case 'gachitest':
                resp_text, attach = await Games.gachi_test(from_id, self.api)
                await self.send_msg(resp_text,
                                peer_id,
                                attachment=attach,
                                keyboard=self.keyboard)
            case 'hide':
                resp_text = "Клавиатура убрана"
                await self.send_msg(resp_text,
                                    peer_id,
                                    keyboard=self.empty_keyboard)
            case _:
                resp_text = "Бро, держи команды"
                await self.send_msg(resp_text,  
                                    peer_id,
                                    keyboard=self.keyboard)
    

    async def send_msg(self, message, peer_id, attachment=None, keyboard=None):
        if not keyboard:
            keyboard = self.empty_keyboard
        await self.api('messages.send',
                       random_id=getrandbits(32),
                       message=message,
                       peer_id=peer_id,
                       attachment=attachment,
                       keyboard=json.dumps(keyboard))                    


if __name__ == '__main__':
    bot = Bot('800771244e789784825e24d2041addf8d70e3b22a2e0fbea59b104f9f6ccb990ce6f8cbcbd60f6fd0d471', 
              185504939,
              5727453)
    bot.handler()

