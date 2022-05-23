import requests
import random
import telebot
from bs4 import BeautifulSoup

URL = 'https://anekdoty.ru/last/goood/'
API_KEY = '5336732252:AAH_Nvjy1FLfOKDZ_LRzH1paElaHaHkZv4g'


def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdots = soup.find_all('div')
    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['stat'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! чтобы посмеяться введите любую цифру:')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'введите любую цифру:')


bot.polling()

