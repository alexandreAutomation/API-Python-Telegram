from requests import request
from json import loads

api_mensage = request("GET", 'https://api.telegram.org/bot1968621328:AAHi8eWYj8oNB6O3ToENYTQPttbibGia3gs/getUpdates',
                      timeout = 5)
api_response = loads(api_mensage.text)
print(api_response)

teste = {'chat_id0'}
api_pload = request('POST', 'https://api.telegram.org/bot1968621328:AAHi8eWYj8oNB6O3ToENYTQPttbibGia3gs/sendMessage',
                data=teste)
api_pload = loads(api_pload.text)
print(api_pload)