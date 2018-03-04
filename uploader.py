from __future__ import unicode_literals
import telebot
import os
import fnmatch

token = 'token' 
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, text='Hey!')

@bot.message_handler(commands=['upload'])
def handle_start_help(message):
    music_folder = 'D:\\Music\\'
    pattern = '*.mp3'
    print('start upload')

    def Name_subfolder(A):
        Name = os.listdir(music_folder)[A]
        return Name

    lis = []
    count = 0

    try:
        while count == count:
            for folder, subdirs, files in os.walk(music_folder + Name_subfolder(Ch)):
                for filename in fnmatch.filter(files, pattern):
                    fullname = os.path.join(folder, filename)
                    lis.append(fullname)
            count += 1
    except:
        print('end list appends')

    try:
        a = 0
        while a <= len(lis):
            print(a)
            x = (lis[a].replace('\\', '\\'))
            print(x)
            bot.send_audio(message.chat.id, audio=open(x, 'rb'), timeout=10)
            a += 1
    except:
        print('ooops')

bot.polling(none_stop=True)
