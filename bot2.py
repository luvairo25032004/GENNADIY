import vk_api
import time
import random
token = os.environ.get("BOT_TOKEN") 
vk = vk_api.VkApi(token=token)
vk._auth_token()
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
            	vk.method("messages.send", {"peer_id":id, "message":"Воу, воу, воу! \n  Приветствую тебя, мой новый друг! \n Как у тебя дела?", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "сколько в мире гендеров":
            	vk.method("messages.send", {"peer_id":id, "message":"Два", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "команды":
                vk.method("messages.send", {"peer_id":id, "message": "```Вот список команд, дружок! \n Привет - приветствие \n Команды - узнать список команд \n Уроки - узнать уроки на завтра```", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "уроки":
            	vk.method("messages.send", {"peer_id":id, "message": "```Вот Уроки на завтра, дружок! \n 1. (Физика) \n 2. (Физика) \n 3. (История) \n 4. (География) \n 5. (Английский) \n 6. (Алгебра)```", "random_id": random.randint(1, 2147483647)})
            else:
            	vk.method("messages.send", {"peer_id":id, "message": "```Извини, но я ещё не могу Понимать Марсианский язык! \n Напиши КОМАНДЫ - чтобы узнать список функций бота```", "random_id": random.randint(1, 2147483647)})



    except Exception as E:
            time.sleep(1)
