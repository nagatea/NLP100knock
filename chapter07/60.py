#%% [markdown]
# # 第7章: データベース
# artist.json.gzは，オープンな音楽データベースMusicBrainzの中で，アーティストに関するものをJSON形式に変換し，gzip形式で圧縮したファイルである．このファイルには，1アーティストに関する情報が1行にJSON形式で格納されている．JSON形式の概要は以下の通りである．
#
# |フィールド|型|内容|例|
# |---|---|---|---|
# |id|ユニーク識別子|整数|20660|
# |gid|グローバル識別子|文字列|"ecf9f3a3-35e9-4c58-acaa-e707fba45060"|
# |name|アーティスト名|文字列|"Oasis"|
# |sort_name|アーティスト名（辞書順整列用）|文字列|"Oasis"|
# |area|活動場所|文字列|"United Kingdom"|
# |aliases|別名|辞書オブジェクトのリスト||
# |aliases[].name|別名|文字列|"オアシス"|
# |aliases[].sort_name|別名（整列用）|文字列|"オアシス"|
# |begin|活動開始日|辞書||
# |begin.year|活動開始年|整数|1991|
# |begin.month|活動開始月|整数||
# |begin.date|活動開始日|整数||
# |end|活動終了日|辞書||
# |end.year|活動終了年|整数|2009|
# |end.month|活動終了月|整数|8|
# |end.date|活動終了日|整数|28|
# |tags|タグ|辞書オブジェクトのリスト||
# |tags[].count|タグ付けされた回数|整数|1|
# |tags[].value|タグ内容|文字列|"rock"|
# |rating|レーティング|辞書オブジェクト||
# |rating.count|レーティングの投票数|整数|13|
# |rating.value|レーティングの値（平均値）|整数|86|
#%% [markdown]
# ## 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
#
# ### 手順
# * KVSとして`Redis`を使います
# * `$ brew install redis`
# * `$ brew services start redis`
# * `$ redis-cli`で起動されているかどうかとポート番号がわかる
# * pythonのライブラリは`redis-py`を使う
# * `$ pip install redis`
# * `name => area`のデータベースを構築する
# * nameが重複しているデータが複数ある？
#   * nameは一意だと思っていたが、同じアーティスト名で活動してる別なアーティストがいるらしい
#     * 例: Queen
#   * idでプレフィックスをつけることにした

#%%
import gzip
import json
import redis
r = redis.Redis(host='localhost', port=6379, db=0)

with gzip.open("artist.json.gz", "rt") as f:
  for line in f:
    json_dict = json.loads(line)
    if 'name' in json_dict:
      r.set(f"{json_dict['name']}:{json_dict.get('id', 0)}", json_dict.get('area', ''))
