#%% [markdown]
# ## 64. MongoDBの構築
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
# ### メモ
# * `$ brew install mongodb`
# * `$ brew services start mongodb`
# * connecting to: mongodb://127.0.0.1:27017
# * `pymongo`を使います
# * `$ pip install pymongo`

#%%
import gzip
import json
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.nlp100
col = db.artist

# 存在した場合、初期化
col.drop()

with gzip.open("artist.json.gz", "rt") as f:
  batch = []
  for (i, data) in enumerate(f):
    # パフォーマンスを考えて、10000件ごとに格納していく
    json_dict = json.loads(data)
    batch.append(json_dict)
    if i % 10000 == 0:
      col.insert_many(batch)
      print(i)
      batch = []
    
  if len(batch) > 0:
    col.insert_many(batch)
    print(i)


#%%
from pymongo import IndexModel, ASCENDING
col.create_indexes([
  IndexModel([('name', ASCENDING)]),
  IndexModel([('aliases.name', ASCENDING)]),
  IndexModel([('tags.value', ASCENDING)]),
  IndexModel([('rating.value', ASCENDING)])
])

#%%
col.find_one()

