# http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=821
import random
import requests
import json

lotto = random.sample(range(1,46), 6)


url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo="
drwNo = "821"
res = requests.get(url + drwNo)

dictLotto = json.loads(res.text)
# res.text 안에는 로또번호 정보가 들어가 있다
winner = []

for number in range(1,7):
    winner.append(dictLotto["drwtNo" + str(number)])

# count = 0

# for i in winner:
#     for j in lotto:
#         if(i == j):
#             count += 1

# count2 = len([i for i in winner for j in lotto if(i==j)])
# print(count2)

# set 사용하기
for i in range(1000):
    lotto = random.sample(range(1,46), 6)
    print(len(set(winner) & set(lotto)))