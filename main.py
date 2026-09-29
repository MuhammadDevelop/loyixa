from telebot import TeleBot
bot  = TeleBot("8947847401:AAGknvhr53LmZsBW7XH8bBIob7l09widl2Y")
@bot.message_handler(commands=["start"])
def salom(arg):
    bot.send_message(arg.chat.id,"Assalomu alaykum bizning ishlamaydigan botga xush kelibsiz ") 
bot.infinity_polling()