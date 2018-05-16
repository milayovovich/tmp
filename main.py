# coding=utf8
import telebot as telebot
from telebot import types
import requests
from tmp import MarketPlace
import requests

TOKEN = '582777688:AAHXqzRxcMwabEIS5nUVtUNE2SVZADudHCM'
bot = telebot.TeleBot(TOKEN)

markets = {}
users = []
transaction_ids = {}

@bot.message_handler(commands=['pump'])
def handle_help(message):
    bot.send_message(message.chat.id, u'''Что такое памп 🚀🚀🚀?В целом памп работает по такому принципу: владельцы канала покупают какую-то монету по дешевой цене, и уже здесь увеличивается капитализация монетки (увеличение капитализации = возрастанию цены монетки) в последний момент объявляют для всей аудитории своего канала, будем пампить именно эту монетку (до этого момента , все знают только валютную пару, то есть за какие именно Коины можно будет купить монету на пампах), тогда народ с канала  начинает ее покупать, здесь уже начинается своеобразная гонка, потому что кто купит первый тот купит дешевле (опять же - "увеличение капитализации = возрастанию цены монетки "), затем надо натравить еще и стороной аудиторию - это обычно делается с помощью фейковых новостей в чате бирже, чтобы покупали монету, за счет сторонней аудитории члены канала и заработают. Уже вследствие покупок посторонними людьми цена будет продолжать расти, а каждый из членов комьюнити будет считать свои иксы. Деньги не возьмутся из ниоткуда, просто произойдет перераспределение, при благоприятных условиях деньги сторонней аудитории окажется в карманах организаторов пампа, то есть членов канала. Последний этап этой схемы - "дамп": каждый, из членов канала, кто поборол свою жадность и удовлетворился текущими иксами продает монету, этот момент каждый выбирает для себя сам (самых жадных их жадность может и погубить - монета начнет резко обесцениваться когда все начнут ее продавать). Понятно, что самый большой кусок пирога получают те, кто возглавили данный памп - владельцы канала. Чем больше аудитория в их канале, тем больше иксов эта вся оборудка приносит в итоге. 😈😈😈''')
@bot.message_handler(commands=['why_we'])
def handle_info(message):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bot.send_message(message.chat.id,'''В чем наше участие? 😈😈😈  \n Мы предлагаем инсайдерскую информацию, а именно, раскрываем название монеты за долго до начала пампа. Таким образом, группа людей, которые имеют доступ к данной информации смогут купить монету, которая будет пампиться, по лучшей цене и соответственно с минимальным риском проиграть на пампасах.Согласно нашим правилам, продажа информации о «секретной» монетке, начинается за 5 дней до публичного объявления на канале пампа. В первый день данная информация будет стоить 50 $ и каждый следующий день будет обесцениваться на 10 $, соответственно в канун всеобщего обнародования, данную информацию можно будет получить всего за 10 $.Целью такого движения является создание более естественного течения пампа, а именно обеспечение более плавного роста монеты и ненавязчивый новостной фон. Таким образом данная стратегия заставляет поверить в перспективы монеты даже самых осторожных трейдеров, а это основной залог удачного пампа.\n\n Bitcoin price: %s '''% str(r.json()['bpi']['USD']['rate']))

@bot.message_handler(commands=['bad_pump'])
def handle_info(message):
    bot.send_message(message.chat.id, '''Почему сейчас не все пампы удачные? 😓😭😰😨 На данный момент пампы получили широкое распространение, так как это отличный инструмент для быстрого перераспределения средств между трейдерами биржы, в результате которого, трейдеры которые имеют больше информации получают активы менее информированных.Через настоящее большое распространение Пампов, они довольно часто идентифицируются обычными пользователями бирж, в результате чего, не приносят желаемого результата. Резкое повышение активности в чатах биржы и резкий рост обсуждаемой монеты, все чаще расцениваются пользователями, как памп атака, а это, в свою очередь, делает невозможным удачный памп.''')


def get_update_markup(id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=u"������� ??", callback_data=id))
    return keyboard

@bot.callback_query_handler(func=lambda c: True)
def inline(call):
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if 'market_place' in call.data:
            list_call_data = call.data.split(':')
            market_id = list_call_data[1]
            # print(list_call_data[1])
            from datetime import date

            if market_id == '1':

                zero_day = date(2018, 5, 19)
                market = MarketPlace('CEX', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'Купить инсайдерскую информацию о пампе', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''Ближайший памп на этой бирже ожидается %s в 21:00 по МСК'''%zero_day, reply_markup=keybord)
            if market_id == '2':
                zero_day = date(2018, 5, 21)
                market = MarketPlace('YOBIT', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'Купить инсайдерскую информацию о пампе', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''Ближайший памп на этой бирже ожидается %s в 21:00 по МСК'''%zero_day, reply_markup=keybord)
            if market_id == '3':
                zero_day = date(2018, 5,19)
                market = MarketPlace('C-CEX', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'Купить инсайдерскую информацию о пампе', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''Ближайший памп на этой бирже ожидается %s в 21:00 по МСК'''%zero_day, reply_markup=keybord)
            if market_id == '4':
                zero_day = date(2018, 5, 20)
                market = MarketPlace('MERCATOX', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'Купить инсайдерскую информацию о пампе', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''Ближайший памп на этой бирже ожидается %s в 21:00 по МСК'''%zero_day, reply_markup=keybord)

        if call.data == 'buy_info':
            market = markets[call.message.chat.id]
            date = market.zero_day

            price = market.count_of_day() * 10

            bitcoin_price = r.json()['bpi']['USD']['rate'].split('.')[0].split(',')
            bitcoin_price = bitcoin_price[0] + bitcoin_price[1]
            # print(bitcoin_price)
            old_price = price
            price = price/float(bitcoin_price)
            # print(price)

            keybord = types.InlineKeyboardMarkup()
            keybord.add(types. InlineKeyboardButton(text=u'Оплатил', callback_data='paied'))
            bot.send_message(call.message.chat.id, market.name)
            bot.send_message(call.message.chat.id, u'''Чтобы получить информацию, вам необходимо заплатить %s долларов (BTC: %s) на наш биткойн кошелек. Просьба не распространять эту информацию и не пытаться ее перепродать.\nETH: 0x42eaA5f407e95c94A54ec3d3b0cb9ff0b3DC9048\nBTC: 12TUgauBowDsAzgZu3fmBYcNxj5RFzYBKE'''%(old_price,price), reply_markup=keybord)
        if call.data == 'paied':

            keybord = types.InlineKeyboardMarkup()
            keybord.add(types.InlineKeyboardButton(text=u'Откуда взять публичний ключ кошелька?', callback_data='trans_id?'))
            bot.send_message(call.message.chat.id, u'''Отправьте публичний ключ кошелька, чтобы мы убедились, что вы оплатили наши услуги.''', reply_markup=keybord)

        if call.data == 'paied':

            keybord = types.InlineKeyboardMarkup()
            keybord.add(types.InlineKeyboardButton(text=u'Откуда взять публичний ключ кошелька?', callback_data='trans_id?'))
            bot.send_message(call.message.chat.id, u'''https://spectrocoin.com/ru/faqs/bitcoins/%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BB%D1%8E%D1%87.html''')

    except:
        pass

@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        users.append(message.chat.id)
        keybord = types.InlineKeyboardMarkup()
        keybord.add(types.InlineKeyboardButton(text=u'CEX(https://c.io/)', callback_data='market_place:1'))
        keybord.add(types.InlineKeyboardButton(text=u'YOBIT(https://yobit.io/)', callback_data='market_place:2'))
        keybord.add(types.InlineKeyboardButton(text=u'C-CEX(https://c-cex.com/)', callback_data='market_place:3'))
        keybord.add(types.InlineKeyboardButton(text=u'MERCATOX(https://mercatox.com)', callback_data='market_place:4'))
        bot.send_message(message.chat.id, u'''Выберите биржу:''', reply_markup=keybord)
    except:
        pass

@bot.message_handler(content_types=['text'])
def handle_text(message):
    transaction_ids[message.chat.id] = message.text
    with open('pump_data') as f:
        f.write(transaction_ids[message.chat.id])
        f.write(message.text)
        f.write("_____________________-")
    f.closed
    # print(transaction_ids)
while True:
    bot.polling(none_stop=True)
