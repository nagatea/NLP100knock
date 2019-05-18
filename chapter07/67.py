#%% [markdown]
# ## 67. 複数のドキュメントの取得
# 特定の（指定した）別名を持つアーティストを検索せよ．
# ## メモ
# 

#%%
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.nlp100

def get_artist_aliases(name):
  find = db.artist.find({'aliases.name': name})
  return list(find)

#%%
get_artist_aliases('Queen')
