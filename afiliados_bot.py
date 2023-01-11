import telebot
import requests

# Introduce el token especificado por Botfather
bot = telebot.TeleBot("TOKEN")

# Comando inicial "start"
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hola!👋 \nEste bot es una version de prueba.")

# Respuesta a mensaje plano sin comandos
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if "Hola" in message.text:
        bot.reply_to(message, "Hola! Soy un bot de prueba.")
    else :
        bot.reply_to(message, "❌ Prueba a saludarme(Un 'Hola' estaría bien).")
   
bot.infinity_polling()