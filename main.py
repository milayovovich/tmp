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
    bot.send_message(message.chat.id, u'''��� ����� ���� ???????� ����� ���� �������� �� ������ ��������: ��������� ������ �������� �����-�� ������ �� ������� ����, � ��� ����� ������������� ������������� ������� (���������� ������������� = ����������� ���� �������) � ��������� ������ ��������� ��� ���� ��������� ������ ������, ����� ������� ������ ��� ������� (�� ����� ������� , ��� ����� ������ �������� ����, �� ���� �� ����� ������ ����� ����� ����� ������ ������ �� ������), ����� ����� � ������  �������� �� ��������, ����� ��� ���������� ������������ �����, ������ ��� ��� ����� ������ ��� ����� ������� (����� �� - "���������� ������������� = ����������� ���� ������� "), ����� ���� ��������� ��� � �������� ��������� - ��� ������ �������� � ������� �������� �������� � ���� �����, ����� �������� ������, �� ���� ��������� ��������� ����� ������ � ����������. ��� ���������� ������� ������������ ������ ���� ����� ���������� �����, � ������ �� ������ ��������� ����� ������� ���� ����. ������ �� ��������� �� ��������, ������ ���������� �����������������, ��� ������������� �������� ������ ��������� ��������� �������� � �������� ������������� �����, �� ���� ������ ������. ��������� ���� ���� ����� - "����": ������, �� ������ ������, ��� ������� ���� �������� � �������������� �������� ������ ������� ������, ���� ������ ������ �������� ��� ���� ��� (����� ������ �� �������� ����� � �������� - ������ ������ ����� �������������� ����� ��� ������ �� ���������). �������, ��� ����� ������� ����� ������ �������� ��, ��� ���������� ������ ���� - ��������� ������. ��� ������ ��������� � �� ������, ��� ������ ����� ��� ��� �������� �������� � �����. ??????''')


@bot.message_handler(commands=['why_we'])
def handle_info(message):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bot.send_message(message.chat.id,'''� ��� ���� �������? ??????  \n �� ���������� ������������ ����������, � ������, ���������� �������� ������ �� ����� �� ������ �����. ����� �������, ������ �����, ������� ����� ������ � ������ ���������� ������ ������ ������, ������� ����� ���������, �� ������ ���� � �������������� � ����������� ������ ��������� �� ��������.�������� ����� ��������, ������� ���������� � ����������� �������, ���������� �� 5 ���� �� ���������� ���������� �� ������ �����. � ������ ���� ������ ���������� ����� ������ 50 $ � ������ ��������� ���� ����� �������������� �� 10 $, �������������� � ����� ��������� �������������, ������ ���������� ����� ����� �������� ����� �� 10 $.����� ������ �������� �������� �������� ����� ������������� ������� �����, � ������ ����������� ����� �������� ����� ������ � ������������ ��������� ���. ����� ������� ������ ��������� ���������� �������� � ����������� ������ ���� ����� ���������� ���������, � ��� �������� ����� �������� �����.\n\n Bitcoin price: %s '''% str(r.json()['bpi']['USD']['rate']))

@bot.message_handler(commands=['bad_pump'])
def handle_info(message):
    bot.send_message(message.chat.id, '''������ ������ �� ��� ����� �������? ???????? �� ������ ������ ����� �������� ������� ���������������, ��� ��� ��� �������� ���������� ��� �������� ����������������� ������� ����� ���������� �����, � ���������� ��������, �������� ������� ����� ������ ���������� �������� ������ ����� ���������������.����� ��������� ������� ��������������� ������, ��� �������� ����� ���������������� �������� �������������� ����, � ���������� ����, �� �������� ��������� ����������. ������ ��������� ���������� � ����� ����� � ������ ���� ����������� ������, ��� ���� ������������� ��������������, ��� ���� �����, � ���, � ���� �������, ������ ����������� ������� ����.''')




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
                keybord.add(types.InlineKeyboardButton(text=u'������ ������������ ���������� � �����', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''��������� ���� �� ���� ����� ��������� %s � 21:00 �� ���'''%zero_day, reply_markup=keybord)
            if market_id == '2':
                zero_day = date(2018, 5, 18)
                market = MarketPlace('YOBIT', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'������ ������������ ���������� � �����', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''��������� ���� �� ���� ����� ��������� %s � 21:00 �� ���'''%zero_day, reply_markup=keybord)
            if market_id == '3':
                zero_day = date(2018, 5,19)
                market = MarketPlace('C-CEX', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'������ ������������ ���������� � �����', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''��������� ���� �� ���� ����� ��������� %s � 21:00 �� ���'''%zero_day, reply_markup=keybord)
            if market_id == '4':
                zero_day = date(2018, 5, 17)
                market = MarketPlace('MERCATOX', zero_day)
                markets[call.message.chat.id] = market
                keybord = types.InlineKeyboardMarkup()
                keybord.add(types.InlineKeyboardButton(text=u'������ ������������ ���������� � �����', callback_data='buy_info'))
                bot.send_message(call.message.chat.id, u'''��������� ���� �� ���� ����� ��������� %s � 21:00 �� ���'''%zero_day, reply_markup=keybord)

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
            keybord.add(types. InlineKeyboardButton(text=u'�������', callback_data='paied'))
            bot.send_message(call.message.chat.id, market.name)
            bot.send_message(call.message.chat.id, u'''����� �������� ����������, ��� ���������� ��������� %s �������� (BTC: %s) �� ��� ������� �������. ������� �� �������������� ��� ���������� � �� �������� �� �����������.\nETH: 0x42eaA5f407e95c94A54ec3d3b0cb9ff0b3DC9048\nBTC: 12TUgauBowDsAzgZu3fmBYcNxj5RFzYBKE'''%(old_price,price), reply_markup=keybord)
        if call.data == 'paied':

            keybord = types.InlineKeyboardMarkup()
            keybord.add(types.InlineKeyboardButton(text=u'������ ����� ��������� ���� ��������?', callback_data='trans_id?'))
            bot.send_message(call.message.chat.id, u'''��������� ��������� ���� ��������, ����� �� ���������, ��� �� �������� ���� ������.''', reply_markup=keybord)

        if call.data == 'paied':

            keybord = types.InlineKeyboardMarkup()
            keybord.add(types.InlineKeyboardButton(text=u'������ ����� ��������� ���� ��������?', callback_data='trans_id?'))
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
        bot.send_message(message.chat.id, u'''�������� �����:''', reply_markup=keybord)
    except:
        pass

@bot.message_handler(content_types=['text'])
def handle_text(message):
    transaction_ids[message.chat.id] = message.text
    # print(transaction_ids)
while True:
    bot.polling(none_stop=True)
