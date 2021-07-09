from aiogram import types
from misc import dp, bot
from .sqlit import cheak_traf,reg_user

reg_user(1,1)

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]

def obnovlenie():
    global name_channel_1,name_channel_2,name_channel_3
    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]


@dp.callback_query_handler(text_startswith='start_watch')  # Нажал кнопку Начать смотреть
async def start_watch(call: types.callback_query):
    name_channel = '123' #Канал для подписки

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТКРЫТЬ ДОСТУП✅', callback_data=f'check')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, f"""<b>⚠️ ДОСТУП ЗАКРЫТ</b>

 ⚙️Для просмотра фильмов необходимо подписаться на <b>ниже указанные каналы</b>

📍После этого жми кнопку <b>«ОТКРЫТЬ ДОСТУП</b>»

<b>Канал 1</b> - https://t.me/{name_channel_1}
<b>Канал 2</b> - https://t.me/{name_channel_2}"""
                                                     , parse_mode='html',reply_markup=markup,disable_web_page_preview=True)




@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):
    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')
    name_channel = call.data[5:]

    proverka1 = (await bot.get_chat_member(chat_id=f'@{name_channel_1}', user_id=call.message.chat.id)).status
    proverka2 = (await bot.get_chat_member(chat_id=f'@{name_channel_2}', user_id=call.message.chat.id)).status


    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ОТКРЫТЬ ДОСТУП✅', callback_data=f'check{name_channel}')
    markup.add(bat_a)

    if (proverka1 == 'member' and proverka2 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka1 == 'creator': #Человек прошел все 2 проверки
        markup_2 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='🥤ВСТУПИТЬ🥤',url=f'https://t.me/{name_channel_3}')  # Cсылка на приват канал # ВАЖНО!!!!!
        markup_2.add(bat_b)
        await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                         'Все фильмы загрузили на наш <b>основной канал 👇</b>',parse_mode='html', reply_markup=markup_2)



    else:
        await bot.send_message(call.message.chat.id, '❌Вы не подписались на каналы ниже\n\n'
                                                     'Проверьте подписку на все каналы. И затем жми кнопку <b>ОТКРЫТЬ ДОСТУП✅</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - https://t.me/{name_channel_1}\n'
                                                     f'<b>Канал 2</b> - https://t.me/{name_channel_2}', parse_mode='html',reply_markup=markup,disable_web_page_preview=True)