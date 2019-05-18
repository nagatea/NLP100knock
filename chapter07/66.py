#%% [markdown]
# ## 66. 検索件数の取得
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
# ## 操作
# * `$ mongo`
# * `> use nlp100`
# * `> db.artist.find({"area": "Japan"}).count()`
# * `> db.artist.find({"area": "Japan"}).length()`でもいけた
# * `> db.artist.find({"area": "Japan"}).size()`でもいけた

#%%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.nlp100

db.artist.count_documents({'area': 'Japan'})
