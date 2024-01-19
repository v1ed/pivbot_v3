import asyncio
from random import randint
from datetime import datetime
import aiosqlite

from vars import Variables

class Games:
    async def get_penis(id, api):
        user = await api('users.get',
                    user_ids=(id), 
                    name_case="gen", 
                    fields='first_name, second_name, sex')
        f_name = user[0]['first_name']
        l_name = user[0]['last_name']
        if user[0]['sex'] != 2:
            return "У вас не члена..."
        curday = datetime.today().day
        async with aiosqlite.connect('db.db') as db:
            cursor = await db.cursor()
            await cursor.execute(f"SELECT * FROM penis WHERE vk_id={id};")
            db_data = await cursor.fetchall()
            if db_data:
                _, db_value, db_day = db_data[0] 
                if db_day != curday:
                    db_value = randint(1, 40)
                    await cursor.execute(f"UPDATE penis SET value={db_value}, day={curday};") 
                    await db.commit()
                return f"Размер члена @id{id} ({f_name} {l_name}) - {db_value} см."
            db_value = randint(1, 40)
            await cursor.execute(f"INSERT INTO penis (vk_id, value, day) VALUES ({id}, {db_value}, {curday})")
            await db.commit()
            return f"Размер члена @id{id} ({f_name} {l_name}) - {db_value} см."
    
    async def gay_test(id, api):
        verdicts_m = Variables().verdicts_m
        verdicts_w = Variables().verdicts_w
        curday = datetime.today().day
        user = await api('users.get',
                    user_ids=(id), 
                    name_case="gen", 
                    fields='first_name, second_name, sex')
        sex = user[0]['sex']
        f_name = user[0]['first_name']
        l_name = user[0]['last_name']
        async with aiosqlite.connect('db.db') as db:
            cursor = await db.cursor()
            await cursor.execute(f"SELECT * FROM gaytest WHERE vk_id={id};")
            db_data = await cursor.fetchall()
            if db_data:
                _, db_value, db_day = db_data[0] 
                if db_day != curday:
                    db_value = randint(1, 100)
                    await cursor.execute(f"UPDATE gaytest SET value={db_value}, day={curday};") 
                    await db.commit()
                return f"@id{id} ({f_name} {l_name}) {'гей' if sex == 2 else 'лесбиянка'} на {db_value}%\nВердикт: {verdicts_m[int(db_value) // 20] if sex == 2 else verdicts_w[int(db_value) // 20]}"
            db_value = randint(1, 100)
            await cursor.execute(f"INSERT INTO gaytest (vk_id, value, day) VALUES ({id}, {db_value}, {curday})")
            await db.commit()
            return f"@id{id} ({f_name} {l_name}) {'гей' if sex == 2 else 'лесбиянка'} на {db_value}%\nВердикт: {verdicts_m[int(db_value) // 20] if sex == 2 else verdicts_w[int(db_value) // 20]}"

    async def gachi_test(id, api):
        pics = Variables().gachi_pics
        curday = datetime.today().day
        user = await api('users.get',
                    user_ids=(id), 
                    name_case="gen", 
                    fields='first_name, second_name')
        f_name = user[0]['first_name']
        l_name = user[0]['last_name']
        async with aiosqlite.connect('db.db') as db:
            cursor = await db.cursor()
            await cursor.execute(f"SELECT * FROM gachitest WHERE vk_id={id};")
            db_data = await cursor.fetchall()
            if db_data:
                _, db_value, db_day = db_data[0] 
                if db_day != curday:
                    db_value = randint(0, 18)
                    await cursor.execute(f"UPDATE gachitest SET value={db_value}, day={curday};") 
                    await db.commit()
                return f"@id{id} ({f_name} {l_name}) сегодня {pics[int(db_value)]['name']}", pics[db_value]['photo']
            db_value = randint(0, 18)
            await cursor.execute(f"INSERT INTO gachitest (vk_id, value, day) VALUES ({id}, {db_value}, {curday})")
            await db.commit()
            return f"@id{id} ({f_name} {l_name}) сегодня {pics[int(db_value)]['name']}", pics[db_value]['photo']

    async def rnd_dice():
        rnd = randint(0, 5)
        text = f"Выпало {rnd+1}"
        attach = Variables().dice_var[rnd]
        return text, attach
    
    async def rnd_coin():
        rnd = randint(0, 100)
        if rnd < 47:
            text = "Выпал орел"
            attach = Variables().coin[0]
        elif rnd >= 53: 
            text = "Выпала решка"
            attach = Variables().coin[1]
        else:
            text = "Выпало ребро!"
            attach = Variables().coin[2]
        return text, attach