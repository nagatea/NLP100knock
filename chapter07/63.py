#%% [markdown]
# ## 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．


#%%
import gzip
import json
import redis
r = redis.Redis(host='localhost', port=6379, db=1)

with gzip.open("artist.json.gz", "rt") as f:
  for (i, data) in enumerate(f):
    json_dict = json.loads(data)
    if i % 100000 == 0:
      print(i)
    if 'name' in json_dict:
      tags = json_dict.get('tags', [{'count': 0, 'value': ''}])
      count = 0
      for tag in tags:
        count += tag['count']
      value = {
        'tags': str([val['value'] for val in tags]),
        'tagsCount': count
      }
      r.hmset(f"{json_dict['name']}:{json_dict.get('id', 0)}", value)

#%%
def get_tags(name):
  r = redis.Redis(host='localhost', port=6379, db=1)
  keys = r.keys(f'{name}:*')
  res = []
  for key in keys:
    tags = r.hmget(key, 'tags', 'tagsCount')
    if int(tags[1]) == 0:
      continue
    res.append({'tags': tags[0], 'count': int(tags[1])})
  return res

get_tags('Queen')
