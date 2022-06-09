import telebot
from pytube import YouTube

bot = telebot.TeleBot('5459666217:AAHA-pPKRREIgkiK3n7hEiPBoGsCVve78X8')

@bot.message_handler(commands=['start'])
def start(message):

    sti = open('images/welcome.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, <b>{0.first_name}</b>!\nЧтобы узнать подробней про меня, напиши команду <b>/help</b>".format(message.from_user),parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "Скинь мне видео с источника(ютуб) и я тебя отправлю аудио файл данного видео!")


@bot.message_handler(content_types=['text'])
def after_text(message):
    youtube_video_url = message.text
    yt_obj = YouTube(youtube_video_url)
    filename = yt_obj.title + '.mp3'
    yt_obj.streams.get_audio_only().download(output_path='/download', filename=filename)
    filename = '/download/' + filename
    audio = open(filename, 'rb')
    bot.send_audio(message.chat.id, audio)

print('\/ Бот запущен');
bot.polling(none_stop=True, interval=0)
