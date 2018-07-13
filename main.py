import requests
from config import token

url = 'https://api.telegram.org/bot'
bot_msg = 'Привет! Я суперпупер бот, который покажет тебе стоимоть бетховенов и эфира в деревянных =)\nСписок команд:\n - /btc - цена за бетховен\n - /eth - цена за эфир'


def get_bot_updates(limit, offset):
    method_url = url + token + '/getUpdates'
    par = {'limit': limit, 'offset': offset}
    result = requests.get(method_url, params=par)
    # форматируем json в словарь
    decoded = result.json()
    return decoded['result']


def sendMessageBot(text, chat_id):
    method_url = url + token + '/sendMessage'
    par = {'chat_id': chat_id, 'text': text}
    requests.post(method_url, params=par)


def get_coin_rub(coin_rub):
    param = coin_rub + '-rub'
    method_url = 'https://api.cryptonator.com/api/ticker/'+param
    result = requests.get(method_url)
    decoded = result.json()
    result = decoded['ticker']
    return result['price']

def bot_return(offset):
    result = get_bot_updates(5, offset)
    chat_id = item['message']['chat']['id']
    text = item['message']['text']
    if text == '/start':
        text = bot_msg
        sendMessageBot(text, chat_id)
    elif text == '/btc':
        coin = get_coin_rub('btc')
        text = 'бетховены опять упали, стоят ' + coin + ' руб.'
        sendMessageBot(text, chat_id)
    elif text == '/eth':
        coin = get_coin_rub('eth')
        text = 'эфир сегодня ' + coin + ' руб.'
        sendMessageBot(text, chat_id)

while True:
    try:
        result = get_bot_updates(100, 0)
        for item in result:
            update_id = item['update_id']
            new_offset = update_id + 1
            bot_return(new_offset)
    except KeyboardInterrupt:  # порождается, если бота остановил пользователь
        print('Interrupted by the user')
        break