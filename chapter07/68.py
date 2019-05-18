#%% [markdown]
# ## 68. ソート
# "dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
# ## メモ
# * 投票数は`rating.count`
# * `> db.artist.find({"tags.value": "dance"}).sort({"rating.count":-1}).limit(10)

#%%
from pymongo import MongoClient, DESCENDING
client = MongoClient('localhost', 27017)
db = client.nlp100

res = db.artist.find({'tags.value': 'dance'}).sort('rating.count', DESCENDING).limit(10)

[(artist['name'], artist['rating']) for artist in res]
