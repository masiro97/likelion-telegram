# 79cb40478a89c4d476748424745775b7

import requests
import json

res = requests.get("http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=79cb40478a89c4d476748424745775b7&targetDt=20180827")
data = json.loads(res.text)
dailyList = data["boxOfficeResult"]["dailyBoxOfficeList"]

movies = {} # key값은 영화이름, value 값은 순위

for movie in dailyList:
    movies[movie["movieNm"]] = movie["rank"]
    
print(sorted(movies))