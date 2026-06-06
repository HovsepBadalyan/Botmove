from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from parser import parse_move
from dotenv import load_dotenv
import os

load_dotenv()

bot = TeleBot(token=os.getenv('TOKEN'))




@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn_war = KeyboardButton('War')
    btn_crime = KeyboardButton('Crime')
    btn_drama = KeyboardButton('Drama')
    btn_thriller = KeyboardButton('Thriller')
    btn_psychologicalthriller = KeyboardButton('PsychologicalThriller')
    btn_actionepic = KeyboardButton('ActionEpic')
    btn_docudrama = KeyboardButton('Docudrama')
    btn_mystery = KeyboardButton('Mystery')
    btn_comedy = KeyboardButton('Comedy')
    markup.add(btn_war, btn_crime, btn_drama, btn_thriller, btn_psychologicalthriller, btn_actionepic, btn_docudrama, btn_mystery, btn_comedy)

    bot.send_photo(message.chat.id, open('telebot.png', 'rb'))
    bot.send_message(
        message.chat.id,
        'Welcome, please select the movie genre',
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text in ['War', 'Crime', 'Drama', 'Thriller', 'PsychologicalThriller', 'ActionEpic', 'Docudrama', 'Mystery', 'Comedy'])
def currency_handler(message):
    move_list = parse_move()
    if message.text == 'War':
        bot.send_photo(
        message.chat.id,
        open('Ryan.jpg', 'rb')
    )
        bot.send_message(
            message.chat.id,
            f'Your choice {message.text}\n {move_list[1]}'
    )
    elif message.text == 'Thriller':
        bot.send_photo(
        message.chat.id,
        open('darkknight.jpg', 'rb')
    )   
        bot.send_message(
            message.chat.id,
            f'Your choice {message.text}\n {move_list[3]}'
    )

    elif message.text == 'Drama':
        bot.send_photo(
        message.chat.id,
        open('Shawshank.jpg', 'rb')
    )

        bot.send_message(
        message.chat.id,
        f'Your choice {message.text}\n  {move_list[0]}'
    )
    elif message.text == 'Mystery':
        bot.send_photo(
            message.chat.id,
            open('RearWindow.jpg', 'rb')

        )
        bot.send_message(
            message.chat.id,
            f' Your choice {message.text}\n {move_list[7]}'
        )
    elif message.text == 'Comedy':
        bot.send_photo(
            message.chat.id,
            open('3idiots.jpg', 'rb')
        )
        bot.send_message(
            message.chat.id,
            f'Your choice {message.text}\n {move_list[8]}'
        )
    elif message.text == 'Docudrama':
        bot.send_photo(
            message.chat.id,
            open('Intouchables.jpg', 'rb')
        )
        bot.send_message(
            message.chat.id,
            f'Your choice {message.text}\n {move_list[6]}'
        )   
    elif message.text == 'PsychologicalThriller':
        bot.send_photo(
        message.chat.id,
        open('FightClub.jpg', 'rb')        
    )
        bot.send_message(
        message.chat.id,
        f'Your choice {message.text}\n {move_list[4]}'
    )
    elif message.text == 'ActionEpic':
        bot.send_photo(
        message.chat.id,
        open('Gladiator.jpg', 'rb')

    )    
        bot.send_message(
        message.chat.id,    
        f'Your choice {message.text}\n {move_list[5]}'
    )
    else:
        bot.send_photo(
            message.chat.id,
            open('Gotfather.jpg', 'rb')
        )
        bot.send_message(
            message.chat.id,
            f'Your choice {message.text}\n {move_list[2]}'
        )


bot.polling()