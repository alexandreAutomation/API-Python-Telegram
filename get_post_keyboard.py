from json import loads, dumps
from requests import get, post
id_data = 0
id_data_equals = 1
url = 'https://api.telegram.org/' + 'bot1905456558:AAFBECwoGxPIbIchwdZO_iR1ObIFogclti8/'

while True:
    while True:
        try:
            datas = loads(get(url + 'getUpdates').text)
            break
        except Exception as e:
            print('perca de connection')
    id_data = datas['result'][len(datas['result']) - 1]['update_id']
    if len(datas['result']) > 0 and id_data != id_data_equals:
        id_data_equals = id_data
        data_message = datas['result'][len(datas['result']) - 1]
        data = {"chat_id": "1635442499", "text": "Olá Python falando", "reply_markup": {"keyboard": [[{"text": "Botão 1"}], [{"text": "Botão 2"}]]}}
        data = dumps(data)
        headers = {'Content-type': 'application/json'}
        a = post(url=url + 'sendMessage?chat_id=1635442499text=my', data=data, headers=headers)
        print(data_message)
        print(a.text)
