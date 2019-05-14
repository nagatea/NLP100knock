#%% [markdown]
# ## 62. KVS内の反復処理
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
# ### メモ
# * valueを検索するコマンドは無い => KVS内の反復処理
# * `$ keys *`で全件取得してvalueが`Japan`かどうかを判別するしかない
# * めちゃくちゃ時間がかかる

#%%
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

i = 0
for key in r.keys():
  if r.get(key) == b'Japan':
    i += 1

i
