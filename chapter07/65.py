#%% [markdown]
# ## 65. MongoDBの検索
# MongoDBのインタラクティブシェルを用いて，`"Queen"`というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
# ## 操作
# * `$ mongo`
# * `> use nlp100`
# * `> db.artist.find({"name": "Queen"})`

#%%
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.nlp100

find = db.artist.find({'name': 'Queen'})
[f for f in find]
