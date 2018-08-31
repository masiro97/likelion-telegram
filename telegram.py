# https://api.telegram.org/bot<token>/METHOD_NAME
# https://api.telegram.org/bot638727061:AAFgfVabTJyx4TEcwr5rgKR5VH4T48iX_yE/getMe
# 691976215

import requests
import json
import time

url = "https://api.telegram.org/bot"
token = "638727061:AAFgfVabTJyx4TEcwr5rgKR5VH4T48iX_yE"

response = requests.get(url + token + "/getMe")

id = "691976215"
text = "hihi"
# sendMessage를 하는 요청을 보내서
# 텔레그램 메시지를 보내기
# requests.get(url + token + "/sendMessage?chat_id=" + id + "&text=" + text)

def send(text):
    requests.get(url + token + "/sendMessage?chat_id={}&text={}".format(id,text))

while(True):
    send(text)
    # 5초간 쉬어라
    time.sleep(5)