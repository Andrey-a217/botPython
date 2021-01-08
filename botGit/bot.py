url = ''
TOKEN = ''
apiKey = ''
api_weather = ''
import telebot
import requests
import random




keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Привет', 'Пока', 'Как дела ?')
keyboard.row('еще')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Хорошо', 'Плохо', 'Нормально')
keyboard1.row('Назад')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Погода')
# keyboard2.row('Время')
# keyboard2.row('Курсы валют')
keyboard2.row('Игры')
keyboard2.row('Назад')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Рандомное число')
keyboard3.row('Назад')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('Россия')
keyboard4.row('Подсказка')
keyboard4.row('Назад')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row('/weather Абакан')
keyboard5.row('/weather Саратов')
keyboard5.row('/weather Москва')
keyboard5.row('/weather Екатеринбург')
keyboard5.row('/weather Обоянь')
keyboard5.row('/weather Чайковский')
keyboard5.row('/weather Ялта')
keyboard5.row('/weather Фатеж')
keyboard5.row('/weather Хасавюрт')
keyboard5.row('Подсказка')
keyboard5.row('Назад')


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['help'])
def wecome(message):
	bot.send_message(message.chat.id, '/start запуск бота\n/help команды бота\n/weather <имя города>')


@bot.message_handler(commands=['weather'])
def test(message):
	city_name = message.text[9:]
	
	try:
		params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
		result = requests.get(url, params=params)
		weather = result.json()


		if weather["main"]['temp'] < 10:
			status = "Сейчас холодно!"
		elif weather["main"]['temp'] < 20:
			status = "Сейчас прохладно!"
		elif weather["main"]['temp'] > 38:
			status = "Сейчас жарко!"
		else:
			status = "Сейчас отличная температура!"

		bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + "\n" + 
				"Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" + 
				"Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" + 
				"Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" + 
				"Давление " + str(float(weather['main']['pressure'])) + "\n" + 
				"Влажность " + str(int(weather['main']['humidity'])) + "%" + "\n" + 
				"Видимость " + str(weather['visibility']) + "\n" + 
				"Описание " + str(weather['weather'][0]["description"]) + "\n\n" + status)

	except:
		bot.send_message(message.chat.id, "Город " + city_name + " не найден")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/Users/Andrey Kharitonov/Desktop/all/Все/все/проекты/Python/боты/bot/bot-exo/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,  "Добро пожаловать , {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.  Этот бот находитьс в разроботке, пожайлуста используйте только те варианты которые предложены ниже.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def weome(message):
    id = message.chat.id
    msg = message.text
    msg1 = message.text
    msg2 = message.text
    msg3 = message.text
    msg4 = message.text
    msg5 = message.text
    msg6 = message.text
    msg7 = message.text
    if msg == 'Как дела ?':
        bot.send_message(id, 'Я бот <b>{1.first_name}</b>, какие у меня дела, а у тебя ?'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = keyboard1)
    if msg6 == 'еще':
        bot.send_message(id, 'Ок', reply_markup=keyboard2)
    if msg2 == 'Хорошо':
        bot.send_message(id, 'Это замечательно🤪', reply_markup=keyboard)
    if msg3 == 'Плохо':
        bot.send_message(id, 'Небеспокойся все наладиться!😊', reply_markup=keyboard)
    if msg4 == 'Нормально':
        bot.send_message(id, 'Завтра день будет лучше!😉', reply_markup=keyboard)
    if msg5 == 'Назад':
        bot.send_message(id, 'OK', reply_markup=keyboard)
    if msg7 == 'Игры':
        bot.send_message(id, 'Игры', reply_markup=keyboard3)  
    if msg7 == 'Погода':
        bot.send_message(id, 'Погода', reply_markup=keyboard4) 
    if msg7 == 'Россия':
        bot.send_message(id, 'Россия', reply_markup=keyboard5) 
    if msg7 == '/weather Саратов':
        bot.send_message(id, 'Саратов') 
    if msg7 == 'Подсказка':
        bot.send_message(id, 'Если вы не нашли свой город, то просто напишите "/weather" и название своего города')
    if msg7 == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
    if msg1 == 'Пока':
        bot.send_message(id, 'Досвидание')
    if msg1 == 'Привет':
        bot.send_message(id, 'Приветствую')










#else:
#       bot.send_message(id, 'Я тебя не понял')

#run
bot.polling(none_stop = True)