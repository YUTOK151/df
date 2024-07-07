import telebot
import random
token = '6404933140:AAGOIeMNgvnkzGauCO0EOIlrreSmK9ePko0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'Давай сегодня не по-фраерски {message.from_user.first_name} {message.from_user.last_name} Что покупаешь?')

@bot.message_handler()
	
def joskayotvetka(message):
	num = random.randint(1, 2)
	if message.text.lower() == "крокодила" :
		bot.send_message(message.chat.id, 'Иди сам поймай. У меня своих дел по горло')
	if message.text.lower() == "кору" or message.text.lower() =="коры":
		if num == 1:
			bot.send_message(message.chat.id, "У меня у самого коры мало. Я зимой замёрзну")
		else:
			bot.send_message(message.chat.id, "Всё меня это достало. Коры нет! Я прикрываю свою лавочку")
	if message.text.lower() == "медведя":
		bot.send_message(message.chat.id, "Какого медведя! Что за фраерский базар")
@bot.message_handler(content_types=['photo'])
def otvetkanafoto(message):
	num = random.randint(1, 5)
	if num == 1:
		bot.reply_to(message, 'Это моё фото?!?!')
	if num == 2:
		bot.reply_to(message, 'Не по-пацански получилось фото')
	if num == 3:
		bot.reply_to(message, 'Это тот момент когда я деда пиздил?')
	if num == 4:
		bot.reply_to(message, 'Если фото о рыбалке, то я вам советую там не ловить. Там мои сети находятся')
	if num == 5:
		bot.reply_to(message, 'Ну в этот раз фото прикольное')

bot.infinity_polling()