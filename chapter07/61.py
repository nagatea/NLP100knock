#%% [markdown]
# ## 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
# ### メモ
# * `$ redis-cli`
# * `$ get key`で対応したvalueが返ってくる
# * `$ keys word`でキーを高速に検索することができる
# * ~~`keys name:*`して出力されたkeyに対して`get key`する~~
# * `$ mget keys`でkeyを複数指定して一気に取ってこれるらしいのでこれを使う

#%%
import redis

def get_area(name):
  r = redis.Redis(host='localhost', port=6379, db=0)
  areas = r.mget(r.keys(f'{name}:*'))
  return [x for x in set(areas) if x]

#%%
get_area('The Silhouettes')

#%%
get_area('Al Street')

#%%
get_area('Queen')
