import logging #Библиотека для ведения логов, потом пригодится
import vk #Модуль для доступа к API
import vk.exceptions #Модуль с описанием исключений связанных с API
import time
tokenfile=open('token.txt','r')
#/////logss=open('loggs.txt','w')



quest=['Привет','привет','Как дела?','как дела?','Как дела','как дела']
ans=['Привет','Привет','Хорошо, как у тебя?','Хорошо, как у тебя','Хорошо, как у тебя','Хорошо, как у тебя','Хорошо, как у тебя','Хорошо, как у тебя']


def anser(vopr):
	for i in range (0,len(quest)+1):
		if i==len(quest):
			break
		if vopr==quest[i]:
			return ans[i]
	if i==len(quest):
		return 'Я не знаю такого вопроса'
	







logging.basicConfig(format='[# %(levelname)-10s [%(asctime)s]  %(message)s', level=logging.INFO) #Настройка логов, на будущее

logging.info("Сервис запущен") # Вывод инфы по авторизации
logging.info("Авторизация...")
token=tokenfile.readline()

try: # Попытка авторизации
       session = vk.Session(access_token=token)
       api = vk.API(session) #Создаём обьект класса API
except vk.exceptions.VkAuthError: # Если ошибка заключается в авторизации
        logging.info('Авторизация не удалась: неверный логин или пароль')

logging.info("Начат приём сообщений")
prev='blablablaalbalbalb' #Создаем предыдущее сообщение 
while True:
	last=api.messages.get(out=0,count=1,)
	if prev==last: 										#Если последнее прочитанное сообщение равно предыдущему, то мы проверяем через 15 сек. Также єто нужно чтобы бот не отвечал по 20 раз на 1 сообщение
		time.sleep(5)
	else: 												#Если последнее прочитанное сообщение не равно предыдущему, то мы проверяем через 3 сек (в случае "оживленной" переписки")
		#print(last_message)
		print(last[1]['body'])

		api.messages.send(user_id=last[1]['uid'], message=anser(last[1]['body'])) #Отправка ответа
		#/////print('Ответ: '+anser(last[1]['body'])
		#/////logss.write('Вопрос: '+last[1]['body']+'    Ответ: '+anser(last[1]['body']) 

		time.sleep(3)
	prev=last


