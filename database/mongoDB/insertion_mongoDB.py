from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.10.240:27017/") # 네트워크 주소 입력
database = mongoClient["AI_LKJ"] # database명
collection = database['youtube_scaping_playlist'] # collection명
# ------------------------------------------------------------

# browser에 대한 정의

# 데이터 크롤링 시 예시

title = browser.find_element(by=By.CSS_SELECTOR, value="#title > h1")
date = browser.find_element(by=By.CSS_SELECTOR, value="#info > span:nth-child(3)")
views = browser.find_element(by=By.CSS_SELECTOR, value="#info > span:nth-child(1)")
recommend = browser.find_element(by=By.CSS_SELECTOR, value="toggle-button-view-model > button-view-model > button > div.yt-spec-button-shape-next__button-text-content")
contents = browser.find_element(by=By.CSS_SELECTOR, value="#description-inline-expander > yt-attributed-string")

# ------------------------------------------------------------

# db에 insert하기

list_reply = browser.find_elements(by=By.CSS_SELECTOR, value="#content-text > span")
for reply in list_reply:
    collection.insert_one({
        "title": title.text,
        "date": date.text,
        "views": views.text,
        "recommend": recommend.text,
        "contents": contents.text,
        "reply" : reply.text
        })