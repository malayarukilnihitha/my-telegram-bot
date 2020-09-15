!pip install adafruit-io

 x= "nihithamalayarukil"#ADAFRUIT_IO_USERNAME
 y= "aio_hsRR46e4Mw8iG0CHiuUzYkJVkkWl"#ADAFRUIT_IO_KEY
 
 from Adafruit_IO import Data
 
aio = Client(x,y)
feed=Feed(name='bot1')
result=aio.create_feed(feed)
result

from Adafruit_IO import Data
value=Data(value=0)
value_send=aio.create_data('bot',value)
!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests

def get_url():
    contents=requests.get('https://random.dog/woof.json').json()
    url=contents['url']
    return url

def dog(bot,update):
  url=get_url()
  chat_id=update.message.chat_id
  bot.send_photo(chat_id,photo=url)

u=Updater('1235520242:AAF6YyIZNOfj3jU7dkBOaUFM-udZYg3oRB4')
dp=u.dispatcher
dp.add_handler(CommandHandler('turnoffthelight',turnoffthelight))
dp.add_handler(CommandHandler('turnonthelight',turnonthelight))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(Message(Filters.text &(~Filters.command),input_message))
u.start_polling()
u.idle()
