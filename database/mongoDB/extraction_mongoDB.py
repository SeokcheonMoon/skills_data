import pandas as pd
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.10.240:27017/") # 네트워크 주소
database = mongoClient["AI_LKJ"] # database
collection_9suk = database['kto9suk9suk_review'] # collection

# collection에서 data 추출
data_consume_9suk = collection_9suk.find()

# 데이터프레임으로 전환
df_consume_9suk = pd.DataFrame(data_consume_9suk)