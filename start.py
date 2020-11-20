from telethon import TelegramClient, events, Button

client = TelegramClient('anohn', 1651836, "f8244276a17b5b2a711e7501857c8e55")

@client.on(events.NewMessage(pattern='(?i)https://www.zee5.com'))
async def handler(event):
    link =event.text.split('/')[-1]
    
    chat = await event.get_chat()
    markup = client.build_reply_markup(Button.url("https://www.zee5.com/tvshows/details/sembaruthi/0-6-675/sembaruthi-november-18-2020/0-1-manual_7adlhget67b0"+link))
    await client.send_message(chat, link, buttons=markup)
   #await client.send_message(chat,"445")
    
   
    
client.start()
client.run_until_disconnected()