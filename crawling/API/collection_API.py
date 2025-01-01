# 공공데이터 포털 주소 : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043232

import requests
import pandas as pd
import json

# 페이지 초기화
page = 0 
# 데이터프레임 초기화
df_main = pd.DataFrame()

while True :  
  page = page+1

    # 요청주소
  url = 'http://apis.data.go.kr/1160100/service/GetFnCoBasiInfoService/getFnCoOutl'

  # 요청변수 (Request Parameter)
  params ={
            'serviceKey' : '서비스키', # 서비스키 입력 : 임의로 텍스트 부여 
            'pageNo' : f'{page}', 
            'numOfRows' : '10', 
            'resultType' : 'JSON'
          }

  response = requests.get(url, params=params)
  contents = json.loads(response.content)

  # items가 없는 경우 종료
  if "item" not in contents["response"]["body"]["items"] or not contents["response"]["body"]["items"]["item"]:
      break
  
  item = contents["response"]["body"]["items"]["item"]
  
  for x in range(len(item)):
      
      # 1. 금융회사명 - fncoNm
      name = contents["response"]["body"]["items"]["item"][x]["fncoNm"]
      # 2. 법인등록번호 - crno
      number = contents["response"]["body"]["items"]["item"][x]["crno"]
      # 3. 금융회사주소 - fncoAdr
      address = contents["response"]["body"]["items"]["item"][x]["fncoAdr"]
      # 4. 표준산업분류명 - sicNm
      category = contents["response"]["body"]["items"]["item"][x]["sicNm"]

      series_addition = {"name" : [name], "number" : [number], "address" : [address], "category" : [category]}
      df_addition = pd.DataFrame(series_addition)
      df_main = pd.concat([df_main, df_addition], ignore_index = True)
  print(f"{page} 페이지 끝")
print(df_main)