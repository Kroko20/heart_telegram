import asyncio
import os
import time
from hearts import *
from pyrogram import Client

os.system("title heart telegram by Kroko20")
print("heart telegram by Kroko20")
delay = 0.1 #задержка для всех анимация

# авторизация в телегу
app = Client("telegram", 1000000, "777532bbjfibjodfijboifd")
app.start()

getchat = app.get_chat("me")

chatid = input("Введите chat_id (ваш chat_id: " + str(getchat.id) + "): ")
chatid = int(chatid)
delaystart = input("Задержка перед запуском (напишите 0 если не нужно): ")
time.sleep(int(delaystart))

async def main():
	message_obj = await app.send_message(chatid, heart_purple)
	print("Сообщение отправлено")
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_orange)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_purple)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_green)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_orange)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_purple)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_green)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_orange)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_purple)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_green)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, heart_purple)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_1)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_2)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_3)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_4)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_5)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_6)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_1_7)
	time.sleep(1)
	await app.edit_message_text(chatid, message_obj.id, anim_2_1)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_2)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_3)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_4)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_5)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_6)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_7)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_8)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_2_9)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_1)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_2)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_3)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_4)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_5)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_6)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_7)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_8)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_9)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_10)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_11)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_12)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_13)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_14)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_15)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_16)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_17)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_18)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_19)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_20)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_21)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_22)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_23)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_24)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_25)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_26)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_27)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_28)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_29)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_30)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_31)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_32)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_33)
	time.sleep(delay)
	await app.edit_message_text(chatid, message_obj.id, anim_3_34)
	time.sleep(0.7)
	await app.edit_message_text(chatid, message_obj.id, "developed by @mikoil")
	print("Сообщение завершено\ndeveloped by mikoil")
	await app.stop()

app.run(main())
